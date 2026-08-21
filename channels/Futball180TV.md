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
<img src="https://cdn5.telesco.pe/file/tGKA_1fIUwtE_N75AS6nupdyrJk8ihfj_FhsV7x6d-QxdO4PRlAfwsAyg812whAyLjzmFJxXdGfqzKpgPqCDjRY0JpyCICx1fGn4eJLuaUqzAFTEifLeROp-MkgrBjE2bBlN4BoCg6hoB3VYGAGGznB7m_-tCZXuaFPANLKhdTemIT38YTIlNhSQLdSQTwGRXcBIA3L6DGZ-dcaFK4dAZY4ZuklLdlYzsJ2fQr6EfFwH34lObwxqWaQm94XcX5e48crjhmRpvdOryu-sXck9tg9B9LyOQrnN7UBe7xjHRWCWkhf8iySeWFvbzBTfzTa2g4HuZPhni6O37RCokmC4Jg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 452K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 19:54:27</div>
<hr>

<div class="tg-post" id="msg-104315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
Premier Legaue is Back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/Futball180TV/104315" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Koe04OvAPNN9b0xT5lmhFqxTLKaX0aeocqXYEK80c9_FFGkMS_UKB1uPDMERApOMZx4yYaM6BRWZiWkY0D_IA1ydKOchUuuB50q6acOvIkn7dcTfvTu_Xa1Fi_a_oR8fSgNjU4EXfqjZQaNalb_jcvgfcpFhrdjEQ2d6GL736WbB62wAtL9kJ5BkmwOVBK8YiX9kL_PoKKV0BnIFjE4KpZSfoGR-8PaAicujOcd0s6PXqrWajKyb2Mi1Xj3KzWcY2cGxB-1CiYfh8GWpBXQtlDh0tW2pvSNA4CllvaXJdmr50lenMjhPtgA3CG_Nx2t3HiPh-34xj4scJkXAx1w6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ قرارداد رودری ستاره جدید باشگاه بارسلونا در لالیگا ثبت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/104312" target="_blank">📅 18:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👀
🤯
یکی از سخت‌ترین مسیرهای مانع جهان ملقب به «Obstacle Course Racing» به اختصار OCR
🔻
ایدا ماتیلده، ورزشکار حرفه‌ای این رشته، وارد مسیری می‌شود که برای عبور از آن فقط قدرت بدنی کافی نیست.
🔻
بالا رفتن، پرش، آویزان ماندن، حفظ تعادل و عبور سریع از موانع مختلف؛ هر بخش، ترکیبی متفاوت از قدرت، استقامت، چابکی و کنترل بدن را به چالش می‌کشد.
🔻
مسابقات عبور از موانع، رشته‌ای است که ورزشکار باید مجموعه‌ای از موانع فیزیکی را در سریع‌ترین زمان ممکن پشت سر بگذارد.
🔻
بعضی از این مسیرها آن‌قدر دشوار طراحی می‌شوند که حتی ورزشکاران حرفه‌ای را هم به مرز توانایی‌هایشان می‌رسانند.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/104311" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/Futball180TV/104310" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104309" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/Futball180TV/104309" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlgM1fK7c_C_E6EqbICgZdrllfzRct5zvw9d-Ob_Ud0v32dQ2at3ywThfjE3089S0Pn3FU0ZTkPpa7rGSq7MBnUDqLsQ_wIEk5zfLBm5ZYKg-T1iFiLy4DnYGgLZhWl8WdZA0XWnUhEm_SO0_fL4EmbKwYvugkII7QbTiFdlr-pKSRAJUo7K1w4j_YZHu_rzpXM0-A-CBFrmKWhR5mjhDsybRolTCWBc7WtUsXgJnE6j_VXb4uE09gkuFIuwJ_o1kthwmcjgq_zIl_YMaC3UzF-GoMcpJSrK4Wz4bOy25L_7bcfXQF8965NiFc9bMxduMCM1yLkzzkaM6c_3tnoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ باشگاه سپاهان اعلام کرد که سعید واسعی و امید نورافکن بدلیل مصدومیت دیدار روز یکشنبه مقابل استقلال را از دست می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/104308" target="_blank">📅 18:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHl5FWd9A3AUHOEvdqa5ikHwrRUdrpeUlAXtRx3GNkP8RYLRhkH3kVPkSkjdNoJXftbwp-x2Zmt4IYhLz69qCzmxCUrSAmKyxGhIHrgNYcOAKRh_I8XVQ0eCZRIMbZKrtKT0dYlnMy8lLCFWqt9IZ8HO9SqE8gK-Zp7jHEAOcYjlKrfp7RNpW69WYjm42jKvPrXjaPPtCUcmSx175RpKiUcwehXZ0UGsiUb5WYoPvo7m7sgoyUCvY4lI2ADuOjAX6GrK3mOCuFVyuUwEGg2ULJNfO3VMsKuUbRgwPTKYyAxQeiRGvV_kX4COBri_Xef_nouNOimPRX5CKz5j3nid4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇵🇹
نیمکت‌نشین رونالدو در بازی امروز النصر مقابل الریاض در هفته‌دوم لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/104307" target="_blank">📅 18:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0cDz9HqXghiPMXWBrdDlz32_jE73RlsrF35k12DWeS1yO5oJIyXxdZpbU8JsKcuOKZclyKSyOCQc3tVWpKwyxR3_Cp3IGmf0_0qn2d0Xolr2uAlRxDpCicYRV8OpYJ0lmhRpX1Vcw5jgkV9gyDfl115R4bEgJAHOVAsvBWTVA_35XGYkeUh7i9VPmktV1ZJGwrmUgfMSxLbq0tVgJirnEKrf1BuDrhviRsPeDrT2IUj28Kzq0kQrjLXLRw7dCldJ1HR8Z8FLZbCvy5T5GNo29cu9bJAb9rWI1Knjm05DnH56CYdXxL0b43LTDWa2yydEPT357ApKFxTDa0LI6navA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
#فوووووری
؛ جرایم انضباطی فیفا پس از اتفاقات فینال جام‌جهانی فوتبال:
❌
لئاندرو پاردس: 10 مسابقه محروم شد
❌
مولینا: 7 مسابقه محروم شد
❌
گاوی و آلمادا: هر کدام 1 مسابقه محروم شدند
❌
فدراسیون فوتبال آرژانتین: ۳۲۰ هزار دلار جریمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/104306" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPZMrPNm_bC9NuM-YaSnLD3KqM7zUbuDKWN7pa7jMHh4hRKuS1QufcP3uYJkyhlQThEE9y2yQrgMbkS55GgcB_NPWCIcUcLKsKnxA-vj7McgheiZMS5i10J4vU4t-N57FDLkMjHqrNd25mEclgvz3lhSMwz8k6txoczc1Ndp5AwqoGsHF4NkR_HS91oWP-tPXjoLsPn72MyOCgGyNIA9tz8RDacJMnkGDCZFrerGCca4hZOlh3_nzXHSXSBFLTFqU0rganiiB_6T8fMgbKbNjlDk_NDR4cvuvJSZzIEQVg6nChrQUWY1xBPO0PkQDo-D0FP_-9oroJPt-9cyZDr24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست تیم‌فوتبال رئال‌مادرید برای دیدار فرداشب هفته‌دوم لالیگا مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104305" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOslcqUXwXuc6tASWAkncMLgwie6x_YAtefxZOFJGEjjOwu8HGS4ukZKzrtP7k9WpBq8qcrPTdI-XeMhMhxPIRlYWOqjAco9vNYhRM5cblXk_2BmjT0uZ9WJkMTdxYuxDxmGoxaDxMzzD79avj4FrSb1xfm4qnxo4Am-vFEjhkaesehdZFwgQSUqZ4bQOcd4AqqW7y4GX6flyA8Y-WOhMOMvs986KOknZtarEQ2GN-RVtEd1Bz8TDIfgN1IWvVRbwZ5IR2ywmy3h8GUSM7BBHFRQyjrn-MdImODvU0ZJVx0Z5YTQUCVhlI6E9EB01kL3wRNdps_PJ5MH5MNc2xguFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104304" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی توپ، داور را از بازی خارج کرد!
😳
🏐
🔻
در جریان یکی از مسابقات والیبال در سانتو دومینگو، توپ با شدت به صورت داور زن مسابقه برخورد کرد. ضربه به حدی بود که او دیگر قادر به ادامه داوری نبود و در ادامه، عوامل حاضر در سالن او را از زمین مسابقه خارج کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104303" target="_blank">📅 17:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
واقعیت‌های فوتبال امروز و‌ ۱۰۰ صدسال گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104302" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
بعضی‌وقتا دیدن اینجور مسابقاتی‌از فوتبال دیدن پریمیرلیگ ایران جذاب‌تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104301" target="_blank">📅 16:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
لیواکوویچ سنگربان تیم فوتبال فنرباغچه ترکیه به باشگاه بارسلونا   HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104300" target="_blank">📅 15:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEYuqkKFU1mNWEPZ0H9Q0i_T5_ANan2a7qLlI_k-HHVwO8ciBlktKvLZfIzlgr6-8uQmhWab69Z8j9orZR4ttIeMg7UPjCRdjXQC4s5Q7qkHLtvwTvdvmAiCbTtP9vAZ4z1Yq2LzZQpFZM5WiyLieFh5Xhhcabj2XlUi6fjK4IWTpoBmEpyVcTprQRz8ApvCV4K3z8oSKQM5puuo71lSh5-5fD0p5a6-Wr2Olp3LkIoMwh6RTgE9eZTI_Tyy1tZx93LtwRjN7C56Ny5cBjnPTXWeofz6E8-5ZqRJY8ygImjiWy23hYITy1YiYuvxw-ZHHv_-gzP10O1pvNu3GkE1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104299" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo9IXwcWGqE1dz5IOt39BI3J3WLSboPcCOlTSWKeBpTE4KkwI8OJbod0jCnNy5CEuK79D6qxUhy5AKK7lVkcj-4reWGAivUd-sFmvy1fbrk6HWMjHvJVRppVhRxklYuDudK1oLFgPSoOTlZXgm66C7PIimyn824wULVGb9xER5w6xoHS8M9Nd31VbNsyqtyYzY8_1a-6N1STXVj6dswTLBoZZIpuUGEHoJIlZsIDNxEdYZgQ2b3kZf2-vldRt1URFtmBUHlMN9t9y6SmWkpHZqxWw3XFTYF_nvBxhP2oTnyO8OigdRaJxS0AxozYeUF5ZeUTJriFJYWZZ-jxwYom9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری
از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104298" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa0_MWvx1tnGmg-OJKhmE5JzIDoy11DBPPC7CUhwJGOA2Tg96GmOzgTki642fEkSQOs5SqiF--7kpAGqGLvqFoAAWQUc7MItgFjA7QptkmNwDbdlngoXfbfroNu9APpLbXqWS2hzqo5oThezvci8k6_ZVezI5GZxvKgtFkP73IFyd4yoG8d_ZpyrM-zH1E7_SMxi9ewXTRPqX3xg8gugC5lLEnAcuvg-rdcI0mE-TZvqPglaojX0SfHEOVTvPesTaWezT7WXPesKRszsST21beMGclBQWeKWXznWX3N1IKdOnpf-an5FeM3JF4L4e4NwdkLwRjNiZXQYTYcTaxe6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد
:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104297" target="_blank">📅 15:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQxQFA7uAxytgp4A2dPm8ft8YxviL6Wcov3k_eunX6KIpJg3UfLqeXhrrDFRoBgz7eJTSOwEIb1ot-75D7YcTUTclMjo2Vbek8MvrU8wDkvHqxWVZcpiZNFuOXG3AL8q98X4iivAU53Gz1bCnMRpNwUZrN_iUfz8wqz-R3udrzGyR5iBx8B7YnIdpRNd4VjvwhaNfMJAT8l2QYNYQAjg1e0s84e-SezMR27a_aQsGXx1q3sf-KzmDT3qjMfYG9QwtSORRKVB6MAP1nCdMXxikJVZaNgekHh7AO1xQdQzVCzWzW7Givy1dQbzdE_NKoZz_arZd0IDnZ7v9jT0s3QE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میزان هزینه آرسنال برای بازیکنان خط دفاعی
🇳🇱
یورین تیمبر — 34 میلیون پوند
🇫🇷
ویلیام سالیبا — 27 میلیون پوند
🇧🇷
گابریل — 27 میلیون پوند
🇮🇹
ریکاردو کالافیوری — 34 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن وایت — 50 میلیون پوند
🇪🇸
کریستین موسکوئرا — 13 میلیون پوند
🇪🇨
پیرو هینکاپیه — 45 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ازری کونسا — 51 میلیون پوند
💸
🤯
🤯
مجموعا: 281 میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104296" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2JcnQpiGR0liBwcZvLD8DaxCP0cM88adcCo5evku5qPqkFRAm96JyQENvoDrk9SqTB1vjaDdpKpoIEDxd6mxDBOLGTaWtA8lwqH_9Pd3qM5FaowgPVLjqDGre6U7L4lH9TAszxzIrRM0anr7kcyAyBScqGRmwvsn75n6s7CO1JlxZ-SGGSKeL7Z4SsxpVoXZtPW9RQpxf7cQfTt85F52ppoTqmgmLnnHpZ7rhKFQ6S719WFASKyraaS3JZ5VVh7XFxPfxFVUw0xlGsRjzjpMszPVKSKqpUflkm7r1W8ntUSZI1QjpAJJrAh7gAUKwBnwg_pPuoBgK8-WJ2Ylntj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایشالا آلوارز تا ۴ سال آینده دووم بیاره
😂
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104295" target="_blank">📅 14:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=em8VlIhzZR2J0_34whmAaxALgDuXtVYBQpmCuao01499WaSpi_XOhbSI2zpqWIPCcDRg7FldlVxX3Le7KD962WLd9frKt5_fIj3X3ULsQd_iqbHQjGStCnH3fsd-hvcQ3PB5-fozVUxaW9D20X_d1RGzkMBezx_mr8Sm1YbTPb2LpH3YqZrDgxzMub4R9ZbSV932G0QaODyIn3hVjf_j91-24Sks4dQNPnsfQQ7N1YMNFsR_7_Pb9e29v8CUZgY5BrOcFhHsJ0XWTzU8ivsB3pbk-65pCDgfv-U2ZuGTzxWJD2_Zvro8duMIeLjnE590IpqKk0wtrmnv4MVW2gavYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=em8VlIhzZR2J0_34whmAaxALgDuXtVYBQpmCuao01499WaSpi_XOhbSI2zpqWIPCcDRg7FldlVxX3Le7KD962WLd9frKt5_fIj3X3ULsQd_iqbHQjGStCnH3fsd-hvcQ3PB5-fozVUxaW9D20X_d1RGzkMBezx_mr8Sm1YbTPb2LpH3YqZrDgxzMub4R9ZbSV932G0QaODyIn3hVjf_j91-24Sks4dQNPnsfQQ7N1YMNFsR_7_Pb9e29v8CUZgY5BrOcFhHsJ0XWTzU8ivsB3pbk-65pCDgfv-U2ZuGTzxWJD2_Zvro8duMIeLjnE590IpqKk0wtrmnv4MVW2gavYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وحشی‌بازی آرائوخو تو تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104294" target="_blank">📅 14:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btIxnPI8Y5ld12drGPwumdWJtilUkY5pEKqcR76xhhvd0i13bpjGOlqNZfk3g0njSdMrcOwiWvr0xO1qzo4tmNO6TcGH32IqnmeCHFEbxFKW77-pTvxKosLYZa4XOEfvWsOhhlCqfwDFPzXZyZ_2tov2kX6k9Hx392Y0Q2TSd2gBmA4LYiN66Fs2dPD_HMw3i3uSHXuDWoYdnJm7R5wjCHw0nT-7-c2LMZEydV7jL6vsU7DP-KDUDYsvLNeHlvgKYO_HrfUSuiooBeDtrhIMSbCs2V7XDIZW5V3ZE_Cuv0UEw3tHc_DCgs6m_i6dCZFT-D7_uZq6CWFrjqIXDGqddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🤯
تمام تیم‌هایی که ژائو کانسلو در اون بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104293" target="_blank">📅 14:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da3520408.mp4?token=GSoYYZhryGyg-r0GWgqiO14QUsrV5-819sR5xaUqoIiKcNy7CPwIvctHu2qdFGuuK256Sc8rkJAz3xCag0TxP3VMqEhqCfMxJ6LAyLEx9oTdJu84bQTR5KjO2Giir-LyHGRZhFh1DxYnNvi06dLh7FWJef7iaWJaVapgyPKQP2L62lUFHrbWCkRG8O8m3th-7QKrWkqv0mjWG4y65rVznkn0ZViCfh3nDvwYikacbosBzePVhaysJbr-xeSkWtMemPFC7JYWM0L--hDtkQsgBqzADdhGx1AsTIi-2ee_ZESOjCPIa1qad0y-lWhpWee7H6ac1B_LAFptzK-yHq4WVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da3520408.mp4?token=GSoYYZhryGyg-r0GWgqiO14QUsrV5-819sR5xaUqoIiKcNy7CPwIvctHu2qdFGuuK256Sc8rkJAz3xCag0TxP3VMqEhqCfMxJ6LAyLEx9oTdJu84bQTR5KjO2Giir-LyHGRZhFh1DxYnNvi06dLh7FWJef7iaWJaVapgyPKQP2L62lUFHrbWCkRG8O8m3th-7QKrWkqv0mjWG4y65rVznkn0ZViCfh3nDvwYikacbosBzePVhaysJbr-xeSkWtMemPFC7JYWM0L--hDtkQsgBqzADdhGx1AsTIi-2ee_ZESOjCPIa1qad0y-lWhpWee7H6ac1B_LAFptzK-yHq4WVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شباهت فوق‌العاده عجیب گل‌فصل‌گذشته علیپور‌ به سپاهان با گل این‌هفته حسین‌زاده به این تیم؛ فقط واکنش حسینی‌ رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104292" target="_blank">📅 13:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=eN1xzDrqxme4z9JWQZqCtAisDKF52HCGIK7TXs5D6wSRyfNwENfljdcKFyeNsjlsHd5lelKeyt7oR0O2Tv6Z5-HbBSc7mVeKFNP5DbrvUaRhssoeV43xYhqWoxRssf4Rge1mmIRctyCtoHcDnNTOcrLMupckVF8Syd3fZhgwhdLnMm6W9v3Xbi2s9BMn58mSmCOWOCh8Rmkx9wJIYcrnG8InG7TlnKNtxM04hrwBQae-6OXx0Rq9WjF7Nih5YUoZFQYVu66ta6_Elf8XcIDcqHfvJQEmR_-y52rzm0fJlgCuSzD6X1iZ2JdKSzeXB489xNUD93xmSYPWxe2AlPgq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=eN1xzDrqxme4z9JWQZqCtAisDKF52HCGIK7TXs5D6wSRyfNwENfljdcKFyeNsjlsHd5lelKeyt7oR0O2Tv6Z5-HbBSc7mVeKFNP5DbrvUaRhssoeV43xYhqWoxRssf4Rge1mmIRctyCtoHcDnNTOcrLMupckVF8Syd3fZhgwhdLnMm6W9v3Xbi2s9BMn58mSmCOWOCh8Rmkx9wJIYcrnG8InG7TlnKNtxM04hrwBQae-6OXx0Rq9WjF7Nih5YUoZFQYVu66ta6_Elf8XcIDcqHfvJQEmR_-y52rzm0fJlgCuSzD6X1iZ2JdKSzeXB489xNUD93xmSYPWxe2AlPgq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
هو شدن فرنکی‌دی‌یونگ توسط هواداران بارسا حین ورود به زمین در بازی جام خوان‌گمپر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104291" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POUIRd9o5PAS4xNhdiPLforT1Vt9tTuCtEwCgTaYvhsESRwHGrcQWS1Tjd_bkY9n1arrhexMvX9i_rQROngjdEKp2lVwlgPlvf27NpOjhd4vtpkDSLMUGw-LswLUHHbAXmaRtg7MU8QfaLBSN_MlVaQ9clxSJMD39GT3AoeALk-VDhhlg-qjifCruW-JIRsAeX1W_evmtqG6y9sEZb5J6q3WmM5RB1slHuwYRYJBV39LkdYugrseZhgTTpLvqKV9gbylhSGJb5XG4hJVwem9xeD3yMXtQY6Nkw7KdYzqd-BLORWmzbns95uqf7DcJkwBKKcZNqfbqzKYoPvTBLaXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
گستون‌ایدول خبرنگار مطرح آرژانتین: بارسلونا با اطرافیان لائوتارو صحبت کرده اما هنوز پیشنهاد رسمی نفرستاده. اینتر شدیدا برای موندن لائوتارو پافشاری میکنه چون در فاصله ۱۰ روز تا پایان نقل‌وانتقالات قرار نیست مهاجمی جذب کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104290" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kch7MkYvrZ-1Lu6CHjb4Ciue66PZGDdVkfoG-TrxYr-tTRSrNfHZAmj9qrDqW2KYOSM21S_XJdvqC95dfNoHZ0HHdz8EH2cmvoflie6qysQaHWMllXp-EIuNCqi3QO_SxAI4MR3q2FyRp36RCeBv7g4fcj2KwT2pTSKSd_1Z9IgIDvvENy81SCnO-yhE9f_pBVc37SNqUdaOd1xLTsDuqOiial3_6Mt0tC6Y9hJFM9DBZmcRxniq2_gt-hYer2Ns90SayD92X-_TU9agDTFmW6Weze5QVoy0knPJR6fIGnbZdM58C1vG10S5j9yiYG99k_7JNbShyWKkzBsP_9qwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104289" target="_blank">📅 12:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFD8sIA9iuzUuQBlRylvc4EJjlqMJoD59RE1iS1CSvFHCYlqMNyGVvb_cdTmAFHe7r1zuvME8IiYxlDn_oV9wR2OEoAePfgOXNGBpLQ_l2TPTY8bnvAuf00IwhzV46imp8q9uU0TYYOOF-nuZYYsR0YI-RxmpNLownCLIfkzwX4fFCPHBUHsMhAMNxvqZX7B_eZU6ewGbXTuGCfzniX1GRdPxUXMDgqEHJJnJyQ_iRUdSKgokJ7nyRJ_8Ga9fVW8CSi9iy_J8RP7k48c-TuE2Ky9Pfa1smdHkdQTwg9Q_UoNq-mlKgg_Vd-_qDOG2nwpQfqQg69C-SCDPdbLfczR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
👤
#فوووووری
؛ علیرضا بیرانوند در لیست تیم امید برای بازی‌های آسیایی ناگویا قرار نداره و طبق صحبت‌های سال گذشته نظام‌وظیفه، باید از روز اول مهرماه راهی سربازی بشه مگر اینکه اتفاق دیگه‌ای رخ بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104288" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iCKOAdSqSiJSfIy9KiGkcrSgUUszBti13Buh9eXaSe_41MjVZo92Jxnjt7k3tiuqoSUsc_ruePfLnCoySykkOiQEMEwQW2LOg1uVJEDzPACE85RgBIB-loLvS9qkPL1CpHNS2hX6io-tFPIZGUuiJrn56tGEkxMpLNYE8VfGnsP8KruXDR4F-6-QoJMnC_oFthjQVmzI1g8M6DdI2QuphUg_B8cLLaVa_SJkMfwqC8DUosMtJXXNEzWufpzajopz383mbgH4Istrw9IolgrR6yWZfFTjiUd1pATjior-mz7IxPF5Xx6pI16jOF2MDiC-31ZBhyDmn5W4WmDC7kDWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iCKOAdSqSiJSfIy9KiGkcrSgUUszBti13Buh9eXaSe_41MjVZo92Jxnjt7k3tiuqoSUsc_ruePfLnCoySykkOiQEMEwQW2LOg1uVJEDzPACE85RgBIB-loLvS9qkPL1CpHNS2hX6io-tFPIZGUuiJrn56tGEkxMpLNYE8VfGnsP8KruXDR4F-6-QoJMnC_oFthjQVmzI1g8M6DdI2QuphUg_B8cLLaVa_SJkMfwqC8DUosMtJXXNEzWufpzajopz383mbgH4Istrw9IolgrR6yWZfFTjiUd1pATjior-mz7IxPF5Xx6pI16jOF2MDiC-31ZBhyDmn5W4WmDC7kDWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
😐
شب گذشته در اقدامی عجیب، حراست سیتی سنتر خلیج فارس اهواز، با ادعای حفظ نظم، آرامش خانواده و جلوگیری از مزاحمت برای دختران، از ورود پسران مجرد به این مجموعه جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104287" target="_blank">📅 12:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9PHAs_dFukTD3UPgwSIC3yfCUEgnfl4F52gGvE8idq8Sult5vVNqKPHKfsDReMcx2WuqwlhCPNfqMRwVw6xbRTNaT_q3-L9B0LwiRzPtRHrq1QU0yFaOifL1H_SwYonaBdPE9g7DXwsB9Zk0yBt-Zqmy0-2axlAB_4xT3UW9vkQHNtrax6Z5iRc50fysGyrLFjLfTiPZCxtKZKiMTN1aAbkO-UXTyFjAYG6_-8ZeAXkqpeewGLjZJOP03JFFpARGwif2dPi71d-hzf25qMvuYfF8UcBn2gpurW7sIUEgpm2MH5xpFC7POpChRFitgTt-1ILoE5TnRKSnJ8zr0oxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2zPf1JI5ANy-61U3Ot7ufFX-EYy8gmrf_zZuyRmoMl6nsCO6MkY8hY0xGeTuPNV94t-Eiknvn0o5ECd1SuxmKFhbt2vldlAKBLu8I2s_4mBerKS-AUxQJaUJPohqu_j9KYoVI0Ak2e97IjclrZjtDohAfBM2Bdf7V3EHS-MoPgg3KaWR5ZAkfNaKtiSgU0pd6V0fpy3eSXAh1RxzockYJQJnCQQczQfxKQILXMapaEmIyPj9gkOYUeLHb8ZUIdYscwTzdapJAnFNwgN996LkKwrVFxBN60ZCjj1qF-66v9c5X_0auS-Wl1eF7qKlczWU1X5YVmUm2tupCGTAgUC-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
‼️
بنرهای ضد آلوارز در ورودی‌کمپ اتلتیکو:
یه دونه بنرم اون پشت زدن نوشتن: گمشو برو خولیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104285" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=NJBvbOs6LE_XHOP02VxgQ9NCi7YswRAh2NddTX6K68vNi5DrQCJo9Qjsu9p2y-X1LWfyOSciJ7_8MzgkYl-E_SRh94uIgDT0lsHs8p1YI__VZzaztOBBY089MVtBqShljyiu32pBmu3CQwnTzGjDvnPs307hWPIaJap78u_Ca_bMfMnbgA3WByhR-C9rXc8L02aCGzk8snp4dNreBPBoEdWDVMiadQW21jBbNheGDWJcd5c71Sz8CWnDxpe6Uq_tX21RI4e9nkjNQwDMlLlAmWBwje2Kel0d7JuCiWcd8cf8ncIL7gTCpXMOcVYryYWHP3OTf_3bBCrRD3bAHmdggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=NJBvbOs6LE_XHOP02VxgQ9NCi7YswRAh2NddTX6K68vNi5DrQCJo9Qjsu9p2y-X1LWfyOSciJ7_8MzgkYl-E_SRh94uIgDT0lsHs8p1YI__VZzaztOBBY089MVtBqShljyiu32pBmu3CQwnTzGjDvnPs307hWPIaJap78u_Ca_bMfMnbgA3WByhR-C9rXc8L02aCGzk8snp4dNreBPBoEdWDVMiadQW21jBbNheGDWJcd5c71Sz8CWnDxpe6Uq_tX21RI4e9nkjNQwDMlLlAmWBwje2Kel0d7JuCiWcd8cf8ncIL7gTCpXMOcVYryYWHP3OTf_3bBCrRD3bAHmdggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
مهدی شریفی: بهمنی گفت تیم ها بعد از بازی با استقلال از این تیم شکایت نکنند/ از نظر سازمان لیگ یاسر آسانی برای همراهی استقلال مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104284" target="_blank">📅 11:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba668970.mp4?token=rGXxbJ-jLWa9gm-xLsCfwQK1-6JU8DfWTMi9UktPenT_uTEz9ZpONVIiHYODpnNd-rlqCu9d2_BosLNXwE23V8_OVnb8dHUhwcTriX6JvPGO8kzORDHtnFer3ZJOugPNnnK14QKVBpbmG2r_O_NR9hqYsLX5MSSGVRAojKOPkaQIZ-aLH3eXp4tNHyVA3E0clmQD8dPWzAiI5_Tm-dM5i5X7q8Wg82Mu1PR4srnP8OqmvH5BiE6TDyMnWymXauBT3Skawa96aH6re8-TTX3c6a8T3s_fwxFOM5DGTWAWi1aBWMzhjvV2FvH5NrieQ-7HjgH80FDwNAZtw3vLpo5CCxFY4hztxM_ni9XgW3lErN6U8XocHVnJQHROfQBzX5MPg4mqz4Vl5JEzZ-bxlZ_rqDgGECey7as84CEdB9UHCOvpWGMmU8wF2gBYRryzqsigJoYa19ncfvFkK3Mi9xpGq_-gd6xmtD2VL6TJxXvi9cZvWj8vqwhpuR8FomBbxZRpZNHWft6BRfRwSkSLydnCgBp-B5WbhFsfdZ0AeakIZ6USGtuODmUOpyxmPlsqmCxjAdopNR1CW-bakce_uDzlnursAMkk0BGpgOHdab-U50MujFuf9sJ44543S3oaDrm4pxqrIkbcVk1ifm80BHpplNDbdziBJFcZSBLrXUKy410" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba668970.mp4?token=rGXxbJ-jLWa9gm-xLsCfwQK1-6JU8DfWTMi9UktPenT_uTEz9ZpONVIiHYODpnNd-rlqCu9d2_BosLNXwE23V8_OVnb8dHUhwcTriX6JvPGO8kzORDHtnFer3ZJOugPNnnK14QKVBpbmG2r_O_NR9hqYsLX5MSSGVRAojKOPkaQIZ-aLH3eXp4tNHyVA3E0clmQD8dPWzAiI5_Tm-dM5i5X7q8Wg82Mu1PR4srnP8OqmvH5BiE6TDyMnWymXauBT3Skawa96aH6re8-TTX3c6a8T3s_fwxFOM5DGTWAWi1aBWMzhjvV2FvH5NrieQ-7HjgH80FDwNAZtw3vLpo5CCxFY4hztxM_ni9XgW3lErN6U8XocHVnJQHROfQBzX5MPg4mqz4Vl5JEzZ-bxlZ_rqDgGECey7as84CEdB9UHCOvpWGMmU8wF2gBYRryzqsigJoYa19ncfvFkK3Mi9xpGq_-gd6xmtD2VL6TJxXvi9cZvWj8vqwhpuR8FomBbxZRpZNHWft6BRfRwSkSLydnCgBp-B5WbhFsfdZ0AeakIZ6USGtuODmUOpyxmPlsqmCxjAdopNR1CW-bakce_uDzlnursAMkk0BGpgOHdab-U50MujFuf9sJ44543S3oaDrm4pxqrIkbcVk1ifm80BHpplNDbdziBJFcZSBLrXUKy410" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمید بلان عصبی در بازی پریشب فولاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104283" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104282" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104282" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClB4bKMhKYudFMe7iN2ayJ8KRQCRZeaWrYBzEIDt7B9iPMh3HThJqeCV8ZBwpeRt61GIZHlqCOuujexefMp__RRRdQ20aRIS2kzsWi5sbqoANHNJlR20oI-U3-LgcB872RHXWP3CSQ_xCaeMqQ7chuUIR_SMrxmUAehztGH0qWUVPyK1j5ieYQyn2h8xzt4DOe0Raoq2EOewRQGrm4OyxjVzejo1kv_dBENzMekfqt5VNgjZDdr4BvFsHC_0uhia0quhP-HtyzDiqgw57XHtdjsKrpzlD-sDar3djmXwVih0ySCoBkYXaMnA0xSWkHhcCIXIUerm-7AfTSEXoleJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104281" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=hx8aDz5pMfUkbzHXZmofqLAynI3LrM1lTbvY51a9Yx7PwzzB3eYd9wRjiNsuxSA5fO-SANJ3d5N7wBjdNVUktCAn0QDApVBUL_5yWfxla89EvGkdytVEZlAflYzMbvfgATQ5vTXv5b7uAslVAUx04c8BLMCQD-m7fzW4ZLtj5jyPpNa23lFqs4tBCKF_tBacfK9lCUd04NyaVAkHQOULQokLQwZlkzUwnbWnf4Ya7iqgPs5pmvRQzNxOOAYmQ1NgTPfpO2YAbjGC2c_6IRbDTJwVBlTdUou2U9sLr7xQvc7qdkgHw68dPpZF9TRHsT_KMDyTu9dhpXSC2o7E_Lq3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=hx8aDz5pMfUkbzHXZmofqLAynI3LrM1lTbvY51a9Yx7PwzzB3eYd9wRjiNsuxSA5fO-SANJ3d5N7wBjdNVUktCAn0QDApVBUL_5yWfxla89EvGkdytVEZlAflYzMbvfgATQ5vTXv5b7uAslVAUx04c8BLMCQD-m7fzW4ZLtj5jyPpNa23lFqs4tBCKF_tBacfK9lCUd04NyaVAkHQOULQokLQwZlkzUwnbWnf4Ya7iqgPs5pmvRQzNxOOAYmQ1NgTPfpO2YAbjGC2c_6IRbDTJwVBlTdUou2U9sLr7xQvc7qdkgHw68dPpZF9TRHsT_KMDyTu9dhpXSC2o7E_Lq3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
خواهر پژمان‌جمشیدی در واکنش به افشاگری شاکی پرونده برادرش: پژمان جوونی کرده و میکنه. اگر اتفاقی افتاده نوش جونش
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104280" target="_blank">📅 11:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=TxnaMdXvQvfx7RWcI-o3mcr3ubuH2O1XXXvi1EZ4Sf5FPNwez6-6O5zyo2IJvZSlMxIhA8sRoz7HLMcYg4_wgyDFmdbhbv0gYYQTrgcJJEnAZCUrZHJ6eMqLnwTmnM8YMiCD3frEmdDYtinbNp_mG5-hDyRWtDrFOYACjnn3GfROfTTOJfABtxKk9Bv-HoKMQ5OT2iwzjPC0shrGMVkTDzPSK5tKb6UEJQAi1iSDTyc_MBCXMbF9CIbgnI4CGxJKn7RkYBY3_DNMSae3Tdf5jGTG2C7CWnNZ_2RZGCrr-Tj0G2q5Xt80iUYFJM3N10tMyjeoJgbARUHlm63lY3MBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=TxnaMdXvQvfx7RWcI-o3mcr3ubuH2O1XXXvi1EZ4Sf5FPNwez6-6O5zyo2IJvZSlMxIhA8sRoz7HLMcYg4_wgyDFmdbhbv0gYYQTrgcJJEnAZCUrZHJ6eMqLnwTmnM8YMiCD3frEmdDYtinbNp_mG5-hDyRWtDrFOYACjnn3GfROfTTOJfABtxKk9Bv-HoKMQ5OT2iwzjPC0shrGMVkTDzPSK5tKb6UEJQAi1iSDTyc_MBCXMbF9CIbgnI4CGxJKn7RkYBY3_DNMSae3Tdf5jGTG2C7CWnNZ_2RZGCrr-Tj0G2q5Xt80iUYFJM3N10tMyjeoJgbARUHlm63lY3MBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
یادی‌کنیم از مشاجره تاریخی علی‌دایی و عادل فردوسی‌پور در آنتن زنده برنامه نود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104279" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAR7CDV-DDWNlmupeWtU8EJ0xrPJToc2KlE_7rigorMuztqJK7X0Afi_i0Drp9CnvVEwOtbB6-vr74qNUT1smuf3kQvAL98qXVadAY-6XqBqzw-5PhY7a_T1QqBlP7ThVX_WUPM5M0vFXf_vRaCgKn4HLnJ50JLsa53PB9hlmp9stqtbnnzLdrDOD9So7ndZ5ykKO-9tGYkA-oVTXpdo2A0ZNE9DXTCOXhhY_6sAUJ9_3xBT-rG5wFS6Ojpu7yc9oAhrtf0TlfNkVTjbYxTA3vkPo7JY3iqrFoPo6Z4uB0pRO1xSgXvOcwJTE16nu12R5gGdgEr9fQvOojylDvybCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
توتواسپورت ایتالیا:
❌
فعلا هیچ پیشنهاد رسمی یا مذاکره‌ای بین بارسلونا و اینتر برای لائوتارو وجود نداره!
⚽️
بارسلونا ارزش او را حدود ۸۰ تا ۸۵ میلیون یورو می‌داند، اما اینتر لائوتارو را غیرقابل‌فروش می‌داند و حتی در صورت موافقت خود بازیکن هم حاضر به مذاکره نیست.
❗️
🇮🇹
در حال حاضر، ماندن لائوتارو در اینتر بسیار محتمله و انتقالش به بارسلونا فقط یک احتمال تئوری محسوب میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104278" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=vJ90pwmwjb0LLiRinDQ88v8KVP5vONBuzeYC48FIR4OwkR5iiiGd2Pgi6XO-8NEQKvCJKE3Ul3sA709CnZVflxsfU_Hl9dkKhsVKTxMb5ETtWzMMN2O9lZ8dUEIMErAzDUT46ZhCTmNyybjR0leKL_u15f_L2ew3lMHrs1J0IIo61Zfi5QOwsJjYdRKex1Et4Bt4ItAkALUrEibLMzYH9ahxq7XNZ47l1V34d2xuGqw1KV9o6DmXg-_3Tf8vcBSm0a6E8LnlDx48A-q4Z0F5hqywK2Qq1AhCuxHIDCOkuDeHdTopayerDohg3BueTZPgzohPZyYvERWfl10P9T_zUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=vJ90pwmwjb0LLiRinDQ88v8KVP5vONBuzeYC48FIR4OwkR5iiiGd2Pgi6XO-8NEQKvCJKE3Ul3sA709CnZVflxsfU_Hl9dkKhsVKTxMb5ETtWzMMN2O9lZ8dUEIMErAzDUT46ZhCTmNyybjR0leKL_u15f_L2ew3lMHrs1J0IIo61Zfi5QOwsJjYdRKex1Et4Bt4ItAkALUrEibLMzYH9ahxq7XNZ47l1V34d2xuGqw1KV9o6DmXg-_3Tf8vcBSm0a6E8LnlDx48A-q4Z0F5hqywK2Qq1AhCuxHIDCOkuDeHdTopayerDohg3BueTZPgzohPZyYvERWfl10P9T_zUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بغض و ناراحتی کوین دیبروین بعد از تصمیم عدم تمدید قرارداد با منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104277" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=lsL7oux0IVEa1LGY-gUYP8eA51BWjfY3xsZLKhE6DOtVHnfCmo5zPSJRSUYZVkmWVXKRlmdPBqP267CElxarzc4Ji5ZrVZa33CDR2O_tsh_hWh7I5IPq_FlaqgpG4s5eN9GetKxbtGJVG6UmGTyB886-bByUJTL3m1PuJ_DKnIcTLUBr4x-x45yn9QQ1NdA2uKXpt9FQJk31chxzZdcPwbRNWPNbQqJzXK6K8GZPqtwOUgoi8beXLtzKgUqZea3V_uWOnWr1pi9v6HNTQOKImh0SJEiA31XHs-B5q80w7Zmvg0NuqcEclJwl1OSMXR1kwSpAvInS1xnPW1zlvchxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=lsL7oux0IVEa1LGY-gUYP8eA51BWjfY3xsZLKhE6DOtVHnfCmo5zPSJRSUYZVkmWVXKRlmdPBqP267CElxarzc4Ji5ZrVZa33CDR2O_tsh_hWh7I5IPq_FlaqgpG4s5eN9GetKxbtGJVG6UmGTyB886-bByUJTL3m1PuJ_DKnIcTLUBr4x-x45yn9QQ1NdA2uKXpt9FQJk31chxzZdcPwbRNWPNbQqJzXK6K8GZPqtwOUgoi8beXLtzKgUqZea3V_uWOnWr1pi9v6HNTQOKImh0SJEiA31XHs-B5q80w7Zmvg0NuqcEclJwl1OSMXR1kwSpAvInS1xnPW1zlvchxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ربات انسان‌نمای جدید شرکت چینی یونی‌تری روبوتیک که با نام «سوپرمن» معرفی شده، تنها چند روز پس از انتشار تصاویر توانایی‌هایش، با یک برخورد شدید در آزمایش سرعت خبرساز شده است.
یونی‌تری روز ۱۷ اوت اعلام کرد این نمونه آزمایشی که طی کمی بیش از سه ماه توسعه یافته، توانسته به سرعت ۱۲٫۶۶ متر بر ثانیه، معادل حدود ۴۵٫۶ کیلومتر در ساعت برسد؛ رقمی که اندکی بالاتر از برآورد اوج سرعت یوسین بولت در دوی ۱۰۰ متر است. این شرکت همچنین مدعی شده «سوپرمن» قادر است از حالت ایستاده تا ارتفاع دو متر بپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104276" target="_blank">📅 09:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=DaIHoC8kyUn_vbg8ICFHpESczSTdTquud9Ckh3h_td3-H2LR2PvECkATfWQzdieGBdz7Jbjve1tSVXPdCLN5nxgd2ITIFlSeF7oohTc7_R0NjTP4VoRQIHE8yH7FcUhi5YWY031cFy1nc1d2r4rME-BPqFs9UP1DY2SbYqH8vrG_M3jcBRmkxaTJvOetqpddcgx9-Z1JmnMtFFyQKCn_ok5cdYtEHg1ulmh3xhAoFpVxi19I-48yjNSB78kAb_O0D_bd-cSBuIvAagPLtxMjmUNM9As-WHFwvsZr_50K05vuXrIUpGtHWiE-_B16xFCPnfH-M8gNflbSZdbAB63_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=DaIHoC8kyUn_vbg8ICFHpESczSTdTquud9Ckh3h_td3-H2LR2PvECkATfWQzdieGBdz7Jbjve1tSVXPdCLN5nxgd2ITIFlSeF7oohTc7_R0NjTP4VoRQIHE8yH7FcUhi5YWY031cFy1nc1d2r4rME-BPqFs9UP1DY2SbYqH8vrG_M3jcBRmkxaTJvOetqpddcgx9-Z1JmnMtFFyQKCn_ok5cdYtEHg1ulmh3xhAoFpVxi19I-48yjNSB78kAb_O0D_bd-cSBuIvAagPLtxMjmUNM9As-WHFwvsZr_50K05vuXrIUpGtHWiE-_B16xFCPnfH-M8gNflbSZdbAB63_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرسپولیس خطاب به هوادار روشن‌دل: علی‌پروین برو دیگهههههه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104275" target="_blank">📅 09:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY1Ann2sdKOobHxw8mCn7OxRYm8NbO-1_j_R3vMo316EkzBOUhDYyIKn6ZKTTNBZiBVI3Ij2lcSKbdjPi75znK86onZJkKgK1RIVgoovyLEh_Rf6_V4rkqPYaXV5PBCEJef5cmPYvZEmlNkGQgLOEJTBV7E9_Q_jl-Zw7soJi3KAYOLP_uY8lvpeEC2u_hlS3juriqDXuXHCY8IyccePGb1-B4dKL50uptFjBw2_B-z5QqqFoy-PbxQfO7tFnl77tQPJOLAwC_lc25Ja3iRPxZDPa3eH6DMDwj5h02GUhhGF7ti71ksEoOaPgmtBgOAG-8b8iWJsi1jlprVDVjGc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووووری
از رومانو: ساوینیو وینگر سیتی به تاتنهام با رقم ۷۵ میلیون پوند!
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104274" target="_blank">📅 02:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=a-ZsdKD9De0kQT4-oMQ67lw8zdax8bTg_EGS2v36wo8YjBc5KXmTCvnWMSVWIQROG5UuzAD1LFXyxRL--ZELflexSQirS3KfFYl1zwDPw78pKUTY77fkDGyiuyb9HdBRRTMjMyZCAS31gHuB8vDG_YKf75I_cDcsI34c_HbFtwMGHh4srtSnzMqtLUNlINtH_G9wY0HoIIYYx0hjcv-P-aEwaD5SGNDq6mn_akIVbFnK5-FOAZVusnotgpgqZycMWifkdf6hdCVlW5L0fggSwonw7gEzq7YMyWU82QttW3wvvgGsL6b9_TAsuWnLbtklF4tB5IlCH613N4_rN6NZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=a-ZsdKD9De0kQT4-oMQ67lw8zdax8bTg_EGS2v36wo8YjBc5KXmTCvnWMSVWIQROG5UuzAD1LFXyxRL--ZELflexSQirS3KfFYl1zwDPw78pKUTY77fkDGyiuyb9HdBRRTMjMyZCAS31gHuB8vDG_YKf75I_cDcsI34c_HbFtwMGHh4srtSnzMqtLUNlINtH_G9wY0HoIIYYx0hjcv-P-aEwaD5SGNDq6mn_akIVbFnK5-FOAZVusnotgpgqZycMWifkdf6hdCVlW5L0fggSwonw7gEzq7YMyWU82QttW3wvvgGsL6b9_TAsuWnLbtklF4tB5IlCH613N4_rN6NZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
😳
حسن‌روشن پیشکسوت استقلال : ساپینتو آدم کصکشی بود
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104273" target="_blank">📅 01:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d167412a.mp4?token=lgoilQ0p2-n5fpehvfgsNcbGvVypSPyKyHJw67aJ9rcjKfqbVPKXJXOXlgoUzZWpRPaVDtck5t73Qx_BzlwBTg0-2mj0lajugBm_dY-fsoCENlKVLZdjjt0W07fEZlhx8mcrVLtQsM7KWWHc4lagG5aKqoXCJI_jslgEkRrWVRdXhl-CHioeCbo8b314CcFVMKwZ56K010ZJirZFTCptOv0MkTjqSrxELgIofKJUcYDVVtiLOfUkyqsn4_LDv5RWt34lYemegNLWmnZLNZyGsZ1B9HS3WlGGbU5ZUMvSbNF7HvcZo7doXzQTc9jM69OsGMNBzdpnlqUPFxx2NwD2Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d167412a.mp4?token=lgoilQ0p2-n5fpehvfgsNcbGvVypSPyKyHJw67aJ9rcjKfqbVPKXJXOXlgoUzZWpRPaVDtck5t73Qx_BzlwBTg0-2mj0lajugBm_dY-fsoCENlKVLZdjjt0W07fEZlhx8mcrVLtQsM7KWWHc4lagG5aKqoXCJI_jslgEkRrWVRdXhl-CHioeCbo8b314CcFVMKwZ56K010ZJirZFTCptOv0MkTjqSrxELgIofKJUcYDVVtiLOfUkyqsn4_LDv5RWt34lYemegNLWmnZLNZyGsZ1B9HS3WlGGbU5ZUMvSbNF7HvcZo7doXzQTc9jM69OsGMNBzdpnlqUPFxx2NwD2Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
😍
🇪🇸
قشنگ مشخصه یامال دلش بچه میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104272" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=ElmJ39FrO2_3upxtTLyaciW567TeSz6ttBO61u9_og8E2oITUghxRlqzWb9AkQZ3NSCpI25urSgcwXsRUORDTPUJg_xkcsWjACMbS-jJLe3YCbPSfv6Cq6tgSaFDlW1WAn2KVSDLCcBbSO5otLuxvbQm_K3ap6Yk16bcRcxNMEAMGIsmArjxJcyfa6Jq9e7nBshLODwOYBhIdR8LKnZe8oMfOIfev2RgRnLgVhn9C8mLps_apU0XfVQybKX459miudtqVnTeVQ6nzMTXjfCV3EZiHHOHKAhezqGTw-jd2NMCMmYoGo3bWO6FNcRtW3jWleMiC2llv7nz7lkU_UlTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=ElmJ39FrO2_3upxtTLyaciW567TeSz6ttBO61u9_og8E2oITUghxRlqzWb9AkQZ3NSCpI25urSgcwXsRUORDTPUJg_xkcsWjACMbS-jJLe3YCbPSfv6Cq6tgSaFDlW1WAn2KVSDLCcBbSO5otLuxvbQm_K3ap6Yk16bcRcxNMEAMGIsmArjxJcyfa6Jq9e7nBshLODwOYBhIdR8LKnZe8oMfOIfev2RgRnLgVhn9C8mLps_apU0XfVQybKX459miudtqVnTeVQ6nzMTXjfCV3EZiHHOHKAhezqGTw-jd2NMCMmYoGo3bWO6FNcRtW3jWleMiC2llv7nz7lkU_UlTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
نحوه سوپر مخ‌زدن شیرازیا وسط بازی فجر
لاشی تو ورزشگاه با گوشی قلب میفرسته واسه جایگاه بانوان از اون ورم یه دختر قلب میفرسته واسش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104271" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هایلایت بازی الفیحا 0-3 الهلال با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104270" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=jksAgyCdTGXpqsjVi7cDu0tT-5saAtISJFalfN13-D0WWZuASqZx7KhH1I4DBamd89qst3UIVvBNvwCchBYcrM6aOddk7_SxN0T3w9_TUsEZpgO5wtnkTHfh2X3gYs-dDMZzNRqwjcSNsk4KY8WtcTwwOk7kS_19oIWpJB3c957nfilySw5zEyrsha_O7IGSx3Yg1l6SXHuebZP3rbU8nVtsN4GOYjLslP5P869rGIw-CD0gXAxcP3YhYxmIh6z7wSU9_4KBgByUgq435vxno2sWyRYYekC3XC0kWsXtiQSZASEmfQ0xnPm84VPJpPLxWaIcGQQNc3m90P1vAtmleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=jksAgyCdTGXpqsjVi7cDu0tT-5saAtISJFalfN13-D0WWZuASqZx7KhH1I4DBamd89qst3UIVvBNvwCchBYcrM6aOddk7_SxN0T3w9_TUsEZpgO5wtnkTHfh2X3gYs-dDMZzNRqwjcSNsk4KY8WtcTwwOk7kS_19oIWpJB3c957nfilySw5zEyrsha_O7IGSx3Yg1l6SXHuebZP3rbU8nVtsN4GOYjLslP5P869rGIw-CD0gXAxcP3YhYxmIh6z7wSU9_4KBgByUgq435vxno2sWyRYYekC3XC0kWsXtiQSZASEmfQ0xnPm84VPJpPLxWaIcGQQNc3m90P1vAtmleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف اوایل تیرماه: اگر به سوئیس نمی‌ رفتم، ۱۲ میلیارد دلار ایران آزاد نمی‌شد
❌
همتی، دیشب: یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104269" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104266">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=ZuAofBMvQmmHxm0_lJxFCp1fMmElkgMYP8D20jQ0TZROW7xIaHxMWAz_Xmdo7zunKeqtHlYjHygz7EnEnNT95Hp0V_M8Bta4LWhxcejQPRaUnLqFbd558llzbX9SvIhAcuKo5OJLuW1jX9vqQMWeAmBWFeZhwqrhOEwR6VUzzcowFBR_4nD1B9CaYoqjwaPJ8golkhX8TOXR0md-mEGnJnPDaZ8OdG-yIg8TWA8VTaiB5zc5iv6MLk4TXK1gNRYstvdx0jPHBk_98wPz_00H9WMOSm5JmmZ8Zte-DQa7b8mmaPtmmdcmvbWZgGy3f3g_zfphq-PrKBL-0lyhUHX0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=ZuAofBMvQmmHxm0_lJxFCp1fMmElkgMYP8D20jQ0TZROW7xIaHxMWAz_Xmdo7zunKeqtHlYjHygz7EnEnNT95Hp0V_M8Bta4LWhxcejQPRaUnLqFbd558llzbX9SvIhAcuKo5OJLuW1jX9vqQMWeAmBWFeZhwqrhOEwR6VUzzcowFBR_4nD1B9CaYoqjwaPJ8golkhX8TOXR0md-mEGnJnPDaZ8OdG-yIg8TWA8VTaiB5zc5iv6MLk4TXK1gNRYstvdx0jPHBk_98wPz_00H9WMOSm5JmmZ8Zte-DQa7b8mmaPtmmdcmvbWZgGy3f3g_zfphq-PrKBL-0lyhUHX0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
💙
نقل قول مهم میثاقی از کمیته انضباطی: دوستان اعلام کرده اند چون فسخ قرارداد یاسر آسانی در سازمان لیگ ثبت نشده است بنابر قوانین داخلی هیچ مشکلی برای بازی کردن ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104266" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY_QyqkEsU5Fe4JoPWePLXA0MFnSe4wHW9aiTD6i_dNmzKIbIORhvQXOkHngIOQFO0S97lL_lb6A_onto6ADgmPBHsiYcISmWmhlWNq8ZBxJxyAArBsJsvpR3Pbw4oJKdBlIxGx0TmnzzpbuZMLZBnoDgw7wBylnzyW9VqcjsrE4mNxh1TxfS5ZdjGFYsBNF6lPyjvsZo3DKOTMraA9A794lR64E9H9rDI30Q6hp7yuNWoHImn6RjEmHJgEvRuG8Fz_yYjQRCjWdEUx6C9saJXQV2AamDjGy_pU7QYkNt3moVppr-dazmmX8V1lBmKA6NVzngxQnJEdWLwCoMGhJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مارکا: متئو آلمانی اکنون به لندن رفته تا کارهای انتقال نیکولاس جکسون به اتلتیکو مادرید رو نهایی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104265" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=qcuvgu6uTQnO6ALLiHCniUtlfibFLyCXaSI4jVbYXKYpc-WJtX781DaszrnaCPOerPuHljX22NDbY6f497B8USTAh8aBT1oLwi74zgJjkj3Ftmkm66uufoaVcM0WLIIbDSahj51WdV63hkxqo5V4ij873QgAdc0kaHa56oljbU3SmIkJqjfTvw8s0xgRP5CpluVgpfFaFrXWUPqHT3D8mHdJ6WGDSQLLax5e79kNNI-GaELXULdFdDMvrXI6ypW2YbYyNwEJO-5g_NnIojQ-0kWat9JKGpK2lkgoneoBHnwvJZW3-OrhQrtKS8Y3GkLm4LOuVLDUCdYHXFjM42M-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=qcuvgu6uTQnO6ALLiHCniUtlfibFLyCXaSI4jVbYXKYpc-WJtX781DaszrnaCPOerPuHljX22NDbY6f497B8USTAh8aBT1oLwi74zgJjkj3Ftmkm66uufoaVcM0WLIIbDSahj51WdV63hkxqo5V4ij873QgAdc0kaHa56oljbU3SmIkJqjfTvw8s0xgRP5CpluVgpfFaFrXWUPqHT3D8mHdJ6WGDSQLLax5e79kNNI-GaELXULdFdDMvrXI6ypW2YbYyNwEJO-5g_NnIojQ-0kWat9JKGpK2lkgoneoBHnwvJZW3-OrhQrtKS8Y3GkLm4LOuVLDUCdYHXFjM42M-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حجت الله بهمنی سخنگوی سازمان لیگ: یاسر آسانی یک قرارداد 2 ساله با باشگاه استقلال دارد و در سازمان لیگ هم ثبت شده است و درحال گذراندن آن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104264" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104262">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=d9lb2dD2oNrPLxtDmRg-GaoNdLkk-g6tfWgxZmjNGb8c942r60ltYtQQjzSNF1Hl8DCV5VCRFyzEhQmsKxds_o1zkDps7mGp3L7uEMgB7zmbzUeKuwEZsJArhnUhsHnDvUQZqrct2LLG8eovkV75RAjq_8MeQvidH1pV8ISPqPCQG7PlfNVSUMu2TlaUYuqKVNpg9bft32lX1Vbwitt51pZC5GjqiVLebfDcsN_LO6krwr8Er9_1MvsR26z6UgGj_zParqolLT34iFH99IMgt_YKyMdunQpDZlUElZh_Ca4j1hneH14N7I-NiIZoc-bJ4lWn0y4_g4NGVCLD349hUYlIYkjK4MCnpuov9hN9uNkK8AuIl4yVVW-McnbALTiXruTke-Kh8a2Bk3YgFnRsBLzbUSQ0iKcMj-3QkxNZPNDuv0oqKteRtGUw3j95Bd8f5UG_LgIjyyHn2q0UrDXDeeG47OmmdsNoR9lVtR_dtZSq4zNkcfAUJnTNsWL7sqOLnpW--SFhzJ6l9y3z5mmNQeC5CrqSd2o3MRvNzKrvNWEk4i0GL88mfCge_9j59aJoxZYX7YgEb7BL90czKTgpnnWVwOzivPas3hRF_QzrDNjvlkdvb5hfUjrXx6CymLQ5idXkC8s1-WI2SGTMKdAQwH4ACNYzAPk9qwZWF_D5-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=d9lb2dD2oNrPLxtDmRg-GaoNdLkk-g6tfWgxZmjNGb8c942r60ltYtQQjzSNF1Hl8DCV5VCRFyzEhQmsKxds_o1zkDps7mGp3L7uEMgB7zmbzUeKuwEZsJArhnUhsHnDvUQZqrct2LLG8eovkV75RAjq_8MeQvidH1pV8ISPqPCQG7PlfNVSUMu2TlaUYuqKVNpg9bft32lX1Vbwitt51pZC5GjqiVLebfDcsN_LO6krwr8Er9_1MvsR26z6UgGj_zParqolLT34iFH99IMgt_YKyMdunQpDZlUElZh_Ca4j1hneH14N7I-NiIZoc-bJ4lWn0y4_g4NGVCLD349hUYlIYkjK4MCnpuov9hN9uNkK8AuIl4yVVW-McnbALTiXruTke-Kh8a2Bk3YgFnRsBLzbUSQ0iKcMj-3QkxNZPNDuv0oqKteRtGUw3j95Bd8f5UG_LgIjyyHn2q0UrDXDeeG47OmmdsNoR9lVtR_dtZSq4zNkcfAUJnTNsWL7sqOLnpW--SFhzJ6l9y3z5mmNQeC5CrqSd2o3MRvNzKrvNWEk4i0GL88mfCge_9j59aJoxZYX7YgEb7BL90czKTgpnnWVwOzivPas3hRF_QzrDNjvlkdvb5hfUjrXx6CymLQ5idXkC8s1-WI2SGTMKdAQwH4ACNYzAPk9qwZWF_D5-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
بهمنی: استقلال به عنوان میزبان دربی، ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت
!
استقلال میزبان است و ۹۰ درصد ورزشگاه در دربی در اختیار استقلال خواهد بود/ استقلال ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت و بازی برگشت، این موضوع برعکس خواهد بود/ تمام تلاشمان را می‌کنیم تا دربی با قانون ۹۰ به ۱۰ برگزار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104262" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104261">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd6aQFKKXQuB0dRUsiKDSBY2nKQyAr13Hs8K7F1waGPfTXMBWaZPgNZ0hJzTNuQO23l_16mnS6QySY3p6XMatfwWdgUliXCmbpbtNS2iJ4lnafA5pYVRGYAaGJ8_ta6CayFU4JxYYm6gnA2FtM50QnPo_GDmhqoRQcL_0KhnBqeiMEgVXC6xvp7hXtbXGk88emJUma4r4p3W01aXQvj2y1TcNpGkdIbgutONmHwzvI0-qqJhMgA3aklQj-w9_Yvr45gLX8dv81JL3lLe6ahIbjIST4cbieNvskgng2akwYp3LVD5OYYgiPNWJ1XxeAfDWyafd3X_nQJDuadrtgQns-Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd6aQFKKXQuB0dRUsiKDSBY2nKQyAr13Hs8K7F1waGPfTXMBWaZPgNZ0hJzTNuQO23l_16mnS6QySY3p6XMatfwWdgUliXCmbpbtNS2iJ4lnafA5pYVRGYAaGJ8_ta6CayFU4JxYYm6gnA2FtM50QnPo_GDmhqoRQcL_0KhnBqeiMEgVXC6xvp7hXtbXGk88emJUma4r4p3W01aXQvj2y1TcNpGkdIbgutONmHwzvI0-qqJhMgA3aklQj-w9_Yvr45gLX8dv81JL3lLe6ahIbjIST4cbieNvskgng2akwYp3LVD5OYYgiPNWJ1XxeAfDWyafd3X_nQJDuadrtgQns-Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
هواداران ملوان در بازی دیشب تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104261" target="_blank">📅 22:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104260">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvMmrFnMieUM68jsSkExETbR87NbtCOwjxflJYTBSNRlj2jJEI0w7pKcTxbeA3K1TRH4BRo70y_WdYifvpakQdk1Ce8-J5xhQ8ypTRJDEoqrjddetCVvWmcbsVN_NaalI4IoKC1M25a4WLhWqtZfwNY4D7LEjKNbo5VwlUIt3aBuv5ft-H8ocyZYMTY98fM_FpvfvtwGQpzzytqslHGNnrt_4U5JAjdRgio03Zb34-xMKZECqowFtnBF4t837vczXramzP4-YCiVafqCsZplZyQvxM8KzUCf7Myaj0K3NwDhblYlRpHzgHrkGp9YGZv7ImLFADKeE6eVLmkWahWChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نادر محمدی(منجنیق) و هوادارانش در روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104260" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104259">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO02QtvKa_T0Qpncdmdd11LIla10BrRVU9r0ORlUWtnb8EipPPcemvrU3B4_j2yw9vDjycLtA95l0Iv5n2k3MTsEtECT-VUF9zrQp6sCcTvP7CmgD-bI2bpOEsXjh2BGJZzaCX3NryzWjIIq0vGPH88NprpluSIqi3xQaeBqB1wQ77WuwFzdyRcmoBB0-RhzjF3xPtAJjQJ1wNDx7cb7vSZxgrjW7s3pvZGuCum-S95ZdQRjTsiDsZ9c-qRbX8rhSPT1vM1F8W2-cE3iGaeislYUiTnK2n7YEv7G3m8jPEfUu9E_dNkvVlDFy_OTzgES73pVWs1_D7mQ5S9jlI7H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
خط هجوم بارسلونا بعد جذب احتمالی لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104259" target="_blank">📅 21:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104258">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnKhzi5GtTv7_EdQXiDK3ieTcQN_ualRT5uFXnzjhdf_FA4d_jDnhsBTi-NFIdWzwqMr8wwm74A5zQx8qUg0K9lb_fOIiIBClO-LyoYnJ1OTcXKwrgVM6xhG0m5c7zLjL6VTCPQGf4gSzXe-Mg4BIH2rgBjWSrruhl0Uuezg_CEcIfZ1YOFaUxmxcdvv0Y0SE7xIUE7xGQPldkUMTuS7YT6GCbdw8bJNpjD1v6XoavfQoNkO0SU9NLyPaBacEHlGXOpv2bgBFPGXldfpYwMemWtD0L6KUoDDT4q6H9gGiVBmCTzdSdfHq-jPG4ljujl1K8Or8hZvsHZaIpqAvQQMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
رونالدو پس از دو بازی غیبت در لیست فرداشب النصر برای بازی الریاض قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104258" target="_blank">📅 21:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104257">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=eMGcfz4-X1IpumhVMGeBUm9w9vOah9_Nwzdht8JDkpdBHoWGUDFC_X80Sbo5bu7dN1e8jq5awmKm9Vx1hc_glhEWUDoXmEEBG6TgKIH4dkiZqRA5LNILofRopZTzC_0T-Y0L0SJ2pMfl2HG5pKbskIIl9bSnSVdq4xY7M0akwUxBdH7F9x3EQ-5kYifwvNNYstEpdidgpXVmZ2ODrDoyvlb-sDHFSFnUpvE6mFRlbn-VvgmlADwbt0G_7A03-wV_UaT8kDlhMD93lI8oeqF-ucGL6A5BEXwqrWW7PduWVdVk1KJIjwIF2hIKNRYtIkm8ZhgAMEOi0IORO4lEEp-mxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=eMGcfz4-X1IpumhVMGeBUm9w9vOah9_Nwzdht8JDkpdBHoWGUDFC_X80Sbo5bu7dN1e8jq5awmKm9Vx1hc_glhEWUDoXmEEBG6TgKIH4dkiZqRA5LNILofRopZTzC_0T-Y0L0SJ2pMfl2HG5pKbskIIl9bSnSVdq4xY7M0akwUxBdH7F9x3EQ-5kYifwvNNYstEpdidgpXVmZ2ODrDoyvlb-sDHFSFnUpvE6mFRlbn-VvgmlADwbt0G_7A03-wV_UaT8kDlhMD93lI8oeqF-ucGL6A5BEXwqrWW7PduWVdVk1KJIjwIF2hIKNRYtIkm8ZhgAMEOi0IORO4lEEp-mxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
‼️
هیجان‌زده شدن یک نفر در خرم‌آباد از شعار بزن که خوب می‌زنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104257" target="_blank">📅 21:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa_ouZPQjt2G1dP6pPOjSZZjVMtRzOCrlnu-zyY6dxlZvuXnX4CKwjfuMh732KCHNx9YiOPjcMiFa9HYNQTlPlr5GMQY86dfOFupZjvBo6hSQOl99YEqMQ2Hsx1tzayAyuSwkCJvyyKf3zk-DJWEk5_2ADyckcwJdYJh1gFuUGHLptKHDe2BLHcbmobu8Kf2r8EdB6fG0MqIBiRzmp60LEAULjj8sOj9KYvlTlaKQBAm_WpMuNBM3OetUG766BQCzPl5TSnytjiQ750nW_IKu70BLqQUbQ-bqIeWwVQX819HFgcDKNDqrdcxEHZW30pwKClHjMkgK9pGrg9ZFvVIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
آخرین‌رده‌بندی توپ‌طلا تا پایان ماه آگوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104256" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104255">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMmk95Z0bQhUs55GF6sKpX_I0jVWeymGFME7gxCX7XHT9QbQpn1DoGQ3kUvMAtABgmoWw9AlI0D-sJGDeILqSIDLVmMtQEcYtebdvOiLUdPRKDDyfH8xHhwDGJsx65m8N6zElXku_ByOV_2yEzgE7pxNVua5_RDQYfQYujZRrKV06haPTW0aUvaVVobPyFDrlzzHtKOAySsMG8GaCJ-mp8wzq_jj-00JR-o1JMChbQrbC-F1FmeshFPZH5mnvHe-QXhuUx6c4MgxAHiPMdYzo5O2v3MkPvQekOA3Mf6LyTSfU8QFIQgsL8asz4NwN32oRK1C1nSfp30aVvafcqvaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
رایو وایکانو
🆚
آلاوز
🇪🇸
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
💰
۲۰٪ بونوس روی بالاترین واریز روزانه
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104255" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104254">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=S5RwAXmIZQzRXZZwWkUM39EH3ia7ZCN5hkFqzKlbO5vI5EL9bqUWtqkdwa84qeYzSN6FMHqJ-j8u60o81ukHhmOSZjo6aGe7m-FRz9wudu-Ycy19j5r3BFyriSpM3adN4ewkWfCBSUjOWy6u6t9dIp5VjEFqCEQYnVT1_zj3XOzOzIx_i3n3QH4DS5awKeypkp8c3-sSRph9Rbrire2-zG0qZ7kr8E3qE9CILBuDEXA-PTZexVVF0_uWdEMqLFH0uCkCc6wFmrmx7MG77bgfv3CIfqJdFhFeo54m73myfj6j8SJ4ID0BX_fNtjFzLCeOCYt2mbTA2rZ70LMfw_Ly3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=S5RwAXmIZQzRXZZwWkUM39EH3ia7ZCN5hkFqzKlbO5vI5EL9bqUWtqkdwa84qeYzSN6FMHqJ-j8u60o81ukHhmOSZjo6aGe7m-FRz9wudu-Ycy19j5r3BFyriSpM3adN4ewkWfCBSUjOWy6u6t9dIp5VjEFqCEQYnVT1_zj3XOzOzIx_i3n3QH4DS5awKeypkp8c3-sSRph9Rbrire2-zG0qZ7kr8E3qE9CILBuDEXA-PTZexVVF0_uWdEMqLFH0uCkCc6wFmrmx7MG77bgfv3CIfqJdFhFeo54m73myfj6j8SJ4ID0BX_fNtjFzLCeOCYt2mbTA2rZ70LMfw_Ly3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لیواکوویچ سنگربان احتمالی جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104254" target="_blank">📅 20:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104253">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05150752d5.mp4?token=L04jcx8iu-CNhmJyi_wrJJHGSUtEklUtdfM46Ah_CzFtcnZVsCPNo-w6LeSI8VXm9ly17AzDo5J8zNKBWu5o486xwBJj27PW2jG0BW8p3KmMStpdCELvHAjhPbYOiNP_WilnmmP_mweAG_r3mVCKmTdz60D29cPiWvHQRTAcjrobZyLA6OHHtJDmxX6TGkRXEtlVtFufzk2OHkAOiRxgreg_JDy27yTdKX8QK_5I11StpciwrACVO2ctIlfA67BWLANJh486xMOFyrJNg-u97A72ODJhIiQxBnPxYDOO16BkwkQF4llftwrKyMyIO3K2VSjyKIk2AaAua6fhS34rTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05150752d5.mp4?token=L04jcx8iu-CNhmJyi_wrJJHGSUtEklUtdfM46Ah_CzFtcnZVsCPNo-w6LeSI8VXm9ly17AzDo5J8zNKBWu5o486xwBJj27PW2jG0BW8p3KmMStpdCELvHAjhPbYOiNP_WilnmmP_mweAG_r3mVCKmTdz60D29cPiWvHQRTAcjrobZyLA6OHHtJDmxX6TGkRXEtlVtFufzk2OHkAOiRxgreg_JDy27yTdKX8QK_5I11StpciwrACVO2ctIlfA67BWLANJh486xMOFyrJNg-u97A72ODJhIiQxBnPxYDOO16BkwkQF4llftwrKyMyIO3K2VSjyKIk2AaAua6fhS34rTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇹🇷
ایزاک کارنی، یک هواداری که به خاطر علاقه به محمد صلاح و باشگاه لیورپول شناخته می‌شود، اخیراً در صفحه اینستاگرام خود، پیامی برای محمد صلاح منتشر کرد و برای او آرزوی موفقیت کرد. او به شهر ترابزون سفر کرد و با محمد صلاح دیدار کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104253" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104252">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=AUSXA7Ei2dPqnfm2WqTnKohOJ0yacGrgR0UQSgZctnERym7kYJitAlKWCAFCAUltFiMElyljkQNdx68DGEL9zUcdwotW1NVjBYusz13epeJirdgE3xXSAxQCi8OgNb9FIn4YPaBsi28jhZsMs5ep-zPSJstA1thtRXW-eok5G11el11rXeu2RWGXvm7H8T5XnW0rt42OFTi1WnKUSIGotTfQqA_WaIwV0HmelMs7cGwLFVkmUAhsaxcNAkcVb1xqyn0eDEBOP0kP9zesM44lUGFEe4EQ1v6XqczH7-nMO4ficQeyjPt7aNXndJcyFZxzEytU4e-SmxmyPeTs026KLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=AUSXA7Ei2dPqnfm2WqTnKohOJ0yacGrgR0UQSgZctnERym7kYJitAlKWCAFCAUltFiMElyljkQNdx68DGEL9zUcdwotW1NVjBYusz13epeJirdgE3xXSAxQCi8OgNb9FIn4YPaBsi28jhZsMs5ep-zPSJstA1thtRXW-eok5G11el11rXeu2RWGXvm7H8T5XnW0rt42OFTi1WnKUSIGotTfQqA_WaIwV0HmelMs7cGwLFVkmUAhsaxcNAkcVb1xqyn0eDEBOP0kP9zesM44lUGFEe4EQ1v6XqczH7-nMO4ficQeyjPt7aNXndJcyFZxzEytU4e-SmxmyPeTs026KLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از گل مرادمند به پرسپولیس در فینال جام حذفی سال ۱۴۰۲، هزاران استقلالی در ورزشگاه آزادی اشک شوق ریختن که جاویدنام مهرداد مشتاقی هم بین اونا بود. روحت شاد و تولدت در آسمان‌ها مبارک بزرگمرد ایران
💙
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104252" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3KmTdALLF0yfkldfgnAww0QaC2PDxG5HFnD_6nO4tIjSvIge1yUF5PxDvfQQ-MFf-XtBBTockZaOiGOePPRuFPmpLabuuyvjTjV6DjqkzbEdXK3Kd7DfWXOxPtNqj7Erzl2oa3nbLELlhRppAAibaks_Fyjs2dtnhIrVo2iA1uuHcF3NgD1KOf1ThsXd0IgDAgKK7ElZlOr3jmr-IQpTT62pJD754fv4r8iyfJm5JeriCPZ8Jk5nn2f6hAO6Y0QOeG9pXdJILpaNIerQCNdIfA5k7U7PyIb5f3UWSaf4ssSFpmK9_MTk8ozXIO7Dgj8S5gzldI9ZJH-suLf5Oqn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyaVIsQoAanIRXNlpjrqbQB38kzzefqxvqIVYUHpfv25RlM1zdM4RuNWOlZMftjgd7jQ5rSax0YOWLvwzhPRKoSrsiNVaiHLOYrErwo-TkNCw_5VH5AQqhWNYHMeyR_ua4fGVVg725_BClxxCGGterC2SXvlBmAjCYwq6RhS32rs9lWjpazUbBKdHPyd2YqlrD44bQTwuDzkFA14VDVCVAXOhM7d1CluaPALFhJIYodt11dTmffLNifcOPsgqaDSTBfGh1PAqULBmUSXGgmW16A7uhcNCrewanr_TKOOVQLmhYdp-e6DGcrZh9KLUJP2NM1RFFgY-1TyW4-hnwa2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Py4Xms_4fpNvmTvoa-x2jlLle0xBhj0HZ9qudmNhoXLh7ktj42a-lTpHTpVuKvy8op7RLp-lPBqaBoDTf5LpHYGY_sT4QS4uhNAUmWFF3IS35EjlNcJTjm1ai4Zj1F7-c08jqgq0-imuu-YGU-5JR4vfg0mtYy5ObEmeCUcgb0ufQF9lJii7xHqJW51ACbcKDhCqOM01Iyt9GPr7KvVueJPaVwK-yTSr_pI_eo9Uzuu_dVvY2F_b0O8jajxTRW9ASpMmgSdqusve4yDZC4fb_NvXbnsW3MBdTeTc1icHMjfik363OF9r6oWDN4RdGbLeFzh0EKPSsHkU1rEjR5h_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzCfTe4jDtS2q00ku4QQfKg8_5JSdVdZSAr4BO9BgAW6u8TqDKhn-WeOEGx1skuLSaYyFTbc9kgxE4d_XruWYZjljbdJEt9RFyXkeQ_jwJqZ0O12hv4NBrkj19rfBpc8_HsmzTF36MiJrUo4slzpWTQsX8uifKcHI46Ts9BZOvAuKmAm4xhvbR-FdikbqziTMLMcce1KUUjN6pdvBu0fIwbUc0HCfQcTelbmSk0Cvg4luZRVpJN5UCUEKwhHUudvzjtZQO9gW3JZCoS4CDQ8wOUgN5KwIIeFFZv1qN94rL5xKqrz_q0edmP5vj0EbNBiDGaqauOxCSClh7Cx7AVpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vft-ynYrcCXYerkuou56zEt06ACHB9iA1bkNWIJGgicFgJUL14prvvAoCQj6p90Yz8dC7iVHcTP0JbMkxZn8eUChj3VONTULNaWDs2KAeayxg0aLTWqeiDdcqPfYRwBtHEyZEzN9e-oi-DLsKz_F4BOXiG5s7C-UDr1L3eAKqH7RbbkZNTu10D7mhvrPk-YAVob542Vgllx88DdKJUEgcZfulaNDimHwpdalQP-JIGMYc_1Vfq8sv9rcS3W75sBzX2tuh9VOwTtp4UyTYCroG8Brmj-rAgEWOEjyZ6WIP-WvgRaZpFsjOpTeJgK8nbK4QtvV7T4V4m9GV7EZB_q_bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
هوادار پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104247" target="_blank">📅 19:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ0dpufHrYn0d21-qXMFHx7GKtPebnu8EnAlQKUefm_oq00cTk28jgCQIPUCLqxjbqvr-YfPTCgIdfERuFU-aV8lbsU_CuUtM1h2NwByJMWGA7HeMUj7wJrEbmRgJd_Lw1NCIGWzefPuyZw2NsdK7dhsmJ3RcfiE-s2y6wRkvruglBwVaG1Yzs8qSvmWIhe_w1-Ca3uX07fw6NXPo24Oih-Nvi93vzOgNn5ecDo2P4DRGOXXGhD2ohMQyPJCAiEinEVMm-gWQIGi6o5oNxiLh-Z9SYc1zkLhaXRzc8eoNQRUDHqh5kHTp92yNol6VzP-vpT8jefl5yivxTiWxCdL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
😍
پست
خداحافظی منیر الحدادی به هواداران استقلال
ممنونم استقلال!
💙
همیشه همه‌چیز آن‌طور که تصور می‌کنیم پیش نمی‌رود. شرایط باعث شد دوران حضورم در اینجا زودتر از چیزی که دوست داشتم به پایان برسد؛ اما با خودم خاطرات و چیزهایی می‌برم که کلمات قادر به بیانشان نیستند.
از هم‌تیمی‌هایم، کادر فنی و اجرایی و همه اعضای باشگاه که از همان روز اول کاری کردند احساس کنم در خانه خودم هستم، تشکر می‌کنم. همچنین تشکر ویژه‌ای از هواداران دارم؛ به‌خاطر تمام محبت و احترامی که همیشه به من نشان دادید.
امیدوارم روزی دوباره مسیرمان به هم برسد. با قلبی سرشار می‌روم و می‌دانم که این فصل از زندگی‌ام همیشه جایگاه ویژه‌ای در قلبم خواهد داشت.
تا دیداری دوباره
💙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104246" target="_blank">📅 19:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=NBdo_NdC-cCanwg4jqRS_rprcM9LvoKAePiHsq5D8PQMOaZteOrO1yG4ZRwwC1ERaT1ql12W66CFhK3HbF_PbUBzIczDbaSgDkC0hhBesSQAo1ioMRLXDs893UrugIbg7GrFH25CbXu_psno95DVo_JyJm00qkAKgbHuq8v_5knrpOK3NaHZhZNnrVksb0__HzjpeuUBOMixBkXI5beB9PfPzRVam7bMJ-sd20HGN7nZtyHCyS-GHk1BIF65DooLzxQ1A9ljXp2nrfzzmz9FKOWIK2YvAtjGmpoTT_PazWsB9H5vYkUidJJfmCBb0BOSUpaxzkLDHpZYIAKhETlR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=NBdo_NdC-cCanwg4jqRS_rprcM9LvoKAePiHsq5D8PQMOaZteOrO1yG4ZRwwC1ERaT1ql12W66CFhK3HbF_PbUBzIczDbaSgDkC0hhBesSQAo1ioMRLXDs893UrugIbg7GrFH25CbXu_psno95DVo_JyJm00qkAKgbHuq8v_5knrpOK3NaHZhZNnrVksb0__HzjpeuUBOMixBkXI5beB9PfPzRVam7bMJ-sd20HGN7nZtyHCyS-GHk1BIF65DooLzxQ1A9ljXp2nrfzzmz9FKOWIK2YvAtjGmpoTT_PazWsB9H5vYkUidJJfmCBb0BOSUpaxzkLDHpZYIAKhETlR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ریدمان لامین‌یامال در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104245" target="_blank">📅 19:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po-i2HLM2n9FnBgzDAGm2J-nUUXK0_I7YUcksUAo0qnvBatQ7O3iQv8GJUvUuBnmID4G1lXNVp1GqRZ9O-or7hPqugPycSwBWmVUDckQVe9cjdt2UTqX_edAQ6p-yo6PUiodO7WgKTql8YWP8RSKGuBh5JD3kFaWgW_ZEgTPRULdmm8d1Y7X9lg3xI9ve9x-PgNPDJQdCdbX35kW8kfkl4d4B35NVWpqrkdFFvFY7m1Dumxxunzrl0DarNkj8ECQWF0gZLccrVemhY5n28RQaoHOt7xCxKf8OIGSnAwjO6nUEgOLrK_iueIqsqluR-aUEJbZrnYyfEiICFaloUS-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری
؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ پرسپولیس و سایر تیم‌های ایرانی و خارجی رقم 1.1 میلیون دلار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104244" target="_blank">📅 19:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRjtDSUFDpIwhM8UT7z5AiBeD6q_laf1nqKMsK8N80rVIM6P752o9zd_71Z2Y_f14U8rjJw1cehOXo7t0a8KAwYmFqXXiQJLZPcudvtEIXwDpPorW92iZOZLiw9rUAHpjKD2h4IT0Q5DMp028DKxP09PCy_soMUGwUUPW874m3qAK-jWKRYD2L43QO53e1ouVqeGoZKDWaGd6jvY0ouh7ozRqCx6HlUiz13LzqygGrPcCxcHk-1o86uSEHDk5Cfa5lo-MmR2OnTkfQPq-q0JCmgC5OGQgMbLzkHRSWWsuvdYP_VdfqTqZ4ieSj9HBzk8G4_ox1rLJEwRgyK4KDLbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پرسپولیس امروز در دیداری تدارکاتی به مصاف آریو اسلامشهر رفت و با نتیجه ۴ بر ۲ به پایان رسید.
⚽️
گلزنان پرسپولیس: امیرحسین محمودی ('۳۲)، مهدی تیکدری ('۷۹ پنالتی)، پوریا شهرابادی ('۸۷)، محمدحسین صادقی ('۹۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104243" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAzp9umokueALS0pZp80SCMAcOqXmFIv1yaZT6ksVgXqStrOLDFObLCVOSHjgt2p3yNamSbkWV3t4e1x41WcwiB7MF9O2eX1Lr8cxS2i-dcLKuB3SN1VZZSYKDcPzmn66bDkx5vSBdce1Ei4we14oWUy4Jm43DdIAqDZzC_GlM1mqR8dTq8lzImk5YA6WL-5Jjy62uTDOgj4F-5TlmI06UumKeIVciz1FPrUF7lDkyNi73khy0QP_rtzqWdGAVLl7hpe_gpIjXDZ2akx443_qKm7Ex0cZPecf-9RaJExvXB8dnlntE6r-d8YESVytj50SbdBNa8nIeF8pBp8xC8pcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇮🇹
رومانو: تا این‌لحظه اینتر هیچ پیشنهادی از سوی بارسلونا برای جذب لائوتارو مارتینز دریافت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104242" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8c825309.mp4?token=H3AnTp3ANm5vZjwkEnzeHxIx2AyJd2CQbqr97MZkUCZ2Ukp_0IVqBoO7M0_JnEMLZbL3jUo_LQ6hS-YmuzSBLe7k3udYyaD1Saqn-rNjDiPeckXga3YH7ce5WAWkkjNkWWPuZsd4FuCr-VztyuGFVkQyovQ8UV1fG7gnUJf4MTlBkfpb1XzARYh8E_cv5Z5m_e7T6KDqPb9psaBZqD2OZ31Zv80912VwIx8oqZ-08W5GKPYNqwptporzeJnAQlNXWpYt8NLnqGJ3wd5Cqz11bnE1vK1VdqptvlC3v95xcg4KjSGewhaoR11Lm3tizVE9Z-WZjcAMvQu147SeKOaDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8c825309.mp4?token=H3AnTp3ANm5vZjwkEnzeHxIx2AyJd2CQbqr97MZkUCZ2Ukp_0IVqBoO7M0_JnEMLZbL3jUo_LQ6hS-YmuzSBLe7k3udYyaD1Saqn-rNjDiPeckXga3YH7ce5WAWkkjNkWWPuZsd4FuCr-VztyuGFVkQyovQ8UV1fG7gnUJf4MTlBkfpb1XzARYh8E_cv5Z5m_e7T6KDqPb9psaBZqD2OZ31Zv80912VwIx8oqZ-08W5GKPYNqwptporzeJnAQlNXWpYt8NLnqGJ3wd5Cqz11bnE1vK1VdqptvlC3v95xcg4KjSGewhaoR11Lm3tizVE9Z-WZjcAMvQu147SeKOaDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
یه پسر دانشجوی ۲۱ ساله آمریکایی، به کمک هوش مصنوعی، یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد) درآمد داشته باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104241" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NQow1MTqDKjqmrNA1hVYrgxJur-JtDkwWsMeva_pnoZUJ6kJQo6CyN8aNL_pW-2lA4bSpKGZGPCxIadpaHDG6dKbxJcK0RkF_Ogx-QeYNnFbBFrzyv6mvVzwkOmHX5-S9rex5wvbynJgDSGeMzch5So9xF1PfX5bt12VhB4BJnYaSctEhOoBRcXdevNhK-QOS0DZTHhGdJ8LOIKfjxxH6GYAj1y_4f40QoX8tfzzYqBTOpCDdl3DwC2MmUOYT13ZmQJRuzjyOjLiODn6va3wQKYUel62cDs0kckjCknLqXEeFqEKBJTRnh3zVNRBOAuYvzQ5t7PHQHtgRbjaNjuQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NQow1MTqDKjqmrNA1hVYrgxJur-JtDkwWsMeva_pnoZUJ6kJQo6CyN8aNL_pW-2lA4bSpKGZGPCxIadpaHDG6dKbxJcK0RkF_Ogx-QeYNnFbBFrzyv6mvVzwkOmHX5-S9rex5wvbynJgDSGeMzch5So9xF1PfX5bt12VhB4BJnYaSctEhOoBRcXdevNhK-QOS0DZTHhGdJ8LOIKfjxxH6GYAj1y_4f40QoX8tfzzYqBTOpCDdl3DwC2MmUOYT13ZmQJRuzjyOjLiODn6va3wQKYUel62cDs0kckjCknLqXEeFqEKBJTRnh3zVNRBOAuYvzQ5t7PHQHtgRbjaNjuQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماشین جدید رضا گلزار، تنها رولز رویس کولینان منصوری ایران به ارزش 200 میلیارد تومن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104240" target="_blank">📅 18:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=b1qSizEWd35vmwACzyLCC68zU0P43aAp1d2s8F5LJCxMJkpm3sw1FpZ8kKya9BFT-xXQut9zu3s4q41LAvurNINVyTvz1b06oloQC-3B8MqJz4HfQAAXl5F1dY4_WfkT3GaNPPFOf_PmO3Ba6hbByBho5c55HFIgVtuvTFhVBNT2Y6CokO_qKCzQfU6LrOCrUWoln0YCskTTIs0qef60YtFbj841V6ZQijopUIoYm79_tpcYXmxRE3ikzIdZXz1bVRl-MwBQbjuwRTHkAVnyPW6C_7_TU7-x1bp_AUOAMtm1eWcjdPWy9nAN68B7xVFvVRWDg-b1r9zRPeGBcezNMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=b1qSizEWd35vmwACzyLCC68zU0P43aAp1d2s8F5LJCxMJkpm3sw1FpZ8kKya9BFT-xXQut9zu3s4q41LAvurNINVyTvz1b06oloQC-3B8MqJz4HfQAAXl5F1dY4_WfkT3GaNPPFOf_PmO3Ba6hbByBho5c55HFIgVtuvTFhVBNT2Y6CokO_qKCzQfU6LrOCrUWoln0YCskTTIs0qef60YtFbj841V6ZQijopUIoYm79_tpcYXmxRE3ikzIdZXz1bVRl-MwBQbjuwRTHkAVnyPW6C_7_TU7-x1bp_AUOAMtm1eWcjdPWy9nAN68B7xVFvVRWDg-b1r9zRPeGBcezNMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
افشاگری ملیکا پارسادوست شاکی پرونده پژمان‌جمشیدی از اتفاقاتی که در این پرونده افتاد و منجر به شکایتش از پژمان جمشیدی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104239" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=mAo7n__UhLz9JUhHnc4_JOjyLIMmCsoO7agwG7u9BiDCBN9Z_KGJY-fklILAvtQZqwXug6kMTnBR2JRJkc9Wav6kpVbVvIbCMxd10UgN_d-drsSnNNgHDSbUtrgGC-H00IH5TDbjtmiRXePdvI4imezCz9o4QUpwb8Qk7mQqXaEgeXTdSE0wpaQOpwrMfONJUTkcwaESRX9foSnuC_f1nnDq_ON6Q2XZ8NDSbeWKHA5onyumJJ9XTBbE6gR82dm6XbFxOusKLpvE4MKX0cRPB-L7C1e6vND_x3tM4xbneTvddsE1rCBlxT0MIL34Zpj_DKAOvgYI6XCknIUiv-R3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=mAo7n__UhLz9JUhHnc4_JOjyLIMmCsoO7agwG7u9BiDCBN9Z_KGJY-fklILAvtQZqwXug6kMTnBR2JRJkc9Wav6kpVbVvIbCMxd10UgN_d-drsSnNNgHDSbUtrgGC-H00IH5TDbjtmiRXePdvI4imezCz9o4QUpwb8Qk7mQqXaEgeXTdSE0wpaQOpwrMfONJUTkcwaESRX9foSnuC_f1nnDq_ON6Q2XZ8NDSbeWKHA5onyumJJ9XTBbE6gR82dm6XbFxOusKLpvE4MKX0cRPB-L7C1e6vND_x3tM4xbneTvddsE1rCBlxT0MIL34Zpj_DKAOvgYI6XCknIUiv-R3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمی‌ترین سرود یک‌تیم در مسابقات محلی مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104238" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104237" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104236" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
آخرین وضعیت استادیوم آزادی: آذرماه جدیدترین تاریخ اعلامی برای بازگشایی این استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104235" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=c-MtuAvP-ss6S-ClMgM9ujC_RTnAy_SgXSjEIP4P6WQv3bJqgoSBF54HQuRLCN2eU1x_n3PySl8Id5w_p86PpdOLZJjq959sMcySue0V4ol32TDAdv7bdcA2aid_C8v1wN5inxFKPe9voCBNIiWAxFL2Kk6VVWJihG-1u_oYAQ8smb91NBDBbrhMws3n9zsZ-ltsxmMNShyVWwJRnao26StIA1G1H9xV4lPeFwtONUOFvvxtb8Hk8fvUXclfmMyzg1t3BTSJLQiqpHwAWNaBYofFaro6nhs_pcdr6PqnNZ94SLBP0GL8EsXRiC_xt2WwCPsmkCOp9A-62al81vRFmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=c-MtuAvP-ss6S-ClMgM9ujC_RTnAy_SgXSjEIP4P6WQv3bJqgoSBF54HQuRLCN2eU1x_n3PySl8Id5w_p86PpdOLZJjq959sMcySue0V4ol32TDAdv7bdcA2aid_C8v1wN5inxFKPe9voCBNIiWAxFL2Kk6VVWJihG-1u_oYAQ8smb91NBDBbrhMws3n9zsZ-ltsxmMNShyVWwJRnao26StIA1G1H9xV4lPeFwtONUOFvvxtb8Hk8fvUXclfmMyzg1t3BTSJLQiqpHwAWNaBYofFaro6nhs_pcdr6PqnNZ94SLBP0GL8EsXRiC_xt2WwCPsmkCOp9A-62al81vRFmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
مراسم خواستگاری دیشب کف نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104234" target="_blank">📅 16:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=G08BDLftpBx7wV9BR1jaUPusnV1KmMpgbA_PnwLNUcWwcOPRM3qCViBoVtKZZS9d3h3UTH_ZdAIUpEe7KeBHhEU5oT3NPKAqs6VF9wnUOsH_ezgB43bJ9XyRmNGx33wW88TI4wFuv_V7XLwOykDwnADwI5hP6gnIIlZE1a7qAoDO9QpujiVd-s3qhur25FY4nwCTv8OBhUa0G43SUCjQmOy1RX1to45mu5dHZjLKT2k7Bu0fbQNT1xzQirf9C43B4LwUc27r5EMuD271o8zu6q527f3Cj9NSmwmyDHRKqeheow2jrDigjvvLv599aQySb_ytvaZSrc070lUNpy-9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=G08BDLftpBx7wV9BR1jaUPusnV1KmMpgbA_PnwLNUcWwcOPRM3qCViBoVtKZZS9d3h3UTH_ZdAIUpEe7KeBHhEU5oT3NPKAqs6VF9wnUOsH_ezgB43bJ9XyRmNGx33wW88TI4wFuv_V7XLwOykDwnADwI5hP6gnIIlZE1a7qAoDO9QpujiVd-s3qhur25FY4nwCTv8OBhUa0G43SUCjQmOy1RX1to45mu5dHZjLKT2k7Bu0fbQNT1xzQirf9C43B4LwUc27r5EMuD271o8zu6q527f3Cj9NSmwmyDHRKqeheow2jrDigjvvLv599aQySb_ytvaZSrc070lUNpy-9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نحوه استقبال از تیجانی‌ریندرز توسط القادسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104233" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=iSRQeQH0lbR6OCzDmTT2SdobSWkcKm19RCj7xfJf_NQebeqGKOv5ynkffaCdhTIHHREo1G88Mgws2z0R-mp8lLI0JzPl7HM_CgS3XK49xpSd97SBD8RLLk-Yrj4rCOrqjtGeB0BxkW-E82FHRXhoAxi5ux0uJmxCcY9VLEj0lsh9-vWrZ_dDwJlc2VWBO7i2GMtQv8wPeX16r3S0XayCZCZfmMSa0VBy9zazHsFsys2fKUcaCEgnilY5-xj6_Gposp-p1N_4ynSjEijPQLmBWY4zCruU-v_otwskaABp4EjexcxDAmaG_QvpkaC1Q3BVRk-Mki2o7WjoXzjBGVn8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=iSRQeQH0lbR6OCzDmTT2SdobSWkcKm19RCj7xfJf_NQebeqGKOv5ynkffaCdhTIHHREo1G88Mgws2z0R-mp8lLI0JzPl7HM_CgS3XK49xpSd97SBD8RLLk-Yrj4rCOrqjtGeB0BxkW-E82FHRXhoAxi5ux0uJmxCcY9VLEj0lsh9-vWrZ_dDwJlc2VWBO7i2GMtQv8wPeX16r3S0XayCZCZfmMSa0VBy9zazHsFsys2fKUcaCEgnilY5-xj6_Gposp-p1N_4ynSjEijPQLmBWY4zCruU-v_otwskaABp4EjexcxDAmaG_QvpkaC1Q3BVRk-Mki2o7WjoXzjBGVn8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه امیرحسین اصلانیان از اسطوره فوتبال ایران احمدرضا عابدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104232" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=smhc-L0RKjvm6p0RpP02mLgVKoQ9udFFxPYZY59H-WuYaJD3POIr3SiB3T0yQ_QALPMk1uzVXqhJn2upxEUhsDwcGTUzfe76EXB2wY1hf4cUzw_1_mic5Lvrnp4s2Mlfr7aZHdMgAubCHaPPDOUkNmhwpybhj10FvSOA5MTcCtZS6kuWk_si7Z5cUjLxtgW0PTJV1Sl5z-VQzb8YI5SomkozyH75PK-sSUyP4wz64bgOPpUQP6zCZbhTrUbMw6m7fCnbHDp9NElzthltru6u4xmZYUGL8fgzpUX8sz1Kg7beUw433qOQhYdtfO1zId7cFszz92JJDPx8lmRUW-CGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=smhc-L0RKjvm6p0RpP02mLgVKoQ9udFFxPYZY59H-WuYaJD3POIr3SiB3T0yQ_QALPMk1uzVXqhJn2upxEUhsDwcGTUzfe76EXB2wY1hf4cUzw_1_mic5Lvrnp4s2Mlfr7aZHdMgAubCHaPPDOUkNmhwpybhj10FvSOA5MTcCtZS6kuWk_si7Z5cUjLxtgW0PTJV1Sl5z-VQzb8YI5SomkozyH75PK-sSUyP4wz64bgOPpUQP6zCZbhTrUbMw6m7fCnbHDp9NElzthltru6u4xmZYUGL8fgzpUX8sz1Kg7beUw433qOQhYdtfO1zId7cFszz92JJDPx8lmRUW-CGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
وقتی میخوای بیانیه یک باشگاه را یک نفس در ۳۰ ثانیه بخونی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104231" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=WeNc6ZPACQmCrP0JD-nvOvzj_gyAfuPZ5FP5ohhsDMtklYEeY-Mb4cfRwS13EpHP8ZUy_OvJEM95_JbowDd0fge6Jpna419dfwBRGH00XytGAEQ0YEjVhRCxkeeubf2Y7sTPhpOAoa8OYi9LJp28wo06yJqnoFqiJpR2VgKTiSyQYr0UZ4AY8aF1OqdImbudMgDGl9gOwKS_ic4yMUo84ujznEO8rXLEeDbs-r09Etf3PVNdU9xsffEpw6J_dBI1jn617pP_mwVlHw-0O1fsqMlPPp0wphqKSolK9h--pD9A6C6jGp8WqTbkZiExDpuVpNy01tfsOM3hQuQlibcAFHGuX4CWCVM_ePg_sR7IiF4tTkV-_pETRLrchTNojbB45vjr_RS3rE5gfChG6oJYKcipMqnrLqPuqVORjSQfRRTXayrniN41_QnlBRTgS02UEvTVxDMcD7O9DA613lM85IAtqjVcuxAXT1OdqNa8z-VwPKF7sMnKYzxGxnAcf8J2qU1ABXovo4bbrji-8Yyf4G3VHsefvmaNMgUsm7SRFulj0HkhcbEoOhGdGhSKD75Yobvj4bFR_n0r160XCe8MTyvYUYv0MgJwyAXNvtoJ3zo-tJpWge3H9_o1NZ5o83V__GLpP54bvxMY6w6IdCyyFkALSXbi3y3jJ6Nxa7aXQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=WeNc6ZPACQmCrP0JD-nvOvzj_gyAfuPZ5FP5ohhsDMtklYEeY-Mb4cfRwS13EpHP8ZUy_OvJEM95_JbowDd0fge6Jpna419dfwBRGH00XytGAEQ0YEjVhRCxkeeubf2Y7sTPhpOAoa8OYi9LJp28wo06yJqnoFqiJpR2VgKTiSyQYr0UZ4AY8aF1OqdImbudMgDGl9gOwKS_ic4yMUo84ujznEO8rXLEeDbs-r09Etf3PVNdU9xsffEpw6J_dBI1jn617pP_mwVlHw-0O1fsqMlPPp0wphqKSolK9h--pD9A6C6jGp8WqTbkZiExDpuVpNy01tfsOM3hQuQlibcAFHGuX4CWCVM_ePg_sR7IiF4tTkV-_pETRLrchTNojbB45vjr_RS3rE5gfChG6oJYKcipMqnrLqPuqVORjSQfRRTXayrniN41_QnlBRTgS02UEvTVxDMcD7O9DA613lM85IAtqjVcuxAXT1OdqNa8z-VwPKF7sMnKYzxGxnAcf8J2qU1ABXovo4bbrji-8Yyf4G3VHsefvmaNMgUsm7SRFulj0HkhcbEoOhGdGhSKD75Yobvj4bFR_n0r160XCe8MTyvYUYv0MgJwyAXNvtoJ3zo-tJpWge3H9_o1NZ5o83V__GLpP54bvxMY6w6IdCyyFkALSXbi3y3jJ6Nxa7aXQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
کیفیت دو چیز در استادیوم‌های فوتبال ایران تغییر نمی‌کنه؛ اول چمن‌های بازی، دوم ساندویچ‌هاش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104230" target="_blank">📅 15:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=qf35DbxPZGF63uT9cJioBQNDDgIGqlyDgsU-9SLFyrSj7eEEy5asgnRyBGUr2gjxo5dioLdS6HRNKiurIgA60SfHicSrVUXbxhD0Fo00Y9ANthwfpL2L0BEi4q1BH5d27IsajWVMj_epvMR9LydlVMezX1Lin3UkJeMPM_JVV2ePRLxEB3UG5d8sK-YVemQq6VZSC0kjq99BmJonG95d73zodVBdcDABUeEoyX5OPdTiSYJitWVgvvCEgEG_hbzbVa-Ac5O5jKb_70OtJqb5cwiiDWjceJ5v7oChAeqdFZ23SxUChBnk9Y6RqcdJtDF2ZesAV42ryHnc4SbEhvbd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=qf35DbxPZGF63uT9cJioBQNDDgIGqlyDgsU-9SLFyrSj7eEEy5asgnRyBGUr2gjxo5dioLdS6HRNKiurIgA60SfHicSrVUXbxhD0Fo00Y9ANthwfpL2L0BEi4q1BH5d27IsajWVMj_epvMR9LydlVMezX1Lin3UkJeMPM_JVV2ePRLxEB3UG5d8sK-YVemQq6VZSC0kjq99BmJonG95d73zodVBdcDABUeEoyX5OPdTiSYJitWVgvvCEgEG_hbzbVa-Ac5O5jKb_70OtJqb5cwiiDWjceJ5v7oChAeqdFZ23SxUChBnk9Y6RqcdJtDF2ZesAV42ryHnc4SbEhvbd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
🇪🇸
وضعیت خط میانی بارسلونا و رئال مادرید در ال کلاسیکوهای این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104229" target="_blank">📅 14:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=b2YgW76xvt8a9XaNmmdaiGfF_9ge-lrsHZnWaAeeIW_AkfyPNDwxNmXTPIAPlVO-kMNDA5XEmnwRE6WplnRfe1hjqsL5nibMKE6r-qJMnBBYeFZuylK6W4z0g5970Dq0voaM2pVtnC1-sYm18mT0umuvWRq8GNIsNbaquDKuGUGz-EYFEBnnSW_LFV2AbtP0_5msRgH8Fddu6Mbkr6wCeedSLHDONmaaAEpY9LkzIxydTevigpNFhc2DDfsJSY7vs7br3wLKx7upFreS-S4KLOgtzvDreFLMFUkeVjmAOiXgMkpb78Ghm5jMuXnNBYJOTh4QrB-OLobY0Mvv47R6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=b2YgW76xvt8a9XaNmmdaiGfF_9ge-lrsHZnWaAeeIW_AkfyPNDwxNmXTPIAPlVO-kMNDA5XEmnwRE6WplnRfe1hjqsL5nibMKE6r-qJMnBBYeFZuylK6W4z0g5970Dq0voaM2pVtnC1-sYm18mT0umuvWRq8GNIsNbaquDKuGUGz-EYFEBnnSW_LFV2AbtP0_5msRgH8Fddu6Mbkr6wCeedSLHDONmaaAEpY9LkzIxydTevigpNFhc2DDfsJSY7vs7br3wLKx7upFreS-S4KLOgtzvDreFLMFUkeVjmAOiXgMkpb78Ghm5jMuXnNBYJOTh4QrB-OLobY0Mvv47R6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هواداران فجرسپاسی در بازی دیشب
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104228" target="_blank">📅 14:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15540c4079.mp4?token=gkC4Bokc0eeastZClmIvkipF9vp1cuWjkDlni09ILtZV0qlqLWeIJXPhLUBEfYX1aOByECNNKm3LwkQ-oyFIHoM9qUiNcm5OwAE0B0SU64P4LDH9Ffspw1RKy-QIbrrWgh8O5Qsk2IM6-04wpaIZBtWdfXwt5xUGcLnbNNxgtJqjywk64X5QQOkqz4H5Rj7ikMLx6SpGr8wJ8auoKgOfydRgX-pURgA2Ope8HIED-3vh2YBkzzYdcgpZImW9OVVw19-vlWZe2k-brM3Nq2pNff0JegxWApLuBHA5m1H6d6xsYeVWIKGYood8CTTGxdBnQbXHy7ajoYGeP8sZJuuIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15540c4079.mp4?token=gkC4Bokc0eeastZClmIvkipF9vp1cuWjkDlni09ILtZV0qlqLWeIJXPhLUBEfYX1aOByECNNKm3LwkQ-oyFIHoM9qUiNcm5OwAE0B0SU64P4LDH9Ffspw1RKy-QIbrrWgh8O5Qsk2IM6-04wpaIZBtWdfXwt5xUGcLnbNNxgtJqjywk64X5QQOkqz4H5Rj7ikMLx6SpGr8wJ8auoKgOfydRgX-pURgA2Ope8HIED-3vh2YBkzzYdcgpZImW9OVVw19-vlWZe2k-brM3Nq2pNff0JegxWApLuBHA5m1H6d6xsYeVWIKGYood8CTTGxdBnQbXHy7ajoYGeP8sZJuuIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
متفاوت‌ترین جشن ممکن؛ یک کیسه پول پاداش برای بازیکنان؛ جشن متفاوت در رختکن دینامو تیرانا؛ رئیس باشگاه پس از صعود به پلی‌آف لیگ کنفرانس اروپا، با یک کیسه پر از پول وارد رختکن شد و میان بازیکنان توزیع کرد.
آردین بارزی با این حرکت غیرمنتظره، پاداش صعود تیمش را به بازیکنان پرداخت کرد و جشن رختکن را به صحنه‌ای متفاوت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104227" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtNk6XwSWsfWNG5glacVXunrBmOb4odcuoTp5QbdvItrQSVq64UWLILxft2RsI2DEFbjZawwpEY2DvMh7RvPK7L0mBkEcEDeH5tttWVk5Kh-TwgBw-OCJ7SWF4gwb36ZEI-QwB8Qw-gIX7_FK9LW32mgPqkL6VclyZ3KFhsjj62iUSwifazxdMN_jbe7s1DUiKIw_BaX7YuncebYuVkxUIIbUeEpcsEax86NgT49z7-qGL_bxEgwynDY1V59xdlVXgOosobT7SWO4W_7trToifSqlvcdszX0ctQ9KhA6eGYEOr0Z52VEJFpO5uF9LSz4EEhyuXZLQtxiVE74IUXNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: بارسلونا از جذب آلوارز ناامید نشده و دنبال راهی هست تا در ۱۱ روز پایانی نقل‌وانتقالات بتونه این‌انتقال رو انجام بده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104226" target="_blank">📅 13:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=C8oTjCKq_PR88Z0Gpy0FA8E2Uu6Hm9SLo2UsFmY4IAPfI-DUaE3pd9KwzBhRyeBYQQJXXZMJt2jhMyl86s2bNyaxG2RRS4LAfASCJqFJ0VbQVCN1UyF2hy7Dnf9770NvDIykDHsziZAPjFvSYGkK8QyvWDxGzWnH5UKLtWJS5r0fBGUOdQgiFmDAKhlgmOY35DNawQgJBA5-YaKcOMrta4xAhdIcxARPApZylxnBSYOOV4_iS5xw4yFMgFBLpxsVa9qiSF63n4EXwODg9jEymuFZnRuHypqz5cHneBDr4xNMneJmjKa-ZL8WB33vkMRk41PbhPhrwDd3xUESSM4NzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=C8oTjCKq_PR88Z0Gpy0FA8E2Uu6Hm9SLo2UsFmY4IAPfI-DUaE3pd9KwzBhRyeBYQQJXXZMJt2jhMyl86s2bNyaxG2RRS4LAfASCJqFJ0VbQVCN1UyF2hy7Dnf9770NvDIykDHsziZAPjFvSYGkK8QyvWDxGzWnH5UKLtWJS5r0fBGUOdQgiFmDAKhlgmOY35DNawQgJBA5-YaKcOMrta4xAhdIcxARPApZylxnBSYOOV4_iS5xw4yFMgFBLpxsVa9qiSF63n4EXwODg9jEymuFZnRuHypqz5cHneBDr4xNMneJmjKa-ZL8WB33vkMRk41PbhPhrwDd3xUESSM4NzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
خروج صداوسیما از ماتریکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104225" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">▶️
🇪🇸
هایلایت بازی شب گذشته بارسلونا 2-1 الاهلی مصر با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104224" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=DRzTlJIEYRyv-A9OTEOG6DAHeiBGTraX3ktb_f2XsTMUqiiKtP-9JHlQyZk7naWfaUcD6jrhNoysgP2vvVJMpp3dUwFoJ5p4mZMrWcQHGLlgYyFLCX39MVsxBiFA0yxRg6clk-d92nhLoGOlFATo4bzSXfEk63l9SaUwvfga_SlNk4kKhPqCOpqGQd4WkymYtHaqrhz9ktPQt0hHMk5YDpL9Oq9GyoZQVyrlhZwqD9h3LkDcWZ8cPpWSUabKO-nqLWFneqVcyofApoX_00Let50uDxvkDc6UMo3yMNfzy918cM9yEcNva8sjG0UbL6cWcmg4DLgOwIqB3MRTbXjD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=DRzTlJIEYRyv-A9OTEOG6DAHeiBGTraX3ktb_f2XsTMUqiiKtP-9JHlQyZk7naWfaUcD6jrhNoysgP2vvVJMpp3dUwFoJ5p4mZMrWcQHGLlgYyFLCX39MVsxBiFA0yxRg6clk-d92nhLoGOlFATo4bzSXfEk63l9SaUwvfga_SlNk4kKhPqCOpqGQd4WkymYtHaqrhz9ktPQt0hHMk5YDpL9Oq9GyoZQVyrlhZwqD9h3LkDcWZ8cPpWSUabKO-nqLWFneqVcyofApoX_00Let50uDxvkDc6UMo3yMNfzy918cM9yEcNva8sjG0UbL6cWcmg4DLgOwIqB3MRTbXjD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇩🇪
قوی بمون، جمال موسیالا.
❤️
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104223" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHURMDRf7-7dvFkIHb2fZsG9--wSleTSUqvQONirF2qbGp4O_FLdUiF6ra_pM4NB9zc-Ka07T0KKiJN5UbxF8kwS4l20NLWD7kl-uP49GQRIB2vgRXavy-F5xNyz8dcUo8eUlcKTQXJzGnQ5lKC7-yQQUHNjdSctn25zuiu3jjM-Boe2N1Cg3FMZhFhTnb7m19ZKLhVhHi7kUCvVHiVPAMW8Iu65Cq1hJnjwiYKgf_MpUZ2v_KfRmBUo06X_sBQ60lRteTLCH_vCrQXXOr9hxIHGMkLFTpT4QhZbnXXUJB11cciKcFXflaUHcAFoMbTv1ot9jcLPqIpVegqd0bNkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمامی ورزشگاه‌های فصل‌جدید پریمیرلیگ انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104222" target="_blank">📅 12:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=nd302cMKuH3oTlmrgm3GzMnDTJdupYwhfUbLwGPk7uuG5lkVmDzZjoDgXoxBzKGVH3v5qJr_e5O5aUhuah7DAFdL7Y7pI2BhNaydwS04BLL9URPgcElhSi2ZlBnaXbM3aHJlGoXD7a1F5p8-Co23Epo6dNn5mUlz5jiRnf5Uw8VIuTorKy7cDHXqrnnd58FHSEu6A6IAK3kCKdDERuMkhQ47cBoMzgvPIVVAUgKvunvaGZxeBRXwS-48IuCdlMtFG9vx3heRRy0dQ_xxAf1OdZWMPS9s-mfQG4P6ePtMU1dJ5lBxfnPWFhJ866gydJo5c5Dqa6pT2B5XY8TZvp6BXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=nd302cMKuH3oTlmrgm3GzMnDTJdupYwhfUbLwGPk7uuG5lkVmDzZjoDgXoxBzKGVH3v5qJr_e5O5aUhuah7DAFdL7Y7pI2BhNaydwS04BLL9URPgcElhSi2ZlBnaXbM3aHJlGoXD7a1F5p8-Co23Epo6dNn5mUlz5jiRnf5Uw8VIuTorKy7cDHXqrnnd58FHSEu6A6IAK3kCKdDERuMkhQ47cBoMzgvPIVVAUgKvunvaGZxeBRXwS-48IuCdlMtFG9vx3heRRy0dQ_xxAf1OdZWMPS9s-mfQG4P6ePtMU1dJ5lBxfnPWFhJ866gydJo5c5Dqa6pT2B5XY8TZvp6BXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
برگردیم به زمانی که گرت بیل به رئال مادرید پیوست و EA تصمیم گرفت به این شکل تو FIFA 14 پیوستنش به رئالو اعلام کنه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104221" target="_blank">📅 12:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری داوود سید عباسی از شب‌گردی‌های دردسرساز ستاره‌های تیم ملی در لبنان برای دیدن داف‌های بیروت در سال 2000: زور هیچکس بهشون نمی‌رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104220" target="_blank">📅 11:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104219">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=YaZLx_G00dVCoXZUv49YOIZTfIJkbWHrRkzPsM_FpILolHB3gQPW-4hwimT3MUlVYkHgb738yvtKbwa7zTnkjaNIvFLn6Mhiw2rZW4xMY3ImRGeoLmvZBJ_8td9ee6qUO-mHwR_YIzlHwgnUIJL-xvfIyayJNt0eDOsEix9DvT2YNhz92q_Pow6yX5kqFX8DOEAk_R_yMASe-fxEgBcE37VYgM3MR5ePN9_r-Z74B2pDFnBfFc9ZgJwcJF0bsyn3UgIPMxIiucA-LgihRn5LwNeA8OwX8CyYRn1M1_xgUe_oAbfeih92xnkZ4xGDMoYeIPQjduINZh166A7QX16O3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=YaZLx_G00dVCoXZUv49YOIZTfIJkbWHrRkzPsM_FpILolHB3gQPW-4hwimT3MUlVYkHgb738yvtKbwa7zTnkjaNIvFLn6Mhiw2rZW4xMY3ImRGeoLmvZBJ_8td9ee6qUO-mHwR_YIzlHwgnUIJL-xvfIyayJNt0eDOsEix9DvT2YNhz92q_Pow6yX5kqFX8DOEAk_R_yMASe-fxEgBcE37VYgM3MR5ePN9_r-Z74B2pDFnBfFc9ZgJwcJF0bsyn3UgIPMxIiucA-LgihRn5LwNeA8OwX8CyYRn1M1_xgUe_oAbfeih92xnkZ4xGDMoYeIPQjduINZh166A7QX16O3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه تند هومن افاضلی به نکونام: کاری که با محمد ربیعی شد بعدها با خود نکونام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104219" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104218">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=aNi_fTbHhIRbsALXCA09m86aHFaCaM3gcCpW_ZYpZyg2WPUlE6vVlDf23ecCCkfCX3XqwTCyO-17LhdwuIxHeMaRgkIyP2sRenLZGKgvL7fd9C3fsHQFW5UO-4zF9BAhNzIoNGXXSFunvAahGVKlpY7PQEOTCK914QiVazTG7EoaKX75Ghyp7cMA2-_zaafl_26BoSHJM4AOVyJsI0aZL8qI4g6SB6gGnFwDaNeq-bJWdP3M_zDZAEVDR1BUbgBanh3vESQF7FzEtqQygtt3IqXZUebdwwiQiOrW1N3hRANM1DD4KMuiTYvvPaYZi4aXynhQyWR2IOshvsUDho73Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=aNi_fTbHhIRbsALXCA09m86aHFaCaM3gcCpW_ZYpZyg2WPUlE6vVlDf23ecCCkfCX3XqwTCyO-17LhdwuIxHeMaRgkIyP2sRenLZGKgvL7fd9C3fsHQFW5UO-4zF9BAhNzIoNGXXSFunvAahGVKlpY7PQEOTCK914QiVazTG7EoaKX75Ghyp7cMA2-_zaafl_26BoSHJM4AOVyJsI0aZL8qI4g6SB6gGnFwDaNeq-bJWdP3M_zDZAEVDR1BUbgBanh3vESQF7FzEtqQygtt3IqXZUebdwwiQiOrW1N3hRANM1DD4KMuiTYvvPaYZi4aXynhQyWR2IOshvsUDho73Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
حمایت ترانه علیدوستی از ملیکا پارسا شاکی پرونده پژمان جمشیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104218" target="_blank">📅 11:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452261b723.mp4?token=rPte946P8lgkr0u4Heuypsxi_hKEtfigGJ9UFAgylZGku7Clf23kpnTi99pWWvqBJWR2pNzUxnYNDvnruJ5Zut4EouABIkwxxkVDTrdpNmZ4f7tibavyfFmVP0YTWuCMFmUa_VOcAFtdCvF2uwHnBgPeRcGpvHEW5EN9t-D5bNA0yuZ9OvK7b0NGvtF4A9W3tshoiq1b3hxon1JDOPy1UFpiwaM5fuqm92fitdkX0XSKCfu57KgXDyV_NTJD5oQFPfg9p4UnQoVACdv3ymWHVZkTUI8A6t2weYIyZKkhti4d6B4gZsu-Xx18j0HkTwVIXZhGJfTG2HvQSO5uodjht4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452261b723.mp4?token=rPte946P8lgkr0u4Heuypsxi_hKEtfigGJ9UFAgylZGku7Clf23kpnTi99pWWvqBJWR2pNzUxnYNDvnruJ5Zut4EouABIkwxxkVDTrdpNmZ4f7tibavyfFmVP0YTWuCMFmUa_VOcAFtdCvF2uwHnBgPeRcGpvHEW5EN9t-D5bNA0yuZ9OvK7b0NGvtF4A9W3tshoiq1b3hxon1JDOPy1UFpiwaM5fuqm92fitdkX0XSKCfu57KgXDyV_NTJD5oQFPfg9p4UnQoVACdv3ymWHVZkTUI8A6t2weYIyZKkhti4d6B4gZsu-Xx18j0HkTwVIXZhGJfTG2HvQSO5uodjht4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل‌جدید هواداران در استادیوم‌های ایران
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104217" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104216">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104216" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YINWlEUNv1fWzYEIBPFIIAFruGC_DCW-kwQ2JASMXeTnIg_YGphjgKmTyfOQ8HDdHA0TBS2JePXxutKCI1RKbYmMTNI9lHsAlQ61KwKafYX6bkAk9Q3y27gxfsHMlhfIEDkWr3XcLdFQI49GH7G_a0LsbZZTOHU2kSo4tB1LcghbhY1JjJx8bmK2IRblPAXIxsPw4pEAl-fam2w8ZmcmIDVTTRhl5-fkuNhX75XLRaIHzwBuEFVCPYboq2Yz7vs7vM7rRPM3K5HW4U6gsfgKzgBUGA_WZka8Herb7XxYzKjB2Bu4Pp553DCK4ThsBuL1VdMKE-0mHozMKxBDazV05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r29
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104215" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=QJxCHnbg_PkWkqgKfYO8MfvZ6Xk41Ic7s5jO9nF99CLf7v4vC5SMy4pLF4T3cwIdx498fAeic9vjM4U9U0B2llbvGt0xujePofegswDi18pE7z5xNEmczPLaMWz7UTOvTNO_6cT5BZfrUgWV9JOgqz32OTC5lACqFhhEZSL-bmygA-kZAp4B5592EdRlpW6IKyfRNkcqqRhDbJckVC9KUr55ml6ALmnQlCOyuu_HzXMbQJHeQWC0k4qQ6VXvTN3kBO8kr3PfanSBwKtprb3ZaDpWykLkBTOdOTVgU2Xr0EsMgbr4AXhtYcIi5Q8GwDZuLZeCNHIzhBXs6rc0rdvAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=QJxCHnbg_PkWkqgKfYO8MfvZ6Xk41Ic7s5jO9nF99CLf7v4vC5SMy4pLF4T3cwIdx498fAeic9vjM4U9U0B2llbvGt0xujePofegswDi18pE7z5xNEmczPLaMWz7UTOvTNO_6cT5BZfrUgWV9JOgqz32OTC5lACqFhhEZSL-bmygA-kZAp4B5592EdRlpW6IKyfRNkcqqRhDbJckVC9KUr55ml6ALmnQlCOyuu_HzXMbQJHeQWC0k4qQ6VXvTN3kBO8kr3PfanSBwKtprb3ZaDpWykLkBTOdOTVgU2Xr0EsMgbr4AXhtYcIi5Q8GwDZuLZeCNHIzhBXs6rc0rdvAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تمرینات نفس‌گیر وینیسیوس برای دلبری از ژوزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104214" target="_blank">📅 10:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWJeetACTdqQheK8N8bzusTGD9Z1r1Y9lX2vLvzKmbiMabW529jy6NV8cbbTdefCG6LMgcPnnOp6ocWrAjjfcNZQ4KnOBfP2qR8F9FB7zg7D0uk66fdVAwDFy_FurS2c3OnuaNjJYEhjMmzgcyiLqsjWoHGkdgBMgHk_SkY8dfecxj__WT_JAo9zepjkM_OUbAUeRKjnx04pt9cIVZxWjD2pH6HpLCM18G5n9kPDcZOT4lBOdbHfyvrxT7bCB34w3SqnuoXHpEnYlfJt3pg9oNiWKaO62-7NNW64IL88RB-TLZad2WBNb3yHpkunJEXoMru7QGT_7CjpROcYruuZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4yqFijnsqjaIyuTlUGNlQuQrN9grku0QUP7qx0-NMoURs9N0onFWCVGa-pxtm-w2SGOI4T_hk7zPZ3bCaQShdoNzGoCyhJDBXtU4vWVV55gCUTlTIzMCDofbqufpl3JAdKDRg49DeG1MqXTv1WEsavZLdOLViurZQbQdoYKxHaFLgcrczvuYud3G9clrQVc9WthF-dmH6r-bX-eek-X_2Rw9efvdKwM0pjlMYqr8aqL_E7eOfWRbIhSNzg4hZ1TlQFyei9I3VFu37X13fQaYUorc-OVPAh6RkgFmJvGNfH9i6AR9eWBacE04YRVP4lGWqY3aBye9yHgAfZH4f8nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_pcntY3lXHQyOhN37xN2F0PaWb71ET0sm0C1e08HZ98UQPs0ZMrY0EoyebTAwgJ7uQ9XnKsRG60FIhVYmoUqXFiI4Mm1tSkIACubDSctGcssiUBbUm2qIKmu3XBxtW9MRwW4OwOZt97ozPvJbE2UOGSymhn3rHK-ZLxEvGc8K2bwTsxXxCHPyoIRSe3KXKjBzH9UtNR9WB0j7PSd2pcBG8alvh-yKIivbYh23gslsvcl410C4nZQ3PO5FcoQJX8JwZS51qRsd2ewtrADlHFT8ODMCOmdVkFIJf78k1Nk6mrItaaHnkiPF-_hhYwDcltCH6khrjNIvTxyeefcurcjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104211" target="_blank">📅 10:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268128aa94.mp4?token=aEV2pfgkxB1V0P5SaCwp5UKjlBmrl0WY5rG6YSM4ilVdn_uyJgWhczboEuJsSP-yChKu1mwmUDfOcPEilhjctjhWRamJ8jN9spE3A90IndbqZMMemsucFvWsLOlXMpCcAfC7kq5tRv3BEZOaZR3eKv947zD-7Go9-snCc9m1JNOdhFZGYBjh7AZpLm0WnAokZmYXUwZNGrKks1T_yrVLJqrUGk4Jdo3eu3uAUqY035fgLtfvgvuWSEeHC93TUN_GBMcSUMZq3Z_VwaMDRbyhaJTt9HzLIU1yrK6H6KS2EPpZe247F2cCNt5cSB37DTT9Wk4qwaMzObZy2-LIq6PMH10vExftycu2Bkg4NxW0DeZWxEKasHKTNnZNCb0q1OamMzITwzLHouDZwhnwcQO88A60L8Wlp_JH9L4juWbr7srM6MDo4yQWCQdNarsc4j_wEqRDZGUqqs1GXGgxCFeKG72K0zWsdbSKt4XzVWtx5xmIUu-RXTsNjfAFBrFCgfTIQKWF4QtL5MCsTb5bIu9g80SAZIYfskdeqGzk4DqhtVcWZWwOt6dja6QxHCaoFiWJfdScVhB59RueEbN61EtmaUKUV2M3g4vSK_c5sRnB-pXvGljS450O0bHMhr8NdhEVpaQ-CqvYf872nRMu7TkvmBfYq4NBh3i4_IAHHRqr4es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268128aa94.mp4?token=aEV2pfgkxB1V0P5SaCwp5UKjlBmrl0WY5rG6YSM4ilVdn_uyJgWhczboEuJsSP-yChKu1mwmUDfOcPEilhjctjhWRamJ8jN9spE3A90IndbqZMMemsucFvWsLOlXMpCcAfC7kq5tRv3BEZOaZR3eKv947zD-7Go9-snCc9m1JNOdhFZGYBjh7AZpLm0WnAokZmYXUwZNGrKks1T_yrVLJqrUGk4Jdo3eu3uAUqY035fgLtfvgvuWSEeHC93TUN_GBMcSUMZq3Z_VwaMDRbyhaJTt9HzLIU1yrK6H6KS2EPpZe247F2cCNt5cSB37DTT9Wk4qwaMzObZy2-LIq6PMH10vExftycu2Bkg4NxW0DeZWxEKasHKTNnZNCb0q1OamMzITwzLHouDZwhnwcQO88A60L8Wlp_JH9L4juWbr7srM6MDo4yQWCQdNarsc4j_wEqRDZGUqqs1GXGgxCFeKG72K0zWsdbSKt4XzVWtx5xmIUu-RXTsNjfAFBrFCgfTIQKWF4QtL5MCsTb5bIu9g80SAZIYfskdeqGzk4DqhtVcWZWwOt6dja6QxHCaoFiWJfdScVhB59RueEbN61EtmaUKUV2M3g4vSK_c5sRnB-pXvGljS450O0bHMhr8NdhEVpaQ-CqvYf872nRMu7TkvmBfYq4NBh3i4_IAHHRqr4es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
فن‌کشتی بازی دیشب اینترمیامی و فیلادلفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104210" target="_blank">📅 09:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08de822050.mp4?token=cuL0uXgs01B5kmMUfm6SXEDcVjbWfXf3bXPfOCpPa4EDWmgfuwZ98qiZ6PMbWcSd7iXDZV-CuxQZ2Oa6aB4c6sqV-GJFh0D8RFLU_wJMa2UAIsaaWvHaCP07lgUnEnhJnTTBUuuMBb0IiaQtvP-jLcSz-kozhPCUkEbxFG5oKMIfBG6oAT7j0G7miCgU6j8HcnC1_ssI2m6AB3shJQjUByAFQ0fAoyh55g645yUSQ3AtceCwrTlos42RG_X4bwXDyU-hmZ-I1o11Eh51S_M6I_7cQASPQr24drap-Wim8mRyqQIHotHAWGp581Z0TpVyTViPPYSljQ3hubkfOwqjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08de822050.mp4?token=cuL0uXgs01B5kmMUfm6SXEDcVjbWfXf3bXPfOCpPa4EDWmgfuwZ98qiZ6PMbWcSd7iXDZV-CuxQZ2Oa6aB4c6sqV-GJFh0D8RFLU_wJMa2UAIsaaWvHaCP07lgUnEnhJnTTBUuuMBb0IiaQtvP-jLcSz-kozhPCUkEbxFG5oKMIfBG6oAT7j0G7miCgU6j8HcnC1_ssI2m6AB3shJQjUByAFQ0fAoyh55g645yUSQ3AtceCwrTlos42RG_X4bwXDyU-hmZ-I1o11Eh51S_M6I_7cQASPQr24drap-Wim8mRyqQIHotHAWGp581Z0TpVyTViPPYSljQ3hubkfOwqjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
گلزنی لیونل‌مسی در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104209" target="_blank">📅 09:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1p0j3N_pdepAyOwPVyZATX4kC1qY9x6m0tEg27x-GM9TiSsB6rpl1OnOmfKpFftzx7OeMU9_ChCOC4yQ25Zc1Td6bzqFKOjrDrDukKgz3q6bac7x2xYKDctirNMVs2-TGBMthhfFlXH06-Nw9ofZP9Q5hgPY8QOwk3GAPku4-lSwrjN14Ec59nFPaEhjp5gx2_krYqCJTIgJ0oSPxF1AqMWuuVqU_yiDiDIZDUtQMtrIkMFtPvKuINlQZq1dOv0R-Ss5qk3frQgccFXDl-EQHz7RYbNOj40Erc1lIkD4RHWGaztYRjr02JkyTlfbTm3BStjj2nL-WWoYwtzCyJ2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104208" target="_blank">📅 09:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=DZYBa_6jEOxot8t4TqqiEo8k1LJ-0-RL3xa7E3uF-ibbtvnfkm6q1WRMXaXU92KwB6ODWWKyKiPSZYZOGt4r0havCfWIZQAeS6I78SxDtOtvBa7JYvYxYSbHXDCKW-QyhOQ1FHFKkIHa0A74favD5YGGYHLggnqnWZDE37y_3k9b2ITe31eQwclTnZLfcbZq1Zcza1f-tDx_qgUV6hCLUQE0JPQW8atsmpjNhxpD-iG44oYffo-HETq7Au4LhXqLZVyTZ9UeVzWaz9x7-OjDLczTlVDG_PAB9zDa62W_AgEjF6beepqpKafe0WQHEYy8HGpo1Iwlc-TiNbiSi6uQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=DZYBa_6jEOxot8t4TqqiEo8k1LJ-0-RL3xa7E3uF-ibbtvnfkm6q1WRMXaXU92KwB6ODWWKyKiPSZYZOGt4r0havCfWIZQAeS6I78SxDtOtvBa7JYvYxYSbHXDCKW-QyhOQ1FHFKkIHa0A74favD5YGGYHLggnqnWZDE37y_3k9b2ITe31eQwclTnZLfcbZq1Zcza1f-tDx_qgUV6hCLUQE0JPQW8atsmpjNhxpD-iG44oYffo-HETq7Au4LhXqLZVyTZ9UeVzWaz9x7-OjDLczTlVDG_PAB9zDa62W_AgEjF6beepqpKafe0WQHEYy8HGpo1Iwlc-TiNbiSi6uQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
آرزوی دیدن دوباره آزادی برای هواداران!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104207" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be7548134.mp4?token=uiKwV1SOrhY6qJ0AKWLb4N5l55psZyjSCSs5K8rM7GQ99YUXu-fHOLhlx9AFqbJ8iKVMsknSlVCwYwqPhJvzVCuCwPFkulce-wCXkEuFOmKbHMcOHWJGy5dpoWLHdRSxTqOUuXeCFEQsGuLmGfkCQM1qURbgplMnVsu8YhV06yXSZxlD_HInls1DlCJmMTlBAE2PCGky4BX3-VbF_Gn4gHJJLNpu1OsPJ_3BN8SNPnJZmdQoN07N8ceuDRD_McdTK3hyriAHJTfVqHhBXYT4glGdaZM-qIyNc8cPEPhVIRWfUOmy95w98WaM-vAlUCY992DP3nDGv-ve16oiDk2gbpKOD0H5TnuMB3RU1W6vpemvkn3T4RabLSyvOFqLhJJgBepkvfPrLWTw88L1pyL2tlY8tsOLwggc0hWYnsHePw5QE0RLIWFL353tBUk30e-IJQr7Cydtc-UjLNFt9jLu629WhUpqPmdcNra9iFSuPvgLlQqFSxm6rBVt9OvNIf4WdaqgxhmkFJ0jiR1HfYPPXUHX5ieJvA2kl9sj17q40-TOAmqP-tdwtijjEQJC_DmN3PI2bbAo7cRgUrqTeBtlPCcuzunYWeh6o--W4V_-DkUSiXw3cuNggmzHUdaV0DVnB5n0CfroI30_f-MOkzGuJz4rM5senfpzDto5dOXC7E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be7548134.mp4?token=uiKwV1SOrhY6qJ0AKWLb4N5l55psZyjSCSs5K8rM7GQ99YUXu-fHOLhlx9AFqbJ8iKVMsknSlVCwYwqPhJvzVCuCwPFkulce-wCXkEuFOmKbHMcOHWJGy5dpoWLHdRSxTqOUuXeCFEQsGuLmGfkCQM1qURbgplMnVsu8YhV06yXSZxlD_HInls1DlCJmMTlBAE2PCGky4BX3-VbF_Gn4gHJJLNpu1OsPJ_3BN8SNPnJZmdQoN07N8ceuDRD_McdTK3hyriAHJTfVqHhBXYT4glGdaZM-qIyNc8cPEPhVIRWfUOmy95w98WaM-vAlUCY992DP3nDGv-ve16oiDk2gbpKOD0H5TnuMB3RU1W6vpemvkn3T4RabLSyvOFqLhJJgBepkvfPrLWTw88L1pyL2tlY8tsOLwggc0hWYnsHePw5QE0RLIWFL353tBUk30e-IJQr7Cydtc-UjLNFt9jLu629WhUpqPmdcNra9iFSuPvgLlQqFSxm6rBVt9OvNIf4WdaqgxhmkFJ0jiR1HfYPPXUHX5ieJvA2kl9sj17q40-TOAmqP-tdwtijjEQJC_DmN3PI2bbAo7cRgUrqTeBtlPCcuzunYWeh6o--W4V_-DkUSiXw3cuNggmzHUdaV0DVnB5n0CfroI30_f-MOkzGuJz4rM5senfpzDto5dOXC7E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زادگاه‌زیبای اسطوره رونالدو در پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104206" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIt5tu6WJ7nTt1VJQIGacC2gQAK5MQ3DUbFCdE79V9n5siGcOZ3VWf5Rf5cJFa8gBhQMsX6YVaBcD0SYjnHKP2uArWmNlzxPv4JSo9aX6xTTmMb0eTNG54iHH9K_fX8H5F8jW-yaNkokJ4aM3GG0ETZW-yoncHdW6Xcsw7CbGKu66Mf6aaSSIJvqHXGWZoCAPmsooxIutu62ByqI5fSHobAvFAdxNrtVdVj1NEqbYRLz47kvj3ZoLaGWdqOAr9CHTS3ZzpZZA2vmTi-jxwhiLUtwyx_nUhIvYqsa59bxzWkkSX1FtGkyEufjidVKJVvi91zq4f1XIXyWculj97rWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ
: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104205" target="_blank">📅 08:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twx7i4RfsQov-GdVZk_T_Dk6bEqTR_gUbxg0kOmwabXro7IL1dXTmPgIjEsZORsTFdg3aZ5QgyM0Pbm_Pl45pLtkILyvype9quTj-p67BLFPNlnS1K0W4g0L4zI345acUo4A1t_1f9p5YnYhAM30rfMuybgk-TfpcH7KZqVRp0YaYIWoQF-JybCbdtNWQsErRGtqfEpHTQ1mOygw5c63b-JnlVqiyfoc0AKNerWF0e0FrTJEa78vBW__vt0BuW1sDi5GFQEBCxJkCgs1asza4FO07XyKVlFBzr1xZK6tDnYCD7L3KrtnKzwjf_20_Hfc6nrejj7nL48T5uOA0T8UCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری یک‌خبرنگار از دلایل عجیب و خنده دار عدم صدور کارتش برای ورود به استادیوم برای پوشش مسابقات لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/104204" target="_blank">📅 01:39 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
