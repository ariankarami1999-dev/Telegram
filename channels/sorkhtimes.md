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
<img src="https://cdn4.telesco.pe/file/PO-jbnKWBj2iqPmITiV1CgPupG4rOVA_aPO2w-GBC1jgMa0MaN5kgX1nXJdfpO13ffmB3nlJa2iu8AxcuuNHtW9kAHxllrq-4uWZrc2nckN0pAau_rgFpG10FzvFVlSRO8giv9D4AY5c0OIrRVI_-HHkNaUqSnWRsrmEaNP1BQkZDxmrRNk68PJdOf4snc5jV3Lq-tzUjGmSRlrjIqpkb0dBbIPLpxd4AXRnxZa_YceGAcxoM_CHpTs94ytznp97pTmwRzDjLkunt2U7kn6s4ZY_ogAPa56Yp_pZMgzzfe1JA-25UtPCjXV_nyhJsHWGW7XAvcm4NUiIUGLttro0LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFk4y5Ht6F35QzlMZEDOuBaWlgktuG55gXE4keV4fCmgFvpCy7mBGv0E51Dng-BVscvY5OfX33vodOrWZL9d3Xz2gMrSMDyWXN7FG41kg4Qj8tpu4HrAUG8t7bFnVtaY4WePovOS79XG5eB2H89hZ0YWYS4tkxInOUm0UGlG-LbP1GoFEEoa89qdKxivz0M8LCSEJM0nCIIWTt3Mc4X6qC0Rqk4DAPj4fB2NQMbez2qP0Ac9xmMQZfO38NxeDzqfXwTkAAcVhtujqt0FH-nVLGmgkveY33wsvcM5yimbVgHuQrExYNGMEP3PrX_YzVJu3LG89n-ldn64_zMbuRmlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SorkhTimes/134456" target="_blank">📅 13:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
مازاد شدن ابرقویی‌نژاد صحت دارد؟
❌
در ساعات اخیر اخباری در خصوص حضور ابرقویی‌نژاد در لیست مازاد پرسپولیس منتشر شده است. مازاد شدن حسین ابرقویی‌نژاد صحت ندارد چراکه اوسمار لیست مازاد ارائه نکرده است.
✍️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/134455" target="_blank">📅 13:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG-VaJSU5WUwBiHUlIuY9onq2G6SBPN4aETmShJcUuvyaQ0paQ1ZSzrJrRWKvGRNyscLRAwapQf7ESIvWF8scsaT32oizC3O0hx2J11wWv_bFj4CGkIigowQUeeu2w69Xgrvm_sxD2GEj_kirkj86PGlsExa8o36YmLv1Mkv5Vu74rdi2XF9OU3RPfSURV3_l1Lh_VTtKjfQnbOUISr_sCOj6mxPWzuyOukD69EIK6QD43CScbMO9U5ZXG5Plg4pVbdHsEsxM6kyYY3EXP0zEjHk9w2xBbIwKgy118Rn7Yk5rkD04dJtHwzRWdrs487VDJ8F34RTRKlGmLwFRXKlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رامین رضاییان بعد از وینیسیوس جونیور بیشترین جایزه‌ (بهترین بازیکن زمین) در این جام‌ جهانی را گرفته است. همچنین رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/134454" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/134453" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5SrQ_l5VQSA8lxH326Pf4EEgH8Qs_7-SkQEDoJaMfHcE0mBVdFUQuLBwHzR6tBOJjKhZ7zld3oj6ztpTdTq9TGh-kkM2l7S3DyQMvKkyZDl7A4I0aFY9vgXQGpdN7PMzIauXkYV5oFJ90Syt1nAMBBGJjsEUtzHCCw0o2CDoYEXvlZRexYUXLaBnNyrbNS7_Jr43cIVPDJmEcysb2X0IVqDH2JtHOYNwQASQLSrBaMuPP7H9COw6YgZZpt4NPvFWuOX_TWiaZqUt4gQ0ahyS7AUF7LwisEeBJy3We2eKDGs_Kt0cpHfedPHUbLqgi6yTlpwLJ5cJNfO0z0LHcOV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SorkhTimes/134452" target="_blank">📅 13:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/134451" target="_blank">📅 12:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWQzUFAtVvP1zlgp4WaFjOy492De4hFLDeCkFnzsJX-ujkLFinctlsAirQawM2SJoGGmaQxa8HYUaUaq701oBShmbzBaA2AHBoQ4bp6WeNWdEyugn0Sol8W0dvVOlYhJ5R9th9jOUOhsFFHZpZo9KnEVEe6gXJJJXGZJajaej5Wm861Hajjn6-JBn_io7QL8JHUaomb6xXcG_bdiCO6lcG95iiR3HXEGss3u9RWXVv7qD_fAhIc9rrGyCG6G0lbJ6hm_bfXH6JvC3XhDvTIYjrD4tAos3huZW-GNqTHz4xOCYf_b5I9eSvUZ9QDHms-BvgFKkE7tgt_qUnmQeHmLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملاقات مهدی مهدوی کیا واینفانتینو درحاشیه دیدار ایران
⚔️
مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/134450" target="_blank">📅 11:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
فقط کافیه بازی امشب اتریش و الجزایر مساوی نشه ..ایران صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/134449" target="_blank">📅 11:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shllglmsr16yzJ8HJjrpLJrg_OrfR4v4LmLuAqXVzhovjeholLbTwJDaMbHc4aoPaCXHi_lHm-dnT5Mp9_hCQbfVqrqlXta4ZiLMx9OrlU_zhB6qoVDMbUngEFrrr3-ojX2jqdoDR2Q1yZc--LCjxRAWZk4JLYE4kxK-Bl1AaxoOhJXPIcvUahN2HYQdJ_mVG_lRdDuLxp9GSyWxRa544QRk0cmNoib32LzxdZyfsyeeQfPG0AV69qYhcq9gE2gJ2tSl0ICr1mCVnjZ1cv7d24HLGTj2_mTbBYTcri1kJ6WjeBIEd8emiOJsCHNu2SvVzIBZpfw7CXWvpXc7WlnabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/134448" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380ln61xx2btHQ7s1c2XwzcIX5H0bZpF-x_eN9kLA5ByWHcNVeyq-JiJ9PLGEWBex729GnIygx7GrucoZbxfjAI3eACpF_GPG7xR85Z6WhB0a2e-eBtIEseN02KbQbn0XyUQA2dAFqmlwnIA35BthUP468baoqqW_oFy9sHkqOpglpn4d_HP1Zld56tMUnhUvcm3LsPkG9BMLLVgI_uNa2EOleZRrl4ibtX1tZ46rSYWSjveLYoOEw-cM9Y-wptmszGhHnsHH18Qcn58366gY3p6vjXv7JydsXcJ9-r_h4fZcXVNZU_sbsgr5FJ3gJmcgKgfJIDYrCsQ8km3rX_gyarL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380ln61xx2btHQ7s1c2XwzcIX5H0bZpF-x_eN9kLA5ByWHcNVeyq-JiJ9PLGEWBex729GnIygx7GrucoZbxfjAI3eACpF_GPG7xR85Z6WhB0a2e-eBtIEseN02KbQbn0XyUQA2dAFqmlwnIA35BthUP468baoqqW_oFy9sHkqOpglpn4d_HP1Zld56tMUnhUvcm3LsPkG9BMLLVgI_uNa2EOleZRrl4ibtX1tZ46rSYWSjveLYoOEw-cM9Y-wptmszGhHnsHH18Qcn58366gY3p6vjXv7JydsXcJ9-r_h4fZcXVNZU_sbsgr5FJ3gJmcgKgfJIDYrCsQ8km3rX_gyarL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش مجری شبکه پرسپولیس بعد از گل دوم چادرملو و شکست قرمز پوشان در پلی آف لیگ قهرمانان آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134447" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTB8D_DVoFrwSuYr-AegqZqdOVqTSklxZmE0TbI06BDZLcStWs4KQhQ_6lXp7zfia6t7_vRTZRO_cnnsSHlQgHAKI7gpQvWSLysAYAr15HQIDqPd0b8h0TVqVvUjFD8l_9OzEiRQLsi1mYQQ3b7uOLi41x_5JQq4hXAgJMq9Phrq6RPBmgojHeNGokS5AStiwgzadZx0938oHq1lxMnj8PWxcnABW4ihDD-3ko2b6vDiIKiah1rWrgjpgcGM-X1JwTSMxEUEBJg9jMgyjdCsD648GmuzztxqI-vdQPSdajsrNwE7uUof-n_cxPYQo9P8uUndYgjW9t_mgeKGVhC-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا منصفانه است، خب اوکی، خوش به حالشان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/134446" target="_blank">📅 11:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134445" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/134444" target="_blank">📅 11:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv54jkREQ_jIMzwaf5qVn3_wRQIye_-sYeKTtqOnMNoJheF3UJsVZ_2pSg5tnZBD5hArysPtoDKxRbSWM2YWZHCuXOdJsauhAJeMtqpRj0mkwaIENXP0YEZb38nOrhC_QNk55PCidU8BIOi8mvzfFLhGDBWYBlNmRZoPBfNUv8gtXLIE0HzIQLhoUs37VOg0UnQ2ZXY0hITd8GL5y2sGveHPHIJ10YlVSW5jd412OJGmhhICfdhHAjjuzFv0wdi3rNyQ2h7AYktBzpt1tmbIuNb_zDuHEMD67tAs--3gsnSjHLTAx_Wc4ts6DfIk-fMeV6nNtfRHMDytOgayx64T5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
دلیل اینکه گل شجاع افساید شد
✅
طبق قانون موقعیت آفساید بر اساس «دومین بازیکن آخر تیم مدافع» تعیین میشه
🔴
در این صحنه بازیکن آبی آخرین مدافع حساب میشه و بازیکن زرد مدافع دوم حساب میشه
🔴
دروازه بان در قانون آفساید نقشی نداره و جز مدافعان اخر حساب میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/134443" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/134442" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/134441" target="_blank">📅 10:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/134440" target="_blank">📅 10:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
سوژه شدی رفت شجاع جون
🍇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/134439" target="_blank">📅 10:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/134438" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/134437" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134436" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=LBaEOhUXnTdeGef25kQNfCahque-bRu55V-BvtNxEFdvyXEsi18vKinUZJT8XMUVwz8hEBrEaPB66Gn4RrTMn7_VSNyKys7-dfqlnWAehWWm_0Ew9_sW5VyavyT5NEVI-OwgpUX4Hynkm8_PjGQVHfueo6d_eE68lzRcIbzxc5huE1W8yZO84E362Z5kq9voA8ri97xGjVzouxDyhoHiJeev86iCcwWhSYB0m6QCCKLR0pNUivrX3Ifip_ryIFQuZWgTyrHK2mCCM1UZW4CFAhKa_bLvFTsmOHbFwMFWLNhV3mz3IlW-TgSg7Z1wbt7AvQ_W2ynOEQv9kWoYkkDokA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=LBaEOhUXnTdeGef25kQNfCahque-bRu55V-BvtNxEFdvyXEsi18vKinUZJT8XMUVwz8hEBrEaPB66Gn4RrTMn7_VSNyKys7-dfqlnWAehWWm_0Ew9_sW5VyavyT5NEVI-OwgpUX4Hynkm8_PjGQVHfueo6d_eE68lzRcIbzxc5huE1W8yZO84E362Z5kq9voA8ri97xGjVzouxDyhoHiJeev86iCcwWhSYB0m6QCCKLR0pNUivrX3Ifip_ryIFQuZWgTyrHK2mCCM1UZW4CFAhKa_bLvFTsmOHbFwMFWLNhV3mz3IlW-TgSg7Z1wbt7AvQ_W2ynOEQv9kWoYkkDokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
قلعه نویی:
اینم یه آزمایشیه، شاید خدا داره منو میکنه.
😱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/134435" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134434">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff37ffd9.mp4?token=Rzz4Ns7eOnfDhnCiqS8uXt2xYXDGKol_9x5hI5nft1kM6_8GaXQEmB3JKg352Xaa9bWHteJQy1Swbj4ydiJMrmRoj0vE1LugBn2OJITOJAUSfty4hn2ie2ZYtkSUXjUnyh86-Wz-qwAr29jhuYz30gnhenNSywerfjwqx4Dx_LtZ2BEzMAwP7EAHk1as4sLv5Mk47zY82W-hswGGw7zq-T3HyE863eF2w9MejwquEY-xRXRww9LRGugZXYwWgZ1i4SezDZUcAtVgrwLLuSLdidAICpWEOpqxQ8juQR9H-N-Nd_ZpDJaoItN5gfEm9psTCdOCQjwM1cvv4hGkgMeqrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff37ffd9.mp4?token=Rzz4Ns7eOnfDhnCiqS8uXt2xYXDGKol_9x5hI5nft1kM6_8GaXQEmB3JKg352Xaa9bWHteJQy1Swbj4ydiJMrmRoj0vE1LugBn2OJITOJAUSfty4hn2ie2ZYtkSUXjUnyh86-Wz-qwAr29jhuYz30gnhenNSywerfjwqx4Dx_LtZ2BEzMAwP7EAHk1as4sLv5Mk47zY82W-hswGGw7zq-T3HyE863eF2w9MejwquEY-xRXRww9LRGugZXYwWgZ1i4SezDZUcAtVgrwLLuSLdidAICpWEOpqxQ8juQR9H-N-Nd_ZpDJaoItN5gfEm9psTCdOCQjwM1cvv4hGkgMeqrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه نویی چیو سانت کرده: همه 5 سانت و ده سانت و سی سانت
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/134434" target="_blank">📅 09:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
جونم ایران ..گل اول و زدیم ...پنالتی و جبران کردیم ...رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/134433" target="_blank">📅 09:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134432">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkDZS7-sty_eHQh5JaZ0D1fSkjAGB_b-1q4aK9m4A_nbfWNF1zMUBIeyej63mkA0fJaiFRCZdmx7VOJpLu5eHEwbfEevgi2cKuJoM94c6vreUoDAbu9Y1uJYX9CE4o84VzSTZPmammnhd-bUg18uJqF5KCCoAzlpNH1MkWyU2pp0f6oiBpyzGkz0ngFVNuzUL64HW84KfozRfmgC4nZEsYig-yVej0tWGBQ939nt9ybyC0xVqwrj7cusLFOw3c_snUtSUbg6fUbRLiIQSK8KMVF6WeOctIl15TIb0_bgYyrWPO1_0JJUvIG_pIthqxziDLDflyzkE5FFka1PS_sFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سوژه شدی رفت شجاع جون
🍇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/134432" target="_blank">📅 09:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134431">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
امیدوارم امشب کی‌روش و ارونوف برای ایران کاری بکنن خیلی بعیدع ولی شانس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/134431" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134430">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
تو بهترین نیمه دوم ایران تو جام جهانی متاسفانه دو تیر و یک گل آفساید زدیم ولی نبردیم بازی و خیلی حیف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/134430" target="_blank">📅 09:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134429">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
✅
ایران 3 امتیازی صعود خواهد کرد یا خیر؟
⌛️
در صورتی که ایران برابر مصر به تساوی دست پیدا کند و با 3 امتیاز در رده سوم گروه خود باشد آنگاه باید منتظر نتایج سایر رقبا باشد
⌛️
برای قطعی شدن صعود تیم ایران باید 2 اتفاق از 4 اتفاق زیر رخ بدهد
1️⃣
. غنا موفق…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/134429" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134428">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
شروع نیمه دوم ....حساسترین 45 دقیقه تاریخ ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/134428" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134427">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2t0wD3_zoUP-9ipjwuoMqFx0mP-dGW-sGGBjtW3DPRlUNOH7iJqh8-exoBIo6ScQmIS-LlTtRycNWFOPg3r8GaiKPm_epS77u43Y1BPtg0wlEBpowTcBNeYUPjdw5K6kfEdCuLB4fFueE2QA_zoN69YPPD_PDLRGCayYy3q2Pjue6_A1AuARkxsBCLR5AU8Om71vOylnIyFqwmd8DjrKs8APCr2OiN69UyYOqBISAuytmSlCTjnvyziNKvXJwrZEpvh8a81hkScabScjBy4BgdiEnSpEUWsPM33D6rBlr0k2JZ518xpjH7aeyS5IGSIFvGmbB01uy617TcohFNK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر بامداد جمعه ایران
⚪️
-
🔴
مصر رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/134427" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134426">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
| پایان نیمه اول
🇮🇷
ایران
1️⃣
🆚
1️⃣
مصر
🇪🇬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/134426" target="_blank">📅 07:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134425">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚪️
گل اول ایران به مصر توسط رامین رضاییان 14
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134425" target="_blank">📅 07:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134424">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20439446e.mp4?token=njwgeit9Ymxy-WJImISzg7PlCLXL8_YVYdEjQ64UZPTyKPKVo2zTk_TaFZoorSs6GEDPlosSL1HnbdWziP72qkg2fP14YdWFXRVwvM12DcSQ28aT8qVv2mTv0_m5xMcZniK5LcJRJiT1jHUh1Uz3qddEri2cwkerN1DscvexAqvlQXGE1525kNpFQDElGSJ3VvhDtMmPPUWMsKiDhnloeq7vA25MYmyskYXdmsnU49UFzrCdqeIZeJJMc90hyxBR9q-4WYko-ckMz43RiSvShsks8JkEuzdXNAU1su_9phDxtTtYZ2j8x0eFcbqxn4NPIhYOSIoIfYo7llt20yVn-CHMKQf9YCcfqNHJohPY30JCJJh4ByViBBI-k5ogYAcTzDIRyLw2YGIP_HUUXUCDj16IsqnjD-FnCJr_E-I4sJcroF_8oz4A_mdd2xxFNqnbQrE03WACmqB_C30r2AAAlYbd7X_pIOiXH6IeIWBWVq-jD95y90sYSfENSkEiqKguwVyanerl7IbCtY1CGiPPJo5bQGsHz5z-VLAY9V2O9aUpahHxNIfkjAyB3b7MppMPcImzDzbV3z-v2j58ADvPivs2T1YEqw35BtkJaCykEcW_b5vUKfHFm56L-8KaZLcEnMBeRp6Rxnbjy8wH9KJ7yRah6RqEfga_UxEkWnGLw40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20439446e.mp4?token=njwgeit9Ymxy-WJImISzg7PlCLXL8_YVYdEjQ64UZPTyKPKVo2zTk_TaFZoorSs6GEDPlosSL1HnbdWziP72qkg2fP14YdWFXRVwvM12DcSQ28aT8qVv2mTv0_m5xMcZniK5LcJRJiT1jHUh1Uz3qddEri2cwkerN1DscvexAqvlQXGE1525kNpFQDElGSJ3VvhDtMmPPUWMsKiDhnloeq7vA25MYmyskYXdmsnU49UFzrCdqeIZeJJMc90hyxBR9q-4WYko-ckMz43RiSvShsks8JkEuzdXNAU1su_9phDxtTtYZ2j8x0eFcbqxn4NPIhYOSIoIfYo7llt20yVn-CHMKQf9YCcfqNHJohPY30JCJJh4ByViBBI-k5ogYAcTzDIRyLw2YGIP_HUUXUCDj16IsqnjD-FnCJr_E-I4sJcroF_8oz4A_mdd2xxFNqnbQrE03WACmqB_C30r2AAAlYbd7X_pIOiXH6IeIWBWVq-jD95y90sYSfENSkEiqKguwVyanerl7IbCtY1CGiPPJo5bQGsHz5z-VLAY9V2O9aUpahHxNIfkjAyB3b7MppMPcImzDzbV3z-v2j58ADvPivs2T1YEqw35BtkJaCykEcW_b5vUKfHFm56L-8KaZLcEnMBeRp6Rxnbjy8wH9KJ7yRah6RqEfga_UxEkWnGLw40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
گل اول ایران به مصر توسط رامین رضاییان 14
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/134424" target="_blank">📅 06:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134423">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/134423" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134422">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d86c48556.mp4?token=cqfWkrA_HMwyurGNzVmlyyzPQqnslLp5neuM80LX9DQ0bb-GwWAsIH9fA7iN3rHRB4J4JGQ3VrG3vCOecSp_A5R7UOwqUi2XVUwNw2AIJW3AneKZL8EK9saqPONek894ZeLWqnVnUxyfgZDefvxmGc8Au09qTgNiIb6iO9Z1-49Gw1FUBCfpATS4T6y-HdfQ2IFORvSyZfxcCioBGt3OYFzgSQV_MgmE07_Le-p-Medi974mtFLyZp5Mf3UXoY9pwy-BKXPjcrpXofQuFpDJ0jTO4DcR1C6j_GAUxGhVUvql9uPl9_dLEP5pF_J_otctXyH-ZeiUaJI_POtnKqP_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d86c48556.mp4?token=cqfWkrA_HMwyurGNzVmlyyzPQqnslLp5neuM80LX9DQ0bb-GwWAsIH9fA7iN3rHRB4J4JGQ3VrG3vCOecSp_A5R7UOwqUi2XVUwNw2AIJW3AneKZL8EK9saqPONek894ZeLWqnVnUxyfgZDefvxmGc8Au09qTgNiIb6iO9Z1-49Gw1FUBCfpATS4T6y-HdfQ2IFORvSyZfxcCioBGt3OYFzgSQV_MgmE07_Le-p-Medi974mtFLyZp5Mf3UXoY9pwy-BKXPjcrpXofQuFpDJ0jTO4DcR1C6j_GAUxGhVUvql9uPl9_dLEP5pF_J_otctXyH-ZeiUaJI_POtnKqP_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134422" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134421">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e272e0aecb.mp4?token=a5Yo-hFHpFooFZrebrMfK5ymB0DELBZDXEZXGABK_icXXgCItL1PtdURZl8YpHypOnnokX96mnOM1SJR5zFe-k0OP27wN1uGoTYjvS1CGHwETcdmqRgI4ZdaTGw2G-mNnF4YIco3IRh2fgx59BNx7BaNKqnxI0ByVYUAl6Abpe9UT0mG5UpDB7HDve6vbHZRKVhuFYmMPLXpOtt5zO7X-YnKo8HfAnTrScdKvRO5vPaOlsMticOKNbCZGvCewO9okdk70epllx0jxJryTjniBsIvDdQiGiltk3wZNYttJlQpqQaE9blOUqT2r4513ZAtih-yKq5LATnR5wsCjiqfNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e272e0aecb.mp4?token=a5Yo-hFHpFooFZrebrMfK5ymB0DELBZDXEZXGABK_icXXgCItL1PtdURZl8YpHypOnnokX96mnOM1SJR5zFe-k0OP27wN1uGoTYjvS1CGHwETcdmqRgI4ZdaTGw2G-mNnF4YIco3IRh2fgx59BNx7BaNKqnxI0ByVYUAl6Abpe9UT0mG5UpDB7HDve6vbHZRKVhuFYmMPLXpOtt5zO7X-YnKo8HfAnTrScdKvRO5vPaOlsMticOKNbCZGvCewO9okdk70epllx0jxJryTjniBsIvDdQiGiltk3wZNYttJlQpqQaE9blOUqT2r4513ZAtih-yKq5LATnR5wsCjiqfNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اشتباه بیرانوند؛
🔴
گل اول مصر توسط محمود صابر در دقیقه 5
🔴
ایران 0 - مصر 1
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134421" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134420">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/134420" target="_blank">📅 06:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134419">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇪🇬
ترکیب مصر هم مقابل ایران اومده محمد صلاح فیکس و عمر مرموش روی  نیمکته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/134419" target="_blank">📅 06:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134418">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7s4bfxwJ4eKYBMeUJb7aSf5LUrui2e_QqcQgmqu_yOTozVi6DpaWRhGDenZwAL10QW4qGbVsUZ2YoInxI8XNWmy0cn65FZYBktUBYiD3MXRbp8YwpbNoEbRV4pZvStlY638-CnkHB-zYMHChxJt1s-hxV5q58hcYUb7vd4uy_S6NzNQuoUhRoMdbzTGQncHOAjnBL5lMYeuEm419MbQDoOXFPHxJcG8RupPHFpjGmMrEfQ-xjGC9neQjsx3dV1r0L3AP485CGenmVZ3rqDDmMhhFi5rPh2oEpo6YWzAQsAgCfK2PszCBbMTgSjdpLzfRvPwigAgUXllJb3X8Vni0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه H جام جهانی 2026 پس از پایان مرحله گروهی
🇨🇻
کیپ وِرد با مساوی ۰_۰ مقابل
عربستان با ۳تا مساوی و ۳امتیاز به عنوان تیم دوم صعود کرد
😐
👍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134418" target="_blank">📅 06:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134417">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
قلعه تو کنفرانس قبل از بازی:
🔴
حساس‌ترین بازی تاریخ ایران است. بچه‌ها فقط باید مسائل تاکتیکی را با آرامش باید پیاده کنند. مصر تیم بسیار بزرگ و قابل احترامی است. آنها قدرتمند هستند اما ما هم ایرانیم و برنامه‌های خاص خود را داریم. شاید بعد از مسائل ذهنی و…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/134417" target="_blank">📅 06:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134416">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/134416" target="_blank">📅 06:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134415">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/134415" target="_blank">📅 05:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134414">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
ترکیب ایران مقابل بلژیک
🔴
علیرضا بیرانوند، صالح حردانی، محمد حسین کنعانی‌زادگان، شجاع خلیل‌زاده، علی نعمتی، سعید عزت‌اللهی، احسان حاج صفی، رامین رضاییان، سامان قدوس، محمد محبی و مهدی طارمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134414" target="_blank">📅 05:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👌
👌
👌
👌
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134413" target="_blank">📅 01:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVevqOLjJS3omTgF4PeTFxVHVpodXoaeMHDwQVEI2Lb9o3IgV9ATQhDLiT7IiLlXHF-IoTfhXjmvy_SUNnWW7ChWKMZA5g58hWbvuM-asj1kfNpSXPS_f1ehv_oyYzopq0DVUZ6wyNd2O_NXDuOpgcsjly3sgdm0fA9vQPcLWec9BG3GoS0jsjDLO9sGBkIflCVe6wMwiJ7GZ_Vsw1UJSw995boTjhEZbafL9B67jr3ckrYZb0BOiPxS3EppqzEIj-Iz_xW6ZrHq1DlX81Y2jxeVhM_QZisL7qWwpKMH_uXNSY64yHdG1jKdXsicx84Js4V3QJP1hyKSjuQKuP7n0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر بامداد جمعه ایران
⚪️
-
🔴
مصر رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134412" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from7 .</strong></div>
<div class="tg-text">حدادی کوتاهی نکرد تنها کسی میتونه پوست اندازی تیم رو شروع کنیم همین حدادیه</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/134411" target="_blank">📅 01:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽️
تیم پیشکسوتان ما این تیم رو باید میبرد
❗️
این تیم باید پوست اندازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134410" target="_blank">📅 01:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🤩
حدادی سهمیه مرده رو زنده کرد، با هزار یک لابی تیم ۶ جدول دو دستی داشت میرفت آسیا!الان مقصر باخت به تیم سوم چادرملو با دو جلسه تمرین کیه ؟!
❗️
تیم ما کل پولشونو گرفتن یک ماهه دارن تمرین میکنن، با سرمربی ۱.۲ میلیون دلاری که قبلش تپه نریده تو لیگ نزاشته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134409" target="_blank">📅 01:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#تلنگر
❌
❗️
پروژه بگیر ها و قالتاق ها دارن زیر پوستی حدادی رو میزنن خاستم بگم دنبال پدرتون بگردید… با تشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134408" target="_blank">📅 01:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤩
صحبت های پیمان حدادی بعداز بازی…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/134407" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
حالمون از این تیم داغونه و ناراحت .امیدوارم اتفاقات خوبی برای کادر و بازیکن بیفته .....بریم ی استراحت ریز کنیم .ساعت 6/30 برای بازی ایران بیدار شیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/134406" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkM9gSHJYT6J1ujKXRgj1dT_5kp_grUVY7KCrrXAuIiv6TLOdu_Di1f21MrsUfv0WeZlpJNPC6gLQFg28-em6WzLfBvwitmjm2S8dPe32MhZhwLWO1h0SktzI29gaVlDucoNpKBb6zou2r01LIGjqA_TPQp9brqB6bqYo8s4xaSFtLKgERVvMbdKQc7XCylwkN-EI8F7uy2taLKe8HGSB23g4FUR2ZSzKEElKT2yxgtDbmvsa_FCaJZBhQrZ9NN2M35fF4FVAV_X0coz4pCWcfO1qNwTyxWD5TaHg3d_KOTJMwyKD3I0DEoqSp7b_q36Ck4PQHZnAGkVne63oVp2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آپدیت جدول بهترین تیم‌های سوم گروهی
❗️
پ.ن: ایران با برد صعود میکنه، با باخت حذف میشه و با مساوی کارش به اما و اگر میکشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134405" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134404" target="_blank">📅 00:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134403">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134403" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134402">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
فردا 6/30 صبح بازی حساس ایران آغاز میشه .کیا بیدار میشن که ببینن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134402" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134401">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134401" target="_blank">📅 00:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134400">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
اخباری سرمربی چادرملو: 7 بازیکن با تیم ما قرارداد نداشتند ولی برای ما بازی کردند که از آنها ممنون هستم/ حق ما سهمیه آسیایی بود/ بر اساس آئین نامه حق صد در صد با تیم ما است/ به قیمت باخت و از دست رفتن سلامت بازیکنانمان بازی کردیم که نشان بدهیم فوتبال باید…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134400" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/744d80c96e.mp4?token=dy_nYlpzcfbRs8wfYaK4wiKy0ahzkprBrDB-vej72ShGKfQaIVPgjdOzHfyUQqsGn9xZljG_W1BEEbx6ryj-JqA_u6XKXLC9ZQnT3pd5G0n9fmRBhoZleBytRLcMJr-F4CpRTVImkoaxjLjfyj08pffmmfVmF49MDYoAeXWm3bonztjmzYBWl_2JJCktJZzde4KqwPd5O2njPtgR1A0sYTC9yAZ3zsLGfbGa95xEMk871n9OU5Gc0pA1vv3xKBZ3OZen22J-daur3CEqr9maG0ny42ZhgyTVVW8hbNLw7CbG09SOSBKttoAmPeyHUZAW55lngs1I-iRaxYlNEw6mfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/744d80c96e.mp4?token=dy_nYlpzcfbRs8wfYaK4wiKy0ahzkprBrDB-vej72ShGKfQaIVPgjdOzHfyUQqsGn9xZljG_W1BEEbx6ryj-JqA_u6XKXLC9ZQnT3pd5G0n9fmRBhoZleBytRLcMJr-F4CpRTVImkoaxjLjfyj08pffmmfVmF49MDYoAeXWm3bonztjmzYBWl_2JJCktJZzde4KqwPd5O2njPtgR1A0sYTC9yAZ3zsLGfbGa95xEMk871n9OU5Gc0pA1vv3xKBZ3OZen22J-daur3CEqr9maG0ny42ZhgyTVVW8hbNLw7CbG09SOSBKttoAmPeyHUZAW55lngs1I-iRaxYlNEw6mfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم لو رفته از رختکن پرسپولیس بعد از باخت به چادرملو، باقری خطاب به بازیکنان: هر بازیکنی که بازی نمی کند قیافه می گیرد/ فقط زبان شما خوب کار می کند!/ خاک بر سر باشگاه ما که زور می زند به آسیا برویم!/ مگر ما لیاقت این را داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134399" target="_blank">📅 00:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
اخباری سرمربی چادرملو:
7 بازیکن با تیم ما قرارداد نداشتند ولی برای ما بازی کردند که از آنها ممنون هستم/ حق ما سهمیه آسیایی بود/ بر اساس آئین نامه حق صد در صد با تیم ما است/ به قیمت باخت و از دست رفتن سلامت بازیکنانمان بازی کردیم که نشان بدهیم فوتبال باید تکلیفش در زمین مشخص شود نه در جای دیگر/ نمی دانم آیا تیمی که قبلا با قاطعیت انصراف داده الان بازی می کند؟/ از بازیکنانم خجالت کشیدم که چطور بدون تمرین برای ما بازی کردند/ برخی ها دیدن سعید اخباری و جایگاه چادرملو برایشان سنگین است/ این تیم با زحمت و تلاش به اینجا رسیده است/  امکانات خاصی نداریم و سال دوم است که در لیگ برتر حضور داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134398" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78f234af.mp4?token=TMfmhOcgWDSkTCqjrllGYVkelSiDIfzXKvSB1s20fR9VstRhFNu9vjZqLolpONgXQewPKQqmg9hXekCw93lve_bvVZvo9tCZmagdWt8OT_-U-6rqv1dsEmBiOho248VR-zdViU0bYBP54vCR9H9J8Wf7HstIRQafonlVQ4W2IcdxVslbLuwdv8s1EUBGEiGpAC676MlTsjSz8JGlsOT5mzdBWZ6Gm7LyMTZbz4qzso21HZ3y1AugEUPB6EmIMwrFNg5d8zp2Z2bScOkdcbuqwmh4QyOoqQUUXbg6HzTVaYiAnXLsOXNpy2aamm8j5WqZnqsv9EjGbEl57G-G-R1ykqZFW1Gyl6rzBkmkaStPPCMbutc5RufkegIj21udfcB7pq7yrvwWX3hEA-heffNe4gyz6wfPi5RWyB_hfpkD-XWkdsVJySq45LtOX2PLCk7JjUyJaqFokE4cnqtKuv7Cd0DPXOr20Ns5A_YLdQeUVLX7AUREWF9CnoepmcGbX1Q_lTFG_VzpnbY2WlehYkQdKamAZwwdw5EunOvTPCmkDriS-_Uifor6qqm8uIoQUGC37OdlnnjX9ZyH4oGzFulvyWBRqbTNw512HyWYQ_PDQniI0as8zHjmX69xXbifT8fa9pBnjHjre_2hn-dmXkJrqkAqeuJEChcianiKLMmd9JY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78f234af.mp4?token=TMfmhOcgWDSkTCqjrllGYVkelSiDIfzXKvSB1s20fR9VstRhFNu9vjZqLolpONgXQewPKQqmg9hXekCw93lve_bvVZvo9tCZmagdWt8OT_-U-6rqv1dsEmBiOho248VR-zdViU0bYBP54vCR9H9J8Wf7HstIRQafonlVQ4W2IcdxVslbLuwdv8s1EUBGEiGpAC676MlTsjSz8JGlsOT5mzdBWZ6Gm7LyMTZbz4qzso21HZ3y1AugEUPB6EmIMwrFNg5d8zp2Z2bScOkdcbuqwmh4QyOoqQUUXbg6HzTVaYiAnXLsOXNpy2aamm8j5WqZnqsv9EjGbEl57G-G-R1ykqZFW1Gyl6rzBkmkaStPPCMbutc5RufkegIj21udfcB7pq7yrvwWX3hEA-heffNe4gyz6wfPi5RWyB_hfpkD-XWkdsVJySq45LtOX2PLCk7JjUyJaqFokE4cnqtKuv7Cd0DPXOr20Ns5A_YLdQeUVLX7AUREWF9CnoepmcGbX1Q_lTFG_VzpnbY2WlehYkQdKamAZwwdw5EunOvTPCmkDriS-_Uifor6qqm8uIoQUGC37OdlnnjX9ZyH4oGzFulvyWBRqbTNw512HyWYQ_PDQniI0as8zHjmX69xXbifT8fa9pBnjHjre_2hn-dmXkJrqkAqeuJEChcianiKLMmd9JY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محسن خلیلی، معاون ورزشی پرسپولیس:
🔴
🔴
انتقادات کریم باقری به بازیکنان و ناراحتی حدادی از بازیکنان؟ در زمان کمی پرسپولیس به این شرایط نرسیده است. با دو الی سه پنجره پرسپولیس می تواند پوست اندازی کند. خیلی مواقع می گویند بازیکنان خوب لیگ را جذب کنید اما همه نمی توانند در این تیم موفق شود
🔴
🔴
نیاز به انگیزه و تمرکز بالا داریم.‌هر بازیکنی در پرسپولیس نمی تواند موفق شود. مسلما تغییراتی در پرسپولیس خواهد بود و حتما بازیکنانی مدنظر هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134397" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134396" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32fe1fda5.mp4?token=UtgrUXNkcU8NMkL3lrwnXctLIeWpiVburNa201PlsdjtsT8xthWrChI1H9DbwmtHTI8S3gRtFVQn77yU2TGqZPGlmmXiDnB7uoJjJ-IPT7wYi-xAr1t1r7nhHLldZjGb2DRTxQEbsIfSPUtZ0bxber0SVvpXpIzHYoBwWKiz5zq6VfZyYVrHlyRM8Q-9MQjoq3nITH96KA3UuSrcC2MdWiqFm7aZvB2X3OpjCpqM1GUippm20I25oLBH1FW9MZKQCsktEq0pfLwWVoQPhNjiy5B8YTLhOjX_wd07Ez3tEQe9uv0dmJGM4BicEeW4Y0m7Oy3P4lxmoYBg6Ds1lsbxekivlifZSedm9ic2n2GDxsVnbe-5dySDHx3Ccj-w9bAzdB9RjZ_Cm-d6hUixgMuf1m6p0qZB6mydo9c3TJIi9fNLx2PGtxRLnNhPldRrKDyjZKHNUDoLL-6l6auBDEHqD4pl8q4a5qDil3tSJfDgrJRqKl4iyPyRAaFgqzmTtS394jm0D27e3V0771q3EcEoDGjr0dTVzJXO_Y16kAMRVW6gqTGxTV_xrj77pw5cC2cK8E9fHf_CwR87_MTyVi9nKbK8yj2eaq5hU_kwPXef6M142x8bly82Qqs_FXWntizUOyV6umwQLAscvU67VFpYehDf2oudIY0ur0uyzTxmyuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32fe1fda5.mp4?token=UtgrUXNkcU8NMkL3lrwnXctLIeWpiVburNa201PlsdjtsT8xthWrChI1H9DbwmtHTI8S3gRtFVQn77yU2TGqZPGlmmXiDnB7uoJjJ-IPT7wYi-xAr1t1r7nhHLldZjGb2DRTxQEbsIfSPUtZ0bxber0SVvpXpIzHYoBwWKiz5zq6VfZyYVrHlyRM8Q-9MQjoq3nITH96KA3UuSrcC2MdWiqFm7aZvB2X3OpjCpqM1GUippm20I25oLBH1FW9MZKQCsktEq0pfLwWVoQPhNjiy5B8YTLhOjX_wd07Ez3tEQe9uv0dmJGM4BicEeW4Y0m7Oy3P4lxmoYBg6Ds1lsbxekivlifZSedm9ic2n2GDxsVnbe-5dySDHx3Ccj-w9bAzdB9RjZ_Cm-d6hUixgMuf1m6p0qZB6mydo9c3TJIi9fNLx2PGtxRLnNhPldRrKDyjZKHNUDoLL-6l6auBDEHqD4pl8q4a5qDil3tSJfDgrJRqKl4iyPyRAaFgqzmTtS394jm0D27e3V0771q3EcEoDGjr0dTVzJXO_Y16kAMRVW6gqTGxTV_xrj77pw5cC2cK8E9fHf_CwR87_MTyVi9nKbK8yj2eaq5hU_kwPXef6M142x8bly82Qqs_FXWntizUOyV6umwQLAscvU67VFpYehDf2oudIY0ur0uyzTxmyuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی: از هواداران پرسپولیس عذرخواهی می کنم. واقعا نتیجه غیرقابل باور است
🔴
تلاش کردیم بتوانیم از حق خودمان دفاع کنیم و به آسیا برویم. با اینکه نفرات خوبی هم در اختیار داشتیم اما نتوانستیم بازی را ببریم
🔴
چادرملو تمرین زیادی نکرده بود اما انگیره زیادی داشت به همین دلیل ما را شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134395" target="_blank">📅 00:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
اقای هوادار شما صدای باشگاهی، نیم فصل زن بانک شهرو گاییدید که اوسمار بیاد، شخص احمدی گفت گزینه اول و اخر تون باید اوسمار باشه هرچقدر خاست ما میدیم بیاریدش
❌
اینو نمیگم که بگم بانک شهر عالی کار کرده نه پارسال ایشون اگر پشت درویش نبود تیم با اون شلختگی و…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134394" target="_blank">📅 00:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134393">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚠️
اقای هوادار شما صدای باشگاهی، نیم فصل زن بانک شهرو گاییدید که اوسمار بیاد، شخص احمدی گفت گزینه اول و اخر تون باید اوسمار باشه هرچقدر خاست ما میدیم بیاریدش
❌
اینو نمیگم که بگم بانک شهر عالی کار کرده نه پارسال ایشون اگر پشت درویش نبود تیم با اون شلختگی و هاشمیان تو لیگ نمیرفت، ولی درس بگیرید اینقدر جوگیر نباشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134393" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134392">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62d8762d20.mp4?token=rtVkFl0u22P_ivTxN8sICIYptQlxtn84zJFf6cHWgqRlgUtdB5qZrGVVrXJXiMRR6AaDXc6I2ZcFT06X7s0jDJXhOk7O9MmzIHmnNBGtc2tOdZxQs1JWiG3-F6VUegcXYj1LNg8KI0GhRNhyUreBPW19GsIPwNv9cWf8CrIC00zVhpJWngFDtOVADTeg6B5WgZl6wSJQAoubCSZyOC7KT8JLosB-Vfl6-gRiYsXQEIphytikh1PhbaQJeiaf1eXLjRVBV07HeEf-q0c4eX6r-PHOv05Vjo0UY2wkMLPzkHM3LMcjGE4a_KOOMCFgIMMAw2VFHSW1wdgSSnsR4deRjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62d8762d20.mp4?token=rtVkFl0u22P_ivTxN8sICIYptQlxtn84zJFf6cHWgqRlgUtdB5qZrGVVrXJXiMRR6AaDXc6I2ZcFT06X7s0jDJXhOk7O9MmzIHmnNBGtc2tOdZxQs1JWiG3-F6VUegcXYj1LNg8KI0GhRNhyUreBPW19GsIPwNv9cWf8CrIC00zVhpJWngFDtOVADTeg6B5WgZl6wSJQAoubCSZyOC7KT8JLosB-Vfl6-gRiYsXQEIphytikh1PhbaQJeiaf1eXLjRVBV07HeEf-q0c4eX6r-PHOv05Vjo0UY2wkMLPzkHM3LMcjGE4a_KOOMCFgIMMAw2VFHSW1wdgSSnsR4deRjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کریم باقری: ما بد بازی کردیم و باختیم/ بازیکنان مقصر شکست هستند؟ در این یکی دوسال پرسپولیس شرایط خوبی نداشت آن هم به دلیل تغییرات زیاد است
❌
آمدن اسکوچیچ به پرسپولیس؟  تیم ما مربی داشت که بحث اسکوچیچ شد/ این موضوعات فقط حاشیه سازی  است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134392" target="_blank">📅 00:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚠️
موقعی که نیم فصل کون خودمو پاره کردم که اقای اوسمار داره با دلال هاش کیر میکنه تو نقل و انتقالات و تیم یه عده جوگیر میگفتن این مربی منتخب هواداره باشگاه هرچی که اوسمار کونده میگه باید بگه چشم، باز خوبه امضای ایشون و فرزاد حبیب الهی پای تک تک خرید ها و لیست هست؛ یه جوی راه انداختن نیم فصل هوادار هم جوگیر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134391" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134390" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
ک… اسب حضرت عباس تو دهن همه کس کارت اوسمار جاکش، پوفیوزای خونه خراب ریدم تو فرق سرتون دو ماه باشگاه و رسانه، مردن دارن کون خودشونو پاره کردن برای برگزار شدن سه جانبه، مدیران باشگاه تا کجا ها که نرفتن….
❌
یه جو غیرت تو وجود هیچکدوم تون نیست فقط پول مفت میگیرد میچوسید، شب میرید باغ کونده بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134389" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9b2dc774.mp4?token=Poz1FFLLJYe1pVFh8igSQ9MKwfVjC8QXZjYvUs7ETuYxrL5eW7F36Q0lCu8AwUkAzF5VgbhyFwI8JeM42TReLWAPqry9SlCwywVyRaqoLihtRljQgO_dwdPL5BzbYn2_VNQVMbp2VEYLUUhvLCZiM2xyAfRgNwhurTOaB2mCozis5jzMtDUA7nc3Xai528DFSF0LscLqhttS158bWDSNQE5PeomFVP53pdGDbvZ8TLZSvD30qget-0un29EWsB0s5ZVOMVf3hILOHq8eYEEskWvijbTlUGl4cyvTJgyRV-E6wYCTw0waebJ8TiOD8dGRApn3ohgCb6KIwQPNHzpn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9b2dc774.mp4?token=Poz1FFLLJYe1pVFh8igSQ9MKwfVjC8QXZjYvUs7ETuYxrL5eW7F36Q0lCu8AwUkAzF5VgbhyFwI8JeM42TReLWAPqry9SlCwywVyRaqoLihtRljQgO_dwdPL5BzbYn2_VNQVMbp2VEYLUUhvLCZiM2xyAfRgNwhurTOaB2mCozis5jzMtDUA7nc3Xai528DFSF0LscLqhttS158bWDSNQE5PeomFVP53pdGDbvZ8TLZSvD30qget-0un29EWsB0s5ZVOMVf3hILOHq8eYEEskWvijbTlUGl4cyvTJgyRV-E6wYCTw0waebJ8TiOD8dGRApn3ohgCb6KIwQPNHzpn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمد نوری کاپیتان اسبق پرسپولیس: واقعا برای بازیکنان تیم متاسفم، این پیراهن برای برخی از آنها گشاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134388" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
اسکوچیچ یکی از گزینه‌های ما است و باید در مورد او صحبت کنیم. خداداد عزیزی با پرسپولیس قرارداد ندارد و توافقی با او نشده است. او و محسن خلیلی گزینه‌های سرپرستی پرسپولیس هستند
🔴
بازیکن پرسپولیس رویش می‌شود پول از باشگاه بگیرد؟ در نیم فصل که صحبت از حضور اسکوچیچ…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134387" target="_blank">📅 00:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: با ایران داداشی شدیم و به توافق «صلح‌ تاریخی» رسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134386" target="_blank">📅 23:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
بخش دوم صحبت‌های طوفانی پیمان حدادی مدیرعامل پرسپولیس علیه بازیکنان
✅
بزرگتر(عالیشاه و پورعلی‌گنجی) باید بزرگی را در زمین بازی نشان بدهد نه فقط با حرف. این تیم باید جوان شود و پوست اندازی در آن صورت بگیرد
🔴
بعضی از بازیکنان پرسپولیس فردا خودشان باید قراردادشان…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134385" target="_blank">📅 23:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
عصبانیت آقا کریم که حسابی شاکی و عصبی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134384" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ee125817.mp4?token=IEEPhAXiImHgFOvnZUFThPzek4ks3uY8OZZpw66pkmUuX5HKVvHmb6nFCNMuJIQ12hLaniajC9IEJbZPrMWzekX5Ut2NGv8kXXY8yPwxB0Znuil0jGmAB-qNrAmWLf0ZFGoHxl5OJeoRo872lQpv-Md5Ux9Ut0e2749jJh5FaopcaXIeIpQjqanMmm2hi9JNRKg97bP-l0nJHzBYagoZZRwA2Z2uAm4pNwqKhfZP3aRswibmyW4xG1cJ78rOJhQfWCD5VZgmAClfcVixKOK4nyimHe69enBxw4NpP_f7s85J2bIqrKX-cbpbBN4C0GMTmw8msqUqZGtG_AUXULec-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ee125817.mp4?token=IEEPhAXiImHgFOvnZUFThPzek4ks3uY8OZZpw66pkmUuX5HKVvHmb6nFCNMuJIQ12hLaniajC9IEJbZPrMWzekX5Ut2NGv8kXXY8yPwxB0Znuil0jGmAB-qNrAmWLf0ZFGoHxl5OJeoRo872lQpv-Md5Ux9Ut0e2749jJh5FaopcaXIeIpQjqanMmm2hi9JNRKg97bP-l0nJHzBYagoZZRwA2Z2uAm4pNwqKhfZP3aRswibmyW4xG1cJ78rOJhQfWCD5VZgmAClfcVixKOK4nyimHe69enBxw4NpP_f7s85J2bIqrKX-cbpbBN4C0GMTmw8msqUqZGtG_AUXULec-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
عصبانیت آقا کریم که حسابی شاکی و عصبی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134383" target="_blank">📅 23:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c153d248.mp4?token=LInbOn8s7sVRWktOPM3p5PdAIBnR-56uNX2DoBqfowb1Ao6YbpW5uALvt5L-JRf8Km_WM-MnnLPTgYawZWq_mxPaLR0rib6iYx1kZCGEHifPvmTTN7N6pGJIgg9uAM0aK11zAKEDO157f5CoQpM7rQvuY7T7RCxk3qIbBWY8hLSoC_aw4zzcVuZFhJnbjx9nCmIzWH2smICUthCp-uIN5I31aloDg3X2r9XUOOa6Nqclm9kATOiRre_PxvlLcc6DKLQNaQVcZMccqUOS2RbU5SALWFsToqu9WrlDQhzzC0FClJKacy0UKheTcVcX3RmvljtFHFDMT-uDGpDW1kZ5g3yk-iypNC4zVJLC0fUJfFoLAmE6loS5hUBt3fDSbgCDw1OGQVUQmTtkqEoNDIu1CaQVia0pBXAlXThJrRzaPjUWw1Sp3X7Viy-kuiOEv5lFRb81GG-EmZIoW4uwmrzdFDW-IjrN4a-8Nch5vXCNpt1mBPblh3tMARdwTwtzfZuKsKowYLtaxncrz6PF1aAh7lrC8Fgogtws5hEt-t8KMryWSZiilOBlTPi5BKBSq-u_XSopKVVuRPSUbnCtoO1mVM5vDF-5BT9Bv2RXV7X76s7IY9bU54Scs7EIo-e0LFB00VYQ08P_7UFb0jlLsG7OgulXnEZ-33CIH_a9I5oYP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c153d248.mp4?token=LInbOn8s7sVRWktOPM3p5PdAIBnR-56uNX2DoBqfowb1Ao6YbpW5uALvt5L-JRf8Km_WM-MnnLPTgYawZWq_mxPaLR0rib6iYx1kZCGEHifPvmTTN7N6pGJIgg9uAM0aK11zAKEDO157f5CoQpM7rQvuY7T7RCxk3qIbBWY8hLSoC_aw4zzcVuZFhJnbjx9nCmIzWH2smICUthCp-uIN5I31aloDg3X2r9XUOOa6Nqclm9kATOiRre_PxvlLcc6DKLQNaQVcZMccqUOS2RbU5SALWFsToqu9WrlDQhzzC0FClJKacy0UKheTcVcX3RmvljtFHFDMT-uDGpDW1kZ5g3yk-iypNC4zVJLC0fUJfFoLAmE6loS5hUBt3fDSbgCDw1OGQVUQmTtkqEoNDIu1CaQVia0pBXAlXThJrRzaPjUWw1Sp3X7Viy-kuiOEv5lFRb81GG-EmZIoW4uwmrzdFDW-IjrN4a-8Nch5vXCNpt1mBPblh3tMARdwTwtzfZuKsKowYLtaxncrz6PF1aAh7lrC8Fgogtws5hEt-t8KMryWSZiilOBlTPi5BKBSq-u_XSopKVVuRPSUbnCtoO1mVM5vDF-5BT9Bv2RXV7X76s7IY9bU54Scs7EIo-e0LFB00VYQ08P_7UFb0jlLsG7OgulXnEZ-33CIH_a9I5oYP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بخش دوم صحبت‌های طوفانی پیمان حدادی مدیرعامل پرسپولیس علیه بازیکنان
✅
بزرگتر(عالیشاه و پورعلی‌گنجی) باید بزرگی را در زمین بازی نشان بدهد نه فقط با حرف. این تیم باید جوان شود و پوست اندازی در آن صورت بگیرد
🔴
بعضی از بازیکنان پرسپولیس فردا خودشان باید قراردادشان را فسخ کنند. آنها باید خجالت بکشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134382" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134381" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
پیمان حدادی مدیرعامل پرسپولیس:در این دو ماه گذشته تیم مدیریتی تمام تلاش خود را انجام داد.
🔻
نمی دانم چه نوع بازی کردن بود که بازیکنان تیم انجام دادند. کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی ها مشکل داشتند؟
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134380" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba8ed1d05.mp4?token=d64GRWkKEEkyrKt3fesyWPzPkFPiQUr4I4-tB1q0J78-3ha965ctR7zMaDXZqVg2pFwZHrNZAzK7-Z19lWmuAHzobg6oTqGFCyab0XAEl3wF5CYnT8c_lIwaCtAKoLi9xub_pWYH2rl7WGswjo5xZr0HkcOG2kPJTe-JHOorz4dTFLbPf7MLr8rva59FXO3WEGV-68k62_4CPszUhnf2et19lvx-ZxgA2_YsnedCweiW3AkZOm2B7Jsno4l3iOiHh56ESRSLK9BN17rXUPHmLhph1L3jh2uKFLwlPcNr32K5l_6v71KXwCR4IylaO7Il5dc9qPItkQbmwXsXJM7VsH8OAxmvSIEEPgS7TQ8ZZ7LljvgQBWVooz22goxjS5gIORWV6wHeSv-qxS1mU_Yin5-BK2Gh16f-HK9_IyT8q12AxCwSr1BwA3_KUH0UVKFLYbwwU1bbs9Q_7Rw6s5ZY1gQNIDDNoiM1AzRDKSWyWzdieEX1DeZC9ebfG4mPcVSOhR136dc0_Nyf9dks2WUDTOKndzMgntyZIKGS__somSQTbiOMuAVMeQWdcRiYMm6Pm8fxaOvTac2fhkFc1ybEyCONKXrBlWVobbYHQ_6TsaCsL4WaNgWZPyrmeKsk5ATYVBbtMjaUtHGFIgJYrTCxiXgSWvqQGrCft-exYywA5Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba8ed1d05.mp4?token=d64GRWkKEEkyrKt3fesyWPzPkFPiQUr4I4-tB1q0J78-3ha965ctR7zMaDXZqVg2pFwZHrNZAzK7-Z19lWmuAHzobg6oTqGFCyab0XAEl3wF5CYnT8c_lIwaCtAKoLi9xub_pWYH2rl7WGswjo5xZr0HkcOG2kPJTe-JHOorz4dTFLbPf7MLr8rva59FXO3WEGV-68k62_4CPszUhnf2et19lvx-ZxgA2_YsnedCweiW3AkZOm2B7Jsno4l3iOiHh56ESRSLK9BN17rXUPHmLhph1L3jh2uKFLwlPcNr32K5l_6v71KXwCR4IylaO7Il5dc9qPItkQbmwXsXJM7VsH8OAxmvSIEEPgS7TQ8ZZ7LljvgQBWVooz22goxjS5gIORWV6wHeSv-qxS1mU_Yin5-BK2Gh16f-HK9_IyT8q12AxCwSr1BwA3_KUH0UVKFLYbwwU1bbs9Q_7Rw6s5ZY1gQNIDDNoiM1AzRDKSWyWzdieEX1DeZC9ebfG4mPcVSOhR136dc0_Nyf9dks2WUDTOKndzMgntyZIKGS__somSQTbiOMuAVMeQWdcRiYMm6Pm8fxaOvTac2fhkFc1ybEyCONKXrBlWVobbYHQ_6TsaCsL4WaNgWZPyrmeKsk5ATYVBbtMjaUtHGFIgJYrTCxiXgSWvqQGrCft-exYywA5Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
پیمان حدادی مدیرعامل پرسپولیس:در این دو ماه گذشته تیم مدیریتی تمام تلاش خود را انجام داد.
🔻
نمی دانم چه نوع بازی کردن بود که بازیکنان تیم انجام دادند. کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی ها مشکل داشتند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134379" target="_blank">📅 23:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
میثاقی: تارتار گفت در تورنمنت 3 جانبه بازی نمی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134378" target="_blank">📅 23:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فوووووووووووری : اوسمار برکنار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134377" target="_blank">📅 23:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
پرسپولیس با اوسمار:
🔴
اولین باخت تاریخ به چادرملو و گل‌گهر
❗️
باخت به فجرسپاسی پس از ۱۵ سال
🔴
باخت به خیبر خرم‌آباد در تهران
🔴
باخت به ملوان پس از ۱۰ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134376" target="_blank">📅 23:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
چادر ملو گل دوم و زد ...و خداحافظ آقای اوسمار .....خدا نگهدار .....لیاقت رفتن به سطح دو آسیا رو هم نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134375" target="_blank">📅 23:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
این پیراهن بزرگ پرسپولیس از تنتون دربیارید که برای خیلی هاتون گشاده ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134374" target="_blank">📅 23:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867470f8d2.mp4?token=r9q5bC2AkwpySiQwXk_mKvQa0nPQ8xLHfxAHCmD9dfeYD-P_uRTYgdLhcyYB5pVz2kmIE63Wrg9JdmYhItgaapecTsCDH-Zuqgo1eMZFjOIAEj9HFu-pidzXZeZ3rQkTfMR_hj1tFd_4sklJCCtqvKn26c4K7ImdYiXoSdqZFhswfSYKDkRP845q1VRtVO-lMfZ1Ys7GI29I4he4YCQSo_yE6-8PHI36aCqtFDuvcVwM8wAQWp9rLvUrM_T4HpYgGtJwndBocajWvo92UM_ZNmtSwm2-1VjYTW-YKsiGnO4S1uJ054aNOI4FAv-KEO1Q6GEBt1Srby2fsh83eYhjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867470f8d2.mp4?token=r9q5bC2AkwpySiQwXk_mKvQa0nPQ8xLHfxAHCmD9dfeYD-P_uRTYgdLhcyYB5pVz2kmIE63Wrg9JdmYhItgaapecTsCDH-Zuqgo1eMZFjOIAEj9HFu-pidzXZeZ3rQkTfMR_hj1tFd_4sklJCCtqvKn26c4K7ImdYiXoSdqZFhswfSYKDkRP845q1VRtVO-lMfZ1Ys7GI29I4he4YCQSo_yE6-8PHI36aCqtFDuvcVwM8wAQWp9rLvUrM_T4HpYgGtJwndBocajWvo92UM_ZNmtSwm2-1VjYTW-YKsiGnO4S1uJ054aNOI4FAv-KEO1Q6GEBt1Srby2fsh83eYhjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
لحظه رد شدن پنالتی پرسپولیس توسط بنیادی فر !
🔴
این کجاش خطای قبل هند پنالتی بود ؟؟؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134373" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134372">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134372" target="_blank">📅 23:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134371">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134371" target="_blank">📅 23:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
لعنت به این تیم .لعنت به این بازی .لعنت به کل کادر و بازیکن ..تیمی برد که پنج ماهه هیچ تمرینی نداشته و با دو هفته تمرین حذف شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134370" target="_blank">📅 23:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134369">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
چادر ملو گل دوم و زد ...و خداحافظ آقای اوسمار .....خدا نگهدار .....لیاقت رفتن به سطح دو آسیا رو هم نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134369" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134368">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
احتمالا ضربات پنالتی و نشون میده شبکه سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134368" target="_blank">📅 23:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
دو دقیقه تا پایان بازی و ضربات پنالتی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134367" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
موعود حرومی رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134366" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
ظاهرا برای پرسپولیس پنالتی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134365" target="_blank">📅 23:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
از بس بازی تعطیل و خواب آور بود وقت اضافه دوم و شبکه سه نشون نداد ...احتمالا می‌ره پنالتی و حذف پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134364" target="_blank">📅 23:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
این تیم حتی تیمی که پنج ماه تمرین نکرده رو نمیتونه ببره ....به نظر میاد .اوسمار و باید ازش تشکر کنیم و ی بدرقه خوب ازش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134363" target="_blank">📅 23:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
این تیم حتی تیمی که پنج ماه تمرین نکرده رو نمیتونه ببره ....به نظر میاد .اوسمار و باید ازش تشکر کنیم و ی بدرقه خوب ازش کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134362" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
این همه اصرار واسه برگزاری این تورنمنت واسه چی بود؟این چه تیمیه آقای اوسمار .چادر ملو چهارماه هیچ تمرینی نداشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134361" target="_blank">📅 22:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134360">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134360" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134359">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
❗️
بازی همون یک بر یک تمام شد ...کسی نمیدونه می‌ره وقت اضافه یا می‌ره پنالتی ....خود شبکه سه هم از دو قاب خسته شد ....معلوم نیست ادامه بازی و کجا نشون میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134359" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
شکاری و خدابنده لو میان داخل ..سرلک و بیفوما اومدن بیرون ...بازی و باید تو نود دقیقه تموم کنیم .وگرنه ضربات پنالتی همیشه بد بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134358" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
🔴
تیمی که پنج ماهه تمرین نکرده به ما گل زد و بازی مساوی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134357" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
