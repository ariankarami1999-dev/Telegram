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
<img src="https://cdn4.telesco.pe/file/JKgikmVwZj_ooOa_vGgHKZPqgerJri3mvV_uW79Ynyxu-LQ8UCU-Fx8vc6PktmO4UWPN1L05YWGBf3jXd-LuuIIFmiiGcq30sg6PkpOjBstc5z4msYrSQNuzzNkiawTlfApv3FGTOVNy8Z4vRLfaPJtYJL7X8tb8sIzye9fEHIJoECtfM0VZ46k9IJOZMcYNZp-RWdpnOZUPq_XBq_90X142rKrjDhD-QMVF-eq5jC71OfM8zSPJKUxJ9kEP9k7CtCSd2OlP3w9Bb7G4enNi2oU6Q-Nkne2t0oa0HJFnBM5WWF71EhOQ8-6DXwRpQjspUGbgVj9A9u4VpsewakrPYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-693517">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
پزشکیان: استخاره روز بازگشایی مدارس خیلی خوب آمد   واکنش رئیس‌جمهور به حواشی پیرامون استخاره روز بازگشایی مدارس:
🔹
هنگامی که قرآن را باز کردم آیه «وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ  وَاصْبِرُوا  إِنَّ اللَّهَ…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/693517" target="_blank">📅 21:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693516">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
فایننشال‌تایمز:
🔹
اختلال در تردد نفتکش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به روزانه ۱.۲ میلیون دلار رسانده و قیمت نفتکش‌های دست‌دوم را از نو بیشتر کرده است.
🔹
نفتکش‌های قدیمی هفته گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
🔹
دلیل: زمان‌بر بودن ساخت کشتی جدید و تمایل مالکان به نگه‌داشتن نفتکش‌ها برای کسب کرایۀ بیشتر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/693516" target="_blank">📅 21:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693515">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17b5f0f74.mp4?token=SDShwsLMd4cofVZwVlx8tsDHt-ly-V3mZxbw8ITVHXzSusFEGIXjyANHFW_6IMX8_VVx1A97Px7gYX8DvbxsRsJr8Trxiy7GIh0pPBL2WDv_bAC5eoueIp0LtCoTKA-dV5zvEmTi6va3IFI-Sk4FilOxI0-PnN_Wn-uHSc4E6buyaW2SRFQFcVLgRNi5oYHtc6VJE43b56PjPeRCQ_209YLd10i1sZ_GT3wP9yhTSGYW2dEWqmAVHv5lPUHN2MPL6wubkN1mjXRYSmNbkPv9IEXrrp7UR4x1VEvzrnDyo6mdV8BpfFTzvjdYA92GofnjWciInDGW5M2tx4LuiP4yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17b5f0f74.mp4?token=SDShwsLMd4cofVZwVlx8tsDHt-ly-V3mZxbw8ITVHXzSusFEGIXjyANHFW_6IMX8_VVx1A97Px7gYX8DvbxsRsJr8Trxiy7GIh0pPBL2WDv_bAC5eoueIp0LtCoTKA-dV5zvEmTi6va3IFI-Sk4FilOxI0-PnN_Wn-uHSc4E6buyaW2SRFQFcVLgRNi5oYHtc6VJE43b56PjPeRCQ_209YLd10i1sZ_GT3wP9yhTSGYW2dEWqmAVHv5lPUHN2MPL6wubkN1mjXRYSmNbkPv9IEXrrp7UR4x1VEvzrnDyo6mdV8BpfFTzvjdYA92GofnjWciInDGW5M2tx4LuiP4yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی سوسک تصمیم می‌گیره تبدیل یک بدلکار هالیوودی بشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/693515" target="_blank">📅 21:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/693514" target="_blank">📅 21:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569e289c22.mp4?token=JXaZC5JUAuSOAJTYOd3ed1hFXSyLZs1n_Haf3COnzLmN50GTFq2tsteyniFcnHIdINrwu2hxgUHYgUuxO7MWW8xjzy53e_m4DiE7uhluSeewnvlXeRY4wWe-eRBjZaMzlo0eRhfTZDhp2s56MrfE6Jllg2PHr-IRv015GQMp0okLNNSbqVf3QRdUsmhJnHTcDngeuLq0fQDOPYTgn5rt5IT9tZUWf1pabHrbWgq5VnDnJekhUc0OLKfAy7YPuhUJfJdm8XVYA0nSZWFjdTNq6hzC_ztLmZDWa_juNqhm4MzC_o13V7-UrKhQ7gSQkYN5cIQHuMFx2nN5HXCrRP8EM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569e289c22.mp4?token=JXaZC5JUAuSOAJTYOd3ed1hFXSyLZs1n_Haf3COnzLmN50GTFq2tsteyniFcnHIdINrwu2hxgUHYgUuxO7MWW8xjzy53e_m4DiE7uhluSeewnvlXeRY4wWe-eRBjZaMzlo0eRhfTZDhp2s56MrfE6Jllg2PHr-IRv015GQMp0okLNNSbqVf3QRdUsmhJnHTcDngeuLq0fQDOPYTgn5rt5IT9tZUWf1pabHrbWgq5VnDnJekhUc0OLKfAy7YPuhUJfJdm8XVYA0nSZWFjdTNq6hzC_ztLmZDWa_juNqhm4MzC_o13V7-UrKhQ7gSQkYN5cIQHuMFx2nN5HXCrRP8EM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس درباره ادعای «جاسوسی روحانی»: اسناد و مدارکی که این ادعا را ثابت کند، ندیده‌ام / عملکرد اقتصادی او را درست نمی‌دانم
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
سیاست‌های جهانگیری چندان درست نبود به جز اطلاعیه شماره یک که در فروردین ماه ۱۳۹۷ در بحث ارز داشتند که اگر پشت اجرای آن سیاست گرفته می‌شد الان شاهد این بلبشو نبودیم.
🔹
عملکرد اقتصادی حسن روحانی درست نبوده اگر چه اعترافات خوبی کرد.
به طور مثال در بحث سیاست ارزی گفتند که اقتصاد دانان به ما گفته‌اند که اگر ارز را ۳هزار تومان کنیم چه اتفاقات بزرگی رخ خواهد داد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/693512" target="_blank">📅 21:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7f8d7b440.mp4?token=RUXmLhrKXfW_FNXvFwJI_VCSLqZhFKy36eH02I5-lSd8QSRrAVbB5DGs5DqhQkFeoYqA7HZP6mzS4fwysGWAkzDqCiFuC2Bfnc5p4EdLhZvHAq0evkk2EA12kE5RaxsZDaLWEcXbCtbvNDyohL9dDAEwunTcQOWwgdMQNZLOlxxbcn2_MH5BOoKySQpJJZKNn0NtAd64qi2Hn-YXk2QV2PQuiAN2c-wu7sYh0SKe7QV2gBK8os8yyb-aPid7AHYBNBKPRBpqrJzAhOjWVZeRusYxliIUmig7s5v0DQnYfBe8Ewqi3R-lq7uhMF5ETPdLC1sIQhgLNa8fVp06T2qSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7f8d7b440.mp4?token=RUXmLhrKXfW_FNXvFwJI_VCSLqZhFKy36eH02I5-lSd8QSRrAVbB5DGs5DqhQkFeoYqA7HZP6mzS4fwysGWAkzDqCiFuC2Bfnc5p4EdLhZvHAq0evkk2EA12kE5RaxsZDaLWEcXbCtbvNDyohL9dDAEwunTcQOWwgdMQNZLOlxxbcn2_MH5BOoKySQpJJZKNn0NtAd64qi2Hn-YXk2QV2PQuiAN2c-wu7sYh0SKe7QV2gBK8os8yyb-aPid7AHYBNBKPRBpqrJzAhOjWVZeRusYxliIUmig7s5v0DQnYfBe8Ewqi3R-lq7uhMF5ETPdLC1sIQhgLNa8fVp06T2qSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آتش‌سوزی در انبار نفت آرامکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/693510" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTrb_-2z0Is4_6yXPgVCurjJamstYCjh8CMUPEVg29nGTaQN3ujUZR5GHrBdNZbc5-2MrEdKsE3SjK2NUMb06plh_bRxTG1XHgayhLINH2TbU0VDFLFKYRFw4c9Agoi1ZPtxx3n5hLrlWppxMBLcZgURSkYZ8IBX6L2F5gi5zFX2QMMN75ye6JBewKi81921J2w3f2Rcj2ycuQUC7RaaJYBr5La5y74E-xi9OhxO87d9xiR6x9Lhx_Pf1zvLIxrHeQD_m-qSAmNdVQg4Y7btePUAwrHoHFN6VcrEzV_6LqY3FELmh4dO4JAV-cNIkixoGooc77jONd6bA59asVL_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادی کلن سورملینا ترکیبی از بادی اسپلش و ادکلن
😍
تازه خیلی هم به صرفه و اقتصادیه
چون هر پک دو عدد اسپری 250 میلی لیتری با رایحه سرد و شیرین داره
✅
😎
قبل از ثبت سفارش هم مشاوره رایگان بهت میدن
شمارت رو بزن تا موجودیش تموم نشده
👇🏻
https://yeklinks.ir/bodytele?utm_source=bhr&utm_medium=foritel
https://yeklinks.ir/bodytele?utm_source=bhr&utm_medium=foritel
پرداخت درب منزل+ارسال رایگان</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/693509" target="_blank">📅 21:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk3YYMG0Lf2I4gCULcOyFycytOfFXD_rdsMFzkbgZ5XMPHTPLPaPmBVMoSN0D-rGZLT6xDwegT9yF1p7PWYIOBvG1fmUv0ZqlCuljIbzlEX7WgWsiKoQOSitwlOXC97zSHb7rYpcC_CcqN7TAMnNZlWBJo6RcbC0Eo56rUzDhirilI--AIRl_VrCV0j9wVCjS95ojE847rQYXPwXUIxrTgitdsLgScpoXX7pQ-oU6VLvShRAXqIrRZTyo6obTGLoKy02RTAt6VExtlxJBBA7pedrWL2jHyeC18smgaRe0onvUskWmKfoEv1TCaSChC3dlXBKQBo3XRsoTHnEMDavyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون، راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه شهریورماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و بررسی شماره‌های قابل ارائه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/693508" target="_blank">📅 21:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693507">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac08963c6.mp4?token=Vk1vbOUs5GVVY_HwaeEK1GUYYMFTiIlceJ2P259DSYA5320Xhkl6GFdg9b5NPKF8BPixsSP7Zg1EqoqXxLnbI4k1_-K-ZubxG3rEFyyUcq2U66qzgAKSZOjHdBN2LuxiduAHSduMr05O0cfa4h1evkqoasK8QHfUHuu14pm9HWr0gJTarqeueuLFl5JaoChuecJGXkLKfSDFM6JICxhxmyVQ5eM9hMiEBGVK4z6S1vJAb5i2YjuLmS9D3gg23aEC4o2meMpW2kHghaD1lPMJkkDtlhxGaSwqbuB7N0QM6B8dpeMhhio-dJWKz1G7_EZ7VSJlEejCkYHzkSQ0via0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac08963c6.mp4?token=Vk1vbOUs5GVVY_HwaeEK1GUYYMFTiIlceJ2P259DSYA5320Xhkl6GFdg9b5NPKF8BPixsSP7Zg1EqoqXxLnbI4k1_-K-ZubxG3rEFyyUcq2U66qzgAKSZOjHdBN2LuxiduAHSduMr05O0cfa4h1evkqoasK8QHfUHuu14pm9HWr0gJTarqeueuLFl5JaoChuecJGXkLKfSDFM6JICxhxmyVQ5eM9hMiEBGVK4z6S1vJAb5i2YjuLmS9D3gg23aEC4o2meMpW2kHghaD1lPMJkkDtlhxGaSwqbuB7N0QM6B8dpeMhhio-dJWKz1G7_EZ7VSJlEejCkYHzkSQ0via0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از طوفانی شدید، نیویورک شاهد «باران عروس‌های دریایی» بود
🪼
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693507" target="_blank">📅 20:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693506">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg1NrmeSqsGC2S54lZaeX5DrsEMBWHNXMS9rSvygYcToBkksaUnStPLiuITcPy-qtkIU6Ql3yDiHLIg--kua3KtZx7XVvNG-RA9D0LgZkT9YJ8HRALa-0iZ8MiUpKbP9UG1N3i5iLwgMOworVixwGkqoLKY918ys_t-C8aG5H_vw-W12hguosHdFKszUw5KLRsKJ52qMUzgeTocylgDvJK_HTpnzmywKoUkvlPl2Upio-J6lop0aFTaV_-LgUnsOx_wsOUS4UoTk4zqOX5bnN8Cbk0E-33tk12DnCGgEAs0_h57YMxK8W6jOcx-QQahnqzWdmUSpKz-jBzyQ3b_mPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهر چشم
🔹
بعد از اظهارات شب گذشته ترامپ، نیروی دریایی سپاه طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک، توانست یک فروند زهپاد پیشرفتهٔ ارتش آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام بیندازند. سپاه پیش از این نیز یک فروند از همین زهپادها را به غنیمت گرفته بود. نیروی دریایی سپاه با قاطعیت اعلام کرد که تنگهٔ هرمز مسدود است و در برابر تحرکات خطرناک و تردد از مسیرهای غیرمجاز در تنگهٔ هرمز، با اقتدار و بی‌وقفه در حال برخورد هستیم.
🔹
هشتصدوهفتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693506" target="_blank">📅 20:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693505">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa6d0f45f.mp4?token=tRwScDMLWOVGuTybXH1kU4i__JV5lxF69pAXGGOc36UsHSlF1oIHg8cHJEGYT81w_pOqhXHYy5Xgvl6qfhwHNXo3Kg2OhUisfic5Wkq4JHxn1SI-EW3j7F_aHU8ZzNogXG3YObcHpwo94H35DuAaLA25cdTmCkupi0j0jRtH4FNybBBxSsrVQjclYWgOKRVV3BJMulx0Ju6yGdceHQSA93cbRLBsLoaO1OQMLlXMSoXQJlXeZdntSAZz8e7Q4f4ldi7JbbX4tcZkW6XEzCZruUjfEzT4ZR8S0VMbSTBeNYchKWc_fApf-YESDFNKui1-UEkyWivX76hKtMEgn77YIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa6d0f45f.mp4?token=tRwScDMLWOVGuTybXH1kU4i__JV5lxF69pAXGGOc36UsHSlF1oIHg8cHJEGYT81w_pOqhXHYy5Xgvl6qfhwHNXo3Kg2OhUisfic5Wkq4JHxn1SI-EW3j7F_aHU8ZzNogXG3YObcHpwo94H35DuAaLA25cdTmCkupi0j0jRtH4FNybBBxSsrVQjclYWgOKRVV3BJMulx0Ju6yGdceHQSA93cbRLBsLoaO1OQMLlXMSoXQJlXeZdntSAZz8e7Q4f4ldi7JbbX4tcZkW6XEzCZruUjfEzT4ZR8S0VMbSTBeNYchKWc_fApf-YESDFNKui1-UEkyWivX76hKtMEgn77YIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیرسطحی REMUS 600 چه ویژگی‌هایی دارد؟
🔹
یک زیرسطحی خودکار پیشرفته و بدون‌سرنشین آمریکایی است که برای مأموریت‌های شناسایی زیرآبی، نقشه‌برداری بستر دریا، کشف و طبقه‌بندی مین، جمع‌آوری داده‌های محیطی و جست‌وجوی اهداف زیرسطحی طراحی شده است.
🔹
این سامانه می‌تواند…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/693505" target="_blank">📅 20:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDh0bmECEWDhsl682S4KxfKCXZgDKNiiLN7LppDmPJzuRwMvThK7lt35t0RC1aNdcDaSdoZpvZEe28B-_6m1xrQsQk8kazLypoXR8vO6R_xOOsAO8WNxg48pvKtltcvUfxS1N18Pjry5FlUOtJkLHECmCjQ7exCK_P4vT6Ayk-jX2r4V6jek6G-W_oqZObuE2_gdnSIgL4JjW03rRht_McjiN04cpYoVvS_tY4KkFO1c4YbUxRcXFpWWGxQaP1jzHMrF800M8WNb8B7Bu-R3P7bw-vtWuDImbwjwfx8SKZPxAQq5fDeeqtumi1BLAx1CjEJvIpfxIv2ZTG8w5d9-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره مذاکرات و امکان توافق ایران و آمریکا / امکان توافق از بین رفت؟/ باید منتظر جنگ باشیم؟
🔹
اختلاف بنیادین دو طرف بر سر تنگه هرمز و ترتیب لغو تحریم‌ها، چشم‌انداز توافق جامع در کوتاه‌مدت را همچنان مبهم نگه داشته است. ترامپ نیز اعلام کرده که امکان بازگشت به تفاهم قبل با ایران وجود ندارد. با این حال، اکنون سوال اینجاست: آیا توافق ایران و آمریکا در آینده نزدیک نامیسر است؟
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3248085</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/693503" target="_blank">📅 20:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTRuTNQnCe5oA7ohgdqdELtx5kLrRV_hQVA-QKPN9H47RuB-NHpO3xxwo5le-eI6bgMtVSh3QzpEcb0s0tii1o5zapTQj6u0AWSE5LNVlHUhW2tQUw4Oy9-rkExawIFC0-sDFCSe42EHEi80qjL8EtpDw4YPU-2MTj2wqSpZJ0CrYHfH6Mts7xDH3pbVHoM-6mTkjb6rWeRHI1qto6VjjpWiXWhZw7IIe7EwVH5A25sJHZ37WQfCD4gOBTHpcSqMv30phaFTghZ4oZvDEwlTQ8rFCXWQJxz8f3I-ao6uiBlvubXY2dG3uQKNAG6_h7cK-w1O_oaKhpLMYrwfvWWsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یا بازار نفت احمق است یا آمریکا دروغ می‌گوید؛ همه ‌می‌دانند اولی درست نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/693502" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073f5f7715.mp4?token=FQ_HoaZujTIcs3_T76bpMH-ghvxKSiRICOLKN4S4150MXJ5KHYbLBOiZWw_f5Fu5MOXZvO-3ghxModTJ_hlWqHF1eNRkIgOxD_suGYPS0vtGcU-hiMUNdFBSo-aAEmFe_4JivRiupSt3hHBJGjI_KFFWRcNuyiQcH-f0mK-bwQsjAOyBaLuuBDmgn8pbgnT42Se9LMoArsVUQ1gnKSZHnNdfOB9CHMsoj7GED_vwukRMkdgaCX5ToT_TqWjCXJmuLOBJ_t2f01psGDR9xkIi5StrpylT4wZpJOrOxejfShP6M9MmJSpr3_YmqXitmwursepTas57rHFKVsz6t-JZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073f5f7715.mp4?token=FQ_HoaZujTIcs3_T76bpMH-ghvxKSiRICOLKN4S4150MXJ5KHYbLBOiZWw_f5Fu5MOXZvO-3ghxModTJ_hlWqHF1eNRkIgOxD_suGYPS0vtGcU-hiMUNdFBSo-aAEmFe_4JivRiupSt3hHBJGjI_KFFWRcNuyiQcH-f0mK-bwQsjAOyBaLuuBDmgn8pbgnT42Se9LMoArsVUQ1gnKSZHnNdfOB9CHMsoj7GED_vwukRMkdgaCX5ToT_TqWjCXJmuLOBJ_t2f01psGDR9xkIi5StrpylT4wZpJOrOxejfShP6M9MmJSpr3_YmqXitmwursepTas57rHFKVsz6t-JZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ترفند تمیزکاری آشپزخونه که قطعا به کارت میاد! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/693501" target="_blank">📅 20:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73786a91c2.mp4?token=s81in4qNV9XoP1gG3eaAyDzfB5ELXCTV1osrvs8mU8S6HimsV4zs46xzUwUV8McDT3xxG6z5XtIaZZ1cY743dS_DC0Jg8XDNFjHmierTVEZWMNVkFk-OczBlSjnBzy1cALQ7wpLqI2TynREEJat6AVCRaC1vYQxH4aN5uQ8qrmws0VLqOu0LhX3YNhsR13Ie1aFpxLuBSyVnq3Iyr282fysNfAE56kyOQ6AplBsCRhbdk2-hRsPriKQNG__PLlYqMQ5NY2T4x9hsmrSo8tqKAH2EkCSFiiM_toN34cj5ZfNz5OZ8e_RC-BSyXDhX_PDZO6O14g5yySV4yRW2tE-4CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73786a91c2.mp4?token=s81in4qNV9XoP1gG3eaAyDzfB5ELXCTV1osrvs8mU8S6HimsV4zs46xzUwUV8McDT3xxG6z5XtIaZZ1cY743dS_DC0Jg8XDNFjHmierTVEZWMNVkFk-OczBlSjnBzy1cALQ7wpLqI2TynREEJat6AVCRaC1vYQxH4aN5uQ8qrmws0VLqOu0LhX3YNhsR13Ie1aFpxLuBSyVnq3Iyr282fysNfAE56kyOQ6AplBsCRhbdk2-hRsPriKQNG__PLlYqMQ5NY2T4x9hsmrSo8tqKAH2EkCSFiiM_toN34cj5ZfNz5OZ8e_RC-BSyXDhX_PDZO6O14g5yySV4yRW2tE-4CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریما رامین‌فر و پسرش روی فرش قرمز جشنواره فیلم ونیز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/693500" target="_blank">📅 20:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
فرشاد مومنی: ۸۰ درصد ظرفیت صنعت لوازم خانگی بلااستفاده است؛ چرا باز هم از واردات می‌گوییم؟
فرشاد مومنی، اقتصاددان، با انتقاد از درخواست ۴۰ نماینده مجلس برای آزادسازی واردات لوازم خانگی گفت:
🔹
در شرایطی که حدود ۸۰ درصد ظرفیت تولید صنعت لوازم خانگی بلااستفاده مانده و کشور برای تأمین ارز دارو، واکسن و مواد اولیه تولید با محدودیت مواجه است، چگونه می‌توان برای واردات کالاهای نهایی خارجی اولویت ارزی قائل شد؟
🔹
وی همچنین نسبت به گسترش واردات از مسیرهایی مانند کولبری و ته‌لنجی انتقاد کرد و گفت این سیاست‌ها می‌تواند تولید داخلی، اشتغال و سرمایه‌گذاری را تحت فشار قرار دهد.
🔹
به گفته مومنی، مسئله فقط واردات لوازم خانگی نیست؛ بلکه انتخاب میان تقویت تولید و اشتغال داخلی یا بازتولید وابستگی به کالاهای ساخته‌شده خارجی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/693499" target="_blank">📅 20:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=QPsBH-AaVG8OXyB6Nl7IfqZ7W84UMVjuO41ffLkdmtTU4MsiqgjV1Cs_PpRnfIWoOcPpa8ePoPiZnu_6mfyicNePlXGTGic9GpqPK5WXJDIunpBVH2yMqtTWPjQnXVsZue9b4uP_Z5TPE1-WQ_H7agVuQdSwdG6o1E-7NEdLzkuvrSn7DO4IA0YyTp2Fg65ixR1JZrNeQ-73X-7T0zJrVoFl4Z4ly7xYYFHKyhsTPukgemVQdTl1ILBtk4cb6LbSX0TuqFFri7mSGv8zkUYZGFm-I2KRvpNvXSwHujWskTYPpBu0khUkSqStuIENuRAUDObzBA9SxG469j_JYq98Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=QPsBH-AaVG8OXyB6Nl7IfqZ7W84UMVjuO41ffLkdmtTU4MsiqgjV1Cs_PpRnfIWoOcPpa8ePoPiZnu_6mfyicNePlXGTGic9GpqPK5WXJDIunpBVH2yMqtTWPjQnXVsZue9b4uP_Z5TPE1-WQ_H7agVuQdSwdG6o1E-7NEdLzkuvrSn7DO4IA0YyTp2Fg65ixR1JZrNeQ-73X-7T0zJrVoFl4Z4ly7xYYFHKyhsTPukgemVQdTl1ILBtk4cb6LbSX0TuqFFri7mSGv8zkUYZGFm-I2KRvpNvXSwHujWskTYPpBu0khUkSqStuIENuRAUDObzBA9SxG469j_JYq98Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: ژاپن انتقام نگرفت و باخت؛ مردم نمی‌خواهند مثل ژاپن باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/693498" target="_blank">📅 20:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh2df7OPa5JK0fcpUms6NyJmNIoysET9j2C9RaS5DnACNA3uQq8mhh5qw0l7KUICYwEXK7UxMxRgFmFjLVM0rUvoo_PeGRAswPXaFtVrM7TTYiUZvAmeFhq_A1c2Vo6TX-c18UeFXA9zquHeOFCJmiQpjJIKG2l7u_SAdzoo37M_GAjX1IlRbB-afE0QEcA5ZHx5a_AgrW8AjwSAE99qy7-Wd65qu0DYJibrX5y1ibDW-2a4Mkw5D_P43LyZb7X9UAvaLqd5CiqTIKtwMeghCbWXRgxGYnEBc3AiikvAFLuRL5Tk7vG6Zt3EVlqJYOfvT3pXc58iUbLi11Pbhq3iAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسته‌بندی موش و فروش آن دانه‌ای ۲۰۰ هزارتومان
!
🔹
این موش‌ها برای تغذیه سگ و گربه توسط مردم تهیه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/693497" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مدیرعامل شرکت فرودگاهی امام خمینی: پروازها به ترکیه، مالزی، چین، پاکستان برقرار است
🔹
به‌ جز پروازهای لغوشده از جمله امارات، عراق، عمان و گرجستان هیچ مسیر جدیدی برای لغو پروازها اعلام نشده است. پرواز به عربستان از قبل محدودیت‌هایی داشت.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693496" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق  یکی از شیوخ عشایر عراق در بصره:
🔹
۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری می‌کنیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693495" target="_blank">📅 20:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappBox | اسنپ‌باکس📲🛵</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on4bagN_KMJ-iqwwyRWiHhpwMnEGRfnkTSxbIC_ulyJ7jcYxsk9VRoaiLh4sf3KXnStr223QgjkLEpy7CS1j2h29mcRjn4NKMwrrvxU2bf8S15-NYoFfuYv3U6tsJpNvh-7q3Jq2wi7bRLGMqQ6LKkSC_aUxhupqy6XaLd-GTL55NArxnKnoH631ZBiNKkzL77uhSBgdHb5HPtO3o_0pZlT5cdsB6fM69n1ZHkqGfH1J3KyDh__l5YL9BNfXYReE4RGDTQ7ozoiy_rt-QoALIxRZkGRXxqJ7jmkZloxVTel9F-izmzbcLJVy7uSvEnJv5ut_S4pI95AUuJeNg8CPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این باکس جادو می‌کنه!
🎁
✨
با اسنپ‌باکس هم
۵۰ هزار تومن تخفیف
بگیر، هم شانس برنده شدن
۵۰ میلیون تومن
رو داشته باش!
💚
تا پایان مهرماه، موقع ثبت درخواست اسنپ‌باکس کد
JADOO
رو وارد کن و وارد قرعه‌کشی شو.
📦
برای تخفیف‌های بیشتر کانال اسنپ‌باکس رو دنبال کن:
https://t.me/snappbox</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693494" target="_blank">📅 20:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f765024f5.mp4?token=O6viXceAolNX4y917MYvZ3WR6inBTUMCZhabaG68wgRV94CnP2XaATyRBWUzKFKQB3DVV-x3e2MyM94BplZ0bcPptmkemcO4XqYVXnc52fVzHXKmVXLQQLVCl-qFDaAynTjt_F9jB_t52AAeSYbpi3Lww9r4nu4LPaf4j1IHT8jHy_hn12yV6ZETQejnTNBfecTsLTvwNXBl33HHR3P0TW0OAIiCclvD91lvTdgf9BJIKCetTH9Zvv1Atb6gxrIyuvgnWZ0RvsS_t1UDalJ3AwmuvPWOVzf_bHsKibvLEmSMbgv28CK0yja32tWMGEnTXiS5lTjm2VAo2EDOWU3Daw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f765024f5.mp4?token=O6viXceAolNX4y917MYvZ3WR6inBTUMCZhabaG68wgRV94CnP2XaATyRBWUzKFKQB3DVV-x3e2MyM94BplZ0bcPptmkemcO4XqYVXnc52fVzHXKmVXLQQLVCl-qFDaAynTjt_F9jB_t52AAeSYbpi3Lww9r4nu4LPaf4j1IHT8jHy_hn12yV6ZETQejnTNBfecTsLTvwNXBl33HHR3P0TW0OAIiCclvD91lvTdgf9BJIKCetTH9Zvv1Atb6gxrIyuvgnWZ0RvsS_t1UDalJ3AwmuvPWOVzf_bHsKibvLEmSMbgv28CK0yja32tWMGEnTXiS5lTjm2VAo2EDOWU3Daw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس: هوش مصنوعی بطرز دیوانه‌واری از انسان باهوش‌تر خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693493" target="_blank">📅 20:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSbjIdIGUXrMOZkoP-qZOTmX0-zy8snH_9tysK3Euy4kwXo8EfJ2u8A1pUXCwmGxDL0pCoHusDG4Dk0VZbH8M8WXyaLXucTw_emEElR9NxMvRtvy_AF8cNgph50GEwsMHZPU_T_t0FBMQ2Yrm2zyq5iKwISamSGm8rbz9kMG6u2WWM_txCgswqXhyTuw41TcDI4v4LJKsGNboyCqPrNZ2U1QRKh59QxxbDqt0SBsuRVpcG5DDnThnAPye5eVAmxiQg4po0Ak06Cejas4yg72nsF3_OUMthevc0O9WVHhUCEAD7E1ttRsH6hOd7AvygCEca-GCKCXXbaTriMKoOYhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی قلهکی: «همه‌ی شرایط در منطقه» شبیه به «بهمنِ ۱۴۰۴» است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/693492" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شیخ نعیم قاسم، دبیرکل حزب‌الله: اینکه اکنون اسرائیل تحرکاتش محدود شده حاصل مقاومت و همچنین تفاهم اسلام آباد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/693491" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDvZxyXnqv1o6UlTTKfwB95Xc8yOnbQ8C1YSVwt53LzVag5khrdWRAes2CMQubcZ_v_5V7j8gm_kV3sjKrgS2Z58hrIi3u6alBedMnB2Sbqo_w8TenOl9l_e9n_lXp2qpbsYoDla6hrlJHftDgUWiGBSxwgLGsF9obWYKdZCQUttp55v7AFeLBmA89BKE9hhDR6hJi_5O-EWaGp9TasV1zP3O6JdKFH3HPiSw6qyONNCuwZ0esa7_B7Fei2XUzVEE641paCxlYhyHxjRuZmFWseu4CCWmuTqDw1Lpd4gB4SeIdQ-7iaOmo83Rb9TdJtMbDfuVTYVXhuoM5BSdw2kiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع جرائم مهم مالیاتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/693490" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bab596ba.mp4?token=nPYFb2MpHRMKGUEigk5z7KWpYfqH1ZTqJbcB84XpCYeDHDi7HCzcQNgQFRcvTwbiI9ZhDjP2XIafMjekSiLH3clfe1qjIwM_ZzgGeUeSUCeXV2yWOeWW2Rgqh9i8hUjfH9YdYZZ5I7oB7yDqqqZDtEUB0b2WR5jmZVenyFKPOPNeQmHQ5iHsAh4frlq8wVAroU57fAdI4yVqqdd754cKpW7yId-FAm7rBEHT7h57hFJlVdwW2LdqHFeIU2S7PqTqriZLhTBOoLeGZlGliuqSEotbueaT6Rq4t4sHj9-naLXej0dbSi8XZY0vRRJP-paP1pXva9hFb2YB1JupSemSAJMrRsRrc8qjgrJLnejxu5W4Z5cuSq4p-2EXL5fTJ6aAAk59PDbOOsRmGy2xd2CbTa5h9RXs03RgM36tq3uak02crM4nn1Xwc1plwWpYN8thS26QbIzt7GhlVMo7-Ix5xDn1DGpbkF3Nu_EZkKt3jn9Yy3V81rVmVGPipVgPepK2e5M333n6PKybT2dXUj89qlRKLm6EZvL2S-oP7RhrXsqIJZb-yBjQ5ySzMA0qWgwe6nKr12KQKafXIzLHIulKjneJzL0JmJOGCzIoS3MoCtebJEotRdPgCV8B8DCtDKJ4ocwYtdXni_w5hot0FAluh5VIy7yIhSgp6l8m1l90Ylo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bab596ba.mp4?token=nPYFb2MpHRMKGUEigk5z7KWpYfqH1ZTqJbcB84XpCYeDHDi7HCzcQNgQFRcvTwbiI9ZhDjP2XIafMjekSiLH3clfe1qjIwM_ZzgGeUeSUCeXV2yWOeWW2Rgqh9i8hUjfH9YdYZZ5I7oB7yDqqqZDtEUB0b2WR5jmZVenyFKPOPNeQmHQ5iHsAh4frlq8wVAroU57fAdI4yVqqdd754cKpW7yId-FAm7rBEHT7h57hFJlVdwW2LdqHFeIU2S7PqTqriZLhTBOoLeGZlGliuqSEotbueaT6Rq4t4sHj9-naLXej0dbSi8XZY0vRRJP-paP1pXva9hFb2YB1JupSemSAJMrRsRrc8qjgrJLnejxu5W4Z5cuSq4p-2EXL5fTJ6aAAk59PDbOOsRmGy2xd2CbTa5h9RXs03RgM36tq3uak02crM4nn1Xwc1plwWpYN8thS26QbIzt7GhlVMo7-Ix5xDn1DGpbkF3Nu_EZkKt3jn9Yy3V81rVmVGPipVgPepK2e5M333n6PKybT2dXUj89qlRKLm6EZvL2S-oP7RhrXsqIJZb-yBjQ5ySzMA0qWgwe6nKr12KQKafXIzLHIulKjneJzL0JmJOGCzIoS3MoCtebJEotRdPgCV8B8DCtDKJ4ocwYtdXni_w5hot0FAluh5VIy7yIhSgp6l8m1l90Ylo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه کسی مانع تسویه با مشتریان میلی گلد است؟
🔹
میلی‌گلد اعلام کرده است که ۹۶۵ کیلوگرم طلا به صورت فیزیکی در خزانه‌های امن و بانکی موجود دارد.
🔹
اما دسترسی میلی‌گلد به این خزانه فیزیکی طی روزهای گذشته توسط برخی نهادها مسدود شده است.
🔹
طبق آمارهای منتشر شده توسط میلی‌گلد، این پلتفرم در ۳۰ روز گذشته ۷ هزار میلیارد ریال با کاربران خود تسویه انجام داده است و ۳۶ کیلوگرم طلا را نیز تحویل داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693488" target="_blank">📅 19:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c21c35167.mp4?token=T8N6fzK5xBwIHvAEJaOVysGJ1HsQXixVpYrvT2M2vywxkzDRDorQzi0zbkk5EdUWtbUox9x0G3Nb9e9Oxm70boo0XsC5JXdFtGGWjT57Vh934mOodE9r6xfgnawVN-jn2Lrs1vWvoWIrEFiRyMuq8qOwnqEz8WZRCF4XTeU76DBLU-GN8z_UsWOavpdwZRaR3TsNlx97yQpvjJzu1dklrF7dp6DwoKG4-aw2mUU5ThBE-SRTglL3YWc0vnHxY872YK4O6Tx3aDSEF75htF-56h-pebnqkgq3urJIeFsF5ME7MmIRJNnR5Ww32JOldshB6h260KYhHh87nSJxjUsAhk-KYHcVT_WBY_RypLyWdyurD1DB0BHmq_z1EawLvCGG-ZAOc0unofQ4SDo9SS-3HIy2lWpbaqFXS5YSYUZZCv1SfeqXYvtaHQBxdonJ1KfaQ965twImkjwvpc5rtzR0TF8IpKKjSrQXJwQMMypsJ8-i5e2f4k71j65fktwj61WUc-Hshr8BtMOBTMhFHnENlNQ6dZ778v_tsZc75F8F_YjjIS6fEYCfIeUG7_Mkxp8wQLySs4ojPNgZDXiXwI1g4_zKRTxRObxyW6RbU069vnliBOhCSOOaThFc8glEdyP7vHWWHkGJwxc-PvBj0bXj5p5mz2-JtYlLLm3QqOY8Zns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c21c35167.mp4?token=T8N6fzK5xBwIHvAEJaOVysGJ1HsQXixVpYrvT2M2vywxkzDRDorQzi0zbkk5EdUWtbUox9x0G3Nb9e9Oxm70boo0XsC5JXdFtGGWjT57Vh934mOodE9r6xfgnawVN-jn2Lrs1vWvoWIrEFiRyMuq8qOwnqEz8WZRCF4XTeU76DBLU-GN8z_UsWOavpdwZRaR3TsNlx97yQpvjJzu1dklrF7dp6DwoKG4-aw2mUU5ThBE-SRTglL3YWc0vnHxY872YK4O6Tx3aDSEF75htF-56h-pebnqkgq3urJIeFsF5ME7MmIRJNnR5Ww32JOldshB6h260KYhHh87nSJxjUsAhk-KYHcVT_WBY_RypLyWdyurD1DB0BHmq_z1EawLvCGG-ZAOc0unofQ4SDo9SS-3HIy2lWpbaqFXS5YSYUZZCv1SfeqXYvtaHQBxdonJ1KfaQ965twImkjwvpc5rtzR0TF8IpKKjSrQXJwQMMypsJ8-i5e2f4k71j65fktwj61WUc-Hshr8BtMOBTMhFHnENlNQ6dZ778v_tsZc75F8F_YjjIS6fEYCfIeUG7_Mkxp8wQLySs4ojPNgZDXiXwI1g4_zKRTxRObxyW6RbU069vnliBOhCSOOaThFc8glEdyP7vHWWHkGJwxc-PvBj0bXj5p5mz2-JtYlLLm3QqOY8Zns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
جاسوس‌های ایرانی‌ و لبنانی در ترور سید حسن نصرالله نقش داشتند؟!
🔹
روایت فرزند شهید نصرالله به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/693485" target="_blank">📅 19:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
عراقچی: به‌دلیل ملاحظات امنیتی و تهدیدات مستقیم آمریکا، تصاویر رهبر ایران منتشر نمی‌شود، اما دستورات و دیدگاه‌های ایشان به‌طور مستمر دریافت و اجرا می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693484" target="_blank">📅 19:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
۶ عامل که می‌توانند به ستون فقرات آسیب بزنند
🔹
شکم بزرگ، خواب نامناسب، بغل‌کردن نادرست کودک، نشستن طولانی در وضعیت نامناسب، ایستادن طولانی و بلندکردن اجسام سنگین از عوامل مؤثر بر فشار و آسیب به ستون فقرات هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693483" target="_blank">📅 19:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c5e80ae3.mp4?token=bmaRCzRsLBVYWImawKjA6MC4VGkxIb1JZbQQA80sXiQnDeICXpdjOQN9Hm1hGb6xaQxY-ALGPEw14ru_8bKkyQrgH5YAezP81YQbDWGCq5bSE6UMpstJa6huo7hVUnxHQ136M_0lWRehiWAQBSF8oX_NNPJ889ssuCTHJsl08CS2k_gBFs-QM3rUZTUc5_--qlcjwFOnvzjjM2-Eo1J99cpZKzxtgrkw6Bn-_CNmh25FytR_VexSwXkKKk0GZl3602CTpsr8nXRVsJuFeXHx-BOy04sZwR7oJV0zLws6BwUjKlZM3pU-Kufwlwb57zzIoTaxmr40b-tysAi_r9NAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c5e80ae3.mp4?token=bmaRCzRsLBVYWImawKjA6MC4VGkxIb1JZbQQA80sXiQnDeICXpdjOQN9Hm1hGb6xaQxY-ALGPEw14ru_8bKkyQrgH5YAezP81YQbDWGCq5bSE6UMpstJa6huo7hVUnxHQ136M_0lWRehiWAQBSF8oX_NNPJ889ssuCTHJsl08CS2k_gBFs-QM3rUZTUc5_--qlcjwFOnvzjjM2-Eo1J99cpZKzxtgrkw6Bn-_CNmh25FytR_VexSwXkKKk0GZl3602CTpsr8nXRVsJuFeXHx-BOy04sZwR7oJV0zLws6BwUjKlZM3pU-Kufwlwb57zzIoTaxmr40b-tysAi_r9NAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به‌دلیل ملاحظات امنیتی و تهدیدات مستقیم آمریکا، تصاویر رهبر ایران منتشر نمی‌شود، اما دستورات و دیدگاه‌های ایشان به‌طور مستمر دریافت و اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693482" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مقام آمریکایی به سی‌بی‌اس: ما می‌خواهیم تعهدات مرتبط با هسته‌ای در پیشنهاد ایران گنجانده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693481" target="_blank">📅 19:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سفر وزیر خارجه عراق به واشنگتن
الحدث:
🔹
دستورکار کلیدی این سفر، پیگیری برای دریافت «استثنائات» جهت لغو تعلیق پروازهای ایران به فرودگاه‌های عراق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693480" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65deb07bf4.mp4?token=tktyHW3LpsKF6N-Ok-4XVku1EgJlnUmwWktip1160yhL1x85ccSjyySR9XklMB49EVfVSTS2giqSjf7B4JWU0Lx90ACKm7rZXnGO6S_NhN2C7DfCtVBz8o4kKcp0vln8mDdQZWxJpuGAQGb6JKCASIG48tPzjn-MQJgn6JrvVGNo9nT2lUsGFjGXNRwlCxU5343HoE_5UY8H3KA2zwZhRCOxXqBzWlzc21NUEzABAhPgUyKnoXBXRz0tRdihTsteeQwSCNNlZVb9pRA1rRIrQISduZ1kv_iwSsQP6pN881VynQQAStjASMhmeTgAP3ZW6f0A8RsUIkKUbR8UWxoEww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65deb07bf4.mp4?token=tktyHW3LpsKF6N-Ok-4XVku1EgJlnUmwWktip1160yhL1x85ccSjyySR9XklMB49EVfVSTS2giqSjf7B4JWU0Lx90ACKm7rZXnGO6S_NhN2C7DfCtVBz8o4kKcp0vln8mDdQZWxJpuGAQGb6JKCASIG48tPzjn-MQJgn6JrvVGNo9nT2lUsGFjGXNRwlCxU5343HoE_5UY8H3KA2zwZhRCOxXqBzWlzc21NUEzABAhPgUyKnoXBXRz0tRdihTsteeQwSCNNlZVb9pRA1rRIrQISduZ1kv_iwSsQP6pN881VynQQAStjASMhmeTgAP3ZW6f0A8RsUIkKUbR8UWxoEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهلت ۴۸ ساعتۀ عشایر بصره به دولت عراق
یکی از شیوخ عشایر عراق در بصره:
🔹
۴۸ ساعت به دولت عراق مهلت می‌دهیم تا از لغو پروازهای ایران عقب‌نشینی کند.
🔹
اگر دولت از تصمیم خود کوتاه نیاید وارد فرودگاه بصره می‌شویم و از تمامی پروازها جلوگیری می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/693479" target="_blank">📅 19:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5YovrsJ8V3PGHHrp9Z2AV_MQ-awSYSPulIB7lkI28dLcnGat5CtIi6-wiGdZwC5ZWKPYmxRc0R-a-a4Y5AK2qWiGZ1EX-Sew47O2IFin8d7syKDHzpF4BMUjf67R-ipZAuIVhD8HZ0rPKc1sB7TRE42hH6iqq_-N_AJJriJsEEEbyu_ON2X1sOe0FCnCEtMgZ2KZqjDcVXH4vs7gZSobgEu7RsSH-TCKjznWLBbROLivKuag8snoa71v--vV1wiBL9cRrb1Uvzbf5syG4WPoJV0tOvfcftHuVhcq0c1A1rc8A4hgxPk08yqXs1O7I6l72pkcSwrimJreplx0U8jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنزین یک‌ساله رایگان برای خودروهای وارداتی!
🔹
یکی از شرکت‌های عرضه‌کننده خودروهای وارداتی، در شرایط فروش چند مدل، هزینه بنزین یک سال خودرو را نیز به‌عنوان بخشی از خدمات فروش پرداخت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693478" target="_blank">📅 19:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f4121d3c.mp4?token=nlNizXIi11JXiHtmOLeR_0LK5cQ5xnGGL8rO7MRriwZw7H1ej2DNMPx3jyfHU179mtDcRMFlsVqMYFFO-vOAeX2_3H8cMGrGEpRF6n1YVp0wD4FEbBNtDXqzVIJJ4cU_bEsKQVkHOXiS24CymvscKfkmlNljaaGqkzt5cPOsMO0Y9NQfDZh7Di6nHXdRyy5MFd9UJX0wo5xPn3qGhb_aGU8W3kXFN8qIb1j5y1LQifPc4ATVtgPqbRl9eNu3uRT7-1HUCc4ehe6YJlRQpweLSodNz-2yX2U9EwETGtJK0l3wp_NQmwhCS_RhkqT7e0X-3oKOau4GNvR8sfbl5zJxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f4121d3c.mp4?token=nlNizXIi11JXiHtmOLeR_0LK5cQ5xnGGL8rO7MRriwZw7H1ej2DNMPx3jyfHU179mtDcRMFlsVqMYFFO-vOAeX2_3H8cMGrGEpRF6n1YVp0wD4FEbBNtDXqzVIJJ4cU_bEsKQVkHOXiS24CymvscKfkmlNljaaGqkzt5cPOsMO0Y9NQfDZh7Di6nHXdRyy5MFd9UJX0wo5xPn3qGhb_aGU8W3kXFN8qIb1j5y1LQifPc4ATVtgPqbRl9eNu3uRT7-1HUCc4ehe6YJlRQpweLSodNz-2yX2U9EwETGtJK0l3wp_NQmwhCS_RhkqT7e0X-3oKOau4GNvR8sfbl5zJxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693477" target="_blank">📅 19:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/693476" target="_blank">📅 19:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693475" target="_blank">📅 19:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
طائب: همان دشمنی که در ۱۸ و ۱۹ دی آدم کشت، مدافع حقوق ما شده است
رئیس سازمان بسیج:
🔹
دشمن با ارسال سلاح و حمایت از عوامل داخلی، در ۱۸ و ۱۹ دی اقدام به کشتن مردم کرده و اکنون خود را مدافع حقوق مردم ایران معرفی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693474" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693472">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-5vco08w1z6wa9dzMdUNP5XH9d0JRagN3AT6XYa7kS_K2NNAftI4dv2BitYeGkHSfU333I-13Yrf2VaXEaI8Bd91bSKvH5nX22HMiebk5zxeCK_7ZHYbkdHCnpXbZtYYSJ-UKCtWgu-V3bxKDLlKo5-AuplcStKrU-Fo3hpmBmuqQAlkYACSKNmAp89C7WqaLxH5I7w8LKcmziqgQ03BDap_QV4Qio1DGzuTv5nldBTmZBNL19szn481WTTMxj4Ow0YgcW8GtFTDjrC2tj_r1QHsTI6Ra99cg59t34Ov5OZ6_ywwxnG4WESdxcOJkBnowVnB2exWUABCQ4qXwrN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم‌ترین مشکل بیمه تکمیلی از از دید افکار عمومی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۷ درصد، تلگرام حدود ۱۸ درصد و بله ۲۵ درصد بوده است.
🔸
بیش از ۳۳ درصد شرکت‌کنندگان پوشش ناکافی خدمات و حدود ۲۰ درصد هم هزینه بالای بیمه را به عنوان بزرگترین مشکلات بیمه تکمیلی عنوان کرده‌اند.
🔸
طبق نظر کارشناسان نیز، افزایش هزینه‌های درمان، محدودیت پوشش‌ها و چالش در پرداخت خسارت از مهم‌ترین مشکلات فعلی بیمه‌های تکمیلی است.
@amarfact</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/693472" target="_blank">📅 19:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693469">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: به ازسرگیری حملات علیه ایران فکر می‌کنم
🔹
ارتش آمریکا عبور نفت از تنگه هرمز را تسهیل می‌کند./ خبرفوری #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693469" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693468">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3823d044b9.mp4?token=uKX8hs-sLzxIaE-hRJeoJvPKt-Akp7pRaz0SgnWavh1JXbkIWhbKKui_wzuqOQxszMFgZhq7rBITUHBjX842RKmBQdjHInDxEcJdI66jIitEvMJPmzo5-IOgsBnQ-2BIGqgJdmzOJS5GlTzOWoqE3VmjEEdfvzCMMI2MsLJefCTAIUHsFaNY91wtLg7lznN0YRWdQ7jPwAGmj__ouMlBzjgMYxG-VOI4YNTvsVp1SMgvKUGekmsyViXQbbPsLjvuM3Hwr4p_b4aw4hnFPuiaN9ANwGI9TMhcjGnQIr1A5wpbTZdz5nT8x7Gti4uUgOCvaeeQxwPgVhTct9qt3T0low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3823d044b9.mp4?token=uKX8hs-sLzxIaE-hRJeoJvPKt-Akp7pRaz0SgnWavh1JXbkIWhbKKui_wzuqOQxszMFgZhq7rBITUHBjX842RKmBQdjHInDxEcJdI66jIitEvMJPmzo5-IOgsBnQ-2BIGqgJdmzOJS5GlTzOWoqE3VmjEEdfvzCMMI2MsLJefCTAIUHsFaNY91wtLg7lznN0YRWdQ7jPwAGmj__ouMlBzjgMYxG-VOI4YNTvsVp1SMgvKUGekmsyViXQbbPsLjvuM3Hwr4p_b4aw4hnFPuiaN9ANwGI9TMhcjGnQIr1A5wpbTZdz5nT8x7Gti4uUgOCvaeeQxwPgVhTct9qt3T0low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عوارض نزدیک بودن موبایل در هنگام خواب!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/693468" target="_blank">📅 18:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693467">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای الجزیره: منابعی در تهران از ادامه مذاکرات غیرمستقیم میان ایران و آمریکا در نیویورک خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693467" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693466">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ به آکسیوس: انتظار دارد مذاکره‌کنندگان آمریکایی این هفته گفت‌وگوهای بیشتری با ایران داشته باشند/ خبرفوری #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/693466" target="_blank">📅 18:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693465">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای ترامپ به آکسیوس: انتظار دارد مذاکره‌کنندگان آمریکایی این هفته گفت‌وگوهای بیشتری با ایران داشته باشند
/ خبرفوری
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693465" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693463">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: ۲ سال تمام جان کندید تا سلاح را بگیرید و نتوانستید؛ حالا چرا این توقع را از ارتش لبنان دارید؟ اصلاً سلاح چه ربطی به شما دارد؟  دبیرکل حزب‌الله:
🔹
در خواب ببینید که ارتش لبنان ابزار دست شما شود. ارتش لبنان، ارتشی ملی…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693463" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693462">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/716ced5d0f.mp4?token=e3E7xM80Hz_miVhJe-lLjCWZHXbmuAVJktarxqO626J8wT1xchLP786leI2EDrjallKpkhE9Ths82u-0He5Fp-EFUYtgjfcKgwz9YSG3vzrCdvWZNTSoo6Llm8SxGJhkqHl-ONVMZFfZnSuulDD5AdNmiO6mKfHJd-Ru_2j1jovGafSHP56J6XVoOP597s2ywHsNyJn8g3JFfKo2S9PnjPu5etgEpwxU9zxz9wjSAo_kjhjWozu9a3Bj-x3iEFWhgv4B2yIe6YvCn1RzgzrO1yRABIwtwm7-FWbChhzLc2UFNzT_zggQy_VHE0rQ1pFCk7mb7j_Kcd7UGV3yP9hlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/716ced5d0f.mp4?token=e3E7xM80Hz_miVhJe-lLjCWZHXbmuAVJktarxqO626J8wT1xchLP786leI2EDrjallKpkhE9Ths82u-0He5Fp-EFUYtgjfcKgwz9YSG3vzrCdvWZNTSoo6Llm8SxGJhkqHl-ONVMZFfZnSuulDD5AdNmiO6mKfHJd-Ru_2j1jovGafSHP56J6XVoOP597s2ywHsNyJn8g3JFfKo2S9PnjPu5etgEpwxU9zxz9wjSAo_kjhjWozu9a3Bj-x3iEFWhgv4B2yIe6YvCn1RzgzrO1yRABIwtwm7-FWbChhzLc2UFNzT_zggQy_VHE0rQ1pFCk7mb7j_Kcd7UGV3yP9hlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را کاهش داده است/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/693462" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693461">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: ۲ سال تمام جان کندید تا سلاح را بگیرید و نتوانستید؛ حالا چرا این توقع را از ارتش لبنان دارید؟ اصلاً سلاح چه ربطی به شما دارد؟
دبیرکل حزب‌الله:
🔹
در خواب ببینید که ارتش لبنان ابزار دست شما شود. ارتش لبنان، ارتشی ملی است و مردم لبنان خودشان با هم کنار می‌آیند؛ شما کاره‌ای نیستید که بخواهید خواسته‌هایتان را دیکته کنید.
🔹
هرکس دل خوش کرده که با واگذاری بخشی از خاک لبنان، بخش دیگری از لبنان برایش باقی می‌ماند، سخت در اشتباه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693461" target="_blank">📅 18:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693460">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
عراقچی: اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم  وزیر امورخارجه در گفتگو با ان‌بی‌سی:
🔹
می‌خواهیم به جنگ پایان داده شود و خواستار آزادسازی پول‌ها و دارایی‌های خود هستیم که به‌طور غیرقانونی مسدود شده‌اند.
🔹
ما اهمیتی به انتخابات…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/693460" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693459">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPllV7EaL7eH7kpIol28YW4i2Xnx7_OnZozRQ_u20GvIrlfxCrKCbwmRMXIEPVveRY0uJpDrH-K9yTzGyDyxhOkr3W1awjRVC7Qxmnltr6AKliTrVqVEctLStJ8WbQhsK_PYblq_5G_2h7i8Ea0gw_X2hAMI855RZbP7-3gh7RAFZQ937HISgmMJ6jBoIYJP8NZMHxtpgQusOXvpr6T9WkGGC_LZfDtYjwjnol42UDfAX7kSgquntHP3QVX0m_45XK3PRtcPFax1gKuJxJ7XdwsxtTPp3KN4BEzXzckSxTYheQpYBfSTjpQqzdGaVjB4oZGu3OuhnlujDAPqm_UDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به گاز شهری در غرب آسیا چگونه است؟
🔹
مقایسه دسترسی به گاز در ۶ کشور غرب آسیا نشان می‌دهد که ایران با پوشش ۹۵.۱ درصدی جمعیت (۹۸.۶ درصد شهری و ۸۶.۱ درصد روستایی)، در زمره بالاترین نرخ‌های دسترسی به گاز خانگی در جهان قرار دارد.
🔹
برخلاف شبکه لوله‌کشی گسترده در ایران و ترکیه (۸۵ درصد)، کشورهایی نظیر عراق، امارات، عربستان و قطر برای مصارف خانگی و پخت‌وپز به‌شدت به کپسول‌های گاز (LPG) وابسته‌اند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/693459" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693458">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS4zW6S5fZzoJ2U_Gi5wprQ2Tm6XVQeK_rh1B6Znnf7_EfytDhx_FegclcTEiLFASVQHR2vqnmL7JIWbwoeQyATN52Ry5GKwCO9bodVDZP4N3cvFfgoA8WHB6Mya0q0NOBP2k-87WCdttahI9Vg9u_eM8i5LLcV0fWBBixR7I8YwFPgiRsxmcbiKoAv2nbZLBGVNUnCr2aE0C42VLcopHtuXWvlfoRgbDYoeYcQiAp5NKKvlIR4E2XF-AG-iqgXNcxCofemQvLpTe3qBqYFQagv4AsqJ7YWxLSQkp5abWgmoS5bT-4VIduj1otRqch10tS1h_y3byoeBCsNCPhpFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی، نماینده مردم در مجلس: عجیب بودن این حکم به دلیل وقوع چند تخلف از روال معمول قضایی است
🔹
جزای نقدی به‌جای حبس در نشر اکاذیب:  اساسا برای اتهام نشر اکاذیب جریمه مالی صادر می‌شود و با وجود پیش‌بینی حبس در قانون، روال بر حبس نیست. بنده شخصاً از آقای…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/693458" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGPSarYaLDJ_M0hBGELpIXteD7jAVlC4jIqG4CJ2V1y7knQnngDbGxWqIEYLHKeHPl96d6SAje9EetFS2BT14NDBS0hwqmDIG9iwL6g_fdCMwpwlNIQ7YOs-p7K_87chYV7Di5kgx1fTQliSFGy5P7F3gQLYv-g1Rjx-rX8D2j3n4QWtkt8WUP4i6wkoYFQq5_wvSqodyjJ7a5LJsOl2DHVK3PDb_2ft0Owhb6Dk9jUljMrc6G9Z824Bnoh3mW9WVjc27cf_PSJGxc2OV6wN1b6J0io6WqjqKKJBxSRtqFM1NIfroz4rj7ATmD8uYESzKfCoEVwFaiW_Im-8kDzQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک مسیر تازه در خبرفوری آغاز شد
🔹
«آوید» جایی برای یادگیری، تجربه و ساختن مهارت‌های آینده.... @AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/693456" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClZzq1_07VB_95SC4w2zjnnAUZO1ObuTHfwyBnVN0RAfz_Z5v_DPlPEQC0hOAouvS86WviQc5CBIsZaoZ13PAW0lpHpEtWgyX9M4Nr-MhaXThUUQB7WyAOaBMmHYV_h48IZ-U37toNfcZav_rSaK75gYYaohRoBimTRuzwHBlDAEVew9pTv1zBcUbx5XIghfILV6uwmoRJDSjqNQpAO9_X3vIzJjZjVFDBQNNm6mEWk4oqDLMz96XN899v6l4Fm2rpeznrxOXVPEVRJ3Owf6zFvE-EQ112VtdBdKYelg5F2pF9LnhbHz_ZjGDRyqBLAlA7umSkiWo-ZGc746RIEvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhRm0woFun0yRkg6ecCnkNFRgZcu3xTpcTbtVU1YojrAzAYeOpgR6ZfpOJh5DhMQB8PSQ5GV-ZN_PJOALEn0_DffMqFXldN6b9LKBSbIr5MrI0fgbnxZ5z4pt1MHSJ5dM4LD9nrjoCo0h2qW_CjdwvTp_wYphLL6_Sg57Z5WaMDdGJGNmjRPlM0Afl_WPi0pqrueDegku6oGYnhB-ZNcZUSw6D-PaIIZMJYbFoslpXowTj4G_NuLk38INN3hqi-9FabJMHqKRHgZTHusyADf_o8inzD9HbVZD3ad-0EGnRU18sMgIbDsvNg-nXpWv5vNyDvBME8hobrFdSBqrS5NdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHVZRCQ4UehBBBrbwhp5i6r0K20T9kHGFX09IAgTzi1MtodjSdCis9feTsNRrxc9EIWMKv8jOIbYtJ1lasPAvaoELaqdS0ElDx_3QscVXsVemqJAkIP9e7o4KLd_p_VC7sOm3UlgPR7eMRxHthX8MBu-dRqKlPQxxXKhRGSTwhzun6kL-UkWQ4dUIf3TH5V42dTXWHDTaK-P5T3Iguy45MumzPYCoGMCoycHFn8L5mie1E39O2f3D1mFTl67k96QIicy3DrAZRKd99GPe53MyB6xQ_Nmoks4MlzWzRET8gWxTl9Gn-e79HqzJRtdXURaNlflvnO8Vu8v2LTVWmlKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6sB7UsnSNfx60dBwipA-Nr1NIak3_U_5-b7PIxrkinj3t-ll-uaL2VC3bwIwFrgPWj_gXSj3lZD9hc-FPiEGnFJQEjQd0K2qZMU5ED8hz_h5FKgU9NG0G3c64jLlL8CRS2WdVMHpL77n6JJhXIq7Nw5A59BYEcSSTKKp4mFrBs93hooy43pwluaP6WA-8J9bKWg9bIlnhnVvfDzXEhhBfI_w4ZHrGPIpsuU-QAGtUXOHlQgW4Gvy9meIhI8-5l26ApqwIqXTHlrJsyNflT_I9evI80glAXQ7h_OOa_mJGKcAqKxVGCQxjezTtb9NOo-W_458yUU5DrU_M5U7rwe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5DhKZwqy6dhLB3r7XbPAUPe1QMV6In_09YpGVwQ-K2V8jp-kw_vXFrI3P-gcSgoiJdKABt8JRvwJQskuyeNy75dpdV0_sxsgYUESO5SYM6YziGDc-CD0KYun6E-jUlIp4968vgYX_EWkidjHGjQbJ7Nkil5j4wQJCAZrpw2lC8CgCkr86q-gL_3zucTrh72UIJDN9r_gWDK_xPNXC-2ZHarMZlfs6R00f1z-ZTc2hHAag72MmsalXTEUz4awQd01X6BxMPnTRZrjwp91ZOhkKeQ8mu-2xRtz6zXhsFL8J7wx0kjAAoZklGXNkQFoeXG73jaZn-SRFTxjLobe0oLSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بسیار کاربردی؛ ۱۲ ماه سال به انگلیسی
🔹
۱۱ دی (۳۱ روز): January
🔹
از ۱۲ بهمن (۲۸ روز): February
🔹
از ۱۰ اسفند (۳۱ روز): March
🔹
از ۱۲ فروردین(۳۰ روز): April
🔹
از ۱۱ اردیبهشت (۳۱ روز): May
🔹
از ۱۱ خرداد(۳۰ روز): June
🔹
از ۱۰ تیر (۳۱ روز): July
🔹
از ۱۰ مرداد…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/693451" target="_blank">📅 18:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/693450" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693449">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خبرنگار cbs: یک مقام ایرانی به من گفته که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/693449" target="_blank">📅 18:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693446">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SedWj9wpy2JBdpGePJHXy2ZnpeM4ZDSuiOxK5UW-N9eTQDEJRlQZfX_wDCrYb19dcfctxSQ2AojoyNA-orskB4v2s0F7W-H86kyhAt0Vcrezj73Jx2BELrbQkLpIqf2EHw09xxv97Bkzg1sL3nYeCXlf0S-rgjUsnc-0lf4OyZDMLTvggBb3z00b9zUriHCzNTk9ltkutcUus4_fppiA_Gbm4F8AFg4yoWSsAOhyi11-H-M5Ysrw5ZK8yvctQeqW4Tu--o5-F916bQQDgMg4Eo-XChkcCpEjwTlIcFX3jBV2GFfCl36Iu5c5zIMMoRgbgKKwN128_k7csPPgwfWgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHzq6shVfmTQgmfpynTycu8BkPwFABCJFgl0s5LBOR2myGxHY35P6f1S84VWHbKXZiqU8W0_4AGgj4iWKJ1g3Hr0xcN6W4W3ddZkCmV9eF3xtCXzJSUfamVKnF31rLiqE4sRNG9aqq2MsLoukav8hcKJcom9glYFG5YHcsjk-cy2m4ltSF6es3HuSLKCuYswX3bDgTGIjV6h4Y8FwOct1olylwCieKZfnkl_DivjWUrMscnZHHJVxdjbPsKIrS793Fs7qB_4HosPHdPBex19gsiknhdkXFFFgdOGM-yMTAOzvG1KjGC8fUKG6SRfLyzEd9ctSXq9kOjxsyXEAAZnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7uK1zv531UCJTp_LbhGF_3NzP2_Q96aJAC_wcyFhl355A6jaBEC5oqTUdMuDQ1x_AVfgHjwQ1eeQ-W23C0mJeT7g2pttQ3RZPh1L-gYflyzUEHZChmUzn6fa_A-gHd0hJkTE29JFgk_eT0L_3era6zF4SvgKmNCtw2rlB0K56MXbUDyXb6R09mjt6bYJ9OXAWypqKspYngKYA34fF1WD3jx_76sx1SggvNYwJ4m1rrnGvmzlBt94RXpWzyMgX0lP_ijJYw7sjp01c7jmzQgRo4JVW-ydXfnqXfjuV88KQbHpobQ1fJvfKEvd5RVV_wVEDypPnDw89KjmgC37oy21Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سنگ در غذای دانشجویان دانشگاه علوم پزشکی بهبهان!
🔹
تاکنون توضیح رسمی از سوی دانشگاه درباره این ادعا منتشر نشده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/693446" target="_blank">📅 18:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را کاهش داده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/693445" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ماجرای عجیب برنج‌هایی که بدون اسناد و مدارک وارد شدند و اسناد تعلق آن به بازرگان وارد کننده در کانتینر پیدا شد از زبان رئیس قوه قضائیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/693444" target="_blank">📅 17:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بلومبرگ: فرانسه برای حفاظت از پالایشگاه نفت عربستان سعودی، کمک‌های نظامی و نیرو اعزام می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693443" target="_blank">📅 17:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157770ffed.mp4?token=NHAGNJpXZ726tqR3zSFs1sVaqnI0XuX2k62TIF4kXraNivfkFO33eVAMnke2Vgnw-SaeAN9fou4Q0QsE8XzzfoJA4F8Pqr7UTSgKoMATSuHaRqX_svXQ2ZP2OR-qr8jiSd1GmlzAO85_l-bVRKPVP7uXzuFzi-VnUYEp1CCe0W_dma8wwy1qR29hnZZyrMHKNz2SAwYUZDa_C736DZDxW4W7N-4Kb4PpbP86eFDYdlv_pt5G0WnnOcoK3TmWhbL3AGxc-yJUuOluj8PIW644iR1MTSsOs5CzZUmy6CaM9wJS0W4JGKYfMGLvnj13HXkOaEjNxFA4iCHrhjHrFl6Gyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157770ffed.mp4?token=NHAGNJpXZ726tqR3zSFs1sVaqnI0XuX2k62TIF4kXraNivfkFO33eVAMnke2Vgnw-SaeAN9fou4Q0QsE8XzzfoJA4F8Pqr7UTSgKoMATSuHaRqX_svXQ2ZP2OR-qr8jiSd1GmlzAO85_l-bVRKPVP7uXzuFzi-VnUYEp1CCe0W_dma8wwy1qR29hnZZyrMHKNz2SAwYUZDa_C736DZDxW4W7N-4Kb4PpbP86eFDYdlv_pt5G0WnnOcoK3TmWhbL3AGxc-yJUuOluj8PIW644iR1MTSsOs5CzZUmy6CaM9wJS0W4JGKYfMGLvnj13HXkOaEjNxFA4iCHrhjHrFl6Gyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی؛ از ۲۰۲۱ تا ۲۰۲۶
🤖
🚀
🔹
مقایسه نسل‌های هوش مصنوعی از سال ۲۰۲۱ تا ۲۰۲۶؛ جهشی از مدل‌های اولیه تا سامانه‌های پیشرفته‌ای مانند GPT-6 Astra و Claude Opus 5.5.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693442" target="_blank">📅 17:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سی‌بی‌اس به نقل از یک منبع آگاه مدعی شد: مذاکرات آمریکا و ایران با وجود رد پیشنهاد توسط ترامپ، هفته آینده برگزار می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693441" target="_blank">📅 17:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراقچی: اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم
وزیر امورخارجه در گفتگو با ان‌بی‌سی:
🔹
می‌خواهیم به جنگ پایان داده شود و خواستار آزادسازی پول‌ها و دارایی‌های خود هستیم که به‌طور غیرقانونی مسدود شده‌اند.
🔹
ما اهمیتی به انتخابات میان‌دوره‌ای آمریکا نمی‌دهیم؛ آنچه برای ما اهمیت دارد منافع ملی‌مان است.
🔹
همان‌قدر که برای مقابله با هرگونه تجاوز، حتی اگر به یک جنگ ویرانگر منجر شود، آماده‌ایم، برای مذاکره نیز آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693440" target="_blank">📅 17:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a5f938fb.mp4?token=KA_L8zPvErIpp6Rym2ZjlTN62tnIXTD9ZbLGxw1Cla_pq9cDQYyeuRlkVihw6sZtCjzU1paMT1kvIAjCVTy-QSC_7BC638BwVg6fdpm33sl0GvDWg2eAb6V-XZMWviPKmdKCe2bV4fHRjXC_rIBaSKyc05XbsFfpIUssma0X_Y4JA6yAEEBbCoypBS4YDEVY6gBQSGFRSzej4Ba-3vCeXuycwa_QRS4kSciZuqPaW6pjfcduju6z4UX0locmyu7OFN_zZVCQcAUvasMMegozpo6jD7gfYP3eXTey25f-KEyCLt_ZoawSY6mrTAyKTi8I81UcFY1d8cv7CY4AKO858w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a5f938fb.mp4?token=KA_L8zPvErIpp6Rym2ZjlTN62tnIXTD9ZbLGxw1Cla_pq9cDQYyeuRlkVihw6sZtCjzU1paMT1kvIAjCVTy-QSC_7BC638BwVg6fdpm33sl0GvDWg2eAb6V-XZMWviPKmdKCe2bV4fHRjXC_rIBaSKyc05XbsFfpIUssma0X_Y4JA6yAEEBbCoypBS4YDEVY6gBQSGFRSzej4Ba-3vCeXuycwa_QRS4kSciZuqPaW6pjfcduju6z4UX0locmyu7OFN_zZVCQcAUvasMMegozpo6jD7gfYP3eXTey25f-KEyCLt_ZoawSY6mrTAyKTi8I81UcFY1d8cv7CY4AKO858w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سربازگیری اجباری در اوکراین به زنان رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/693439" target="_blank">📅 17:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693438">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آمریکا ۶ میلیون بشکه نفت ایران را دزدید  تانکرترکرز:
🔹
نزدیک به ۶ میلیون بشکه نفت خام ایران به ارزش ۶۰۰ میلیون دلار که پیش‌تر توقیف شده بود، به‌صورت بی‌سروصدا در حال عبور از اقیانوس اطلس به مقصد آمریکا است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693438" target="_blank">📅 17:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693437">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez4nVJda1wRvpLfK04B6RrIN2_1zBlfMp6Z0QpnkJrxT7xyIF5nXvEEKyzSFPEFls3dJ0kKr4MVRWTBpHKfgibmzoZwcqBVn9IXXgKiDq4cUYELOTMRMQqqvJk-wm8M3Bj0LFc603IUvwFFCZBEat5329DXkWWFwbyGJ_DynNWj5EMyufJO24UKVuqJ76HidJxy0ocEBCsu_XW8AQb9r1hVWBseWlvm2A_akOBg_aTZ0nNFbV4dYiRPwIbEb1OH63-Wq3OuuKgFw270W4GFdXXs5pGilZ42cpDiLvkMT26QJw5GYglrRCns3gMUjNgsmfrPwEWDZyh3Ls0lpnqMcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماشین حمل زباله هم میلیاردی شد؛ ۷ میلیارد تومان برای یک زباله‌کش!
🔹
قیمت خودروهای حمل زباله از حدود ۳ میلیارد تومان شروع شده و به بیش از ۷ میلیارد تومان می‌رسد؛ خودروهایی که به‌دلیل فعالیت طولانی و شرایط سخت، استهلاک بالایی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693437" target="_blank">📅 17:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693436">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس قوه قضاییه: دشمن تصور داشت با اعمال محاصره دریایی، کالاها و محموله‌های اساسی و استراتژیک به کشور نمی‌رسد؛ لکن این توهم دشمن را باطل کردیم و موفق شدیم ابتکار عمل به خرج دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/693436" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693435">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95014c10ee.mp4?token=YPx7Up0aZ1Uskao0oABZgg20usY-Qm9KlDwCMEpQ-xFcOqcV2MYkMKdiuzZnAN0ak54ggPFSTvj6e8ZhIUkIa3wiWhT7spS-XE2bSDfZ-ywIc-SaNSGMmHPH9KLt5cJMWOp9i8Gfx1n4omiT-_mSGvCo10QZuQVnXv9wAGtAb5rpveua2jvIuhUDlvlOesC3uRQIvMqvRsUySiYBv_qpai7Pevx4Rh8uvhzMRoIWev9q87ZNPGS4Xwkk8VRsQvc9pC18BnjXO5G7_zU6eR--mY0BJhlNHt4fEEcyKdCmRoC6NrCWxluzcsj5EHFH1W5ydfjt4mHyquzI6xysMyfuQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95014c10ee.mp4?token=YPx7Up0aZ1Uskao0oABZgg20usY-Qm9KlDwCMEpQ-xFcOqcV2MYkMKdiuzZnAN0ak54ggPFSTvj6e8ZhIUkIa3wiWhT7spS-XE2bSDfZ-ywIc-SaNSGMmHPH9KLt5cJMWOp9i8Gfx1n4omiT-_mSGvCo10QZuQVnXv9wAGtAb5rpveua2jvIuhUDlvlOesC3uRQIvMqvRsUySiYBv_qpai7Pevx4Rh8uvhzMRoIWev9q87ZNPGS4Xwkk8VRsQvc9pC18BnjXO5G7_zU6eR--mY0BJhlNHt4fEEcyKdCmRoC6NrCWxluzcsj5EHFH1W5ydfjt4mHyquzI6xysMyfuQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بجای یمن اسرائیل را بزنید!
🔹
یک شهروند آمریکایی-فلسطینی در نیویورک، با انتقاد از سیاست‌های عربستان، خطاب به هیئت سعودی: «مکه و حجاز را به اسرائیل فروخته‌اید».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693435" target="_blank">📅 17:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693434">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbFMiHJWJCWBpoIA44ORC4Krc95Na1-zajZEWjZu5p80eCzpFg6mmAwXw9MDrVZncmOqTldL-igxLVzOZDZlq4dKhJVkJZycwwKguykcztIGAcyCt1-JsiLnBd4i280ToGPk-qqf3K5v86eotYdlknfdreVcNo7kVwqqsctPjhE5f7hsEMK8UkTRmMS2TIA65dHF2_7AeLrvFwOY53HKGtEzt4GoHK2mBNqnkxc9XpIoSOrvmxzQG_eyFlGc7joiy1bmAPDyL3UCEfvQHgtc1FSwhlGtYK9JpHRf-hNLHAz9vyyIOLm7uO6PHev-qDakImpp1nF3PvLokZjRGvN_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
مجوز رسمی خزانه‌داری طلای آنلاین برای بانک رفاه صادر شد.
طبق خبر ۱۸ شهریور ۱۴۰۵، بانک مرکزی مجوز خزانه‌داری سکوهای آنلاین طلا و نقره رو به بانک رفاه داد. یعنی طلای دیجیتالی که در اپلیکیشن «PayVal» خریداری می‌کنید، معادل فیزیکی‌اش در خزانه‌ای امن و تحت نظارت نگهداری میشه.
🎁
برای شروع: با نصب و ورود، ۵۰ هزار تومان جایزه بگیرید. هر معرفی هم ۲۵ هزار تومان + درصدی از کارمزد معاملات دوستانتون رو براتون به همراه داره.
👇
لینک نصب:
https://payval.me/app/Login?ref=8RP9NPH8
شاد و پرروزی باشید
🌱</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/693434" target="_blank">📅 17:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693433">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سهم سالمندان ایران تا سال ۱۴۳۰ بیش از دو برابر می‌شود
رئیس گروه بهداشت سالمندان وزارت بهداشت:
🔹
اکنون بیش از ۱۰ میلیون نفر، معادل حدود ۱۲ درصد جمعیت ایران، سالمند هستند و پیش‌بینی می‌شود این سهم تا سال ۱۴۳۰ به بیش از ۲۶ درصد برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693433" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693432">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835e710b86.mp4?token=V51ciIzpCQj1vTVu7IWi-S1m0PHy5pYESgnBNYVyS8diImRf9fYngA8lOVtTI_MWir5OGmYWX-BA_FGQlyAIIx500VPh_excBVva90EfhDo1QRT1qvTSWV-MkPW_-CzgonXgIglyE1YLFzPKlmhljearZyu1V6zoMWTDRXnT0xA4MFE9HUw8ZZMLCuHEDdLl7az2pkhksbDARtPKQhhF9YTwo-WbfuNm3idipEHKy3YkawdxCop3iA82i2NgkAiv6vR11H91BHBlUmYfq7EGRqncGGDgV_LUm_9Ho28OyWkt8UoGfv062zLoF_o9OJbGxnTzSvtjdXYvSkU6m2TVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835e710b86.mp4?token=V51ciIzpCQj1vTVu7IWi-S1m0PHy5pYESgnBNYVyS8diImRf9fYngA8lOVtTI_MWir5OGmYWX-BA_FGQlyAIIx500VPh_excBVva90EfhDo1QRT1qvTSWV-MkPW_-CzgonXgIglyE1YLFzPKlmhljearZyu1V6zoMWTDRXnT0xA4MFE9HUw8ZZMLCuHEDdLl7az2pkhksbDARtPKQhhF9YTwo-WbfuNm3idipEHKy3YkawdxCop3iA82i2NgkAiv6vR11H91BHBlUmYfq7EGRqncGGDgV_LUm_9Ho28OyWkt8UoGfv062zLoF_o9OJbGxnTzSvtjdXYvSkU6m2TVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خراتیان: رهبر شهید چند روز بعد اتفاقات ۱۸ و ۱۹ دی ، احتمال جنگ رو قطعی میدونستن و نامه ای به ترامپ نوشتند مبنی بر اینکه این جنگ بسیار بزرگ خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693432" target="_blank">📅 17:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693431">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کاریال متعلق به دشمن سعودی در استان حجه سرنگون شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/693431" target="_blank">📅 17:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693430">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای سفیر عراق در تهران: بغداد برای بازگرداندن پروازهای میان دو کشور به وضعیت عادی، رایزنی‌ها و تماس‌های فشرده‌ای را ادامه می‌دهد و توقف پروازها را موقت و گذرا دانست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/693430" target="_blank">📅 17:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrNUqN-ng4txma2gd6bgZ_aMUhzHxlL-5ZuZpqSfVeAG3MS8Gf42UP0Qsv2PWMS8odhdDv0EUXTjEfccPq4Mxu55G9FG6pnm4S5_2KFv8UVR8Js61T8-9p6n1jojxnFtWS3L9AGuoCE2VcEyKs4COgyzGImRhtqTmUwJRaXet2cKl4QL16pNxh9QstnloiNbi-K9Bi1mKV0hF6NIRMM7ZJByCrkwF1Qevhy2l4ZJ2isgw1_TuspiF5dVdrhekVvwGnusJSXVXDREDlfKpLgQ5UPZBMK8JwHNQ5iCJGJGC4wNOutpG94veKsCy4VYyAagCCNIjNkQWsvfIsY1af2biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXpALR7C1AkvcBMPTAUldcCFd_SH0DYnPavGeaqlYOGm8I5sQHNVpzjwhEiO06y5F0z9xTGdt3sjEdD23aGXCZrZkXScBV2RMDXdKGVm-MjbbZ-KHlMrD8B_txjfD-JwEInYwfoPOuxof97NEp_ptm2QrgOyMC8icTcG7q2v-WOXpY9kf2UiCssqsQKwshaWCi2IFih_qLi1fwpha87iy3cFe3QwEC9pQcHctXBjru1HNrwDFRWg5rkik1ARtVYVdqmNlGzZl-5LPAWCDr2Ac7jDz-SHiaexFWzipl9FAPCoKnFrA5UxdCjL1CDD-q2fc38npEKb6cQmZfLv9ViNIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قارچ
زرد کیجا
🔹
این ایام در جنگل‌های مازندران، وقت چیدن «زرد کیجا» یا گوشِک، یکی از خوشمزه‌ترین و لذیذترین قارچ‌های دنیاست که ارزش غذایی بالایی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693428" target="_blank">📅 16:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
این ویدیو مطلبی مخصوص کساییه که همزمان چندتا کار رو با هم انجام میدن؛ اگه شما هم از این مدل آدم‌ها هستید که چندتا کار رو با هم پیش می‌برید، حتماً این ویدیو رو ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/693427" target="_blank">📅 16:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJqAt_FtNe_nLOHFyjHIbZ_NxbdAUuo8JGiTWdjIO8X6f04Nro7KcTt8ul8H9_XxsMyILVXiEvpGu1v0pNVS999dt87pe1h64B7I-BxT8KneBO4Y9i5G77dKWkw-uyeTgZFr-zfgRgj1p1OpCyuHBVqeaAfre6ymaH-pVTzGg54K21on25rwaqb68_BGVTpelA9xQYQoNjjEQ20oG8bOCUArIFwjbiT-LLznGZChi6-GhatUwX-9j0G_RgVJv7wiOnn2OJcTA_H8y59eScdzdq5baI0vGfL06bvFKQlxfiQL0ZUH6I74MKvMJ9hMR-kANtKS-kvGDZNVg-FmnweGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از انتخابات آمریکا "جنگ بزرگ" رخ می‌دهد؟
🔹
برخی تحلیلگران معتقدند که نزدیکی انتخابات میان‌دوره‌ای، یکی از عوامل کلیدی در توقف موقت تشدید تنش‌های نظامی بوده و ترامپ ممکن است تصمیم به قول خودش مهم درباره ایران را تا پس از انتخابات میان‌دوره‌ای به تعویق بیندازد.
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3248205</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693426" target="_blank">📅 16:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvD4BnAhmag0KdkODtistNm02G3oZqxsLEtLNykgcQcpk5jJ7mby9rX1Dmo_F2sXeR66KMsQHgoHQOg-kOjn3UeyH8EkrbaPg8n7BNkASFKo_y2Yy9yXhk1IFvjuUQwsz0-9ERczp7WEET5NoxYHSj5VZCp3lqRQLC5N6JBCxAFVFuH-5F-_koSWsfgX2Pdo-YMf0OjcIT-jG-olEVan_nsLFwnRjzngHmqIOekII9lnt61h7TtnU-bMBctDOS5hH9Kq8NObrYDc9gYY5qCmZiFMViiYTyNqb5ac0hKlK5ZQhMzTDteq9e8iRrgKrAoK6WRoMRioxWpU4sj-DnYAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بیت‌کوین به ۲۰ میلیارد تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693425" target="_blank">📅 16:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رئیس انجمن موبایل: با توقف پروازهای عمان، گوشی وارد کشور نمی‌شود/ بالای ۹۰ درصد موبایل مورد نیاز کشور از مسیر هوایی وارد می‌شود و بخش مهمی از این مسیر از دبی به عمان و سپس به ایران بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/693424" target="_blank">📅 16:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: به‌ محض اینکه ایران تسلیم شود، قیمت نفت به‌شدت کاهش خواهد یافت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/693423" target="_blank">📅 16:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: دیشب، ما مقدار بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از میزان نفتی که قبل از جنگ از این منطقه خارج می‌کردیم
🔹
قیمت نفت الان از دوران دولت بایدن کمتر است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/693422" target="_blank">📅 16:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1zwZm47Tb8dfl7TvQ2Duk8yyYlgw09fxCSEubbONFy_wo5yFo5FHYZfqWLxR_1ZV0FHRXXTdPKhTboxNIbVbDSAkOa3CncZ8wlhosvV6zT1JE43aCaOZO1bUrwY6hTjZEQb_3-b4BR0EuK97HQfoi1vONTZhOIsywtjCzS_MH7d3t7wXpZLTRRSIQYOWgbtQo76c_7J4KY02sJvkUfR9bzHmblgSTuy8tNfe8ex1Wdsmk0DGAE2li_hLvvHNBrdK25_XcoI-45TzP-fcNd5mgq3RxED-SyRni92UCOZeM3lNhuvUA3yXaMvele9PGkR5Z5rtik0sRyqC5n3668tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاطمه معتمدآریا پس از دو سال دوری، طی چند روز اخیر به ایران بازگشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/693421" target="_blank">📅 16:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211153c224.mp4?token=etUDN4pxXC-v8yhau1QCl4VwGubeLtiF4MAZE5pIG890H2Rb7W8ylPi_sKxlB7-6sNYv1daTzwL0L_fQ_b4OgTt4RIcE_uuGZhnS45nLGjT1WmoUKy4Rl3HNtlYqUtyuelAq3z7HHzGg01XWhk3VAY46b1gNtjq6N0G2HSd8zhyiUPET0oTE6A1ZJsdgE73iljoq35eM2RiHaYoXtpgy1zoBNxePs2MdeE4O54WcVfsNgL4GhLoQxeFW5jkDJSzpPj2hZnpFZTiFABbSvM1Hv8ls4ztdlUEKfN_c7ucPWxFbdI2prsnwHw_OxZrrXE3lFXCPXeN0yHRjbD8hut-2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211153c224.mp4?token=etUDN4pxXC-v8yhau1QCl4VwGubeLtiF4MAZE5pIG890H2Rb7W8ylPi_sKxlB7-6sNYv1daTzwL0L_fQ_b4OgTt4RIcE_uuGZhnS45nLGjT1WmoUKy4Rl3HNtlYqUtyuelAq3z7HHzGg01XWhk3VAY46b1gNtjq6N0G2HSd8zhyiUPET0oTE6A1ZJsdgE73iljoq35eM2RiHaYoXtpgy1zoBNxePs2MdeE4O54WcVfsNgL4GhLoQxeFW5jkDJSzpPj2hZnpFZTiFABbSvM1Hv8ls4ztdlUEKfN_c7ucPWxFbdI2prsnwHw_OxZrrXE3lFXCPXeN0yHRjbD8hut-2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیارشور فوری و خونگی؛ با این روش، چند ساعت بعد آماده‌ست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693420" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بانک مرکزی ادعای میلی را تکذیب کرد
🔹
در پی انتشار نامه‌ای از سوی یکی از پلتفرم‌های آنلاین خرید و فروش طلا با محتوای «رفع موانع دسترسی به دارایی‌های خود و آزادسازی طلای موجود در خزانه‌های بانکی»، بانک مرکزی اعلام کرد:
۱. برخلاف ادعاها و جوسازی‌های صورت گرفته در برخی کانال‌های شبکه‌های اجتماعی، در نامه مورد اشاره هیچ نام، درخواست مستقیم یا ادعایی خطاب به بانک مرکزی جمهوری اسلامی ایران مطرح نشده است.
۲. مطلب منتشر شده در فضای مجازی، در راستای انحراف افکار عمومی و القای اخبار کذب و خلاف واقع به بانک مرکزی تنظیم شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693419" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کاریال متعلق به دشمن سعودی در استان حجه سرنگون شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/693418" target="_blank">📅 16:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس از تصویب ماده پایانی طرح تنگه هرمز و تعیین این قانون به‌عنوان مبنای نظام حاکم بر این محدوده خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693417" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نقشه دشمن برای قطع بنزین تهران و شمال کشور در ۷۲ ساعت خنثی شد
معاون وزیر نفت:
🔹
دشمن با هدف قرار دادن تلمبه‌خانه‌ها و انبارهای نفت تهران و البرز، به‌ دنبال قطع روزانه ۹۰ میلیون لیتر انتقال فرآورده و از کار انداختن شبکه توزیع سوخت در نوار شمالی کشور ظرف ۷۲ ساعت بود؛ با تغییر آرایش خطوط لوله و اعزام هزاران نفتکش، این طرح خنثی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/693416" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32ddb527e.mp4?token=eY_uY_xhmfk_ZdvPXqpBLU60StTmeI258I3xvfTWmNhRE2TJkwdKilEISs8DZYoxMZhR074r5PTR2n2VT5-72UhU_ownIb_n6-WEFXZ9z-t0Nn1ioFv5koluD-L1LfPl77jBF6ZMttonm-sdmXxsiJeaspMJbC0dtTbozCD-yIpwNDHY7OiJBVhdKh8s-16ZxWvoO-5wi-Kih3qsu9hQy3cIWNkd7Hw42Bd6QtdYlEI0KHjBE1Xs6ErX2sflXu8-jIqPymMtg81luaJOyatptes0rlSsGanU4RR9MtbZgRooeDTzlbqY-7D7_pl9vQfluH5Pibe5aWSlfmnJieK1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32ddb527e.mp4?token=eY_uY_xhmfk_ZdvPXqpBLU60StTmeI258I3xvfTWmNhRE2TJkwdKilEISs8DZYoxMZhR074r5PTR2n2VT5-72UhU_ownIb_n6-WEFXZ9z-t0Nn1ioFv5koluD-L1LfPl77jBF6ZMttonm-sdmXxsiJeaspMJbC0dtTbozCD-yIpwNDHY7OiJBVhdKh8s-16ZxWvoO-5wi-Kih3qsu9hQy3cIWNkd7Hw42Bd6QtdYlEI0KHjBE1Xs6ErX2sflXu8-jIqPymMtg81luaJOyatptes0rlSsGanU4RR9MtbZgRooeDTzlbqY-7D7_pl9vQfluH5Pibe5aWSlfmnJieK1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلب ترحم با گریه بچه؛ وقتی مادر کودک را به عمد می‌زند تا با گریه او، پول بیشتری کاسب شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/693414" target="_blank">📅 16:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df514f4855.mp4?token=TtIBSrV3G4AP5M7ZFheBPo9ngBXQ6q7y4orTx7CCXfySjC0c39oLBHhCYJRNdf9OcsheTzJgCddHxYkEly2PzsMrfFP1fSAGARRPvJWNUt6m1LQrWBmzuWziZPm6MBjrMTwXXM80RzLQFlypP-eCuHaTzNm4ZxBUIwpKcEstNC5Iwm0ClhcjqEgL5zxmfwBFLin1BM5xiySc5hMTTTdb59CwWqGMwRvghEvXAeUiXy5OzP7C5QPxG5CfRQIg8Vf8a6rRnCI7VvmOr1fMZVtZ1uRY3pDUNLyCCqaP32a0zrCJKjy1O9jA9Q7D0_3prZKG8WxVH57SgwfvMNebXuLb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df514f4855.mp4?token=TtIBSrV3G4AP5M7ZFheBPo9ngBXQ6q7y4orTx7CCXfySjC0c39oLBHhCYJRNdf9OcsheTzJgCddHxYkEly2PzsMrfFP1fSAGARRPvJWNUt6m1LQrWBmzuWziZPm6MBjrMTwXXM80RzLQFlypP-eCuHaTzNm4ZxBUIwpKcEstNC5Iwm0ClhcjqEgL5zxmfwBFLin1BM5xiySc5hMTTTdb59CwWqGMwRvghEvXAeUiXy5OzP7C5QPxG5CfRQIg8Vf8a6rRnCI7VvmOr1fMZVtZ1uRY3pDUNLyCCqaP32a0zrCJKjy1O9jA9Q7D0_3prZKG8WxVH57SgwfvMNebXuLb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثروتمندترین خانواده‌ها چه‌طور بچه‌هاشون رو تربیت مالی می‌کنن؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/693413" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfd3010.mp4?token=a15MlH7cVSH1wHeJcVNeYHryNAlgFUNwyW1j0iWl6_e1ZbFHA3FIQ1tEDcRRTeHzRKKmfDpQfuSSpB_5EVOWBmym4xAdVT4F_ULbMI_w2sjNsDnIRUVAzsdwmB7LMNYb8gyVcP8RyV65CLybGma0yFdDsk5_0-gJ2YEL0rurZKgvKZ6CNsJP0cacHtKj228iGUNFPYAzF3on4DUT4Y3lKC6kEJIi6R-j-V5dLBhBwSvrPgdkqC70aouNpr11zkFxZ7q5Nfz0u90zVB-qs8cnaEZU0XRHHEAnxo-C3aaFVcudPPKNOZYwLoVb5FgHQk_PzVkdmYMXqGwhnwP0axgmCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfd3010.mp4?token=a15MlH7cVSH1wHeJcVNeYHryNAlgFUNwyW1j0iWl6_e1ZbFHA3FIQ1tEDcRRTeHzRKKmfDpQfuSSpB_5EVOWBmym4xAdVT4F_ULbMI_w2sjNsDnIRUVAzsdwmB7LMNYb8gyVcP8RyV65CLybGma0yFdDsk5_0-gJ2YEL0rurZKgvKZ6CNsJP0cacHtKj228iGUNFPYAzF3on4DUT4Y3lKC6kEJIi6R-j-V5dLBhBwSvrPgdkqC70aouNpr11zkFxZ7q5Nfz0u90zVB-qs8cnaEZU0XRHHEAnxo-C3aaFVcudPPKNOZYwLoVb5FgHQk_PzVkdmYMXqGwhnwP0axgmCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تابستان را با همدلی شما گذراندیم
🌨
در سرمای زمستان هم دلگرم به قرارمان هستیم....
قرارمان برقرار است.
#مدیریت_مصرف
|
#قرار_همدلی
|
#توزیع_برق_استان_تهران</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693412" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ناخدا هوشنگ صمدی: تکاور اسیر ندارد، گلوله آخر سهم خودش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/693411" target="_blank">📅 15:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
وزیر دارایی اسرائیل: ما باید در کرانه باختری وارد جنگ شویم. باید در کرانه باختری همان کاری را انجام دهیم که در غزه انجام دادیم
/
می‌خواهم همه تروریست‌ها را بکشیم و همه سلاح‌ها را جمع‌آوری کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693409" target="_blank">📅 15:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسه مجلس: مهلت ۴۵ روزه دولت برای معرفی وزرای اطلاعات و دفاع به پایان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693408" target="_blank">📅 15:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff1136501.mp4?token=SZemnTFtynKdgvxG0WkpdbktUH6l6AnzPg5QeIvUsST3gavuesAsUGy3G9-7XrSwZCxjxM8Vvn74qA8kqTRsxv7WsZmgWYpSeqGK0ZMBFURbshVZzU_cgXBdlpn2v-YWYN5K9pWz0enw5Hn4UPwLBUfIOQCT6WmWP_eqDkoiwWV39wW2prZ3gSv29rWt7XdNQNDG6z1oS4igjqaSJOu5kiAZx5Hw5e5icD8iR8RURL5xkksccnUWrRXy6AyxRK5cA0t4klpuWjLOIzQxHcrPrWjlLXd5Tsid1LwUstgO5ZJYSYCDxR7VtYqNP6GvSnaj3oTXLwPbBlLVQV-hAySiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff1136501.mp4?token=SZemnTFtynKdgvxG0WkpdbktUH6l6AnzPg5QeIvUsST3gavuesAsUGy3G9-7XrSwZCxjxM8Vvn74qA8kqTRsxv7WsZmgWYpSeqGK0ZMBFURbshVZzU_cgXBdlpn2v-YWYN5K9pWz0enw5Hn4UPwLBUfIOQCT6WmWP_eqDkoiwWV39wW2prZ3gSv29rWt7XdNQNDG6z1oS4igjqaSJOu5kiAZx5Hw5e5icD8iR8RURL5xkksccnUWrRXy6AyxRK5cA0t4klpuWjLOIzQxHcrPrWjlLXd5Tsid1LwUstgO5ZJYSYCDxR7VtYqNP6GvSnaj3oTXLwPbBlLVQV-hAySiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گام تازه دانشمندان ژاپنی برای حذف کروموزوم اضافی سندروم داون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/693407" target="_blank">📅 15:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDv17Nn-kPHniNgS6IijfEViIN0N3piyph6Q-RSVMPwxjIrdEVHUmK3uJw2fWTm93obqLv80B2IdCKCJ6oc5e4l1D5PcfSrAN22hAYYKIqugb49_w3bEaSqMTtZgM2jvehMkgzUQAwgQISDAnx7fl2cidZIAGFsfL9AsjiX8FrOHSgMy9UuDy55aAhdImvk7hMW65_P5rWUgDIElFuKV7IvGu6ZcwuXWdLf2KFWLFZrTJftvWxEby43HeTvP1ARAgkbQGpvhmvUjFxcpVsMkCahUip93xZCA93EU6uN75_EWqYyIB7_bDhCg9DeRAwobnopd0WKVIvo3fXKhpooXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرعلی اکبری از MMA خداحافظی می‌کند
🔹
علیرضا استکی از قصد امیرعلی اکبری برای خداحافظی با رشته MMA در آینده نزدیک خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693406" target="_blank">📅 15:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33bfb381a.mp4?token=s8DwPnHjfkUB5oiY5y3tdltxvvd5mynz2Hg62Z8vqV4D_ye_4mndOnk4ljJ8mneit7V0B10_hOOi2uJGMfHC-YcTqVFLnVO3hsVSJH7Y3zPALWry46enClzZY545Oopr8oJeLKWHH4GHTsP-PafQ4jy_P5cFvILddOKJ1dgeDXjF5saV47BPoN6XL7fJmm9mviywb5uCztTmjY7-rq87s-5gh6sUsF0kJIu1MKlHchlffLS_rEXj_0nAGXuWmb3oIX6zvSRYSaM2TNuAb6AtNWVPuS5atySmY_jfLQPNAFQt1ewVga-LMlcSgkukEMP-FgMbabt_67ImX71AymKUtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33bfb381a.mp4?token=s8DwPnHjfkUB5oiY5y3tdltxvvd5mynz2Hg62Z8vqV4D_ye_4mndOnk4ljJ8mneit7V0B10_hOOi2uJGMfHC-YcTqVFLnVO3hsVSJH7Y3zPALWry46enClzZY545Oopr8oJeLKWHH4GHTsP-PafQ4jy_P5cFvILddOKJ1dgeDXjF5saV47BPoN6XL7fJmm9mviywb5uCztTmjY7-rq87s-5gh6sUsF0kJIu1MKlHchlffLS_rEXj_0nAGXuWmb3oIX6zvSRYSaM2TNuAb6AtNWVPuS5atySmY_jfLQPNAFQt1ewVga-LMlcSgkukEMP-FgMbabt_67ImX71AymKUtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا از پل ورسک در میان مه و خزان پاییز
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693405" target="_blank">📅 15:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b8447922.mp4?token=GbA-lTFQMk8Iyf5C_DambYyYhdIgSnbQvvH3PcZ3g4vTMPr4A8uNBbemK0LNWRAv3b80LRRjfACxeZ5bybB8k5TSOfiLacscwLzbMDQYeNUfVTDOfh41IL5K1i9Bq85eaRvWs00U8pFlb22I5kOs3jKH8oXBHS7y0jT384pTEGqaYAprZ1kDyjfkFEdCyY6jchNNkuyFa7M_a6ZcijCiqCSDcJNUIOtd1TTm46TtXXkEDIzh-w2oDa4L_HaVCiOG1BlGdq3udmtzOVXHDnq64h0fLdFWg8oN49L-cziiDRtIwhSkyiF6WH5-6wFVmdfjlZHSiJmzkodsP9Jb0EwGww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b8447922.mp4?token=GbA-lTFQMk8Iyf5C_DambYyYhdIgSnbQvvH3PcZ3g4vTMPr4A8uNBbemK0LNWRAv3b80LRRjfACxeZ5bybB8k5TSOfiLacscwLzbMDQYeNUfVTDOfh41IL5K1i9Bq85eaRvWs00U8pFlb22I5kOs3jKH8oXBHS7y0jT384pTEGqaYAprZ1kDyjfkFEdCyY6jchNNkuyFa7M_a6ZcijCiqCSDcJNUIOtd1TTm46TtXXkEDIzh-w2oDa4L_HaVCiOG1BlGdq3udmtzOVXHDnq64h0fLdFWg8oN49L-cziiDRtIwhSkyiF6WH5-6wFVmdfjlZHSiJmzkodsP9Jb0EwGww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یا بودجه‌ بازسازی بدهید، یا مانع‌تراشی نکنید!
🔹
درباره واحدهای تخریب‌ شده در طول جنگ؛ اگر دولت تمکن مالی دارد، باید هزینه بازسازی واحد را مستقیماً بپردازد؛ اما اگر پولی در بساط نیست، به‌ جای حواله‌ دادن سازنده به تراکم‌های بلاتکلیف در سایر مناطق، باید با اعطای تراکم در همان ملک، پای سرمایه‌گذار را به میدان باز کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/693403" target="_blank">📅 15:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeFYyVAP9YCAbVEIuM2wI9i-oqgerXyWdCLYWu38qNAc5z2b3EHCUukSttyQMm0ye3sl-VWrBmJ2Uc6IVS1XpmmA6TAD-S23885ii3oREiMhJvMc1Cpmhoi2Btv5b5t9oSyvgggw8ylt0FtyDv-Pd4qsKOTEqzI4Sqlkt0FgchdmpBWP4AsNENYSEf31Ds1Ijebwkt0wd7J2dy4I0SvzwJ6cNWKbH_bkHQIZ7SwmHgnrA6V8V4VM5p9YsB6CcauyaJos1x8ANvPkruts8JEnLtjUOaTHcb5BHyrlIogZDB9-4iW5PuD8TX0Uj6kLMb80g409tsu4jBvHyPglyXckPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون برنامه و بودجه مجلس: مسدودسازی پلتفرم‌ها راه‌حل مشکلات اقتصادی نیست
بهروز محبی‌ نجم‌آبادی، عضو کمیسیون برنامه، بودجه و محاسبات مجلس:
🔹
بهره‌برداری از فضای مجازی و تکنولوژی، از اهمیت بنیادینی برخوردار است و امروز تمامی کشورهایی که با نگاهی دانش‌بنیان به مسائل اقتصادی می‌نگرند، بر این حوزه تمرکز دارند.
🔹
این پلتفرم‌ها مشروط بر اینکه به‌صورت دقیق تعریف شده و دارای تأییدیه‌های لازم باشند، می‌توانند کارکرد مثبتی داشته باشند.
🔹
این پلتفرم‌ها یک فرصت هستند. مشخصات و چارچوب‌هایی که این بسترهای قانونی در بحث شفافیت و شناسایی عادلانه‌ فعالان درگاه‌ها دارند، قطعاً برای کسانی که از تسلط مناسب برخوردارند و با آموزش کافی وارد فضای مجازی می‌شوند، شرایط بهتری را نسبت به کسانی که شناخت کاملی از موضوع ندارند، فراهم خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/693402" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25b8c231d4.mp4?token=HMmPl-OO80ZSsxFHUKTXd9xiSv9fQb9-0TgTDEEtUJIXl3bQdlW3kdkN2NmI6Ju_WIgSKs20ru4zCDMgGOSwe3xvlzaDbvI1UgpDDps0AaMI8Krm6192XaE72Xt9w8ncVbn6SQgTw51WadBMQqt-g0DdyWLEZMUGUNlP-JIRhvOK4w-yF1HO_k_o5pPfI5WcmwGRkmcCMO1WeJfPnTWre7hXVmWZm4EywAqONVf6kuL76cmRQrdbbAygllSOiUGP_GKxksljbmEMOk1pqhk7hG4SVqf-3PxxpxpMjrTYZNX8YDh4Cj5S5-cJnQYa_d601_A9qx3hj-m-LbaIfbTTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25b8c231d4.mp4?token=HMmPl-OO80ZSsxFHUKTXd9xiSv9fQb9-0TgTDEEtUJIXl3bQdlW3kdkN2NmI6Ju_WIgSKs20ru4zCDMgGOSwe3xvlzaDbvI1UgpDDps0AaMI8Krm6192XaE72Xt9w8ncVbn6SQgTw51WadBMQqt-g0DdyWLEZMUGUNlP-JIRhvOK4w-yF1HO_k_o5pPfI5WcmwGRkmcCMO1WeJfPnTWre7hXVmWZm4EywAqONVf6kuL76cmRQrdbbAygllSOiUGP_GKxksljbmEMOk1pqhk7hG4SVqf-3PxxpxpMjrTYZNX8YDh4Cj5S5-cJnQYa_d601_A9qx3hj-m-LbaIfbTTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای مسلح ایران طی ۲ شب اخیر با کشتی‌هایی که قصد عبور از مسیرهای غیرمجاز در تنگه هرمز را داشتند، برخورد کرده‌اند. شب گذشته ۷ کشتی و شب پیش از آن ۱۲ کشتی متخلف هدف قرار گرفته‌اند
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/693401" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1027a78d5.mp4?token=Yj7ZMOgJdl6dg9iK8swoeWM4gYHO5H7IOZ9PuP_49Tyk6PBlned8M1sMV8hSq02XOnPdE76WReDQfIcGFdWjNLjFZ8pGOORNeBQQNvbteKh8aDAZnh8ITnbGwRdSAMJswdI9bRwP93-2IrEHDsCaMElJHTjlYnSly2dyJusIe-qlv4J-WTPoue0ab-GCBxWW_ovt9ms3nS0xHqrgtb_WC2hRlbV-Mw5EX5VKd5_GP8Mo8YPuwlIm_3Wqi50JEqOi94doCNi3khDD603b_2taeWMR1tQXfu8-2Ku-G9YJw6-3_g-qvN60FXDVIavQSlD6MsspwkyPmhjZlr4_RIT7vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1027a78d5.mp4?token=Yj7ZMOgJdl6dg9iK8swoeWM4gYHO5H7IOZ9PuP_49Tyk6PBlned8M1sMV8hSq02XOnPdE76WReDQfIcGFdWjNLjFZ8pGOORNeBQQNvbteKh8aDAZnh8ITnbGwRdSAMJswdI9bRwP93-2IrEHDsCaMElJHTjlYnSly2dyJusIe-qlv4J-WTPoue0ab-GCBxWW_ovt9ms3nS0xHqrgtb_WC2hRlbV-Mw5EX5VKd5_GP8Mo8YPuwlIm_3Wqi50JEqOi94doCNi3khDD603b_2taeWMR1tQXfu8-2Ku-G9YJw6-3_g-qvN60FXDVIavQSlD6MsspwkyPmhjZlr4_RIT7vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک‌ لیست کامل از اسم داروها و نوع کاربردشون که مطئنم نداشتید؛ یادتون باشه قبل از استفاده حتما با پزشک مشورت کنید #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693400" target="_blank">📅 15:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: یک نقص جدید در هواپیماهای جنجالی بوئینگ ۷۳۷ وجود دارد
⠀
🔹
روزنامه وال‌استریت ژورنال براساس اسناد شرکت بوئینگ، نقص نرم‌افزاری اعلام نشده هواپیماهای سری ۷۳۷ مکس را گزارش داد که می‌تواند هنگام فرود ایجاد اختلال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/693399" target="_blank">📅 15:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: یک میلیون اثر تاریخی داریم، آمریکا چند اثر تاریخی دارد؟/ آن‌وقت آنها می‌خواهند ما را با این سابقه تمدنی و آثار تاریخی محو کنند!
🔹
پزشکیان: اگر منِ مسئول جرات می‌کنم که با قدرت و با صلابت حرف بزنم به پشتوانه مردم بزرگوار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/693398" target="_blank">📅 14:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq1xzzRk_fRYTZBxhCZFBeVQaPC7pm_ruYvzKJLbkgf3bYJDYct6MGAuGyiIy7DxWNGbCdNW14_9ScpPkLD8X0JG5cmSvewEfL9-wevfRqlQp_VUtGsR72D8ipOHC8K3lpgYpj0-vH-r-PjGq5jcca9mdbra0peHqNCnZxU8ivjFtKUW4N1BlmYw3N4f2A6eReVpzpPT7RGFUUGxr1VpOxuaMwvWGwjQ3MaRnIl50NBTv8pxSqq5QF80shIP4tOWlCe4dyV2RGwHCEutUcjvro6wqMktVmgv3EtffZ0xCdZtMgOHS0Rr5G9yd9eX96qKpMWjIfO3oKz2161Vc7_QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه قالیباف به پزشکیان؛ تمدید مهلت‌های اضطرار توسط دولت غیرقانونی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/693397" target="_blank">📅 14:55 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
