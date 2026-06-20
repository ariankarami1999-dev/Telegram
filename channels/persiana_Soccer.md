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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 03:31:43</div>
<hr>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUzyouT4b_PHW5d4Jnse61EE4t8REvWBbdahrXdcph-z-PXNNI2-Vm768Fy28OkoXwt_xpx1H9j3n30yvWP2GAcqi7crpUwUbpVlaKSnNu7KyCVCebuTZIx3RL0pe-_wuaxDzx-cDXv_hF7lBW2XChm7nXeGMoa4wNdoAABY7cBr2LpbVkr7IkFzKJ5msoqxxB8dU8N8wDCQzp8hpYO3UoYnknsqUfaRfjs4Tkju6Djrm8r3SIrv_leU-W8alBxC03HQCQpXJrRnFYCS9hr3Ojtd74iFOncoDKnhMvZKvPat-s1FNVSSL75gll0zBgk7jny-P-Mrt6eIPZSzZjzkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfRLsTOEaRo_TuB0fwUoKgp7KOcy1awslM_azZhg_xYSH2fVgtH3kabKJoJBHjtHr5xuAqyEiTOwt3XbsOM2Wf6gNT5bjUT_N6WTwQNPCXz-HDN1kpPuN204v-CAzbPt8tkwaykk92MSpBPiOqrvhJA4i9FpTg9OuydYK1LwVeCU6WMmuJ7w-9LATokHjlL-AkDLJz_o9IW2S-UXLQo9lViIzYYdLN_RxhOS-IbGoALDzvOajHt3wo4ZJbBJBKGakE4glL5FLZLM5gMSmsPZ2GmDBVvEJuhBWwEka1Ag18iwms8RulPj7jr9dkSPvX5fA-BhkyRbfWFx7IEOleNsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMf4M6E-oJBX1h_xKkqW5yUZV8ZovCqP0fNtmCh4-AHLh8M7hlN3515V8zYZmiwgpQrLsbFawr80lPp_lvQ939qHj25xH7J53m-l4lVcyfB2OiYT_go_FvfE68gm31I9uckJolzoE3bJsWjIIqhBAoup40jIjKvnYXg7DiccItKJDh6kdSpc6bkV1DISq6dPcW9o1KwNYsLDNW0z4r5gDCjDDUpn3gagoru0Hq4aC8nDkVMBHEnaesIl6MVaxGPXL7EFaof5xFVJOrMEeIODv7-AeiN9hI1yjEQF78a2A-SCc7vluCoM32s5A7MZhwlgQi2e2zlBxaTTFQX2SonAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2_cfzb2pVB4TR-cZgIU5dcAAljwcgdmQ_rx5CYsnIIeCkeRG8UD3rb2Q-iq_LZG2XJNhd45r5TxWUu6wkDoYHQ3VrAmUJ9rasDDDwyokwbUL1BucbLZTAo9DUjeNgDsvzjk9dUqg05jjODAOTLSWjmMJSqPjOoKUTVgb69qax_QXq2n0YCImtFTeeAi-jSSvew3Ej05mzq0UThX1it9cD036Ig8Js8NnYbDtpunbp-oB-E1D-q-jA3blM4nGi1zIPQpzfrRTrCvRppmEA09BpP4Bc_OI7VicR2pAyh1m2AsEaJAqSnc3GKu2H-mnyq6sMnNz1I1IWcf874qOBAWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-tMnIceBFvANqcPpAXM7KNx8huIISqTCE_id1Zn7nGY1NdtMvEDqhaRzsHxTJYcv2HR9ewHOX5Eh_Lez_A-wxEoaNfiiO6xXfUtlPbZ6KLRODgWIOKDMUFoh_FIiq8WevybDpRmKdow2kMj2Mugx-GOV37s3LgMK188TjLWXJ6Y5U6ZqNdqx5pOPwTk3fBa6X0XP2USthCZAlxO6qtkQKWKxJYxspIUBMSqQmmqYcccgqx3w73MtVY6KXo4RXYq-89Fdrc_mSfhdkvZOB85m3Hd0msQ_yfIVnCdHKGWYKzkj4dmVSjJhjN0lO5yRwmXx7b5zJQjzxfFTnkbvJpNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23869">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwkmeHGLSEgN3XKBA1IZ4DdM54NqacbSgxsIQUpyzcPyGnRuhAmvPOp4ZaMTMJuS12MIV9N1e_3NDr44vPnXk7jrYfE6nZmljJ-FVj71n7zfpwB6s08IJUQI_pUU5zqeJnJ7muRE_qakgu9N-VEtEf1i62dLN9feSk4P8zA6hisZCGhGqNK5vmNqyKGaiDtMdaJsm4sNTQTqRRfqJDz_NClP0yoOCWEZRZACqMVP4qVsY3ltRoldk0xoHCLqxxQXfacp43R1I6dkHBPr65WjTH1o3_Naod0XGazGGWZxlfMHyg-gOydIKBVcx47YwlrbRoL8cNkZpOuaVv5wj9zZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e29
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23869" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omZsKjrenN5Q9eoE0DqGQvye91hdVHp4qqLwdfpTN1-gnenwr3werF6DjOg1bK1TW5R02_cwlwppIgm3UfZjR0DOfqS1-vK9BGPerHSGdIU7wAQoX7zEOOsEZSrrV5FmAWmI44uomPamktjB4AQvmtgrITfKCecYNPzfejT9gXBSEA1fNjtwlwJ3X3OiB6eppHVE9xFH_nFb57WzLzGmv4UokLnxqRaRE5stkHKx3Pszy0leXoUu9H_9YhkmAo1mQjMdKUcxaBUMCqYP-hXLQ928CY-U6dcFmWMHgj8OBnbleu8lCGB5wUuHua9o-8ChiXQvvDO3FeTvEyBYi7-uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g85Khn0c_L8aL2yjZT99IkbBcD4NltSlCTsQPybkAfBQeFzfs9OyYKjSAn6HJbDypMIbj7lp9hOEBcfIUQGh1wlLQ7exORlcQBD3Lkvy4xPcOog0wz-M7qFpIh-rXSJ5-yO92WCLkH0NL7caXj9fMmxgsP3t0DLt_U6LlsEwtrMnqCnNkp7DKmZ8VZsQWMUVLl_8n5FHEINnMLHzTEAIBX5gIv-oqkUv9ARweXQJOqKSkfc55cgD5DvIVTCc0LrmNumFgZ4JxegKh58KZSxzsnO0Uvi3UCCSbUKs6KkuY2jMj9ETd_jnxnTJWqoN4nESeimqfFemlm0wBbDFKAO-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVN9TfCywV2XLnPCIymacnTE_aD0sdvrmgs7kZuTDpdJHQey4p5jleeo1WVidf1Hbgo90SAXwgzj1gLjjPasJNZSostv8ogNyQuKNGHcE5o3HbzbqFbkjyFDPxC6JXISmmEmY9hduZA5rzlYllD62BWlLLdzStwwYI7RvU2ibhD94ZhFPvQUwUw0hjutfuLMjKoedXvHpOm10QsC-nxKMpUuqfB8OFO8lBL5MkWP3x6dC70AxGXpV6PT6g99faJijRdzYI9suNRq4wtaLQjxA8zjFslCLMbWdt0CuUtmC6gXTJttqn2rrTpX-ykcZKjXHYClPiZSY-LG3EXqzoa_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSy8HTlaDYK1i-0rRz4pnA1btaG7YGwvpensnytDf4LVaUfcXFAgoRbY7PMOdM9qzPAOWJUWVIe_VRESgYkQoc1dsvrGda0j3H1ZxNi4UA7u-LinrsUTEndDOtbSOp5VC7Y8AeMUyk4fiHjWtXykUsOfJG8t1xhu-epNJdjG5i63GNgwcW8yOMtSk7LkNM8ZLQm6RkLl2lffTkWy_mDkCNkdaniOZhP9p6W_6uyg_VPAC_OgcgOaTq0skKH_Dku6mbKhAjPlJWpVYbuyQTByzvXbXkqGTii7F46sgJeNRWHxJLIx92NxlpfT0pgsCEj3glGC2govdyAT784zMuANGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFL8Bi23qd3hsVDp9jPGhRep9SIPotzNLSlbOWlLKT6ODOJQ9bDaf1jRz8TqSgPEnSGUhLueG4vx10563RSZGt5SQpponXlDNnLM2y2qBmnnA0Zd6k0YE3x5iQZLpLFmXE7rM-oFcimSQGOSrXUcMyGEBUTsFzow16dUmtkTvo-dwKpFvLG0PneccBHmyFZGIBwot1zwGN99ARTI6fk1g3TzUMoZZAkOpLoETAQAiLrrhfs8mYq6btKM1oy87dnPkyCA87vrjZA3TSHnwGBZX8SlHlh8Xr6R9s9q-TinbxRJPTUAfl8Xy3fow_CQpKg_jqufJaA8mD0eAFiyLbxs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD7KLBIt_PzxFKyOYizoVfBUNDu_HVjRMwJS8txnkXIkqI_LkjWDV_QF3yOUMH-O82My2UZj6KobQ71b78uK7J1ZRzPN6VaBs56SPMmsu-s8LVzvGA2ia_lpgaXvGwAoWoEYuLqjSUct7HAiPL6Oaoocwf5seEWnfKmZoUhdtFMajf_D3jsyS-60UQHA-Xax7m-gVcovtXT5rTBk8PFOaYZ9jDA5nZ3xhy1URIWb-5gpcY79CniigL4K5FcL9xCzkPGZ0emYhKyth4ZTruGhPsbyFBEbxHvatB1SdKko-YaCJDkHxtphLtoxd4F6dIyoUJ07dZXHBpa3Q80QSTOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erTBKBixWPLZIzOLecVYG30cS8r8GUk5JqDgKXjPkK9m2ZF3DFom3S9apAGybBdR-knOMUrWjaU31dQvnsmro1o5XHSucOG_Pxlby64oKzP5PXUWRYh-1-dbz_vPKF74zQ4P7dyCjDlM-P32gPihvgPz6ljMcQLRiC1iVTeX_rm0NKN6sNlhc61YeNL5YEWGGUiG5iZvFm5foZ_HVxgyihKJgbdC0nYQOa8PWZwfMK2r0AwUuTJWOP2aWoWdNEorSNFoN68eIEhl5sol4_Kxvr5W42W-feouhlCb4RHpxVr6_thYH4T1kGwYM_0y8CyqjIqRpbcZbWwKmZFNReVobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhIwQG6BMEHwQGUFdWebHjT8xVPNrpirpzYUc9IVuum3k0EFAqNOeaynj2iVRpYAYp7j3Hw-0P93-KipxtsH3bAQ9kdbyhgDVJ7lBKXWEe3Xz7261BA3bW2s-RpJnv4dmAUJ-COGt5jJwWqkZB24J792WiF7He3O6x4AQtnPq0yp67bNFnojXf801rARbK4VBglWVakFh0-phYNaBtndFT3tFGQQqyGnIictjSm2ijbIQcrh8naNa1sxapLVryH9NMQZAfuXZFkwwTbv6Go6_64Hy4A0Ow70KRX4geq_GbcgmbEICrXrMHiMItuKFCtP6Bk9W5mNBSkNiAQP4_WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7Iyg3F232kEkycerc9A1b4diBeIrtllMUvUIY1N2iVWeX8ALeQAXQ-1kLwghSEV_GO3EB9B9eV-3oMtECFrNoLnG7RY-qn_uudV-UrXESir1Y2X7hoOD2uDw5yhYcHPW6KFIyy6Vh0JAYO1YGDQMvWSEEhu0Tqgtg2lCc8-YqOrh_d3J21QUAm34i9q-bwlmKKlbIgFaGIWozQYVWweOgabEDYBr297vHV7TKC4TjvI9kU_3JjewkIq6WcxOam0WvZuX_odI9pHac9LtoYPS9KV2haCXdD1fwnUFYZodMPUKYKgoQP-IOb5m0NXTUD7zv4EWWYa7moT8XVBxihu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdX9ZWymePNNHBamec50M0tlRCNGAkLm8_XdBxVlZDoDLt47W2dqXkE5sfhPFYO9KKaxzj_1Jp0p5mflIj4tsJS5fcj1hvrKgKczkbrbvyzqiMGCgLqWK8zrhedQb2npR9UzO-6qi71Ny3ion0w6UWJzVW7tL-wwkATUAPtgmb0t8WbnImcmmvi5j0Ggm4k-DajUnyn-v3P-zRWnhEI9lveVBghZAGv2TV_Au8p2_dFaQmCubxd9gSE5e-JFM3FSjQyn624cvVS9ON9z9oMrgSVJ0rHfSnmM6esx-sMGYawbXZoelIKo7jPCt2RnhpWSvxgSW91nXREpBVp4adINAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmNetkQq-fsCATYjixgP0xr0rxPnCZdI9KUIObu1pPWlYQk-dIQUFyivRCvrIgVPSKsDqrIy7vHN9MxiCfe2v52VHxqZRDaJ1G4tx4Fh_LeBJUqFm496ISllsiSduGYXJz5PAnCFhIbC_4y4a53PPgY7ghMjrv3OvP5_qnTjEPwpHMZuKwwBCNBeL4HcOWwfBU5u7z5UtShtYV6_WfLb_tE1fyIRM5bENdM8BkG3kec_Mhe51NuAsuAmTpBGj4hWi-hKAFveVrkmZUZntuK4Q9a8rXjRhJ0PzmfQ1yh6uzI1DOXmCBztzxTvt4aNVJwdpq9rH_YcG96kvT2w_oTylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mui1kahPgwY3GVvLXcYIvrZ-fXifyDICtkmw0pB7WKbVT9gpVif9AJWKyj2VSEumN9fVEj1jIdWccCJqhh2kTOhI2zPS9vRvSnnGRZiqcV70YzUL5FkMyljoH1jB0X2cDS1-VBDJPd0Bh9RA-bmez80dYSbbuVEnXbVRZ6XovhS7mxSvWp1MMkxe1bnwzhm0dJJlO7d8VyVZ7hk8ADVO17ID2RGbxmc4vBK0jc8sAfkPB_MZTnFPamtkaIPzVIR5YH6iuxkMyj9ktshEF-ax3vweL7D0cH1iptgQqw3lTkofRSYyFyKnTl6RU7uWGMtpWgyZZQSqiBm_-nfDHy-mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxx4BJjzT7cUNlANntvcHs-PSZTsFI7SlzjhevXFMj-jKspW-Ico8jAa0rAGoMSoTuIu2xO_M7MJX4GZagKxZ5LvOtdcV3R8I1Y9A0ag5QZv-feyILSQvl0C36_5xOeU88uv_YK8qQ5iuG9ogQ117646EUihjbt4Cx79snjZ269DNX3wMYeS6G5Fdg7YWyQqClEgxndsa6Dv-lW-QEa76tcw9IUQ2hHtaikM0C5ssD4bYkR-Lj5RaYS64DkdJT2qMMYjsosKnbDJuGGbu-7vYmrOymKpYhmNYbJc3uWzPhQ46zGPXcPmzyfevKNzA_kroBvkcdJv-EcgOwV_TelnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-DqgBXJpolvsYQx7ZccW2dvSJebC10ZI0uyVLVTlA2Ci3BEnpmyI9qnBDSQh9jKSQs5B9ypWlW-Dhd2rPI7hGqWKmVBYIyEvIBInqT8X7Ao-TWu8Kw3xDsE_nrXvkH3hNNbiC5n-_sidGt5r0PK14iPI27DoTF9pyoyuSikm5KFwbHO_3XahrfOIh_3t8UO6P6ooKZYWQeyEtp68Ws9-YD-uRojT8xuPwU28D7ZujZ97ublYibq77ZZTwxxuw_roBYCUs3FenRwQoGHBvf3ENXugFx13IkuMOuFfzhWIEWs4MeWOdZ8j1H7vIxYDnZqgIDu3eMAyUQqq0PBuFaKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaHe6dEhd9XP43ZqaA-_FQh-ij281L_J2MJIGMYIJqMR00DXU9hy2PTk5U-BdhSeSoh_Vcbz896Y4Pl57BsuDCHz8X9mRmEy42rjtY57_SimV7gOskfJ1nR-PlFo0CQWH14P3bu2S3oIHjZGE1eFFy9b_HGr9sXfTyBlRi5qMOddp63yTe0yAZgdyRCb1rGFjDch7WYf75_gLdcddN8doPoNx_AlMG3KNPDeJjizxoQeJPsVgvqInUJbgzFS5PVxvSA5p-9MlokLYLgRsIqlJkQk90kjHhL08z8Yb1py1pExTnYWDR4C6FglI_cXaxLssEQrLGQ-sPM5R2K0JxdqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1PGFvjB7zxQTukSX7YYs98tO30Zjruvpk8nAodE3IRD8GU2TWe9KYMCm9viSTRIX8HIXfO_9cUu-bjbbCg9Z_CE3qAyqsIM6y55QZ5AUmsv2sqmUIUiYJZ_6N61LyBbr8-pOyhU6b1IKHuh1mIdPaZenPLO_gFGmGSLbaToZwCDoE53Jrnw-Wrmn7k5lGIKqwlDErwkhiAoW9TmbR3Q8TBM1Bgx7zWUYG0v8cDHlCmzrhRfl8UMJfHsKzTBRdOdNwroYrfTnq-YzEqrOULJzxPCpQOOjGObFImqUBHcKfLK3txyrunkwd3bvcZGj7AFes3USplbWQHi8jitSdGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MciWV93_Xyh9TVnzp3b5UFC5FpjtGSzfmuzE_RrQ2558dQ3zKY9_d795hvO_hDMe2Ysdvkqb1QToT9fJ1_xllOu0cr2LDEm9lEdkuy1iK1c0J9MQoZt4oabccmLc321ZXc5FziK9jl_nqFaR2g3PxKMJ6nc2WWVGCM0XVfKH5Lv_bShIDsFz7czU0trqnpFbA3Z72FFh3dQKpKZzsPxiTUSFbncqd74R5FqDeFAx1XM4--Mgg-Y7TLBZHBlmF1-2fB9mizsoRpUqBbwpUHXCkUuHtumMjblpoEmO92BgO5orzwuV6URbY4UFAncD-iQ1kk3YwgMKKx3bnpC34_SM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9XSkhRRRUUhda3yunVtVHrjBK2jeeGTz2lwu9XOEHcpu98qL6WASCEyI5u_XBUWEFx4bZ8tPrWjOpDp4Q2lJfe7KL3zpg__cgpfeJEfSiMJDZD766B8DkEruWao2I50D45QfBOqqDOvVNZzax3v-gS9Nmz9O4iE2WgLL8j5ZSybHI8VdySprF-osUJ8rHjVJg6u1DfdhMmg_8rcaTBnY1464h_AzqWGhLkCuU7XR7YECLIfJM8ZZbtYsLi408bqvEBttcO64zc-mJBQeBuGlj52MQgffFVzDEp67EbiT_hmkB-c31rCHMoPFc0jBSbnbaJXu1eCFyumExD2O1Ef-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvi9H6iEEPgl14X2kKtd_8EKcQGKkdCx9niQf2Vl-xCWCFNolhr0BkB088n5mfAGvZgdeXHuOBt10u9hGWDCyqYH_v63_f8QRRoGYeW2AnHtLtKLOymIimcBmzeKE-L4Flo0hXPRcnfKb1bBCgbsCnYv7dZOcnsXnnGARJkRzBHaz3EyT8qka-BJkq2te9zPuxHbY8xojpsTOr69RlnCpFkSQhe82G7oySiezqO_NkbVXIjKUAQlpz3vFiBmOX7r3vT0_VqCnkTE9NzdBPyZiP368W3qI1_oGfoklcar-ySD_u1ChxS9bhdBpTln0pnZOVxtRrpYXktBEnoVBo8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0PAFHpnngm7NME1YMMOI59LHVFpPFX9tGJXs6FTwyToil0xXyeKMplUwjTFTRaQpMYOslI5lgpI68cRhK88JNhlEje6piV3QvJ689cheKoi7v6uR7nFVPgZaSjfK6KOzj3Doj0P7wolK-lkRwzIe4A-RBcKsBX8n9EEq0Zvobgfo_SEr1814lzTkiZ106c-VcsMsvntiZMcg7coqCStbUcpRS2niWv2qFv3PkSFX5pB915M458COjX1HyAo0rZpYW90h9gS10Ua8hNK4YTAfhY8dbAKne3_m_08c2UbfQfPdo87GvDzhwp4xhruLxr_SNSPuA3fCbEnEX4bXYCPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCvasBVOObox-2No1ETeNiQfz7tWEe3fhGhs999oqJj2dZwDzEz1nN9xOLCg4Xb4wWtARaWMn1ax1fDZxPAwUalfUce92fvJKUnQtlMYPtqaDoEjZgc_lviqgFOD8oMlUg--BYIrV6FqFEcA397NJNDGEPezdJZ13_J1QwGDQYHQ3ssSjZE3ar4bZW3GngWvDyUiYl5DHlcMmpv4PE8m_HCfqWNGvlWlnWF-dJxgUzY7K8nCUdaFQxRqgwOV773eACDJk74PFfB4NesxnFdaLQsycpF8fqWaF6Z-XPckh_dOzLZjuSXk0pxEAaPlT2EX4JG9Pg1umM895RIvl86uwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4MKvVeYTgOxkhAjMSJTyrFTn55WqRmOKN6f8YVVSQ_YMWDVGpj_kzwr1gNoRkUKKL9meK3kSjYWWnQpbH5Tj_LhOE7mWMegP7Wr03ROc805I-QnbQGK8C_xoRZHUc2RVfmz3lfBWpH9LXX_juXodSx1G_hiMGlgn2JyBaUBDK1j6Wrd5H9EccDVnCUR0qZTpMV53XjoX8_bYaamBRDHisOoeqHWX_kPjxbomwDhQF5zl0Sy66yfRhLAJLfTpE9gFhUWxCggAZsq2A4v-XiW9QjmOIkDjPGOPYWwky4Hds2huZJfiM3isGMFB4KHHoym0R6L8MjkqgyOwwM5AJNOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPnQojm9_6fWOP_GwAHzzIX7ia1sCoy2He6MX-Q77x9EZH02fMWSJhDJFp6jgL7LOKgAKFSNDofb9d9ImgW1_b9cKPRI9r5jSi8G1j4EAoSRxv24nz_eE1Rpyb92uSPM98UXAxt99nteSYv6mu3mmw_1Heo8MbHo7ttqtwL1segDAO4cOULQdmjdG5UrcYtfA-pG_2-9jin7WtjT9rNOxHsPIDPfd8j3lsU_VmU2EqUFxTtLt_sbpfYt2BKkPXFbdMk6YZ4Ijjwcl-RusX1YfcJBOZSWUPwvsk4HXBcVDfvNalsktZ_u8-VH2dCwA1ftkwjWK8YaafmqfNgYYLhz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJsti36wZgr_7DXLPKN9lgrz7vWC7OvMSxdpgFNrB1q_AGtlBL9BxzRbVaMihjyBuZsDSxbewfonNWdWA_HlhISt7i2Zg5eJqgNgGMhH-7tl_MTuJyvKDa-L5Uwyt5S6eHKXtBiQrdc3FuciDTcsNiA3yX0KLz0QI046LlG9akrG-uqnzGRTYS_cYlVGiQPh87xVPlFGkrpSMzhiRDAD1b-sEsr2TnDr1bFss-GKLHXk8JeM2NkUrCq8dn0eNNPx6E9FCaoGMmOPd5DN6uNipualHGb9NL__yct4SH4JmlPIYf48KCo1CaGtMF0iVCp1bUnq300BzsQ8OhOM2Rs2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfk0MOivTRbLCHvXVHV8BBTBjL6lGBDlvp1uC0_je-c5kh6vQ5ZD6PvjvUWpxrEUvyhTro7j-gJ3aJgcrtZ-9W0IZ1JPjCrp775l21maosoUlOpJSRuxhX49PNNrK2ZEFjhjZnARm-7KT1n3Ge-DM3bgZEHkxOZvi0EFFrF-ewgzI_Sz1SK6MGqLWfush4oySh79u4cCkySZ8_ESVlrLz7L9VjeoAE7uVAsuQWrFxUMojYeZ7Fg7-_VgXTvYal-fBEhIxRiiYrHbD1gue-W_Lwr2MNvSU8IrdrzUG1Orf5WG9xy44HWJvacAgvDLDeeBhPBETdSs8vjqFeN_OycDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=SsYAMKvwS0cTuls1ZGOo9YyJQwwzy5U2eEpRh5V6Y9h4YQuO0vFKX1wBQvEKLqwjGNR4WMHoz9qeQXNzSlPl7XbcBwfzRXexHHZQmneinet5vPH4cB8SnQE74zLZR7Up4I07GNweyx0oBB50DWC0fOHJuK4uFdkzC2R6h1ijVTNkUEAofDAUl3Nf7vavAs4hyTkYciSVj1MX9h1Osdjo0kYjpVX92tfHuFdUi2QZb1zExCKeYGWTTybW_qXCL3E0bVd1CPDegawkMPygPmWjE4285F0KOjr2k9vUEIhTT8Wd2L4Xt0SceEW-q6iE3ACAeJ_Ys7b97dkw1SALRzY58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=SsYAMKvwS0cTuls1ZGOo9YyJQwwzy5U2eEpRh5V6Y9h4YQuO0vFKX1wBQvEKLqwjGNR4WMHoz9qeQXNzSlPl7XbcBwfzRXexHHZQmneinet5vPH4cB8SnQE74zLZR7Up4I07GNweyx0oBB50DWC0fOHJuK4uFdkzC2R6h1ijVTNkUEAofDAUl3Nf7vavAs4hyTkYciSVj1MX9h1Osdjo0kYjpVX92tfHuFdUi2QZb1zExCKeYGWTTybW_qXCL3E0bVd1CPDegawkMPygPmWjE4285F0KOjr2k9vUEIhTT8Wd2L4Xt0SceEW-q6iE3ACAeJ_Ys7b97dkw1SALRzY58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfKV6vbaWcHfzWY_YeLPdRcI3lb5QM43IcKc2hDk34JoauXR3sFR-1Itg5165f1N_PU-fl5MDG9-J9Sl2iqETgm4lPukhQOvG7X7RwNC6w5Xikh2Rtxpxp6y9QOi3EmSeIDN1ZpMGDD92vnjyb-2coKypcunvI3stjpyU9lL3REqwghTAj7ZkZ-0X0p1JBo4CVyW_Nzmopu_aFH7KY44TlMfsRIYEqkLiOCzA7KXk04-GB9Tbe0IVaKfBwLeVyupc6L4n7dGlAAO9WFodWLHWjwy5lA8HqWYLpQBnBMMyoEvKeJTu1HZL93m6fQTYxSA2mqD10_jB0HO8_vJpT_jnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmakQ0Ue3LIAgHGstBbK5cQcuC4QkTjVXC3GRtoWTa72sog_3Ypoa3y4BCliY4-ep574qNh8vNSFbp8Rt7scWsBC4eE8AkU7YrWQkrS-NBTYOZ1XuY6rQDa82NtL3xs76THR_KRptp0bRso6xGqJHIRVt9qc6Ne_qN4ey-oAwxOpxN7ugWf2x80ijwDfvjhx_jR2Hc_wUk1xzYBzHKz9tPHSQBm6ZUOz-eJERTZ67NJm28SiOYzeZQ8CDimqoG770AlnuQ8C7WugIuUnTieIrllwXczWo_bH3f6RGSWkSk5lBmROnUdm7g0K5twYj5h7orGF8i7b4B2NcO1ZO-Gbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=ZczVog5oOZlSmYQg1Vm4-69wMWd7bV2nsCN3mhRk9ncIIgCJW0BEPKUcTZCVsw4xIuYs4vhQrjfXzJZ6rpZFoZlCis8bfPD8F6GQZVNrm6zbmF-oGNRdxBcXx4qFD3eP7t7LrUDsBoVxPyUY2yb9gHK3tfy7CP-Cq6KnJpaCELvwfHJ9-tTVl8oBRIzkP9R2EW6xUqxQx5AhQZxtz_1LXGZXP-xbzWL1xiJWnNM8HErd2S6RtMu2Xxe5q7IbuH8ibobrXLPAzymeisnYJa1Jg_g37GQ8GhxSBHT7WSEnQjOjGX24I3QKpex-vIlBRdb6MWTHf83YKOqAH32r8dEWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=ZczVog5oOZlSmYQg1Vm4-69wMWd7bV2nsCN3mhRk9ncIIgCJW0BEPKUcTZCVsw4xIuYs4vhQrjfXzJZ6rpZFoZlCis8bfPD8F6GQZVNrm6zbmF-oGNRdxBcXx4qFD3eP7t7LrUDsBoVxPyUY2yb9gHK3tfy7CP-Cq6KnJpaCELvwfHJ9-tTVl8oBRIzkP9R2EW6xUqxQx5AhQZxtz_1LXGZXP-xbzWL1xiJWnNM8HErd2S6RtMu2Xxe5q7IbuH8ibobrXLPAzymeisnYJa1Jg_g37GQ8GhxSBHT7WSEnQjOjGX24I3QKpex-vIlBRdb6MWTHf83YKOqAH32r8dEWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twM1QyfeMnq5BSLSjgySUnT_1sNhv2fFx1gp8QBN219gpxFShEF-vLL37vww0L34PM3ztFV_kT8lukyDpfisyXIX4UMU9E3fGHJ_WIOEhnfJo5qgOnhjqSr6UhO3u8FVeSjdk-TRkcgi-R3pNGeT5ibXYWXdpoRk4HpVvAUpPbWHrNyJMM-lBy8lhnz7LN2GlywnanRSFVTrHcRxE4Y5mNUJlX5gnZGnVxuzYuKi-qOAYYJffa3MdAd9F9W1yfeIdRUoB6LsqO8aHtbSKDUa25KlbjvHuS7_QZPJ-5x5aN63bzJgAXVC6uYxYwcGaLlVgWT7cJGhAPQfNsSoSC3OKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-D9IW4JjmG36PYqBAJUhQ3dgNygPPNolXiYRxg0a1uiX0P6x1sEmMKcvqrre4ztQypRvAVA-cPHA-2cCmsdJE_HKHK_3A6ukVQuWKzKALbi1l6c968QDocjQbUzzFxBTkZSMfFQr55v6POSKgGv3y1DTbEWBk7TqDsNjmb10QCQGTnJJIVOkQpWrYG9251WFf09pUgY507hKJg40dtc3sUdFxhlm0a_PyobHpblmZ_685oSpMjueGEN3wI35FGpr6EcZTSNe1QpKSJ2PRgzs-ICCwPzRHJtu36J6dyo6Q6FnsSVWk3gW5oVXPYLG5CcmfBkrRdVuC9jowcYeNxHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=qpZNgdJ85EhVQI3GYnb24NSmd1lqGoSy8f6NjHUV6cohKHO4N-Bu5tsAZ1TLBf5__HHaQtphWYS3RYqaU1FkQc7Lj2FjIaWKIvwrbM81Prh_cS9uA24vT8_oCuhrpgQcT6tPmj3ku3zE7t1M1_pzqT89YJMIAmhLC_8D1hPZH2NgnmmTW3YDIOMgy55JoD4QoK2s4gYW1ZI3sKRa79yA54wyus0J-WC_uuv2nFRkPOa1s-mjc62Jb-MqdNIv23uHbYaU8P3nkK3fDgpXtA4HzTVD5AEUEALircoUP28ygdhTiOlmiR3qJE3uD-Hs57QoVGXipKqfm8T0ZYO-l0_gJJQZrEeWlKHbLMtlvFP-EEUiMqFay1CcPrTEgQ14vnwqua4-tZKSpsfD_CHbGGX9BIcBgfX_GyEL0D--cmP08V-UzHoi83tJwEfMIj2SLURvBbo2dqjmRKtA7F5wqOClGpQg6MDLCw5v09i1zw6CT66pUX7guc0h0U3pqqx-Jy1330CMkBCWpRpDwCm0Ly22fcIISLtHy8FyjfSaMWcDyB3A1aHL0rA5SE3TowGG5dBPczPJNuAt__5LdfHJ9fUTohvogUXgCwCdl_Z1dVD-6Eh1rn_x4Nne9xQaDTCkx999OJMSg8Fqf2YdTh5WSpMJzZn_7DlgiaXQUPlOeSUDK2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=qpZNgdJ85EhVQI3GYnb24NSmd1lqGoSy8f6NjHUV6cohKHO4N-Bu5tsAZ1TLBf5__HHaQtphWYS3RYqaU1FkQc7Lj2FjIaWKIvwrbM81Prh_cS9uA24vT8_oCuhrpgQcT6tPmj3ku3zE7t1M1_pzqT89YJMIAmhLC_8D1hPZH2NgnmmTW3YDIOMgy55JoD4QoK2s4gYW1ZI3sKRa79yA54wyus0J-WC_uuv2nFRkPOa1s-mjc62Jb-MqdNIv23uHbYaU8P3nkK3fDgpXtA4HzTVD5AEUEALircoUP28ygdhTiOlmiR3qJE3uD-Hs57QoVGXipKqfm8T0ZYO-l0_gJJQZrEeWlKHbLMtlvFP-EEUiMqFay1CcPrTEgQ14vnwqua4-tZKSpsfD_CHbGGX9BIcBgfX_GyEL0D--cmP08V-UzHoi83tJwEfMIj2SLURvBbo2dqjmRKtA7F5wqOClGpQg6MDLCw5v09i1zw6CT66pUX7guc0h0U3pqqx-Jy1330CMkBCWpRpDwCm0Ly22fcIISLtHy8FyjfSaMWcDyB3A1aHL0rA5SE3TowGG5dBPczPJNuAt__5LdfHJ9fUTohvogUXgCwCdl_Z1dVD-6Eh1rn_x4Nne9xQaDTCkx999OJMSg8Fqf2YdTh5WSpMJzZn_7DlgiaXQUPlOeSUDK2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxJCdslrg4DKLqYDfQ2d5ObXscGjiWpQIsVGCxf9wa0wEAIcX3diKTO0K2keGG5lteyqfeu4QkwAjKD8MPhu5YpqvPG846_76EAHhT9deCawDh-2GV2Y88VtvLVFVod1_unAV6P67PHmuUu4wi6BphP0INlED666GCcWrNmyIQXqo_lmGzVwGjDZYld5DWKvvt2K6g8suJmezkrQZhNavxRg_3Djyf8rji8Qk2qEO34XpUGy4CKRMLZFo_W6E_Cf-2nT87dhx4oygVVuc-fddCq58QRBVXyQU_vJk-UmhsMm7FYtj4X9zuX3E9w29lNMiysze2BnxDyFo-1eri1VyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1UBilSSEuLydW1x6Rck-aTmX_tdoPuc9XRGkhrA6LS3sJWxKMTEDg46sQ1Rm23h3LCfmpE-H1rSpQ7L23hblsZxl8XVANWaOCfgLw5KZscFNh6ehJNmxEoOaz7Ohm7b2Vmb4S0GmTnf7WQoc94vnAXHUGVfR9RnD6l7i7GVa9WQM9ILQtgPBLG6nr21T9hSTBTHbCKo7hQZ6A9cigoY715T2myq-GG7K_eWLcs4_dmNZ8ITDPwrt9fEN727IbdZ7YuLPBjejp3rBKQoJ1mvde5OJzUiWvxp8snGyNhe8PyEDJS4Agvgn6UsxOcjBBaqMFZc_edaWMVl4_AvePf_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7_GuNA1eY-VzAbkxoq8dD2prPRUGxPS5N4nK_MCej7zo_D7dgCJ6-dcBULeDTvp1Cbaf0gvni_ESuw0DlGQcwM9Pv9-fx8d2bIUl4jwy4H_j242fubkQbpLrAT_DS2wHM3DReNnLA2aN4F8S7KHMCxd-1i1PL-p3EnVZ4WOr4HE57Tg3jDqkzFQpEB-83uPir-e_SQDNGjn12OOUK8SfYFz47b8ZHzaBoL6Um4D2qFNQP7VY9xg8oe2baqtB2MXAmgedXM3_OCDtR7OW5btUE3Vj0EgLfGLzpdVrvb9jgGWh6bn7aO6YSpbMDuyR3UBFFA8NieRXXA4n17wynxf7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdlkWkHZLz-Z9M-FDO_xyezsIMPLRGoAJs3pzNB8EvOWg-CbAU0eYwo2oJemWeauDA4ZZZHFkEf3LqLnrggZ6pe1Hr0O_qPZrBGPWHKfK6iOwZ2a9fll7onNlu1LkXdp4t7POVYYYRgxVscBzBEcM8WDVj-iSSo0tA7upNev0kGhLSseRAKy4Nd4yP4EFfIdZ9BQhteoSwW-hyI2BIa3Og4nS1JUav1lqXaeJ2A1kth7fH9IL5ib59OsCpjpt3cl3vhvfpEq8HmjxYnCzStL9EqOZJzXiLYF9UaaqfsKxil--O6dQRs2pS8-gbS9dlbhe9s-86fwzMWBhDioWZ6UPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=d_9vZ--O22_sxnjt0Wkv3gYiHuo2pKn2ofqSgpQ4d0LGQHRWkLXiiTJz42XdKMFTGS9iYDADncDF7CFAqP-t6CAXieih1qazsWyVzqdWkU5i-2QFhE-gVgHCvV-9rW6cGCTn8K7IXBr2A1FL_HUAyNwROdxlehJHDU1M9GN0potC9fW_9txdVhWyQ_DXEa7yRrN5lQi60YB7GjMM_MZYb23pkZbxCUGy_JsF3cht_c0NHadwdSaf4sh1S4TEOLezv3wa3tMVa1wUxcGCoaShcIYaEZtTfYLU5FgTL6w0egQqnAFKJGFiJH_Qs3babrJEKYL0wi9SdZw1eIZISG3-nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=d_9vZ--O22_sxnjt0Wkv3gYiHuo2pKn2ofqSgpQ4d0LGQHRWkLXiiTJz42XdKMFTGS9iYDADncDF7CFAqP-t6CAXieih1qazsWyVzqdWkU5i-2QFhE-gVgHCvV-9rW6cGCTn8K7IXBr2A1FL_HUAyNwROdxlehJHDU1M9GN0potC9fW_9txdVhWyQ_DXEa7yRrN5lQi60YB7GjMM_MZYb23pkZbxCUGy_JsF3cht_c0NHadwdSaf4sh1S4TEOLezv3wa3tMVa1wUxcGCoaShcIYaEZtTfYLU5FgTL6w0egQqnAFKJGFiJH_Qs3babrJEKYL0wi9SdZw1eIZISG3-nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Wr-z_kYjYIWDMOPUzK10SV2shHXkDB-Uc3f_eI5UETZmsI9-N5DZh0abIZWFN52EI5nGUqRO2YyV0qQX_5Iy0AnxjAZvBkI34WdREjNX7fb5JOVPfb8n2qd1jfrykJJKS5hypiV3JiL5RmJbFMOJjNf_9lLirr3tbVlwbopxdyhBd9I0PyRV7a9-jA48FP5JYCYQ69zJgTie33FjD6pdqrqLyT1c2qosJByb53w-w1mtvMtnvPuv5cNinJTT_sdLmW22N9kBu1h5SB0ZmaPKL0LkAzN5o1Iae7Sh9t6fFUQFgN1Uvg4qY5ct22wdz5E3eeW7TtSYnMmMMrROKCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=mLAH7cR8kIItpnUuUASIVlVBUMEhXsNuOOpS2RC6n-WwtTIxxY62AZY6_schlHA_NJVrWBJN2BuswyjpCJT8dCE-2a8wXWqj7EMHb-VhZEDMut2scy0GnEThhY40WDwHeMia4oxMLGcMWO8A580VMyASLF3swhpLQWK78vlPHkhJPQdGwO2Ls7f7jqIcWMVrN_yoNIfH5gyyrmYDEjYqdujG3f3IWoGLDtVspL_z5_weC-2aclBz2RNPcyKkXVvNdGjl6evxOttl5hZxIuZXQHP6QnazHW06J4MHJJ3P_Vd8l4TCTphbIFjfa11CX5gJQLUa92WppvQ2FyEytNzgkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=mLAH7cR8kIItpnUuUASIVlVBUMEhXsNuOOpS2RC6n-WwtTIxxY62AZY6_schlHA_NJVrWBJN2BuswyjpCJT8dCE-2a8wXWqj7EMHb-VhZEDMut2scy0GnEThhY40WDwHeMia4oxMLGcMWO8A580VMyASLF3swhpLQWK78vlPHkhJPQdGwO2Ls7f7jqIcWMVrN_yoNIfH5gyyrmYDEjYqdujG3f3IWoGLDtVspL_z5_weC-2aclBz2RNPcyKkXVvNdGjl6evxOttl5hZxIuZXQHP6QnazHW06J4MHJJ3P_Vd8l4TCTphbIFjfa11CX5gJQLUa92WppvQ2FyEytNzgkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTu4Zb6Va0ztmYFh_tvDYAyw_nC3uFFskPNu5OtE0fb8rVV4m-oi4R5dljmTDqx1bl3Dc-H2pCDDeKqbWV175xs9QHWTkqMpA3__olM5xkC1Y2kkd3EcDpw-20pFq-CXhREh_I--gk_NdhjtesY_xAlXXe87tEggH_stCp3JhnaLKjy514rP96Y8A9dex2eqWl77-ILoOWuF7RXPRRzwZHeF5133N3dX770FKyFspGlRg11fDp8_nAj_tLj2XVN_84_SVqUM3Az8WyI6kX_0CiW2ZlklyDcGCU3joTJOTIcGu4URORfGLQpDX2uIlj3K47-CRwCreRT2Dqvqa492wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjhC5V3J-ENPFFcsWFKJ0YFJzgmNzOriuQvYejnfzHna1o1_lRK_xsGSprA_tmz17rcVnqedFyoctvgEZlIY5BQidJDzO2j705HAAO_G4B2v4y71K1taxmL5xISXQeE7mt_QkVcDkUbvRkk5JOgmlfZiCVNoirqRom7ljNyljR4AOYQD0tTAzZU4XowncyBwC8g6JUVHiJuVEqhgkVnvLOXdiBkMMTTe5lSTwO99EFfFCyru4fKMG_YShsAaHA8cqGBCjbVfHM0NZqoS1VvXrG8tulCg-7HHK8fxSuo50W-R0DmiVClwLZOqs7UZlZGqVePjxzQdZAxMSfoEQ4GlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=clbg_6l2xzXDrbs6UPb2_4GvPKqRCY1ArpVCjsfU0UasbGwS1LF5VynfTmzvj8GSKelQ4Hai3kMk9SyWOFI2vRnYAbze4R33NCWVBkZTdiZNdxMY28dP6nDiwPRkR53-sbNI6DJzRu5QskV11_Pon9hjcX7NAOoa29O2e28lpeuDrTcMRAi9Ngmk7V2Zh49BT0vHxFWmeub8dk95-1liSfTSOvksrbTkYawK2ciCL1YVown0XaeDyHFbQ_cVpCG-vuWiiabW-ynr6xgheLYmbaVylELxrIMaXWNohikV13wiUM4ZesTLTqQi6xJ-CuJxvXXZB-90cIw8k6gee3BjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=clbg_6l2xzXDrbs6UPb2_4GvPKqRCY1ArpVCjsfU0UasbGwS1LF5VynfTmzvj8GSKelQ4Hai3kMk9SyWOFI2vRnYAbze4R33NCWVBkZTdiZNdxMY28dP6nDiwPRkR53-sbNI6DJzRu5QskV11_Pon9hjcX7NAOoa29O2e28lpeuDrTcMRAi9Ngmk7V2Zh49BT0vHxFWmeub8dk95-1liSfTSOvksrbTkYawK2ciCL1YVown0XaeDyHFbQ_cVpCG-vuWiiabW-ynr6xgheLYmbaVylELxrIMaXWNohikV13wiUM4ZesTLTqQi6xJ-CuJxvXXZB-90cIw8k6gee3BjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=tw3Lt7wjkEpzw2py4yaWBaP7auv3Da1q6Uw-tdpNw_0C3p1o1lLtogsnx-UzuZTWfb4p7XrOkElnQOVdEjTLNGl6goQ2VdOI-OgahHyQLChUMgBq0OKLJSJNuw1E1j-d7V4cdpusD6sTOWRRCIAk7FEBXMwb26z5kJO8-ymEOX8pIr_n0fZXjHtM7-oUNcV0AqVmC0NJ8T4NL1lEkiGydpgcPwoJLamtfzbQlG0nllwYMd25K3GaB4ZPiZxdq3ZbAcF3IP2QmBJfdRBs917Pch2yP17PpmmGRQWGhCVEnqrt_Tk-CTt_DoZL-mkOxXUobCix6KXSxmp-SFDmvGK-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=tw3Lt7wjkEpzw2py4yaWBaP7auv3Da1q6Uw-tdpNw_0C3p1o1lLtogsnx-UzuZTWfb4p7XrOkElnQOVdEjTLNGl6goQ2VdOI-OgahHyQLChUMgBq0OKLJSJNuw1E1j-d7V4cdpusD6sTOWRRCIAk7FEBXMwb26z5kJO8-ymEOX8pIr_n0fZXjHtM7-oUNcV0AqVmC0NJ8T4NL1lEkiGydpgcPwoJLamtfzbQlG0nllwYMd25K3GaB4ZPiZxdq3ZbAcF3IP2QmBJfdRBs917Pch2yP17PpmmGRQWGhCVEnqrt_Tk-CTt_DoZL-mkOxXUobCix6KXSxmp-SFDmvGK-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUpS1Nr-bswW1auQBZjQw1mqFrNHE1A4c1UQP6qhbOoiuXAAYJKcoYAqYpOKRFdVMs7Qym8P38-5AL3fAuB0FXtB1d6lSeifY3TMTd0WrrRzi9VKWPnAVOleU37_ywaxCPQgBfP7n4dZ_UY80MrkL3ddfG_tuS1lr5c8B5vqvCNOxs1_zNdncf7YU9Ma-ENQju138LVBIjwc8KEF_TByXB1mpiUqkCPXw8SN6mAuh4KF-1uMgAnsYAo7KUXnO9aDIfcOeVlDoRWdIj1TjDJB-IIW22m52rWrCJUddVVjmJOPLPVLnexSrToPDrWvfwcVmLeQZNlpZY97mgibhBJYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=Jnsv3zT41e4mj9nfxxeqKwpIb32C1qhpbIJ9y97QUqmKJlfeqLhI2Jsb8NlwZpSxnTR0Ki6vEZ8yxkzSFjCgH8dGUBSzDlhF7vKeXUQX1ubO-ajfjGR4vNrp5q6L9BxXVsqjvIq7y4GHfsF-f6KajeYODXZMRFp0dl6uIk6WMgFjTadGiBCpRXsQYF-DQDU-bnGdZkgmZgEkdJ25dx5ioBY9FgCqHH8ZU-0UPxJdl74mzpGe9_zxFGL_r5r14dDl8T60sJgJroyFzCvgnBu6oGjQ74Ohlybw4g2wpT9sFHavauuCqYRqRbh21UuZ7TFY53lpPsaTdAfW8dc_E1Tx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=Jnsv3zT41e4mj9nfxxeqKwpIb32C1qhpbIJ9y97QUqmKJlfeqLhI2Jsb8NlwZpSxnTR0Ki6vEZ8yxkzSFjCgH8dGUBSzDlhF7vKeXUQX1ubO-ajfjGR4vNrp5q6L9BxXVsqjvIq7y4GHfsF-f6KajeYODXZMRFp0dl6uIk6WMgFjTadGiBCpRXsQYF-DQDU-bnGdZkgmZgEkdJ25dx5ioBY9FgCqHH8ZU-0UPxJdl74mzpGe9_zxFGL_r5r14dDl8T60sJgJroyFzCvgnBu6oGjQ74Ohlybw4g2wpT9sFHavauuCqYRqRbh21UuZ7TFY53lpPsaTdAfW8dc_E1Tx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=N6Ofq--yTFDgKtQbEy-SUR4E1EU4v9e_eRmGfZsTj7Z56Po64bsUdan65nn99OEyjpgut7DU2rZ20xAIbJa_AMROQKhAk_PPBlYnjDoEh2puxwQb2b3d9JQdq0GBfza2yC0noo6Hy3bHtP9lvFw222YCYDAt6mNlMUe5C0SbK-W4nmlSLk3viXfuIvU5JaPFmqt075yqIWpqwvZ3pUuhfqPjfI4QGbqD43G3U73pJCBn8V-NqNI7lT37gHtori7spgLtTjdc6NXVs2A2VreRFqL8Lq2Uq-en0F9mCs714ohI3Tj1rRIVwQNFjAdfFXIbm-Q14yJAcLTIPOJ0QxUxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=N6Ofq--yTFDgKtQbEy-SUR4E1EU4v9e_eRmGfZsTj7Z56Po64bsUdan65nn99OEyjpgut7DU2rZ20xAIbJa_AMROQKhAk_PPBlYnjDoEh2puxwQb2b3d9JQdq0GBfza2yC0noo6Hy3bHtP9lvFw222YCYDAt6mNlMUe5C0SbK-W4nmlSLk3viXfuIvU5JaPFmqt075yqIWpqwvZ3pUuhfqPjfI4QGbqD43G3U73pJCBn8V-NqNI7lT37gHtori7spgLtTjdc6NXVs2A2VreRFqL8Lq2Uq-en0F9mCs714ohI3Tj1rRIVwQNFjAdfFXIbm-Q14yJAcLTIPOJ0QxUxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTIzqSORO49JvEHCuo3jLYq5B_cADwAp9a0tcDmC8NbZ4RSCaerjDH3JNd56Usp7ZAUiOq9a54FnuxvERq--PO-wxwZ1cYjW8_vSWgcoAH4go87IKqDJyy3DFaDCxq3WyFqIMnLkdfdCFgxxk658bhwCp-CG5XUs0zp5uwp-hP4yk_YG2Ho1EXyl9UI78-G7lz4kZ5uD9jXFd72zlsFwVwAK8EJ0RzLPbzEOztMn2e5bqMmoDkmDqBqG8ot7NjF-GNQPWVAKchtGB8QNZgMnugAOPbRsmyCYeK2ySbQ9ucfAqJUjKOgjqlogkdE6aS1-L5HFzrnseUWfs4-lHlESOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKTAEy7j3J9whYDhVHJyz5aBgH_tlTMoxE3DY-TSO6g4Tf4Hn8rJQzcPJQg9x90gSgTwWrtzOxyQmN6wqTFHRYwJlc28-ek0IMYYMWdNjW3H6B7-WBX_DmjfWE5OGXeorWMUSY3WkFsGuRN-r50s8MuKKAlm3aVxVxKhtZ9h6tto0d0L-fJL1Vm-XFta4envycXMblqCok1a6MW-B3wG-3aazQXjlkag3zIx2xJqtmBeGMvbVIwKxnqb4Lag4N65FLycyC3GUTu2QYYd2gXnFOS7QfsMjanSlnfjQZ1swzgpNF8uBFnKvmj1LzoyIcZsWMoYYkyu2ShRb0-dlpK_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=eZ-v_2MG4bYbmzuNAFW8eTr9yLyi_5rAk4Ergfyq2w4oXPn6L_h2_wWilNScym1sPLFRRGnlXyu5eKYRZm3Kx4nO6WlXj787M5Y3Cm3fSQKVVKK1rdQqjBH8XHS0L6M2Grwb7FXR_GwS8IQ7IVdtsL_01XR07V_irMOz_mgKlbXNuke003CDqy0FP-YaDF4mpmNE8jaYPR26AT0NIqsIBR4ppnP1MPyYm-rRdlSV10-qYXZV_YNy-Ngy7InxcflqKXC556oTFXHfRGzKUUYe5YVVc-KDLJ_X_8Z9_cBFmTzP7mnB9fA_puu6O38is1DWYiMyO9G5dq_SCUYmvlHUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=eZ-v_2MG4bYbmzuNAFW8eTr9yLyi_5rAk4Ergfyq2w4oXPn6L_h2_wWilNScym1sPLFRRGnlXyu5eKYRZm3Kx4nO6WlXj787M5Y3Cm3fSQKVVKK1rdQqjBH8XHS0L6M2Grwb7FXR_GwS8IQ7IVdtsL_01XR07V_irMOz_mgKlbXNuke003CDqy0FP-YaDF4mpmNE8jaYPR26AT0NIqsIBR4ppnP1MPyYm-rRdlSV10-qYXZV_YNy-Ngy7InxcflqKXC556oTFXHfRGzKUUYe5YVVc-KDLJ_X_8Z9_cBFmTzP7mnB9fA_puu6O38is1DWYiMyO9G5dq_SCUYmvlHUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e629wJotbIqlzpatqFcjKDj2J0k51kUOe6Sv4cdXQ6z1nzYVic1IfbHkSvXxnWUayjamx7zIKAzIvLQfQRlR3FlujxpxPThVFhz_BUUnhxvbU2LXRAStUmUlj7IoPIiZ6R_dCZrN265F_YbbfDwD7fFeqTfsQvLQAaZgCjD2W4uczQ3rqxHrQuas21ZnGeN2Eu8zQeZGAh4FuAPnVwY0s835eaCVQ0u14RE44Hz4hFee2fDfu6M1DSME6z4XJflHbz3VyWVS9K3lZPPj3wF4iRg56V2fb_ayFGgnt_tthLgLrBFGtdhch7vPMv-K9gGsfHWGLPYgsvSFdt6vqE3Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4WyDTcxnFxVXFS11K_dRCL28GxCiJ3o2_mAIASR4ObzZ9GAJ6YOCwZXQUrHjN4QYj-qtOJn6jTLyElT1cTfer4ITRtX8vJjEZVWiCg2n5_5Df5KIantuRnKa1sTMs0Ba19O6JM5YN7bsy6pYy9Yj3VMjqWtlBSbYxyHjQ-Nmk1yF3biUKxO3i4UunQL48rVIvC5ogXeHJFpdAQDU4hw31r4tYfKBm1zwznkYNPK3psvgYJwbueiNbjCXVvaQlNeR5W0SYQobVrH--uI8Y46d4YMgyM8lKkzDClsXC9WM-I04LPfgX0c93JctnreFWjDH6I_smXiMb51MucNuLZr5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-x9XORl8SpXw5zO1vd2p6atpN5ePm-85hGj3Jmokamw96SU2Hb7JwTV9YSG-ERyPbBXIKco7zdkTnd7EE5dIH8NSURXh2kaQdfxAY8735pMxMLUk2hw2MxSpZw5NQeRwQE_8C40gdPYkLi25dj5M7HjoisVonb9basfZwYZIHMxI7GIaTSTAORYd2AADNDa-2n1Z2nYDzXN6ittSK0WpSc1K_TJupirlAXZbDCUXiih4sgqImS2iTy9ZSLn6gBdpj5rVNE9-EX8980yHQjSy2uuFRq2ppjCQlU1E3FTWmW2LOTzx4iWw-AdMORIglvNCKzQCpP5umgDZF8dzSx4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=jIk2w--FlIFinpzz28SbEjNq_JD_KgVRD3wdL8_uJHYaMYRaKGzX0hWBYLgQX57bPmmqtk6Cv_-Qc4NrS-NvsmY5WqG02JV_QeA27p2YpQGmuzXWHyKfCu1afclyp0YkKwgxInJoZ0bVTPE4cFhenSOQjW8Y1Uv_VhNADUdZniwWWroJwRrIioP8Ci4ClmjtEWljIJpsJd3SokjC1TOlkOTckmwKwr8jQGEJheLihBrSWk6xytH87Q2n2fYIrlu_rDDUv-tGNa_ZWy_3fiP-2EoV88fw_0KRqR63lrsAVh07fSOjJOUYqfwpBLTSQNKYL64e-F1HWLwC7o85953Oiw0-z3kVllDk_9ikmH68o6Gj0nXn1QVhj0jYsH_nYu5vFC3Fh0W7hUc8hAzy_VNte1r8r4c-xewcsSUMsdH5QWJN8upbybTto5klmudC6FkKwPiiL8zQfn9GBgrFNjZWuk5Tfn_-pXGOU3_ksGkdyN2e1YComBQhmrKO1W69hU8hTLTpCXPF1Oj5QJqiiiUAeFY3gfFH0_oz_Rn-3w7J5rTtfkxKShHD0z3vgz-Lag8rCFlczT3A_9Cz8BffHw9mwY7RYd9H5Mmg1WuCxRg2CmzD-tw7MN1giZip7zXW_wLGkjIUl4P6RsqgfI-IxCnsPbbBRTd3rVglL5kK7JnBFrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=jIk2w--FlIFinpzz28SbEjNq_JD_KgVRD3wdL8_uJHYaMYRaKGzX0hWBYLgQX57bPmmqtk6Cv_-Qc4NrS-NvsmY5WqG02JV_QeA27p2YpQGmuzXWHyKfCu1afclyp0YkKwgxInJoZ0bVTPE4cFhenSOQjW8Y1Uv_VhNADUdZniwWWroJwRrIioP8Ci4ClmjtEWljIJpsJd3SokjC1TOlkOTckmwKwr8jQGEJheLihBrSWk6xytH87Q2n2fYIrlu_rDDUv-tGNa_ZWy_3fiP-2EoV88fw_0KRqR63lrsAVh07fSOjJOUYqfwpBLTSQNKYL64e-F1HWLwC7o85953Oiw0-z3kVllDk_9ikmH68o6Gj0nXn1QVhj0jYsH_nYu5vFC3Fh0W7hUc8hAzy_VNte1r8r4c-xewcsSUMsdH5QWJN8upbybTto5klmudC6FkKwPiiL8zQfn9GBgrFNjZWuk5Tfn_-pXGOU3_ksGkdyN2e1YComBQhmrKO1W69hU8hTLTpCXPF1Oj5QJqiiiUAeFY3gfFH0_oz_Rn-3w7J5rTtfkxKShHD0z3vgz-Lag8rCFlczT3A_9Cz8BffHw9mwY7RYd9H5Mmg1WuCxRg2CmzD-tw7MN1giZip7zXW_wLGkjIUl4P6RsqgfI-IxCnsPbbBRTd3rVglL5kK7JnBFrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQjnEd9VhnI18SjG6FQ9LDN1GAi5gqYPUft0lKwkFaFD47VHg5F_uw6kUb_3yzZuXcQCVW2ipXv2fKLkwnPRp9MuV7dSpDLuoMsjEnDxjC3O7Pewna0rXZFTBgYiuQgjpxXhKCI9RoSd4PChlxQKB4nbYd4NQxARjU7XVxb1BAz0AoPL5vYEtpeYWYk3u94nibfAqa7F34DAZ7CTpLY1BwwjEZ3NBjIsIkknSWulm93AA5-SfwExTr8yCt1WeTFFJA03wt11aiEeKnJ9v-IEEU7NxfXwQv8MU-GDiZHHV-IyOkDnSkBH1flfu4LHSzV0olijKfY5pXPdi-6AmUJPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfLmfretm5e1xxNrBtTm8rVd6WIeIOg7CzAw7uliY418i3UpYFSciiPXjk-EfYyotrvWW6aGHUOBQTR6cp0XdN5sbD-XJzmRayMXZ6Tttd8xXVgM650ushSZm3c4TeJAhTtQ0Yv9eHPC_-_2BbgPCaDxGXyT1MjQHuIjA7RWFFxhk2Ng2OibflGg3pOPYSXXSJjhBq-XEzNksxIx_UBxptWrD9fdbjUxfWFWNB3iCinBrhcHXF384_UW22_tR8DrUmCPhcn7EpWCBMiG9Jx66unH_8T1LaxB_GN1D7k4KQkaVfXRZ1Wr38mEa4IBZrInIorFu_-UlXkz-sleT7ETkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=eyaN-cj1xLuAsQMo8nHo2ToijBkp21ylYcXyaWg4zJ989Vm7EKlfctooSAwI04aS_K-SZJ7JIzyFYM6CRxxffYJbPYVcqEGYPDMwxrQFXZ8fAQhAb60T4I1lrxRrsXJebB1f2ETD-cL3_TonlEtW6KouIlwPLXJivzGOUNouCldzcvGRgdVRhjDlUHLdz4qnPXzlpR-075MGbZuABr9hGEPxtA715fAeve3tp1ymkwBa_mCu4ucIHGh3uHJSs0g3qYrtPke74ZLrjGUoB_lRqFS4_IOSk1HULvoLXmqBGZ0cO49imuA4Q-ioYmrd-6Bhc8hYRIYR_oeyzZ69azaGgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=eyaN-cj1xLuAsQMo8nHo2ToijBkp21ylYcXyaWg4zJ989Vm7EKlfctooSAwI04aS_K-SZJ7JIzyFYM6CRxxffYJbPYVcqEGYPDMwxrQFXZ8fAQhAb60T4I1lrxRrsXJebB1f2ETD-cL3_TonlEtW6KouIlwPLXJivzGOUNouCldzcvGRgdVRhjDlUHLdz4qnPXzlpR-075MGbZuABr9hGEPxtA715fAeve3tp1ymkwBa_mCu4ucIHGh3uHJSs0g3qYrtPke74ZLrjGUoB_lRqFS4_IOSk1HULvoLXmqBGZ0cO49imuA4Q-ioYmrd-6Bhc8hYRIYR_oeyzZ69azaGgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOc0ZHxgGxspjvuWsW92_Whdl8NBWfx75ugg2IX7fdjP5VupbIJcr9dEnDsQCO1Zw7h4bXxKT1zUQELXM1BKSdjmmHgMAvQFeq7BBPDD4POnyfMooPqxLRHlvjdR0tRI47pqk5Ynd5VLR-fzCgBMfOl3Vzy_miVLWfpGIauAGGGMdvcSFcA2O_G2n2cnZasR-odadvAj92KVAYcO8zucUKRdRRT17Gg6qWaXAmzhQ1tNaulfEBQCnRkMYP16u7CPTQqUA9D3hOPV_RHu8us6qwgPMvh91W6JyFaDXo5b7iTd_TRa8LDF9TPjBdogIsr50XJrHzPstJG6Ec0Q__WrgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO8cZLERoTime5WNvmDXuIdeH5AMAlwvqJE3Lyf_sGvvFJgsnox95m1PAlTRf4gb_IhqaRiVNlm4oUTg_m9PRyAry4fEkiRobptQk1VpT5iiR-hLrNgSkXlDIjbvxYgBa5hlSBpbH-RtbRcGusPW9GcssTIFge8xFXtWsSNRiR0BMjDeCPzLHxyAmgCkY_rJ-ROJQ-Vep5oAn20c2f6cwwvGtw6A3f2YUyv5Dsch8k128oZDQJk5IU1NHwp2x36FkmvfNn1MdEArilJV4JLT5GhNg-nbRZo76O9g1f3gQAp3kmBbUSIR3M19rB24za3LUjgdM6QNOV21dmsmvslfzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjjBLwqfXJI9HKIy7ytkdioVVLSVyEhu3Hq00sdMCETHcCkAzcDJ3Zh7uPwQRor5PVzvPOgQxltPVDwoQqZVSSonm6OlcSstAdxvdBOhTPE19a5PwprLUuC6mV_2ih3EE4fP9mxkBoGf0K9oSEZpQgFudjvbJKLG9P_3OLjp5VUnDfxtV9yDGAlvy0e6J93KFCTED_sDcLEmtFb4zia1j72AIcfXUyt2tSeKrUc2aDJS8JpY_oYvlqhNg1_bWhC4O75U4umfUWdsqHaXMBeSpela2DFRaOby31WkPn2E2fjRuuDaM24GANIF2cY0vO7FH3D6l9axxCpKV6mct7xbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrfiCKXtGtZiuyKSjd-AHaF10HxpUZ5P6BN7IO5jFgqsaa5n1s6VXIA0lT0zxtK2KNqgcSFX_gfo4RyxcjboyJ2_cplJ008LncAtzKSKJOGSgBLb2waX3A_L-1Rbo3jXsystmFp89DIwwXKhvsJQooy_3w7w2tsqGUl_CDtD5syC3mYOxRtqtvDZjDidsI4Co9WZ41ipZ9K6r_oyB6Hb22mtVJyZLd-G88Ja1O5xK9-toR3kTfD-iguwrAX4xhIsGBwZ49Pxy324HBA2kvoPfbJyYCU3NBevxuRy88tRRHrozEnXaGlbC-ftzvsAn7PEKer06L3kJ1pgHYuRFz7iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN3q9fcW3Za78GFrsyJfTISqGZOV-ZyoQw-YEiQicgwfCWShvr5Bun5-JAo5l4Vb-JriPy1_6AiQEToCn84gVqTpqKKgbuZH6j_0Nuix_81C6Hoq2iknFVnmmMtVFq_29griTbEmVyyX3mj9-Jl4tx_luHfxL65cKYJnyRGt4Cd31uawQfJnCfJcKsHCk1PtprLlU9N5PRx-Mkfzi2hkm5mSTquletGgI8umgAQ8Wo-UO3RRKU4lXGrpIJ-wLRfAvRjeN7x9ck1lTrJoDrdDQZq7wsax4kpAQOUBQ2VLkVB7d4swneP7U-cZkhgEYF_zeSz4hDDSpllG1T3tjYsJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsHuvXDFM2OpzF1uaP5Gt9ONBeMRg7zmHbgyR6l6P_WDYmXh3KCbXl71rNV5C7oGiFdyvzHAtpsHbGeuT6acD8q-f_b3Zx4SbMz6Ao4SBs4XyDVoLaKc36WdfK25JUOHAA4ygrKYHZqGf00SkNrLiqvEbwgDNM69ntqSrgCkekKLwDytPOM-drjiH5IQwBEtKSEEAYcB8Ieo3d-pvi89cji9jp6D5tjx2tIMsCNBicPADl-Ac7KuVO78iUyOq4WwFJOgVx6Mg5n6JodyF8FxZU-jw5Qtc78uFI4C7c1RXCKAct9q_mFJ5GFh_DK9xDP20d7O7qMtn2RrkTsg-kpzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APtmQO8Z0cgGYZW052he-OYRNTRYlpP9EFu6bTbz7Uguh0E33EIrVSU3fz9-P76yprVODnqODMYalyubKpxUjxjhe66E95bjKYDEUS2yK29JFse4L_eO5jgWkNNO68xhu466xiqA-j4NtYXtJ5-I3gDJbqIkum39db5JEQJ7N2m5abog7k0iCD8ePvfPq2HLaPEOrPQ6Sal-AMeNgCyBUlQpFbuIcsaNParkxwop-G_w5NVW7hq-VaRDF94soVk4c08_6CAlE0etPFKImkZAFEAXPSdMTSdtFf21NKRkY0uE_kGGEKf_kUj48TNZsbyJXrnIgzwOB6FIcwYofk47Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFS11riudmshe8oJUoCWkJZuRmoL7SL0_JlXFb5LYt9R_f_yzobgO-Hn_-dlQcK0K8SqTP-MaPjQHjE-gQNmp4GZ7ok-aHun-Il9js-0uty1_s8mxM7AWPvR2HtEMJyrQXkjSRLxbKrevGgwYxgDzW6NtgdFuTXxf74HaNuJhByJCgWiDW2ZeXXbsaefnUMsPaVD78a9_LQ4WPEN-GONSlfIlafGOqoXIhbq_AiWSNuRWWOc2ZVggo15tjA_bx8xeIlRnLCZbgegINCqCKOHKbyusRReNZBnhBgUFTejZCGJAqExZhN28D7FIJICRHxWjixHe_gPuGmY-oPv3TN04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=bpxlf0FV3wXr1t44nCPTEc2VQKxY7I1DUECIvcAWZ3ac9jQdEye4_tTuVMYVeOJdxDTgF-EWjLvdSkDZQpmyaBjSFe1jhAuPZskY-3RrDgGF-TVPtbuGn_WRqLoUH9puujoIvqucSc8WcZhHESa9MFlBhQxQqAVSxfMMR8nRwEbRqePcfdM3WI-VzzYvX5HtJAiSsSI-ycU-3LIZBxvNpSvFFqAvJXv0qDU05hmMLN7VaWYs_8F9q_9A4PmquckT1n56A3gkXhyki5UEinpqLxfpecLWUSgdnrsnWlpM5JgebSXZGlF4G8u_em15sbn-X82l7gX8YDgY00A_Fe3XgkTpyyJFKzP0glWKj50R5wZB_l8f-Xv-e7zubG4vCnDPTY7IV-HPm638oVPUsIf0qfadrzqmSHwQ49FZRQV3JnniBqp9wIHUmJKE20fAV8U6y972vRKJr46W_92o-BLitkC0ZLFsYsfZp8YxJIvvfCTwaKrmeDM1mNzWZcq3OirzrnCt3UwxDuD5V7wTEDzc7a9EOf3Skq_TBLOsTHPfKjhU0GlUUTQaSM9qJgc12DeSs4lYJiaAOL_ecYRLQiQbProYTAOXtySixgcva3sRLtbT6EBvj8IYIFdjcnmX4lriQZt6XOj7ZKuJolO6YwkP9V10wizMpxlyL_ZLlU11ZBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=bpxlf0FV3wXr1t44nCPTEc2VQKxY7I1DUECIvcAWZ3ac9jQdEye4_tTuVMYVeOJdxDTgF-EWjLvdSkDZQpmyaBjSFe1jhAuPZskY-3RrDgGF-TVPtbuGn_WRqLoUH9puujoIvqucSc8WcZhHESa9MFlBhQxQqAVSxfMMR8nRwEbRqePcfdM3WI-VzzYvX5HtJAiSsSI-ycU-3LIZBxvNpSvFFqAvJXv0qDU05hmMLN7VaWYs_8F9q_9A4PmquckT1n56A3gkXhyki5UEinpqLxfpecLWUSgdnrsnWlpM5JgebSXZGlF4G8u_em15sbn-X82l7gX8YDgY00A_Fe3XgkTpyyJFKzP0glWKj50R5wZB_l8f-Xv-e7zubG4vCnDPTY7IV-HPm638oVPUsIf0qfadrzqmSHwQ49FZRQV3JnniBqp9wIHUmJKE20fAV8U6y972vRKJr46W_92o-BLitkC0ZLFsYsfZp8YxJIvvfCTwaKrmeDM1mNzWZcq3OirzrnCt3UwxDuD5V7wTEDzc7a9EOf3Skq_TBLOsTHPfKjhU0GlUUTQaSM9qJgc12DeSs4lYJiaAOL_ecYRLQiQbProYTAOXtySixgcva3sRLtbT6EBvj8IYIFdjcnmX4lriQZt6XOj7ZKuJolO6YwkP9V10wizMpxlyL_ZLlU11ZBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T34OQe32GmV63m45__R0qdRPIGCEa_dab0mOwukPpdZM-FFUC88nv4bbTHGq8-PcNvDYzea8vG6PrEk-4X1XVz2avTlyZOVJWrmtcMSvgBuSmQnkJ4wVXBeD8j_YpuOwh5ra6hWaADYMEsIzu7X1KqlYHoWqrf3biz-ValBrnKuXPaC2iOG1vvEDkgZUBrRWaXN7iB10Fn5s1s-Exjd4z-yuGOukcvqPJdq8lA50Qa18dW23We402Y69RcRAWw2k8tw7BkaHIoSU5PlO94XC_d-Spy8p0wE8caZEaB95y-xGXfo4xlC13plBQ4lnuFF3UTz4WYK2fbUqn8cpN8ff0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1kSVNsLbDTdxjyDd4z-R1VYv30uph_MsLbflZtDxJxEGlbl46pnL8OMa_Q3st8Ljv2LAkwkppIIhsYpqBnW5uHTdCRsCpISe-YkpAHyDhia7cBeAzGsShr3RIpQFcosKBdCYvmnRhMoQkQDcsQBpTH7F-TpJrsFExjhQJGFKCLy3eT0Qnt42UaopYKc_R4g-HB635FOEgNEFp6i60Wz0xlXNBEHNOFMgqR4IgFaT8UKpuIQZPF9t_x0kSV6o5ggxrb61Wjeg2qFv_CjTRKcnMF0yYJ0BWkZVlw09iBRhqGftnBQSBpCD3jHUQ7JEvitb_oVUGRxND8ODH_3-Ajwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7zjyqBiAQ-oRhXdXbbUHKiNs1G7jsmUagvmWeGeI9qpCDZKrREwNQoZU0hY9pQW5DH8WxsuoEhBri_u1FCSQOXzOBVLrXN5VimKDYkuVELwcJzaqQ3gy09udK3T8bhvdj13ixUvh1ip8i1di-iXahDc2m3QonWsmpJMvVUOV4gFqC0XGfAO2k_EWziAnJEWLvqw_j0QsWXqpeJj--abJ6Ka6ES1Qh_aucDTMst1L0mjHHeUFykJs-iDNxWVrVxJxI_K4gFZbffXxKdxQh0n6DMEU0aKnaAi_2d6hoGdj3H4FS_g5K49nlYjP34TeTEJ8Jmuu1aIe7J3a6VbUA5Buw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ive3NtdIUuvTWifr-MAWewxN7oqQCt4hYvTRBxNPIECvDq7KG6YzKq_gFsawxzhlxxQFImN6RZVZs-DnZ_ptqrtFq7fwzXyHc5aRHcujvpawC_EfC-rJUfdS6FMsjbcNJTxfoS2nKmwDD_H-gF6B4k_znfeF_2Rwvc1JhCWl5f5oDQkrMJKWtAmBI5tdvsyrdZMA-SnH-fFyJ32O8OegngjuAHwqo-Igx-LGe9B2Bo1u7-W9sxmc_ZTDnwdGNYeGP6OROl1kSl89Fm7VB9MQh4wdXxVVoYJjzUvqT5yGLd7Ld4rQ9hbVyygZTChPqxTOjQbMbGWB24KL50IS6pJdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=HmWt9QQMMSdqqZqXOSOVXp0lMNhmcMpcfz4Yhf9iqJ0Ye08OjIHR50tEZQzeyaXFm7Riyh7rB-udfY4Tcr5B1SBBd87djM2vsm6Xs9KjpY6xsfm187HLNm4R-CDohHYCvO75YOHXqqEMCJI9vX_0c3yUDHqzSrJnWONbOtKZDRcl-VHWHe70tZZfzebsaEB8oNf6SI5WabQ_vXdOcni_qAlBth63ZArhPjF46QyIlAbSoVuVEkiH2eJtzAjTfEEoGgjpK0xL4cSEL0R9F6VKMRF_aaeRNxMkyzNiUxPx24fa8sYWIq26UjTWO-33m5Q5fQZj_Pjli2vbM45okoNEkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=HmWt9QQMMSdqqZqXOSOVXp0lMNhmcMpcfz4Yhf9iqJ0Ye08OjIHR50tEZQzeyaXFm7Riyh7rB-udfY4Tcr5B1SBBd87djM2vsm6Xs9KjpY6xsfm187HLNm4R-CDohHYCvO75YOHXqqEMCJI9vX_0c3yUDHqzSrJnWONbOtKZDRcl-VHWHe70tZZfzebsaEB8oNf6SI5WabQ_vXdOcni_qAlBth63ZArhPjF46QyIlAbSoVuVEkiH2eJtzAjTfEEoGgjpK0xL4cSEL0R9F6VKMRF_aaeRNxMkyzNiUxPx24fa8sYWIq26UjTWO-33m5Q5fQZj_Pjli2vbM45okoNEkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6pkZzNIeYgYgtvgycpN3IHMtme8OgfXaacIeY6ROVUsx9dSQH1r9y4hE6iti2STmByyeGmMxroy8dFo1WeD8dfzpZIswY1WHELfzW0Au6_pC7A5qtByHrrIfWbTt9WqYpTpqAa0D17ZlEMREph_HgEVbSB5wc4E39ktiK_AnhaPDlJtdmUMhdjdRDpj6H6ULkOJ_rIzvublbnFWQhn7rKGEkfQJWXa6Ptzfmao-gKefgEDCXTZgbmHJGvfQH1rFz_Z1e_kUSSKzHfWKCSpWdjkUXkV9BJ1k-nfqe42MmXmaq8CJk5PUO_U7Vbk5dFdMUg0AtP-jbmD-SLaQdXh4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4UhziIDlWL8OIDuXuFdNfN_VgxMzy7rVuxb6Z1jWNTxwWybt23pXG5naTbYAAVBmwCrH2CrHgW4nb8QBCXCJXWyOLwnjWyVGTbtRkCiF4P6Gfx7YrQWKhDH-mPaI08EGq5wavoTvDTnF4GYzVBPzDth1LfJfBQABcRIgqbZ-UY_uclkU-EANbyfAKGGB8NnNc8As_arNtxh40K8Mk2UFEBR-RaUye2Q4kC2-lYqI4BRNdaXm5PDo0-6VJQ1fd2CaZ4Ri_a0juSnbrNGyfdHd5otrVcPdiULeLLUiYJmeG9me_DHG-eQWq0rJenOzt7LcaSLyusHaXRF2-531F1OrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2MoEIcw-uHrjawgiz6EPncx9QhO5dqSHkpAsGhlx-LACV8-wGVMPRXV3hOGErfE40_bZG1DzSdw9VO-jDtQAb8ltG206MZvtv5cSiqpwn-f5ObJqin2EGWvn__4YtxFB1TvsqHOjWB_KsnzgTcfCfO_YT5oJPrebSqSIzB3f6a91uhH3EfiINdDf-nHBdhtCWdatCH7IoCPnOzIEVsucGrycCXexGQkKXIi0BrJmta309uDewzdmfUiTtd7k74-PPH_DM2WquqS11LYvhs1HRtQFuJYbgfoTfb7Qej1eI-PjDM-AoLOLAvuBlYpw1O05GytmphbZt-MfVMXNGZEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF1QAOsFHWM-tZaRokDPOOGm7MNymMwC4WBE26MXllfS_zbwAbjkTayfk-yRwy5kvykDcNIRBUEf-ddX0IqXVDQ58oO6-BiQKk6c69t2NlkwdeZ-AjsfUVndB4nCaXnJZhT57axCZZkvV07UJOpA_ryr38NWxVnZgpa-rsp56kIFvodxPvq8zkVK9aJ1lbnBNPMfFz40nnJSLuZjASfOi67Egl1xsmOn0It4CjWm0Jt5BCtPGtu_m09XIuH_nOXMuJ2Qgv53hiX7P6xtx-fBR8CjwOn1dk8TTlU804ueGkRiCDJeSB5d4lyoD8UMpjRLN8yG96RGnRFpYUT1an6JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9rh1SItj44pBPeFXB1jR1ENQWM559xeLjho3fxGD1MJaAfF_7AgLH_rgO_Qsx4bw5xDPfa9LJm9wYBNrsACHIJPLmTclf-MZBvibHCeg8OdyDJchLbyXGTHMbzmVRe750mMecKoRXpu7uZRfktXsPw01O3-e4j0ODRsd5P1FE9KeexXgVdXS9fwTrWY14nKvHgPebOI0zsfmbXuQ-k4o_bAglXc5MKnTQUw8A3U-T-GvRW1pne2MDxZOQ1ahWlJuo80iA0IZI2x4pqbfrci8ZiJxXJ9AzVGGh-rSTELd7x5zb5GgZ0UX9l_x2JT2joBXntndxa66Uog_STm_mh8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-s7au2b71Mhly5Hw4e8TNdmJj9loDmhVRMMYYQx0PI3l1XJn9gy10d0I5yDCUThS7-qSMgF7vpCYXb9lA3YujJoMNBywKW8CGjemtuL1u_K3ulkJevBzhF989svEry-qH3ewmZmaGL0yOc_5aO5UdW5P5cB7Qnwt355g9Gn8CX9JyMr8_H6Ysf3f3Qvs3m7osNfeBgn-yXAYRzuIWo_BQuOxcvBokqxueStMUK2IOoFVsIgYXO5so3C7U-A1Ia262SO7pwTJk4DAyHnKhmyyjcKzpzLBbXYnAf3RFWt9Tn3CIAu_S4uYuSHObGModOgS6k8Wi4QEmh-J6lGTJYWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExJsL_Rj7XHVumKwDdf27qFFwQ4V9GthsM0n9pKpSgYHCLLaUVjKH_iTzd-0JKPsJrZOPl6rGsD_yOznF-xOI5zJ7ld4sDsiap5HnuqCzP3FaptKTMPLKrGcl2l2wmOEL5Bpf2EwkwimkYWcyA6FkRH4D4S0pNRxPYavosXyV24l_31Muh-Xhs19K9urBs8pUxya72CMeEDj3lTU0-30Rw3HLXdGGKTbm4668L0qteN3HiXTvZFlXRIpKdSVxUd4aQY_iQe9Q1d4LaObA3tpDmgvYNmFolPlq2wINIqGFI7IRTskYffOjavIaAzSmdlwdOcPe4E4PuwWiYRtDWEc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znr5bRXKME5SIlE9J8sVz8V8Y-zJJq-ajn5b3Zq8G5ylbD8DaAAmv8Lc2Em13qvmDCqlgp7I7P5KFQGg52Gg1rK9CK1XL1JkrilxbIoPmfbFPmmAvWdPdeW60FU6RxsO2xhOTwHrcvaKQdIjWNlOLMQLS7worwZRM-FL8WmhHP8QJbFRScKNtyxVu34R8GLn2ZVdnKLiCEUt2LVq_gM32TpZj-Dy3GTPpyb5UhdpSRf-JgW1LiRGS2d63E7dfz71uztVpmeTX4Ff2NYpsBFyJ5dbJF1lctOZ6DjAKaZllIAqCIkbUV0P6X2wc9iRC3Qr9TMWoDzsHjziuMDwWLIW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=DZSLDaBBBz3oaRYFUDp-vbHKcDtiOqi4gyrfr8Z9q-Nt5UOLH9cGrr2LdFl-IeVH8gQHcCLur3H_2z0kgoDZOCBjaM6nhyzEjEhnzX-AFQ95PULzFlxtabhLZqIetpdwNdoIaQpiYfmZqSHASweVKErBGgE7HWFG6vlMTLedajQn3lb7yQUwmwnltUjNxQZiFZw68kllm9PtmwPYvryoOyz3-KQoNLKk0Km-Xsk-WjcbL699A6-ePejIBAJFiA912D3oZ8mAFPSa2_nycXL4rj-QjmJvGHfeLo4chWBec64CI3DzFIJQWCu430AFSf_oK-1g0F3SaBYOZJ1e3CDozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=DZSLDaBBBz3oaRYFUDp-vbHKcDtiOqi4gyrfr8Z9q-Nt5UOLH9cGrr2LdFl-IeVH8gQHcCLur3H_2z0kgoDZOCBjaM6nhyzEjEhnzX-AFQ95PULzFlxtabhLZqIetpdwNdoIaQpiYfmZqSHASweVKErBGgE7HWFG6vlMTLedajQn3lb7yQUwmwnltUjNxQZiFZw68kllm9PtmwPYvryoOyz3-KQoNLKk0Km-Xsk-WjcbL699A6-ePejIBAJFiA912D3oZ8mAFPSa2_nycXL4rj-QjmJvGHfeLo4chWBec64CI3DzFIJQWCu430AFSf_oK-1g0F3SaBYOZJ1e3CDozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRU9wIjlStCeAJRi_5bqI9wKWV9egUzcq6OeDYYy2JPLDL783jl5XLJbsYvuddz1P9Vm1Is7yij1C2_FqEb2K14hO4xgOKbpBNPf8DVNcKbGbb_VUi65DsQRzogaG8nUkpCL6VkEc5RXYUFwWr8JIuOWhuCUT2FVgiGBUb-U7HujLE6AA3oycYQzeFGHL1sycFr9gowyYRDt-pr0SqE0MhDIpzrn6xTdh-mxEiHL9mkiOBZoAx64Td4Ti0VVEibRhy64ipjrJimH-59KZqjSzvHa4eFIgm7YrORa93o1BnGv645lTbrXAZrhklerpumr2W_EW4hoMM4vD4z1w5_tBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poriv9kAXK1A6bCa3qHRhr-0pUfWWvQCA34Q-pA-nZFwZ7wP-rRDWHRv99TkuSckzhC8Qcs1FR5ZkZRJYu1E6ddLhWLy0SIw3EbbdHg7aoBZAAYrOGGeCC6dwaqBjJO31WW-ORaZGkCkXBWAfBgkJAbPLL0lWW5Dr27X4aw5pjZUPb4JSUzhZ1LM_-mETsVv1IpWF7K_Hb1JE4sv9jNEZBS2K3ebn_88l5svzDFhbJ3nTCrnNqMtirDKv5vw24QCg3erPK6EEYSWkS4Mmug83vmEclLm3wkXNC2zYY-GkWhdV-3ELCLqOpILltTOrFfCPX_C7gazDyZ_YvF9S1Sm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odmn_-6jbNVS08qUdzsGOZxeTySqIpcjEWmGmP3fxFoNcvYijkPWpS_T5MDYYI7oy4tYotXzjKZcf07CpEgukYPAw3UdRL6nHEx7NNcnLRPdQU-PLQUdCnZlKBR2eU-Z7noFmGU_-SptN7D6ZNOn7g96m7ZRrtmtdy5jiQduDc2Y5MZy-xcV7QNOD6TjQi1XiyJxYq8cCyevJ0rRZ6P4em478-uRbe7IYWqlACWvxA4i_UiTwJpZgBDOciPjaakeZmfwO328ssuePpuxW5NnK7o5kFNU-oTlEZJluJFiNGoN2cK8OwmXuTx4-Tzb6f_W7bKmJ-Uh6spzsqy0ZUJl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG6fUsmduI6WLPKHqdBmAgnZko09yTHplekZQdTmGMoep-n-aWktdfULisrASHWwzwU_FMmxZNZ3iHg3QO3fd8RKqG0A8ASeddQnYS5_HpsUGfM2UP8XbVy4wyf47PbQHyCOu8A1-ZPuDhjFK5Oz4kUcIjZWMWKqwhdxvkqW7hmmqygx-AtcDdOf1-plVRsMNyUFet9n6VG0CPIxsxdfpGUkhmAyibP5F8N7Z95J0Pe8OBy7MgNcgBniMaizMBHmBZ1EZTBUGUZFZJ_cw2GJ4mkvEAKtFaxo4w4tevBy0_GJ_OSFAmtYmOTzt2my4L_0AViyt6wAeWBOuKX06wDqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXpZ8TOE4dN5bDKybynyhL8z0RJCcLaUq1c33qfILjM8H7GTdZxos1iO1VRjRHmsoPMQdE5rjakAYJlkcc2Hkm-ioErpd6TGiglgNEkmASo66ayhRcruLSP7c3Yrc0fqdUHwhI9-PhNqxyxCaARrekHRfSpu_TpVu0Dre06mPSTst1yVek0xry_Kb3bRAzw9fVNwzUB8-FuwGTU5s3LBxwApZdWWXOL1REKxh13WgUi2uHw6ap9Fsh_qfyQLoc9v9pp3j9JDI4rJJqZab9zN4h9i1v4BoP-s1XIdskcZjiSG9pe6o0bK9aSt7tBA7zYCfgeJAIfGGH0N4-XcK-Omwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDhXf2J3sYNlkgz000WvL9Vt4pi_BTFXR4d4MnlMeCBCo3DJUacMqBZCzVZE2A9fpdH3ccF8nxlhS1DHrnj8YxR86wDs9dHriYPUqFqK4VV200DQrcwvyFkYgWxWwIhvLzjY-orG4VLyXs_EEbFmCDe2aLq8M-TI-kLtSyIgc8IhJ-N_ftBGP1doM1XLRje5JmRJ1l7mq0GcVp0BBN6yvjKWRZ1s2DTzC32YBBeD6_9Oq-UrAaPh420klGv6ePiwqYyxMSoaqPljLfD6KNbo4TcVLhMMCsBg5cdQcHIOs_DZertavXyznw_4snoSFgnj-3Wg1Z44t40up_Ko15L4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=HSNQoGkQlovOYBLqLjcB-JAFtheTv7fNSJuYJE95xRQeX95loSujwWDSF0d_vFNSiAtsc24KOJWQYB23-YqWShMks0_DjJjE27SJwC0z5j8qj0uqUgPOsvOqThCjn06G7C_83wEO27lXGpV-oOj3-hsXV7xsdA4mJ0wxQ18GRRVJZtv2GYIM_jMogh9_EQnxw1mfdWvMmDKQoN-_wf97UnJYqDigHRAAn5uikE7fwZcLgdmczORcQcBtMbiA6KeRTgxthAS6S2F6bA1efrLUZ4rpL4U_RPLRlXe3byzVuoEoAmry9Cw87yVvUnbIOzI1GCa5vlahHAXB4lRAR4-UEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=HSNQoGkQlovOYBLqLjcB-JAFtheTv7fNSJuYJE95xRQeX95loSujwWDSF0d_vFNSiAtsc24KOJWQYB23-YqWShMks0_DjJjE27SJwC0z5j8qj0uqUgPOsvOqThCjn06G7C_83wEO27lXGpV-oOj3-hsXV7xsdA4mJ0wxQ18GRRVJZtv2GYIM_jMogh9_EQnxw1mfdWvMmDKQoN-_wf97UnJYqDigHRAAn5uikE7fwZcLgdmczORcQcBtMbiA6KeRTgxthAS6S2F6bA1efrLUZ4rpL4U_RPLRlXe3byzVuoEoAmry9Cw87yVvUnbIOzI1GCa5vlahHAXB4lRAR4-UEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbSx1JfGHFbpt6Yu3jwTbN4lhibxUkx02SOhc8_saxizE2vYP8QJOaHL8sMx-s7MNN7PORJgdqGnIUmEpESIvinna5kCOc4rXEahyaZLrw3hXb1g7xFR63yjg0vNR-JvTVOTsUPEQ5Zyp27G-3n3Bi-oEObRXhVTxXftD8Uk28SU4GK6lbhe8c-uQFzibs83Z9dGDmFJhr1w-IGQjMNf1cwRTskIzd3Kpw5IvkaXiG6hCJdJDDkpp6O0wQ_4b-EVJSzTKTC3zvmcECz1wdk5Bvo1ZrKEsJo89mY6Mqcgq2fcmUbHzzTOfi1mrAj1CSSYhPQ0NIHuh7xpq2Zcfx8iDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfp0bAVHSlBf_qi4ErHfPA0V5NE5ISHRPZjYWLqq5MQPiuMuCzwXdzOoaRwqTk6MlnFfg4_0S2rewC69cYqTMuFwuqaoOdK-Kv7DyIwUldiXvXqiNai4rkTu9-DRCkyM-0TTCbj9nLX-o-xSFdFZG-xaRnBYXJg_r6PDkkTQUXTU3Hg1OD2pIzcr52IitrBtTJhIirOqpMPqyC3iWyaxKLWNB_Ymn_hmV5G5gbsGTvN8GZ7kbLK1xRRN-JBwiLqMiL3Y18c8UufTTSx5tH1TI5jjJikJiFi2ShblsLE3cnLV9g-AMf6zs_LI2kpde1aYO2Vk-CWzHNSJ-zvkRbwydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0XUI5a4eX8NpiGZ0aiaWl0_U_qEKyMCFa0FTho7IGcKqnRAadk022G9PGSNfsV_LkFnT1sOYVGK6knJRpmuouf24lDeD8Wij9u1A7_0qTfxcWdpTQ9-Pw10uc8eyK47zRhbxFTXDTEhYBEMRGnB_7q_ORNuhoqKcIBZDFIOXJZAVeGJRz5bDWFzAFdl8p3Ld4tfJwlBeSZSoIWfXdcNK0AEMHqM5Zt49Ao8h3cP23h-R3-qW8UsNpCWw9wezwswUwgWc7ijHYKv4oUwHPtGdYgShIsa4le8sKrrzZsCXCNv6JPGg7M9TeS0qMWZrKC9WF6RzuaEXtf6aX_hMEREeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgTutXoSwf72ZFlwEdi4tV27vCCoZMvf9qxpMKO0bCrTvl9854gTMwhApoRJ0kpJPem3VfHpHlYoIHifgIF_IqAWXGp0GfmIkC6wcmlJ11qNg1YwfkYACLm1vWvyATXn9plOys1Ip3WyPDS6cc7fSpwlnopRccN0eYE-Fd0U_BH9bo-ISOJxRA75ABrMioU0Vqa5H2gzLU6VscBqqY3gIN2GWrh8TjJpDS3crZiddfSmcQjv57NXYH-EahxW4xMpSSwFjY_e_wrT3smpfueHsFNllDlFNyn2hOpI8JQRAjZW1sXTd31NLn2_3Kw2TxByBW63A_GaK54wwH5uvccjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
