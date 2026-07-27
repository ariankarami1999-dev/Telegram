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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 602K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc8CAtxEjgo1r2AVbxYEAfLgTPe9EMnl87sBBbFck7YhS0YI67j2bFqjhayrWvsdGrcMAsWiLYc9plw3G4L-cO2lXvk0aX_DckHEs1mKHC4ZzgM3aMKvlsIJYYdPg2LvatvOp720filq50knsRcoCS9p5wSTNjUJhtFTJnGDEVmeY7OTehQGDNoFEEutH0I3osjI-_gtwpaXps6qLoW63w76o_ISwuT2CIcTbi7QEUk4CCoaVv1LE5QLlog8AeyAz2d_8s5AG_qgVUeORi0hInXAInheVYBef5W4OEKGM4MiE4TTpeVmOA2sYZOMksLukaQi77f3Vx9Vvz9obulV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 273 · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQS1zVIj1VWgHvShiywc1gnpg-mvBDsF0pmSNneq1z3vNHOaQ6e90sORi90xWQRw1CGjYpLhsA2JYM9PNI67ZcOYApee5aR0wc4lKVQYC73gYIuex7fm2SM2W4Ey2KAxl7LfWD7FMWM3-mZhEitTrpuwbwALdkEIu5siLnjSvo8lfgKDqLEV_3GB4h86i3EeGt2JMixryIJq1V_8Z83FRQv93s_lfMABNAN-36cZ2yjk3G4cWoLgTMprtXEOhTio_UCvo-EtT8tlmL7G1cghFKgHUFAR0n1uxrbwiyplXLA_G8xg20n12MfBK9khi6vG0E0v_GSRSX5pAXfJ5FRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF4IFcE0RDf5RVkJtVqrXVLV_vAkeZGJhd0GqtR90uqERC-2IjX_Av2ae7DNQBPp4vAgr8DRN5gHXELHvZf3KPcShZbKupQKc3y3tum7dbTcROLc8eKh90MmiFgSiJXiWoxqaRNb4eV0F2XkQtqXpj8PuooVx-1STJW4B0do6VEGvIORP-0Igcm6z-xoSFMh06pBfJF7G43sJ2xUdPvGXhDKIvt20GNRpcVfQIVyftEii7_wDQyUaLDegqVuCCNjYnu1F212TbGGjj4p3L77_M7YbqfvXLIUz_mx3_6z5mml5S4naK3ORcqE9KZKgf-6mssr1uK-b6baWvJiXyYSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/26625" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag9Zo2borfYRA5NtMqaRY9rWREmp4xKuuF8hcEOdPrsB5Y_6aIr80R1n8jrvRFdWoyUKMfvmF43edJpk0JThM2SdbUtgiAyPiKY93ZgSbTUQBiuDpKbzIPshtCDRA4kPwMEGmJmHr2VUugEM7qpp1fdbxMOrwhy7Zykcx-lSeaHd0SKoUuhOLecgF_CCTNThylW3n8Ycos95saHy2JAlGz9syCAOHlyTsVlCC__Bes77Ea8xVVMqyEoKVrtqI5H5Z3izD2jI5j55wKPsLt9XxiqpVQCtFX1XZ_IinG2uQ9bFu6sK2ZJbnqVQbGuxcLrYVaEiyZjk_m4ZReWImThoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAPTjzae1IcCUl3Nj17IXKk25bvtUCb4w9MgUlleUSfk4Rin6cq_d7gR_yXKXHgWythCPL8xWaSbV9nSbnrIusQ2a05_0Rq0rJ4zXCcCd9gg1w03Vzwu93-W4Ehim1yg6AxCKqiDCpFnLpVZMvlGMwHzvvXh3v9Vx5O2CBCLjz16QobdcXLKjxcaQSI2QLTz_H_wS87qtBhphULIxtR6Ha8KuD3jDjLYHfuI6wYlqZ-fKTXoCYdGophxXJSkvww1YIdNBFrdM8_QJvbfjk_HbubaduTyCs_zNJZrbTF6kwmaDQ1k5Cs-ufvAUYjDDRS5bX3EajiakJhfO7EVifQNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HevWY4EdI9t1ofsfo5QwqlGIKpVyMQ4jZAKpcy7z1ZyV96jqo9bMPYl4SF1vPp3ca0KUSRYrXnxaWvNUvRAEHY46UYeqYpcr66FGPQ7NreeIlzEC8IQ97ZoREafENzoUQ97DKmbGCWVFN35fb9CsyVEEvSW3jjDHMW9NeC6-CI1IMDsGAXFn6GjVBBPZlXpnLCF54G4vBBfu2Z4CwVl-fAhN60eHuNeE-z7jc5Ztx1WzHMTrR75Y8CP7zTIzvaeA7gGVF_qtCfNqXhNBhh4_f98bmwD1WkNbYhTAjqDjVmKVgH_TeOO4URwUCtAFWN-L5mocBV9k03LG2TNvYQTlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6KoovFOQEwCzSzAtGqxkUhlvPADPxmeQ9Wa7tWo-Hi4arAJJr9nuwsC4z9kwTY7_Hy1w2uyD9UtJMnoaNPaNK6DWOT3pIQbsMbAjDOQLJMTo7r5-TevWZjHFqI-fDzoZ-P5r6YeiiXe3x_ofVULOCo4_l0a8AQvwyd9r44PC0170xU7m1TzR_0YIPC2-vgp3pCtWpPMWSDv6CL6KLO_mMgTNjMRJy6FdNATVQyyQ9A5jhRn3q4bEjC_Dj5m7y3iSmIqnIxlJlhFa6l8ftHZrq3oY5e9uhsUQRMcjHE_MzBonw82TMx0vtIm9hUm_5jPJZeuvPaxOWi0iUzQZFGfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m47grzWkPYPft66UbBbhMSNMu5BLZ-z25hGx12uk-9P5h6BIjb32GeU7btvBwkVG8lArgKPjlt2tYFAtkUbFF82Nt9a2yylzN43hyl4Zm5f50boy-1wFLY29KVia1G_zWjSW4aDDuGrnOYxaj14D6cUhFo_AkIzbxDY1r2c4942uQJgNKoZfW6p64whlrYB3HYZFIz3y-R1gzqbkaeXHS6WRdGi9LIORVEF83Pe07O57JnuoGZ_FTXVdJkPXdgvkmh0qVJ21ggd1WSobJggBxZP0kR7II1sxu3enGKvxcuKlRYj2sdTENINwR2u3L-2CA_JzTPw-Qxi3Hn0O28aEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3C65bpnQDvO2-8yghxpTZiAJLu2-JFtuWIncY4a3B87lJUl4c5ZUbiqnpOq35XpSy37Lz9Pr_Bh-3VnOD93DEBPzGMbevNDqdu0caUaQKpfRanzaXHQ0sqh-xaN7tn9cUzvjNjYTQy1tplEn-2wt0o_4X0wWB9YZmeQV9j1B_ibdft97IVuZUhsxT-BtdowNlp0--9ctfO2Yv8Tsc0u7WjKoTaUaLtqMxD7e4fORtPkGelBA2P5Z-wfKQnDYlcCqCCcja9i-7OehE2nuzFCahrYMxymRLN2zvWU0sUGzGFokBM9ALyJEA412tR7rHFYsDw3xkw8vkxy2aD2dWgzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6C032dX3A0m8V2t0N0P5ar5YJwkR8pjwYMXH3TADPq_KmuDWKYwWZbEwJK3zhSPGdahwJyTMMAQd5aNFgVfzcj9Ylo9HnvwnEWwdVaUSNap2JHE-UfkSIJGeHZXr-JhYsLLWc-0n6EvJCtovFnFvCWeUap78RWfZy18qChEnACEZjn8Ddi8YucRutN-E_HkJT-hs2oieGV2tZW0PocFqpQ8UTxpByaMJxyj3LRMpk4T79Si32aZmuRlpdLzP8jkm2i7rOff-A4lPQdGUrd45ojN2wYkyZiQPL3ryrmVHrP5HNNKOQo2we3IHazlaug2nQbLPY1Aa79lTkbHuHwTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5EDdSDYeyp5EC80AZoqMCsmjVwNcgPvkt6QH4tKi7By1FSpTsE9PyfDUOPQKWZbX0hyXewYhYD57W5Y4rXPyEjTULY3uKg-gc2PkXijHjTq8GWMxEqfEvjYHMggxP1QDSBY3K0rn9U9Yo5jDm4NxUZGMl0-JCaX0soN5hYE0FZiZ64MB9vA6LajzFedplyJbdGmHfTbv-J0Qt0PW5EzoCcH9RuknE7D04q8eq7_X0MeD_3ukShVVE7JNW6zzSQvS84hIk8Nbjn5POEm1JeTP_ElpsLanKFmW0tJubh6uJGMdTTnQlFF5O9XGdCJOp0ZQSac0Lx730oJtUm4F_-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ORqeEggHrIJXkj-0TWGRl23g_CKcjx2nXuFHA0v_4e01Q3racpbrxaEEkjhOuG-sOUk9VzbmvEXPWvVall66JRKZc8Zzx_bqRxMlfSOudZZp3mIqHK1e5bgG9RLuaR67LQ47n7vPIUeA12MYmdYZhMdJruB6xjscaoGd2N02KkyBVGmXyFwXrsymnJupJwm9zMLI02_LaII_j-fF-0EF3GdX8ucrD49wXdENZ5aTXNvYYxWEtaqnx5hbncKtOQmx_G2ptEpXJrFF5TrO8NkwbhSgpcCiKZefhqyUl9PznojkmN8R0hiJPc0syrqZg-j7TB8miz0mDm3OC_p9VfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJWwgR8EJolmuAlDRWREtAk3BK_mRhyUTzMTgFdkThE9_gKngU43qBHMKrj-0zyjyWd6ftCLlJX3aHWIVHf5-DbVAC4YzZThgDpu2yQI_psHXQjlRd6CmpwEC8HFfZvvuCmCqCskBGFniyUvTTtjpAcugJPyZXpR9X9azl7wzuAa8s0qdtA7voy-ch7huM-Oalwi7KoNgmB60rp9rmu1pGik4N6bK_PiyK5TPYIQF3CkxnfNf9D5ExrYgeL8icWF_rxhbeagDchPrnQw5l44iLvTjQnY6vXFHenPVRyqao0ca8Ug9jXx4O-ORdoIUjuOtB-Nk9kB7rHhYJc-grItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esrgE2-IfiZhg-XvHPQbyBqfbQwRVrffh6PgP2k1eOekn6D770b8jtRzxZW_VUZsxMHuhEMCw3lxq3PNQXlonDYyesfzeAdJhk-rjyTTmC7le5adBDqubVRfDU35f90SRX6cBGEOY2WWb6boWlao3LhN009AXh-XfmB4PbhcwdnCDEasUQSEPA2szCLcgJxgnIjVN2NLKOT3vNfbPXLHz0gUmB_XzhwIMao7BOGy9jjd5gf7nO51PBH_gEEDoR9nVgEsEt4nC6wa-PS6pvvbFhDpvTpkGQHAdCst4Q5XW26wtuPs0WadTjpqBb8L1ij4LdCbLDjVsbHkYijJv2OOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwkTNWfCjXt2ccv_AAkJUhF963HyogEzS-Gh6aKoPtc8b9S_19SoBa7xgYGFFItBk5qXMzGbMH3xJnZhB73VV4Q4s6qoRwijYqtt-HRy91W-023jliBCu7XS1bVcUedWexKYeqQRZ9RZKz8r1emLX-7fbQi7gfV0_SUC7Ad_JKDfhqVnXOcZ8Q00qcpNbI-k7vvw5B4J6t1jjlCDpH3eFp_Kh-U5dUcbhfALsIXO-YGGCFOhbnZlfvFou2N1_TTuUnGqd6KGD1IxVrmVet-YTNrmiBFH4QzkKaqu_VGv5GuiQ-oWF0M1RoASRcyljtYfRM47w6PTp2TPL9qalO_03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmG6wYVxSR2htEfFgNP8cxVYLAcAaj4yu-JuG0qrQe4xdTAhzPMgGh7MNCyFGRM9A4NR8pJeuVKKTKV2RTksdX9vcY6JJKcen6g-XKwCCO5e-G97pSfRye_c_NBgDBv2-E_Bw4pccOBuvo5v-mbEwID6UGcMe0t6--PjyhYSIonhQbk_TZftVKVHpDPEj5ySlmywj2-BqHKYy_L1dJ02a-awNEpvRAWe1wy71EyxUcBo2GbWgVA20eVxub4Re33MazgFTql4q374IEANa149TMKcykwgLMufk9mECoonhdfoJ6bdNCpV0Kxh3l88F3RIXJd9ehSRP-SnYXIZRz_9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4u3hrE-OMlRXPWZSYScVWsgO07VkLeZ6UpKUau2NVDZIXNKo8Jtvij8kjmciRnj0UWwSzSGORgxaKT6e2s8bV2rhX_tr_FtvgvOEXyJA0ZIIwF9P8eIc94LdCxyglIOpftjrz2Um9srG0a87Hppc2Sr2inYFf-ftwOwFTRpegVcZRqIQOe-CBC6pUSVe2kdQJkUG-Mw2AFLLd5hv5oyBuW_IDLsXDNxVCWcKnNWdgri3DcUTOaSI6SRRuAluCJoRanshxAjU6Il1qYSAq8kNpa-IwLGD3TEk6yHd4kowW1a9aSpKBXOl3gORO8SqQsWmmS6mXt9xu4ajVzSN5ULvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op0_QB1M1MW-jYAnNwRtWFdZ3NrVU8vtd8-Hv4Yx2utANCNjlS8_bNVwcL_5cSpItwPYMsCwUAwpbLFPekN1zRWciQbz2IEwYK2sVO71Vz5IFurcN14njASgGipfqNOmRGLkbUYK06jT2JA-3B7WQh1OVQM21uNFXtIpc9WxItkCz67Hp-S5HdkjVeq-6M9Hl7Qb6oMkmi9bOhjapIcQyKG9JZ4TSRPzns_REIG6LaFoP_BfYyd7nhJ1I7S-mVmyFoBKNOnn85DnCNZPmXKaMOPQghwPvsfkXogtNokjJSnCecTAq7r9_4Qj6Eaov8IeRd_V7o0gIti9AQwvqz7UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhL7amLJ1lvI_1mzGBDcvHwVF-L_CigGowdnKXA2iB8k7-yj8NK8OB5bgsS7gjfFvZy1eTSXg1l0blAw7k1zftrQd47_QzB4t_DoyCL-snH5APMxFxdBoaF_zr0kZnMwYO7W2hHnQyijlEqQkVEe4xaYBS9a6H6i58x7lZRvgKhOQ23J1K9r3PU_IK3wny8aJMpkohlHg0QJsLBiDlELwH2pBGqHgvx3qQT3XrSL_ZYgXPY9EVtuEASKpKzGvkIhjbXkKSRc2-qGk_EPxvk5e4YctDfkRXpZK3iLixqzoXrAx5367j_mzAerNj8NdKJWR3dQijGybrYc9PDXsJG16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfWbxd5Jpjy4cXY3Jl5rEc8siEmeYnwGLWL4GdbophzwNVtCKUybhhGv963IhhtiE5oTWm8Jmt6aMAu_xxGsjQH9dx6JTAEel4sLgJWKjn9tKprL1mAHyvS0Fy-YWkfgj6AYHChAg8XV-6ADaBeOa4Dg9ddNVa9I2wLY2MA8hje-4GBjiZPM58oT24KxQ8EOXXm-cm7aHTOD-XdEBeO58ns3DoJjw7_D5QdsxU9KteRHC_5TeVSsFWc2Mmn-Z9SmKDZc3nyAdtY_6Ydqv3EFhVPPSy_fv2qoM1xd9B2N-7XPje6vfGfnCSqtDjoQpabFrpfauU6Eppmet-aVooh9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jfor7dh7YiENEq4GfCZbtvIjv8EHFH8EWCX57uWHDigRD7pJBHiY2guy7EvO95cY5HqAp4mm5btL1Z-cyOrSDN52jQK_8m3Gao_P2K7w_eK2YJEZjaC00ITOcGbW2wXFoydVx3vfyQgsuj8XclO9GCFzsylmuagZelBWBp8liFOErz_Kxt3rkeqcnC2I7cnkrtUjdYGMjrxRVk3UG_0TkJaAnF3d7tStApQWtHAiEhWxqTti3U1e2gcQwaUXJUJU0I2CiNLapzNIwsn4D4CpWZQfUHkAD1YUOibyA9Wuhn8cctnmqDCtiD2rJnCmOix7d_ITt9Y7J6m16dUvZkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJq2QsWI-7ASYu3QAifBVtfc_W6gc1ArF4C6trmOtYIGjSvxmBqBE0sUFGmqPfJXT9RJZaFX2WsoYoQmN0zPrHvQnwcssGSnBPYYhGcp_4526uUt3WxYWXac1KjQNXZxzEn6ifBksc5wN4Ky7OtExEo7uhhVZ-AfcjCLomnz8q1hJ76Pv8DY1bRnoSojqtrfk7h2G5ZekoU8oZzdT5bbyFo-TO6mdq10GFyQBbba2kQaZka_NGIbRU5lwuupihCa5eIYf_oS2Om-6M3qA4YyeY37T8rtoVP_GHhUNqpw5dIykugeh3BU6JT-j_NmmHCkBhA7S8SyB7KLk9hAHjrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLXHisLts73Dc6cMQnrOpMqb6yUQ1Y16A8NHWfmx3b6g4kziikAlE8mzYNTtck721SGuZjFndLb3GWemhD9OTiEWpILJ2WtT2YYMdNWamc91cq-wFmY_7YYVJZ426kf2cfs5-XI1F3NcbtIJF9wF5SZ7caYCf72LCn2K_4TK2phh24tGNAvkgJsYOmIZeaBkG0feFafYysK_cZ0fu4Np_cCl9chMcDJwL-zjaGgZNp10u6MwCjAkjj9Hb4niwioeEfUNUPUz2z0hwuyZEuELHGt-j0LQblgSWDGb_6BRQK9qzjJTAt7SPJXee_-0fGmkINaq06RytG6_rC2CvuVzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE4c4mrzs_9Z2tUD32ogxI5Oe_F9sRVks_63tYzjXparFi531hBA7f_EelRyRBpD-G3CWNdTJ_Kko5NgLOBaOoMgneiL5wRQt2l_fqwDXZ8lRZF6hAPcOLDgBRRQSQNRUOhS2xmL8B7pJ_y4jHsI2tw_7Du3TiRPgF_JgXU5bZqt6ICmfNFJHvqJp4iaEMMy0aeVjdgEhhSyy0-yJb7Dy-w6feeR8D5TYY_AgRRqJ2OuQQvCr2fjtGNI3S_tZkKOx9oYuLyK7mhx6HcxfkWOTQ__35z4gHZnuhoyp5-kF9xCEPlHtNBTRLjbVV1GJ75j-mpauBiu2aL1PqylGE_rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpUlVK1JRkThEzdcLmr0fZVBxaxria-bNQPo8Pp9ekwYWvrlfTRWj5FyObImCcXOxSsGFFzbjib4knerWEdzpByRzhLnpljVfWvw8bTkiP6v0D2Trg0ReChfdbMxzkexsRtW5TaytH6D1DBxXzRTdDeZwP9ijCVi-EjSmvsza9BDPR3leChiPNKLgih2mQB2JXq4uTyLA4xVECkwxfW7xB5TlD7oTMUXgntW2VJGsM8wKrOr2cBurL1dNPvr_5SJMRJyMPTDyywq_vDf7ZKZBh4dhKKlOamu1_kqHeXONk4JpsJTBLmjRMhkE59uKVfwUZ9BaD7a4RJ8PF3zDja8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnioDMJ0BKwRhcy1BcPpXcL36xk-CLtlaB9ASFN0PwFYLNoIm36UUfzEwUaSPEy3S-awUITpqPkRhoY_p_0MulUzV-X6bHYziAVNpvlcjLd6OAlSK3MyUH_4v_OGRp_owGKkxN7fxb1k8UR3EYkpcJQ7T_CnjneeCSyZgq9S_f3VfxKCEZl0rQoypftiKiTBjXMQ-sSvz8cV7GkJo-243qZesP9CehYRzdwBnxB6OGhyQgIEluOG5J3WhJ3Q7ym2jehKcNPRBZLWUejVMjfLAfyRiYG6oMtIj8NUmJCd2CKNqkNpq-MVVmjFuozC5SOx27k_mMc5LwhRJ1lAaP0PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1iq7ZqXr56n-qfjvdzgTEZOB9HxjwXJpNAtcNml_fcyxOF19zCF2BCdHLDXPQZhN7P7hJ23D6PEPoS9vMcvDJQHeqVO9lw3GUgMR4B6X4v706aE4e65G4cM-Kgqq-xFGSjCBDLoDCDH9B8QnLod08SiotgHd2qfT4N_LuhumCgtw384-JfLWgE6DF5jzpaRdDxrxeYvi0n_sQNCBPpF_gLKG4jTrDU6r2av1LV4QyfPbLpyUbNehfYv_V4PbRuULptwZ5qZqLGJdzmGfsEB4vzyokSlswpaPqnHdRaqSHNfInl51yGwySS2B5iKdGlTqF93iL6B9YjAfl6VXd6SDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzpcm25TcyX9OPb8ecdDfo1CJuJw7vvOJO_Ol4HcfNfkfUedm1y3giRkRgVcgZYBcROiaay1rxyzGYnD9B9XFzo3GfmHOFS4P5IrG5QVIiJYCrdtVSwdZuO27exEgxMn94m3O4ar1SpU_AIVQj55TYt-Av2NQVwTMZUZtSj9Si1WtQw_V7PvXJPq69tfVyLPnpnGtX55y7XQ0f4g6ELoJ9XRO4bLjnyK-Sq3omTKKPvdC2EfuQcnUp5es0XLvMcr7xWsKRn8aH7XxgUbiq2n0qDKGcfklVFdrBfBSpGfhBYPCPCrqmk-FUuUwimoAcpo7k_MxzqseUYtAEHOSV7Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmuFB4BooXYbvGLbw9BQzKcm2iZ3r_qFP0pkrnl3MegM5ksxwOfVLc7p07c3ie1GvqQj_77j1p9SFXGOggBtzSN2hfJDQwLssUfae-Pgh7xoL51winH4ih8y0DIp1OYgbEy4Soc_DPw-zwYtQ3sVV8h8OQH0Zt-e_NZ7l011ZALT7wgJ8PAv38Kxc7_WGAimNH_ie7XdqwVbFAnqtiYxQVbcQi6uKcGRy4y-f4HIP5wZZctLm0pqPFxVhy4kAOO-DbxfyEvF_5inDm-R_P0leykaooZN-axk0hTciL8NCrmA9p6LcK2sHYBbwcX1bKC-MDS-FP7Tf5S59wDM7mgVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USRAEFdqvvx8sMY5fmFq2njZr1Bcw8I1buWbJor6znqyxRkFMGNsF_nooyueqUSpYYSH38cMnQ-0TXP0dgJTOPpchU9K3rpsWyekUvJvDeoE6mzne-UFNVCD9LCQESX4ORD7Cn2Il30RM7NNQkCKqBObLPZ9Flg9HJssgZ3HUhsYCNs_O6eMQUFxplSiQs-uPOkTnhqaMNUQR-BF8sRE1TaEezx81TU-QizLUs3qcAQBEqfTEthB-E5o3a60ODP_fdmSTF5VrueO9cmPjyl4XxB4w0VGrDk7rAhhI36oU4YP1GSVeXzv4mrEfGWzfu_tX8vwQ1hnYB9d_PDdTsUxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=uG5UXbK4IxWN_2CGIArFxYKCcElcn3qOEcWCFE_sa__AHxXs6YV6RDlrgVKQNaDFpx2m6qFQutQrVbwmoacCCDAblejv8uGebwiH9rJcz-rli3Wnqs0GAZ-UV0ktbiCQbKLOy1WlPsyPw6JECczGKnOqZnuJ8HpO9AYP_bI6GRm1ArYPSHGwsXcilBOYb0peMtD_9SHcYNtnbj-77I_dPQid6faOGQJ1oz8tvZ78ptt-arkxoTh-7wsrxKcuJBlVePl1zxd5YhrwdOUqTGEll8TywL541TRNJPC9XWOtKX6jw6KVH8xUqL0kumbavW0rAvWrpUVIioH6d_ZhHUAvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=uG5UXbK4IxWN_2CGIArFxYKCcElcn3qOEcWCFE_sa__AHxXs6YV6RDlrgVKQNaDFpx2m6qFQutQrVbwmoacCCDAblejv8uGebwiH9rJcz-rli3Wnqs0GAZ-UV0ktbiCQbKLOy1WlPsyPw6JECczGKnOqZnuJ8HpO9AYP_bI6GRm1ArYPSHGwsXcilBOYb0peMtD_9SHcYNtnbj-77I_dPQid6faOGQJ1oz8tvZ78ptt-arkxoTh-7wsrxKcuJBlVePl1zxd5YhrwdOUqTGEll8TywL541TRNJPC9XWOtKX6jw6KVH8xUqL0kumbavW0rAvWrpUVIioH6d_ZhHUAvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7oAllsL8QTcaMBsLxtKrphmzMrHRynWNyLn8t4OI-IwUq32Yed08LhAP9iQJJnK59gUOPY6v6NA447x0bx91WR6XcoIqxXNWt-ML-U0Dw3vKCXLcbDawx9Im0nF6gCFRPmd7aru0RYGyKCq-LugdI8PvvcaBzRrY4rChYC-j0sTMWoGOJ_Kwa8lyhuvJRh4JlnZBlnDsD89qFvUaOzFNZgwBThbEwmB2rXMlkKrKj_D8ax2sgd1FUZQMU3CCXnEsTEgrWkO2-rvAX1oH38phodjtlka-7qU8XSgaUe9ROwcGxqbOhIhjZN59Dbecv_wn9nsYmQwEAFPInopdDe9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-aMjpN35VOTfTnVAXcAu4Mwy0dljrEjT_DrwJAzI4MQ1J4dLzJsm3ZE1N1onj29iZBKBtsmD8-ogSHYUUCgo_3O3e5x6rtYXGSalZEqAIVI01TMi_avOvU0m_R4yOS-anwyCi4BdPEtS-f5jALuBAeT3tASdQ2lBY33FB5h0wKSVPjKtNyhDaNVeH5t-6W06UYzs41ctBQc0QlBu1j0fJ1WxsyCCVd-XH4xgDQaRpiG0J2hk4cfdUbxvgci5ksVC4L2CpVZvMx6CTj10IkNXQQgH_wed__gB2TnfNuKxUYokQ-UeYms6f2rV7kqATLI5BDnjfJnQk-ZDhrpEi3MLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAN1V9DEx1bxm_p4lxw6L5gbwEmHDRTiHTsiyHftzZOXgqIrR14c5Tmwfd-zjhyuQAC92mh4ppchPmQ9X3_t9-WFkcJcxPksPR5hs5S7NO8fCseU87x6BPiw4OtneD-dVamdhYIm8R0rZuSAmUDe7atv2EYV9pbBGdz40ud0Nx_gwRmCdP1lF86GuLaR79cboFVF0aKXwO8UruQWNKE-mFb2y0_yO-L5mjrAWEw9FPY4oytanuzeo8vNix_i2J43VO91krmF_YKRFvfvq7roB06g3LOmjpYhXon7dZEFj3S2i49fi7wxgCRbJyo6R7yDPfx7wcZRaNgZSzyy_YPmpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBatBncM4z5Ha6id25h9uml9Js09MuDVd0B1xSiTAaa3vwc_4govjkGYjS6rX6Hrn8dAXFM-vE8R4eBgkYfhr6zvTUiX7JbzOq2gqP7oO90a908MCdWD7lYZt6Vagu1CwLVXzpHsADyla0Bmphov_97_pbSXGzZsjnN8nRc5DxMebwj0-RS5VMrbvJMVzilMYpa_J-XqbuT48EFJX_AHHWVRUOuVG11Lz9LyYvgmTB5OvBzR5UWhr_Kg-iciXWo1Kd0YOr0S5TzXvDS4gUVLcMB16209heeKn4VbJXa8q-xF_FTCPuL2dXRXr_uACLPir8xm36wxi4klMKbBBzLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXNTx1ufjD4sknClmx2sx9xt1NQ70lmZTN2nheQo75-eNXArSpiwpZm4OZ4zPnAfj0k4jxNNhgzMLNpGgQBH6VeYZ0KkTt_kp6PoKUUJUraVz2LayhkjsDmni76oEXopAfm8cN675mxe56O3dROGfXa6ErVzH5-CjHiNgkgnjRHoVVDHV4GJJOvShwk0M8g-whOcLWky5BTzjDVXaz_SqTdkQxNsbQMkTIhID3beRfO-L5DrjB2xpPKrMUNbt7VmLhdLfBnNWJlQ0WuDBtJ11wD6VucxBigt-cIY8r0akCXP7m8yd2DU0Ahz4KE-FJG922KoC0wA6VlrT7gubHHqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfpG40VCkE7aGQhW6j83U98Spri46JtzU52kFOYKHrEfy6jh5-J_K4tklB9xO0o1-9Ma6kyvLwzEaM6w2Wlk_DASnNYLaFQA6f2Jb0rB6TcdgmrVipwbaYpLAnFwdos3ONf1ABIdTKhMM12S3UmMKY9es6J9WCHZjohT7f5IdB7WltPkhZyFhC5zjCBcQPodnirgNRGfKMmG254txmR-bzYiKnXIZC8FxkRO6TsDr2Gak_83ud7Hkm3qNDTsBlcBGwcQbZoyXn_OLlWlXsw-PiP8z9v8ewcz-05eh0IvKcp311x0DRueSA5YGFxjDsXGJqtQ3jWCd7OOrc9rDm_p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOoYWJxCEzVixDvFnGpUjm7LWYQP-tFNnnie6_HgpSIAdXYBpZQ7Z_LH3S1c0cA4WuIalDLpq5J6uXrqVyQAtu1gDRgTFaHn72-xFJHAaLlYPL4oAOGpnGkTXwhSJ_8dGVdWa0j1rbs5f6rz1-lCZimYPw3djQWm9o7magOMvMS5m3ENKAqZb4zfBJbzObIrarIAWkbrMK5Y4arSY5S3B_it3_QtELVNQ5cH2Q5rThVmvVhwvquU98PMW4quluPVgd9S0XdkNRmyW-GjE-Z8c7_O4sUjVo8Tr_Vh01Cj4sG6cPUro9M0Y8FstNPWlAT4LEadA7OoeBH-JEEBrwzUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpNZunTGIY8nQA1Vf00pKk_kYHsAQLVxtktwqfpOC84TLAjORDEFV1CJC6SkhiR0ah_W1_UAocTQB0_EAhyamV6bYd4WwUaML6s6Q_ybSiDdoaECsvUKXhs9EdFRRjGw4Dbpf7H7HRoly0YCvy0ghuHA1_wy7sev271FWIUlNto9rI_iUEIPikCL1viA76rC9fPIb794O6u6asY_AgUHaQKn0WRdtdRS9dbkXMg7u0Gp0DR2HLz2gKgQ8kbhEw2lem2lnpBTUUUJopIClmubTN0dA89m1OokN8OdbuWi0RY5SndqJ-B9dvlwQR9B2spPGitHfRG15X5gGjUmLvqdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edVA5rO1qJjEidBB4Iy5gIgA7Xwye0mB2TpTIuvScRPnmMIZUAx2JUxzkxW2hLb6U6sjJucRFBgcO4i80iRqmS9zaLetIgDUbBHqIlyNfb-942BjXc4QGOLdCXodlVzm9LpGO6yVCcQylxS-JbSrSJDZGXJddWoGxu63YHfsb68diuXkisvX3m7C06fwDzVKlAMJQYUfy4VW0fz6x0aYdbA-WKdyDQ8HXWNGU2hLEjOrxA0MRszsOt1_YGXFGxdtaHEJZghjUAjVhmv5xVSF5ruK67A39Q15XcoEgk7W_iLQZJWB-gV50eXzdwVuFe9_6UEIQ_UrT70DuxDLtc2KoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=oHIfSI0b5Q3OrsdpnZYGgNwMxFQ1DXoKEzqBWX2qm522OIxfMa68HOMXt4CWHncqTjCrjCCv5aB91rfG5-TR6U6-hLGTyiWombrVCKeZQqcsX0lWIlyVdU9LWE_DAMeeKv2Hz75xP4-RPKMTLm5yU16n7XV9x-gGa2c_B1TgjDIRPwdd0H4pCrCKg5mh59V1acYsw23GxKqKajcIyjZ7JQLbdCpmtKMtgkAip8FAksxEiDicu9HIyxS2As1_G_Tnd1QZYVQC2KU5WtFVgsdjYX2SAxNHwSiveER1z9w_Ep2UdfU2lNxKBUoiwtlXx8pfHLok3wjqe7r_kbs5OqXvFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=oHIfSI0b5Q3OrsdpnZYGgNwMxFQ1DXoKEzqBWX2qm522OIxfMa68HOMXt4CWHncqTjCrjCCv5aB91rfG5-TR6U6-hLGTyiWombrVCKeZQqcsX0lWIlyVdU9LWE_DAMeeKv2Hz75xP4-RPKMTLm5yU16n7XV9x-gGa2c_B1TgjDIRPwdd0H4pCrCKg5mh59V1acYsw23GxKqKajcIyjZ7JQLbdCpmtKMtgkAip8FAksxEiDicu9HIyxS2As1_G_Tnd1QZYVQC2KU5WtFVgsdjYX2SAxNHwSiveER1z9w_Ep2UdfU2lNxKBUoiwtlXx8pfHLok3wjqe7r_kbs5OqXvFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO_cxGY5mbrnjkAdugPaAEl2BGoXe2EZfpGRP-IuRYtICaElie05UsfxGHCykFFJZLkL-hPmixwG8iySqYqrESQV3GA_vnB1dAO0wIdaq0SdN6ZHWmrn9u2c4C-Xp1u7SWYk5hrCsBNDrg_h6Hj5YffEddx3c080629Hxw1mVKujpst4lJtFqAgVY2xjVO8C7kQo0fnb-S43KDBijROE4kmLiYEOdW7BQCRKV0kiOsZsbDK_R78sIHr8uu4SK6vCVPdXmoVfffTDognBnV6zuhBvEZc80XcDsol6q25JiJQA694RSa0cZB3Wnsk3wohXbCodmmOtiSpUBp_oePuxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-gFOPiD9Efc3P2JUZ-CzbtxF2Lo-FxWFK9yL3GC98HumLXXWhGhfqI_gmnGYeWUy9AjUGTKYFQt6Ps3OsE577auXIVl6KFNAM1X3hihxQo110xiC2mgXVk29I30bZy7jPrkVOz98n2kjU936ZHtIaGcqg4ON3oBI6qVt6_TGlRjobaprIpnk1RdpLDnNlJkN4u632e_MmX8OdutcHG70UUjQn8dJlR5uW9FF_RcYbhkjdvZts0hXBkpZttRpafCVWg0smc9LDAZjiAAlQgH09kLFKL59GxLAWi0t2QFXYHoSe5sFFF2UdbbPTPI4KpzMX8LVY5eVyV9p9D4OCCTwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTndy8M6U-eJiecdNjwXvgrfK0F3x4d1giP1Ff8dqjzMG_--pqWaAxjs5a1uxRMw_lAZAzLJQg9EMMAIJi_6-cIHES1xw9CkS-i5lVZPKM7perSVz0nwPVWdswv-_U1-2n7pbqOcDCgDw729I0m55_Y8r6lvHU8x21uuBzoPOjfXUUDXm09bpvFduaHq589VFp9hTF7jMN3bXo3RUgW10LA5u5zxDD9J00vXcu_Cf56r92G3BK-jVFgcsURGomF98XJD-nTfhnDmS18SN1ki6Iu81iD34xLOcIQB_gHZJFrO8lq7hqc9bZTh-Q2Cj4hMbAWdyHlvwQ7W482zhncpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG4qtCLbGlL7SlEC1GYhzNr0BEGgsy4TE41xprQi5W8GNvXNAADKiVBMQTpKuraIQVYoWrBSQHVZWIjHHMGX4lyaXgZYG7GtHTj1q-afOnR-NEleAMFS5s4t6NSZ12KcO6-HaI--DaDOBHcXifENWGQz93P90-u3UMsrhqgVewGAaLIi1ANGPZZKicq0y5-j4RfMsOYseo9JlgXu4O5N0SWTdSv5avrpWtHYwn-mt37biS8hrGvo5eoIgvidOD8yWBC8Z2YX7DPfleDou6qkwQN3hdjYyJkZv3g2fm5szLBsdZz0vCKHepZDRi3KAtyf9RWrP3KsuWD_yPceeXM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdlJBRmyEtt-Ve8Gpz1b58PwCTTGjvGTB3vQB-X2kRXwkVWmIFgyiwwEQ34Xh0mQi2bGMD9GvTp1O2kepVLuE5HyHD3Ev6a9awbZsRcCDAbnZ_nUu03oFiSUoNe3MEK41IcmWY7-hxhB2crz7iYz0xWGL_XYxJEFb_MHbXoY9hOJ-xTOSdkoYt9rv93hsfsU93eJX7-FXhisiqiN-J1FPx2jeBP7hIJCrndPwp3V7dkwp8FaO0WLbUqqvp_QD6slB_dVuBn3CgDw2aU93TWx2rBOqDYEjQwiIWMkRTzONor9ipR6Weu-hf0gFMbrfNSmqDC7NvzOSWJjeYpNBN6G6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRF6H2RAr9o0AItvo7yuGYqk9NkebAvkixNhTkSGSesUgbcTV7Pg7e5XtVzLOL1Q4DrJVIUBOa8QQU_-tbSXmaGaYXJI44s3OSbLAFReuD89ij2BWmXpTAw2jqOaDUR5ui313fYkvB4KdEfKesORjzyfy_W2upAwplXGjhvUBRGr4hUCgQSiBGt4SwhTsQMPc2tmySYAABaPYWj3koEEo23WDaa9nixMSgm0C8ncgCKzP0VisrFXDz1tcomEaUXxPZyWnQHyLN6vuQcpoH0XU1krjatM4PX7V3AbxJCs_TzIOYfFUkf8uEGtmwS9PQYeH-fadwGgH0p6tvk183c91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VadgKjE7yZYBiZf_szi0yOd6SuZH3dwcor_ttbdGhUxBXc5mARHMWq0mInVpY7HDR7YCueB61WSxEgTZOwXnArpgB0LHMFL2nVysDWOZJ75f6o5oxhb0dFP7CrHyK-jkJuBn8vWV6xIx3EEgGnHfvAjd_Y2a5IZUU7ULNk9QkWlOp7cweWQsop1dTt8bvEz6RmUgD7E5S2ak-UCXlRjwOYDXoXQh6qTkKv6f6VNiy8xc2-_Z4uer7K-oor0gF5x7mCtCCW2vslUBg192GeguPXAQQkyxUgB98xeEeztR4XKk8Q36JdhUFkIEoddlSnqN8tVTZf6OldQ-LS551R9a8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2tlOiisd3sYO0bkW_ONFihnkTPLkRBbjw05X4MC1aCSvobFTVQobfsvN1yQ6y6ZZNZ2hve9riGn-zUzmI_2VZVQf7UbivP1ZLURicaqtDzuuRlC1KobKiF9j_gI_OkAFXFKCdAH3l3UXZrGJ5CvtK8ErXq5Rsp3M9ciq1YoiqjKRZHAyHt7lvqIt_aMZjzsYCcAKMBYBELM4p0ZVpxqXbK6-9uMKtuoBcmlbl8heOF793AoBDTI2gE9EGeKqrhIe4wKij-F-u2I_HlC41msKC7PoM3fRLN_B4pfazxH9ubteevsOB_lHffkdvWfE7lRormqyzzS8IlCu3miO3Golw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EonnrO2tu0zM4wunjeR2qpr5-5nMytdhAFbBhglRbBNilyfiuEx64YEPIRFViOjFraHTa4I0vo6eugl0QLFfKFD1U--wPldjQoMJ3hv22JoKVtFXcuMS1zg4aqw3dWwNat8VQ5tsmhEpQZq1I4VUIzTn0LuMUmVo7Ad4jpNuUtkq3Bgv9m5QOiOJqAtP7wRS7RB2EjmY5ZCz0xl_el3-EI_6mMkcNTApJIb_Uu3eWHQNNand6mUGF8SFAXbNijWhxJgVZVD_UzttGlW_IYSRrXff_KSf40Uu6MOOaQVnJnE1ltRQzJBQDte7aaozJ0J01XCCDGCezC9zwiHCZstYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVMNM5lS3ERueM2OIMhVu3NtNI_kaQhALbuqZ9UC9EmhU5XqvIOndnrpbPBC57demoft1sEguADQzDyNaCJNMbniStlvUzrf9He_PsFruk7T-cCXHqwXlKruP-C1gsW6E_LvtBCGZYj2YScSfcJk_HQsyNFNZ0J1_i5AErom3u7hsauX6K2gI8eZ6Io1IaZzL_HzTW1Vli0XvHUElhPZ6-6tpFpOmMh4Emj5qUaoaxCHD1p76DI8QO0HquRQA1C3BH7Rf9i0ape-JOB5DK8Da0Hosmr40JIRj78UnScYxMhVmSaj7dMcoHXVyRV8DqQV29jqryxyYim0ae5FguTceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=O1Fpb1T5Q-LRsQWFdT0YjqH-XRVCaya4G7g7BW6o7sUTNyI25Ij1OTPqwtPqBQmKI_3rqkte8fVXvp8cNcXRjuwVSp7u7giS468ByHQUiCk-toxHK5tFrN-rs3jIX1oJH0TGHRIJxHcnBqVMCA8wsHt_HVItsO1E4x9zoNRQwGAxFip4tSrBzyb9CEeYM6KWLvzanKbG1KEIWHw292HJbYr1KUQGyhzg508KaaPNTgnyeli1HqqbJleDdjKAjFqhgr0xzlGmmn3Dxy86Jn3OIUfCfPbmSGLGPVAtieoWuom501ruqsWPVOVml8-QwawaSpUjeJp_dxvRONi1ZHnJvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=O1Fpb1T5Q-LRsQWFdT0YjqH-XRVCaya4G7g7BW6o7sUTNyI25Ij1OTPqwtPqBQmKI_3rqkte8fVXvp8cNcXRjuwVSp7u7giS468ByHQUiCk-toxHK5tFrN-rs3jIX1oJH0TGHRIJxHcnBqVMCA8wsHt_HVItsO1E4x9zoNRQwGAxFip4tSrBzyb9CEeYM6KWLvzanKbG1KEIWHw292HJbYr1KUQGyhzg508KaaPNTgnyeli1HqqbJleDdjKAjFqhgr0xzlGmmn3Dxy86Jn3OIUfCfPbmSGLGPVAtieoWuom501ruqsWPVOVml8-QwawaSpUjeJp_dxvRONi1ZHnJvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_7nXpqcMfRp6SfEqNoh8cdtm7sl5vHj6t5uuG6Fkhfq0J4sDggHwaQB19YjHwGzOxbumEekaA9p6PkUOJt_QfqembBgXftA7gLxsPHI4_JipPc2sWw3ZXrNdJtkqix9x7lmROxELgvfVGE2oVJqXZeGHVFNKZLJnJQLB4UYuksqaX1u71m6XwLrKROkzoLql2gNdNF3n1-Jn9G7X98u7VudbnWOAhah9jIKZlB9JAsyVEUvDgparVvAFht5zbCLyEQfljiof304WUZ0A1FcVhxQlzVJ7momKCZU_qHcyFEH6L0-6x3Dg4hUVAJpZ9FLZXA2ue2opaUekm33m_-3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=DiteRtNhwreiWp8tkVdVpkry_xHGDCJu79PT1yK8r9r-6ix4YhLZbkTKDgi0hrsGhNdQfRZvCbCd-YvQor-uUW0Zoy7MLwk9_T4wI6aaOMiNi5vNAdwkj6sMqK6E0KHlGHjY90OGIhOZt69m_R_MAwu0rH8rCTHJH9p81Z8qJ2bagIH-HUi4iBV246Hw7TM1Z4ut82nm3Ew0xxegdDMgb7XGXnpmlLunFz25UKq8aTODeWaivp6xPeYtPNdbsfB9b__q7nDasBrRAN0KPPY7fWVIxh50BITXxTPnFoGSlqayCTFnAN2oxpMXc6571gsTJoz6e4iPyZm26ioNVIjwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=DiteRtNhwreiWp8tkVdVpkry_xHGDCJu79PT1yK8r9r-6ix4YhLZbkTKDgi0hrsGhNdQfRZvCbCd-YvQor-uUW0Zoy7MLwk9_T4wI6aaOMiNi5vNAdwkj6sMqK6E0KHlGHjY90OGIhOZt69m_R_MAwu0rH8rCTHJH9p81Z8qJ2bagIH-HUi4iBV246Hw7TM1Z4ut82nm3Ew0xxegdDMgb7XGXnpmlLunFz25UKq8aTODeWaivp6xPeYtPNdbsfB9b__q7nDasBrRAN0KPPY7fWVIxh50BITXxTPnFoGSlqayCTFnAN2oxpMXc6571gsTJoz6e4iPyZm26ioNVIjwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvtoIPpzUmCW98FVpxTZQReADojZfo_yJm-YSkBlJu3wV4OacnCVadescl3nuwNOb0T9JP9Qs3gEr6wyxbHTPSg2FrA_t-kPWijRLvAhU_WaSn-EFMm7FZVitcviOJwgNFhfabYETPcj1D-HrOagOp27cDPZSPbxBwEdjNMV1wBMLcqcVFvX23vQYZVN0Gtgz7X4NDJJ9Qn0JFFi2laZY2k4RRzvuD7tF9AxTjwb_JMYnfoUrOJZ4uJUUWq-lQv7sytsFjU5_UZzWrG-8CT9kIcMcDsfqODHFno9XBz7t6dFmEoIIBfxGmdlOjipyZ2VpOTHKajKHNT_9Dg9v6SodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmw3yaL4UPXN8BTloXIPAmhchGPfVOB6r0uIy9QKOpBJvagO-0GRW7uSCjYV-XZFLKzIWxF9t1GDaAqTueDqG6PTjRHR4o5rMflxuXn5-o4UQ6X97b2PuHwTGtoYuopZnmkpivP7NVYFlZdjUw2F_81TWzGomLtJQUzufacIf9bApoMDZ4RqfMmeaqG_DYVd6nbkW7hZGZdPh8worHhQbB0PWPgAFVcUjzc6ne1ZOLKEFova7GuLKWAVzoUviwyWZ47OZZS5iTP0FNiqCWVrvTXKULWyIRMk91paJYEHI4mKJz-3eb_EQgZcET1jpcZKg5sJ2h2EA92bJ3BBtB8fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th1v62-j4Q9cA6pF_2KlBWq5q8fKXmmn4PF8sayaC3lHoC-32yJLpDzSMWe29kE4E8ee2QgeYihzhPl4eD3cKgkGKagnnoU_qTUjH9vfCr5jpgOh2xd-YTvN4tq1FlDnkOI9d6FsuKJNVXhPDISQ_oid8j_z0hom5nWzJHoeOi6f45en41wb33dfuLfMtK7q309gVqMEnyIPlOQBtdKm2-LUlzx5mSiGIBvLroKl4GLaNA5aFm1lcsci7RA0sQAnpa9ipnlZ2qTJourFsjhoaPPGky8qBLnqjL19ZvXGTYTvm1Ln_vPHIVdQxKsuV-ayVkDGqbgFsXSq1I4w4lqczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX-NZiWZ5eJNNLtC-QX09rcw6PcPrBl-6I00sf1kMcPqgHZh9Ha8xBy91tDKG8-wRON91LPmEeqgG0tloFiUuiCm8FXRB9Q0LL_Iv7DF3n73ZocVqXH-3KtUmqIqODSc8iA1mh4RhLftM0zKbpn3azXQingaNy6Ujh411xhqfPpTbkpuTJV4_SLAx7Kdmidg1Z5MHiziPD3q-_O8C04dfIRPNe2N0a6oT-mwhrLPDWi2d0LSzq-nZooKc1nXespdgGv4xfcfqJatPk1YwqMCMk-F2d-hnUmV8atWkDafbr4-QxX8qvpgDmVmHRD3bLFnPQvnLSCqtPjuf82pcTuMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfSpKsTrf5KAJPjiRIgMA-QgpqEI1FpYhIHqz40y0tSGtj_R2-Drc3EW5yCU_5ZDLqMglX1v9Fc3l9KUEV-ggq_RFPeQK0Zgcz70Cx0ENv7YwLunXNvk5npSJrIz07A1diil4OZtsvQTvNEI0y_CRROzEbCpBTt0wpfx6fDuKXCBTDnLrLdwu0vCRCeAon_-skPcPRHwIlzFTblsdEUPG9gTCmImEyJ9a4usAy41MVybu_pSb_NYOXDj9VDUS1LmFQ3_XPRxdOFILIYxNEFY6w57O6uKUosZT9hsjRRxkuf6MU5JffNKaJRJ1ngOxCLpSbp-3rx_DD6-C-tAPc7JHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCYMYt_qRqzDh-kRQICbwelqMYIhALXFU2n2-7eOYK5-zLFrBaBh5N4col-Xr5d5ml6xSxXjol7i_CNN2-BB4eo1nwLqyogoVomsgUV-VtRlvegL4xJEJ_Oinuzl3-Xtfk_uTE_j5w69l9WwINV1oE5P_mnajPds6FrdZQXqG0IQJY-CsgHfJnntap2GJPJLqwDHaF1ZmgGcyjHBFJ9Wi1gCWVajz18eJ3zeCt_2FEYb9IkZFPXFLta3N66u-hhGlFART3X-UtV-CR_rDoxYDFbMgirIzhyMkwf-WxVMaV_-ASyjhHOGT6_juIFJmNyK1WyDl41k-2qo-geZSpUbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=YRBC9DaKo_6lwS9r-MNtPmHeHd4brkvj2OnSE2082MuFNV3BDmaRLcuscFljeoNTJeb3Wx5mRjgltYygNlJ7tmjp7BmeFiDQ-9Y_M0akloZDlLNX_i49QySTzCLBHAHRbEgvW6XfIFFksBcksHzwZx-AuLZOErV9_0baMnzXjLwNkUVJuSV7bOKA72MTciVcdUkaN46KNPQVnJ2LvTT1o-J1dlUbYPFK-ddPvykDG2tMtbu83DEhZXGxn4-jkvUyBbvwlgbSau83rCVb3AvJ0nkj_Um1rSFmgJtGGQslF-c6VZ2CFI1gH2gqFSvbykCTQGB091Ul-Ig6jXLzux1zeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=YRBC9DaKo_6lwS9r-MNtPmHeHd4brkvj2OnSE2082MuFNV3BDmaRLcuscFljeoNTJeb3Wx5mRjgltYygNlJ7tmjp7BmeFiDQ-9Y_M0akloZDlLNX_i49QySTzCLBHAHRbEgvW6XfIFFksBcksHzwZx-AuLZOErV9_0baMnzXjLwNkUVJuSV7bOKA72MTciVcdUkaN46KNPQVnJ2LvTT1o-J1dlUbYPFK-ddPvykDG2tMtbu83DEhZXGxn4-jkvUyBbvwlgbSau83rCVb3AvJ0nkj_Um1rSFmgJtGGQslF-c6VZ2CFI1gH2gqFSvbykCTQGB091Ul-Ig6jXLzux1zeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=Y2uaGWtrXOccBGfr3w61-Bpw11umdP_AFQqz0aZ_YmyjKvK7BQfxW0BOpfiMMhGI0lyXasrVIiZBb_d6FPbnF1ukWqhluIMyJg5ok0C5qEEYIG7q7hbk7gQMXq-4huMuZxGxLPVh5LfsKh7go9DbsgyC2wbndC4FWaA4IQ6vvlQk_hQQHTC98Hx1mKggEWkZNqtB_CbxirN3jVTR6jBYoxt_amL7i32y9MJMm4aPDVqrEiYxxrsl2kCUasNKT-IgCgaw6PSUYPzjZKy0Keys9_2EoOsXONhi5ygwN5okHhk5EOXhmhGypaPlrVl_P61hjeSyBpwTOXXoo4das19nlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=Y2uaGWtrXOccBGfr3w61-Bpw11umdP_AFQqz0aZ_YmyjKvK7BQfxW0BOpfiMMhGI0lyXasrVIiZBb_d6FPbnF1ukWqhluIMyJg5ok0C5qEEYIG7q7hbk7gQMXq-4huMuZxGxLPVh5LfsKh7go9DbsgyC2wbndC4FWaA4IQ6vvlQk_hQQHTC98Hx1mKggEWkZNqtB_CbxirN3jVTR6jBYoxt_amL7i32y9MJMm4aPDVqrEiYxxrsl2kCUasNKT-IgCgaw6PSUYPzjZKy0Keys9_2EoOsXONhi5ygwN5okHhk5EOXhmhGypaPlrVl_P61hjeSyBpwTOXXoo4das19nlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-JHozfbcQTXHNjuNVrJZQaz5ESIk4izcFYVlcbYMPx1gw4j9stHP5UK4zJHfvofwm1FdSc-TU1itbmmsd0kS527q5fMTB9sL_wDeKgeW_GK_aCA89TsGzRYsUc1uCmQ8XBlyL1gbSgiay7hMbobZ-QXO98n2OGp7R3WRk8IpNwhvCe9XNvSyadWVfFRJvhhixLYoimbpSM71Qwi1pKjQHOPKR7PY5DTKvsTTwLc5R8lFvvvfP_1jshSgTuao0TeDQf9GFIAu8qCm_mku6RBb5O16YgK6AsDfO_RMloIKLjLCgoMYUh42IPPvxe2zSsNXcOsoDVMOIUBKUBu8WtL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=VIr5aoNjJQi1PiAy38E5PVDEUfVPsRqXGiJp-CocTdAOH9X6Q8yHUVM0OOuFlIF4edVRfrsDlejyxZNg_A6zJX-iBd9AGKppnROIccH--qQdOOju0AuUBUDgZkZcNRIDyg30TaOJ9sSELgoylZ2DsyVCDU9E_oXdoXrXPZ3BEJFizWdK-9lpcvODg6RIw9EFatuzrUp94bX6d2kMCC-JyHGjfsVzTqes3gPN_7-PsKFJwt4q4bmi2xPuj4vg9XsEcK8hCZd-3SrQURm3OZoT9josj2STEnI25CMNmqENihEAdLZDoe-Mb2ZoA3ujPKPJd9fZKs8PW_k4Mr0RsxGcZRXbWotH2Kofm5AAeypVCB4Acyf0W-7HasIrIzHKGs6Pr8HZETQAiZVgPkEi0DpLGUH5a1pZ6QGNWPQynvUZ4xp__3rwI3YhaFzsw2Idd-X9lkbHLfTCrkakxEYfEfJKAyawhjFJyRsNKdjK04s7kW2DQlFVlFI-D2yfmEiyaEfDofapt7SyBaSnpm8qUReisbosQJpYZRZ7zAVXNL4wzS060qlTIelawy_T3z55oEb0i0DUwelNNKbyar_yPIdzDmGHXsGAhNYGPMtau4hkzYUi5LTnbuVwzHZWlbBAKspprMddQKo435xMdxakbunkVlr74t_hOmeegiFN6abMDHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=VIr5aoNjJQi1PiAy38E5PVDEUfVPsRqXGiJp-CocTdAOH9X6Q8yHUVM0OOuFlIF4edVRfrsDlejyxZNg_A6zJX-iBd9AGKppnROIccH--qQdOOju0AuUBUDgZkZcNRIDyg30TaOJ9sSELgoylZ2DsyVCDU9E_oXdoXrXPZ3BEJFizWdK-9lpcvODg6RIw9EFatuzrUp94bX6d2kMCC-JyHGjfsVzTqes3gPN_7-PsKFJwt4q4bmi2xPuj4vg9XsEcK8hCZd-3SrQURm3OZoT9josj2STEnI25CMNmqENihEAdLZDoe-Mb2ZoA3ujPKPJd9fZKs8PW_k4Mr0RsxGcZRXbWotH2Kofm5AAeypVCB4Acyf0W-7HasIrIzHKGs6Pr8HZETQAiZVgPkEi0DpLGUH5a1pZ6QGNWPQynvUZ4xp__3rwI3YhaFzsw2Idd-X9lkbHLfTCrkakxEYfEfJKAyawhjFJyRsNKdjK04s7kW2DQlFVlFI-D2yfmEiyaEfDofapt7SyBaSnpm8qUReisbosQJpYZRZ7zAVXNL4wzS060qlTIelawy_T3z55oEb0i0DUwelNNKbyar_yPIdzDmGHXsGAhNYGPMtau4hkzYUi5LTnbuVwzHZWlbBAKspprMddQKo435xMdxakbunkVlr74t_hOmeegiFN6abMDHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNQCx7OVbLkyCAD2ElCoyoRNlRmOcxtNbTjyW1TQtx2-NVabHYVWlM22RbiV_8CUHL3rxPXEe3NsMgOADFqvHluxfeS0jUhmgaGa5KwFO9lpOnWXy-RNAsllKso_UOpecf4GXAQzcQq8lrrLDQQdYR870FVwY8Rz3KnzVW8-ooM8wQ99OcQHazc4Ope0ZBLll6WEaTyhhh7XJv2QoFNAjF1yXZoW20uMrdAevY6yb43_8ldGsMlddU45_zmQ3V1-1YhE_7Qx4uRDyNpJ-9IOITV7Lu32B38UeSBL_svLq61HOycjDBIoDRtfX-s3kQoX2m4p5YX3s1lGz1BFuRr2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgTogczJvX1H3nYPmR9uiNey2pU7nFyca7g8qj-2C6ALHAUP6UFh_BsiVAM3ems_BMegNoCNkTtx0lsTI1eBuVMVxmMSzBHbXtt_hvfkYhQyVuVUHH7Fp8uqnjdBREBSY95a6mKL_7SxrAbc8sWAPA3EJIXwehJnBsi2-v3PgXeB67ia1r9uiAD2syjDW3s9waDLAlQgPx4wB4zaSEyCvedZnnksgI8DZeHeP_N8Nzg3R1mTBa06hq6z4gPb9snbFw8yjodRjibEC8s2_ftKpsJ9M6uvSJE9-nMjTN5VWuduzD3bW_3zqHMFm-rCgCqIcjh9JqPf-KSgvQq-eVPbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqS_4RuT9xstpuTMenIptTLGnVHlg-fpq6bZ28WrKu2g3VjMyubh0S4mSbesGF2ea1hvhJlLKr0YZcHxrf3nGptTZ821i7PZjNCZlMkqi3Y8QatFrOWj6GOnuO4T_FOnjl04Q_ehdic90lUE3fGuW8ulic7iH2XllkBAqetqsqr7evSmjpCvg4464A-yb5yZHeSJAVg0JYyPSlh7c4pRQo1LyvnfDR1nas54XGWweFRKIdl5A95n-9Qh2QlcAvQJ0LGgVgq8XUWKk3s0yAPHYZNIkN1w8NPOhlZ_eQN_YQKOScQLjL6Wgvl4zvBI3d-zllDTjovobReuXFk4svVRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=AxjJvb5zsRjill_SUz-ZWPV2TPzW2eeKqwAwswLOe-jSwpBYl34biKUoUpgquwILDamlA15M4QQPDerFsYt9lAVh8lPy4KYOW4mqVwSrfRat94PaYlhJi2q6AMkZasSilyk1BSqafrSemP7u7Q94gNU_cP2r4XtBbYLOSEELTgTfv9enhgJEslHAPb-vLTLV-UyHzsyerewsvDr34DOoqlj9PmIvw_exx2M07LiA1jYp4SGNujCUx03OTuaNud-oaSq-mzKk5O0yOwkyoE4C7NILQq_njDnjqdlOcQqJp8xrzyrj4TxbPKx_29_k3yZtA9UExBadoMWqH6IXQGEbwZEaE-y8CbvvHXwApcFWjo4deXQBg0rrh4XZ8TwsZGxbxKMALyzdHcc7Xtyvs9VGQ2p8Zb4yXqfrZ_-QRpJHGlm4Glp7aFMyeW9lwJlRUz7XJiLWMNYYYBA-BrfyHuBxQlhKInct3C29fPxFoP2X3E8w7MyfdWmRqS7yZSQKdViCKEit5zN40ZWnmQG-ivD628cf584Ql5thZYfDvzzg03CbYC8OB6WHUodGyUBW8ScLboQeTNOb4k3-9dwuTnu3E2K68azhYgGMLmlyUAGIVQsymWw2PkErpKcwDgheGYohtVseG3XaKQJI28ZguHAhBXRP86CXmLVRKouOdWwGRjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=AxjJvb5zsRjill_SUz-ZWPV2TPzW2eeKqwAwswLOe-jSwpBYl34biKUoUpgquwILDamlA15M4QQPDerFsYt9lAVh8lPy4KYOW4mqVwSrfRat94PaYlhJi2q6AMkZasSilyk1BSqafrSemP7u7Q94gNU_cP2r4XtBbYLOSEELTgTfv9enhgJEslHAPb-vLTLV-UyHzsyerewsvDr34DOoqlj9PmIvw_exx2M07LiA1jYp4SGNujCUx03OTuaNud-oaSq-mzKk5O0yOwkyoE4C7NILQq_njDnjqdlOcQqJp8xrzyrj4TxbPKx_29_k3yZtA9UExBadoMWqH6IXQGEbwZEaE-y8CbvvHXwApcFWjo4deXQBg0rrh4XZ8TwsZGxbxKMALyzdHcc7Xtyvs9VGQ2p8Zb4yXqfrZ_-QRpJHGlm4Glp7aFMyeW9lwJlRUz7XJiLWMNYYYBA-BrfyHuBxQlhKInct3C29fPxFoP2X3E8w7MyfdWmRqS7yZSQKdViCKEit5zN40ZWnmQG-ivD628cf584Ql5thZYfDvzzg03CbYC8OB6WHUodGyUBW8ScLboQeTNOb4k3-9dwuTnu3E2K68azhYgGMLmlyUAGIVQsymWw2PkErpKcwDgheGYohtVseG3XaKQJI28ZguHAhBXRP86CXmLVRKouOdWwGRjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-mS9HxL4ouOiD8DD-Jdd6LuyNRLJ-K2AiuTZ2O7W2czAhozhhANVMgImzjQp3A2weMvRf9ooJtOL64jQmOxEIJElUJI073SdkKY79jaqzmf-6DozUF8zAKNrLKforov_6yL2NhZNgmKWpOx-VG5EnBxY0CDhCU52pMSo726ujtVtuFBCKYjTtfH45sENJ3volmbldKPtM1PeENMc4MwWAnDBj6V4caqbY_oiXGDbBV-GfNJYxGC1y3veBVnvgRFAjGRr9tJSUmdokR6PPliSR1c5kdzrgikN_sfqJZYkDWq1e5ePsZZzFZqMOe3vfItU2JgVhL7vWOljqXMHB43Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8N9-ZpoXxRT7FUgJbIFWYayHBalmerlIjbYMCYZiW4tsWItFiai1hhOFkRjw61qFH77XCmSZOQt5pSeek12m-ujcf1wfm7XrWbKmBM_IWaXX9dL6OZj2viF4rfFhyX7E3Y5eQObpLAAagIaH4pxRyCoDPuP9I5K9PhCgImDYU_wcftx1mK9zYixLuBIuZaDMGv2iISmVSwzmdOuariUZTaMqbgfPzdkNgPygcNBkt68wCpQ05Sa0uKSyHMB7oKfpBsEjSR2HRQipTuof8pAG6_Gk5JgnH72e0cvrKE2RW-Ps86iOBRGgrqrqnvRNp4IIHfSkguSR0WDqWdS2CaT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJGetkN7Gv_8LEjp9f9PPNSQYExWP8Ue3D0dPDA-de1Ulux6MsUhggFH7sfvyMKcw4bFEmN_yvtin5QL53jTYERQeTn496jC03Sz1RN_LEOGDRiYy1uJ30M-7Pob2YoM3_WwClobQwoZt8UcWszYMRCjCHcobDHhtaQyvYMLI2lvv8vSPfSZ2nVMPCS44cvb7cKUGWzyXeiUBcSr6ZcDrfoLyqDnmH7DtV3oE6yYwzYrBBvV4gmszFWugYyRkVbB45HE5O3fjA0mrFxzpnlVrXynwEhYdBBziWkGoZpcdOYqB5xX3cSbGopNWYP-tGYSWYBg-pxJ3F3JwX6VzfB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0xKJYj1-MOt3d_4_AsIOgkJaH_w2oZGu3VJtXL5qWPiRIk4-d3jImmk7zcUI_vxNPsmlc-5DGfd8gsqmUyxTUcdmp8QuGZBCDzw7-Xo6HKrIXLV9yX7AoTVhE1lmzTcJXABCjG9SigWeUhu9Q0Jjtc0nQkaxxeQdHyQEEb_z4XudjMkXfUYr20FI75g_mYMEUd5m0G93emc3VeQsdmxDyzokGztwzh0KB6RI5kqBb2FnT7E5TYlikJqzSuQ0UFkv-_Yph1qTbH1VQ00OABSK3qBKluNEdLcNiiN1FSj1G_8kguYHV0BjpCODpNOQhoVDaryPAWTBXeAiDDI8Q-xOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVrCbJa4DE1WTaJwa6ZawlPDpUIXhFHbpw3cvbKzQWm-4p9EPO7HFy-SwtAYeAzQSK5zCjz8YRi_dguq4ni4cO17VqpAVMVTLpoWpmjwORqs9wyNVx_PdJRRQAbvAeCT7EHSKpILgB5k9zoAwsEsGs8Orqe-MxRUnkVP2d08dLqCwTey8--S6nwMR_mrZR6bPsgBaOyvBrCt50obGPNd_wAd71tfKbRKIQhntVTq6P1-jfQbCV76gWHCd0--LXRo5Bw2o1DSBdv0ri5T3Jg483-rNPuKaaFCs5P7rpijMrUnVRLYbofS22EDpwcC6nSqnrAkp92sGAL7P56NSNCwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=ivfwpIIHH-XAL94dpdDdNKQXuCGuMEm5EclMeuCn8NLQtu3ZxH8YtNRfEGcrJ_y4CHXWNrzqeX2w9FftdtM2gjOPJVgW7rEo2h8WW2Truu0OtGV1jfsFqkkWEYPnD2ZjeL0IceExrf20LOOLdzraTkIWlDJlJdu12vaVe24Xf-qZSS4hVM3kLzniRKdE9eAc1dy-VeLp_Noues2-Fiy6lFH7xyuVZts50C0mjPRCE46k8-75UedCnrtlQyJS0tU48b4uNApclYUaZoqrbQsVYPqaVZ8JHET9NLmODvyOvRv-BVdL1GIY7fnuQ3iXuEHbNE7zB2ux83Fp4nWu7aANJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=ivfwpIIHH-XAL94dpdDdNKQXuCGuMEm5EclMeuCn8NLQtu3ZxH8YtNRfEGcrJ_y4CHXWNrzqeX2w9FftdtM2gjOPJVgW7rEo2h8WW2Truu0OtGV1jfsFqkkWEYPnD2ZjeL0IceExrf20LOOLdzraTkIWlDJlJdu12vaVe24Xf-qZSS4hVM3kLzniRKdE9eAc1dy-VeLp_Noues2-Fiy6lFH7xyuVZts50C0mjPRCE46k8-75UedCnrtlQyJS0tU48b4uNApclYUaZoqrbQsVYPqaVZ8JHET9NLmODvyOvRv-BVdL1GIY7fnuQ3iXuEHbNE7zB2ux83Fp4nWu7aANJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/algynGzrdMuklEh_IDOWFw2yUjV9rt-nIesHDrSA8kY6BTdyw8pkmR6dqRzs86c9Y-r7qj3VgVbB5KI1jXpxIVlJCsA1f0LKc_LfSovK-bMGQYnjRwE1YWCxe2-90du7GIe-eFp-5x0s3oUWdWjLKQlH6rwo4BhTCY32hOCTFMla5Nq9b6jRYW8pqEROA1bnVa7H0iuxx0bGDiJvz6efE6NXeF753ptUlvMNhpTk1mjd7a8wU1aam2tGHAOscepyvksYRJkRjauafLO6_o_9H3m3OftjNPW6HtC7a9xBcsOhZmy5Gl09k4aK-ZWag067mVDmzdyJw9wd6mvsrzKLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiU39N2jJssFOIFXk95Bw6hm4jaZT6IfUYOOXZ0NLR5b4jI90CHvC5xTkhlgiSZvWVhClv5EVZlMz0_bQLr-fU441XaP5xBzd86qGkSeXPSN9Pc5UXMtks1a30nBj8d0C1StKlV9nE_znPrSebielrRPSu0nWhxW-qqu2cngPx_mHXNxMF61_ipm5JCS-DRZSqusm8ijc9wXaPxnX9CBS07nhlnZE9a5x5wgE3stcQmKbBjacgDW_LwzSPexKnNCS8En13jULAE4D3zAgyZ2_nkCEUXKfrlqbhQ9nSoekbAJzox540x0Tqs1jynocthE2ae8m5I7scFPAZzhjSMGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI9FCfNHEOyYR4vZhH8yauOoNUYgebxPaBhW5nh5CoWGrMbRi1MS0-odxUvXKFkD7p97eWfk6FXEnSBRphtGhyieS1t4SEz-zWtXkdpq6oG-Fen68dPeDAWN8sEMScF4Zl5hGtd_0CGhA5RsPbj6lpZn8TlMGduj55-N5XS4CW5mDkJdICREAeEifRaJplrpV5gUWhGYI9KbSRbVkDCirOeyblxPRIkLPFQdfEBNBKziUJCz6GAOQvmQ0aomSI5N24dLiKx8M-rIX2YotYr2sMHNosWnlGkMQmHDglfFljeT0-_oVnw5ts9cTUKT4f-4sdJsubQvmU5nKsxUQRpUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpEkDmjbcAq1FHcSFH_qTe_esynEikcwH5TWaB9RuQP60c0933U6gJ_q3DRNXoxlzB_sSeacu1v1JKmXzvyJaC-3sEQzxqvtMHyz8AmJPvzo7vm0Z0r8V2kBYWPghEHHVsHS5IpuYSiGqYJNuok3iQPvZKYFq5Jwq8Q8t7sbNPycWAF2K9ijT2a1Zwz6RRikG7t46CL6qG2gi9RCddVR3cq5i4fH9KTPZQN9wer_ejnZgPKKXxUjAnXzMJ6hGoL63HbP98_clKB-XaL5X7D8Ma15EWiRZ65os_xxbT5LQYs6Yhk1u9hxJhQC9uo-Zmr6p_CARX__8gWBoSm_FRFGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya4H_w82lEMOuYFI2L24t7V3oudNaFwBN-ak6nTRYyeugSQhcGmqPWz1vz9yL21FlnYRALsZR8RGSM0jb2SjJqPJ8NDohk41KkWuZUbzxRaj_O8a3TsIkXEAf588lvz6tHJP5clRnkPuUGPZFDtq1VDd0jGHQZNuazwQUSdgVnaJPsOXRdUgQDcrGFpsY5GdYX2Vk1sEdiIemmRTJnDDq1XH1_P2FILxIY5V-MWCWo7949kxZtW31Ut58LLXu9a1nTQ54txIqXSlWRitZTJz99gbirVDcyzyNaicnTiwHxpILJQ75z7uXe0dbnj5wF7rS9HMhMfH7XSdSn-pHzW3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=prVyu8j7feqF4-OrsCA9bYXQ7-Mfmvz0Mk2dq9kDr0l_66WrITE4nXVcR9tt2j4XpyGmGJyYFaCw4z3zeBuwg7U9sHTXI2qGn--qDjAjflKrFCo0dqRWaEp8DBciDe_Ao5HWqTrtf06-I8iBGve4Zi679_JVWuD_W4QLEbAs6uF_5hjd7nePrmcaAHJCQEyTVpVvkG79J-5l2217XA4Dxk5z9mXIGQ8wj_yTI3eWPHn2BUTq1r65ifMNN6BjTpWKX0EyRA63DjpCBUrNiGkhVWFYQrmDeGMEuOkjFvA9Ko54bYP3d0wV4GM7QK_h8Uya4nBuSwhrd_x7m3vBeNZZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=prVyu8j7feqF4-OrsCA9bYXQ7-Mfmvz0Mk2dq9kDr0l_66WrITE4nXVcR9tt2j4XpyGmGJyYFaCw4z3zeBuwg7U9sHTXI2qGn--qDjAjflKrFCo0dqRWaEp8DBciDe_Ao5HWqTrtf06-I8iBGve4Zi679_JVWuD_W4QLEbAs6uF_5hjd7nePrmcaAHJCQEyTVpVvkG79J-5l2217XA4Dxk5z9mXIGQ8wj_yTI3eWPHn2BUTq1r65ifMNN6BjTpWKX0EyRA63DjpCBUrNiGkhVWFYQrmDeGMEuOkjFvA9Ko54bYP3d0wV4GM7QK_h8Uya4nBuSwhrd_x7m3vBeNZZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiXesJEh5DhJYXTH5FOCSCakGMhI3xj_oBRN6kg6CksN2k0yjavWb5W_JQeLkeMB6D3QwjFVkwRaDoBtGIqov07uN399dWL2njkXHNClpDVId2dOZSxctROe6AEdpld2E8mcVWMzYqAVkTR9L2w2DA5J_Kcy7-NVIikWx8bLCdqrZzsvkjtQptY7BkVpihbU0zKT9F2aAdxUQ-uLj3xMJy2WbUVe0vLAhYFBhe0aI0hpE5-hvDJsLcNm4q9Jk6uMjA_oaRTclM_50WfwVy5M6Kb3FhdUzRQqyC60fINKSg8-VV_mriwTiha0Q5nwlMr3JaKqEhhqpnGc4Gf74HYJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfWHRSFBsXUOC9UAVo-gMF1WNhHm7VWODRcf5hdkyzMrG57XlQ6Xin0jieLUZunxPkBCycEq0Zu1EvFTFN7RVSfDtHu5QzhUkN2z9LL1cfbF6P1lm5Kbwxk1mbmKzc61nBbL1i2WgWf3jZRPiE2pPBCHAsWYRtaTCeBYsriiQTK0t5mDtsfJnuSqyauDZqzj-nlhc-pYqTJuEs8iz6F1H5gpeqawiIVnwPvjmBdnMywGMOZBLc9L6vdeb-JkHHDI2sxHwL8CSa_odQLoWOI3f6MJ2qa_0f-aGioQMWnphSkBiUDcDXsORgBNgJhNhmpJWki6_teLXObZjYQ6NhhH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEzUhuBRfeTyuujVl4y7Ez_vXdYvTFm6qrkKhR4xzlVxnz78_6vfHFxwX_1tv6lbf_b9c4LhBcUPZoaNoKVNqZGX7FiaC-mCQLp2toy9Y85bk03PdXTd82j159S56CWfxHmKGfx-poS6N0E5xM1As8CZVf_SEaMStaqSr50Yw1bT6UM-f8HOG--snOqbyBT4hOb5C73HwhzdnK7tfetDnW1b91e6x9LO89OSClSFGjXgP_RVp1SHleOh0WFm32zfbv1WpcPE0_O1XTysEdWzdT37DRwwtQXgcVJNm51ngdJlkvVUEbONeO17sIJ5xIkRAuZK1AnuN8LJ-OcBSq45Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUw-RlNC2WLSKwiU1LMSgP4W9_1GKj2b5CC-0QDpE_8SzC6FZb_nAd9-JZaD_L54womKLrUO4jSzmUdd-qP48hpFimOp0QLhYQuSyZI4nxnvNXg8TcDclnGqfokaUl5oe0HETjPTGi7k3NxznJt-MYDGRPWdfWzGUYFGSAXnzvD1NMc8QrPcptiaEDMmoy-ZYqMONn_84FX0ea2M8Ex2vQLfpNRCxYn7r7ajRi-yxXX_s-_83TH6qORDmOFBO3KZakIJ8q4d8Nuu064PkHdXbtbSnVfny08LVZpRMOIAbCTIy82SKk1KXfuG48PES46yZ4cz_SElxp3v-dN_vxd2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE12pvP4J8nn-whpaBddzFTD-ZAPRDsf4iItFCDRVQJtL1NkUT_FyyIZutiiF-QBDqckKdKgT4fGp8XxzcB-gt6vzMQnCrBiLhm3KdM2EJjy0csJ5C9N6V0mNWPX4lbto8QtewvbwpO9ODZos_vJwJVGdwGQ_DPRQIeBiLNXdCLrmRmb90QKQOIta9KmzFMnYjxk0CYt0GWB5yxQM4BUH5Lr5JJL0KOm0C3Lf4e-LTGKw87bMnGQAgDe0XTV3YlceWiIAgEK-NnsZ9284n-Tx7x3KppSv2xE3KP_rc2JXyjAG8ZphYz2mR6NSzTq6JF28p0LSRG8na6qcmbzzo-SEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg5ZOAjPQfAr9EUAI8uOSgLbNiJnX9F_dNheZ-N5G1_cM43W8H6WepykKN_AD6YPKxTr1JN6oJVmWM8VqJoUTzXXsVwrCCN69xSXLBWH8HU6SdWx1eL9X9ilGwNVBU2Xlswjzjodwbh4ft4S7SrbEEQwvJMBoEdTQctdf4m-6qRLQE8VeTqDlNWRCnFEmxm1-jpe7kk59Dp2EUifrBLkVad7wRXCrWSNNGy6jDPWo4FKFJ6lzvORSTpuZuRPcAAkkUZ9yvuAPTLOZ7l7ZsJzYE0kKFKUPy5gB2VDTQOBdyxR-QSsRTasuWi2uO5CG00rgzkXsNQrt9zWFwWtY7n-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=pBbUkt_6On02GF9KLQDBJYpFI_jcsKaVHmqnp49lveZNW3cgisaqBqEAVhGA7s-i3upPmQaFcGgD9O1avOIbl76IZI207jHWnaeS775Nyt-_OxJTPbMfajmL7a_H3mFym0x1LnRYYXxF1JfERSD1ZvXW__DcqS_qOW69WgZhoUq-nP2fs0C0cYSrbz_QiRbC1e6AAOv5x6cImMMT_6PGbErFWDZb_yneIf-_NFvJib3bXm0J_3dzaCvXPtX1GIrhhME_uZQhTL49J7UF00g6IJCFDLLyxoP56vdJUVhlNFbBxjmHZ4_GUnC2qoJUN-emv6DiqvbWRz3ZXcBefQI7VzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=pBbUkt_6On02GF9KLQDBJYpFI_jcsKaVHmqnp49lveZNW3cgisaqBqEAVhGA7s-i3upPmQaFcGgD9O1avOIbl76IZI207jHWnaeS775Nyt-_OxJTPbMfajmL7a_H3mFym0x1LnRYYXxF1JfERSD1ZvXW__DcqS_qOW69WgZhoUq-nP2fs0C0cYSrbz_QiRbC1e6AAOv5x6cImMMT_6PGbErFWDZb_yneIf-_NFvJib3bXm0J_3dzaCvXPtX1GIrhhME_uZQhTL49J7UF00g6IJCFDLLyxoP56vdJUVhlNFbBxjmHZ4_GUnC2qoJUN-emv6DiqvbWRz3ZXcBefQI7VzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGmUes5ngT2XSuyIzs3_j86-5YNiKlJXVyVvAbHIazQS8mnztcqvJ3aqkSEG4vpSE_YP586JF3NG9prYuriLWFRVjIXBq2iyOZG-W6l8zGlw4NdE8XRzKAOJi9Br7MwvyKCMhYo01ZId3I64PSh4xqDh3YpVskktaAHZgbFcUeOn3vS1L0sNLxcxdH76jIFX8MdAKZ0MtwR4CrtuV8Dz_9A26zT1MFEa9VDWIL1Z198KIR3a1LZexYDCoUCOkfjSNlT_mFEY18UQBpERFQMh4qu2ByQuDiqJSThKNmpnQ198gCev8v87GRnHDFA1npyi7EmHYLaLLAKkJTEI8oNadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9EktooExmRTacYzBeBqOo7L5PGKix4gAs41zBi7FxlQ2vQ14MkmhyJSAfm1JpgCzHj1rfMefFfdB6XyTRnvRkhTisQYbZaLDhkPBN2a2QK2CPT9UnS3rVKTcNEn_XDt7iyeSMeN8tK1VVvecPdGyvpmcjQecv15rfg-o7UQfgP_adn1Iy2ul9OWr0mK0SNixoy7Ml_iao3ikNc3X743lsqiDmEyNHgtK7o9dUMS6dOgH0jfSwyTlbENY3l2D9_VLRr4ihX8ueZtKGa9Fywlt9stJGV_jkmUwvUmF2YaLrx9eXgTGRXFbxXOxjJAH4yQ3xNCV8AbNLwpXgjzzhO8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb04hfn3hCIrB9EGKcpSWF2LOBijcrmPj0KRZHoksRrKHcMDB0wGNbfEJ3tQr-ICscm0wTY81irQhfXShZK2B_isw49rEK7fP2WzwWdJ7zxTaRyE4EMGXq33l5NvrN4m7meQcHneKaG2vMt68xDf-2h8Wj0a6vLc36STnN1LWmmk7KROym0HZ0vuz08Hz8QDVsL5K4JACiI98goNZGFdVZmzbLAUYcgr7EHgtU_nywCgmh_1zRC2x7uUmec7OiZI_5xt5zH0AjcqpleiT9utsxb_WXgBhJSsi6wgw43XgjBKPwjCgT4k3C1G3HCYjKfrlqDYNvMfLpByt2tk7grBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
