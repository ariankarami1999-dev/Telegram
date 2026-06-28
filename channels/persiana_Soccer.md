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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 334K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 02:25:41</div>
<hr>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPtCsuVASscOh3LZFRRmKiDi3h17xgf_Oc51QZAhMQxAic5XVYGr-OW8akLIhp5rnSH2Nt8aOvUidTFvRtMRhMxBgCl2ZddFbVLlzVA0IaK4SYUQUKpVdpDApf7XO1fFJIWav9IO0kklTWrk4Z5PSLxmayO9qfxYLwEByXGqEtUku_1Ij3T-nUfk1usrJzqyrRPimqo2T8fACJyibndHjZovGBF8jGhvp6sNX4mHrVMlag8g6xqPFIcJaeaF9ksE4Iz0DZ4iEPpv7lXxSUQP_TZVhSiDmYOr95RaiR-zmtxZ5jppwAG017qf02WADjxNxc57GLlzTPOhGCCWLTyjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJMEmWd_0MNmVoe0I-A9wd3HEoZOUe1iodZelPnleHaXrZ71dols9KLrGW7h3cgw2z8zZHaqhD1Z_l5KdskbuKb2jBYzbumXeg2WkfuyXQJ8ajahWI50rBUvJCcHrppGpbfq_suYlBkNYdmeKDq5gWuqo6TCjMTKtyU1SXqKtp0c-HWbFxS4fnHv_6mM1VcbTdUCxePAVz9TgxzUqIXfCyyyYaAkHbt9yC4C-0gNmzv_0fRnPrb7Xn4UIbWjVK_yo_jr4mKiueje7ZzbLdpMkfEX6tdlqYay1o48jR_ej-0XBgu5QEj09G2GcBbZNbpCfIEhqcKxpIdyWy5VjQtzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUP5WlqJxBfmVY4UAJ7YHYPH4d9fJTErYq0SyPTig79rCxsNI0YO5Scrd-N7niejkeeF0ZbIauTKQ-Izd181elrqko0awR4BIzaKjY3y_XQI1c2ofQQxs5_UIJzSn00d7AMuscAYspoSBwlUTNwmCuQ1q0Uale7us6zmH68FVAhhpMs4-jzXxbkBQSxjuh4aPmjIZXM5Sgc6VczzTKl-82mG1X94DhWMdzNdUnlL26e7uBePxEWaG9wV9PgotQgnek7s7DGcBKgcQ_OZx1UkOO0xx8IhFnTsOIqoiTv1LC9BvW1yW7n45cWl8yJbEobjCO9RZDmqTctf6D90PeWNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9isMOTg_n4wJOYPodo3om7IN8ST-3s9qP29ZrFXHuSk42Jyr15vjYgJE1iBl_m0Zwlz9uguEMLip0kUsIbH0fVYL-F1zGFgzpEnzJnqJ-QuDa5AbDoPuHyZ1idl343VLxDofs8V7WhDyZYOeJIe5waN3DdbYqv9AcAZROR4OOu7QHdeJTA5INIVhh86xC7mzkieSSfMI80_AQ-_n1HyLQT6PpzgEUOvwNK399j_8Tm6UosQUiEYGMc7soLJqqOm9ffpsXQV7FWCFD7i98HDztgvWOSP-78Ttw1Zx59Ptlo1ICumS7FX6Fnl9YtlWFVX5yktlUufrU5PSn3C61zklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24576">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEG6zZggDc29sM2XNx2CeblY4YYEjOEM7LTrdQGKzDCB6wxCog1CRdZJZuyVlBTEzb0fUObTPm0snYtps0MuYGtdk4xiwceWh4aJ_t_kXKu68CTzg_8AQ7N-pv7rtRH7mM9X141FjR_pMGR8aRbVByUHwVE-lOx3wkfYGYx_nAGmn1pAJnNAFFyIl91cIAiQrh60Q8o9LR0wpHNyIrco5KofZXt7IYdxDrpKwVThkoAs1KtGq9SGG330Yn9G73cSuEVAOVb0k-8Op-jzBwprJefvWE1g5PMaokKEUtMhlc4254Ru8h_MFOSm8Zv1T6sojmjII6Bs3lMQVtZGQr_Jrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت:
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/24576" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUZlpTkOujeCB1YS2cKceX9q7ngb4wG_pawhxf0UM-QAjhFd8xnepSejnbUOI3Ml1dnqo52oU_b_R_75JkOJcsaLycwG3Qw_BnJZePBAjvyh85-9RU3WwPmbzc45nByCclvUGNBrEnWEgAeBTlprwdqju-PjAjMqSVrXcaDIzCB4dG785x7WZXV3M59DFL0m5NPMTgrHIpYMCkOgaZOTf81jWCJ67wC1fCJi9xfhfHVIsyYIP5Up7EUm9TV_uitlZlz4KZY2FYoe8KqZEAGlvDJCVTY16TBigJ5uzNVALnwrM9UtkyKXtLmZp9B34jlbrktb7ewokFGZiHo9kOU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=HlMqw2apWoGTghO1SNmSf71X1b33VA2RBaPBBoprtrjW9tnvqEcsfx85EvXcZ2wQz_1FO7AUoXYNd4eshp8z2tNYgHpiqynfOXTT-C7KKRZ-VlVzJkyC7TKoCW1v2tQbOeWfpLQfgA_4skB8vu5WNs6Q8pXD4QNfKgNf8R_X5t0k70ysSrrEFZgi057EG3glx_OKAKERZBdLk6QKChC41HXyFKr-4SE2bVEaM8dQ62ARlvSmhCX1scfkpgSMNFebaKfHNaO8QQNby1mGyHUipOVlUaE4w9Oe2swp3WpJWS7uM11Vc4I8Tr_jFRGKo-r_gQlSsq-OWWLELIr_k19jAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=HlMqw2apWoGTghO1SNmSf71X1b33VA2RBaPBBoprtrjW9tnvqEcsfx85EvXcZ2wQz_1FO7AUoXYNd4eshp8z2tNYgHpiqynfOXTT-C7KKRZ-VlVzJkyC7TKoCW1v2tQbOeWfpLQfgA_4skB8vu5WNs6Q8pXD4QNfKgNf8R_X5t0k70ysSrrEFZgi057EG3glx_OKAKERZBdLk6QKChC41HXyFKr-4SE2bVEaM8dQ62ARlvSmhCX1scfkpgSMNFebaKfHNaO8QQNby1mGyHUipOVlUaE4w9Oe2swp3WpJWS7uM11Vc4I8Tr_jFRGKo-r_gQlSsq-OWWLELIr_k19jAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jCwhuKCkvOfZeqhyY7MM_hDZhhMV8_lF6SOifbUlfbFbQYpIr-2NyLP-PEJOYfSrMDt3pZMGzdpygm_cYcv2oi6qxUFz1HQ9xRRPBPRMYLGxvKqj-yfYHMEkyYWKeUhCfIjBaPo-s9hBlKGXzT7An7szQhC00Z2-XWw8t8K9Oai-Gc-p8tXr3ltM3qlKcW-b-Hk4Q-gsilCNduLAuLh1i-oWVMDO-MPVoumAu7skOvHoahLqf6loLLmgnwG1hXrhtSxfxYVrkaucGYQ5KuLh3BXqqyNnlhsWewXd9ELdRwA1VNtgVOYDn6opQ6IxQxZ3yqr5Q_V6T8NF8Lttjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq1YQWv29tw-U_AS_H6HCSbQHA1CblLyRVsO9FuhNmGihYQibSIX_D7UOE5w48dw81rC6M56ZTw-ax2bAJm9l6dbp-WroUXhwtTS11u2g66fYxfZQZiE8EOanxSJLy92smR28eQ_RYRQ87wWHzCIitZZ4mlNJvQcUDtL9Zfz6AqcgCz5lz92C5KNNFZpDnEkB_A0PimLO0uWRmi5RpWEyZ9uQn7oDlvnJoZZXObJGn7TXp0M6esk5ZYzE_LIn1rVk9ljdmDCfQN6KvihFovOvNakMslSnXGSJBm3WSxuDZPhgwae3MpQbxWvHs4fJADC_xZeu2Yn-XN0peR5yS9Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=raO-Up9VoQO25m7BYcRpocG-L7KSzOt0CTlafbXuiegtK6ntc5SpQ4VEeoFWRNfaIf1cxCD-FNoXTppsJ69SqtE7fYu4RfxBW4ECdBWGNb4BA9rcs5umGC9fKJR8fcnjbxSIOqM4Mzp3V4Hk9baHI3or09kgDYl1OKcMw_odmgQktiYgXh4JidiuwHuZ1AU-RCRSKvm7yDmo7XClt64TUUFz2oAjIMaWIRmKN2R1Vq2lATAObW-nUPCd7r8Mjz1QSXjxMKl2YNikCQ2E5gKBfbBRxVrJ6LUdFYPlefoG2mEWt6iSnwbNdAgobp3HrhgIJaIbxIWuU1ch64j2Dh8lkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=raO-Up9VoQO25m7BYcRpocG-L7KSzOt0CTlafbXuiegtK6ntc5SpQ4VEeoFWRNfaIf1cxCD-FNoXTppsJ69SqtE7fYu4RfxBW4ECdBWGNb4BA9rcs5umGC9fKJR8fcnjbxSIOqM4Mzp3V4Hk9baHI3or09kgDYl1OKcMw_odmgQktiYgXh4JidiuwHuZ1AU-RCRSKvm7yDmo7XClt64TUUFz2oAjIMaWIRmKN2R1Vq2lATAObW-nUPCd7r8Mjz1QSXjxMKl2YNikCQ2E5gKBfbBRxVrJ6LUdFYPlefoG2mEWt6iSnwbNdAgobp3HrhgIJaIbxIWuU1ch64j2Dh8lkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKux6YJMIc7GDnttJvAeQlf6IrFBLu3C3pHtJrXgTLWzBwaO-1BTG4SmJ7Bq1RHXm3p6f7idCrRWtAE2NsQMna6pl4v-7t_3o3fW6WKlpGecKVKNLr29inaZVus3uLAX0xU1Y673lvEl20gmgQ7opVrdjcHqX7IHoAxQv7Cev8jjO9Qke0kEFD3S0i05TNFIZW6JUn0PEupIam4G5Y8ea8ZMuEfRNdjBZbCFWcFpQ8ZB8Gp6jB0bg79fq51_oyASMnfPw467QcBeam3fgObUp6DP04BvukFTaAZ7h1w_COob6PD8C1x7rbrBi2Sm_4GZpndHXmdL-YetOzwubIsBmJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxKux6YJMIc7GDnttJvAeQlf6IrFBLu3C3pHtJrXgTLWzBwaO-1BTG4SmJ7Bq1RHXm3p6f7idCrRWtAE2NsQMna6pl4v-7t_3o3fW6WKlpGecKVKNLr29inaZVus3uLAX0xU1Y673lvEl20gmgQ7opVrdjcHqX7IHoAxQv7Cev8jjO9Qke0kEFD3S0i05TNFIZW6JUn0PEupIam4G5Y8ea8ZMuEfRNdjBZbCFWcFpQ8ZB8Gp6jB0bg79fq51_oyASMnfPw467QcBeam3fgObUp6DP04BvukFTaAZ7h1w_COob6PD8C1x7rbrBi2Sm_4GZpndHXmdL-YetOzwubIsBmJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6tCIl2IGgB-AM4JRDADFC-7H_fSZpdg2XRIdZhw2tCRl7oIGZWR3jcd76J7Q4p2Obi-j-FaKCZ7y3M8TY4kukwsklPQmJ16pTJPLkIpu1LycBQDi_MhWohohXVcFcgFPbUlpRJOYy6e6ZsWOVcMLn1rty-ftlEHVrigUchcuN4qUAabtNatB9aTsS1tvPst4TeDdjN3bsk0V6uNlX-cnlCupP8PunttUVnuh-gn2pBgUhjZFit-d4h_Gx3C7o6SacvY1ECEMNvS7QPnMxR84TrzuACeNY8M8vG4-zEKc814C245zMbcfLM6dCS9yII57u2ktEDXppqw0VGuHTUOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9cA1E7sn-nNCA9jf-hLytv5HD03V7PbdSlO2Uhz5y-Wlk6fkg491sdlpWncPeoQ5QgdXgbv6xTE_BOPj6Qe9469gc8b0HKxBGj4GMBsD08p362v6IwMmRUTWP0bo0MpSl_4UuTttcn8PKKeoM5ccHghX4T3LKyyLZMUIp3YDl7s6Bp0NS4i2U1VugZoWpjBa-ueopZIlviWjf_m48ubPUQPNRB1SyUvPt5xwTzS5JU5EEDRopVd5wv-HSLCjORNQLnf25N_1l2GAMs9LHZIrFwi_XdBDAHnU3_vh4uLhez6IE3xdiUbnjXj-SLLf_-KBwqRYxns-9NqzCLpHrcSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7ZopXmkbb23LkNoUlZHHH3Ii2CIFQKd0vO5wyZcEEnNGAtASVSQs4Zzl-aW8BEi-yPap6f1UU7BQSmBq7aCWetDzGiRq1rXuJSOMvcsRYdUIaj6ukqs-s8LyjtBA1Ba9kgP1hDEHJaKpwAYmd9bMyWjRTVFioPz1_g8qQgD4eF3NKvd-6fS_Aq_fE04BPZIlhcnaHtQixsIgkjWNaePedYkP7Uq2jbLONKQc3p0ACKTfmdbRXEN8o4jVjrY7d9OZ8ryOIRk9q-4lGpSiF4-LXQKcia-Xjnfp25aQ3dDi0PiiiNdG625C3LN3kgZPhwKh4AlKYptTpCevalmoWC9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=hURGrJn4VcBOId_KibUtjCBnGSO84BiFGGexWzQ7ewXjli2y9x4z6idzx54I55uzmLtg5j-ZBXXCHVvubErNemnBQe22D5cDR7fJJJOTxatBedZXTXMv8P48qOdHLTJPIqxovIdVjWNigbLNKlKFByIVJhT-c4c-n-96gQPnt8TeC6KXko2u5-g8cBWaVvCRZ6cSabU2qAt-W3fJARGfsKrRcmEGH7tvDHahB8MwmtOF6dHRVUC5xAisR0feopYRmmFIMBzp-LTzOWYaPsDGwdJw7PIyRP1bG7-Vu2t68AE5a3REqQ1Ys2WLYNmFBCROkvwAvZuRjXRgkeH2LO7Vxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=hURGrJn4VcBOId_KibUtjCBnGSO84BiFGGexWzQ7ewXjli2y9x4z6idzx54I55uzmLtg5j-ZBXXCHVvubErNemnBQe22D5cDR7fJJJOTxatBedZXTXMv8P48qOdHLTJPIqxovIdVjWNigbLNKlKFByIVJhT-c4c-n-96gQPnt8TeC6KXko2u5-g8cBWaVvCRZ6cSabU2qAt-W3fJARGfsKrRcmEGH7tvDHahB8MwmtOF6dHRVUC5xAisR0feopYRmmFIMBzp-LTzOWYaPsDGwdJw7PIyRP1bG7-Vu2t68AE5a3REqQ1Ys2WLYNmFBCROkvwAvZuRjXRgkeH2LO7Vxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks5Le3iGMEKgPLBOQ4_hxC4JiUancAHWvRQV-Lzahhhmoci4hnSdXx8Je70nplSXdRrfZ1EZGVuD6rhG-FXK1T1veDY5NtiIz3ZzHjTs5Y_BcsiorF_oNMvUT_7l-jXcafHuf9nL39fBVyU9dSBFUACWpy0rkaoNaU7sEgaL3EkBXV5R--AlKZhpGJQxWhD2t7anVHa320JS0sPsciJ_LE2mfYmyS1xmvC6raizHvUR5wPAGGEGUPyauWGFLsndMOxv_goCE2F3nwSUvu9dv1rRW2MWQA3Pd49TBCDKBCd7Kf47aDC8gUTefFk0gayEfYTrJe6o_DjR9iCzWmDu7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiX51diyPx0-kj4WJmIBBSNDiJXaYR-hvvY8hxeUoqdnln6K-teHhDjVZ2na7NZqxrMJJseR2VP0p6u9i-X1EC6BFTh1nebW4nQR7rzUij8gmZXMYGDiOX6KDix1dPDhh2lrymRca2JiSgPoP5vQssTx7LAqS82pLgzlAudjSIgD04HaeFYIR0uZFlUgx3JQP3h3UJcnpdYHpAmpALAW-m4rV8SVxl0m7d7W3q9-YMGVd6kgkRoGHpItTfdUYxU2BKCGXJKh9AWaX-RzLEllufIWUQUARgWGxyy5M6hj6XcAJjPthAsC0dvuxB2q2oDNQQ35Xk1UH_NMlj0-LqnDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsEKx_omK7QRzdzED3yCnfGcmUzxjgXLTbO_huRrzOjLEpfc4W2IajkGuAP2p8zGtwdYacsLv0rhVn5gtyu31v3wv5TxbyTe6vqSDC1iGrYL_xNaPPquV2z8yQB2AH_t36w-qTVRrxbzc-wrv6FWVDj8skPkif2RRVYnnpIYkjQ059EM4OJA0wYNuHLehY4n_SestmwftXDPqi_3E-TE0UuOc4Sp5vhlVk-uV507_CDO-t5ULk1-s_wpGL_6gkIKZKrjJjZ5l66L-9zUXcJDJoYH1Zh45XX2NAbryspABtY00DhgWP_Opjz25CioruSuh4DRPPwosdV4P80j5221w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52zAoaptBA2uZisKsrNOWGUqakKxq8ArBM8561dKC8MXJwhhuZHH1F4gLpJikvdR7T1J3nUTFLB1QB-iSbMR-e5O1kD4ZRaW-Iq6hfZvd8wubuNlclVyPBaJbEXgVsiE-cwn9rJ04YMZmjRQkwpQ7t3NYBdm0iOX4Kbx13YbastcG3_EmmnjGpDn5IrV4zm8c53KdT4K7KvNSOQJhsiBDz5CAYtEb6gVVpLXC1UF8tDGUfcOmq9inRk5nDQikr1nBDgIKnIkOFBF8PiLNoK5fXkeiAp5hxnaBbRAa9G9bN2-X3pe7KME4jC_Hvapkdu_yh7GKJR2AiV8e_K-EuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr3pfjmshehlFoNMm9ZeEzhq3j072TZwb4RzqyahGwimX6dz1DLrtOsmjM6bOC08NyoouIwaPqfn2lGd4og6qh2u_MyEt1ImBbA-9S2ooCaD8WYa9MFPwjU6ga2o3WCq8Ts0dt-gl9LzqWCFXV1STfnv8l9y9A2CKQb7i87g-Iinh0bJnlGcgoP2YDZs1UnlEs7HDUBo8j8i2_Zg6LKP7YgiArpeH12fsdmQPOfUwkxdfISfdX5EhrWr1YlFXwTmPZTlb0loIHIEsu_82HXJVOZMPiZk-CBKPLY3QAPydfkGu8qFjKErNNa1_KRjp8pA4bnEKKr6KMyYWWJgNy-iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qw4qp4dxEDFqU8Q5JOrcr1CiJOqzRIqTXSDljYLzf_bm_cppHyNSCa5VhaqLJehNL_Fnj4LZAgmCVWOH91EQ9C2kAsye0MFLco3nZcbZvs6IhjejmHjXsPcKYriGJpNqp1DdIhsYsP86tBUt3NE1fJnQQ7qrbAjtw1PzkYiIZufswSqawf4maKWKrbjom_qAcNKOgS6xLLls7apOUvuxfvrT41B79OawQlj8p7cFrxnPRBAOSTFXNkkbyn-YOElxvb7kwB4Y3xvSBP1n5ddJQwNtRGSXjoB5g6cuLP4fm3jPpxAfPFgY0ZyCON9tbRNGPPD1n-m0cwI7GF1-fbSApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بالنزبت هیجان بازیهای جام رو چندین برابر کن.
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوسهای روزانه مخصوص کاربران فعال لنزبت
🍀
🔣
0️⃣
3️⃣
کش بک هفتگی
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet8.online</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24547" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=tSzAXg-T8bxf-5QQnkJ99yc3W19aGahX2ohxiQtrUdpsbEzqWpm0mvvk2BC3tM3TDhOiUxkNrS5AIEFohdhQbB0MwoTz5xfWkI2DWrPVO4cGLH_pbHfSGn5zb5s7z3eg5NRJ4vat0BYRg494jkRpehVw_JxTZ1zj1nf5u8lLmJtuP1OGBi08OPXYfFR1cx2RIBh4QDrt-1IMiglNPuIB7cmr0Hb9qof-OL0RMd4RY9x4hEqPl2hV6Z54aBn_Mnk-9gcXwVquaIqe5pXhcQutFhJHM0VeDb-21jvsPImOe7Lo9AIX3a6WBgRsGIgzor3RE1YT_kcvP0uxnvxfyAPJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=tSzAXg-T8bxf-5QQnkJ99yc3W19aGahX2ohxiQtrUdpsbEzqWpm0mvvk2BC3tM3TDhOiUxkNrS5AIEFohdhQbB0MwoTz5xfWkI2DWrPVO4cGLH_pbHfSGn5zb5s7z3eg5NRJ4vat0BYRg494jkRpehVw_JxTZ1zj1nf5u8lLmJtuP1OGBi08OPXYfFR1cx2RIBh4QDrt-1IMiglNPuIB7cmr0Hb9qof-OL0RMd4RY9x4hEqPl2hV6Z54aBn_Mnk-9gcXwVquaIqe5pXhcQutFhJHM0VeDb-21jvsPImOe7Lo9AIX3a6WBgRsGIgzor3RE1YT_kcvP0uxnvxfyAPJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY-oJvfUP-RrMPr5vPZcZnat2eG-IXDw22NWuJ6LCZLwAZGuAB663Npw0BKnKnwEA3rNUp8rIvmXehW2AmncDAGuLaeeL5GkcglnYXKxsS4PWOEeGlJ6elYmVET1b9PR_ld4opaC2Bcf66xd6Dfb1LNJ62eaJyCUHBs4lWtsKFCsppPgSYVToE6flGXnBR2UU8nKtT9lfVXQ06b34rHgj2U_jPUSrDIScUsV02rPilRse8a1qZYUPxnTHkfWAXDILeseQB4jTQkmakCcH_ZuGeKDsgBx8ZIwl0Cxjq2rzLnLyTYTmnqMW35Mfja6D8mvVzlK8wZnPaSxbPwEWDi30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZPf56BPrf1-59603PpxyUyHKwS1TtYA25wh74iUvm2KUSqMN8yGxWe8kX9XHEktlt6qssdM1pQ0oaApPzPgG20LS3zgjjMVqMuwrOf4OFcUyQMKWvtgM6QHtaRA69co35Jjv4NHK0kJfns1Vwc3EhOU2_bB9GBuHMzilqFdflKLQ0UDdQG1CgAFr-9bbDaytNnGKXKKIpBFNLFteuFzEoCurpSzpIhwPq-Pfy_iWiMHbuIUofHLrqEJeMT-TZ7R0rlljtyo80QnVa7It1mZXxZgxK_ff0L_YTpwp5FQVMwKpoP4OQQE8R64zA7qYHY1AhZV6TY8FVIGlTsIlwhJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9nui4J2MXCAD-wPyIILDwlUAdfwwnmNehorMaBejHc5OMVlMhhHqPmHEBWtS2uVkc5hXGeEyvWBnJswWBzYTXOqxiRgj1CtHoWmtPqV6zjSj3zKH_QjrQE3TQG0emXVBlXS0b4QQihYs9aRs-lNs1i0QDQTz57ugWbGiTvd1y4upd-kilp5qz8CIgjzQLZwCZgbhREtNNp2Edz4f3kLE_FuY44NQzlWWjUNpDBjF69gc5RBDML1pRoFoP_jJzgVd5_MTVcCfESuRgKKvY7T7_7o7aTKacbelpmRf7rB2ckLrRs1QotdNZjr-PCt1vjwlhD4xT-I42uw-Q9mdhvNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXriB3_oDatSFPsnds_or5n6p7Ce7PazTJ2BLC7T1aNb8kQiiWuyBYtx6DHPqRtGVmYsBXiK7oPTSCUtR0Y8olWe6vdQst5BAaveOHX2K425YF7KSCraC8wYN00_jV8NTV-PdeQHbinDCRmk14C5VTvk4OIwbA2NiJT9qEPatfeDi1g4RBbnAYRIlO-f4Cj6rUtDUX49wCOT3kub6HfxBru6PcdOZGKy2K2heqX10VfqmSBCbg_OVmfYkfZe9bHmOvgUEjtfx6wA9ILCaUbXsZ8z1cY7yQX48x6rGo_lYg8f3JfW4mbfZ5fC0NaHbWpalFxokUNO4IGoa09SEROezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg1ut-ojf7_eYoAqyit8xCS4vP68JN97WfqtjBoZaejUvpnJNL04_fn_hoKQekApc2hMEoAZikBsoDke_mmrtDH_3vt7A7-DdP8WqdRRe6bmjVjGo3bPLj9b2ayy1SacTLzZQNpOBqiF0qGTXC0PC4WmqRUIB6on17RsJr9YoNc7ad_3saUlbWvp3FIvs3FwGxsyFNMQkSnvKpixo5DVAIJcobY4Xd-dt7KvuKZVSqpOup_aqVyYO86eTvKHQ8lL103npU23RHPwjaNZjtuLGpVGy8AxpfxC6wwQB65U-43P1m5KsngikPhusT05-1Q36V73Ho-t--Ed-XsbSq9Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkv8Jr9mvQSqtIO6vUSZoltkdjsDpF6Zy-oli7vV4LCEyYEacAvK4AfoZ7L47ECOin3uQhOSxi6LMbMYo3WU2hO5KZNDAuJSBAYJePXYj-u-d3Bjw4p4AKHhzlzoRiFicX-GexdyordzIDawETCLOwDHwucgJIXcs9gV6XWh-NuhCkGb4kfxFasSulg8_reCsoHy_jP7YvKXtcAjiw83TkpKC8daNrplLLcf7FJbPBGHCToBo1sOfkcSSijTHGZsfxyS-xXJbt_BszvHmsFhxO5tefZwYdhM_-ul9puGCihHdRW-qpXYHMbPD7hh7z_DEkI7lfF86Gaizja1iIw-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUwJkWcVcuBTWVuLoX14RpQtm9wpX6E2014CA1Mup6jeHDCD8vz3fi3H2kRaFPDMMyJSgC8ftR6JF8ZkCGEnRaO6zXL4vUejateWa-mT0GAGodecmNTf0hE-8CTEy3ujxYdmndBSNKFxZPPh5xZFXrcxPqTMOst5IV5mQ_vS8FDi7w6nCXYEw1GaRfdC6HH4MoHIANXKjeEq0jGSWHoM73hpO1yFrxrbW5PoYmJaK1q9Zbf0ignn-nH_J3aCNQqW48TUmVFe_KOhMfwHPJpr8Tu7BUr9CYtcmLbzX-K07qJGSaA2T8-jW-Wp11Va5gtgSGxdcqMvoGhZeKUgiJuF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdxRHvl4AuFTGi0lFdtiVuDCFaVbRPKqFCqfY1W5M-22LBqOm98-s_-UwFT_IOTfjAw4jM4X5B6NsYC5eWZRc_aBAm6lR-WwhKxECgwnluMiG0EP7XF9WKJUldbgCoJh7rIgJ5i_CbLz-AAPzJh59cEriatfNbxGRCOargkuABsilBRG1aaVKxcx-7mJb9Xrn7kNqr-TGP6HL0cFpEIC7L9MALv8svbhl1NmgttEmvV6j4OrqivsZYZK559QqcTmTbBAnWPoTXipTDZwKq1WmB4VXC2fBTfEBnsQmtb2edHK3b7DvRRW8F2m5NlgiV9826opW0fb_85m8BWc1JXRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=u9l6xjiNNQW5IcvOuhd1p03fFyppOz6aTYXcQl-Edzs6qdA-_kcysyqNAspsAtELDVlcGDNfBv8R1sA2OxJQdsyWqAycUPBmoHu_l1VaIK7A-tCy0jRhifZpRANv-_mAimMXGs3504U0-ELLXaauDCQVPYm21RAW4P2JH0lzYm3Enc2tW_C2q20m5HhDKudPOf2qMhgpAfqwt_K5ioVqLh4jSX_jcwa4tqCnSsv7-LuXhOrR1qUckyWIB3eNRpu7FaC3Y13JIfa5jPuBagqsm0qW7vNqH5SVXA6GVmH_WJYIHxJcDZXiFwQfHAuodJjxDlDTne-MCeg1QnDeo6eqrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=u9l6xjiNNQW5IcvOuhd1p03fFyppOz6aTYXcQl-Edzs6qdA-_kcysyqNAspsAtELDVlcGDNfBv8R1sA2OxJQdsyWqAycUPBmoHu_l1VaIK7A-tCy0jRhifZpRANv-_mAimMXGs3504U0-ELLXaauDCQVPYm21RAW4P2JH0lzYm3Enc2tW_C2q20m5HhDKudPOf2qMhgpAfqwt_K5ioVqLh4jSX_jcwa4tqCnSsv7-LuXhOrR1qUckyWIB3eNRpu7FaC3Y13JIfa5jPuBagqsm0qW7vNqH5SVXA6GVmH_WJYIHxJcDZXiFwQfHAuodJjxDlDTne-MCeg1QnDeo6eqrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKM_jU3BtH_qRPcIotYKSHCKbdo195ExFOaEVfSFiIy72-VzQOepkeCwY7cNXVuCjk-cLzy53S2Igqb9S6vP8E9fKG4jgqe340SC359C4wpxtX4pSXBxTjwaJmIbbN4I4l4o-a8eu_CRwBM6IRmtV8E_F7J6r3OkYxlXdsYCWlGMejPw7qYfHp1cIl0Na-ZM_METoGypNAwcQD1zK6psCJX6OffI3uOVFlSah-FliwrKwwEfAlv6KvpoI1mx1WXxZjupzVMRpWOi5hg44huynmmDQ6oi59I2LLeyT_XPEkpMIuzarRTbtxNkXGhKpjZk4ahEUsT2wX0Ze-BoptiGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlH1WS1MncAaHiLKdWC4JnFsaigi_k6GZ6xQTDVdSHEgAgddci8_1nuFXwZ2Le76nxfgeZ9Mb3xHLkxp4nyzUqiPErIqxN2r7d6wSSbu6m_4BXj3jch3zo0I5nboCAkyjT9CdEFlyxGA06WY36hnOTrJ9KNHTPzCxmr-fUl1MQzn6SNxDZDEueutwl9OJ6obksErDo_swsc48N-OK8xfpZgEGG3eUywtcUOJO1diwhsq1P7GhlYTJkqeJ04aBRlFilBBn6oo3SQKk7EnZObW3VJRu5Vl9yjvU2FEFDtIN3CafMUdy0leN-r4ctz26zZEIgVO3sxoZ5mlXxGj8JAoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxu-9fyd2RIiWold2QW5gdk4rlV0t7BihzqycWodwiiDm-EG3iQZmWfUKvViYvpC-VbrztQD5VDL9JloqF8hzazBzADNYEwgeyP4L8qNKKrX4qIzMlzQiujZseCt22yCexEUwzT8IqhiwmUNqIBp5fipceuhDMaXGWmMaqS6st94LyWVeVWRDMjnz8VpFed-5x0W6r0JwGJp74Qe29dYl7dWQFrrHx45Q-qNJHfKrNAzKlhpSL2o30GiODUZ-cjPB_qXno-uH2BhrDekJJp_jXYkEbXMfXADi10yGYNeHxpCqdc-XUiZmdklQiwWgBbgk7mQTCkTR03Z4MAOXpm8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0xR64TYxR3yF-pFgI4r_Wa9sjPdx-r76UQ_MgUIdHxDrG9uNWtic1CtWUUIsdSVLJIqegXw4-rTtfgQTl2uIOlEsmI090iFNqI9LK5nhSkmUXOen44iuODGYR8XsO7aqh-zWe7_olUlFixYxWcrFimzcS2_QXnsGwXwkBVAq7qYiAhnV6TqxS7vJEkqpbEnHiZ7USVd7uY7eAq4u2yE7JRdoexZrfCHgbjdauGDVBI91M4J0fivP2UDIOXjIMd-Bd267hLR0gOp1gFQ3qx5r8caRYqw27ecvIPLk1YhPIP6QeEpzN0V1Bo0laFVLdwsMEr5xvgeuMQcWdbYazIRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WXk74c_PKlGIZw7cCuig1-Sdz7kCgiRhPorSldDmXrn261_dcTu-kXtcJv-psJJksNZEKV8K0s5UpVIcQEbEkz0EZtEzWjxvTQoMvzEJqCZEb22KCW5Df6DsdVHd4eBcHQOJvoaK5uoE94eHT3IMSmbU7wn5RuQBcpnqAKZofeUruO2ryleyf3kvmHVd5oTm9ndVeBJn1yikmzDFIKt4a8D05fe3JE9tjL6hpM9lS8P4eTIEaLWZT5CJNDd3d5VqhJNMqjkIRaRjq-2IHUC7g5bCcaH8M1zwjhvSWBnMetGTDXpOuUUsTlOdaJTko2mu9fDFK-OnmnVdEVzkq8sosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WXk74c_PKlGIZw7cCuig1-Sdz7kCgiRhPorSldDmXrn261_dcTu-kXtcJv-psJJksNZEKV8K0s5UpVIcQEbEkz0EZtEzWjxvTQoMvzEJqCZEb22KCW5Df6DsdVHd4eBcHQOJvoaK5uoE94eHT3IMSmbU7wn5RuQBcpnqAKZofeUruO2ryleyf3kvmHVd5oTm9ndVeBJn1yikmzDFIKt4a8D05fe3JE9tjL6hpM9lS8P4eTIEaLWZT5CJNDd3d5VqhJNMqjkIRaRjq-2IHUC7g5bCcaH8M1zwjhvSWBnMetGTDXpOuUUsTlOdaJTko2mu9fDFK-OnmnVdEVzkq8sosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FebAB0gz4VNt-xNxTdWGdYUuNseHzfKBjc08-quqkHyF2y-AlsVaFu8tkFLaUZ_CkJU9EolDAc6rAvRiNyKqpEWvhcGn18TbDn8iGI4lwXaiTqK7E2c3ccFWpMhaHOIQM4GrzqE33DEO64Ui8vClazvUKHvI7C8_gh-u2KtAmI6YpiV3IXFMnWUYcwT5VIuWBJ_Hi_sM3EXZi-Q__9KAT0tk5maL57B_S4TyqLobLgo-X7u6Tph4_UCrJtcGZHCW10Sjqo9HHIjZv-R3IFU3SJgNsqNo8e9gtzCy27ihQ9XKo2HI2XX0I-G73A42XXue8V6jZCH-cc9auVGbDvBavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=ZrW8TccZumA46nyPGNsWy_yKmOmAiJ4qRhC5oYamL7IN6Hy0Upo1iDQAw-FIVXI5Tn1718Zt9Bfp8XH6Mk4cMWNxWtF06OxuY9vG04Krfpi7f6jC5lhAq82MgiVFWdzYyx6WA8-LEGjki_m3PgdcATspwXmvg5Y3JPa5AnKO46WQtGoCOL7fhGW_IQMllMzn5ZL2zKM_36XiPVfS9LwLJp6pfosi_Lt1dpaJ8f1uZvzR8Ll9Mo5za26QuSVtNink4ktSmPFcjBQbmTEQNpyyGJnHMq2kOvAQ_3HYMDbEFV8nwe2Er_HLvi0PSRsOVrTChZ4cZ6r8crvHjnDZazIBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=ZrW8TccZumA46nyPGNsWy_yKmOmAiJ4qRhC5oYamL7IN6Hy0Upo1iDQAw-FIVXI5Tn1718Zt9Bfp8XH6Mk4cMWNxWtF06OxuY9vG04Krfpi7f6jC5lhAq82MgiVFWdzYyx6WA8-LEGjki_m3PgdcATspwXmvg5Y3JPa5AnKO46WQtGoCOL7fhGW_IQMllMzn5ZL2zKM_36XiPVfS9LwLJp6pfosi_Lt1dpaJ8f1uZvzR8Ll9Mo5za26QuSVtNink4ktSmPFcjBQbmTEQNpyyGJnHMq2kOvAQ_3HYMDbEFV8nwe2Er_HLvi0PSRsOVrTChZ4cZ6r8crvHjnDZazIBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=qzXS_yYyKfRMyjGnoK8T2Ter6_unJJlrnCane2nIq6SHIVYIfEdq6-EVqFUBEJfhVW7jqjjEeRd40cxAy6zH6u628Ule15aJYR8qVSbUxf9x7MX7nEqkRDJPqNu5nVvJF-rNeOX-O6NK-wsRcNfqJDzL-i6crpDKBSHZE2jNA00lcKSjTAThxKoXCSXyxEsTeSqK6heNqmjNzVxb6yq9dTl1JCpOZOCmDXL_dcxXBw-C1WqWpUl6RBXg4T9WPkh-gMkgry9w9Iz5ncIOTgWfKpF6UhMhxTgVMVYTYh5Ls_pjxW-RtATpUWWuwgS7HAX_t6nNFjaYUDNqmK3rdLF7Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=qzXS_yYyKfRMyjGnoK8T2Ter6_unJJlrnCane2nIq6SHIVYIfEdq6-EVqFUBEJfhVW7jqjjEeRd40cxAy6zH6u628Ule15aJYR8qVSbUxf9x7MX7nEqkRDJPqNu5nVvJF-rNeOX-O6NK-wsRcNfqJDzL-i6crpDKBSHZE2jNA00lcKSjTAThxKoXCSXyxEsTeSqK6heNqmjNzVxb6yq9dTl1JCpOZOCmDXL_dcxXBw-C1WqWpUl6RBXg4T9WPkh-gMkgry9w9Iz5ncIOTgWfKpF6UhMhxTgVMVYTYh5Ls_pjxW-RtATpUWWuwgS7HAX_t6nNFjaYUDNqmK3rdLF7Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQJD-XNYoCD_oJEgupJkYKT5fCRWR_u3-gbc2XB6ZnaaU96gLyxLJ7wAY_MlAkLyi9JY-lpE7muqsV7HajZDMdIAJ1whXThov5YxhpEgUw9blQ5SsTwTe4X_VpNDqDrwIVIW04bawNgcu1MyerrwxMI7LnyVJxbTDvZelr03jYJJU-AUb9uOv4FJxF4zzyS6LURy54VJt_fy8vtyl_MLrTCEvJKntCBsBSDWC0w47tygB4Va2wmnNsE_UDHQ6QRSOZDoK2AWNsJriNWQNxMWoaEueJ-gw0_pt9wXojYIji7aj9qzYFGqz5kbKEBvq9IJ0elrJEmtWaL72gPfncIqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOU4izRwtttGoVd7ZzI-ffRUkapOZMsM2q0T1Y22S4UEEfJ6T3biZ98NksBKgTD60AIZnPgP927EoukPDdaHKcnMmEk6Pfw0dtnli7dwz9SeJe53WK2l2Tr22m9bzuDhPjN1rinnW0Wj5ANPqSGHbotFJHxRD-aiEunTXRERrUjIpPsXoKNEdduMnayjZrkqxPUQdud96K8RITKvxZuNzKyRDmTbX_7pwtf5nBeSRS9bnipAXFsSVnHo1CPQusjFdep-cnMkGDA8CRDt8sHjyOoj9EnNaIZM79AsHLembFAA7w80s0FC8sy1CKGzHh75u-0CHxgR-cvv7QFFF-Mllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM2ZqFR01UW193olFqzzc50aD2AV8BlaQ0v7HWo4JaB8ye67CyfEWlgbgKmmCxvVrLzTYI99UeIssUoTG2_ewbcVtbDPaVmsUAu8Z-xbIOUHfiJ92j_3Oqo0IHlR7ihBlkDdBZJPc-S5NRs4_vUDKdUTFFZTxow7bClgJE1Uv4ykHoDXgWH9eS8FM9_AqgW_xiO1O9GR1dYCDuzAH8Z_vTvn0JqgltZuoFxP3O2XjNKV9_sZj5j7JVVMxFWh_NuzEBWC9SClka4Ca2_MeSytfEGYR5P9R6tmnt-s-U9H7tcUal7jynIaK_CeU3jSQyypSROhBscL27PTEC0NLpFQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC4Nv3yIZUk-UaBb1_0ubQSGvMqgY1qE7b5c6Oe5FokN0Ssm-sNvbg0TX2jv01_zHOiGlZAhaKa7M82mfUOJAZfjBJK2sU71xLy5BufIxe3_59c1Udjzqx8cx5TFkak1unMNjhJ2V7r_KS8KchccDVabeY9FkRUjoCG37JM_iFs8Lo17SGaxAkFhok-URNVq4wmqpSgzEDdMVLauDx3kPAz3Xm5ZUxFaguErDGpnAXRlIS5RUDduS_3oAAEiAJpr93V1QC84ITFQdrNUU-7YJVRfx5g-C41GB1GEZlEuQoJKIPXfGcNdV_g9eUvKop_Z6o4x8zT1quA746_MMWSkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irMgLaPTjhZCV7y0DfwdsAPLMP-xzeRpx2kpP2zSSqE0Sbqsn0Tc7J9f_JSaRvJOg1RJRtOQ363zowkG2yXadmUUwyP0-Yr1pFWY8mHug4hc3-JoNRKceC5U4rCw0dS08Cz9QoirIqTLIowNaL5Zv9q0WfnbPxVzpEd_FgK0HnB64ztTouNd4KIvaZ_WMv1LBvax0pUHIF_-Ii8Ildy0jPZ8GgNwr3Y_tB94neuNnz_KNbWJIfQbMtAqKSVTtMW9vd8rV_J6PR3ZYKCpByF5bUYODrDJ3_GONSMebF-VHDlHaDjiXj9etHF5RcSyiHRVkywkCmrbOjbbpQBnQ1Cacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=FtPHhG1KHTTG8LV2m4jJzJ6cKqBrj_8jbhUAJ_f4d2J0u9cXey55K-6pUVFBFiu8TGqUX4vfcsQU1XrVbE2TOBweOAm5GHTPFNaxVOIVwddMh47uUteSFY7ZNVA_Bf1MRZFBj8KjoQWxX3zZzMQoFf9QK5gTcRN6MV_acI9TmBCHJH3NwB-IbLKrGblUg-NrSeh29huj1hzeSj4pZocTqq3fQ_MRyZjpA_uU97j1b90gDqfLtKYtmikj_Szy8W4UAUKDsYEuNG_VJV_0Ts2pROR0sDI-ttWFmnrx5VgvY9-qpSMn1ft-Hbuehcl5UC6jogOdTrW6lNFxN3yydtH3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=FtPHhG1KHTTG8LV2m4jJzJ6cKqBrj_8jbhUAJ_f4d2J0u9cXey55K-6pUVFBFiu8TGqUX4vfcsQU1XrVbE2TOBweOAm5GHTPFNaxVOIVwddMh47uUteSFY7ZNVA_Bf1MRZFBj8KjoQWxX3zZzMQoFf9QK5gTcRN6MV_acI9TmBCHJH3NwB-IbLKrGblUg-NrSeh29huj1hzeSj4pZocTqq3fQ_MRyZjpA_uU97j1b90gDqfLtKYtmikj_Szy8W4UAUKDsYEuNG_VJV_0Ts2pROR0sDI-ttWFmnrx5VgvY9-qpSMn1ft-Hbuehcl5UC6jogOdTrW6lNFxN3yydtH3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=iiTkYNiNVVb58daieodNhNbNui_yhsOzqNhZaSpw44TKmlu199XoTzYpuhayDXfZgXWPhy2RbDP6eaRjERUp6EFRV9dho4RGjPrc1XMgXJtaWKBYc3xN-RqYxsoEk3CteJjz8MwO9N0DXV9qT_uJ57O1wZRjYdrE5-8-cVUTBJHJ2O-Rqco5cGUXmTm8Oj0U8t-9SF4kp362c5SPeV9ZPntGang3hwXFon4_GZlv-ax2M_Drv3WUd6JMQFLFmmPYjDSljWzvCQPS68_yXyKql0cshfIrmxrmspc0j_MlikWeaf9RnXd2yUUGrVfwjwjNq50UsvElExcaqmyMHpF47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=iiTkYNiNVVb58daieodNhNbNui_yhsOzqNhZaSpw44TKmlu199XoTzYpuhayDXfZgXWPhy2RbDP6eaRjERUp6EFRV9dho4RGjPrc1XMgXJtaWKBYc3xN-RqYxsoEk3CteJjz8MwO9N0DXV9qT_uJ57O1wZRjYdrE5-8-cVUTBJHJ2O-Rqco5cGUXmTm8Oj0U8t-9SF4kp362c5SPeV9ZPntGang3hwXFon4_GZlv-ax2M_Drv3WUd6JMQFLFmmPYjDSljWzvCQPS68_yXyKql0cshfIrmxrmspc0j_MlikWeaf9RnXd2yUUGrVfwjwjNq50UsvElExcaqmyMHpF47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=UVC1Tq1yErtd2KWie-Uag36yXNDdrxIretO-ZcnwrAqNGKwgmkgp25y1rBuUrc0GAlgAnEFMiHHskc-_iBTsVgEtnrKYViVin9G1RM_3S79mZUIRx2ED8zyP9buI74ez_kYELtdg4xOgIWRayDF4dBl4xBgIoC-R779vY4v4QDxQucII4opuBGpEhBWNTQS7dhZqKlxKVrblskHz323uDgFWlz7TU12_qA7aUWQQuAMtcHZmCbVWFtmkmTLr09g5di8iCl-8gEBkImSQhTr0Q2M_gAuGTtA6CcNffo-tAOxygd-5VRfEpw0GuxHE7ZztJ-C2nZsxYUnHFwpo0x9tew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=UVC1Tq1yErtd2KWie-Uag36yXNDdrxIretO-ZcnwrAqNGKwgmkgp25y1rBuUrc0GAlgAnEFMiHHskc-_iBTsVgEtnrKYViVin9G1RM_3S79mZUIRx2ED8zyP9buI74ez_kYELtdg4xOgIWRayDF4dBl4xBgIoC-R779vY4v4QDxQucII4opuBGpEhBWNTQS7dhZqKlxKVrblskHz323uDgFWlz7TU12_qA7aUWQQuAMtcHZmCbVWFtmkmTLr09g5di8iCl-8gEBkImSQhTr0Q2M_gAuGTtA6CcNffo-tAOxygd-5VRfEpw0GuxHE7ZztJ-C2nZsxYUnHFwpo0x9tew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=anzz0DLdh1kFXN8lfihdjwmoS5RUYFShnQXhe8aAceZrLTLrPBGCvCb4Td00TboOr93TR5MQvuMqqxxQ3m15g7S8nZw2AkjxuPjgIE5W9yJhicTGQlsYCmID5kV135w5UnBPpw7qZxNY3xr6AAH0codaFedb1Iqo3jwziddefVmDcns-WrMlkCSuP7oBYsRG9760xxJFX47iYjfeh7ntQicHp0Bslo37R2Z0pVcZPKJckbrtl8L7eNMgX3tIM8SFigJ_GnsTByDAfSrUMlk1w5McF6DGh10Y9aAHeeLzm1urikR1ZzOGmmAo9jbgxA_4z6eWQK-Fh-nTQoIrcYoIiLg8oQY-zxJtDzzHXfYlvnaJ7TCJwByfgEtx4jjwTVPKo7aaWPmoANTCz9KaMs76aUkp8VRfm3vDa7HApGtVcWJv52BRKFAAFOKOdmOkTCM2EKLvQ9TYvsSSCn22hFbOBPDKp_PgwYAclf3WM6n12Y0gtTqyicmUclGxlUMS26DJWa9aw_0NdJnLUywj1pbLlOfhgo-mvP3QkUL0oSozlCfz6N3yciXys0EkcpscCtL_pNhr6aXCBNaJZPdCcZNOE-113-z_Z_2bbgLL-qZpYFbBJ2KAp-dZKG8oFUTMHtI1Nw4ahLxZPQNeQ0RFxv7aShi_UGiJY46D8tQvRgakUHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=anzz0DLdh1kFXN8lfihdjwmoS5RUYFShnQXhe8aAceZrLTLrPBGCvCb4Td00TboOr93TR5MQvuMqqxxQ3m15g7S8nZw2AkjxuPjgIE5W9yJhicTGQlsYCmID5kV135w5UnBPpw7qZxNY3xr6AAH0codaFedb1Iqo3jwziddefVmDcns-WrMlkCSuP7oBYsRG9760xxJFX47iYjfeh7ntQicHp0Bslo37R2Z0pVcZPKJckbrtl8L7eNMgX3tIM8SFigJ_GnsTByDAfSrUMlk1w5McF6DGh10Y9aAHeeLzm1urikR1ZzOGmmAo9jbgxA_4z6eWQK-Fh-nTQoIrcYoIiLg8oQY-zxJtDzzHXfYlvnaJ7TCJwByfgEtx4jjwTVPKo7aaWPmoANTCz9KaMs76aUkp8VRfm3vDa7HApGtVcWJv52BRKFAAFOKOdmOkTCM2EKLvQ9TYvsSSCn22hFbOBPDKp_PgwYAclf3WM6n12Y0gtTqyicmUclGxlUMS26DJWa9aw_0NdJnLUywj1pbLlOfhgo-mvP3QkUL0oSozlCfz6N3yciXys0EkcpscCtL_pNhr6aXCBNaJZPdCcZNOE-113-z_Z_2bbgLL-qZpYFbBJ2KAp-dZKG8oFUTMHtI1Nw4ahLxZPQNeQ0RFxv7aShi_UGiJY46D8tQvRgakUHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpf1zkL-fA3vKscrtyXDVIPKWdIMMgkAYvWFrkCtBMUcW6qUoVvAXfzO-ZT_NuuXDnioOGRJJI-3Nk0L2afPoMuqMEvUGcWeysY5sKqYXiEowUYNCi9Dz01tKXLabFaZIle4qxoBm6wjxQuILfH2ibFEhF5g9koaAIOop52iBUoir_wFNWwQ0EsDSjDKzNYP9SHDG_60zmJMFZfgbaYmiIu6fpUW6_Mjm5P5wACrB2aVduyIyFj0gsuy9yeIMoxpRBLHhGzHSQo7vOG-0i95OcuRi9WrrxG7Y3EabEn-B1aPR_3De2i5RORoulxhiFEruDWwh1ZjpUTexprA1OvVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIu9EJ8Ciag7wPfGMZclKEVfWL2qv7NxkR7VHcVDNECcyBMSPLGW_wZfEWe66zrDlueYHLrmV6dNhuOSrWLyqVP6gDpXi7aXSkk8b6JzUB5AUj5aoiK3GuDvgFyvUTo8rFNVsY9hMMdkteBgwaxE3wckuUvH-fe4I7a-CdnY7G0unnliYtq2aftc5J4Ofg0Ksw1vJhcABX5qv58dN2fnR6nzvCuehlRu6oEhk7e_OA00etDpDeZ2BeC-Z3dIXs9x-Gl4sGr2XEclbdtImvSaPkOVEjV-puksuaKTv2OkBuAeYhHV9Rcbfi1L-oSIiXE7OXcGgPRq1plQz_V3AJZJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoIpbkLzSy2DSR94m5mNZdB1IVfBscqrut-KIz0_krRcSB59BegJ4f9UaKLQc13F0lLcxvSjNjtBiRqYhZrO0R65xvfDATQeWq4SuFHlqYfxJhyca5uK-zbsDJhqCH2PSdIGYKhpb-3GpUQU37yXzkphPIFnClhNoaYf5jiuDmgp3ZbB8fEQU2geb44CKAN_nbHALruZl36PpeyTe8ODsj84PBVqvTqRiPHaVFNwqm1D217egHPZm81bRNInXj_xoPKXXauLivSOS7C6JafFP-zGDYdT6JJfo-n79l8cgcG-judtERFO5ne5ykgdWDCOutIr399oMV7bl31hRIDQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YS9ElVH43GF0dItH1sLvsFYixcNu1SDJD0AD95K9fx-KWnTPM4gPib5fbUFntCqRYM7i9fHORalOEM5XPwODeW5FgPR73_lNLTXsI9xDati8XoHSTft64e7ZBkn41FAUEHhFpdfmTmlDImfUyM3oCFK-z8caekFH30NWlYqKNOaO6kj75C4vpXa22ZjwVCwnveg2TAY-LUOgrMkpzAxKJflREHYXSsTM1M5dxmfypLDd1YVwnqW8nE6NOvK3tcl_bFVQjGZOVzgmoXJNbcBwld8g2igkDFmVdPwWYjgDWBpeRV6dVyuBPusI8kCkeLOG-JVxWc-1olkMNknIAJOuNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=d1udy4Z5aqsiMjP8NhJfvZbe93aEO3_00r8VdOek5H0F4k8Cu6InKz6QJpdSrEYRKkJrHpZ99awbpS0W613UyEJnalKxcl4kYGWmxsmFoP6pc45pT1FztJZsC2fBaYCsXhOO8FKnpIuJ2278I8bWrGV8rudQpUaVYIoqnVpH2bNTxWps4wA68aibrq_2o7Ztu8Ofgb7OXf20IfCR-W6zKgh-IfxhdIRpf4x2FpsWcHSERtus_ZO5me79-2MQ6JIlJLB-OaIeYJVbKH16w8ylxjbM5ixiKzDR2K4-iPequcDcPLXORai4KoF4N0nN-nYMRtd3IWPGhZBVrG_EVmujs40NwI-ZnZLpcrrLXVnVlBGPYo5sfbnFX4_pamLBm1WGw6sMOj8aMwQxZfDVRFbel5nf3xh2umYkPNHWG33l9BC8Xr6_IFa-Zx0orDKAxm_jgdy2kous-ZpoC6O_lG0mzNPOUkesOGndri3xq54IwzuQiD-B845nW9s-K1MVtHdBY-dC2YSCzwZRrzay4XfDyDB9Zaq2ab8qvVs49HWmKqs7eNXjHOgK71bpt0QuVXCN4g8oRWX8xTmiZAXGBO0EEmdknoMXPXvlY9RJfpaRb1x7wfmxvzTe-8Bn6_FDlXqn3AhTh4mpFe2do9Ez-0iCZXUAmVlFrKs6sXRuHYtTjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=d1udy4Z5aqsiMjP8NhJfvZbe93aEO3_00r8VdOek5H0F4k8Cu6InKz6QJpdSrEYRKkJrHpZ99awbpS0W613UyEJnalKxcl4kYGWmxsmFoP6pc45pT1FztJZsC2fBaYCsXhOO8FKnpIuJ2278I8bWrGV8rudQpUaVYIoqnVpH2bNTxWps4wA68aibrq_2o7Ztu8Ofgb7OXf20IfCR-W6zKgh-IfxhdIRpf4x2FpsWcHSERtus_ZO5me79-2MQ6JIlJLB-OaIeYJVbKH16w8ylxjbM5ixiKzDR2K4-iPequcDcPLXORai4KoF4N0nN-nYMRtd3IWPGhZBVrG_EVmujs40NwI-ZnZLpcrrLXVnVlBGPYo5sfbnFX4_pamLBm1WGw6sMOj8aMwQxZfDVRFbel5nf3xh2umYkPNHWG33l9BC8Xr6_IFa-Zx0orDKAxm_jgdy2kous-ZpoC6O_lG0mzNPOUkesOGndri3xq54IwzuQiD-B845nW9s-K1MVtHdBY-dC2YSCzwZRrzay4XfDyDB9Zaq2ab8qvVs49HWmKqs7eNXjHOgK71bpt0QuVXCN4g8oRWX8xTmiZAXGBO0EEmdknoMXPXvlY9RJfpaRb1x7wfmxvzTe-8Bn6_FDlXqn3AhTh4mpFe2do9Ez-0iCZXUAmVlFrKs6sXRuHYtTjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNwJKurvAAXLCSjweE1GHs_IDzk3ST3G0N83UMznjsGtEsr1tHnhqAXei3cmqnUB2xBPlFqwOCLkZK9XljT1LizkbZLCEiCwSQ8t7KAn041W3EbGeAVBHs9Nj85Z8D6dm7dSZT3NHrP1dqvhJ5fQBE1hvDi5E1KNiT1Nql7Fe-grSu4Ms-zXDBdTbhnTBDhX-UO7Dk-Vf00-2GBrV0adbyA1obO7USYCXbrzMWn1HTgubU9WGU-xTKqPbjuKekzFvGKEF0daF2f7ZdEfqVze3LYPCgFUqb2UsiLSYeKMpQDyStWZZqXAGOdI3kTSMCrOnH7RDzATd1boV8iMIkJMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Rg8mxVnFTF8Ys6h0JZFMLvDM5OG-R1sVNJ0orTNGGdXQnuV5XujMVwNbH9PSFIpZmHi_CpcAXhghFqsyaiy18NmPG-bEQM-n8Ghr-vuvRBG4QkW3q-8WJsdQWz_XyozN3H3rmz8bJUlwpWdrpodR49oFakDaXq0AT2CMX6epzPk_XE2hvkNwSjLC_f1uRZsOOtN_kbN_ftPNoTCZlKn0GGOn1bUFaNcJqlyuRVp0BPmqZtIcC4uYNfczl3Hp_CnOjTwWmW9c7cWAPTW-i9WBoGrhS2nMmrc5A8ZfQnrZsxQnzvxZWC6pp-u6CGAhqfJUqRCyIga7TA5SABQw-bucZAaa1G3U4dUixr6YshkzldWd1yFivA690QCb0j5h8t7Td09c598I9QaubNk2e1uZexut0AThwKTNk7_-RBoZ8ImPdVYyNafDVbf-_hz3qqiMzDtETlebnypExycJWX5Tn-hY-jruwNqa35J1Q4UrVvkjbvq1ZS12gqiR2PPDUIraTCo6wARFVLQap-HM3g1wrJpFa_JNHVMUa-MJXEkQY4TYZBJwLm_iotPUePLepyPEQb-tVnWvKepAmPzmH6ukgOYIioJb0HIr3hMX_TFS1ojxaH0IUlx2tC5_SnZ5_gacqQgUK7Dk7q6DMBXsxR0x2MB65CKKNdEWVjP8HSEgJJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Rg8mxVnFTF8Ys6h0JZFMLvDM5OG-R1sVNJ0orTNGGdXQnuV5XujMVwNbH9PSFIpZmHi_CpcAXhghFqsyaiy18NmPG-bEQM-n8Ghr-vuvRBG4QkW3q-8WJsdQWz_XyozN3H3rmz8bJUlwpWdrpodR49oFakDaXq0AT2CMX6epzPk_XE2hvkNwSjLC_f1uRZsOOtN_kbN_ftPNoTCZlKn0GGOn1bUFaNcJqlyuRVp0BPmqZtIcC4uYNfczl3Hp_CnOjTwWmW9c7cWAPTW-i9WBoGrhS2nMmrc5A8ZfQnrZsxQnzvxZWC6pp-u6CGAhqfJUqRCyIga7TA5SABQw-bucZAaa1G3U4dUixr6YshkzldWd1yFivA690QCb0j5h8t7Td09c598I9QaubNk2e1uZexut0AThwKTNk7_-RBoZ8ImPdVYyNafDVbf-_hz3qqiMzDtETlebnypExycJWX5Tn-hY-jruwNqa35J1Q4UrVvkjbvq1ZS12gqiR2PPDUIraTCo6wARFVLQap-HM3g1wrJpFa_JNHVMUa-MJXEkQY4TYZBJwLm_iotPUePLepyPEQb-tVnWvKepAmPzmH6ukgOYIioJb0HIr3hMX_TFS1ojxaH0IUlx2tC5_SnZ5_gacqQgUK7Dk7q6DMBXsxR0x2MB65CKKNdEWVjP8HSEgJJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5dXSK1Fu05IlPmIlyP66l1lKag4vAOPaumg6IuKF1tKPZoTdXIUQilZ81aavjY_GaOEGR7284RlhrgM87RzuTmLyh6guWRWcEOrPmyI3DIU9We-DGGk5_CiQwKZpGDTzjz6S-fDVM-B2tGmcUH05xK66C7LXqh50OE51knF0msOTd7CL2BA6lzV1mYW2mwgHW-Y_3SM_Ne2hcC2o9JzcuQH0duK6LwRdafY0BAHilbXIqsNxXncIdAzw7UE2sccJKqTkdbtokaC-UdIuD1bsj0dshtOD9-zZj4pLlMeDGYtILMRW2LftS8ZRXzEolCaq3xKYkz1OQhCXxgQINH4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVizT3rgbZ7QVP2pPbAg4IqsAUOwBqfWyJ34HMWIoqsCJEw-DY85_J7Z60kO2GNnxQr5oAGA58gf2YhRddLecHXucVw9Tud4LCBX31AC02ZLp0jwueTHIsZh73A-sfGFixU123t0k6BwIU42jATZk7XoxsCpvZa8myfhVLclm66XVauekcx2KOWvS0M8v0wJgBiVXPOiWr7d5OxDyEd-B_ZLnQS1y2_4L9OQFy7WaZOfWXJAHSueAib6QE9LmqF8AhDKBsm87wfSI2Nxzb0cvuIPPsQTSW_9ayreRtCm-LxkIt7XVYPUUVhnBcDm1dgcwYJaK5GGlWr_1yI6xn9sGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A77a17dEf63CulEIJmslQmnpYk5NYE9bt3AoJB3X53QzPjBuFZAC5AZF0Z2SCs5Cu3Ttg2-1Y_ompV8F3aYDH4WAkDEQunoRRQ3CvmXKmPqwy2Ujtz8PQIC52ckmE21_QwaXdn9N1rXCJHBDWVADGmp_4wPaNsio-Dk-WTESizO-kbU6CieeTM9uH4Gf5kFP_irSs5Lb1XCViJzL5Wk-28DbKoi162Eu_l7lCyxeO89sKj_AURs8QeZSjsu4uX18-r8lJMmYbC_UARgC529AzyixQhzuPReQkHfB1JsQYXlN4oEjd090CMZqYE2dZJ4sQyiRTwXvC1KL2Ugq9MYNRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p78oFGLPLpm6aW81ZmzgiNX29rfqPWnyJJzdMspz_CzWMuVEG1IX_wnXNKlJPceolcVHxmgBD9WWgmmbovm81dbVrz2-ytyVL7apq7xLnJUsqYO8IUJK4MFrPsJLCAAEZWBBKp2wFhVOdF5bCwwVqEE9ODTl6zEj5s7FKZNw7w81MHxJR_8ladOZPvs8lVS1yG8gA1A8XHggVuUgQcRx8gy3nvTh-keAAUmB9Dovq-PGS2EKrs-wmV0Hwv0YRnv6qwfw6V8BGR7YPHtIcKzM1S_35mWv3O_KzVhmqOxwfLN6U73lYF-KO652MfILQkHEY1hh1dBCyrXhJJPb950-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfOX3b4aOHOdc6_FY-d1M0uqEFlScHg4DoHHBAUWhiRFlHEmb3oP8RxAFxYT2dU11GF2lpp3sUEOJtXEYGj492QFe-42zPnjOqByrtn3iBajRJbzwobQA3cKLfkzLCPBCxQxAQn8c0kYjLdx5ReobINNvFpoH3DB93oiSj62LuwIA0BMlEvA0ZN6EJjwff2ykzpruIpI6XgSFXBRyLMJNCAGUxEgGBZJx9KWnMAZ7RrgzU5mlHXpfTvpMeTUwJrlrh4FIbyBMTywCMP7oI8OX_WXz5yVBjwmqqcw3rWLFKjvPL9LNK5BhMXlwvWGKuXCq6X8ZSeiFvYckuH5HnkZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNSboTPj6EunEFVeBpOpqqIQrR_hhodJVrr3qUZkOOa07Yl4pXbZ399f7cDj5Ow09B_BTYOUOQpQVBtYxELkpxUwNqkABx3lmLv72aIN6Fj-sQf3b2AhxjEW-dp-xpzF9YdZKdGwqM9CA9ND0fqkfvFTmetQunFpFFYgpwSNY3Ve60sW8csVOCxIuD8y0OLms8_pZbtfvriJQ0WcdbTFDaysbLPDqL_q_oQt-aQg7hfDbof9eJC-y_02nukdSwzY-Y3jwDJG-PXqT9I4eacQihbA-FPYCVNxbNwxuCJDlJSCtqjtduYLTZ8j3CDScpzE4sTF0hH5m8vUkn_Q473q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOwXUzQG_XYSVpUuFg9B1182-9h7Zhz-xLDRj_Upx4xA-TZQ-5rBGTOFjgcQ_cxnkFBnZ-tcMOTw7Mjg7A_eKSgnCosTSB5poyNevnInf7pk8rcU3zcSCHrCjJpsLW95TAXbF3pKFvIqKRfKV_HQCTB7PNcj9espd5l71AMT9_hiroERIFHO3ZQl7KhWam7-aqp9Yatd5zUmsiHO0uIFaFlDGi8o3dgm8zfAWJIlCb05NOGDkSurkVbxNPdJ0jC7FH9yYFciQhrGOM1gmSxYjH7rlGenDOESZh_0q6sXn7SYJ1XxfP4xjL42otfnvkOyhDtG7zKMRl5c82pTG_EAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9pun0nP6jbgtjITVFnTtUXWefZ_XwocMdmryPWIlGO3d4i_dc9dVyM-SWNX4I5wgXhUxW0sVjOtOs5s-i_5DOYBiWkp3X6p3br97ZfnJxpk-1vXLnQAt96edVgEyMQKPYnYtQHGkMW-QnzYnHBmRolwtb0UTQfN2-1VNPcNaP-nOf74W1g6kRbJ7f2f_RlTEcQ5QPuzEj13eV_bu0ycfpka-tYQWGfBqQSYW2Vy9U6apYRphw8opu_rjW7yhB1rkrM4pfZSka7uBO-uyAdSvDyobcK1o8IOwpoh1gD3nU6wzO6v0k62zYzEhOYeLk9zFtKV_z0cC67Wk7PrtW3IAxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9pun0nP6jbgtjITVFnTtUXWefZ_XwocMdmryPWIlGO3d4i_dc9dVyM-SWNX4I5wgXhUxW0sVjOtOs5s-i_5DOYBiWkp3X6p3br97ZfnJxpk-1vXLnQAt96edVgEyMQKPYnYtQHGkMW-QnzYnHBmRolwtb0UTQfN2-1VNPcNaP-nOf74W1g6kRbJ7f2f_RlTEcQ5QPuzEj13eV_bu0ycfpka-tYQWGfBqQSYW2Vy9U6apYRphw8opu_rjW7yhB1rkrM4pfZSka7uBO-uyAdSvDyobcK1o8IOwpoh1gD3nU6wzO6v0k62zYzEhOYeLk9zFtKV_z0cC67Wk7PrtW3IAxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwVnGXV8TZgau5npE1Mx8FC46xoeG_6PQmdk1t5EQ2qPp6QTso3p4QyjQAEJlknKl8dIiO3pEDdFM109gZcVgnQqNrvVYXV3shEpMAA6V_L63SAVa-CELaqzvVWDKa-3CatL-R1bYXI0-l5BC4WEitnV66wELoIh--flbQvUXZUudOFhGFuFTn8I6IBxHEdvMr8eSqknaXYzj2Xyy4FoIsgUADyA2xjC2AaOUynKBZIaOD8fE6Vi_RklsgbMOD6vD8k5dj6tOrmNdUmwAlI7hSV3Z5iTGqoQyhMqqvabHH4zjEjgrjJDmXEiDKJEobD7IedLo6x9Lm014Z4_MHWsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-j9TVJoHDRt30DUdVMOd1vMmqYIyOnaGLR-k5LJU-YR7H9915EeANbzCbQPabFtGKPd1A9Y8xntn9BTIHd4KiPjuBNTUfHFYCK3d1UnEvHUUfZHbXxX17gBMUR89Ajoh9-b-SDcwA9Kk7kXYgcy3sTSIt1zoYBEurerttPPw4q-quYc5fTzfyypZfUKwKlU_XS0G5dcikNUiodASmXvBY8_oePKKU76363oL2hmWhBLsVVmA4eImSpxymV9sg2HtwRt5cogPyP_ia5tJ62StbKpoLnn-5LCD7Wzv_nqswYm4rgYv_cd9xKSR0iAzDXFVw56pS1L5m1MANN-0seUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZRnRK-5RnPeDwbv45hKBQZiB6_HOyBacDnF-ZyoPbE4ryLKhQKFVcBop_g_dDZ51M1jFiYbXX7ICNc3kIooZwBYaQsEaTdz-5BGZXRKibaK1FekIJ19C9aWtH_izQD1G1UhPq6ljXL3vYhxyoFYerfyiYbPiKfLEVNNuhc803dPAMmO3ebjhxudczw0-yT8uccZRuk9oXMd7v6uMFlKXJvPTe5yODjqjDV1dCKHoro0IWXyXNiFzlK5nKtXiRxHJqkuQMjT_GKx7P1bMZD7qhxfEysODsLOhfGET51cYPvC_aHUPpVSTO1N0lwgubCuxkbWxPmpq5uNK02eD1Qdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=BwOg2DeedfvZ1OQxXnMuShDcSuaeclSWPgL9plhJ-RcKXaiuUb4SVtdJr4pmjA5lmgRiorcEM_mXWvhz2mcHvWOhLdwtIFZYMYywUlh_B3J5RYDjWH6NacMXsJbyYgLAwEhND9kZdqMdXS6URkwMeD0D5mpEWzJt2hdH2w1DkWaSv_q08a-V3fu1YSzUBO4Q__8ZB5L56vj7iSUtvmT5hY8tjXfmVwcSqF6N8_C-5RU7HOMWouVA3lvvdJ8GxQ9k9bY3sHXAp7d2bY3PeknNlNZMEFJ4kZGY7mtThzQP7MuHdda7NOj8IBjVMvfaqHwWFO7Ja7CGxtuIEydVjGGkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=BwOg2DeedfvZ1OQxXnMuShDcSuaeclSWPgL9plhJ-RcKXaiuUb4SVtdJr4pmjA5lmgRiorcEM_mXWvhz2mcHvWOhLdwtIFZYMYywUlh_B3J5RYDjWH6NacMXsJbyYgLAwEhND9kZdqMdXS6URkwMeD0D5mpEWzJt2hdH2w1DkWaSv_q08a-V3fu1YSzUBO4Q__8ZB5L56vj7iSUtvmT5hY8tjXfmVwcSqF6N8_C-5RU7HOMWouVA3lvvdJ8GxQ9k9bY3sHXAp7d2bY3PeknNlNZMEFJ4kZGY7mtThzQP7MuHdda7NOj8IBjVMvfaqHwWFO7Ja7CGxtuIEydVjGGkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG9LAESfp8rhatg9U-m8Dg1hXu9WP8TDkkMR-tWllbax6SHeW1vYM3JU5FURYCXkbuJeGEebZazSCcy3o-mZDqlgwXHnzutc6WoLErNqwqw9o9ukkSsfmdP-okKERCKIEr7Mx2AtMYnDzOhD5ATThFTUYw214Enb2NPRvlaUnSwilkoi8pCOCXHG-4gHNglxYzAkNAtvWq_H6hszuWO9F-VBgtoypYoYCZhD9kaXLg73bPQUsZC19q7Vo4Z-PmUKALT4UuuIGOsn3thz3slGVjYdZ2MGCx1JDT8hRt2eXObjfHHbjbkvGtqBFsKbgiLmsyB1lRPZyVJqN_zdpPrOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdA4tk8YpWYnt4OpFNhR_38LxG5gClKOYRpTio5LM6T6YJGqdSnLQ3-_Ml9Sdn-5b8zcCY1u9ydR8vZIsGROtLoaFEj5L1_QQfGyr78kYVW811vmXXtgBRZ9dBLTCHjeR1ARgbfOrRPlIGDoF6fkzz39_Gnsf2kru4GdF-TFCpxLY2OZ_klRSZlUyV2UFI5pwDfCoCSq2_QX6Peq_uOmWhZRM7B7pkK-4thiiFYfIZQtLTcwZ4pmDn0xrMDNC81ezQIT7p6igPxaDbsDfX8hIVnbbp7md3SR6LnnsRRq5Zg0C5yftWVQyHqJBk4eCyK5aVGwadGqCV0UyQR66UfFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNW8XpcSVxDmdkSAHm-mVeBKVs1ycBqS-JcTKzHPsEwz-zrF2td6Zdb8iGiYGnjcCxFQ6K8UFdo_wWTkxr9rYJEYAyH25bXjkeBr_LBPC2LzVlzMXsvzAmIunrpYoISKWAMmHrNpXD7vg4t7e5W1711dqiD1kljGvZdCBcwF2MDP9LSSDdcQbFTMoq8pMT0hR-LURMVPXyU602Wle2teasr_QQlHKe6Zb7xExknue6QBhUaXuSvnNu2-Bax7PJhO4zqmyG-IVLWE3MyGl3SwBrGpVG_GF2TzbfNpSbyKQNSdq9llVBKZZPlpcB83EdOqPUDIEjfaFeqt0zqh5574LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EScO5Kgh_AD_MY7xuS2zP1uFaUqycVeuB4F7lmJjiQngC-M72qrZBKxrLcBJN1QZi405WYy1MHEksY1yYlgrE9yZ4ffC_f8eC2d9rIqIbvCO4s1vh9awRu3OqWERB_uOGb189z8H1AyUWcTiJIJD6lVH82XPus6kge9gXLNBrT5D44zttyCejZvVXOFb_5L0oPEoVpHYqoTw-K6zA6878XIsD2iUMfPy2S4Tq40LgjOeiIwYL9gaeuncGWgvL2zvlCuneykB47bpw98MLcpsDOgs2-LNaG0P7bOQGytBeyFW4yoiXAqC9vmLW56qmV9rAP28yuzHHlLndDw49tH4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEgnppfQxSR-Oy_gylUH4D4RBIP6tJMXhYAzg7t3WrsIH1uvWihjkXw7mY_b8lP2JIBrQ3ALvEX44x2mI2W_6QC5YVYbLDESjt9DWJgLvn4qJQCoCGeqMhEzu6Zc2BZRplQFJ45fgGUrIkm0C2PHEmOol2f6WI8VSsls8k76TITfEMyK3fQg18KKV-Lu9CYHzdwMx2a9wGuRqNx8JzjXDuXy0a4m5B5A7JZWfndzIvo3ozYBJ4PaZM_s_O7iTdZF6hXY65yURTa9OxPZ4NaeaiyFwYW-wOudaBa122QF9ZtOz9zBHKQhst4nudK7uEEELKB-AvDUYoey7QCgsTF46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijcjg7MUnshUHU4HtodxJjKPSkEmLlGEpne5xgVmLQbmQH83A6Tz3AKF8bainj83jTRVHWH8HoNkz_NiBa8LNgJjQVlRyb2cQjTXquzuJn7A4HF5ctLeq24lTaVRJPeKXeF43LnNACf_pzqNH33a_B88AqInYbGD5OsyNY2nORO14EQie_IQvoZKy9oCvkofUlQJh9Oj0AUAFTjSL7ia0t6hmZ8wOjWV8ExEd6eTT_wOrSOsjKxOKa2CHyDRs637VfOOLLgqWTiQKmky_TbmmCgH5rCgpRjBmOwt4Oe8RGJ_lUd5XRBUXNCE1VxUTJVMih11PLsUJSn8in8CsMpPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0C7LYUhvlx6yBLzeUVeVEeDjEECawHGe6bWRCYfaOx5FfG66gA-RsmZANpYDi0Mo5nxECKn_1rripCZHgle-TmKjm96SeqnPeH6Wk4Gc5rErWpDNr1j7HfUm6HyuZCDbaOBE4cR1dBE5VwjPE2iP6EQQaMBYt__FotO0LzkqXfILsraK3w1BfOKc9jRycEZ-a0x3F7qmqVInQEjkamMybWIRonS4v0dnD03xCqsu4XWTd5_B3XQpeEz6dpAeaaNtcyewskfKOVkoiFm52SYe_qPfrILe0YEkAz6oNLJnTnb2dRsmyOP5nILELbQxJmE0ejOE64MSajAplaZTI-2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkYe85gCQyhbGMBijAufJG_i25iWikVd-b8nFjBiVD4pKI3BTR9h9-1J2CzZRS_WqF6xO4o-juhk3iP5xklrxiA1p5PgtGwtPVxlPK7ks6oQ3FPR5_jE8FpJITngjsIC7-Ivx3yIgEw0C01t2i_I4Mq0aR1zv8DxY4968cuzZCTAZnYlFjNQunN3rrXYT-2ejxo2JsSe8fTRPAcPQFkiOApMYiHhamgR-rNHO9yhR4ouRe1s5pZt41yVd6IrWm0jGPgPMNDWv-9fy7suwXEuMfYAHlebcFExcx-s1Zz0FqAnxhvZBSiLycoYlRIBOZgXT0Y7tYbslDCoe140e4l8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nwpmbMnVwadn_F2ohvWLoOr88IqTEHm8v_sUMj7fp7J6qB297ey4nT89pablqkkT29ObKLNGXO2KgM7Gv2Z8ccE9y5NNLLonLv4pem1NCJxvMKvBz4fS4Nvpo3YY-TjBBIdhjH-wf45HgJYStkgG5ODYqHfGUbBUSz6ip2WVcs3u2MdQAQR8NDnVb1l3puz8vqIbjnFEpR7t7sdX-2DkayUsgtxw3ILFOSktQadTnnoPCCBz_yu7QwtICIXoAy9p4sH87Kcp0tbEykk2hubrSVA5_oRHcWI8yi-9OFUP6H8AIh90yMt5Q3WaXYvXwVHPL6YQszxXO_SK-nYQBRlDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nwpmbMnVwadn_F2ohvWLoOr88IqTEHm8v_sUMj7fp7J6qB297ey4nT89pablqkkT29ObKLNGXO2KgM7Gv2Z8ccE9y5NNLLonLv4pem1NCJxvMKvBz4fS4Nvpo3YY-TjBBIdhjH-wf45HgJYStkgG5ODYqHfGUbBUSz6ip2WVcs3u2MdQAQR8NDnVb1l3puz8vqIbjnFEpR7t7sdX-2DkayUsgtxw3ILFOSktQadTnnoPCCBz_yu7QwtICIXoAy9p4sH87Kcp0tbEykk2hubrSVA5_oRHcWI8yi-9OFUP6H8AIh90yMt5Q3WaXYvXwVHPL6YQszxXO_SK-nYQBRlDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxW2r1FXtX_90nwFwVx3vfQBRghUrAoiJmDUr-u53Ci5ooYUCbHLAWOVVTOcnukpYoZc6xi1OgwSo5-_z6-ltIb3_FKs7Fn8YKDR4iOPq3P9K6cCLsO3pMURnDaJ5lYz5yq3o_9MBtj1FYQTV4n-qXQCk2zYtiyjvfeQ37PjQ68jnUDdFnyFxBnn_6wzrnIQgea2D4nJQ6iLuVLEjlZA83MmylxQgNG_rokfcmGelnxiwLpj2aNtDBWNQlzSVQgSY56_S3mwiEbIeK28Zi8lvu70IRwfwMS9XWdjrUMJzqEAgLAuHKkYH_l6PssuI6UeO6mIrPwoCoPeeDNFw43mRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrXwkcevqhyvjEXglDZ4U6XBt6A2tkN3qagpTzY1NiN5AyUuhYOxFL2zjcj9xSPR5CcBI5w8oB9_Oke7FfA3S8OxMBgEVksubDtQ6NcnaepsfWdyabXGjr03U6vwe-D3w1TDIBK26HD60PQt_BNXZnzl-I53sqzDof7l0_Td9O00J6JLebe0dfJqHjZHu8zLdoBsqjMqdp3pFBcXWb3PCC0SVsnxWTy0fgiEL5s23EsTKOvY6gvyL0M2-2AEBdn6IAU6KE-PMLlyudnOjlUaBwvd8QOeE1QVW2tOxk9GZlCjdyHPnGF11WsOhrbC1aJG7oWYko-4YAk6tY1KpMIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brr8wcCFqrZAZXlYwbBxrty3gvqjmQhBA_4w9c8XUCmNche3PjgfY1prd08hUSiz-tj0N-PX6-LuGATMz597IOMiuqvWrZYYnNHcjfjYpuK1J1RNr_Jd7LHWCTbGNDtoyCClpbQSTi3yjEfLjwJCsEG6krJlpPlaKgO_qUwp6Ou_gyqNfotOQDifWajGJj3D1CU6Z8HLmyjgP3xqQl4cBXw5cyaLOcQ95lxEy06y9KO5_OCN-FhKAIqjKTbS8zebXChUqqrPxRw3iDOT0N2GYolI5_EN6wJKoN8GpaILLtkRbiTc7UhR--Lgka1UMHgFyjF3RxQGlNpxAYjC91AzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EULw5383BI4EI4qFTNa9TfnuX2uDI11hdRm4xaEa1tQmDbtYoLKnv4UAU31hR0_efcke5x309_eTwGN9fwetDLwCNn9kumNwY4C5Cbpoa-llIApiNJz8p4u9DAhqtXsQsFECsinqK6KDAp3RPzRPkQNLsDY8sf5KAD6Y2ekYIIOWW4KLuG0j9Bss7XODgYAriuAnI2wryUGstrswUkACg32uaBGCSR9l4WyR_P05aeyWb-Vq4PY7JPFVdrQ-SwuI_Ms4h8F_becEupCPbZ9kVBO_l6HdyFlKcW7ycdg8Mk94HiUOdnjJVB6ZQt_THjq9GJ7uG71OGaoOzNzo1s1G2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=WyzOmefoIQMGnMIQgfSqqP2N1RaPFi7Ro1PYm58H-VwTSSKTdLQmA7qsbStQp6DQKbJ8mJscydKOJEIUQr3q2hU2sUiRRlDuL4J8KdgEC5uylHncDfuYwgORAVsiWI4lm5U4tnICBYUcfe-TqO-vsuHTiNW8be7ebd7-yDMp7haK7kmA_sO-Og60CzMBjQiSqGVOiugSeFh6wAYaqvOwLrOzsToQRiVLhdgbHo-FXw6bujdt03mkNQy8ymZofki1Ok0Zq0jvj8dwj2Plw9Mt26eW75eAkA-o7Zy8NAkXCtzwdoqjkfO4DraQomXIRBWQjxHH5zGTFKSkB3HZv_mobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=WyzOmefoIQMGnMIQgfSqqP2N1RaPFi7Ro1PYm58H-VwTSSKTdLQmA7qsbStQp6DQKbJ8mJscydKOJEIUQr3q2hU2sUiRRlDuL4J8KdgEC5uylHncDfuYwgORAVsiWI4lm5U4tnICBYUcfe-TqO-vsuHTiNW8be7ebd7-yDMp7haK7kmA_sO-Og60CzMBjQiSqGVOiugSeFh6wAYaqvOwLrOzsToQRiVLhdgbHo-FXw6bujdt03mkNQy8ymZofki1Ok0Zq0jvj8dwj2Plw9Mt26eW75eAkA-o7Zy8NAkXCtzwdoqjkfO4DraQomXIRBWQjxHH5zGTFKSkB3HZv_mobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI-HmLSICe4UL4wtfa5SVJGbRsPwQq-hTihGpOmbymJTMwIdQX6GIRsD5M2NIiqfCyQ9Z0-bNnHKdENwG1AEmLlTDmqc7DCHZ8opWnLFuwlnpZ_Ot0d2g57V6bBPi_m1yVYVG9S_Bq7W9QUdLU0xVLY8CuR0CRKk5hyM4w2nBp9EXA1kfGaUXwLDknEulKLOor_LmQTKUjwSnmrZRppdei_vhNpEQc4PPjItHszk-6uAjGTZCvzCo695phbtXlg1mViE1Rm4cHj0psfzVaQRWUBibATSCaTW95Qyld9h69ETdRmTIGGD8fd0jgMV5gwqvIN4bNNOMXgEnt6YokX3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH_zQzU_JEs-6RkxIE0jaeW0V_ER7H5aZ7zq3n_cPJMmthxgIdD7iry-GmmJzWfgFsvQbqk-MuL2GHsED9-cqOuqmw0Awf4VNGeVTfSosKGmYB4pT1kAOkyk_2-YSbQOG1QXxrU1ygeRtqLtL5K2vWSBLw5icQr24xRQux8t6OAnbUyJ0W9fU53wY9VixLk8EZW4kxa0kt9I4mZdFfAKIwqvKu8XYR7Ny9Cn3Vp9wj_HG-9zgeuT1u-f4WRT63tZRkPmY6Pma0B-GeegUggpDuhOAZO_RIkc85D9_xHAYv5FdSDej9Kh4J0DXyJ7ONHwjlVXyX3cgeVNPSN8JxKU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
