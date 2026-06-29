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
<p>@persiana_Soccer • 👥 340K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 08:38:32</div>
<hr>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvdSzkqcFxa5oTK5eGqwgnY3XkReJi-wQxp9Uv-GM9QaSHgqR99rOUJlzUFBvLYXLwan3eFrbVwXtSf_zel7lpzSNlTJd5mQgwSuK2QEnGjzW1S0FhKTZsOfwsMkNSSbhasLndi70kmkdQGVFFQyC6X2QXLWYiW6F9qKxxtHuy_8KpNf-JbWl5wabhrHifBBpA8ee6tk9w_M-5xx_Xbs8po4lKeHl3sa44bmaMR5pTBlfq99spSu9i9oTnA-0xLMd61r7xuuSgW6ZWgYzbRhH6l7uQWReoWtFMGgq2vC_ROtGAr1esOE6QYX12k46nxS90zhNx3LKWZsJYfSSsl8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTGH4XTwx1E2GMrkKUs5NOIgzmheehTujEPjTO4Eg0zIGeyRoeGBGmLYk1__4rZprBBf8gePJBn3W_11gcKR-BFd1BA5S7mNoP5-HDk5Uvr3DqaiZogSTMKCmp96uuZhTqEeXyqR8o1rAyVglPJBUZOuRlfhOo0TFVtrWY_wq1kTQZqOK3mL0-C02TUPAYWbvb-mp6IRsOClKaTHiBOfx3YKNZoLJ64KX5lBa7xReto9Lav9iR_-Dq4KmrHLInMd7VvYb-Tg_zO1UCtq8sKWvxv-ozRxRpqVklk5Vk5LXtpuBGdqreAobvvsnXR2jwJAwvHp9YWc4MX5AexyoFXonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPtCsuVASscOh3LZFRRmKiDi3h17xgf_Oc51QZAhMQxAic5XVYGr-OW8akLIhp5rnSH2Nt8aOvUidTFvRtMRhMxBgCl2ZddFbVLlzVA0IaK4SYUQUKpVdpDApf7XO1fFJIWav9IO0kklTWrk4Z5PSLxmayO9qfxYLwEByXGqEtUku_1Ij3T-nUfk1usrJzqyrRPimqo2T8fACJyibndHjZovGBF8jGhvp6sNX4mHrVMlag8g6xqPFIcJaeaF9ksE4Iz0DZ4iEPpv7lXxSUQP_TZVhSiDmYOr95RaiR-zmtxZ5jppwAG017qf02WADjxNxc57GLlzTPOhGCCWLTyjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJMEmWd_0MNmVoe0I-A9wd3HEoZOUe1iodZelPnleHaXrZ71dols9KLrGW7h3cgw2z8zZHaqhD1Z_l5KdskbuKb2jBYzbumXeg2WkfuyXQJ8ajahWI50rBUvJCcHrppGpbfq_suYlBkNYdmeKDq5gWuqo6TCjMTKtyU1SXqKtp0c-HWbFxS4fnHv_6mM1VcbTdUCxePAVz9TgxzUqIXfCyyyYaAkHbt9yC4C-0gNmzv_0fRnPrb7Xn4UIbWjVK_yo_jr4mKiueje7ZzbLdpMkfEX6tdlqYay1o48jR_ej-0XBgu5QEj09G2GcBbZNbpCfIEhqcKxpIdyWy5VjQtzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUP5WlqJxBfmVY4UAJ7YHYPH4d9fJTErYq0SyPTig79rCxsNI0YO5Scrd-N7niejkeeF0ZbIauTKQ-Izd181elrqko0awR4BIzaKjY3y_XQI1c2ofQQxs5_UIJzSn00d7AMuscAYspoSBwlUTNwmCuQ1q0Uale7us6zmH68FVAhhpMs4-jzXxbkBQSxjuh4aPmjIZXM5Sgc6VczzTKl-82mG1X94DhWMdzNdUnlL26e7uBePxEWaG9wV9PgotQgnek7s7DGcBKgcQ_OZx1UkOO0xx8IhFnTsOIqoiTv1LC9BvW1yW7n45cWl8yJbEobjCO9RZDmqTctf6D90PeWNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9isMOTg_n4wJOYPodo3om7IN8ST-3s9qP29ZrFXHuSk42Jyr15vjYgJE1iBl_m0Zwlz9uguEMLip0kUsIbH0fVYL-F1zGFgzpEnzJnqJ-QuDa5AbDoPuHyZ1idl343VLxDofs8V7WhDyZYOeJIe5waN3DdbYqv9AcAZROR4OOu7QHdeJTA5INIVhh86xC7mzkieSSfMI80_AQ-_n1HyLQT6PpzgEUOvwNK399j_8Tm6UosQUiEYGMc7soLJqqOm9ffpsXQV7FWCFD7i98HDztgvWOSP-78Ttw1Zx59Ptlo1ICumS7FX6Fnl9YtlWFVX5yktlUufrU5PSn3C61zklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24576">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/24576" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXUZlpTkOujeCB1YS2cKceX9q7ngb4wG_pawhxf0UM-QAjhFd8xnepSejnbUOI3Ml1dnqo52oU_b_R_75JkOJcsaLycwG3Qw_BnJZePBAjvyh85-9RU3WwPmbzc45nByCclvUGNBrEnWEgAeBTlprwdqju-PjAjMqSVrXcaDIzCB4dG785x7WZXV3M59DFL0m5NPMTgrHIpYMCkOgaZOTf81jWCJ67wC1fCJi9xfhfHVIsyYIP5Up7EUm9TV_uitlZlz4KZY2FYoe8KqZEAGlvDJCVTY16TBigJ5uzNVALnwrM9UtkyKXtLmZp9B34jlbrktb7ewokFGZiHo9kOU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jCwhuKCkvOfZeqhyY7MM_hDZhhMV8_lF6SOifbUlfbFbQYpIr-2NyLP-PEJOYfSrMDt3pZMGzdpygm_cYcv2oi6qxUFz1HQ9xRRPBPRMYLGxvKqj-yfYHMEkyYWKeUhCfIjBaPo-s9hBlKGXzT7An7szQhC00Z2-XWw8t8K9Oai-Gc-p8tXr3ltM3qlKcW-b-Hk4Q-gsilCNduLAuLh1i-oWVMDO-MPVoumAu7skOvHoahLqf6loLLmgnwG1hXrhtSxfxYVrkaucGYQ5KuLh3BXqqyNnlhsWewXd9ELdRwA1VNtgVOYDn6opQ6IxQxZ3yqr5Q_V6T8NF8Lttjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq1YQWv29tw-U_AS_H6HCSbQHA1CblLyRVsO9FuhNmGihYQibSIX_D7UOE5w48dw81rC6M56ZTw-ax2bAJm9l6dbp-WroUXhwtTS11u2g66fYxfZQZiE8EOanxSJLy92smR28eQ_RYRQ87wWHzCIitZZ4mlNJvQcUDtL9Zfz6AqcgCz5lz92C5KNNFZpDnEkB_A0PimLO0uWRmi5RpWEyZ9uQn7oDlvnJoZZXObJGn7TXp0M6esk5ZYzE_LIn1rVk9ljdmDCfQN6KvihFovOvNakMslSnXGSJBm3WSxuDZPhgwae3MpQbxWvHs4fJADC_xZeu2Yn-XN0peR5yS9Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6tCIl2IGgB-AM4JRDADFC-7H_fSZpdg2XRIdZhw2tCRl7oIGZWR3jcd76J7Q4p2Obi-j-FaKCZ7y3M8TY4kukwsklPQmJ16pTJPLkIpu1LycBQDi_MhWohohXVcFcgFPbUlpRJOYy6e6ZsWOVcMLn1rty-ftlEHVrigUchcuN4qUAabtNatB9aTsS1tvPst4TeDdjN3bsk0V6uNlX-cnlCupP8PunttUVnuh-gn2pBgUhjZFit-d4h_Gx3C7o6SacvY1ECEMNvS7QPnMxR84TrzuACeNY8M8vG4-zEKc814C245zMbcfLM6dCS9yII57u2ktEDXppqw0VGuHTUOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9cA1E7sn-nNCA9jf-hLytv5HD03V7PbdSlO2Uhz5y-Wlk6fkg491sdlpWncPeoQ5QgdXgbv6xTE_BOPj6Qe9469gc8b0HKxBGj4GMBsD08p362v6IwMmRUTWP0bo0MpSl_4UuTttcn8PKKeoM5ccHghX4T3LKyyLZMUIp3YDl7s6Bp0NS4i2U1VugZoWpjBa-ueopZIlviWjf_m48ubPUQPNRB1SyUvPt5xwTzS5JU5EEDRopVd5wv-HSLCjORNQLnf25N_1l2GAMs9LHZIrFwi_XdBDAHnU3_vh4uLhez6IE3xdiUbnjXj-SLLf_-KBwqRYxns-9NqzCLpHrcSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQWnjN-oitT_q-wsYz5XrnsP0JuNMgQC7DeoRWxggNuGtjIk4MQ6NrxT9xZV2Wu5Vj1E_1il5lBRCznC3p1FFzU0lwnWdRcUgiZTS4Q8_BInJrErqc_lEWb8jhgv3hA9ieQo_HGSc-DAZnMaxI61oVJjHZcDR2JtVCH0UDSsWxzAnkNPcWdlPU5mJJmVgeroNbdef3vmqANdVly9oiv_e5ysT50dxRzahGbnMXxK6bXyiVWFQ4ohFL_a2rQIQCWlu8ilP30_tH51mNqQ-3gTOAOfehcZLmW3ANjx_KyYJ4DZGHizQN6jDIwpGBVrfjmgvZpdPv_2Mf7nFgQlnHimMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbxZtjBo8MHYj_CzZlU_JY4oiXe1v1SQgS4Tsx6MgmgYvlA9o6TQv_nnfHaamchLqesAIgUSuhr2PYef8b-OrDUCmuAbLuOLLri7ocy3tSMYsjefve6PMI24b0sGNbTIOySHT2R60AXTVsGgthqzwHQFiIe3QyA3HRi0Vl1RWyP-qwqZdodY5eduq6QNdE4ciBUw4WHLLTygNNvj3B7P-xpo7RoocFPRdEUuRJx8-AlNNesTHzvACH43nVO93C1bBIMUYouttRW8Ehi6pMGmsE4gjP35i9Eo9aACHLm2Eb8ChrC3M1WcsNcs-CNV32sRgPR_sDVPmarohCW6IbADEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsEKx_omK7QRzdzED3yCnfGcmUzxjgXLTbO_huRrzOjLEpfc4W2IajkGuAP2p8zGtwdYacsLv0rhVn5gtyu31v3wv5TxbyTe6vqSDC1iGrYL_xNaPPquV2z8yQB2AH_t36w-qTVRrxbzc-wrv6FWVDj8skPkif2RRVYnnpIYkjQ059EM4OJA0wYNuHLehY4n_SestmwftXDPqi_3E-TE0UuOc4Sp5vhlVk-uV507_CDO-t5ULk1-s_wpGL_6gkIKZKrjJjZ5l66L-9zUXcJDJoYH1Zh45XX2NAbryspABtY00DhgWP_Opjz25CioruSuh4DRPPwosdV4P80j5221w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52zAoaptBA2uZisKsrNOWGUqakKxq8ArBM8561dKC8MXJwhhuZHH1F4gLpJikvdR7T1J3nUTFLB1QB-iSbMR-e5O1kD4ZRaW-Iq6hfZvd8wubuNlclVyPBaJbEXgVsiE-cwn9rJ04YMZmjRQkwpQ7t3NYBdm0iOX4Kbx13YbastcG3_EmmnjGpDn5IrV4zm8c53KdT4K7KvNSOQJhsiBDz5CAYtEb6gVVpLXC1UF8tDGUfcOmq9inRk5nDQikr1nBDgIKnIkOFBF8PiLNoK5fXkeiAp5hxnaBbRAa9G9bN2-X3pe7KME4jC_Hvapkdu_yh7GKJR2AiV8e_K-EuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr3pfjmshehlFoNMm9ZeEzhq3j072TZwb4RzqyahGwimX6dz1DLrtOsmjM6bOC08NyoouIwaPqfn2lGd4og6qh2u_MyEt1ImBbA-9S2ooCaD8WYa9MFPwjU6ga2o3WCq8Ts0dt-gl9LzqWCFXV1STfnv8l9y9A2CKQb7i87g-Iinh0bJnlGcgoP2YDZs1UnlEs7HDUBo8j8i2_Zg6LKP7YgiArpeH12fsdmQPOfUwkxdfISfdX5EhrWr1YlFXwTmPZTlb0loIHIEsu_82HXJVOZMPiZk-CBKPLY3QAPydfkGu8qFjKErNNa1_KRjp8pA4bnEKKr6KMyYWWJgNy-iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY-oJvfUP-RrMPr5vPZcZnat2eG-IXDw22NWuJ6LCZLwAZGuAB663Npw0BKnKnwEA3rNUp8rIvmXehW2AmncDAGuLaeeL5GkcglnYXKxsS4PWOEeGlJ6elYmVET1b9PR_ld4opaC2Bcf66xd6Dfb1LNJ62eaJyCUHBs4lWtsKFCsppPgSYVToE6flGXnBR2UU8nKtT9lfVXQ06b34rHgj2U_jPUSrDIScUsV02rPilRse8a1qZYUPxnTHkfWAXDILeseQB4jTQkmakCcH_ZuGeKDsgBx8ZIwl0Cxjq2rzLnLyTYTmnqMW35Mfja6D8mvVzlK8wZnPaSxbPwEWDi30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZPf56BPrf1-59603PpxyUyHKwS1TtYA25wh74iUvm2KUSqMN8yGxWe8kX9XHEktlt6qssdM1pQ0oaApPzPgG20LS3zgjjMVqMuwrOf4OFcUyQMKWvtgM6QHtaRA69co35Jjv4NHK0kJfns1Vwc3EhOU2_bB9GBuHMzilqFdflKLQ0UDdQG1CgAFr-9bbDaytNnGKXKKIpBFNLFteuFzEoCurpSzpIhwPq-Pfy_iWiMHbuIUofHLrqEJeMT-TZ7R0rlljtyo80QnVa7It1mZXxZgxK_ff0L_YTpwp5FQVMwKpoP4OQQE8R64zA7qYHY1AhZV6TY8FVIGlTsIlwhJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9nui4J2MXCAD-wPyIILDwlUAdfwwnmNehorMaBejHc5OMVlMhhHqPmHEBWtS2uVkc5hXGeEyvWBnJswWBzYTXOqxiRgj1CtHoWmtPqV6zjSj3zKH_QjrQE3TQG0emXVBlXS0b4QQihYs9aRs-lNs1i0QDQTz57ugWbGiTvd1y4upd-kilp5qz8CIgjzQLZwCZgbhREtNNp2Edz4f3kLE_FuY44NQzlWWjUNpDBjF69gc5RBDML1pRoFoP_jJzgVd5_MTVcCfESuRgKKvY7T7_7o7aTKacbelpmRf7rB2ckLrRs1QotdNZjr-PCt1vjwlhD4xT-I42uw-Q9mdhvNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXriB3_oDatSFPsnds_or5n6p7Ce7PazTJ2BLC7T1aNb8kQiiWuyBYtx6DHPqRtGVmYsBXiK7oPTSCUtR0Y8olWe6vdQst5BAaveOHX2K425YF7KSCraC8wYN00_jV8NTV-PdeQHbinDCRmk14C5VTvk4OIwbA2NiJT9qEPatfeDi1g4RBbnAYRIlO-f4Cj6rUtDUX49wCOT3kub6HfxBru6PcdOZGKy2K2heqX10VfqmSBCbg_OVmfYkfZe9bHmOvgUEjtfx6wA9ILCaUbXsZ8z1cY7yQX48x6rGo_lYg8f3JfW4mbfZ5fC0NaHbWpalFxokUNO4IGoa09SEROezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg1ut-ojf7_eYoAqyit8xCS4vP68JN97WfqtjBoZaejUvpnJNL04_fn_hoKQekApc2hMEoAZikBsoDke_mmrtDH_3vt7A7-DdP8WqdRRe6bmjVjGo3bPLj9b2ayy1SacTLzZQNpOBqiF0qGTXC0PC4WmqRUIB6on17RsJr9YoNc7ad_3saUlbWvp3FIvs3FwGxsyFNMQkSnvKpixo5DVAIJcobY4Xd-dt7KvuKZVSqpOup_aqVyYO86eTvKHQ8lL103npU23RHPwjaNZjtuLGpVGy8AxpfxC6wwQB65U-43P1m5KsngikPhusT05-1Q36V73Ho-t--Ed-XsbSq9Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkv8Jr9mvQSqtIO6vUSZoltkdjsDpF6Zy-oli7vV4LCEyYEacAvK4AfoZ7L47ECOin3uQhOSxi6LMbMYo3WU2hO5KZNDAuJSBAYJePXYj-u-d3Bjw4p4AKHhzlzoRiFicX-GexdyordzIDawETCLOwDHwucgJIXcs9gV6XWh-NuhCkGb4kfxFasSulg8_reCsoHy_jP7YvKXtcAjiw83TkpKC8daNrplLLcf7FJbPBGHCToBo1sOfkcSSijTHGZsfxyS-xXJbt_BszvHmsFhxO5tefZwYdhM_-ul9puGCihHdRW-qpXYHMbPD7hh7z_DEkI7lfF86Gaizja1iIw-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUwJkWcVcuBTWVuLoX14RpQtm9wpX6E2014CA1Mup6jeHDCD8vz3fi3H2kRaFPDMMyJSgC8ftR6JF8ZkCGEnRaO6zXL4vUejateWa-mT0GAGodecmNTf0hE-8CTEy3ujxYdmndBSNKFxZPPh5xZFXrcxPqTMOst5IV5mQ_vS8FDi7w6nCXYEw1GaRfdC6HH4MoHIANXKjeEq0jGSWHoM73hpO1yFrxrbW5PoYmJaK1q9Zbf0ignn-nH_J3aCNQqW48TUmVFe_KOhMfwHPJpr8Tu7BUr9CYtcmLbzX-K07qJGSaA2T8-jW-Wp11Va5gtgSGxdcqMvoGhZeKUgiJuF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdxRHvl4AuFTGi0lFdtiVuDCFaVbRPKqFCqfY1W5M-22LBqOm98-s_-UwFT_IOTfjAw4jM4X5B6NsYC5eWZRc_aBAm6lR-WwhKxECgwnluMiG0EP7XF9WKJUldbgCoJh7rIgJ5i_CbLz-AAPzJh59cEriatfNbxGRCOargkuABsilBRG1aaVKxcx-7mJb9Xrn7kNqr-TGP6HL0cFpEIC7L9MALv8svbhl1NmgttEmvV6j4OrqivsZYZK559QqcTmTbBAnWPoTXipTDZwKq1WmB4VXC2fBTfEBnsQmtb2edHK3b7DvRRW8F2m5NlgiV9826opW0fb_85m8BWc1JXRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVYm1XZmqPp1CqnybvtEzrh252RQfb3r6aNOInxVkfPzHyy6Pu9ZNYCKulLXemF1MObUbjYwUrqsYj0IRvuiMHfM9Hi8-vs6NakjEoTF-CkqiwPlmeXitc9zl_k8PPjeIkFqpjv7DAk_PWB_3ouhVDwBiAfAPQu99E39nmgtB7VGvXZvJwr-_uDvGMiw03XRzNY-KyiRyd9xvxkAgv7zHKxcROoEMWsgcewTG3GJhZlVdJw3rvBwLb9T7PhunId72UU8zPKuWOV3Xv3jJVY8s0wGL9NgWqggym_g_5BLaVvSg8rYnu9rTKcwRH6Z7kztj_CFyrCLm0P5zuGIxdmdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlH1WS1MncAaHiLKdWC4JnFsaigi_k6GZ6xQTDVdSHEgAgddci8_1nuFXwZ2Le76nxfgeZ9Mb3xHLkxp4nyzUqiPErIqxN2r7d6wSSbu6m_4BXj3jch3zo0I5nboCAkyjT9CdEFlyxGA06WY36hnOTrJ9KNHTPzCxmr-fUl1MQzn6SNxDZDEueutwl9OJ6obksErDo_swsc48N-OK8xfpZgEGG3eUywtcUOJO1diwhsq1P7GhlYTJkqeJ04aBRlFilBBn6oo3SQKk7EnZObW3VJRu5Vl9yjvU2FEFDtIN3CafMUdy0leN-r4ctz26zZEIgVO3sxoZ5mlXxGj8JAoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxu-9fyd2RIiWold2QW5gdk4rlV0t7BihzqycWodwiiDm-EG3iQZmWfUKvViYvpC-VbrztQD5VDL9JloqF8hzazBzADNYEwgeyP4L8qNKKrX4qIzMlzQiujZseCt22yCexEUwzT8IqhiwmUNqIBp5fipceuhDMaXGWmMaqS6st94LyWVeVWRDMjnz8VpFed-5x0W6r0JwGJp74Qe29dYl7dWQFrrHx45Q-qNJHfKrNAzKlhpSL2o30GiODUZ-cjPB_qXno-uH2BhrDekJJp_jXYkEbXMfXADi10yGYNeHxpCqdc-XUiZmdklQiwWgBbgk7mQTCkTR03Z4MAOXpm8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FebAB0gz4VNt-xNxTdWGdYUuNseHzfKBjc08-quqkHyF2y-AlsVaFu8tkFLaUZ_CkJU9EolDAc6rAvRiNyKqpEWvhcGn18TbDn8iGI4lwXaiTqK7E2c3ccFWpMhaHOIQM4GrzqE33DEO64Ui8vClazvUKHvI7C8_gh-u2KtAmI6YpiV3IXFMnWUYcwT5VIuWBJ_Hi_sM3EXZi-Q__9KAT0tk5maL57B_S4TyqLobLgo-X7u6Tph4_UCrJtcGZHCW10Sjqo9HHIjZv-R3IFU3SJgNsqNo8e9gtzCy27ihQ9XKo2HI2XX0I-G73A42XXue8V6jZCH-cc9auVGbDvBavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=KAmgQekzyi0PnoTNqbgf8tSh8e-VcRFsoxf_2Wx0UyBDRbJ_tj3OBbEnXyHC9VGDA6UgItys3gtLahFD59sUM_rxVerxMfuYjCe8ctFVXAQDL9blp0tX0tiDjpn5-GQknjrqaPS9JfjlbysrsBlolDS3g_sovSjodkdNoW7TuDinDKnlfHnwMHQ4Owo--VTZUhUGqwXtacNmfwHJlstEoEKjjKPkek55mVTnuKt7M64kd0QKWF1h_3DETPbyjdXP5-_sm0Lkij2P5fIKuACzecMra-d_a8y1qUD9ajgAZY_d_5z2drI1f0UEoc1YsUxnrIFPOEozLWrpqEzoxs9z1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=KAmgQekzyi0PnoTNqbgf8tSh8e-VcRFsoxf_2Wx0UyBDRbJ_tj3OBbEnXyHC9VGDA6UgItys3gtLahFD59sUM_rxVerxMfuYjCe8ctFVXAQDL9blp0tX0tiDjpn5-GQknjrqaPS9JfjlbysrsBlolDS3g_sovSjodkdNoW7TuDinDKnlfHnwMHQ4Owo--VTZUhUGqwXtacNmfwHJlstEoEKjjKPkek55mVTnuKt7M64kd0QKWF1h_3DETPbyjdXP5-_sm0Lkij2P5fIKuACzecMra-d_a8y1qUD9ajgAZY_d_5z2drI1f0UEoc1YsUxnrIFPOEozLWrpqEzoxs9z1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQJD-XNYoCD_oJEgupJkYKT5fCRWR_u3-gbc2XB6ZnaaU96gLyxLJ7wAY_MlAkLyi9JY-lpE7muqsV7HajZDMdIAJ1whXThov5YxhpEgUw9blQ5SsTwTe4X_VpNDqDrwIVIW04bawNgcu1MyerrwxMI7LnyVJxbTDvZelr03jYJJU-AUb9uOv4FJxF4zzyS6LURy54VJt_fy8vtyl_MLrTCEvJKntCBsBSDWC0w47tygB4Va2wmnNsE_UDHQ6QRSOZDoK2AWNsJriNWQNxMWoaEueJ-gw0_pt9wXojYIji7aj9qzYFGqz5kbKEBvq9IJ0elrJEmtWaL72gPfncIqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOU4izRwtttGoVd7ZzI-ffRUkapOZMsM2q0T1Y22S4UEEfJ6T3biZ98NksBKgTD60AIZnPgP927EoukPDdaHKcnMmEk6Pfw0dtnli7dwz9SeJe53WK2l2Tr22m9bzuDhPjN1rinnW0Wj5ANPqSGHbotFJHxRD-aiEunTXRERrUjIpPsXoKNEdduMnayjZrkqxPUQdud96K8RITKvxZuNzKyRDmTbX_7pwtf5nBeSRS9bnipAXFsSVnHo1CPQusjFdep-cnMkGDA8CRDt8sHjyOoj9EnNaIZM79AsHLembFAA7w80s0FC8sy1CKGzHh75u-0CHxgR-cvv7QFFF-Mllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM2ZqFR01UW193olFqzzc50aD2AV8BlaQ0v7HWo4JaB8ye67CyfEWlgbgKmmCxvVrLzTYI99UeIssUoTG2_ewbcVtbDPaVmsUAu8Z-xbIOUHfiJ92j_3Oqo0IHlR7ihBlkDdBZJPc-S5NRs4_vUDKdUTFFZTxow7bClgJE1Uv4ykHoDXgWH9eS8FM9_AqgW_xiO1O9GR1dYCDuzAH8Z_vTvn0JqgltZuoFxP3O2XjNKV9_sZj5j7JVVMxFWh_NuzEBWC9SClka4Ca2_MeSytfEGYR5P9R6tmnt-s-U9H7tcUal7jynIaK_CeU3jSQyypSROhBscL27PTEC0NLpFQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC4Nv3yIZUk-UaBb1_0ubQSGvMqgY1qE7b5c6Oe5FokN0Ssm-sNvbg0TX2jv01_zHOiGlZAhaKa7M82mfUOJAZfjBJK2sU71xLy5BufIxe3_59c1Udjzqx8cx5TFkak1unMNjhJ2V7r_KS8KchccDVabeY9FkRUjoCG37JM_iFs8Lo17SGaxAkFhok-URNVq4wmqpSgzEDdMVLauDx3kPAz3Xm5ZUxFaguErDGpnAXRlIS5RUDduS_3oAAEiAJpr93V1QC84ITFQdrNUU-7YJVRfx5g-C41GB1GEZlEuQoJKIPXfGcNdV_g9eUvKop_Z6o4x8zT1quA746_MMWSkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5dFpLc_nNPKG7X6VzAW8J3bhZKYabgq84077WvAbCYGDPMsCcuR9PpByjUYGR-RZmIkaB1I2OXTu64fgSq9Nk_MSzh4INK_fLd_x9_042mJibS_y0I6Sufy29g1t2aOPIze_ax2VQyQYxW13Z9gDypDcRRY7D8dviRTr0QazCBPEP3hxeyck7norD5JCoq2vRaxInwYXshwC7tvk5XzrJ92D-INoJoI5nV5O6ZjTPRYpWQcmt8bSCtewh5RocybqkaDXDYmk2YhF1eL2IpNiXv49IOiI4yNvAf1ZSMub_gG-CEMjRFnbgcCTxkScoQFSkkRoxOgEwOpil-Tz_Wgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=vupwD33CD7VLW83DOOIWKQLpbtguCXTLCGnN0w-zJhc_MEWVgpky3jJe1RNco9cwTt7CUBBkpbpJ_6HkfupzMAYGdIsDrSEUafjRCQifrYwPXqMEXeGP5bgdyZE9IBm2JQChEwKptmtMOGVdjmu12cQ5fcqs_OT-pgIqj3WCWG_jQwYpHw21Q8CPCOxwbYD85QEDUhR66HA1XSKxTMrmQHP-Rd6JnphXwu_4qlABQoPse6uQLQUWUIvUEDKp0trVlpfeBbztqRkNBHfE0g88X-EhKj93QME5GWuhpB384mJ5VPWCPqHFUFUlYz3IyTbWOS_JbH671gJgLPD69pdUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=vupwD33CD7VLW83DOOIWKQLpbtguCXTLCGnN0w-zJhc_MEWVgpky3jJe1RNco9cwTt7CUBBkpbpJ_6HkfupzMAYGdIsDrSEUafjRCQifrYwPXqMEXeGP5bgdyZE9IBm2JQChEwKptmtMOGVdjmu12cQ5fcqs_OT-pgIqj3WCWG_jQwYpHw21Q8CPCOxwbYD85QEDUhR66HA1XSKxTMrmQHP-Rd6JnphXwu_4qlABQoPse6uQLQUWUIvUEDKp0trVlpfeBbztqRkNBHfE0g88X-EhKj93QME5GWuhpB384mJ5VPWCPqHFUFUlYz3IyTbWOS_JbH671gJgLPD69pdUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=nFAIIwvm2GOvz0rj_lT4d3gtxZeGuunTeQcGvuiSGyLNqP7f3vJHfs9MWHL2USUou_kgKvHZGD7gxuzbhfY_PFTKLEINGj9pwyXgtFZ7HNTX9vMsLe12RSkGyVG9INdR1PipZFRKuMT_5dwCsg2PSk0YvX-WonmkAZ7p8TnabnA1V6ZKeczbjb1Mq-i3as8qF_Zdqb2--oBTDzpPylUIW4oDRuAgaqZ5jNlW-x-f-tWIEtp4YCZNvmAbX_hwZsO_30r6Q8Nesmtkp1Pnv2MimZukrMp_FOIg22BbtJb43sqz0sviP70JpJmmo1D3-I7-CQiXQzo8gOfExoWFJbG6ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=nFAIIwvm2GOvz0rj_lT4d3gtxZeGuunTeQcGvuiSGyLNqP7f3vJHfs9MWHL2USUou_kgKvHZGD7gxuzbhfY_PFTKLEINGj9pwyXgtFZ7HNTX9vMsLe12RSkGyVG9INdR1PipZFRKuMT_5dwCsg2PSk0YvX-WonmkAZ7p8TnabnA1V6ZKeczbjb1Mq-i3as8qF_Zdqb2--oBTDzpPylUIW4oDRuAgaqZ5jNlW-x-f-tWIEtp4YCZNvmAbX_hwZsO_30r6Q8Nesmtkp1Pnv2MimZukrMp_FOIg22BbtJb43sqz0sviP70JpJmmo1D3-I7-CQiXQzo8gOfExoWFJbG6ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=lwxzddRgN0XfNHh_1HyQQlAKi49ji-PDfbt2aDgChMf6PqC_-yEzI0J49poLlNsLIMPmTcdAKCMRE0fqjIZLYUYXckQ3KTiyar9d-20x6g9A-VGNsKQ_iFSgIAAgPT0LrAzzTfqAEyS6P4MxNeQtL-rUD-vXZAEFOnT39pUS7J09xD6FBi1TXEIkBR8gFBx2p34pSW0gOqHrJK5_e_4vOv1MdplD1DioRAbskTmUCCEVlYrZfS0CQHHA3aGaY9iJJxPeWqaXlraZ6y-PWanVEb9MsksnYpaVVMU6bTE_eLfnZmDrxEqzS_XfKiy6PTLgSy2sMGns7Xw1QDKE_6QJpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=lwxzddRgN0XfNHh_1HyQQlAKi49ji-PDfbt2aDgChMf6PqC_-yEzI0J49poLlNsLIMPmTcdAKCMRE0fqjIZLYUYXckQ3KTiyar9d-20x6g9A-VGNsKQ_iFSgIAAgPT0LrAzzTfqAEyS6P4MxNeQtL-rUD-vXZAEFOnT39pUS7J09xD6FBi1TXEIkBR8gFBx2p34pSW0gOqHrJK5_e_4vOv1MdplD1DioRAbskTmUCCEVlYrZfS0CQHHA3aGaY9iJJxPeWqaXlraZ6y-PWanVEb9MsksnYpaVVMU6bTE_eLfnZmDrxEqzS_XfKiy6PTLgSy2sMGns7Xw1QDKE_6QJpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGLMeLzCV-pI8f_C4-3oTDvs4WLbuVq0M-bmlA8EOdb70St6Ua6rXt_r5X6TWt3H0Fy-g7xheQsnpBqtrJ_-YY907RVTjZHbzYt6v19MpD8MWJDpEsRQRTsfv_aBDECftG0CZx1iN1-xP13fz53dCyhNkGA4b0lH9rIbrwQexisSaVwwshb9_4jqi9hB6We2G0-AA89MeuWeEedcgItbdMMD27HtWyJL2y9h3RnbhT4Tq40FF39DKZ7Ap-L_3ojcy4Y2lEAzo-liBgBAqA69c0WtO_vYnttepVq-qkYddq-cwTHIFa5Vg764YH_7FLITmbqGZE3H-FjBSZMvUQoyFCo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGLMeLzCV-pI8f_C4-3oTDvs4WLbuVq0M-bmlA8EOdb70St6Ua6rXt_r5X6TWt3H0Fy-g7xheQsnpBqtrJ_-YY907RVTjZHbzYt6v19MpD8MWJDpEsRQRTsfv_aBDECftG0CZx1iN1-xP13fz53dCyhNkGA4b0lH9rIbrwQexisSaVwwshb9_4jqi9hB6We2G0-AA89MeuWeEedcgItbdMMD27HtWyJL2y9h3RnbhT4Tq40FF39DKZ7Ap-L_3ojcy4Y2lEAzo-liBgBAqA69c0WtO_vYnttepVq-qkYddq-cwTHIFa5Vg764YH_7FLITmbqGZE3H-FjBSZMvUQoyFCo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzwOR3b4hC3-pdB3DIdD5ZkLzseuw5iUnExB8QBQ5y2n_-IpI2_nj3xhkIDeZ_abf669dzquXNBLJgJiXfterypMZ0wb28S7dBeXtVuPsK6AMSfc5v4yYyquHPghgTGkl4nN8zzIfvSAxrBeVaoMF8J2mLo_aPmKYrSsMUSwSnyWH0R71kZPQNDpOxfHw-tQiiDDB32ZgJKW1Yu9b85DtL0d-2zE5HzrJn2kaqBgeU4zuHyp-mrSRAgnMA-Bd_CVbQlcCcD-QZ1O9SZtc4Wl1PNwfhXxbphvtJgLKVjnyTbzFSMAciarLurzlQIOo14TFeZNic5J25GXIPbIdLh8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZRvROokEk3sch5Tg27rX5fziyJj4UVuPh5NlNaevSuSePxtbxHh-56OZytg75lsfqFurt2I7SLg5RN0r4ztjOMBEQwsm6Z6tTdsKw4NGc-koJL5oB8XoeELSPYBeECutKLxU5HUmPE5XyV_WVW7D0aVcBz1D-XZMs7hdNeQwl6axbfm2TcaHo6_f5IWkx12P3uSwVw4DVfVqXgKGNFidlu-MofgBVST1k2wa45BDsEei2hFiuQ6VrWt0lKPzMVvJlhvSRFNKjQevjrVQsf_dwIrhH4Pqcnx9NHEJV2LGt8Ybs0vAKUjrxm0yBc8Mw2l67wmLjhcbR-TH7TYQJ-0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/II9JddlTLctyl_SeBAiQrdGmarBJ_Ty8ykSal3iAi-IGKq2VDZhK-NHI25S0fko34ACsTpHE9eNroXN5dIlrjOXRX517qOvbCblTiTwlo6w0-RyrqERDYMOeeK-hc4jziKPlIYVzFKyrzDDNNvBG7_shg4RlJlnejmjq5nzZqLZ3Lm40fA0MCrZxOMPlAL8w-KeH9z-Zl9ESfM8eBvSIbFuplXt0OXSgOTIxN7scwjj_0nT3WUkjYDzxzH1EtcYxDQH605eFHQ0PdsUtAWXqwbK02RPL0y0abtEmPw4aiYFcfjjizZNBFcagWbRzeeLtT4eyYb1tlA2cCv_2w9OtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYC8TqiI8V_khcnhWS6zu41awp2cJ-RKHwR-cjHpgDB-8nUQn3qzQpppgurj_xK3gW9vFBCSWTMcMhJEKGTG8YA9NWbVJlqMSfl-4UKRzLGgTvdAJUTBgEpg8TsWaUMOZJPGygjlq-kSfFzfttWvVdFBYcUBxnNr9bSgBs7wLik6iD2Ub83K1RYE3BMvZSPvVrCp8ZPaUeOdQXfBSmtqHaqgIo0fKneT2CDlQ_mzYKgUGhI-u4MwiFT6FueDeEgygSXS7Imhs8Vy9znT8DeFDUw-5lWFWZcPQ0fvG041CPD8ZgUlAFpSuDqf7BDc0V7uucx1ZVIvWDbsLw4CcHFPbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=lfshpq7R3qpcXFbcSHQQkgqV1aq-jsNxPy-OiU5184IqYRiy_jEpSfsbcAIKtxJmjXMSspSRQKvfyNowks36Lvhrf2TQIBO3yfbEnFaN0MqiXK-wjwItv4NdvpVQRw7x1beUPUg60x00vCW0jgm-JHD_cY5UFGNpRCoX4amJYXe1a3o9DphVsZcxV5lO_1aMsLAfi-wT-Ew3WyhKhIckPTYjKT0mYX_TchvRMqkF0xC4QVZIkod7KLRSjy_dYsDNCJjUir0xri5B_QdEwE5G1jb3qwPmdXycRiYBzvQNKhwMi3PlgkbW0TLaH3gfGasoEZDOAGFlCIc4RT7vjKeyZ0QeHZatQRfqca4UeXk2MnBQ7Ym34DOhwe83Jb457wov59vlkXBWmQDC5ERgRflccrjDZjbV0-pYU8pFutLp7xVLuAH_GolGQVOu-c9skefooTv2BVctZabRtgFsbxYOerVyehnJjmewqp_iUIBSDEqiEVH_MWdUR9ssLFEhoRt3BT6vBXA4a0JB0G8-DiWvr5kQ9pCvYiErifmTDA4e1hLpB4_XMPcYMYoj2blP3lUGt0kVV5gAuJC-d68azom92Pq7nYoyIxZGFboIoWxwYOLzBp5Aa1mSXCRYfNWuUhbLHTe1qskDVAVbjWoKSZ8ORiab7KdpM8cEYZH4IP3GxqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=lfshpq7R3qpcXFbcSHQQkgqV1aq-jsNxPy-OiU5184IqYRiy_jEpSfsbcAIKtxJmjXMSspSRQKvfyNowks36Lvhrf2TQIBO3yfbEnFaN0MqiXK-wjwItv4NdvpVQRw7x1beUPUg60x00vCW0jgm-JHD_cY5UFGNpRCoX4amJYXe1a3o9DphVsZcxV5lO_1aMsLAfi-wT-Ew3WyhKhIckPTYjKT0mYX_TchvRMqkF0xC4QVZIkod7KLRSjy_dYsDNCJjUir0xri5B_QdEwE5G1jb3qwPmdXycRiYBzvQNKhwMi3PlgkbW0TLaH3gfGasoEZDOAGFlCIc4RT7vjKeyZ0QeHZatQRfqca4UeXk2MnBQ7Ym34DOhwe83Jb457wov59vlkXBWmQDC5ERgRflccrjDZjbV0-pYU8pFutLp7xVLuAH_GolGQVOu-c9skefooTv2BVctZabRtgFsbxYOerVyehnJjmewqp_iUIBSDEqiEVH_MWdUR9ssLFEhoRt3BT6vBXA4a0JB0G8-DiWvr5kQ9pCvYiErifmTDA4e1hLpB4_XMPcYMYoj2blP3lUGt0kVV5gAuJC-d68azom92Pq7nYoyIxZGFboIoWxwYOLzBp5Aa1mSXCRYfNWuUhbLHTe1qskDVAVbjWoKSZ8ORiab7KdpM8cEYZH4IP3GxqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI2JKl2Lwf64JWh7h4KvYN34854mYEKex824jjta0aqcAt0JfPgAq_eAQ8eKkN7ipwKs8ahhhMUuKlLVojnAz52yvwwb7BxqbgGzdtC7bA0gOUHmnPl0O56qP89ptxHsVCMYZhDQqhFmGPPbecqiurBMzA8099OPHwua5T9XGJCV1qLLedfV7LOErZHZlcvglEtqfFvrB2D2WGSCbahZ2XQxW4tGBlpYj6ZZG34nc_M3cy5QKuhIyHg0W-XW24_727S9HE3moKq14dp8SPCZigLY6YD3d1U3hfxf_lI-X7v2CGA5peeXm4Tc0Pn4RCNIBzcAaBLLQ9zUxbotJppJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=W6SCKuWTd1Ohdn1XLnPYYen02tgoTtQGfxwkAwMPwQmLNm6PyKByePF6qo6pCZRxDCfNSIk4_U9o_SH6uul3atdm5kT_Yh8dHkQlEB6872howt21_nqRjeqFb4t5IkiUoBlNR8eK5XKVAJ6OZHMROlo0jQsBOCceCQv799QMFDYjD81z4x3MLn7rmD5xAMKTZ0_Fd7DtsR_TwTT3tOcittONxRBsUSZLUkTXBgARYrfenV1Xqelk2voiEed5vHuR03yOb1aLgDV_8NsNMbAAZwya0ohQo8VPLIeYqawjIoCjzdh8C6G0XGS56dNFRBJJl3Hed5gDZpSePMs5VqkxKl22ghlPT_W7nVi1DyUSVg5MK1_KB-r6UTIg0wKkkruyYW5gc20HMJupPXbOi3Ria3Z0ACjSWiphZFV2C2TCTcm-6P0KIMX5m2J4bG-2F2fO3w2twixMSQ4kc4yJsASZDEW7pRvz6qzYnDvBUivwe1K0ShmcduccYWalBnQoTAyLjL1mwXnwjgCAhdA4bMzk9S8Y4mXrPWj_8jNa95HkAW8yxB47cxcB4bZKIYZ7nuNW-FZt_w9L_zN5PPfERVBwGf5SUhrh57-eBrJMXzIrkGYG_m6J1xJ1C5Nngm-0TWzht1pe1kaXqviZUGdqVD_WIGy6nGcRQuZMQbBYWzuXmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=W6SCKuWTd1Ohdn1XLnPYYen02tgoTtQGfxwkAwMPwQmLNm6PyKByePF6qo6pCZRxDCfNSIk4_U9o_SH6uul3atdm5kT_Yh8dHkQlEB6872howt21_nqRjeqFb4t5IkiUoBlNR8eK5XKVAJ6OZHMROlo0jQsBOCceCQv799QMFDYjD81z4x3MLn7rmD5xAMKTZ0_Fd7DtsR_TwTT3tOcittONxRBsUSZLUkTXBgARYrfenV1Xqelk2voiEed5vHuR03yOb1aLgDV_8NsNMbAAZwya0ohQo8VPLIeYqawjIoCjzdh8C6G0XGS56dNFRBJJl3Hed5gDZpSePMs5VqkxKl22ghlPT_W7nVi1DyUSVg5MK1_KB-r6UTIg0wKkkruyYW5gc20HMJupPXbOi3Ria3Z0ACjSWiphZFV2C2TCTcm-6P0KIMX5m2J4bG-2F2fO3w2twixMSQ4kc4yJsASZDEW7pRvz6qzYnDvBUivwe1K0ShmcduccYWalBnQoTAyLjL1mwXnwjgCAhdA4bMzk9S8Y4mXrPWj_8jNa95HkAW8yxB47cxcB4bZKIYZ7nuNW-FZt_w9L_zN5PPfERVBwGf5SUhrh57-eBrJMXzIrkGYG_m6J1xJ1C5Nngm-0TWzht1pe1kaXqviZUGdqVD_WIGy6nGcRQuZMQbBYWzuXmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8naM2uPPx5E-Wmcunk4kSBbeislDbHEEIBpGwkBYvTihP2_KJ1r1ZjCcBRcl423xm3c97wNseg0MG9KtCaP9pR363R0vRrB9phHNynKAZ11i4TX_t4NWTuYj90zmK5h8t-3CVseTOulo_sToDcaH_EGLppXajM5obTTL7u8J-LoBJkdifwpCv9xQ3C7_i2SGz1iL0r9Xf6Z7wa5KVKrjxJEjbZtuOm85rnsq7lVBESV_RmLqo5X5rbJvoyUIt_Mk_L-9dKXfJqtcAkBPJEQBXYsKAWm8Q9ucQNsavly79duURg0brKeRpsbpi9R8ouZemeQQduTQuDAGPoWAxEguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKa3D20X8staNmVyScw51lRIHU2wFtoKJvF4xDk8a81a6-fHjue7aMhPerkAuQ131fYElezGGIigzjCcqH9MIPcn2XeFmudNuhT5Nn2_onH9MHa4pLK-fOog5g0vrhQSBJm_Yn0-Q1zY4flIFUK6MIof4z_9DxBCriU68bPhqTqmvjWmKoexCK7oSS5BB15nwQFYTMege41xfATwZEaUXxOOkFs9QaO3KTNuQFk2fk183Om2u0JMa-9eqp1gysiSOleCTrWDktrHccjm4tLcCgibjqAMsRg9lKXHXbH9U9DzIHclqsgrJBcnm3taBuD-h8DKU_wrpsuErgkkce10xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrrFV8OOR5B5lfQJiY201IiukdBNchGSA3YT1w7M2Gv-IH3f9ZH_fLe-uSLaxLJuBrZbpLM-MmnaDImJgFKCgTov30AU9R43oQgtlGTyXTJHLR5FrPcXjXOvJFhsZ5caTzf4galG_GCk_kAE7Gz5IprWd0YZU_QCmm1Cnd-GfW_roiBHni5NqQO-RAcuHPY9JZCS8s04VUFFrSRaiOhg0NZWV5Nvkut1TQ3yKJb6peTLqNujOuFKli5ZwF76omkSKGooVRtHPMtkN1PXybLRfP5cV_nkl9Mj8JpfdCYCYGFvg7kvrQuu0QlmqQco-ncIySaq4px1c2o0X4c6H2PNRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h21az6zxMznVwlqoggXVHqQFrmE9w3brzw55p23MyFK6yJheCiOE7jcVb_-J8fuY_P-Bx8V9MRZ4fCdvQascwfOXYlkJOEHnJP9yck5ztydbrL8p25IyodiaBWpG3bpCBsIseeePpTdBzuI8R7Q-hXnb_UV-succGwvg74gsM2aVGiJh6dDj_7fygA4zrjV4U5mf-WaDNaMSmT4yI5CDNz8GaEEnQktEapFPRjfyVig9LPZB3lkzZuo28Vc2Ia-nNBuWMAkolxGMMHi4fAoFs0f4WaQpRroi0W2R_djpZukp3p5fnls6FVhDwO1DNQPQs7OLtq-ttvxPFYrqRRTAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMp47ld2uLXyOKt5OXkJDKmwfPkXqK-UEVh9IpIelOO1z0PUeTd8IlUQsP-7WxTFVys6fkaprgpIVHv0dlHA1Qv6ej35gUFBKiUKT-bZcbmohEnavk74LOBo966FmJN9umNBJjuvHwPh0GPRWvP5N5jssBCTmCBoiXyaPMIkwDKej2RWYVlfDIbsmCGaw6Bsfx7ZebBo8HosQjW50wSg5En-zWuFx2Ko_cri-JOWFndPRrup0_yRbiU0m61zWiyhpL19W_ow9gUhfaZDab51KvmH68Mpoo-chyXGFwgFtO514VTZTrQrS_EEJXAJXrEiAST9BKxJEsDKsWVu6Ia37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkYOrcR0peJHPygmL-gBQB_tGxBhiOcajJWPVuZrAXseBiuUE3rLSZ0A5c2ickylPkizWMR0mXNdj2QYVB_GnfGEDFWAgImBcOV2wNKLg2JkO0ZeB-dISgwYGQsEDAHE4VF9Aw47IHzLMSUuW-9WxDUlnITce90v91W_Ccl1rI1eCioOgeP-1b8UxAn2Tly4kvNC1PCu9L6ZDaUZNfAJvGKG2T3EnVxnyWW9rGjF4rZdwpZLC-QjneSmb0Xcqz2e5jFo81HJy5np-3azvhY4R4tk_YaN_kVspnkJcWnITH8vODSHss3spP3v7MOllbgyhHxPJNd5b_IqQCafIHFqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz9aEg6S0QIK66-j1NbhlUWgO1XJVNIOuxTEGojt4SVn8nIuYfGTaI_euJ_nAzsSr2vL3xvQ6pf0w5k8U8GOOkt8EK1ViTtvozFC-Wr6Ud8RXUe-ly6qQ8hzNPlG7bCw_pCHl2BwmVJe5YWgrggN66Yw7x_hNBfgEYog5flSn0h4gzMUA7BiUonRcezeo58gxKa30BLdKQWOg5TDe84K2u9r3oyXM8IxxPQKyXWj0c2IADMPmAyrHtk3sp9o0VQOw3jvLDvYt8GAR4nqU-D5hrCCnvwhW135u0d1Q5Sf4hmxh8-u46t7opyEe3Xhs1N7PF4wLbFkLPoElI5YAflL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9jKI_Mn2l2BixWDfYnWhUuuCZYRYfiy9r_pLXLw3LJQbHLFHMewrTUxPGzM52gKYPgOg7UvL_ApaYEuDoEFUFUd4F1F1jp01Pdu61Chl5KCy-J3ZABpU9qs2CBhqv8fR2y0BBpf5dpvHrxe6MVwJS-_AXfwIRDm_O12MDpdaZHBG6twvmMl7k4Iyh7UPqhOGi8QA5BBMHQrr5mWmPb6ksEqyONgtF-b34aXSBnryT1MMl8zuJixYD-eqInewG5hvpbVwU6uTrWWf4zKkAJ_lhByurcE9aQbv7L0WJnycBOjkE944EtaSgQEddtxXWdX3fX5gKHTJYW23PT9udfK5C-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9jKI_Mn2l2BixWDfYnWhUuuCZYRYfiy9r_pLXLw3LJQbHLFHMewrTUxPGzM52gKYPgOg7UvL_ApaYEuDoEFUFUd4F1F1jp01Pdu61Chl5KCy-J3ZABpU9qs2CBhqv8fR2y0BBpf5dpvHrxe6MVwJS-_AXfwIRDm_O12MDpdaZHBG6twvmMl7k4Iyh7UPqhOGi8QA5BBMHQrr5mWmPb6ksEqyONgtF-b34aXSBnryT1MMl8zuJixYD-eqInewG5hvpbVwU6uTrWWf4zKkAJ_lhByurcE9aQbv7L0WJnycBOjkE944EtaSgQEddtxXWdX3fX5gKHTJYW23PT9udfK5C-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa4AbR1hL4xOGJUhT8ubx4Jf0wK6VXWzzu98BobJ1MKH7pLmrUcdtjDgsgi-kxxjX3fF9IzAIcOxYKoNCYUfHVKKCqHiiZQcO1X8B3FKdsLh4J7JGnSGyOHZJxuuKWjGS8YZWlT_vetQoByNziefFTL9A9Gqe_r5R9FA5Hcfzyscdq5e87CYppaeix1xeFdm4dDYRS3kDBENo49UV1vxeC3FvPXR_-4SJv_ikRmGXfENthbzfd3Yj9i0uZrYQMlZC5Mmd3AmRYkI92BkSmMvm7OP1N_EVoot47zjQxreDeGgDYYgsZrKbkzM-fWvx1lzzxE1nh4TmJd0BEzFJwOySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ1XlB0_vonf4hQi_W4_H0ohhPrvrSiP1JFFMLo5puU5uPoiHBSvOzR3icFrLflYLZZt9VmUHZuhQgYJtprid_cC8maBUUMBBMgSeCgH6dm1Y3XQ691rfrVo4Uu__lVd8jBRcKw1ubdStRNVAgAqOPmBohZhbjhSS6j-2Ujim0yDgpWIt-paK5rNGT78c67RbejIItBXJwmQXNAoBnerqEPxorRHH0Y2r5M_cW3JFaOKXM_KChNj2FvCExmqTg54U0lPN7eN4i4YVBoPxdceZ9dCtEyvrM0Oyf4chZNsIwS5000foV0SqMgp1ELHd-u6gEg5kk69MspQ5KKIkDEMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kavznV4vTvvdVQHvxm_S3psxOty4YP9tl2fSgT80Y5wZ-Fiw0DhROlLNjO2cL8P0pOn95l7ClEHcF7qEJhqdc5Q3PIqdpEiwCV3ZB2boFu_LqbyFIE_80L7d2_oIkw265aP7LOfk_arzEtRB6ad91Iu2zVonDqY48EL1KoUtqImQjr_7iMWmyhTq3q4EnEOE0KMvvlQ5LWK7-1dWk5ILii7C4uwYMpAv0HwfXopTbENu3jS7Hxuh8gYrKaKItSJ_ErAl6wZG9kiITrYWI_nTds-LFmWdcDgW8I5HKO_5saXO_CsnYR8oWZ6St3Lwxq_pGvMpU7qhGICHZobUeAhsAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=YJKRm13_1X51r6Yh1FD0Dc2Y13xVSzHD3cLqdBzRlRt29pIi6STza06Q4UXVNsUN8UXVKDwf51PETdDgbNK9xWZihRGPHTHe4EP9c5VSTHlGqIoJbK49cXjmbJz0ykx5QJ8QbH91sxqfS79WNoboET6amjh-e0E3L0h5kLnIV5tZwkEdg4aMboZXLhik-AEyU04ZQ1fEilbkwljKQZ1rQfmfc0AilII6rAMcj0RcZfDkTBA5Ptin_clcGvKlzrjkCuH3HiXeVKNhC0JV7jEVa0Qt6aHC-yYwLFE0BX1ywUMWGdg84AGzOQ9CdBqFXLyafb4xgA-GsAljrSebLQtOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=YJKRm13_1X51r6Yh1FD0Dc2Y13xVSzHD3cLqdBzRlRt29pIi6STza06Q4UXVNsUN8UXVKDwf51PETdDgbNK9xWZihRGPHTHe4EP9c5VSTHlGqIoJbK49cXjmbJz0ykx5QJ8QbH91sxqfS79WNoboET6amjh-e0E3L0h5kLnIV5tZwkEdg4aMboZXLhik-AEyU04ZQ1fEilbkwljKQZ1rQfmfc0AilII6rAMcj0RcZfDkTBA5Ptin_clcGvKlzrjkCuH3HiXeVKNhC0JV7jEVa0Qt6aHC-yYwLFE0BX1ywUMWGdg84AGzOQ9CdBqFXLyafb4xgA-GsAljrSebLQtOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLKoYG8D-h0jtbFxeVTCsRMaafKnvlIs1ic013xKQlswFGyJWK6fZ3AIQUyLqwo-wXX9x9U3185RkWrVXpOIrdcRAjRV4zqXxvhAGU20BcNJpvDhe-4iojQvePVBthvUAeoFBqXFAzUOmq59vFu-_qEEH8SIEFOZPGlzMJTGSf1TZKMqBxmgY_noyzfw7pWrsYZtRNP8FcU5xrKJiDuA-6dxErlfquS0lQLaDsDkxsvumKu6DoC1kG_Gz241-RF5smRPhgcYrq7DS_Gx_TItO2tiJqdiauJlxNy_vhc2PdLzUNphAVFKpR_SnhpS5YjaUOjrmv2Oab778kzkKTXMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU-5xHQALZF-_kOuRBIdR0Ba8HfqY81wnoRkAYbv4BEhAalM-NGYlp6Zim-S3roGNyAq4pWn9l_CqsqsY1jAmDv1CLwRSJK53In9PqvVQuZ_XK7X9mBxxsa6iFWjK8zMcM_Kz42t4fSD4yrBC6tBe7xrBWuA_19gH8Txw2T6axAEMUZMwVdYG3OqVwfhmP1UOuMxeABK4vI0rzG15XUNRmb_gq3YLaXB4bcKNV9CDVpPKc3okwOIjXlCVRCT14_C63HVFQPSu-65lsoIfT_K761txAnxOSUF6YQ0b7Q03Bl3d0_4dxuuo0hJJa2qM06Vtk_PQtSWa3sx8RUYF5JJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn7EqFIHMHdzBwZElDJib9v5dWEOum88cASuqcPz0nsPio4q0J3sfEkHVzHvZbGdLTwbAsdt14w3ZOaCcTq9JgBF-DJi9u0HaqntSJqxYEQWde5EXeNmahtiJaXRuEI7Ehqv2JsXRA2Q5f4Q_AccOmrIXKZd0B2FW-KvltFhw_CksmaSSa5WdhIQUdpc-Y2PQcU4e_r_y8NKggcAwt8GEuGw2-b92Gg3LW3BU8SEETOphBhpfzVnA8wiL2byIH8k5kzb7A92XukbByJOEKHGu_LY162RxQ_SemK0lSVObdCn2339HGUMSjMjf7B6NrljwO2bs9g52d13HOn2QL1SBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWfmiEC3VInjf9DVAL_ACm5hCY0prOirXV_W_EYVGNwDgA95M6Wg3LNgOkfOs0GY_Au7CZYKMe6h4AfWLd6L59Uq6qzuruRJRVooRP6tUZX-gSUUbhmJP5w0VfdZi4pekynYI10Tg5AyFZNERtprs-tl-0T_X9lurf5FFlMVAW0TXTUAMrifoobuwY0pMVHhdRyZLmbStC-s92XNRtKQe-_Li76f4U92wrGI4JjcDurxfA2YfbUedYTv3zSXKn9mFD21mvkqfpCew1mCc2KFWxqS-T4lcCgrMz4Qlhy-5k3QI-059lI3NY55EoQRoaPaSm3wGUbcDTGbSfFLu3tFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5evh-LmPgzJG-Vzm3TwgYeOoz42ZD7KV1Pe9cW1K17g-b8P3YzbYIyN8VP_H3_44LAUuCg3dLAusKAVQ0DW0c2K-YGT17w0k_8bJqoBhOEsRi-C6e_WMU761yDiwmScJYzg9X4b8CG7GONwORM3dZ1wQNJ3Lwp4jpnQHspOVUAkVQ8w0sg_1CVtBFRhGy2teGdxz-eFmSG0oWza_lOBFSCMP6zlo1qyTbOfwjwFRt0U52Sd9I0X5Z_zk1ywEhL9ur9EtLFaMiOmp11uUTPbUJ6CcCyySHY7PJvu06kXRpOmP38y85R4R26uT8e0O-UF0KgeDxCkvbu6353W1evOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSsbUqbGn2F0V8asOaouR-zmuvWcCZrXYRf7s3vYZ9NiCNQlLvmEnYh2IRTMFBi_NhVO5iTL80CZPvkpn4Jw1gl6-6HuKXyvyZHnSiY4NELtVIpUFv5Uz-1nhX0pVzAZDNCv5YN7UGRZAbHNXhaLqdcWxNfkypyNF4_VNrOaPjiGiQTu94LcCrdFtiBa1UqRV4jtPGBKMToo7FxSz-7yllvspbct9paDmVRW5yWo_uhGNKx_OnvRtc8X4aeWQ4j8mL--0Ke2CUcEZ8bakv_LS_j52LSkVsJ8V6jaGQBEhCLIKF-Kl5LCmQGKOPz5GJHZzMF5UCdTHwFDXyCY8Anp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmdlALovhmK9Ejzgg0CicDc44w50F3vZUG6Zr9RPwkEfdQO4mx9hkBDRQLrZGYYjBSrSzpEsngNbPkk6mfBl9QQ33IqcxSTyM4bKe_bbsIJubk3tNvJ7aJQZ3JIcp4Nk9E0tbP3QW8dtPn9D1dVqqSQTiB43ZN1UhQJBXdKGVZuz2lodbftrR3tYNSoft7KXNF8kDjzs7AewvtsMzcHwMc-RbduH2P8xr9hjRs1lHUa7hdYo3GwOaFcVfKTonUQRdCRzcUVCeT-_7PG98hAoEFa-9rfjd2jhi8FolD0D7AdwJ1uESLKyoxfFSHXsWtsV9WZQ7P2kA7_NcJeltYjrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv5uhF246UO59QMhd2VU8qNB-9Pavi8fngWm3KVcG7qZWFrOaU47g76Y7njdEj7AHlsB_YAEbVXPxOpxaaaE_IHC-bsvIzXHSHAAtDXMbGVQEICxNPaxMhDWOBqo3UXfG5AoHgyUmsF14FoTdNH3KYMJeJgJ3uEi4UhbcmKbqzQ-JbL45834D7CW2kaHDDdQp2R3iVzFdiNtBp8_Lb4F589iFKOJPDG62XhjXve_Ud3ShNPTUo9Mn1njGqVApgJwIdlMNNsytvGhlN4mLDIayV_IkLahjGk1lVAiLafho7PvxJkV7uyaL4unMmxUuilBwIfulrmPVyQNb48ocKqVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=XfECMQw3uRyifzu6wQ524xCtPDLuhVZ4tF2ZIk-MYQ2Rd66aoS5wMEOXh8oKKzoA-gQGnkVTbso_4LYgPPH7EHi0eo8bIbIC8CNGbC-LeCmc2MelpeVjtUjWtgM2nYB38icmnHaQnPn_VQWAYaCxbYeGmy_RBRpL3c8vQVVCM3VMmBfiq83F1kDI_p5q-bEIlHFgLIizeP7L61XHOxZ5bniwyR2n1qZvGhPMZdYcbgo_oNXsE4wEo00heEftyFwOcrKS-hVS610-yY4oWeQ8_GG5NWnfPg8zy9fS6WD2xmx1JWz1NHyK8DY-yf4NR3G85UI7OERLJEznVYu_BVeqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=XfECMQw3uRyifzu6wQ524xCtPDLuhVZ4tF2ZIk-MYQ2Rd66aoS5wMEOXh8oKKzoA-gQGnkVTbso_4LYgPPH7EHi0eo8bIbIC8CNGbC-LeCmc2MelpeVjtUjWtgM2nYB38icmnHaQnPn_VQWAYaCxbYeGmy_RBRpL3c8vQVVCM3VMmBfiq83F1kDI_p5q-bEIlHFgLIizeP7L61XHOxZ5bniwyR2n1qZvGhPMZdYcbgo_oNXsE4wEo00heEftyFwOcrKS-hVS610-yY4oWeQ8_GG5NWnfPg8zy9fS6WD2xmx1JWz1NHyK8DY-yf4NR3G85UI7OERLJEznVYu_BVeqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxNZ6zK1XRQvthucW8tMJUlYSXF2QjAtyzOEiL0tPbHAJ1ldnKOU5UIszopWG8BbAMmLmLA48SL_jJlBW_4knKVr3erEd6qTgXgQSq5bOvBE6qt9x6p_N89Tjx57sa2oQqdxTXX3637DMKIhkvfRu8knkjNo8Xbk04ciLTBCcD7T7lqQAgtfw6quJ0zEErO9Y1JtYjdmspmZ7xoCD4L4xwLp2D-ImF1oWh8VVEIfmxhMSs3NHvDzpuwU7KZ0XFdmBNZSLxDi9JbrsW73Z9p9T0akQHth6tNc-yjg0S3mKnd4TtzQkybSwGctNNwgHW_B0IzYwfFSfolNzdFr_7wAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXCovGGJQbUUfj9ZmLgdqxho6xbqmRZ7V4hlIBDeKJYm15cMkxnvEMM5gtB3f79mjAqgUClw_VdqAhJ_7gdcqZbSwVe3h2B6rcAEwQi7cuMr2d_n9A7aiMWHv5iIccfO7AQboqYYfF7nRlY0SQOdQ541ir0gswyP4zIbpLqIuCBszZxSsyKBkOULLtuaikhYV4ggqBuxiIG-1Jv1Ak67lONm8r9spHC-80zT8CXPVHcV219523PiwAnSxTdMrlJEXCXL1P_3s7LaVR_uyv49i91MV5mpApQHxuG6B03tIYjxAmp1idGmnhIUde8xLmEMRtK0wTpSiujyCRnPRZ6kvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZwuereTbFTCCygnfEjokU8DgdPfACRMOXQac9tQBptrDk4z_ZriA8144BXEHofM4Pvj2wTpsKusshQ54I89TmR28jGaCeLn1EtDeKVWFM5ZHvZGhut15KDi2aVwcdJTfac4opAxLj17Kq7SnAQm2DtB99C4Fkv_5CdqWfw8AS5NnygQqCv4svKPQ7zUCgpLtPEkKCzBfVWEKXDXAWjic7fOYehRQaKH_Qg4JqdSEaouTx7aq6YaCtKF2pm5HUoeH7ShfDkyQjyXqYJCcxY8F0zXlPVOS_dKL2xi4xoqnBa7nbxA0-5PwotsCAesBn0VoMZ-NSM0Q01z8QSPfUvCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVRTEeNX3TOahy_-cYeiLd623cTqXvMs6RwLiKYd1vrrqCKXaCBuqFpCKFLmOBL6ET2EFYv2UupBIA2Mhh69bm45ih_MhhjowTgLNMAvbamqy2BRXQzh5QhwSbMA77RVWp6AIh9pc6z1p2bepdlVIFijMUoVHYos0oLuHkuHQtojKs9bMqMcrvuqUAICOcaOxWuDcigS7WxvNxHiARDxo9FkFWrTYSjJb1Ycj5b9nVfhmHndIL911dxAuyJUkGi9weIEaWLaaP15sD7CBF5j60B55RS9YG3v_tLrUESYUmHrSZIBC8o2Tk8dia6SqDk0lglAB5ZN93IMEVMgWxR81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=VF8M0ripdx2xUYJj0HqK47QoMZZREP9qwJBlpGt3U6yQ4Ysg13VNMnFUvKyBrOy0b-DR5uk6H297IhWiFGM3vYwfMupAwHffFHEGqp7JQsD0sElNQm9hslSvDXi4a99AXpUCtCdkdgWXjr1Gl6i42cHn5xLO4NFcOMXuOd3ehqe64ZKyP1EWlbwRFsefE9IGoitATDKpszHmXcYcUct9y5zoc3K4ZPqHRKU6TDKnLk05v296bdUX7-02pIdkAutZOWeMmZlkeqXAHIE5s8JSTCUiXjkxA7b8OXepwg5oWBHeyCPi3mygN8Dz6aG9z0yartKKsW99ZLiX3vPtY3RFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=VF8M0ripdx2xUYJj0HqK47QoMZZREP9qwJBlpGt3U6yQ4Ysg13VNMnFUvKyBrOy0b-DR5uk6H297IhWiFGM3vYwfMupAwHffFHEGqp7JQsD0sElNQm9hslSvDXi4a99AXpUCtCdkdgWXjr1Gl6i42cHn5xLO4NFcOMXuOd3ehqe64ZKyP1EWlbwRFsefE9IGoitATDKpszHmXcYcUct9y5zoc3K4ZPqHRKU6TDKnLk05v296bdUX7-02pIdkAutZOWeMmZlkeqXAHIE5s8JSTCUiXjkxA7b8OXepwg5oWBHeyCPi3mygN8Dz6aG9z0yartKKsW99ZLiX3vPtY3RFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWWZ-1BcBGZhP7t6fGN9dTlkHYgmc8G8gY6iLxjTFsM3PKgF0x1da85DYKrAFT3H107noqsVJY4QPM0ByAn9hDNWDBaoxAcy5ABQNPGPPps-8kfHBoaqTRoWMW5-L0TNRI-bXlEN4d5gavxDHW8qy-fA9ApNsxjHLTBmxATdvVi2R60dwoQWhNt2eRo_8CjdYCOVl7ysn_F236eAvnQYKc8OmwxMB_fkB6hO0BoVjtKypq9f_Lxol1MKINFRAgNFVBE8Z7PT1lOmTqBLjZu9FKHLqR9E1xz5cb8NgqyHH5ZxX7Vh892S-7TlDZLPbtIg_SMfwRRvlu1wxsDaxdOGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsiuNw5aMwuBVDfUyGG4AsXw6TQ1L38zjnCBG9wV24teFJs3h_JimiMyJ9FWCvhHYkfZzX0PyYoWlSlBXrIMMwxIseQhHSdU4LoS3bPERMj7TDx_XERfcU_47sfGp3shbXC0UrpX4MIjVpHDcQepx8TbEvPJ1QlSIPQCplWsHEaiWbDQV4loLoefbni1as4NFdj-t-0sKHzZfjN6bB5NefS5aVMDaXd_Ufp-AKGaCDEOEZgJQ_H7TQE5qW48F5aC2Zsl7oY0xREj1MkPWpHl2KeR-m3COKI1r775TaoEtsRY2B3mb43VSEEnWw3jEbKCjXrRb1dKnLstpt1v6ksCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
