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
<img src="https://cdn4.telesco.pe/file/of0VlTGJj4q3skly5DxL0aqL_DkXW4JU5FPgvO0OHZ3RH_7o6JF9ZaGqqd2WapoGsSOB7PN7A3LJJJ9UJpEtqDUpwF2QCguzQKyTQamkdVg01Fx5QaFc7fuJUuo_7toiMQAFlyQc6kffiuRbFLs46XT1RHQalhfrGCgnuKX64ff4s-bkdW8tO99-MoAuZF67pr0ryxUpeWad9PPem6YgTlkUdYfhVfRMIjizrTvMwrWUuhb-UeMzLKvmq9t5JAx_O8vgbXFbx9nkXGnLJESvlk1FPcDujOrwonWNEW4sCvFCH67fUOOBvOh_hftrn9l86RrKiUY8P7J6Ax-5Dkirog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 04:30:39</div>
<hr>

<div class="tg-post" id="msg-136283">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136283" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/136283" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z--7TvFK1bdekOT7vXDGVGp8ojSBTydcdxDm9O3_9uoLAaejgd3jPrtfBzp_ZY7vXuN42IR5TQ2_7Wqx3oNo6SdEKheKchdPiXROGR4wAtTt5sK1K7qqQm-lUuPjJF6xjWhbpuusqvQXLftxAsQiO0eRQItvjpGQWUTJ8aB684Z6HAWoy8yJb6IW9w6VPU61e4pmp9L8Cdwcc2hw-UmJ4XZ2u0sE2-HdW3Mkd-EnrVIaIB_IxV_z4N4gRfBdUtTQ-jYXg5dmWPQ5ad6z44qiFNztQcucr0tPfufPvD7CyzFtJ4i-0nfy5DUXETu6MIGJklwxfyu4EB-LNn2BKeMaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/136282" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY9BAmLqaXuEpdCcatd1vwoTGlj43uLrwyimW4ZOB0nLTqM3WiOKhnNWNBhQN-GLHclP4FNAgfFdYMRoXKN_hJB1GGktwuES0pi6yYymy5MKZXH1lxGEMmz62tMuGMfWRD4_sPKwv4-gr4uvCmEQ9aNyX6lDKQI_JIqySV4wEZq83sN41S2s0y1kSlMtdSes656CSqFQQU1SLduLbLz8zITAb4JdrBbIpg32p9ARjt0tPHF6Rz4pxmgclK950L81bj5jZj9wDtt2qU9SWh8132TsvVIQ5ujN5-R7D3-5C7NYLlmrHrZuzUm_-Cx97Y4Laf3R4ZypZPUcWcLqnPqgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏆
بالا رفتن جام قهرمانی توسط اسپانیا
💢
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/136281" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚽
فیروز کریمی: مسی الکی داره گریه می‌کنه چون دید رونالدو گریه کرد وایرال شد
👎
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/136280" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De67C_kXBR1WYL01xXROB-O__ThEJcYV2Zr1qKdMt_phQDvPt2W7rE7YjREz3ssTu_1_kLT_75cTObJyNRheCqy4UV-EEg06mKbXpfOK7TO28_YW-nzbB5dWdvCq1ygi-FPjG0zhWiAY2Pem_e6kDmfHpRlkrpPv5YGbLZ94x4WN-VTJevA3QUBF3va6T2p7gQksr8EY_onnSSwOZj2jwhZpBOmB2aiAS0qiExd4dDSOrT4ygufaR6FidR-k17qdKFZ0RQ6-mbFU1OFa7WlBLPBZuXuX2UQ6gb5CFDT5P4aYgMLg4bkNDplazlG0-zqZ2sCGklYvi-gUqfvetaTwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
سرخیو راموس با کاپ قهرمانی جهان اومد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/SorkhTimes/136279" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueypOWUnsGEgLXG3OZXh8xUlPt5sxWWrpyRZ3l4QvNDShBp4aEUneu3Uq4HGdRMNoj02BMx8nuKpU5X12qcY8ZIqqwmIQGKt6GWXzmTxd-zu9onR6IMshjyT11crSY_8KckGUK7mZKpDEciOkqiIGpr0V9-SOGSWwSk998Bv1M0Iziv1eF5vw2ubDCHUYl9orYDQoIxhxpSWeblH2GVlgDJKh2MESRMqhWdM5M_sW6b10Drpq7TMtYR6n7sLcjTFwmo7OhZ9f10m0OwPpGypQN03eXBgBN4NRlSCPlwl00JS_o4MOG988-N9DG6Zvk50waxglrzVx8XKn06Xgo1oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/136278" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇪🇸
قول و قرارهای عجیب ستاره‌های اسپانیا برای قهرمانی!
🇪🇸
یامال : ریش و سبیل میذارم.
🇪🇸
گاوی : موهامو صورتی می‌کنم.
🇪🇸
پدری : موهامو بلوند میکنم‌.
🇪🇸
فران تورس : سرم رو از ته میزنم.
🇪🇸
کوکوریا : چهره لوئیس دلا فوئنته رو دستم خالکوبی میکنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/136277" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c877f07487.mp4?token=moW7EzgPrnCfcHmsnbilAGjaiTOEeqC3N7peOSy6NggHjkQZNzqr0XeaYrkyNYb-8CMtMVDmgrRylk_J5HaQJCRC7UCSpvrp2ljvbssHw9LZNWC_7FQsutmfOav7Ax3XrVtn0hxM0PI8vXWqp2x-ZsYOw_zqQ5ofInsW_IcfqldtaW0ebgAMjCVg-HSvXg9wRLsmK0-W-14A_VJiZZnVc9-Wo0ITXL69dpqX3A3kAo7jtbCXgXP2KwjGIXxOrWtGIFjQxKqQC1msII_3Kj2tax43EyYg7q95gqta3g3Gd4EDb1kxmNE5vQPzI7PmQIt76fx3qLcvzekG3zzH4NLkHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c877f07487.mp4?token=moW7EzgPrnCfcHmsnbilAGjaiTOEeqC3N7peOSy6NggHjkQZNzqr0XeaYrkyNYb-8CMtMVDmgrRylk_J5HaQJCRC7UCSpvrp2ljvbssHw9LZNWC_7FQsutmfOav7Ax3XrVtn0hxM0PI8vXWqp2x-ZsYOw_zqQ5ofInsW_IcfqldtaW0ebgAMjCVg-HSvXg9wRLsmK0-W-14A_VJiZZnVc9-Wo0ITXL69dpqX3A3kAo7jtbCXgXP2KwjGIXxOrWtGIFjQxKqQC1msII_3Kj2tax43EyYg7q95gqta3g3Gd4EDb1kxmNE5vQPzI7PmQIt76fx3qLcvzekG3zzH4NLkHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چخه سگگگگگ
🖕
🖕
🖕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/136276" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚽️
اسپانیا با دلافوئنته:
🇪🇸
قهرمانی لیگ ملت های اروپا 2023
🇪🇸
قهرمانی یورو 2024
🇪🇸
نائب قهرمانی لیگ ملت های اروپا 2025
🇪🇸
قهرمانی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/136275" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136274">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4lLlkjgWFA3eVRRlyUSnpLyj5ms4lOC0OfZNmVkQNxl9MUs0zjx03RQmvoeFZjN0S-wenbAOICiTlYDNLMFLXsYqdiEsIAgGfu-jNhMlspqMVfrt-8_v4xIbvzvHqi1HzIqm--plI1GgDPu6buF7pJiiC3cPrfqO5EsJM-jYBUfFGkzNEfwfJV8ccdDRmWEeaOvR6wPULh9kObmYGr-8ujG-5Dq0IcWyGZrqIGjeQEXpv_8I685jSXq9nd6w6vdTW_x1Iq7XH_T-gcJ-nUrIxLBJ8paZCEZPNfamjJ-qLVfPlVi7dG_a63U8IpE4Rz-iD7H2QOB3NQ1XD8NkiNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
عکسوووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/136274" target="_blank">📅 01:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M5zUZILfVCSZHsaVbmi6GlKh82I1YDnvke4XKswzft5n-eBpKvELwy0lJ6_m3rAptQa4wosjB7QihTzEjjlIZJeKhYpfYHf8_JwAJRKR_wrkqWMw0lYSdeVT3elUPO1-GponQiunML77E5GNGaKory4g4Kv59uBeL6MmxsScfIKOQHBKwG2pGJbXYOX-w4bnZMlNPYun7N-nfpOiIf2xLtR4cP_GBvnfpe8jkYnMiQxZ-5wjsNE7qTg84QGsXZdYGZtCfj2_AFT-8ql4PVW6qGDL1OXIX76JQ4mikeBHRaodS2M6cnergm97do4jh9QKhAAfGuMTS5WsOYeKOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
کنایه سنگین تونی‌کروس ستاره سابق رئال به آرژانتیی‌ها:فوتبال برنده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/136273" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHnGi1uDBWHPLrR1hDG3SNxlDzi8JKvANqM9upSaPPJXtdKcZ952YIE-zFgHO6bmOelERFxuhc7UXk2eajKU0wboLwKio2KS6R9UVk7t6JF8Y0TJkTU7fXCEGdz7GwkoFFkqnspSE4FLOG_dO1WsGPTRxmRaueHIxcWKtkqGZWTRSTs4vr1AgOWoVFgSZagbWQbVpIv5N9_QWvIIKH_IY1q6Vnwn2y1D9CXmattaWSDB28Kj1Lig6JcXwzSXpzYbE77mqmYQ-qdBEpClOXYTVeF68DlHJftT-rCvdN3eQ9A19rA0xnH4M4M9bnx4ovwBYvMo8GMGnSVKyMaRUKwlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپانیا با شایستگی تمام قهرمان جام جهانی 2026 شد‌
🇪🇸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/136272" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWIQqpgdtgazhJZzloLFzQMoyuq_WLe29lVC70Scqc4kVUjoARTWwJZ_LiExKDK4W2nkk1lLbRCdrdlzVLI9xFA3YRFqUtw1PJFRhusyrg3gGMdrFYhkTtQ07ZMae-Jdb8MFKhhTaC5lprAJ8SyAqfD4MjmQw1P7sCQ2f0sJyHBc3JCXbmNN6dKercRjQtqQpcDdhPpo9PwaRvrr5EGJp25tzMplUZzQNQRvtrYC86QLY1terPGoOSJCa3cSn-zfX8BNWzfwIBcyfby39X3C7FC6kg61tKhbPLcRiFMo2nQ12c-NLcCPeHNuxQYqdv0whE0Pb-LQsT-5XN6w0sVKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
پایان کار مسی با آرژانتین…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/136271" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
این بازی فینال که چرت آور و خواب آور و کسل کننده بود با نتیجه مساوی تو نود دقیقه تموم شد و رفت برای وقت اضافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/136270" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
بازیکنی که کلا محو بوده و خواب بوده تو زمین فقط مسی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/136269" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
🔴
ارزونترین بلیط فینال: ۹۵۹۶ دلار (۱ میلیارد و ۸۳۵ میلیون تومن)
🔴
🔴
گرونترین بلیط فینال: ۴۹۳۸۴ دلار (۹ میلیارد و ۴۴۷ میلیون تومن)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136268" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/136267" target="_blank">📅 00:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❤️
🎥
ویدیویی از تمرین عصر روز گذشته تیم
🔴
از مرور نکات فنی تا اجرای برنامه‌های تمرینی؛ یک جلسه دیگر از آماده‌سازی سرخپوشان زیر نظر کادر فنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/136266" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏆
اجرای کامل مراسم بین دو نیمه فینال جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/136265" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
نیمه دوم هم چنگی به دل نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/136264" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
نیمه اول بازی .بی روح و خواب آور و کسل فینال با نتیجه صفر صفر تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/136263" target="_blank">📅 23:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=QtLaODZ-OV9Mf6l6b2_8MrOV_jrkB4fwzIvPsP8EQdTxwfsbMPXgAA16KZJSGqQv871qc84yZCJ05ID_SRcjOQvX3LxQeY5GOEfSOEfj86UurvJKgzTxk9dZtES3RUGmc8bZoqw1ycqdCbV0U7Wm6vmoXUGieeHbaASly51UF44_4zCvSQtHuPNE7TemrozVccbdFkft9li_bAl_NfCeb2PwGeYi2jBvQ2tCx6Ws8FuFO4m3b2eT0pfkm8dbOj5kIrD5oTB8B6_RX1ztXFgOrgMorvSZ46OmI01Ol5YBizHVizOF2dLM65dxSGoQP0jFVC28YFghe7N6lAAs_uuTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc7fc060.mp4?token=QtLaODZ-OV9Mf6l6b2_8MrOV_jrkB4fwzIvPsP8EQdTxwfsbMPXgAA16KZJSGqQv871qc84yZCJ05ID_SRcjOQvX3LxQeY5GOEfSOEfj86UurvJKgzTxk9dZtES3RUGmc8bZoqw1ycqdCbV0U7Wm6vmoXUGieeHbaASly51UF44_4zCvSQtHuPNE7TemrozVccbdFkft9li_bAl_NfCeb2PwGeYi2jBvQ2tCx6Ws8FuFO4m3b2eT0pfkm8dbOj5kIrD5oTB8B6_RX1ztXFgOrgMorvSZ46OmI01Ol5YBizHVizOF2dLM65dxSGoQP0jFVC28YFghe7N6lAAs_uuTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/136262" target="_blank">📅 23:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
با یک چشم بهم زدن جام جهانی 2026 هم داره به اتمام میرسه ...بریم برای بازی فینال ..آرژانتین و اسپانیا ....
🔴
پیش بینی شما چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/136261" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsevufAzhRyWJPBgJlS1ea-jVuiSNMxyWnz1kM6PpmakcakwhMPrLCcMxRNr4lTT_IYBbPHJRVvWbqbn1tn3GsAhqk5ZwdU1PDK1l-CY_aFrdPJisrWz4Sf9HxVzo_O1E5x_PYUFnAOftEyT_iwnlUYD55APv0CcUIJTit44WgcYpvMJPm-i8jB0ssoKgqWpOfpHDyE4N046K5T8FjY9v6tJIYEqAGQLRy8bb_vicUqVJxrRpnxdRIhmmf7A_XKo6BoEWlg6oMwLNBSZcefn_BS-KelGNAMBNsj293ckIJ84upKuThhzlao2bzTvzsWNlJ1_P0JP9ULAMQNw4A-gCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/136260" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/136259" target="_blank">📅 23:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
#تکمیلی | رویترز:
🔴
ترامپ دستور حمله قدرتمند به ایران را صادر کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/136258" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
خیابانی: چرا در ایران کسی معذرت‌خواهی نمی‌کند؟
🔴
واکنش تند خداداد به صحبت‌های امروز امیر قلعه‌نویی
: واقعا خیلی از حرف‌هایش را نفهمیدم. ما لودگی می‌کنیم؟ چرا پس شما حذف شدید!؟ ناپلئون و هانیبال هم یک پلن داشتند نه ۷ پلن. آقای قلعه‌نویی چرا نباید کسی انتقاد کند؟  من انتقاد می‌کنم و نمی‌تونی تریبون را از من بگیری. مگر بزرگتر از علی دایی داریم که انتقاد نکند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/136257" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUy9QVxcFX9AvqrZ_mDbDbsX8l7TykbZlBilkQfjM0wVcrbKRbab-_hziklEGWvI2OQWs_IVd3FYVELdvF9vrRGtRUWZu51WUNqpm32RgSFAi_oAptPcIWGt_Ezu4T_npVkbhCQoUCWDZsha6NLcPyE_7l3ocFAa0pRb7ee_ZxfdMjXmj_8tPVGZyJM_iVnaqQJ0hDnjcosWBFnZ1r-FhDaw8zNfsTbEdTNlpANA6H8FsjBikEsa1-4fIZEq5JpdPpQ-5JRTZAC6vyloqw0F5aGFKMykfrvDYizp8TLeh8pGPzekdxrVoMjG1joJe9a457b8qSUFQ_utUZYZNrAuXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپورتی تی‌وی: کاپ جام جهانی 6.175 کیلوگرم وزن داره و ارزش مواد به کار رفته توش حدود $713,000 یعنی 140 میلیارد تومن برآورد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/136256" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/136255" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=nd8kPuJoxkJcDkfk-3Vm27-l_-MSpCXK8444syg45jD6rP7o__SJHAMVmJJWIHWxbKxqz5lNhfYsIqnDrkZUSTY5lUH2E3FxibFKYS9sa8jBhkq7pm4nf1rDiamP_M5CgiOpa1gknYI6m1JTRzps7MAqPmFWpneGZxs3C82oDlcZmM1tcAcWBhme80wyrdvUIa-O_MRvTXvHftQL8QvEqQXaLMzVYu5OH06THBOgtySTPSuPR-Sz6wGaKO5KBrb84TK9wiR252tza0f7GWr-MY7-A0Cm8B2J4WyYLFp5Ah4-qzhOtmDzOV0B979PsNaysIgbvl9ZBbsmbtCBryRxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85518f3eb7.mp4?token=nd8kPuJoxkJcDkfk-3Vm27-l_-MSpCXK8444syg45jD6rP7o__SJHAMVmJJWIHWxbKxqz5lNhfYsIqnDrkZUSTY5lUH2E3FxibFKYS9sa8jBhkq7pm4nf1rDiamP_M5CgiOpa1gknYI6m1JTRzps7MAqPmFWpneGZxs3C82oDlcZmM1tcAcWBhme80wyrdvUIa-O_MRvTXvHftQL8QvEqQXaLMzVYu5OH06THBOgtySTPSuPR-Sz6wGaKO5KBrb84TK9wiR252tza0f7GWr-MY7-A0Cm8B2J4WyYLFp5Ah4-qzhOtmDzOV0B979PsNaysIgbvl9ZBbsmbtCBryRxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: مردم نون ندارن بخورن آستینتو انداختی زیر ساعتت همه بفهمن ساعت 10 میلیاردی داری.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/136254" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
جزئیات اولیه از پیشنهاد قطر برای برقراری آتش بس:
🔹
۱- پایان جنگ و برقراری آتش بس
🔹
۲- تنگه هرمز تحت کنترل ایران به مدت ۱۰ روز باز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/136253" target="_blank">📅 22:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه ، وقتش نرسیده که از فوتبال دیدن پول در بیارید؟
😉
✅
@FuckBet</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/136252" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqPJYKrzORNnQB8rekXg5bW9fSgKTf3eyFDEmm7rECxZTVFbGJsCzNH_J7pOYNlH546dkRByc_Bjrfh0xctxO-uUiw3jGOhacTLaf7k_b9KTqV18I-WoZtZrOeG03KZTqD_VPS9-qdkjWja4PaDvZUoA3gqF6-5EM29Yp3PT2I3bjJpgzAWgjzNtNYjsQhtYPthXvsUc58oK2AfXP0RtNu5JTfXw7EfCfy9mQ8TkWUHqsOgruKBlWte68Q7YHDwkPgqrPLkzGr1XB1gbPYo9jRsbhaawpCZuDC5slDjdehERYxcAg4RQoLTFF4Bs-j-OSxQSBEmgk5NPpQx0KKRetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/136251" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🔥
فوووووووووری ؛ از کاپ جام جهانی رونماااااایی شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/136250" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/136249" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8pkiXamq9MCK5282r97VvPR8J1B83PY8rEfAdXJgihJF8tQZTNa9EwUte0uLvgjQlgeKfMvTyXatLI0Ig_u6rYDmSVL2KcfGkX1AhyNJPA-C2hKxhqw3Xc4o0zeRZ1MwyVpEI-7QbiSxxT6d49qVWgUF40E5yH7Jq8HWS0gJ9uYHQB_EdAhFtqO9UCSzCLaUFYSUHisUXwHCnwbxPtXfoQgIGytj4qcF6WQBcMbi0RRVmwddhgCqcQ7HpkvaCcKCAMeGjWDp55v_AJH06hnI3T8It5SIU2RKGRwXItun5lBM_YHMLQmajrjBZ_e7ia7TJnzcyqC3rXMG4Om9lHUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
فوووووووووری ؛ از کاپ جام جهانی رونماااااایی شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/136248" target="_blank">📅 22:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3XbNJuAG3VnmFxv8b44pyMyw0UjTctpVLe3D0Riv1E4iqfKMozwRgno87oC0wlYA_BrbUNEyBCQp9d2_z0hMeDiwDvTkVaANrZE-Sq0gIBb8SpLmSAqGQOitjrXtXHti7wjc7PQCM2FssR9_qVbvhks4Ycli4CHi7VJiBEcVPUvPIVMAdlPrLdhN5cFSHGv54Y-syluQz4hF01pma75jxhi2BDL-BdIj7gqdfcJ6VDyEu3Xi7XJODi48OzRfYbour9Pi4w93_7ybQgFkCw3rloCs-IKD35DitxwGVh1QDkxMWRnbdw-GNQ38cld2ShwESlJWk7dt2te2aiEpl4qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از پشت شیشه ضدگلوله بازی امشب را تماشا می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/136247" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
امین کاظمیان در تمرین امروز پرسپولیس حضور پیدا نکرد و جدایی او طی روزهای آینده رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/136246" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXYyVVxnXfCsWKQxVbCiyaAZ7OZBIOS4CpdQcKwT9eAg9CDpX4tTeln1TRtBOrW8uAr-l1-N9Ghl4EQPdT7YeuklkC2RgKLK0e2r8RGA2234eLadOPxhxA6NINxI2znvZB1M7oUM201XQAo6TvXcWza-RjmK0tfFFEtfh8JF3Rp0ULL780lrwJLk0jMFe8sYYSZC9x6V5FFbZBktM3SC88uOyAXey7TkR77GW2Yxhy5xxWD6pltbkZuDxvUUS2pnd5mDfXCff7gPJ4cAHRbupQnOnZuL35cju3hHRQNMpVPKOmLomuyERDKgHl4VQHNkolAM4TK4x_cl4fn2hAnCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/136245" target="_blank">📅 22:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=CfpJ5GhCbsoDHrotrWTpqWxlqnBcuR19dqh5IgSWK3BmSfAYR_U9JBDUiy6MB96iD4dtNdXshYVpaAFKeXR9UAqqzLqPojDDRZX8yzX2FQwA6DOjKiCwejGSqalqaArRyZvK104azJR6hPx4HaQhP-s5bQnZixcylEIty-LLd1xUmZM1VAZfl8OvQuhqTPWC6OAnj4LoB5i6Zq-Z3q9Z8R59SidqIfTD7Y9Lq-LVzvLWkCVhql-3f83tqfVZtVrUtqDcwTJT18rHxfj6Yr3KocniejV7as5jExeqXUxBxWU_svqvp6RtOAjkYXMGzJa1xxFenWQFhT-J9FHXPta0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b943d93e.mp4?token=CfpJ5GhCbsoDHrotrWTpqWxlqnBcuR19dqh5IgSWK3BmSfAYR_U9JBDUiy6MB96iD4dtNdXshYVpaAFKeXR9UAqqzLqPojDDRZX8yzX2FQwA6DOjKiCwejGSqalqaArRyZvK104azJR6hPx4HaQhP-s5bQnZixcylEIty-LLd1xUmZM1VAZfl8OvQuhqTPWC6OAnj4LoB5i6Zq-Z3q9Z8R59SidqIfTD7Y9Lq-LVzvLWkCVhql-3f83tqfVZtVrUtqDcwTJT18rHxfj6Yr3KocniejV7as5jExeqXUxBxWU_svqvp6RtOAjkYXMGzJa1xxFenWQFhT-J9FHXPta0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ برای تماشای فینال به ورزشگاه مت‌لایف نیوجرسی رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/136244" target="_blank">📅 22:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد  پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136243" target="_blank">📅 21:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKWmvMBaKln3Xc_GPtK9PCj_LSIyjXJ5aRuWEr-KznVW_bDPZ84WTNt5KwYo399wsQlPi0akxeW7BQ1BeImh5jajByn9s_eYaA9ruGWvw2TSDNxEDMOXPbpnWG_ZFSTSZEOCA1kZGrLgYJo6Z9lADrLairC8ZNmg82Xnn6dvu2MJlk2tFuk1q4u4veJXBL69dRatdcN_slez7vpw-52ZlKhfSFU8Pk-tzDbeFG5FAngmYUMM76BcX5rfut0A2gd1zvCOxkyF4mqCm4f-8V1VJ2jPuGWlJ76x1BSASjXR6hGawFa3OzGn1JY-o1XGPJeSbyQF3JoRfU_f2Y5msA_45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
پ.ن فقط 45 دقیقه تا شروع بازی نهایی جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136242" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_XG1PPwDyzlQ2zGPccHChspmhhC3pC-RO66n-dpNxXsY13CqEiw4s3gD2GaGANxlqivLRD3ywfPQfebfHkZtsa1XSnDmiSVlntBduHlRCzqRzUD9CRP1R2iaWB3Ny-RwVOSO6509qEgCOWJJ7EuB06ohVj8s5bBBR8sgbg4kCXhWFhlKX-h6EWhFuSBIL4pLcSjJ6lx121GE7N8zIBtOg2u6x5wvGjrlWuZSeftJgWMZLeCenJQisPh9PBXPvtwqP7obweXibTqU4O2LylSkYagdQP4Fp8jw7F-iTUJ2cVlYc1HXnXNKjH06wCfgUcycNONRO3bem4beendTYWdRUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92f2cfaf9.mp4?token=fUBCgxuFqpdzJvg__9nbU-Scd3K6Tbonv5ZHjRBSWlREPKuj6P_yr3_olJ2EI_uZbrbPfyUJXSmXPVDQY3kjxAqh3Y9sz-HjpcHpJ9SFHfu01Uyadx84G0CQWvyHkAKuCBb7QGVHlsRv9_Fy8UPLhAu_ODzD3wiCRDIDDrgWggQh-aNURpBzR81MHg6X4nDNDm8h2XbbEYajI7du0Ru_905i4ZZO-219xfmVV1vSgJdRH78MMto_g1chb6Kz0POVy0JjrM11f5KyiOgp0USGeuApy6QxVMml84wHty8v-1nBA3uykAPQDEoios83PZRjDNG9EcTAX7UkxGSBEbC-_XG1PPwDyzlQ2zGPccHChspmhhC3pC-RO66n-dpNxXsY13CqEiw4s3gD2GaGANxlqivLRD3ywfPQfebfHkZtsa1XSnDmiSVlntBduHlRCzqRzUD9CRP1R2iaWB3Ny-RwVOSO6509qEgCOWJJ7EuB06ohVj8s5bBBR8sgbg4kCXhWFhlKX-h6EWhFuSBIL4pLcSjJ6lx121GE7N8zIBtOg2u6x5wvGjrlWuZSeftJgWMZLeCenJQisPh9PBXPvtwqP7obweXibTqU4O2LylSkYagdQP4Fp8jw7F-iTUJ2cVlYc1HXnXNKjH06wCfgUcycNONRO3bem4beendTYWdRUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ادامه حملات عادل فردوسی‌پور به قلعه‌نویی: هرکه از "غار" حرف بزند، قابل توجیه است؛ به جز آن کسی که کل جنگ را در دبی و ویلای آلانیا گذرانده باشد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136241" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
پست خداحافظی رضا شکاری با چاشنی ناراحتی: خداحافظی همیشه تلخ است، خداحافظی از گوهر کمیابی مثل پرسپولیس تلخ‌تر...
📍
موفق باشی
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/136240" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/136239" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
عادل فردوسی پور :
🔴
آقای قلعه نویی من و تیمم چه جنگ دوازده روزه چه در این جنگ تماما داخل تهران بودیم و تکون نخوردیم ولی شمایی که یا تمام جنگ یا امارات بودی یا توی ویلای شخصیت داخل ترکیه حرف از غار بیرون اومدن نزن. من تماما کنار مردمم بودم ولی شما همش توی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136238" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136237" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136235">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/136235" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136234">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=SFNMEYiehZkvZncVWSyviPjemRos7MUfHUqGA0gfflrVv-JSMsBrTAAbdfVedaUv_MA250UpO_pE42R5bClqSZFIw1XV3gjWXtb1dHj5SbQVWUIwtgIoMvQn9PCWqN7C4nxJNt9wq3m_dCL42ZlCSjWOgfaO9n7nzrrltCTjeH-dnl9W-f-WH2orGPuoXU0zdSpCCvOnh2I2rgAoqP_Lmalu-P4hGTEtlEByo5YsIcxylIXDm-ohadB28heStfj5xmaBfy7uvhnPdyxkc0s9aZj1L_WRWVKD3DPemWZD2wyWsTaa35ip_4ltWSg7OW-9T2PTuljXnMwV4V4LJtbAw4_xOWrUSX0mp_MtLfqZ3ln8uC9BVb_Ac0yw-wKVwMs03_iHi2cixeHD3lfFdl1Hos34q2TQPrZSW0KdGLtTMNNL8VGdcYYPZGylUci1JDCRUft5-pU7FhHNOW1b_IGh2t_WysLW-3dHM4NIdDKs0aYVCwTMGgprmYmvxVQgZgyhTzgTHMrbDE3yEZurbIayVrDMbkFfGyfMLwe0ZQzEYJoTnDIqtp67NXzbnC7w-CTgvmXN4hqqeSlZURwgFKG3ZWRDO33Gdhdo3yN3V05TM5p8bRdKV9SccFHW2I5VHrGzTkQ9pFAjXIS6hWAuao29iJFsEWrGZbexacEobET9Ulk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9106b20ac9.mp4?token=SFNMEYiehZkvZncVWSyviPjemRos7MUfHUqGA0gfflrVv-JSMsBrTAAbdfVedaUv_MA250UpO_pE42R5bClqSZFIw1XV3gjWXtb1dHj5SbQVWUIwtgIoMvQn9PCWqN7C4nxJNt9wq3m_dCL42ZlCSjWOgfaO9n7nzrrltCTjeH-dnl9W-f-WH2orGPuoXU0zdSpCCvOnh2I2rgAoqP_Lmalu-P4hGTEtlEByo5YsIcxylIXDm-ohadB28heStfj5xmaBfy7uvhnPdyxkc0s9aZj1L_WRWVKD3DPemWZD2wyWsTaa35ip_4ltWSg7OW-9T2PTuljXnMwV4V4LJtbAw4_xOWrUSX0mp_MtLfqZ3ln8uC9BVb_Ac0yw-wKVwMs03_iHi2cixeHD3lfFdl1Hos34q2TQPrZSW0KdGLtTMNNL8VGdcYYPZGylUci1JDCRUft5-pU7FhHNOW1b_IGh2t_WysLW-3dHM4NIdDKs0aYVCwTMGgprmYmvxVQgZgyhTzgTHMrbDE3yEZurbIayVrDMbkFfGyfMLwe0ZQzEYJoTnDIqtp67NXzbnC7w-CTgvmXN4hqqeSlZURwgFKG3ZWRDO33Gdhdo3yN3V05TM5p8bRdKV9SccFHW2I5VHrGzTkQ9pFAjXIS6hWAuao29iJFsEWrGZbexacEobET9Ulk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری خداداد عزیزی از امکانات تیم ملی قبل از جام جهانی:
❗️
به من گفتند بهترین امکانات رو داشتن، شما اگر از امکانات آمریکا انتقاد دارید در کاخ سفید جلسه میگذاشتید والا، 15 روز قبل از مسابقات 400 میلیارد بودجه گرفتید، 1000 میلیارد از رئیس‌جمهور درخواست پول کردین و چجوریه که فقط می‌نالید و ما رو سیبل می‌کنین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136234" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136233">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=J5oGBSDeHS6_gahOeMCqfw7eJyqzI5tEfnF2JizuAxiUxEBgcMwPsc5KXzku1_DprR9gYdH0dkdPkfuy5TFiCID80uMyZcIvb0FbYD1VODBr_wDBnbeLqoiaJ7JeB4eRlIsnMuFamZeguStsoBGOj4-8nlXEF0w_rauuoFLM-vVp8vnPXA-s5G19mbk_-99FIZO2B-2paeWKM8s12P70oaXD6XnFEyIO4xHDlU__6x6xVbn72QqbMk7WzgGVxdI4zdtnY4ktUAQXmHsDGHzkN-JMY594zjY8y_vxLypfDxU90l-utGWRN8Xd4q8-nz-KREEUF5I_b-k66_913BCGyTt7503BxDHPZGiQof27lzC2aw7aPGK9h9DxiVxdq9pHH_1M7iJ2D0KNI_HVc1bb9_e8i3p2loASxmHBUb6d6CxJJll_lNvMSCMlsG9eiIKnxRZs3GnFD4zHZqYKW1k_RYc6vrI_meZHCXZqrfOdy9m1T32bFSn1X6UqOS3bsonkM9fNX5KPXmbyJqMkOkb9oS2E4Zuu1X9mMIspxDcOcl_5Edm7IVmmA9CVukyvL01mnbkGTvqtNV87WvhY1stZJnhbSN-cAAKEG3HFl4lU2Bd5WrZZfmIqw6ZBI7kfqy173vBB2KlA6U-Hw6v3Q-r8aBgKkr--jEA72EYVEMyv6Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cce783d5f.mp4?token=J5oGBSDeHS6_gahOeMCqfw7eJyqzI5tEfnF2JizuAxiUxEBgcMwPsc5KXzku1_DprR9gYdH0dkdPkfuy5TFiCID80uMyZcIvb0FbYD1VODBr_wDBnbeLqoiaJ7JeB4eRlIsnMuFamZeguStsoBGOj4-8nlXEF0w_rauuoFLM-vVp8vnPXA-s5G19mbk_-99FIZO2B-2paeWKM8s12P70oaXD6XnFEyIO4xHDlU__6x6xVbn72QqbMk7WzgGVxdI4zdtnY4ktUAQXmHsDGHzkN-JMY594zjY8y_vxLypfDxU90l-utGWRN8Xd4q8-nz-KREEUF5I_b-k66_913BCGyTt7503BxDHPZGiQof27lzC2aw7aPGK9h9DxiVxdq9pHH_1M7iJ2D0KNI_HVc1bb9_e8i3p2loASxmHBUb6d6CxJJll_lNvMSCMlsG9eiIKnxRZs3GnFD4zHZqYKW1k_RYc6vrI_meZHCXZqrfOdy9m1T32bFSn1X6UqOS3bsonkM9fNX5KPXmbyJqMkOkb9oS2E4Zuu1X9mMIspxDcOcl_5Edm7IVmmA9CVukyvL01mnbkGTvqtNV87WvhY1stZJnhbSN-cAAKEG3HFl4lU2Bd5WrZZfmIqw6ZBI7kfqy173vBB2KlA6U-Hw6v3Q-r8aBgKkr--jEA72EYVEMyv6Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خداداد عزیزی: صداها را نمی‌توان خاموش کرد، مردم ایران غارنشین نیستند، آقای قلعه‌نویی ما جنگ رو دیدیم، بهترین کار این است اسم ببرید، شما نتیجه نگرفتی چرا میندازی گردن ما گردن رسانه؟ تنها جمله درست شما در مصاحبه عذرخواهی از مردم بود، دوباره در جام ملت‌ ها من طاقت عذرخواهی ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136233" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136232">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/136232" target="_blank">📅 21:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136231">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
🔴
🔴
فوری| وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/136231" target="_blank">📅 20:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=Cwdb2Wt7UwrLTnPBjPoHGdLExU0TyR61HCs6OxdhlNZuWgRaDC1HUG37YBaI-bhvgNHiy815ifjgFX-ZDThf9mZRzTbm2fDWTu_06WfXWRu-HUA2UpXtpMm7WV0skZwVU4O_Zx019Q7FWlm5LlBZfVUD1dGxmEUCbeQ3H2vllj1d2zZ_k_NmYTQQo6bKx7Hr324AakGYRvznF15xYtaA58v0eVgOutgQ6t6Y5m3i6jdfLtO5RgXaZGYwehTQgKoIXzW2b5NxWi5v6jsGxE8eJYFQhPIT-zwwB_ExAViZ8OB_nVoQ5R1bjJQdFVgg3YaULAgSkhC47LWFMei8Iw5DZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=Cwdb2Wt7UwrLTnPBjPoHGdLExU0TyR61HCs6OxdhlNZuWgRaDC1HUG37YBaI-bhvgNHiy815ifjgFX-ZDThf9mZRzTbm2fDWTu_06WfXWRu-HUA2UpXtpMm7WV0skZwVU4O_Zx019Q7FWlm5LlBZfVUD1dGxmEUCbeQ3H2vllj1d2zZ_k_NmYTQQo6bKx7Hr324AakGYRvznF15xYtaA58v0eVgOutgQ6t6Y5m3i6jdfLtO5RgXaZGYwehTQgKoIXzW2b5NxWi5v6jsGxE8eJYFQhPIT-zwwB_ExAViZ8OB_nVoQ5R1bjJQdFVgg3YaULAgSkhC47LWFMei8Iw5DZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله شدید‌اللحن خداداد عزیزی به قلعه‌نویی: شما فرشته ما شیطان؛ شما خوب ما بد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136230" target="_blank">📅 20:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136229" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0w5xRVnCK7VvsgjHTmqbg4ejy6shxtFRasxnnZDl88gMEvIn6ylX5NlwnUe8cE_5SFp2qaMEbfBbWostwjlYsJJcItQuKUTJJI7B3VPywmvi7srDBtaJFJqLAZRcOEWC5PJfbILFhLGHUk4phuHxp54fvLj-D2AwpNX5TC8h4lRfwYA8UpTZ8zX3IQt_CZv2928pUwSBB3pMkkGXRtji8StBGYzWbyjyTk9wC9Yc6ulgFHqDXhR5w1l3ITX79k_2msOm67mzYzN7wRKB0l0A7sHUorcT-E6x39iDKOVYL5fMsEoB5fCDNho8MrJX9QLLT2Yet54zG3m5eg4JGbizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
تصاویری از احد میرزایی عضو هیأت‌مدیره پرسپولیس منتشر شده که داره توی ساختمون باشگاه یکی رو کتک می‌زنه…اقای احمدی همین فردا دکمه ایشون رو بزنید
❌
پرسپولیس چاله میدون نیست، ایشون ادم زنوزیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136228" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136226" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
#تکمیلی؛ باشگاه‌تراکتورتمام‌توافقات لازم رو باخودِ علی ‌قلی‌زاده برای قراردادی سه ساله داشته و تنها رضایت نامه این بازیکن باقی مانده که مالک تیم تراکتور قول داده ظرف 48 ساعت آینده مبلغ توافق شده رو به حساب باشگاه لهستانی پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136225" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/136224" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136221" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
باشگاه تراکتور مذاکرات مثبتی با علی قلی‌زاده، ستاره ۲۹ ساله لهستانی، انجام داده. او قرار است ۷۰۰ هزار دلار به عنوان رضایت‌نامه به باشگاه لهستانی پرداخت کند و سپس به صورت رسمی به تراکتور بپیوندد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/136220" target="_blank">📅 20:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=WLZrNP9fq3AF5FIHnGmwVTf1ggc_gp-_ecXQhV-gBm5H-HSfZsTiW8Ie0Yech21I0FscU_L_wcdgke0CZri1uERgQPcbDk6_kk_cEc29b-BLsndZUiY2g7g68Dp_0lLDIX905b-JHKaE6caTWJ290zceyb9aAnTo2ch4unhPOYlnGXlq7Ls4_u4UoyRZFaiYi-MNSr9n4eEa5lF-_-p4NjF2YgljhJ4Hm9pSEYsh73Hc-jcS0Va5-Jo4jNnlyxs2fPgBTNnfyeIxkJ9bAWR2u4KktJrlk4liU87O2364TLBnRaKu2TM1_Nz2Y6hGlRcG4w9HCb9T2kaCy_UetPOa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bce486c0.mp4?token=WLZrNP9fq3AF5FIHnGmwVTf1ggc_gp-_ecXQhV-gBm5H-HSfZsTiW8Ie0Yech21I0FscU_L_wcdgke0CZri1uERgQPcbDk6_kk_cEc29b-BLsndZUiY2g7g68Dp_0lLDIX905b-JHKaE6caTWJ290zceyb9aAnTo2ch4unhPOYlnGXlq7Ls4_u4UoyRZFaiYi-MNSr9n4eEa5lF-_-p4NjF2YgljhJ4Hm9pSEYsh73Hc-jcS0Va5-Jo4jNnlyxs2fPgBTNnfyeIxkJ9bAWR2u4KktJrlk4liU87O2364TLBnRaKu2TM1_Nz2Y6hGlRcG4w9HCb9T2kaCy_UetPOa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
واکنش قلعه نویی به تصویر ساعتش در جام جهانی که باعث حاشیه شد :
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد/ اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136218" target="_blank">📅 20:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
تصویری از خانه دروازه بان کیپ ورد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136217" target="_blank">📅 19:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
شنیده ها :دو تا از بازیکنان ملی پوش و با تجربه پرسپولیس با سامان قدوس تماس گرفته و در تلاش هستند که او به پیشنهاد باشگاه پاسخ مثبت بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136216" target="_blank">📅 19:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHVo9PUmPWpxwQ5RX8zK_0CJMXA6ekpCzTrcJLeb8hDPtFZqzH5ycb0JTdSadb9qr8_7xFu9u6Pvldimnp8LmtV9smc126_vjxREifMtB8wOsrPxYiw3D6ZnIXXP7lXCUVJOO0AhlpiC-z2wFZVGpCrs5WqL1gY2F2SPaQASvCdzZqKbrqJA1Ftq6Rz_Px8qnVDW62iqwOX-cNk8pPoZfHyiipBYc4iBr-yn9lLOySj2T6MWvny2XbC8MGAEBEbGXAHvgggQzYyzoKKURdGKBP0Gf7xVDCjdZAYRqVUUrA-jCzu-wOQwVY7Cqj15FYSPhh6xzCVJwH80gKPhMoALgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
یه سری عکس منتشر شده که نشون میده احد میرزایی، عضو هیأت‌مدیره پرسپولیس، با یه نفر درگیر شده و باهاش گلاویز شده. ظاهراً این اتفاق مربوط به گذشته‌ست، ولی بازم خیلی‌ها معتقدن برای یه مدیر باشگاه پرسپولیس چنین رفتاری عجیب و قابل انتقاده.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/136215" target="_blank">📅 19:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مذاکرات پرسپولیس با احمد نور پیشرفت خوبی داشته و درحال حاضر تنها مورد رضایت نامه ۸۰۰ هزار دلاری این بازیکن است که باشگاه پرسپولیس تلاش داره کمش کنه /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136214" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
مذاکرات کوشکی با استقلال مثبت نبوده و پرسپولیس و یه باشگاه لهستانی مشتری او هستن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136212" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136211">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a174835238.mp4?token=NpSHnJB0tZLPrRSlwCwtWXAxo3LUo-hR2UgUpLoZ8kN3GBnoL-bVxpssIU7AuwIZCVfslTHaLMDlP65kxLNgxtfKK7s9vejWM0SuCgmKyy1a4s1A1iZegOkPlzd0lb9mxbpSWIV8dqQ9OQhp9M49s7h7CcU3hO2nHsa-UFRgQnwxgaGekTUcg6TzTjOGUgZjVeQoA7NznGWMEeyYC_KDPP0m2_jpBoNY436vL1rpDTTLLIyrQ74ArGH1INbDI2b1Z3HN37jNBu2zenoPE-gisZubKQZbYApF0iuBhbvoD_ivIukVaMLcdorGzFpt2NvvjfdVSQYTNx55tRKI9M7LWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a174835238.mp4?token=NpSHnJB0tZLPrRSlwCwtWXAxo3LUo-hR2UgUpLoZ8kN3GBnoL-bVxpssIU7AuwIZCVfslTHaLMDlP65kxLNgxtfKK7s9vejWM0SuCgmKyy1a4s1A1iZegOkPlzd0lb9mxbpSWIV8dqQ9OQhp9M49s7h7CcU3hO2nHsa-UFRgQnwxgaGekTUcg6TzTjOGUgZjVeQoA7NznGWMEeyYC_KDPP0m2_jpBoNY436vL1rpDTTLLIyrQ74ArGH1INbDI2b1Z3HN37jNBu2zenoPE-gisZubKQZbYApF0iuBhbvoD_ivIukVaMLcdorGzFpt2NvvjfdVSQYTNx55tRKI9M7LWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووووری
⏺
سپاه پاسداران به یکی از نیروگاه های بزرگ برق کویت حمله کرد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136211" target="_blank">📅 19:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136210">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
❤️
🤩
طرفداری: احد میرزایی بزودی توسط مالک بانک شهر به سمت درب خروج هدایت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136210" target="_blank">📅 18:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=lYU_iuODVdoX9E2oQpiIFz4ovi9XqfGV4uUgFX0P5yRd_3emVjvTpB7MT1oGr0UVa_ofpf2x0zH6W9YmdnHWqwvJg0FAlKt_vRWwUH79nchiFZ0763hM_oDTpRw00YTMUe96K7z9jyY9mG64RFqrwUpNVzFxOo7Cye4kFstj8L3_prxfuiVcXVzt0cykIAz-t-2YuQhoExCN3PFY6SfvR6JgujfrvHU5cEi1GuDWmuHVfZdIAKm4UwnQ3ViYcH6TxQyLR4hUcG0TtbxleK109nQcfNTiwb9zQYlm-ZzCa9OzWe4VeJFEqdbIOocH37_fYHmtNgtGN5eQujHI1qSgxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=lYU_iuODVdoX9E2oQpiIFz4ovi9XqfGV4uUgFX0P5yRd_3emVjvTpB7MT1oGr0UVa_ofpf2x0zH6W9YmdnHWqwvJg0FAlKt_vRWwUH79nchiFZ0763hM_oDTpRw00YTMUe96K7z9jyY9mG64RFqrwUpNVzFxOo7Cye4kFstj8L3_prxfuiVcXVzt0cykIAz-t-2YuQhoExCN3PFY6SfvR6JgujfrvHU5cEi1GuDWmuHVfZdIAKm4UwnQ3ViYcH6TxQyLR4hUcG0TtbxleK109nQcfNTiwb9zQYlm-ZzCa9OzWe4VeJFEqdbIOocH37_fYHmtNgtGN5eQujHI1qSgxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه های استقلالی: روزبه چشمی در مذاکرتش برای تمدید قرارداد با باشگاه استقلال به مدیران این تیم اعلام کرده است که از پرسپولیس پیشنهاد دارم تا رقم قراردادش را بالاتر ببرند
😆
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136209" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136208" target="_blank">📅 18:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136207" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136206" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVPtnxzm1UmUJxSOQztgOYkEo2yeDqVFuumy18JFqOKQ2f1BJd2ffAzJNRcW_g165Nip2ame_3oWRB13bIh0ktszAvRUF2degylf9FCgFWbZiBgtfE6Qs1WesiXfvridudccAff-FcXwr0f3OkRloI5P_ziIfzv0cFlUEQbcMEZs5upjON3x4gu74sRBnb-YkSePi9_u8Jp6BmyYg5Vc8xkVx4rc9OBz3kI1wUttus_ukakbEEB6ieaoypPEUtX8J6D3fEw5-FSkzBXJ9Ptm_utKnlGnpQqv9w4NqrFxvvWmlwOn0d-KyGuGGmDROaxvwGP-Je1eNRkXWp50pTOu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قدوسی: ابوالفضل رزاق‌پور گزینه اول جانشینی میلاد محمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136205" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136204" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUz1ugfeDJnOzGjXbiWxqqQVN-zoBqaInIcGEyeQvHEqsfgyNCyQ8CO89eZJVkXc6XAqrL6upgcvngBpOq-8AyHQ49DKrXi9itf7fow2FT0mWEIoK1B05G6UUuTr_lr25psLSXzuMNpzvoXVaj_baOfzmvvasdcBG4z1mR44pQYXx0Ik-_MbkCcMgyef7Tws598x5zu-hmlUd32nho_c0-FTrhx-wr965SStGBpFkmi4oTaRb_sPSHk7s9s2XvLMlnvlDAdslv5Ph7_Cq2czolj11qzlZrw9_0Eu2_Mn6So9ISMQn7TpJZIuedRfeGHNpe612cAFTzrXvQCw7cvf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
میلاد محمدی در یک غافلگیری با عقد قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/136203" target="_blank">📅 18:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136202" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIyRdDreA9EDlgDu_Ou7B3eR7FB8noc3MM1ES8exELlN_hZNUWnGMi_K_GQJr6Hdb4kllx58DUCkUf4ErzYEJ6eBx-1a2Jekl43-XUXVZrWSRR9gAxKRn-Meurb7E0QG-vR5dT_y9_TSJ0HdrhpP7giVWcnLCBOx35AGKtGD6e5yg8toGKNvCbd1iI74UBpPefXisjxHvPsWyDIxsFDtD1P3P1VlxoMHXWxVUYOL4yeeF5O8OdkFn5GKgXbF4X-_D9Tz5uCALo7gkzKNs4EXR85h7NEi6mXyIjkIJrfBG0bQwS5Z8eZ7mNTymdmlP8pqyIVDZdb6OmArIIj0ohisww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
خب میلاد محمدی هم ترجیح داد به جای پرسپولیس به لیگ بلاروس بره
❌
رسمی؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136201" target="_blank">📅 18:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136200" target="_blank">📅 17:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
❗️
درصورت عقد قرارداد تیم پرسپولیس با آلن هلیلوویچ این بازیکنان جانشین سروش رفیعی در این تیم خواهد شد. پست اصلی هلیلوویچ هافبک تهاجمی - بازیساز است اما در پست وینگر و حتی مهاجم نیز بازی کرده. احتمال عقدقرارداد زیاده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136199" target="_blank">📅 17:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
از تمرینات پرسپولیس خبر رسیده دنیل گرا را در پست هافبک دفاعی و دفاع چپ در حال تست هستند اگه جواب داد بمونه!
🔴
گرا برای جدایی درخواست مبلغ ۵۰۰ هزار دلاری کرده مدیران پرسپولیس برای اینکه غرامت ندن فشار اوردن گرا بمونه اما تصمیم آخر مهدی تارتار میگیره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136198" target="_blank">📅 16:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
آمار افتضاح تیم ملی والیبال در لیگ ملت های امسال :
🔴
12 بازی
🔴
3 برد
🔴
9 باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136197" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYpXh5OMz7IDbEyKpBt6avlT1oqZswJ9PXW2KOJTvu-RoSk5v5sbnEvlmj2uXPwBZaS1_HaQIaZnhZDtS8Zx-ciLVmlcwhWV_hlL0CDDO7Tg5gWFEKPY8sNY5Wyz1qwH9SBTBlVCdfcWClDft4aWCPLljRFCJpKKFFfYOFi7GfQhYKtlSp3Gmp4Rzb8QYn6BsS5XP1FMq4hMb-IQTSG0keye2e9dDjBGt9nk80NhSoiZv_8UT5NxZdpPxYrxSFkHJlc8qcun5j2Z6sq4iHfxqyuOqFYQDvJvtaCh9KeACVkUeFPk7sBk54u2WXDWJgoT75bAFmqF668wf60Tl9sH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رقم قرارداد دانیال ایری،‌بالاست، ولی می تواند قرضی به پرسپولیس بیاید. او بند خرید دائمی در نیم فصل دارد و بنظر می آید نساجی مایل به فروش کسری طاهری است. ضمن اینکه جذب علی نعمتی و قریشی هم قبلاً کنسل شده بود
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136196" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
فرهیختگان: پرسپولیس دنبال مشتری برای بیفوما و گراست؛ گرا مشتری ندارد و بیفوما فقط در صورت آزاد شدن خواهان دارد. چون قرارداد بیفوما ۸۵۰ هزار دلار است، احتمالاً پرسپولیس باید برای جدایی‌اش غرامت بدهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136195" target="_blank">📅 15:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
برای جذب طاهری مراحل قانونی ش باید از طریق فیفا پیگیری و استعلام گرفته بشه که منجر به بستن پنجره نقل و انتقالاتی تیم نشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136194" target="_blank">📅 15:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
❗️
شنیده می‌شود شروط پرسپولیس برای هلیلوویچ نیز با موافقت این بازیکن همراه شده و احتمالاً او در اردو و تمرینات سرخپوشان در ترکیه حاضر خواهد شد.یکی دیگر از چالش‌های پیش‌روی باشگاه پرسپولیس با آلن هلیلوویچ بحث شرایط خاص و فورس ماژور در قرارداد او بود که ظاهراً…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136193" target="_blank">📅 15:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136192" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136192" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BUl0TPdHPd5luRhD7b-GSeUp02nG7qPoFmzDOF8wKiI3snoe0WytTP7vfzCzgSUxaHBDCJsebDR0DiJe-2r7_FetZNFueoSHQRxHrXnPg_ScKhWmZpgNGhYopZwmvLcPcugJLtcL2i85POoJA3zpJAeX0Jv8m6lQRa-jk9-EU8xmKAuxHiZoaGDajkoi7KEj0_YEoBZj-GSidux7_SfbVKisiO2uDiHARc1G31qSqRhQ4jJp2c15e_pdQBseNQE20ReFuGmDfrCZm8IYw3xBjfiS6pd4_7lq-uqs7ilb28lV1jNzsVP3oSzwgb1BJdQaPB1mPkB2XPVtGTLQ4jWhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال فوووق جذااااب
آرژانتین
و
اسپانیا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136191" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136190" target="_blank">📅 14:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده:
🔴
افزایش لیست بزرگسالان هر تیم از 20 بازیکن به 21 بازیکن
🔴
افزایش لیست زیر 25 سال هر تیم از 2 بازیکن به 5 بازیکن
🔴
افزایش سهیمه لیگ برتری هر تیم از 7 بازیکن به 11 بازیکن
🔴
کاهش تعداد بازیکنان خارجی هر تیم از 8 بازیکن به 4 بازیکن
🔴
افزایش تعداد بازیکنان نیمکت نشین به 23 بازیکن (هر بازی 3 بازیکن زیر 21 سال باید روی نیمکت باشد)
🔴
این مصوبات هییت رییسه سازمان لیگ است و برای تصویب و اجرایی شدن آن راهی هیات رییسه فدراسیون فوتبال شده تا پس از بررسی تصویب و ابلاغ شود. همچنین گفتنی است این مصوبات تنها برای لیگ 18 تیمی قابل اجرا خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136189" target="_blank">📅 13:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
غیررسمی: محمدرضا اخباری با قراردادی 1+1 ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136188" target="_blank">📅 12:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
🔹
تارتار هنوز درباره‌ی جهانبخش و قدوس نظری نداده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136187" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
قرارداد محمدرضا اخباری به خاطر این که بازیکن آزاد هست قراره به صورت بازیکن آزاد ثبت بشه و مشکلی برای سهیمه لیگ برتری پرسپولیس ایجاد نمیکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136186" target="_blank">📅 10:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
آخرین وضعیت نقل و انتقالات و شرایط باشگاه پرسپولیس از زبان رضا جباری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136185" target="_blank">📅 10:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136184" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
تسنیم / جزئیاتی از مذاکره پرسپولیس با بازیکن سابق بارسا، 2 شرط برای عقد قرارداد
🔴
🔴
باشگاه پرسپولیس ابتدا از هلیلوویچ خواسته تا در اردوی این تیم در ترکیه شرکت کند و کادرفنی پس از زیر نظر گرفتن این بازیکن، نظر نهایی را درباره کیفیت فنی او اعلام کند. در صورت…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136183" target="_blank">📅 10:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
پروفایل ترنسفرمارکت هالیلوویچ، این بازیکن 30 ساله به احتمال زیاد جانشین سروش رفیعی در پست شماره 10 خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136182" target="_blank">📅 10:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=bkuNi9SAHDPsdO_yPKJ6TE01AIVfKjXmlAFkeSsD6cn8hKroqiyG1JhNqm-hAPY_4UYzWdScSUXfsnb5sAbq0XSM-dhB3y6yKinpw24KnuzW4Fponcptx9Ig1g2FPE241NtvCjU8O9mz7mFW0bm2XLhbWz9d4IhsyK49MnCulYTCAcfPa15GffuSZ-o27qptShTWeCPs5F0NUQhsuFLGejazWWGiJm_bnBa4nxF4AOJiOCwTGCuWCA2ue2yUiWVjhUEnNRHMNRrMbuxT5OVsWhrk_zIDkJ652dhVY9SPOqE0kL4O9isuD-UmcBxAa0cS8MxDbSj4Hld-6rW5ifGouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=bkuNi9SAHDPsdO_yPKJ6TE01AIVfKjXmlAFkeSsD6cn8hKroqiyG1JhNqm-hAPY_4UYzWdScSUXfsnb5sAbq0XSM-dhB3y6yKinpw24KnuzW4Fponcptx9Ig1g2FPE241NtvCjU8O9mz7mFW0bm2XLhbWz9d4IhsyK49MnCulYTCAcfPa15GffuSZ-o27qptShTWeCPs5F0NUQhsuFLGejazWWGiJm_bnBa4nxF4AOJiOCwTGCuWCA2ue2yUiWVjhUEnNRHMNRrMbuxT5OVsWhrk_zIDkJ652dhVY9SPOqE0kL4O9isuD-UmcBxAa0cS8MxDbSj4Hld-6rW5ifGouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جواب تامل برانگیز جواد کاطمیان به سوال اینکه چرا ازدواج نمیکنی: دنیا پرظلم و پر کثافت، پر از آدم کشی، پر از بچه کشی؛ ازدواج کنم که چی بشه اخه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136181" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
شنیده ها: پرسپولیس برای جذب محمد مهدی محبی نامه زده به باشگاه اتحاد الکبا تا اگه بشه این بازیکن رو از تراکتور هایجک کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136180" target="_blank">📅 09:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏆
فیلم خلاصه بازی فرانسه 4 _ 6 انگلیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136179" target="_blank">📅 09:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
مذاکرات مثبت پرسپولیس با قدوس/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136178" target="_blank">📅 09:09 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
