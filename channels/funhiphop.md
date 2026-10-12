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
<img src="https://cdn4.telesco.pe/file/fBAmYd-I9BNuZ9ku8kjiNhbLvFZ2r_ThimJMHr8g3NbUTl7vT17zxg5CyNMYDQyxf81HTjSS40djUGe9e9b1hkuQDMpOn0Q4Lt8Dja7EnnICgmTe-IGD-vDZf0peSc_cwDkInqfe9tHuNOeT0rrc4pYlsOeOFX_hfh51iBhWynbUL9luppdI73osm6LmyZzKAs2GAjE6kpkJIMqU0S6Behe1dK0wTLswlQ3V6RXstg2ytYGB23n2MH9kW637K2sXAvf8R-bKWDcGQSpK5fqIpJmcNEgLQ0Z-hCotm8YsyvDixfbkFt80PnhdJj9XKADSpTzLa4XJ05Iu9nYsyQn0zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 268K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUvbrH2bpp22UR4bdfrKGYN9nIpy_wnhTe71zO17u91oBcdIdApXWCs9H7yP20JyMPhsCatxk3Qfze6YItXp98V9--Muy7Xq5YeDEISTpGajmDnw_mRzetJ2B3DGW8F8X5s7DiP27RSj9rpIymj9Uzq7-m6MTsTNHwagrfCTgJdoR6g9-T49D143IU0ZSdGJUiBSgdafPZjxIU8kCuZjo_1QgoBTWRo0EzlOj6Td4eFmJudmKwbHrel9mC_tVGKezQyukZxVRi77Dzj2vaG_5XZRsYumnxiR--DwmsC2X7fjBcdw9nfstgbYEw0rYkkjsxLBm-YsXwGSCMp4XKMaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/funhiphop/84716" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXBzhBMZeTTYfhsvLcLvpIKiMTOtNG5pfVCs4DamKb8zMaRi6V7coXFn_ZTYr0hp1y7twAXFgUx4hkSuLjNmxHr3b2QLzBHm1rAIYVE8wtDzAwX_ekGRLDLwvRyKowNUaTg_VnKENN4IQpaztft8tRE55uBaRKWEbj-oNawdDyqxIU97LiaevfJtOlj0cjYxjFWsR1EQRKOnjdEdumHisUzzRfJXZfhw7LegMGZe84iRPgc6p05kb5_IuqrRvf9KPqfiqiCa7IyA_EZJ3OK6n4fnCtuhk3QyJxf3XKfSCp6E_HyVZ3H1tSNXWH6dSKpkp_Qa_oFkmjBvaCbnEroiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBs0P6QchLxX-yL8sbRYCIRfg2v39NI1uynfrzxtL-5tW1TIh85WjmiCFjVh1U0odLGRTWVD5Ovyl4Eou2ZTCdHZBWOaikbh7DhsWvwJmCqh35M6hWyMUBIC0npeuvU1GQ2qN6KnoSZHV3bUTTv5Ah_NF1aalB3yiIw6ryAYV6rRJsh-YWC1SabLeseVJOuLfc4lyF8LOEQHRlchbzwstNbG9FweN7VikE0hLXxiifL0RqPMDnsLtuXEUUZFgTG75pvlL9F2dyqLkm1snxDYJHj987XewsdmUOZKpaluCoTKhr8-PTZ7bbjW6pohKv4i0wg58HOMs6xzyHhiwuWy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNg07j-SV424XMO2xnrX0tGVkKUgR0U9DZ2m0XLEIQ8yzaD-n2CpJ5RRYIljx3_4tm3NtLMqgjXTwxyio4YaBuKhX0q_8lsJdKEjBAY7Fvow70m7ALrwpzG68VhslutL0MJs1wSClt2iWOvvzdO_j7Tw0_w6NhsZ2XtFPm07iGF68yUrpHtb6MNnox4cfYznUTs9q73oARA44V-k0MFs8s0LpCNMC4Wwm3NLP4ckqSbcdewvFlxlSa0YrkbedwQuYbrOVCa4skt14VU2j_gc9vYXkZlnOE8xNi6zYub5bGGApDOYKyxhUJ7oHuSYNRHqMUmkRr7w0YzdE-2-w-DzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=of8OKQhQUP4STS4-E62APz9NZzjLMFGOUaPF-wMdKvc1B63AO5TYUvPjNzZPT1ORyOJ3p7ce3c7SO9bXhXw415Mpivw4-HrPPxnvutqx8t5Hn-R_gkc7ucTxnDBSpb9KGDuxSFdnhUKX2Rj2xscXi1WgGy1mwgggfm54nHu-XpKBXk13SRwGzfw5jm5DpCtE9bOrWUGx5uTtFgLr2vU-W_l0Ctx29VUaDMrahcxI3Co0lY6wEg14LBofI-0-jVDO_S76rNKA7UbsZvRgC0gysMqBdFqUcFKmZIfZ4aPtcJ4QDalbh0LD6LvQY0nWtpWB5thD_itl3JXtmRSb45CChJZXFqLwXWXKYuWUB0C8k1zf7LKsrjQjBoXTunkdWpYVJtezK7p-dMFPLnZT2cpdGb2g6ilrsPvvA7qJ5se8YtRmm2VU2DfrO3GYWruoQLxSkJvpiAU2zR6Tkhpot58zTQUlhm0AO8JpajZT9hoeHk8sWeMel8Z-_mpSPwwZVX3CKYTa87E0sTtMH_jZSFP6XNKnwiM7Ab7-yFXXUSmVje6ABt8XoEZHti4L0SNt0ZYxYdjQA2bb9Sk6l9PEDHXebUWaY8WsOmW7YGm4Vp4FsHYRp1swYN1J7IahdEKRXFK01n7G9fRNfhJJSUjNzuIXN7PjoNBZ1PNYYsJmDkeLC8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=of8OKQhQUP4STS4-E62APz9NZzjLMFGOUaPF-wMdKvc1B63AO5TYUvPjNzZPT1ORyOJ3p7ce3c7SO9bXhXw415Mpivw4-HrPPxnvutqx8t5Hn-R_gkc7ucTxnDBSpb9KGDuxSFdnhUKX2Rj2xscXi1WgGy1mwgggfm54nHu-XpKBXk13SRwGzfw5jm5DpCtE9bOrWUGx5uTtFgLr2vU-W_l0Ctx29VUaDMrahcxI3Co0lY6wEg14LBofI-0-jVDO_S76rNKA7UbsZvRgC0gysMqBdFqUcFKmZIfZ4aPtcJ4QDalbh0LD6LvQY0nWtpWB5thD_itl3JXtmRSb45CChJZXFqLwXWXKYuWUB0C8k1zf7LKsrjQjBoXTunkdWpYVJtezK7p-dMFPLnZT2cpdGb2g6ilrsPvvA7qJ5se8YtRmm2VU2DfrO3GYWruoQLxSkJvpiAU2zR6Tkhpot58zTQUlhm0AO8JpajZT9hoeHk8sWeMel8Z-_mpSPwwZVX3CKYTa87E0sTtMH_jZSFP6XNKnwiM7Ab7-yFXXUSmVje6ABt8XoEZHti4L0SNt0ZYxYdjQA2bb9Sk6l9PEDHXebUWaY8WsOmW7YGm4Vp4FsHYRp1swYN1J7IahdEKRXFK01n7G9fRNfhJJSUjNzuIXN7PjoNBZ1PNYYsJmDkeLC8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84703" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmGffRPiTIbK32aWcNr1Ddsx2SHGf2sy82cEaC5DMOvb0iwgUspT6mxjaocQlwrTDZLoKY7YcrmP98P0UhOxNKYr5Pj_-pCh92gQUx0Iqw0Jo7hrh_EFOY-8mr2n4J97XvSvqNFiwzOsBGGLqLPW0vaO9GLi8dGD_WLGVxLzG-yD9MEJOG4aM-1FDUP_uH3z8Q557YQxu-rhDUKfp1bFiOZk5-HRd35HEg8h4p6Z1vk53wRztJXE3ykAa8rl1duwvjYFx4k4tgCbYJ-ykkpbLIL-zNGH3hSG90aS395FHFwZUfGGRVFNXG8aIcyRHgq6--1TeQsVBYxTf5ht8u19AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL7YXPi74JAG1zMrIkgg5zLWSRHw_560dq1KkGX7fbCBRE5X5mzi-4ro6cKwebtaDx7CLWvxYs3g_MDlK55u21IgIx8TEIq3B0kXQ0IqohHo4FrJSK0_s7bwaozyD8zKUvAJjdLeVkRiL4S0mFOXIlYBRp3uLRr6LLmU4IFjFclxmlHBz1VostTR501BYPsaeuH5UudF4XoARpX30n9fO-x_1AgGPbUiL7czYyIjlQKxXzpzXdcywT3aXRNDho5u0OC3ZAZ290migKZwSycoCWloZ013_Ronyirba3tmJ9yjSUbBROoJTEN9GrgF8RJMSRJ3XZKAAULk8A7YTF3T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdOJk-ZFX6wqvv24ufwgC7DSY4-IFiLF_BOdgcinOs9AQ4nOZbLppti4CNTNOwBrRTXJsmHUJzxnr_fw-U3qG6RrGsUQG3hgFP-jajH2KI6Hi_tWL40_6KgNAC4d8i7T_CzvXuhcSuInTIrK6tqW0-vblrPlpWa2OPj__LtPuTLlANKeWVHF_XkYHe0M1YnZtKzE7rw_US5xb_QfnZiXuKj3iKkuvpUy13hKh3dZNNQauuaTcuREnZbtyB1RRmpmzHZ-nSPgkJR-p64_IjPk_mTe39F7_P5PEwPgl0cwkipvFA-uJ-NgQu8orFZKjvGAfTRDkGwp-atvftj4viz7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TyKi8e8UNBxn2irITQ8qIR8PbNk8dnPdMoKqfMcqNwk7dU0e3XktaDqebIn72zW5yR7Ytr7qU6GL6-eut3GTOEvKcJ4mW13dDdnyJ86VFS6rqteGZFt-kVqDRB5xkH0CWsVtaoq1ywQreAXevaBkvfcrwsBBoysDha96f9_lt_oAI3GAedwlBHg-FLMw6UNpQF_wwbTmDMytmiq4Lr6GO7h5xM176c-DGVQgwOyjxJe15eUaMPINf0Xk3h7Ngp_gMM6NGRwym72hM3MBUwyVznyTH_MDmNDtXx6KZH_5VDtHI-4L26vqOQa16xC3f8C6y56_U2vniYoaP8Wk2WUD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRvVFJiOxBDM0ayAFgPTL0_0AY6Ndk6_dW6VYqIFnjvdRKqMUE_4CO2rj_DzBwe775q2LiAmAQBYeDsBoPNjtVD0_tRmZL9TjaROcni8NrKAmDcwVgIWXSCnMGAcqpBStfRS009-qFDbyYtpzYG154uZID2YHElBSmb6GQHHvncgqhmGrXmvCHIyGrFpd2MFB-YtA88lR5-Cnl7fTBDgBCDHUkhDISoDOudocMsnpLLyXyc1P3TJGriPRj8xyQ-bv_hcf597EE1qrFj9SN9eEaHy8wMoJVUU8HB6K98j6AlgcQGv0oqqBmuPHwXqD5jlGDyBYSIFTpuxmdfpDEum_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyzh6NaUdRrwRYCWwuHVWGbbNWrPQZMDaXzMObiJRakzd8pTGqUTAqotLYaOx3bH4JT-lcxsrhUdcNd0oqK8mr8z-Tom3dpsB8WYFffc4Q9v5t5e7k2VL-SAjBRYtRP72O44JYITYXjeVhNfYJ_kIzJvaoKYq_i7q4wUn4YDJteg2XHu9Xr1ocHAAI-5qaKj8ZNtRyuNsrcm6FN_Y0QiF1qYL6Q8-XuEDu1RVokDXwiqRwxEx0wcGTgpwJvQ8WPnAbq0ZF10cMF0ZUxc8F72XzPRecncj12xO4JotGcGfDm0dh45e6ZRVewGWQgIMtH-UiiKxLahKbYHApYK31KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=bAd7OxmF0SNLhXRYeOh_t_Y9h82TXzYe48qcrx4kBDAsouUXI6HTiwlP6S5LJThgvdzWCh9iKBApIg0wzBjSkm8phjQE5GFi0-nIkUyN9Mpur_F4jllPBm15Frwa7f1DMXM23txibZqqEZ_zOodxdr7LWml3-AzUpjcMakabAvVCXg5CLcld6ZVIvWmQNsXTFsTFt-3SJTkrDXomup4pFzzbOmfvog0uDv_yBGBU2B8OpYeAh_rpGdbfGiLal9gYgdQZ7MBAESL1Gepx0VR-lJvfp5YgTxDPEx1hoD6XttLOTf-fRtgaxSgQIXAz4ouGXvGljBg7kMivHVX_ayyJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt6foqQwaTnE7IuSAeeQsW-dCKZAtCrLLphzsZa4VnLLLi65-mteQywFUS1scHkdXNZUK_S-h9Hy5Td2mKRwa_ZJ1i4l8VmnF1dPOf5o7ko0hM67lby3rpTzSLGRhSbCLLoEUUcIdPhy1FeGwAn7_KBeVwfnO2YN6m6Lq0EGz6xQzi4-7y6SpO3NEmzIU_1tfj6T3lMa8QuuZLTvvjyHK0d0M4FRZf3rIgvXLrgU9QzEsUid51blMcfidyikyT5CvhZdFnMiI1hOxVjkoJ9KOxM5WHryfctkVc-a-3fE0fgwUzJLkIl29bvQT6cMfaEbPu-4hk1bm9xI9JfKRvAojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh7n5u7gfDKWoySFaz9CdcwE0Td383AEwjPnton0d7EkzxWgdHYVrAiz_rvumIxWhlDNt95kNAahoJWKDH7GoYsZyWYAIUIgohNHKBIoGPWIfAeMEDe1TchZPzYNLQsk_TIeX5_yX0UZQYrqzhVISZAaoEd_a3Tyu8JoxZ3cQooT8uft6Olu3k-zaChU3UMFfXJN9QF4Lo1W8sWj3N-mzyxw11DmLPpNv1JikcF_PHh3PHVDCBnajmap_iQ65hXWUoN5GCKkYpM5D2xL9JbVojmU1wSJyrVo9n7hIL1Bbs5J7lv5OsOE1grokbwmYAk-4IMPX7zbrWATH8Y4NI8JbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi2LLhk46PIKCFtH2ZN1fWo8yl-Sn72q0TOt2bynEflwgcrN4vYHgxXoqk5ZJVkHEsqmlbn8wpgty8letjXHpj_E6BjaeBi2_djD_nDcS1ftkfu-vgg76HcpddTnmwYp43le-CgTpKnHCNP05-L8HhkDNcHzAPHfUq8HtvCquj5GtTR9rgF9v3Y-8r2gbr0fBAMbRZ_VRzJpod_B4dXot_LVaGYAlPgkEOPOOBilHuCzDDzCXgoiIMrcbFHKHjWNROglhQseOtTPB8w-VB8Iu-Y_bGy_HLhaKHlbmtnNhHWMB9XFcnlgIjcGC3SqAtwzacNW67i47Yn-Rymsv7RsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxflcAxAXWXMkM6-aXquWxc5e-tViRy-63Z-9R_EH4d72xIXpt_ln9jtCUIv8cm07LSmxkj5lupAzZlC9BE7OpN3SnwZkLu4BSTyskbFRT9VCVp9hHdfRtbFuwpH4U5QhpRIgqtM6otdMm8qenNWdJLh3tDTyjybqGFziA6sQx1SatUIZifRT8mcUrVz7F2U89dp5Yt9owp04rFrytI7pATkw8qQbvrUnbwCnm_0n4cGvXyHlekmEnPOXktHUiIS67Qyfy47E4U0CyAsnjyJOkGXsGcayGeKTuoQx96MJneM5DN7IcVt0d-Fhsh567b9QCI2HU2REn2lJRA2zaDXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=PvRDoiC_nqmYZwRxIcRbvVQ5IeXI4pvfvrw1cTmJOT-pWJ4Ti6uEQwMrBuIQsXtYPXKCxRYd6Dy1ipfyaFZTWI5fuVv2IJTMXBwuR1t7toCtptXOzG6UKo9Hw0hl-pGKNbl-xSFJQjlIDzDcc9SCiXXEl7G9W-0PpTJzbjSQz6ZAZsHJt_MDnyyLfNTdeAgrb4WJN0aY88I8gAs9JOQA7qrV7aimH_pKWYUk30pMyB9oaDSDeCrFjnf2peazmG2BgqB7A9R7IUvjG9NcFSNAlean4VhBv0LPKtCvfFo82rkZzUP2KbzAjenDfCz_SQ4Os26VaXJKz4UcsM6P-rh4yacxjLjLQ8QIjU75SelOLhot_oOTCkjhNpJ4EU4k2cv4lC2_4g8Ox7k9lve28MrjNKtdy5sncJEINKHZDv0Bs1XYzBJYp9SwjUwil-wrOUayJPRajJmUTEIWk3DQGeUUwbMeWKhTLcEMmYApkObk0k9sql_wlBICEDFq6uTD_QhFyGOTyYPd_yFNAuzWmqMZB1mEIEQuFcw3yx-4jfGCN6zKCIUd_6tTazUtOP7IEGAt-9nFuvzJrUFMR4YOuPmJiDBkqkiF_xxPyinALVVqGql-xg2RtkT9ZRc1MTYqo5GoY1-G4c74fooLGImrGOr9HtbGsKAhaO01un_f_ozUXK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=PvRDoiC_nqmYZwRxIcRbvVQ5IeXI4pvfvrw1cTmJOT-pWJ4Ti6uEQwMrBuIQsXtYPXKCxRYd6Dy1ipfyaFZTWI5fuVv2IJTMXBwuR1t7toCtptXOzG6UKo9Hw0hl-pGKNbl-xSFJQjlIDzDcc9SCiXXEl7G9W-0PpTJzbjSQz6ZAZsHJt_MDnyyLfNTdeAgrb4WJN0aY88I8gAs9JOQA7qrV7aimH_pKWYUk30pMyB9oaDSDeCrFjnf2peazmG2BgqB7A9R7IUvjG9NcFSNAlean4VhBv0LPKtCvfFo82rkZzUP2KbzAjenDfCz_SQ4Os26VaXJKz4UcsM6P-rh4yacxjLjLQ8QIjU75SelOLhot_oOTCkjhNpJ4EU4k2cv4lC2_4g8Ox7k9lve28MrjNKtdy5sncJEINKHZDv0Bs1XYzBJYp9SwjUwil-wrOUayJPRajJmUTEIWk3DQGeUUwbMeWKhTLcEMmYApkObk0k9sql_wlBICEDFq6uTD_QhFyGOTyYPd_yFNAuzWmqMZB1mEIEQuFcw3yx-4jfGCN6zKCIUd_6tTazUtOP7IEGAt-9nFuvzJrUFMR4YOuPmJiDBkqkiF_xxPyinALVVqGql-xg2RtkT9ZRc1MTYqo5GoY1-G4c74fooLGImrGOr9HtbGsKAhaO01un_f_ozUXK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QD2s46-Z8M1tDeoZn6BiBvQYHWdHB3mFH4OXiUXTsDjo2UVEhDCiQQjyuBKPj4uKdN6a77TN4pVnIB6QMiOnWk8DJf4zfbOmoet7tJIKIfegx50pUzjMqxcJ8LOdTiunbJ_E3bsrest6KNE5nbDV-jVFrccJs6G0dNq3b8o49hfllkfh6YzdFYdId8XZ5NQX8ByMLxF0b_3U2ZFHfUBAJ3dEH21jNEkWilhhCpM6THDT0ILjVlbUu51OeGhnzLnGEKRxZx72sB-hUtqCXlihimNKuBkJ3A4h3gJKHo2Pj7KIXeHy6eSyx6ln0MgdcCK1rpdpO7lathTbIrPP0QvfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsktRjfvxnIHk_5ahbQxYYegt3V2MB-JltIj-w4ZguWx_goM1zU7CD6GiSj9odCBMkW4pOKFONO2Y-CcKNI8sVTlAmJEGRu7fbWFTv-LKmny6uc85KW2UNt0QfSvlgdSeuqyca7fBmyxU8yw8I2Q-HMJKN3VpjO0oKGpVKdKNY6uQy1f1netdefA0jOfLTzcCL8wS-6ATGbB_I-ULKEPU9F9IMYorfisVKVR1tL_tnSduFPh_CQqjL9hVGRZnNr1wzMA92jFGtNW0zXT15_caSBBw6TZc76C95r8LKcy67cP4GBTWJMvDfFvNlAzALiqMtZkVs_ASxIGUTDxFdxM8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2NkMCzIta_OPNqmRYlmgkYnXEA5qSGgJiWG6d4kBjGMz7TFTdvbFUnwtY0mIu_0zHsW2sOpNsowScvX-OE8NCru8Yjxhsb_BN9_TA6EI2NZKPxjkQn8A_aa353-uMzahqSeogRe7xRsYtHW8Xj3Ryr-PhCoYGUXgbWGwt5mHgqwE_rbwRLOoBaY6p4lWJ_2aRgci7jA8WBwNMVozajw7MtVtAHFO8qB9rLfTDlrbgeTHrrQO4yegijkFOLaC_Cu7NKwC0QzuU15BJtXBXNbfAGp9pR9TSaMtF_8xIvaY7AZmxcIs0qCBygPNp5vhYIM-nbz7mF-X55nvo35MkR0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmTtpuBjGHHEnLEwVGoBt1myEsry_b5KeQeLqadZDkrIp-cOT3eQpYbb2aPWivkZApuLZZVe_9mBeSDHLunj9_FDBf-JAnexinskEQDqVIkBbw-ToW00qVk__BAvRt0IQvGTBvlwNRuZKABxUL6drsZTRRsbc6l9oKzrxNV0RPx_kLMkZlQtWK3V4aHsa99-Ohia_xm8Rx5TnwCkVmjpv_yD3qt35nVAsOCHp2rJChzG4AsA5ycukQyDYhAelWFeqC4Iwcui3z-yAIwrkn2Ijgot_0YeqcPTb-KkH_p2GhCygc-jtONTalQO-CpAPvEBizADBNMVU5eW7idPB-p81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuZfBeNHT_92s7NLIzhYkadIQqc0ARyq06N3XHTpSbz6PSA1NLIn87cdlLi-Er_G9FtHJe73q_s24qr4atqbitoxCcFVMsO5sYatHpcIy4k06BdjY3GLyxY1bpVQmWQdy_VdGWWeuITzuVI9aVBOdI8ZwfEg1zFn_zxf0rJjADHtByKh_jCuXftIrvHiYZd_mxEqiUuq01sLJNNt1d-phVhMLVR_mmyThY0MDIaKwNGSjXTk56NEidTpCCMwqjZcK3Fi2fs2ZaBOQJwidmyp1qEEv9pkPi6hhCKpaMxuSgYZZQPvb2gGwEC4sGmUh_7PzY_J_xi-OIds1-YLsCPQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WviH6XvRQbCJCoaIHI0r9Y4TlKvNqnTBAN_zgRGZ_QAaMD79jGXfpXdnb8jmeE7xtYRia_1T-t4tca8GOF3BXQY3xkFX5PqoKYb6zXr1aSWVHIapPyZvD_M1u36TcJsnq4XDF7Sfa4hJbYYvxz2sKMKrWX0frR5deqZKP3JCjtzByQG-nvas3Zkdsro-hZDbRoNK5KFlZbd1ybwMB8pyUk9HObQbiT9-dnW2csfgeUt11cURqw65el1rhcRfHUeeoBv6P5btibvrAbmUU6Qk-xQ5Qh98fQ50zBKHx5jw11akee3WU9gNd5pCasRdz6tBZVVNZKdcBLZqr5kvH-xAdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=KYtjxjaUfpZ8lTUbFfGjCkAV3_KqnvW9UkphQ-BPDU3PGK5aE18xagcFlnDCYNi5rCti0xaZAJLjr7yKIaGzS_cqSnuHVklV9EflvHtJbWVXXTjeJBf3Ru6EOPBHQFt4xa_rS1jPnnuh6aRp4Pwn6LOlAC1_bhZD2r9pnW3obGA5jiPDo02hqecASLgrMN0wP3PnAPQtfvrh_mUMayXcvKquOTB-NxK_PdQ5BX-LDHmoJfXasr4MwXi1kwM7fwcdzpXqB0wzy9QqWEj2Yz2PCGdwWtlGib25TY1AHLySQcHAJ3Evd3MGJCs5-3Ynp9qGu3D7r1TTQvBdM-mcGFy7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=KYtjxjaUfpZ8lTUbFfGjCkAV3_KqnvW9UkphQ-BPDU3PGK5aE18xagcFlnDCYNi5rCti0xaZAJLjr7yKIaGzS_cqSnuHVklV9EflvHtJbWVXXTjeJBf3Ru6EOPBHQFt4xa_rS1jPnnuh6aRp4Pwn6LOlAC1_bhZD2r9pnW3obGA5jiPDo02hqecASLgrMN0wP3PnAPQtfvrh_mUMayXcvKquOTB-NxK_PdQ5BX-LDHmoJfXasr4MwXi1kwM7fwcdzpXqB0wzy9QqWEj2Yz2PCGdwWtlGib25TY1AHLySQcHAJ3Evd3MGJCs5-3Ynp9qGu3D7r1TTQvBdM-mcGFy7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxyZkPz1dkzm3NqcnF-t4RyGXeUDej-7KNpDCm4GuYjjV_NcB8vAB9AbWFop6Kb9fH4pkkR5gVld8RTr8gWo1lns9uO43rn1Uxjv9XY51uL1aVsimkAnCk5vnmqFYrdjkbRgLy6Xk7ruBsZ7Cl4jtsrzlJmhI86GwnPhqE-F42jKpqKB0jY6UTHJAolwoon7sXFehpEkgyAWujI1wBVsz-Er9JVc0FUWn54p_nwpxVNTM7u4w3aq9JZsx-9bADgt7lLL9pdpUHKrsNw6QkbiOiFflEknq4lnojGz56m4CZg9F2spzX2AP0Ge08bjsB3usDDXknUiqaQ3jdkZnJSpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clnPzevm3AUfCtnXAMuG0HcQEzhynQAGQWHNLDuYMOI4d1-upWA94NzP84F90wMqJyQatF7sUSrtcUQkA1DpRMDnYRr-GU9ylR5AaFKxxnzOYp7QA8CCWYrKrlhEN_Shmq2OFtUriCZZuasABUr3JBtUFMMoZU4HX0Pe1xKlSeWlVRqPjvb4RRFOx5aTYrmYECv2YmvWK1WRpOSlh7Vvwq9JbGcGemNfJBB0Ooe43EZ4fPNeaK7uhivMmd2FrqRhgPv8XbkRIfUl6tkYSlNmtghjk3daquxmKyxWSSYB9Jb4zLxrCrRx2ayCt6wyzJSoqy8SXIcYrkGai3y7ysT1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=o7d-SZqCi5rVOZ_nqpnT_v8nnsVRwBHH---VCOkVP8G65noowBQfdiphgZkRcM5W_PSNqzZzRen_3tGVDiGlrpWb_njBjL_vWPyO8yhT5jLEqi7kyippjI6RoyUzE9g_bkQnp30s7gXDmEZXJwntEoERIhUBk8B9eOnGrEdUiqomLvKLpXYMejzHpSiKZcff66pZe9x8tVPhcZGUg0BngU96OLvwgaba_dBZzshJoiMjihIpMu9IR6jJsmQ7axaAthHHkwVK7lAy7fSCO_vey6BHTQf3THEvvdL5R_tACx2xWIXtWY1Rf9dMuUjBKnzdtfP_ZEyyM4KHfRIju3my3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=o7d-SZqCi5rVOZ_nqpnT_v8nnsVRwBHH---VCOkVP8G65noowBQfdiphgZkRcM5W_PSNqzZzRen_3tGVDiGlrpWb_njBjL_vWPyO8yhT5jLEqi7kyippjI6RoyUzE9g_bkQnp30s7gXDmEZXJwntEoERIhUBk8B9eOnGrEdUiqomLvKLpXYMejzHpSiKZcff66pZe9x8tVPhcZGUg0BngU96OLvwgaba_dBZzshJoiMjihIpMu9IR6jJsmQ7axaAthHHkwVK7lAy7fSCO_vey6BHTQf3THEvvdL5R_tACx2xWIXtWY1Rf9dMuUjBKnzdtfP_ZEyyM4KHfRIju3my3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrsfPOx-RVtLc0IgMkQIur448--fRllGbXwtMlAPVg_m3iU6bNk5GWroRfK68Vax7qEX4EhESqqqe2WM3GPo4AoKiv4yUFQb0Y9jazhHCXcBmHPOq4NPSHEhrXq7DasIO1imIpp8tki5Mgsda6uj2jTonbLUOWsID9I7TVK8HxPzcfnUs7z0OxHjAnL5N_as2UUA2kpUqUgY52527eekuemlEmMduCH7xOGx3ni-G8O9uY9s_2lrW9oNox4OI2kr1b3rgIo5nJXfF4q3wrnqD5CJAblJzFzuZwpYS9qa7eAqYJHHv5qHv9awFL8bIkTqkPOifGZj8CsFmnporio8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOVLvHAWYqkxf8fVvBqeqqPdEuGVijeor41-ZXWrTvEHiRZME_HOVzPpVHv-KhXzps2dyHcYj6DfuPxLZreO6nhj8tWhU4acG3QnPIEy9COQ8IPzYocBoUBh6R_kzh9El-fIcLy6yMY11Qfu9nuY9vofIfx6uEv-P1CrkwQ-pAeUYP3KgwTfVRz4LwK5YhXqrdMAfo2duCjEHWp-qAhtbdcapLOxIs6S6C0fG--pwkaZ5l0E399CKC9CPZQwLD0hd5fZjwD5RPj6s2ToG_bW8RcOW1Rx5Vt5W8LlYtGU_EHTquxuN7yPatnu0kba-7FjMsB-8AC1QEkJ7HvavW73og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=MgNL6KiqPzNJ62wPybNrpNcHvkis_45LSJh_z6L15TrvNdHVWQB69zrjEs4Fve4Bmc8aegXbUTcZcXZbLQUF7UZXLR7bHpiT0IgymZzMRjJUSLQ-bCyI6l5klZY4G_4utbDJgCB90YWoF7jo_vSW9syF2bqn-XAHNWlHHmTe2hI0Qj_o_PyEHvSW061L3ngJGXq7Betqo-mcPUQDZrmdSWMjXniBz2ZL03xQPz40U7b_PMiuJ-0TAcRm6TRQoXUW8cX1zEZDhmAkzyzyphPmSoayrM7yv8_YO_5p-aR7tcshgr6OqGEuO4F3gYItBA85IonfyqrYlAPptGHwQigAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=MgNL6KiqPzNJ62wPybNrpNcHvkis_45LSJh_z6L15TrvNdHVWQB69zrjEs4Fve4Bmc8aegXbUTcZcXZbLQUF7UZXLR7bHpiT0IgymZzMRjJUSLQ-bCyI6l5klZY4G_4utbDJgCB90YWoF7jo_vSW9syF2bqn-XAHNWlHHmTe2hI0Qj_o_PyEHvSW061L3ngJGXq7Betqo-mcPUQDZrmdSWMjXniBz2ZL03xQPz40U7b_PMiuJ-0TAcRm6TRQoXUW8cX1zEZDhmAkzyzyphPmSoayrM7yv8_YO_5p-aR7tcshgr6OqGEuO4F3gYItBA85IonfyqrYlAPptGHwQigAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czXdeB7DjAtlWr8o3i_3wQ1YVnrvcUlQvW_XybNQa5mKMj4ZCoBzPLCqRrSHgX-Rz4M_XjbCE5Mw6Sjz_pbtIg-ZrakTVNteygAmjyw0sKFdzEdnPJjq5vD6bSNolQQnQAArBDHEAKQMNbRlYTup_x73C-cc-fH0UTEPlwYzUv3xvNQ302tqmr0m8vRBgNNOtbFo7obHAGX6xBgf0hT-YKggBQqmf43DKckpTPp-u3O6vI-lEj2H36z_IBfrrf22pyaDo2bqRukqsZtnHqxkuHjJCfomLZgLm8soJsQpDAdHNbaucH4_I5TB9ottMa4l6dJeFF_21F3t_0Tm3h3jSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9z1NTINuZWljKqIwEEcF9ZLtUb_OP80KBd_GVmPLTvFxLPlMe2OLFd08KUWDEq2SRxIJVLkoMfaKtdIiib4OsDnJIBepCh9OqCgLG-QMmoj9PBaJ-izYvKy9RKRt5pB7vjm7De2hSGrisF4WWH3sMeZFGtcraVoLU7FX4mbHmbtML1TRomBtYerRpgTYnpczpUjcQPAyLiRJGEUF3t8LSvPkXVzk8tpTM_RrUH0k_tRfeivOciCsGBrMRuoWQOIYPNmO4Qp_Q9GuIbcIWMp-hDYjGh88eVTD4xjunyHFibuBul-bKbPosELCI1Ls0P_h1a3TzJh2ldHO3cWdBAXlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFN34yDJ1CRT5NIeeHN55LM1Tr0lZ_iSzKmlG6zCHoY0oHgRhRbBYzVe8wVUkeGtDwNoUl895KcrPa_beuUngiO2Oyrx4e5Fb4t57r9kyhWCcK-xOIV3JplBqn0EwW7R5iJa4sBlWm9EHZdbA-N1w7zX3bIG3L1_dwnuSRpS_VmAjaztoMn6v7LKNBRlN7BQsrBBVzN2Ls-2_k9Di0JRHv2TpHuSEHn96whu7KHWWlNpOAgJ4sonyMICDAYzQiDxipCT_dZttFcQ_vF6MCs4wzPGulxp6698_vNCbR1i0Vk5puPtphBwPX4eSwFo5ocdbMe3h8Oz-RpkV7-BQ_ievQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GP2vnFOv3qNtPU0sBv8AKE8Wn8XxMDRdoNf4acAqWy0bFUknNnDXhTtd_YDmkqKKyJAVJaoVUn8Z9h5V3R6Qw-BjJVb9kOgJqYqele6KkkK9i9Bkrigjqqzk4tU0nkwlWbZgVdAKlLtLt50Sz7kjiHVO21KDTRrBLwPnEbKpZ_bULgEfzn9hbiAzL7Mp7iX785f8qfMLidmH5N1fH9eExd38jfV_jDAA1eAKYlZ2EMGC8czcP7bYX31M9xSVKu-9pkKW2ZWOHq3Ae5vr7GmaPoDmCewrEvIQ_zY1COvoV8i9lURQ_xWBPJAGg2swfotDsiLo-a5J6bED0-lmL_LLMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKxZ2bC2KEBoEK7C9mYfMiATP2DvuCNzHTZsKHdq2JTZzVipb4QkdDHv4Kbbh6I0l-mQlop-vspsQGD6oi_VlEK8LpVzu1cBon18p8Xzuk4TMgzFMWD15Ar8FFIQz37zZmg2rMe1r8ykpyMk1s_O3w2mgn-DmhQtR6CWiZOG4ObNwmo-UfP6Z-G9GFCyxIZubplbZB6nn_WtkGytDK7YtdUL6kDT6N8kY7qC1-UNFT12KGwHWKHgjPepXxT-PsfsiXuF0wn4Wl7AbVHMyTjChhpTcIJOkHZLeFDQCGTmYncRdZsFp1_fcrwEDG1WCBDnk4Sq_cO_2kuyJpbNV-dg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-D_QZfjERIESGdbWyhYarxIbsW3AtQR9XMDwYPWL4K1CtDYjvsa6RUueoP38iRhW_EFsbFqb3n8mcDhbTi4oV3CDv45nC0oifUITb-5oQrErpCa2LQDhkmaKQ2ays5bNrdX0x1u6ghfDmgj2mcNXsxYUONdmJYwNUqdQNCYmLy_0xykqMsdiBZfiYu86hb96RivfQQlAkPF7RshLBT0wJ9O3dC32VYYwQzCWVIL_V6Pug7-R5Rcw6UTrKZt3WWNBLcOm6YJW5fbCW2EAqLS27CfuABSYwJefAISs5BKiB8gi9zK69X4jN_UveDl3wkekY63YcZ77rt_a3doIlKG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=Zi1yc3kOHvSifKu4kFnTdzKvXR-KOL5xNJxmfTB86HrQ4T0_RsPVF9K6OI6bvqmyGfE4wG0eN_anMhxvsrpyxaoQekN3K-D97HcNVJCgic6AGI9Mvs7EUtWhxA2JQLR4G4rnlc_Crq0EGjEiYYDE9O34iW-5lZchwzaEm-zk33-RufG1m8FJI8-LXebaHK8Xbj6f6vZTON7HGSDmDG2a2fZfOb11_ssL_gg0lWxOjGd2zIU6Z9H8rx3ZK2F983AQ62Mrq64DwbyQIcenvhsEQCz7HxEdWgsuvq1l1n4603BqnsBPwMmRikepdLUFaH6QrGxgc4rdadcVepHEzZRlxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=Zi1yc3kOHvSifKu4kFnTdzKvXR-KOL5xNJxmfTB86HrQ4T0_RsPVF9K6OI6bvqmyGfE4wG0eN_anMhxvsrpyxaoQekN3K-D97HcNVJCgic6AGI9Mvs7EUtWhxA2JQLR4G4rnlc_Crq0EGjEiYYDE9O34iW-5lZchwzaEm-zk33-RufG1m8FJI8-LXebaHK8Xbj6f6vZTON7HGSDmDG2a2fZfOb11_ssL_gg0lWxOjGd2zIU6Z9H8rx3ZK2F983AQ62Mrq64DwbyQIcenvhsEQCz7HxEdWgsuvq1l1n4603BqnsBPwMmRikepdLUFaH6QrGxgc4rdadcVepHEzZRlxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=DO1StJ6UGoxFpwWXunQ9-ssICKv5VxjEU5RwM4Z9U1ZT85R4Z7gy3IDCJJNjwtTSg1NxCMWt-shYKjSXTk6AY_5I03VoT9beZj7gUrpKY26D2nxEHghavc6mK8SzruHDBhIvjInaILlxTIN9EZkDAd9NKCoxY6GbZrUKw8YjGe-M5pPFJf0Fxn6XxfQwWvUI1mFJiX2YkznC85sJKNDdDrZ3fT741Vonvrz_4wRjrLAIA385gDX3UWZPxyVWvFigfi0qjZqktCSAjL3PKlNwaPFH9YNCo4KS31LSvAJuR7bLELu-5MPNqXn42-lBfPnA79wdgp55tetw1F4TXTvpoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=DO1StJ6UGoxFpwWXunQ9-ssICKv5VxjEU5RwM4Z9U1ZT85R4Z7gy3IDCJJNjwtTSg1NxCMWt-shYKjSXTk6AY_5I03VoT9beZj7gUrpKY26D2nxEHghavc6mK8SzruHDBhIvjInaILlxTIN9EZkDAd9NKCoxY6GbZrUKw8YjGe-M5pPFJf0Fxn6XxfQwWvUI1mFJiX2YkznC85sJKNDdDrZ3fT741Vonvrz_4wRjrLAIA385gDX3UWZPxyVWvFigfi0qjZqktCSAjL3PKlNwaPFH9YNCo4KS31LSvAJuR7bLELu-5MPNqXn42-lBfPnA79wdgp55tetw1F4TXTvpoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbV2_VaBO_YIQmobIYnTKw8u0ZeLpSSHmQaI59bFAW6np-ujPm_GQDfioq3LuL_36UNV66UdrNwlKdVyVueoNkREVawt3pF94VkUVm2sPLO6jRrzqK1qiKGzXGDEcUmJr_WB24MpSWTr2laF8N08DA8lGAXcXYBYOb3-3FgtbExX2jZLeJ84wnclxAEeyoFirca03kmWeLjg0732GNW3OCOytfrU2y4Q4jskJyiug9LqYTDwpS7gmdczInRAZOETe_ds5hrmjzR1rR3JVVvhRy-oIIH93ELYMwe1_mz6ba4bMDuy04PH8uhodQWD3XoKVWwbqVeckyAvPa9jVOsnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNZ18sW-juvneBvIL4T2FTb-0GVA96bYOGZwAlBf-y2FRKr7qOGDuAeIdru3RWQMCc84rqBgJ09oKJP0IaQLQADSHvPyxYYusQmIlfEzUSykJbuCO1gBbyiUem0oEUqDgM3x4jWb6pG0ErrLw908PSEUFpfQ6jeJ-bCoIh2C5bxyK3lB1Pde1LR-lVW4y3ZV6gEw0WnlEpwwg6AHl58QaZjq-_7diSmC5-SJONQXz9kuPnpBI30CyozFiwDMHnIHSb9MbTtTt5wGvCVgUU146GZaG0wq4C2zuyGoIBMgKDjER8zrLiPV37g7A6vs5XJgrxZGKpLZyUDNRMYvgsiAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a8YeDKckTWdEuH0dWbhyJt6oqA713yMyI7kOQ07abdPP_pI_DMSXwIUNc3v_dEZ4CDG19tA9NkcS07Ev3pTTu1HmXP21dVfsHO-hSaqGzbuqoNBG5M-Ousc8b5DD8QexSWZfxJL3McWAzmap_M7GQ0UZfJDqblUPlxt8Vny6c1-v_QZcTwOPTXK--sTV4nHYiis31SZiGATM-SWvmnVSeJKMpYt_ziAB1tURwYnzGHSKqhLLxmzV6qWvYobHZw7mAhNUeY7kYWcaobPiMtG6rDwaZ_mbMFOxLXLkMzGXNDYABUe5MMtTyL9P2BsOsBI9H8DtG-BpGivHEb215g5oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MmpN7HTqq9TbchmNljBilh1OYqEZoBkFBDzw7X5UNyMZWARW0kIrgXMvf0i8VCbKI0UwtbCVtKxniMPuwCQBffF5KLw4tbYGS0dKfgxYlPjgfyjf4X8rk4856fg2-RaAyJdLfZMlgFMN2RmozDMgmnkVTQjNyPNF66WRtXf99-JgEkh5VWMeMqy9Wz_ecM0ratDzWnBKg2uHK6FI_8Ngc8wSiNs7BwjC3HmDZDNSEdH3RU_FfqR5BWIjhglPNffJ3hadXsG8gHayYcCHTA60sWz8dsZU4rbzuKlRwML80thLrsBaslNIgzY2wDmyAsVn_pBVqQUYkGgEC0qk1Q7jUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WYnFdM33pUv86eIeRRTRv3wYLkX7ZKErr6ha2kETUEYhkvoiiiR_jPUU7Dv15G98YtHRLTzaJq2MpiiZWbQ8p5w4fhZ0PGewUZ_MQEGmXUJZv50PaHLa3XOa_3qmut3zKtynq5Gv9v_YYOAU1ooTneTZNXPNDCWIDOvfGvu-GA3atE5wMKZ4VIwKiH6ZviyP7L6TccefNNtPLC17DF3_ovcGlIdhNjqYUbXuDis_77kaMjOdLAHGjqbQqUEWimiqW7U5Nyg1YRjKZT41uDJCry1rNlXiJjIJ90ixL3iLSn37inYmkDHIgAxUDzDYBJaUPdrJD_s-o7J53bTIdKHljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OHa3ukwwLFq1tMjrGUc3B5wBavq70Dc0Ag-GgaC5tfYvCleKXMyJPasXQoIxTiCj93eqlJzEQl1OAekeChaZfwHRoym72efVmzhT5-AByMyb_4RqUFbxjnO8PrqUBp9ZAXEp2a56jBMVaR2SwDvARuJv9lUFdhiuIESF7XqrIqgw0EdYM4kPyCK5bQhqf478jndsyXr2NCVVXHuwSNm34rxFf4rEXyrTIxqD8HXyYBAFSNWquhklL6reQaZXcW0vkLhstxE75YnkNzi--5Voc25eyhUwOtLukU1NZEwAl5V1u8WTWGekAtaPG31-CzY79XuZMC1pT_FuDBWINCOGRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfxKFQPlVjV8GtQ7jjq2DLzGh8YwrR0K-JPPwqG7KkdFpgulaVNsZx15HNUOWbkfYYDQ4Nwh1DVUlxUkBCxXgbyCCZ0xWC2LVAtUyf283jO7uRO_PDS9Z3B3GvK58Ho0qduKtvJTi4YhhZpNikvYeNxZNqPxc2JhUDU_TQ821n1s0ookp-8OD9G6-9stkNBQ1Alx0XQml_wlDMhNTT5vJ0_jhVFo31xiOmUDzxeUQ2SMEEE4KktEoxJc7f28YQFCmmJ6F_n8spTVK72976omfcjlUJV44N0pYaWMRVnL95zyMH0GgRmbuLNsbMAm1y9VWWHVvXjsLMaIRNSWiV3zpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyjhDjrwemSUNEDlFphOkcGnt8yZ243reEAQYesc-7YdilBSb74ZauaNkp3PospIbLFqI1n0XzIgzkf_3_JCie4y30y-dkqA558tnJSn6ZTkPc5VDr9VTuqEcwz4BOKrdwym9o41pC5OHoFWGnx5h-8DVnzVdF5KjWP-Mkjl-O6mokqBZCI7azwyREnvX1S7b7zJD73_VSAKqIPHuteKiY2zyQkRSCfeP0ao8HiLWV9v01-G3y2R4A3dqqF0nBpxDgHo_TShrO0clShqecl0BaK4uMYJmtOsb8wgsMB1qAP7SEIdd_W6veTWqt3ZPyYedI8JCGZAnfEqPhaJdDPhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUCjaKtXOMSgnPBmmf86mMjmB3VUravPF72SWq0ZbPTeg4x9SxnxUfDV5RGhcT_2mtnw8WxOOwi4mhJsj_8bCRZdjGX1mGuTBkAtrGu_AqR9h3yy3kWWIA6A_1BTP8VJJGiRC6nWKOKfaUcAEIUPDvzKDh00-QP_Rd9mgPnpBzmXpf8kH6bOSZu55Y73kex0v2_KgkllIC3_oYZgKGiIlYMAvtnlaK4XJIvPtbVZodWUFtr8rX6utmhL0dYK2n3rdPVITpfkWmblNYFcqVlSkEh2ilgXCMJbCdJeHxfZ3nE44-8sq6GPyRNsK6TrHtPrCyu0L41YZxs8mo65C5Kt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2F1qMGwWIiz0fpR1UaKuR2Sfs1iG7G6bxzB-4Te8_mxpscopWySU-SsaqdTwLKitsqBRQ0MtrmcA5vnNg7It0Rw3ZTWkP3cYPwwL5rHxm8nfLlMj65F3CW-8-wVqoYqaiz0IpabCFQti0huk_Pke2c4jkIwCBpo4z-ItfYw3NIwcuj60wnwsOCCNihuH9V6cZ8h31_l-q3Hli9qAEQGxHDQA4WI6lCbXZcfKAidgp6AP5SBeHTBhn5PB7FVsV4qUamMJA4y49sup2pJmphKrEKmLycYDUrl95HrZOaKOoniMwfBmjADnN5K-LQPyUwuX8F_E_7OcH1xx8_YduGesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGr_YcW8TpI6yLlLzvZM1a_ombF68uk0dT4c4X6laN182s90GG_1BWhKcZzy9ZwuPyuW3RaL4H7bDgxgMKiQd1t72J_M8MKqqj_LOi4Z16DWgC7YHnuQfWdAqJxw0aU-kmlbPvZ6mHy9JZlR8sotPXwnqIxo6B3QsOhxaQGEPD4XPu1R6zjp9P3-2UO1uk3wXzgwQrWVYLG9Y8QgXraPRMSVGm4SfUyYTgetrWeCJFocW0UFRO577i9AqedsfVUjeQueHRuadQftwNUg6uLn-dQJXCquCFfbr_pXt6ITgKMWcACqfIDYI9mGnAp4ACUxo9ojMqa51H-_F51wt7PUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyO-yzvyufR_feyw_EN9TdZUvZ3tN8KzxlPwxZg4d-MxAjJ9Uy9u5v6nZ66U5WaMNd2Jjp0Xc23qBvmX3jvhrgIjeEwaJQpOwRecfKLEpjf_yqkU_0YdjkWlKr5R2pkeTkxBoiJEAz0Hkt1Xr843DUIbG96hZCVr18tIeOz5c86LqQqF0EBhRBIP0ZhD72pHMXUeaJPQvROPg24Z-N2SbNzTpeWC5UfZIkHbuDfacirRToVO-djj94xFIqmlgC_0_YXeANM-WF8mQQanX0kTIib8CQ3RQxaVhbgzIOC9Q_WomRyguSXyTXvW4oxWvTCmk0xNDe882FikvhQXoTHYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET72CdVMyDoNZmej1Iax_uITHr5GaJpFyFJc-7CBhC4OCFN62ma1P2OUHwDXJnAfBs9AIbQkMpkTKRni6IXUQjBlYKZYgSv5cvKV8dvKPXucDoLAoi7kdxpZEMzDxD4vLv02ZwspVqaTXxOrEiCXazBzLzgqablkbZ0z0SvnoZZUcFjlclcLb5gjZOzk2p3VRlKXsfT7ymwWEc7AaX77nnVLmqhAECZ8NrgWVcKQN0HAGReOO5kgeagylGdkH-ZtO_bYHfsEYJeAs-QUBjn26K2DBuf-i4VT12Gh5B2jrNe3w18mAY-C6GRC9UHyjNL39hSRvBZ43h6sEYg5G9GQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXiqwfIHfSG12VSgLOvsuGDFL0xVmupsYbILQqR7GsBI2ESnAdhJQQ4MWr3bvLMiDUuZqpyctTjt3Tc1i04iT2ohuVSpzn5QT795BTE4WS86DZKVyVcTHZwmupHRA-epe2UHoZEkmLEXRJRvp78wS4wxDyRfNFmrUxQPVUUrt4obRUwVzhC5qA03p6maTmxxaVFITX9ScniTRuARZT7C3gCFpI-Mmz3ZSagqRMSV9qyVNZl9mac3v2g4dtE_oXGr_wO3J6jqNDbPe_pm2SD9pn-M7Mi9grqQ279FVjuKes6blSadcntLfjPRofJB8TJZmYheDxuUs5hS9kOMOKs14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSilrVQflAJYkOPGAQ-dkxH1g510fRweXyHL9MMoUCgyBMC7GHP8GuWVsV3w7s-Y1_riz39fKYMeNjFN7OUfbGrZ-rpJVfz5frnrP1nGhdDtS4ALE1NnCuS7PQxY7laClru7qPUWFHWkBKts4geqn67SPGaBeO24F7tPn1EDV10FYLBp7DD0LX0N_Q0-GhtWVxDNzZWTjMFvrQZLz4A8u3mdGmp1NhNG071ycKEOtMaiHTEXud8l-i_PxwjeHis3J6V3E8rvsc4qvyzliR-JSsafn72MhoeJZjKXhiYw0t8ELVRYebZ8EjZUATLAI70IRHVIRxPkAt1iB7UQQ8MovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQGQf4t-LqD4vd9PcCXLJ1z7pvr1cRYZazeg90yLrrfkTTib7OGJ3jBdxipfTfWT7sTjfIA3i9WjZqHS4D1utSClnUxyCBNRwUwnn2l1gKxE9tToyEbNZCNfdGD16UiRa0pgE5sAo31_Nq8qWseMxEFfA3_R_8EN_aQF4JmoTJ8wpvJQyDyaY47H2a9gyLW_lOs8pdJxpeGP3rWhf5m0FwBCbOkK8sNqmLqA0pfMYdVolE0wq9nW6lF5uj29Nzp2eAVpYB8PeMZwO8tunzEBrzBjk00C2D_vbNOY2vBomYCM5L_KOQP-VpQhhGJkT8LUOJTwunwD0VX3L7KpD-VStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=l8PCxTRszAzCGETwHqBW2K3GJGKwLPUlfu_NTfkLwMVWCK8N2y6ZpuJI1l7SftH09cGZyayNoVEJ3fmi8ldecCvtqqE6IW4TlDb54txI2SHS8iQZ_i6C3RBkZhpz9-j_8wdPCDFKvOlQIKoKmMQL5gFOnnCVZ8W9ijrr-T7GVFCUzOEcL2BZ8akoU2R3agFXbaqXkld53MTFe6tXlUWdAjml49-1IRBGiI3JSFsKczazfGmbvVXnG-7lhmpIAQylpftIJUnKt5R6ScLRnZDchlbT34BsyD2DdvjfciHPvLagZerx-G8EJTX1-nU7txB8lq7S6ONzeOD5ZheAYINyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=l8PCxTRszAzCGETwHqBW2K3GJGKwLPUlfu_NTfkLwMVWCK8N2y6ZpuJI1l7SftH09cGZyayNoVEJ3fmi8ldecCvtqqE6IW4TlDb54txI2SHS8iQZ_i6C3RBkZhpz9-j_8wdPCDFKvOlQIKoKmMQL5gFOnnCVZ8W9ijrr-T7GVFCUzOEcL2BZ8akoU2R3agFXbaqXkld53MTFe6tXlUWdAjml49-1IRBGiI3JSFsKczazfGmbvVXnG-7lhmpIAQylpftIJUnKt5R6ScLRnZDchlbT34BsyD2DdvjfciHPvLagZerx-G8EJTX1-nU7txB8lq7S6ONzeOD5ZheAYINyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxOyRB9kZeAD7U3K_uijSe5lrIRkOv5N-oxuewrTmDocEOhYUea15PQchR-OAeA9wBeGe_NadTqaOD1k1EiSY8AHIvvI0rMzQw-9-FmrLRGQ8ioRexH0_HtqFOt0bzpi3GDL8BiLgDSuJqoBQqsRsMe_Mrm_Incpcs7mBCKMPGxx7mhln1pTY6ExDN3O4sSgsm42njhOPXu-8shddmNrJ0DPEXJmrBbPMiRlRCfQfP8Kk4-HZuiyniOakFBgteFlremGPMPMqS9Rl_gfZp9UpaKChaWfqzVDsBn0Q8e0caNWWABqOgMQkOTZrnrQ2sU-WK4g-M0d8_BJmp7zatkGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=fZ4n3bJvmVYvlRZqmUr1EFIBGfkhMoSypWUV9gaF_Uz0FpCl71JLnMUbyXbSPjgbEsK5GLecWHzsXm-iCJzGBfnhGFmPk_a5rXBVoTXGm_N0dsDUPEYsoIIxtyHwCMl5x9XT8Bi7-WQJGgcbaANjVQ6lRSSy0l5_DfxBvTW7TzaOmkwwbf8Wyj9VGdJQo8m-jLWybkSdYp-osan56m0WZE6oUwkVIfsXEXDlMyQYjhdT-WNOvXlYj8hruKGDOkwuRSAeiycc8sLtLq_Jw4Y5t1oxEDlEgjXp7xHmuGVxGBohxRJfTuBvtKYHpmPoJtU21GYpJi6hfM4xHTaP8n-EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=fZ4n3bJvmVYvlRZqmUr1EFIBGfkhMoSypWUV9gaF_Uz0FpCl71JLnMUbyXbSPjgbEsK5GLecWHzsXm-iCJzGBfnhGFmPk_a5rXBVoTXGm_N0dsDUPEYsoIIxtyHwCMl5x9XT8Bi7-WQJGgcbaANjVQ6lRSSy0l5_DfxBvTW7TzaOmkwwbf8Wyj9VGdJQo8m-jLWybkSdYp-osan56m0WZE6oUwkVIfsXEXDlMyQYjhdT-WNOvXlYj8hruKGDOkwuRSAeiycc8sLtLq_Jw4Y5t1oxEDlEgjXp7xHmuGVxGBohxRJfTuBvtKYHpmPoJtU21GYpJi6hfM4xHTaP8n-EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=akVB2M22k9L4WQPp8LFIEl3vT2fuXLQosvQTyKzZlcygPjWU8yv4ZI22-oE-8w0Bsx3yslQWVI88nVslpasuhoUOojDI6NoXQhsXJ59qlXnMHqVFQSDovs0WOHxZ6XAG9g0xwVkchxg2FxUvF72Lee5tM70jObGyQz4QZyqsqFVdtjdtxRsLRqwkzrmWOatG4nhB_FqMBteITEK8tUPrPdw2CT2WaKFey3k2V3IG7mC3X_-CoGldCwGN2Mk5sHVj92QRNRDQM0g0B78_VxRP7OYL38oIm5tOMZM31lLOfXVBR6t0Ms5BJz4A-p5YeG-O_q6pYeUZ5sQgCfAY9FE-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=akVB2M22k9L4WQPp8LFIEl3vT2fuXLQosvQTyKzZlcygPjWU8yv4ZI22-oE-8w0Bsx3yslQWVI88nVslpasuhoUOojDI6NoXQhsXJ59qlXnMHqVFQSDovs0WOHxZ6XAG9g0xwVkchxg2FxUvF72Lee5tM70jObGyQz4QZyqsqFVdtjdtxRsLRqwkzrmWOatG4nhB_FqMBteITEK8tUPrPdw2CT2WaKFey3k2V3IG7mC3X_-CoGldCwGN2Mk5sHVj92QRNRDQM0g0B78_VxRP7OYL38oIm5tOMZM31lLOfXVBR6t0Ms5BJz4A-p5YeG-O_q6pYeUZ5sQgCfAY9FE-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=LANrUgwEHHT6l3YiEiX6XJZawyu__AI1-ywB8SdYt-rYgxQFIDw1KZ560wlnaCE_q2Tg6j9rnUBtpRTiKv34VL2FbZnealwxBJoqglEYbuO1tT6igHeryaejapF-GW3QgsV6j6ZfULsuk8o_M_uQFXZhudocI5FHOtAXkRzw8anNa7FiKYwjBqg3gEggcvnBw4o1aeBaGobsqGYqb9G2i4GPhwfVDXYJVyPPUJqtM-DcHgDradztkpjaTjjCe6XvPmO1K0hjCfam7IBFpWc5CsH6u6-bh8AEDkLgubB9oPD3RkgLK29jrKNY4lmzGymrDnBcOXJPgxTMB00NcNg_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=LANrUgwEHHT6l3YiEiX6XJZawyu__AI1-ywB8SdYt-rYgxQFIDw1KZ560wlnaCE_q2Tg6j9rnUBtpRTiKv34VL2FbZnealwxBJoqglEYbuO1tT6igHeryaejapF-GW3QgsV6j6ZfULsuk8o_M_uQFXZhudocI5FHOtAXkRzw8anNa7FiKYwjBqg3gEggcvnBw4o1aeBaGobsqGYqb9G2i4GPhwfVDXYJVyPPUJqtM-DcHgDradztkpjaTjjCe6XvPmO1K0hjCfam7IBFpWc5CsH6u6-bh8AEDkLgubB9oPD3RkgLK29jrKNY4lmzGymrDnBcOXJPgxTMB00NcNg_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=q7YookonQYxOaqkYQe3AYLXJrO5T4_OIC8LG65e41ob8VQlX60Iy_ceMQhYS8C4QFsr9GBgtx6x8-wzY-qrKFGnr52mD5h0U_EdnCggSyb8GJso55l8bTtH0S2Kkpyq46tcyqJi_VVwLGPo6WNhNSs2BV166PFpBz5sdkItruqtmzbJFUTyJ9ccJAubcjXB6KHvZtelI4UWeBKlhLCHPr2NZWi3RHICuk314Tw-2phH-IQWKiEActxgeOqcIvKu1sGeixbEylTH1_p2OTelriCi-LriKqtaiJMJpQLAwPtCdADYCFR9xe9G00KPlomKZnRAGwk0UZejSra7tkvzV7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=q7YookonQYxOaqkYQe3AYLXJrO5T4_OIC8LG65e41ob8VQlX60Iy_ceMQhYS8C4QFsr9GBgtx6x8-wzY-qrKFGnr52mD5h0U_EdnCggSyb8GJso55l8bTtH0S2Kkpyq46tcyqJi_VVwLGPo6WNhNSs2BV166PFpBz5sdkItruqtmzbJFUTyJ9ccJAubcjXB6KHvZtelI4UWeBKlhLCHPr2NZWi3RHICuk314Tw-2phH-IQWKiEActxgeOqcIvKu1sGeixbEylTH1_p2OTelriCi-LriKqtaiJMJpQLAwPtCdADYCFR9xe9G00KPlomKZnRAGwk0UZejSra7tkvzV7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5IF6cfBVR73q6deP6GuZr7cubIquVfd3XorkkaTZ_7Re1HwRCb1Ejhlhj3_-44zcQzEGDcs1b7wEFncUACI_FQqgYGZaVtQjaDxD59EDyzQ2UiNGlkxwfTWz4br0QOyz8zxd8K9gjjWTErffRXaXi4hVnsoVf2xXgX61GhgbhxtLi9G9yBwOkVYhH-SxlOEn3sxUrrZzJAseTbtFrpFipheIHEjRDLGDgYkqHbsC81bWlQYba7yHc_7_ESBghRLKQGCS-KIs7owzOuqv8MaZGMhJv07cvgwyfVFVTU_PcjlLDM44LzmakvEy6fUb-wW5waHzeKMvvDP04qyQok4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udRCIezYIRtthTvU4KA7BQH0sYKboZboi-oqMwQXR1sZ9anL9a2BqhqLXHGl3pHZVeoxqwDbwY2tLCrcIU1dHbx-526mMybSodlyLOWSh5NDL5aE3QVZgqy94pDy6R7keKn-D93iEuFsq73zmFCikJvMUcVEcRBZ6DE-sb7ceGUkqjNjIUprhj3rOsWZy1KtmTFQbW1JGGXZh4ZtFK5oU2tt-Alos9CtRrYKAJZr7mkURrKVB-tQ_AFAgWU1kC07_XE43o5GvsYyheHDA9Hw1zk6Xoz46YjrsUCC2nj4yOISQotsBVR46W7RBzptVK2PWY1JfifpUEe69a-UgAf96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
