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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 529K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 22:24:25</div>
<hr>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBn0SEq9Ptw84nduwkMrmcuqjfw8nOtcsxM_O3k6qMRzBkzt2q1ffntA1ahxVuUTFRCoANdEz0yw2FURDdRQppDzi-LiRlMg6k3NCYFau5FPIUvd7Zn-C71fT9sgCrExnv7rO-XFzoeL2XHc1JxytWh3mga9OLXSz2-x0reuJuSMW55ar_r0PyVH7fCtc3nOlasHIKfF7MZGQaNGrTgQdGzFxt5V7CifiVf6k5HVvWitSiNupIobtNN4JjjNQOOly8YXGEh6Fj4B85e4TBX-GyJhzNFIPSVREi0YKaoUqpYy6QTEdNFTWMYy7wv7rX_ooZCgG02HXf4NEXOk7IAlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2J9k4jI3P2DiRZ_pBfTxHEbarS7XX6jaMiyTok9RWI3LNyccvCwUIxRuPGo7Gy1DOme9SdcOJTccpxMI4Q7HGfRIOmksEWlfLkk5DLUi3Jd958GfFOxeCnhTiE9dimSk0iG1iiYLpPbmAFkSLXhbMi7xICKttgJTJ28QJ5UwuYgIJMhLjIz9ugYS4HdwMZZAlc8CnBjTD8wHNlRjUbmfYfA0wcvoxunauQimCh-GGmBRqs8eRp4jvKe4wPSRca-fYwLkZYg9JUXY2ImtxZy_dUhInXckXil2UX1BR9aQFqoUEDedi1Ueih_mF_qrdHTfig9Xx6cZlw8M6BkHNxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoFhAUEAdkGEwJHpsk2Yq1ZxcsR_-BuGe7TA3mSz6oMsaG6AcSVjPjRbCGhAWGxfWXylj9J_U6x-ZkJztCU5KSrDcYq_No4bijBRQY-dnD-_CvkRateLMG21-eEbXbnsaIxJ4kRIZf-xTV6bvE5BmxwG7noX3XeoQIFrr2c5cT2yO8LQeAerwTsZqsggrPQoYeKIecS1fU1aqzgIHpPuyR51rb1xJwDSexytFOGUPn5UdQWRJuih3q-WNN8Q3OzIisVaxRYQ77rB89PxNBtttfM6W_D0t7QrHVnVAMmleJHY0tgCGkefaOF7mhXZhXqntrSluNIyhURYxubY_WcgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TML8hGT-zVAnuZlZuC-KgH3hHOMrrSZM8VMG-18lm9v9hS-XaFz73F18umG92bRvrMox7tP8i4HJGdP3ARrX2HsHpH_zL6YfcDzXIu1NR1zkJO39DgYuIvSURpTzsTfwJLQjbtzJcGGM01NRLALoLqgsfsiAlAmeIFmZtPfs3ti38QTKeVKljCRbty2LHXY8BVjnS_sK-9U49R_u3brLAXgghIkz6vcSJJaIkb7NddobME3eSYeNYoqaiudgXG4xvOoto9VGV17FUoBnN7mzd3R9bbfIiPMafPRELLpOMM9F671yHQycxGN8vFxvCsvjNr7RCtOj8YEPeN27Rgzcqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HstE1qMe-ptgh1q4IL-n2xHl5Yb4VSJ7oAzzGeFw5NDfk4EnKnLBMJn2CP5IDVKG6bEJzOjclEuxojiXw7JMiaamDHgjItp4XMU-9HvkJrtQvM4N7VNAa65N8ctQ8uENJt1AgMrvyJI0IT53Z-kdd01n--OD5SQXT2FkeMvPHb9b5LyNFu_rxZsyv_lSAU24dCPZjLhrD5MKGNe_GRhooegtyehtR-RA1bcdV0V_-L8jZtdDkAFMgvqbPkNelzY5Bn6Fv_eKD5zpR8YeYN_NSqC56sHqwyK8fJMmKKW76EqwSvsnAcO4-eyQjwrryRCtikDisRFzrIfmN0O81kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFi9fi27CU7rxX3BN2Q2ycek2OQNVAiPSO32yU27aoCacVklg8Sy7NcEwFr7CAxwOFmpUwBV1AEIYWHm9yTbRHPpBO4mgDQofCAzM6999y4RzJvIke2_o80vGs9uXYMBPAboiXKQy2lb3j90kar4ommE2cX-VTfjBvoCGxV7rjvM5c5F-L-FDcb5CoEq84ao-xDrIsFGABG9-CJVGWkcgII-woWzUc0AAdAfg-OnQNZVj2VhFVKbQ_N9OVitT1cMWfPKPLDFestn3R5es5UwawxWS79q79X2xsi9dLZYgOQ4zGFnB4VQXz1PbofDvsWFH6f9Lx-o90rpez4GBcbJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUIG_lnhWsbFQbjy0CT7R8ps6irJ_61Cl5a8gGsM5Dgjsbowa3DSPqHLaXwvSnZ67zRwDZgDftX3nS_RnxNawuoJl5amiJV0x3N-SZMjQKl4uqr6-oc5inYR6l5Rg6ci88xa4hxrPvKHzFk3TUtPfS7k1MWG_ZgBQOv_zc1NUfcQivlvI6gi14zvm1Qmxdv0NnlIj7tj6qNtGA34YXWGIJkgewzmJye9l7eRex9_KvqXDsOz7sJek-628NFxCMWLY01R2mQ7t5W6DuhyC-ksRga8kwcUcYgkC75oDpw72uOuG3nI7L9unoNEcXgfmAuvzyM5EmmD0sOfmAtZzFs1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvwBT41ihk7qChGWBU7-py6l0CluTN0AwpqbhQHjRYqu396odHvO_yB2meowFAWhSSAGnKrvKIC0oEYtWKQXzcTDNJdIi94IJVGr0PdrHL3rmZapFx9AFRPmZunzs49NA1FAHHru-HFDr4i13TwUEv8yPrWyAqjlzKcs_44WGDRpz9R7idjUF2u9oXgdF-kg_WpND8wOic9YZjgMZkn2yQQ665_1zXSRCT6vhHyDiercLsHL1I567HK0UuePLuqiizf4MvKnHyYtguyi_abljnqxbaW0jpLvIBMjBDuCVJpC992dnlt66xxvvt988EXD_o8RFBiLNalFsUswTLF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQn5CY9z63GkhJZyvs9NwuWnKgD83Abmqxb9S9WEKfpLDodLQN66SrcnsvenheOf50PGl7IwVtnkFloNLuaurK9fAfqTF9eu_OGr5jqicQWvbUPhgqjql0f4EE7epq0XhUBHg-4evvYF9bQHFsh_wgL1g4hBxanl1yCEYYAZ4mQKV8c2ciMylTQw2fOhMSO8T3Wn66xn_lAAyEUnh2DBVeQEtKBTZyV08YiLmBNdGUdHbkebJ8IyvC-D-U46ZEkxhloLa4ZdyPm-X2L35y7eMFQtE2BH9eWRYccyHS55Dhj9fTW35Z-RiAg-ODYIGy6iZMQiSSdDLwyjG-_nPmuPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkSQHHOyIPxM3ZdWPE4dcOhPAFNQY1eDHxNBu3oUXVsTe9z5t1_7itga7bEdcT-om28cQdvpwLvt3JOPdvJwhr5e-a1SFiZuQ_qVy94bplKmWAKZcRo8bPYOl37c0MxxI6zWumODSfKZvOiTIOYo9_USUnGlp3yhP2dXJmzRQ2XuNnuXmKy1PjO7ro-7YTORQ05pjkZbYUxC_a3YpV7AzNUZIReeF_15HhWq9FMsY9sYnRsHGYIzrL72yETewa18RcOMxelmxAtmrjy_QQhduqX9n5Gw0KidZ4A_X4rN7TrHFB6svYE12124uox79FSRbM0Yc-FkoVsxne9zqFhXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcpiRRyF-9D607XaBEjMxecDH8HJMR0yvxh5--6YrEcrfPasOth880aZ_j4PEOSNjlpfHn5K9wKI60HdmpVYwrLUM_9zOABZos0SgS83FYGGY4gTUjG30b-GDhsYv6xm_Z1Y14Exgs7XDA2cmNZkJWHJxzyI7fxzlaac84mKfI5f_B_OgWeg4izQqBSWqfNwOtyQjcVDq1TzElnhMLt6UR1kl6lcOVngWNMgIkN_sUOS5UrvT7g0UXX95tMzRcrdqeivurgWSjZVf9sBe3rNFKWJ6L87Hva5z482qh0UsG0htYwPPh0ngcMoKmUTimTjND-6yYwIaBUPsbAu9C4Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ijrOIIB0qSUL-tnoZ4OZQKlEvtp1Ai8izcgCkaTlMwZJePRx2xDcVvHTl9U-wRPUp5vNext_ck7D-q1Pt9ctPUsiS6Ug2AkizylstoLXK3w0xbypL8hxsSGCXjnpugLOE_KOKYsvjxW-xdNCSl3P098dM92c-pNbeNjItMpkZRbC-uTkIU_m9SoZNKQaARc8R3QcEO3m2Horo4tJmzN4CgE0OwZPhpwWffmBTmUJ11ci4lKNcBZ91m6pN-fBkyKPekvzUEGjDaa3_CBmvRfpW9N3jMaXiwAlzA1tITtZQ0E5mFA89_jStGgBI0nifENOCtXkIO15Dp4KL1skhxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9DXPPsX9-nhFiq_tuTISngjEMm1xB0qwdtJnQpojX9gU_5pJGc4aW9ZVzaMxss55ryz-leyiebfN2_xPrWWSxL5d5ctFnniBK_9Kq2cbTTMsEluldfOTGp6myIAhUzq7adYNOGCDx92EBWlVmcEiU-tQS2GF7kC7vt-Ziepi9kuTsa5PcvaktkBbXS7h7If1ww7noogf0MBBn9TeSmQhp6FGH9-zAbAbEmXALqLYEPk7TKbYmIMPvIo96XQAotSqESE1Ig71HF6iyNf3cpkNecTLaPys9n1u1QzurWn1yUT3qSNmgU32LBcgfWPNE9-etyX31CW_OisISmXaA9ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q57m_-JKndkh2Yt0iivERluGF-t9KC661REe9iSbOqhrTfBy1TWxTdBNLb1Xhc7gzueCLppwa_jN7fv4JuBQSiMb9ybaS9oOHZSbsErnTdAtSDNIGbiqwpJBewyKRGT5aInhE31Yx5_OiByz0wNzZiIHOPANeLA4jsjns1psErsCdx8FxyINGibei7tmXPiQNxL3EfLxAthwSUhfBYVtQpiU05dgByV40suPSqXhgh-GoWOPg0NvHHj9HYSqUtophu6P29NBDrGfmy0_v3D3l4Xw1KBmBLCQ8-uxJq4bQciyKPfuIfN9ZC5PQiZWiXTII30OkfJkUbH-Tv0tlQ31Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8N-3yq6njXoPloKlKkxbAI7kH20VN5gRqn3VH5UpegweTQyh7eWURXp51Ff-hHE5FTYGzdyMJRHOjAFQq_cOmV8Ub2t8q7qUl9H0JJ3v8slrvzyz7rFwiSMRBVpRFzDPCdDCEXGxkwnyva4L1JntIY40W3b8t4d3PHmehuOej51BNfEEu0_L2xnnvZ39kP9p3k5X8pSP0pL2L3HgD3RI9BXmerb4d6kXMxjBzi0oY0xQNxiZxgQpJR4L8PmjYSNqcOZJ9_FIEWUPd9tanX3VgQQw3aKY40sv2pKa0pAv3sN_DwPgpqoEA7Bte0Wr4qGNkk5tlFmDlqY9eTcM7dJVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3HEotsHio4aLvFLOASytFyWKJLLFQxKCeQzbNruN1Msyn39L14xzyQSb9GFZ_wS0QLtnuWTHUZl4BinUqSoc5R7dMI4FcjROPRZcBbwQJGmVLD2WkP44RPZKHynPw7cXOJ7xvWiPefSckiyQ_7KwIxwIu9uA4P42mzKluV8KMsuypXDxqi6IVEeV71qWOZp-B_O_K7-mQEATr_ScBpgXeW24nqjfVVWbhX75HtalBPFmS3UemJqnMu1MYmZNjuYZq-yrNH-p5Gp-Fv5Od1N3kppe6LG8l1rh4mDQL-mc6hKquczw7w0k17QNQwkoLyDCetR5INzO-N6PhVnHJeQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YjuyUkoTWgwIS9B0_LIYK6EkwZiJaVcJpxuCq9JFKdOr8LaUwCAJgDMMAs8ll1DdaIoGs1rDfOsJKCJvJJyjGdFVKe2HFr_9uKY1Y_OWG4AxzPKq0msqedD91DiLWf-inEEPNyO6lecbc2-_jOvR1uM_R2UeCo1tsJRdYmkOeFEVffAxbOgCAg9NCIY2e5p5W3mEnbdB4oWpqkWimeiGWX0-tDu1la_r6R1_GLyGo6KMVKCWj0k0Uz-vigQKNMq6eG7M5iJ3HccY1ua2lbbWtyEmvED0wNgJDj4rPiGIz10_877qyM7a7BMe15VFHAHELGbn7271YItz4vEwxK9X1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YjuyUkoTWgwIS9B0_LIYK6EkwZiJaVcJpxuCq9JFKdOr8LaUwCAJgDMMAs8ll1DdaIoGs1rDfOsJKCJvJJyjGdFVKe2HFr_9uKY1Y_OWG4AxzPKq0msqedD91DiLWf-inEEPNyO6lecbc2-_jOvR1uM_R2UeCo1tsJRdYmkOeFEVffAxbOgCAg9NCIY2e5p5W3mEnbdB4oWpqkWimeiGWX0-tDu1la_r6R1_GLyGo6KMVKCWj0k0Uz-vigQKNMq6eG7M5iJ3HccY1ua2lbbWtyEmvED0wNgJDj4rPiGIz10_877qyM7a7BMe15VFHAHELGbn7271YItz4vEwxK9X1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k22YGGhKz4w6KY3ekOMscWEbOt8mzkAlI3oaak0tt66AEccKGncp26wM0Yau25lrM3ba7j_guJzpo6ANS548l3ZUMWqlhfbWcoXrUHtabVrov7cGWOnxzuX3i3KJcRrVIDLJfaWxs7Hnakf9t2IoYCAB_Ph7htqaGIPekgvTRnhOwn3q-rYmtHMSwygxDuM-rUFJUxtS6X3hBuoBS9Y4jtxWdyrE6OWISAURYDi0SDS9NTFU6NS9_ldF8VAcVNdPmtdzL5PBtcj347XN3HQfxtgEC05lv5P6hQuy3DxojJtZl8ZSvfKEA-lRon3Dld02sXvLFyRwqJzqP-65re3zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5Z7758IpCnTzAFhc1OA_wyNJwT7-eBuf3n1PYowyumHCJQ0avB4znzwye4VWoQof2h42vDw6GU045nrj872L-OOuVc-BceRVQT3t2pdFH0WjaknNlo1aNDBpy-CNKSKwIe0pwJ8T3Kgg7A0PLrwqRJrmqjKlsw54LIzxMGzno7xSd7IzxJ7QmLz4lx7DnJrIYKpnl9PVkZVafLGzG4AN8LtcADBADiEvH--s_Iywh9Of_xbmjtBWvXp7AaZTX_HwYVhmX7acpYrjXQIiJZS5Km26c_jWTyR-NqLymt5fLN1gQ7gMX2RU5OREPzJ9G7yrsrNDaQm2r1gulBTvFbbzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKSExVg-3awxqVDRn_Gmf7rgItQjC4k0L7C21ChLNyhrwHM4tlzerNE1mCPvVRrCeXmQKE0YEt4svalm3SEmkFH9QvzAODTZHNProFnDOQn3vQrveq-bQj-voXWyM8bkWnySovv3V7SqQ9DIyvZ2rrWECJitjRwgPRjNIj7O4n-FTVNdOEiR4wuFigqGCypXwM7J77CgYoowS7o7k0LUfkICAbZaaw9_FJhcXYfDKHdXaYmpuElj-WVbdrVtp9EtHaVqY_HGSbGF60EAMV1WF-ng2hANXyEbsSfhdPXN9zeETBnZlO0DPtLb9ZIzriVxw92N7szxjz3qylYEyFRo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=giaDLplCmaPIt1vHQxZGhs6WeNKbP42zNdDVJYj4b1TdWN5r1FDPz9gmQKUtm0NkgGZ-srcWkoDHiLVIrQefKv7tNfcMxHNr6XUN_icvQZbwdLc3wgjwusEU_1mQnlNL4rKcsqLR3NcrGWLHFV6ZJB3MPMnWZL70wi9mmjSQHhUrfI4pY0UR_SOEXjXt0EU7QZxmQZiKV7XF0Z-XllTtZmx8qZykRsHYhYNHJZmjmi4ORSMoWxS0uUpLqKhoa_BY9f1i-IP145ajO40TPNXFt5aaSUBLeZQ8XICED7tpWIWI8vy-s0egsnaZV1MD68a8sddC7jC2tANsTAlpa2kWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=giaDLplCmaPIt1vHQxZGhs6WeNKbP42zNdDVJYj4b1TdWN5r1FDPz9gmQKUtm0NkgGZ-srcWkoDHiLVIrQefKv7tNfcMxHNr6XUN_icvQZbwdLc3wgjwusEU_1mQnlNL4rKcsqLR3NcrGWLHFV6ZJB3MPMnWZL70wi9mmjSQHhUrfI4pY0UR_SOEXjXt0EU7QZxmQZiKV7XF0Z-XllTtZmx8qZykRsHYhYNHJZmjmi4ORSMoWxS0uUpLqKhoa_BY9f1i-IP145ajO40TPNXFt5aaSUBLeZQ8XICED7tpWIWI8vy-s0egsnaZV1MD68a8sddC7jC2tANsTAlpa2kWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfikSsKPFaNf6pZU9zd631NiG-igzg_ulsBMxpcjQrH3xl6Bd45bxaYzAXf4leEHr6Qj8Ch_-onkcXKUMoeN_EI4JliYCJ9OVQzaquZXlCvhb1ID8SWQVi0xWT9jdHmi7ZNFasp9NRceecax9kuQOgrc68t5-Xbazkulw0IUT4wTHVFqOD16fg9bySKrWWs7Iel0xyX_0nx_OD6PWbeAt6bh26kPmSZzXOYLNMuvMs5T4pqXhGEGHBp49jiq9I_h9Vlao34MvJKwTJ8GTxGFDIPYXYrnZ4iGceCmMeo86rmmbf3TkCFZJQ4UYdi9cxLV-zm9KlBCZQZOhDyVVGoEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=NLYXICGWnwC89M-XkJs7_7DTUnZLjLpYkO7Eu1gmyqcJXeE57Xm9iZZvHyeIbTXTarioN6v56CjQ9T3lCyCrqy7zs9mqiPFLqGGk4ulH9BdMs6uMMnVcCx3HRq8cONJH0cfyBZUIRauG6EghCDkkLicLedDw3PK88BXUU15nho5P9P_MjAxy0FndOpxl3KI_WxuUkIr_sYdM5aVVFh7z9qfM4QpSb9AGs49t3xLYh_GNhfBK4A64k5XCneaZOrzFgTzbPRt5lptXitZQ_C_q7AsCeX9m0dQoxGD77TZXjHmiio0hIv-ME_pur9ZY0Gu6gXbk1bF1qD7p6mmwHB3X6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=NLYXICGWnwC89M-XkJs7_7DTUnZLjLpYkO7Eu1gmyqcJXeE57Xm9iZZvHyeIbTXTarioN6v56CjQ9T3lCyCrqy7zs9mqiPFLqGGk4ulH9BdMs6uMMnVcCx3HRq8cONJH0cfyBZUIRauG6EghCDkkLicLedDw3PK88BXUU15nho5P9P_MjAxy0FndOpxl3KI_WxuUkIr_sYdM5aVVFh7z9qfM4QpSb9AGs49t3xLYh_GNhfBK4A64k5XCneaZOrzFgTzbPRt5lptXitZQ_C_q7AsCeX9m0dQoxGD77TZXjHmiio0hIv-ME_pur9ZY0Gu6gXbk1bF1qD7p6mmwHB3X6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaMsfau34NSLn5E_Lp_j8ytqXOHGDe2AWV7X4SeLfJ4VQ3FM1aeOgfhi8PW9t6jSzVb8iiC1CxWPS3xcRTfoc0S6DC7FDgBq7_2tYT5fOOuGnFEMRXzyDMMKNyGDHonib0tcreHqUzDNn8WLLcqsw9GrswMbx3ZngerxC3DjKLYn1aU54JY9VUiqMjC15QsIrC80jdBcpY5iKcp9hPiZ4YS4cvn93xpsUH1HcaMuicx7tsU2RLID1iMde1BzXn8mULrr5073nJF8aj9MvdHncYz0Wj7IpkrCwzGeXc3ro2wKFv_w1up4Bk09aFXopnS4SSV-NY_WxP7AAxf3kL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFdA8b3Hefx738vdL1zKfztwqC2xCOPNM-0sJm3Rnpi44ehXhD-l-UJVMc1ZAdTQP6roznOZb24E7Q3lh8gm6_yAF45kiWfxhaR8u7VsmNZM4_YpdWvGLz3eWOc1Zr_5EEeYlgl4viLVMAKauLcWZ7izGRANYYqOD6ZBC5pLpMFuLjGfNGJ_KKAea24c01526PHzZ7-T0_bat8_BjyTSh7vFQu6wXc73A5nvKMAXr-iw4ZrB8h3aLWQY2PY28q3ZLSUWtyCAGrrLqhnOwcqtEG_8MWtwttiMd6OY6YPP83U1Izmugyvug78tr3FgreY7MJ7l1wSFD4a5TGAo3bSosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYXNS59OLfsAwWRDhpKJ_1erurct46YfkG5ZrYzZ9kL3rMQfiqSt2Yd5U_6bGGUbAVfvAg2GEltaOUem2DSRbTLMBnoOgTv3k3ZH7q4HTcoBy0rcmSEZ4Lr6FnM1Yo2l0A4u5MnEQ14My4B8qYZLk2H5WgASjrhQUsqRsVutEzYi2qaoAv8MM5cL54H_mjDK4j3XyYaHcQx0BRmX9-bloJWYAOLrxwC5b13Otr5tzOq4fCfHITRKxNsSIlg-x-vfQQZGG6bC-sNBG0TAiRHDublXaqQP4rbPl-sJb4CXWaqzf2-E1Yt60IJ9jRpAkTkGOOoXpxW5NjsD80usAlYS3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5cZbxb5p7gHtDJI2_3sMhq0nPoEC2SK9ORoQm5t7AceHs3JCRSr1aCxBGjIZe7cjAWlxa36nsVf9voHZCRJW7gMIw3VMbk7Q9qk7PdWwmSh4vprk93gNLpHw23eHognEsnoWLcyNr1sMODHh28TN8qgvlhuXmaqeon6icxH6zrqh_64A1qBSb3BMe3oTj96oPzHZG7Dqa4D_nw3ywOrBvCWRZRACF8nzG4Z52hijVmyOnEf1za_PVHP8mJfCGw5Xj0tpgZ1V0xiZ_s_k6prRpUIjQyTMsuMraspjaVKJxLX_S4cji0LSEcKzR99G42oJRp12Q9ZJD6geCAI66bwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrfSJQxcoDh5Vk7OucBxA6NHPQS1pjw7Kigm76bXOXpI_MV9eb2qyd8WR_35aNI7WvnOG3qs7PcF2014z7VN2i0QJx9G6Mp-9VM-W_UY9MSlD3-2Z8MD4iNhg_i8m9Usc-E3EUyJuAPRya6_XEXHXN7fE17TQmiQmpXZE0VywmPgho9OnHPsnD-Y02FxakVBPmJfdRWULZ6LPg79rgjqVMfCbiACtlxd3D9zxQO6AKl_9xMiUO6Db4F16_b86m1DoblYIJ-2_EjwU801UzoXXEdhGldx_xHYb5qaB4vO1ugaQNNdtq1sF8ZcJjU8KMJx6LP-tdGuGmFfo6_fmds8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZciTsgatI--lUyCdIOvpFnOVuvW5I8gTFBaBaondrbQ2ZWqvK7tlYBNtbK1SYPREYpd9aw6fKd6Sb9OmIS5XgeX0CmcG-T1CeGXwFgOSb2MSf6jB1L0qYGV_pUQQpenGBctMbqkghz0c4-6-pMz-9QT1_ryaHuLpQbtdfXleo4KJX5AVcRvdF9C-OFowDUAJRbjRgvrtuzJv_D6-dZs5WlegiuCh1vYoH2yLn2kwnC75KosZM-AK67jJgiMIxfGJUgsDgZIR63OgngpkB2yHWhNc9yDLsBXqB4U3YrzjOfqy5awfFqUu2-66m1btfI-17bq58iB6PLcfUVDeiPfQ4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=mhIi4UnsGNiwcnHhdGc7y-y-WF4dAwNoMeXgV-0ywQBsKoqhsu05lekCSTXEYLi4ZGH4I9yQtnjSPW8oRIfINTVvRLwId2XLK5Veksx38zVHtYsXjayV5acOYi7LegbbcBfkrJVGWPz_dB81L1yHDj2MXxc0in4V_vn4yVgfGG2GhKzqJsjbTto85PKFZl9vnfi3E4L02pJvXfRdPVhc0uNCAZrSOOxyoQ5FvljG_wG75aHsp1GF9UO9Gz2ZkwWozT1KWYj4YeV8_l9C65y7kqUHYNIS2RCZHpIcCaUrE0syYbtAnACABx7F7igR48IF3JjGE0caKNttsbYvHleBmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=mhIi4UnsGNiwcnHhdGc7y-y-WF4dAwNoMeXgV-0ywQBsKoqhsu05lekCSTXEYLi4ZGH4I9yQtnjSPW8oRIfINTVvRLwId2XLK5Veksx38zVHtYsXjayV5acOYi7LegbbcBfkrJVGWPz_dB81L1yHDj2MXxc0in4V_vn4yVgfGG2GhKzqJsjbTto85PKFZl9vnfi3E4L02pJvXfRdPVhc0uNCAZrSOOxyoQ5FvljG_wG75aHsp1GF9UO9Gz2ZkwWozT1KWYj4YeV8_l9C65y7kqUHYNIS2RCZHpIcCaUrE0syYbtAnACABx7F7igR48IF3JjGE0caKNttsbYvHleBmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=uEKjlW-G8ybTIK10Mi00TR7hHxtNpi0n1lFCrrpqSiiZCgLacWnGS6wKVYMw_KX6_EqRVdUxYRwZgqyiHEQhi_WRo5xU1Cps5memrNZ31y6_vmDQ7ycbRZucp-DJ2SeAbpAyKHy0-JepAztuglGrJC1tJIUsTp9iXLcNe43nyVN9FkCLo2C5Ht629uTEHqT-9MWTqfh7Y_Zhwx0oyH6Pfy9gqy8J2pqKIjI52YYzooJLjWy5bXdEMPjU6SHGMBoJmx6KIccu2Kkr0pcv0JSZ0serklPv5Q9nMeibTKTVqazDJKWDzvpS3gKVftftiw8y5uK6JIx1zTmXz_KsgjcZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=uEKjlW-G8ybTIK10Mi00TR7hHxtNpi0n1lFCrrpqSiiZCgLacWnGS6wKVYMw_KX6_EqRVdUxYRwZgqyiHEQhi_WRo5xU1Cps5memrNZ31y6_vmDQ7ycbRZucp-DJ2SeAbpAyKHy0-JepAztuglGrJC1tJIUsTp9iXLcNe43nyVN9FkCLo2C5Ht629uTEHqT-9MWTqfh7Y_Zhwx0oyH6Pfy9gqy8J2pqKIjI52YYzooJLjWy5bXdEMPjU6SHGMBoJmx6KIccu2Kkr0pcv0JSZ0serklPv5Q9nMeibTKTVqazDJKWDzvpS3gKVftftiw8y5uK6JIx1zTmXz_KsgjcZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=XZeiPjU-GTMzWEb5xmm98V8K1OpMyk17B2BXYr5BDVxDtg04H65pbyMRR6kSLjTWZ2dbVUJi99UN7LVSIuFt6kIqSllbgs9l6nEg9olxGg2YfhNO0mH8ya6UmG7yo7ObeJpQW51ZKonyhcxMyKe_7Abah8cnUST6lmZXnY4EjnGF1U7KmVZNaeKFfMD1NV9OmZlgwQLEu9RICMICnLuQYYknJlUIy_CDzdp727ayaMR2Dx6mPaQ3gRQTGM0Xs9X_JqSmr8nQ45czHMFvDvqU1WwG21qiNHH2GozELiQ0CoNUuRpkeZ1HhhN6U99kbZWax9YlUCyGfhaah6l_ha1icJKzVUYsIz7nZiAGNdId43YejVsqULWTAd1x8PpUc651TXjgQfFnrp8Os1Z6EnRD6RVb5LXQu8cjTRkPR6IXAB80GEnimvmOlRAU-ajjj0-7ZhjU-bpVZlevsVlEm00--0XDnDKm2tGxQz7_Z49tkuCoLZL2_QKCW2yVcY9_eLeT32s35zi7Mn92u2AihdJOpTXksbYoPAT_WU0qW5nCVi5xIB9RN4B_gQ1BFiOiqqzKkKnRZ60qU1ggY1de3y0v2PxKsaMtCbkSfKq6cioaxgvBlUrF-7cSPW9bPTtueUY3c21eu8OKzrYmqlyDa-sSKPkhEbAL-ANNxYx1ILf6zUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=XZeiPjU-GTMzWEb5xmm98V8K1OpMyk17B2BXYr5BDVxDtg04H65pbyMRR6kSLjTWZ2dbVUJi99UN7LVSIuFt6kIqSllbgs9l6nEg9olxGg2YfhNO0mH8ya6UmG7yo7ObeJpQW51ZKonyhcxMyKe_7Abah8cnUST6lmZXnY4EjnGF1U7KmVZNaeKFfMD1NV9OmZlgwQLEu9RICMICnLuQYYknJlUIy_CDzdp727ayaMR2Dx6mPaQ3gRQTGM0Xs9X_JqSmr8nQ45czHMFvDvqU1WwG21qiNHH2GozELiQ0CoNUuRpkeZ1HhhN6U99kbZWax9YlUCyGfhaah6l_ha1icJKzVUYsIz7nZiAGNdId43YejVsqULWTAd1x8PpUc651TXjgQfFnrp8Os1Z6EnRD6RVb5LXQu8cjTRkPR6IXAB80GEnimvmOlRAU-ajjj0-7ZhjU-bpVZlevsVlEm00--0XDnDKm2tGxQz7_Z49tkuCoLZL2_QKCW2yVcY9_eLeT32s35zi7Mn92u2AihdJOpTXksbYoPAT_WU0qW5nCVi5xIB9RN4B_gQ1BFiOiqqzKkKnRZ60qU1ggY1de3y0v2PxKsaMtCbkSfKq6cioaxgvBlUrF-7cSPW9bPTtueUY3c21eu8OKzrYmqlyDa-sSKPkhEbAL-ANNxYx1ILf6zUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuvSxepVcZxvhSjSpjG2b0IgHNmypdJp-QBXxZGDqVChMRdg0F-3y-3J3p71JVY4BpizNDCP4kQAUmEuzP6oxKMwLpzj-9i9PcQUVi8X095aiR1-z-6yZuajDK33P05jTiw0hxUC1TVMsBR4U_u9fM8gUtSv7ie8xe-93_F4SudpxxwnFuq6okYZCxjmR9MBTQta_evYWct_2_LbCXvlLAvzdnZ1BdfkE57DXdTzk8JqrOcUk78c7G4CzNHBiblKg6lacF6qD9w2-e6zabQgY2jaZRFztZf1Kmo7-ocBnCTMuxv98e4wLW41MF0bPKUvBIsc907rcPGWTefL_sutyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApwBj56ADNkL1hU_VbdzVPpJOzAGEiLvMycJzmIseiM_m5ejEjM5r-tj6-BZGv1bg4BmGROdB8c8PzWhjNXeA-AfzY7NaN9nXGRuyBmRMTxNg4m6S7MxoRJvx8eCMtDfDcSPiYr9q7SvA7vTc_iN2VXT5zBRmlG9x65SqS6OfP3g5ATkFy75SyblEWoMUlIhCKRtUecQSa_MZwrsNEts13QLZF7KZMNnOkgzxE89bYAgxBBRy97aweo-96XG4ypozB1LvYw6DmFe8mVtRLIBZ2Z7u0cijdIcn_4qCjLQEzLd4EPQ8-YonZXRak8ZLrTu5HMtb-1NoIYNj4bonjYPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apVzD9tyd2a17FLipZlgdgbCFewRlI3sQvMKSzRvs-zEfiZr6Tcb5ASp4dISUE4M0xbRc03Heet8JrBaCtpylaKLx7W6X9nRab7cAiOhfxVKAAHJhlwDUbZLAUA3dl31HcfmbOmdOR6gvf4AWHbnW0lNy4W921VJVl17a5tKEW0DQg2mFzK6F3d-lXNyBxyMITc6xo1OJvgNmBchN-vmAhuDr1LqUVPSuEcphKwb93PKg73c1UgbgyOYND8PMePtpfFBUTxK6SOtQGNLWHueAyOBYm7HpYs5cmup90zkiKuJjZneWGJz88WF6gP9CIZ3vIWbSb0vZH-5ZWcCZ5j4Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=vatavfQQ1cF7RuJP3P6a3ClqYfNK_YUJUdLZ6S6n_JCU96LWab8cPDfVgP7uiQiJVLklsqQwAqZ3aBnF7BajXycBx95Gw2LwFBgZb7elKq8Zey9mAqxRrjN-peRoXYgWe4AyoMrij3gz24w7QUi0OFhutVOMJYBYivBykb3_C2N7x3lO01MufdGj3yUBfVEi6YHXEDfNqkPOpLOc-3-gky1vdYobJxSavd5axFAG57zulPOABp4h0RnnfHmGonbqvLpn6ycEGgGl9VEJn5sR3EX7tnQKE0saNQwdUUXMef7DKbU2bQYvkl40CHc2T1PJP7qdnqWyklvQyIOim_ifCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=vatavfQQ1cF7RuJP3P6a3ClqYfNK_YUJUdLZ6S6n_JCU96LWab8cPDfVgP7uiQiJVLklsqQwAqZ3aBnF7BajXycBx95Gw2LwFBgZb7elKq8Zey9mAqxRrjN-peRoXYgWe4AyoMrij3gz24w7QUi0OFhutVOMJYBYivBykb3_C2N7x3lO01MufdGj3yUBfVEi6YHXEDfNqkPOpLOc-3-gky1vdYobJxSavd5axFAG57zulPOABp4h0RnnfHmGonbqvLpn6ycEGgGl9VEJn5sR3EX7tnQKE0saNQwdUUXMef7DKbU2bQYvkl40CHc2T1PJP7qdnqWyklvQyIOim_ifCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=X18DCpaEUnIt6vBGyvxU0_w0BTm73rv0aaOAJgUhY3UcXi9pjjjlbRas44gm4jrgglqgHB2hBv2iBTbEyP2C1g09AWPNJ3iscjpcoQHLhpCSwNjtLbVCiRTAhR2AL5qKJMRIFvVS-hWTHsOa-dbgAIHU8LaErHyGb-UHGiKAy6SpTI28AZs7JEqcG8KcJwCii2BCvTTDL1v6y-zSd6gEL8i4H-cVZ8x4YTRMykBX52WB9ZppJwTXuqxp2wDOCtS5s-i6Fjqq-H0cbq3IHjBEUvQbIzHdBF0oWaySaLECZuTfm9uc2D1KjSO8fT82WHH0FsDD39fgWR0Hv0kHM8zT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=X18DCpaEUnIt6vBGyvxU0_w0BTm73rv0aaOAJgUhY3UcXi9pjjjlbRas44gm4jrgglqgHB2hBv2iBTbEyP2C1g09AWPNJ3iscjpcoQHLhpCSwNjtLbVCiRTAhR2AL5qKJMRIFvVS-hWTHsOa-dbgAIHU8LaErHyGb-UHGiKAy6SpTI28AZs7JEqcG8KcJwCii2BCvTTDL1v6y-zSd6gEL8i4H-cVZ8x4YTRMykBX52WB9ZppJwTXuqxp2wDOCtS5s-i6Fjqq-H0cbq3IHjBEUvQbIzHdBF0oWaySaLECZuTfm9uc2D1KjSO8fT82WHH0FsDD39fgWR0Hv0kHM8zT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=csWtWLsQHhj64nKAplo7_tBjnir_uXSDPfMsNJ81mb7AF99fvzwDzFexCDkDfvWo9Hhwqj84ojMGRcNBrr9E9ObLOX10tl-8fNCC3vd1ws4ImBJMxn5NCRIC-1nCm4SXR8wslcCguWERN_kobFs4jOtFjEfrivy_UI8D49JntCTL2KHAbZfDI6mXRw-MD42MZBPR-ezkm0SvwZG8A1cKd67Nk7EPSnBjbbbsxbrEXOXGXNTzdnwAD8hVCeIoHq5V_IRvxuzPA3lirT8_uK2ETMtU0ka75-LHpXtUPmlvJnM0bzl-qQSGZD8cEG3WQs_Rkltat8Zeq-71-sby0BQj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=csWtWLsQHhj64nKAplo7_tBjnir_uXSDPfMsNJ81mb7AF99fvzwDzFexCDkDfvWo9Hhwqj84ojMGRcNBrr9E9ObLOX10tl-8fNCC3vd1ws4ImBJMxn5NCRIC-1nCm4SXR8wslcCguWERN_kobFs4jOtFjEfrivy_UI8D49JntCTL2KHAbZfDI6mXRw-MD42MZBPR-ezkm0SvwZG8A1cKd67Nk7EPSnBjbbbsxbrEXOXGXNTzdnwAD8hVCeIoHq5V_IRvxuzPA3lirT8_uK2ETMtU0ka75-LHpXtUPmlvJnM0bzl-qQSGZD8cEG3WQs_Rkltat8Zeq-71-sby0BQj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=tEzAV3FJlcuoCPei6j5gAnIOGb36NmumIflEfih5Ms2a8g1maIuroTAro3ZysuGxAra97F1QIx_2l3cXEtcUNBRZWKk5Jzq5Y0z8NNvlyw8chMI3aWvuVknsUlOXvo-0iv8R2M183xzCD-qEgDpNF_u8Pthxe8SkeNevg58pumYgi-yOqknlZRcvKBCRZMtyHGUlUv4rLxlxL458zUkrQ-2acAH74b0zSSIgW-N3mr7T6ZzPJ--6_5irpTp1VwjytAntwmm_YgZqeU7DPgE5-49OwawvgWgrSvafgqLNXkYPLR1tvqrC31PfJq1UMLUWetHvBRjGMZ8MXh7OnUpbiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=tEzAV3FJlcuoCPei6j5gAnIOGb36NmumIflEfih5Ms2a8g1maIuroTAro3ZysuGxAra97F1QIx_2l3cXEtcUNBRZWKk5Jzq5Y0z8NNvlyw8chMI3aWvuVknsUlOXvo-0iv8R2M183xzCD-qEgDpNF_u8Pthxe8SkeNevg58pumYgi-yOqknlZRcvKBCRZMtyHGUlUv4rLxlxL458zUkrQ-2acAH74b0zSSIgW-N3mr7T6ZzPJ--6_5irpTp1VwjytAntwmm_YgZqeU7DPgE5-49OwawvgWgrSvafgqLNXkYPLR1tvqrC31PfJq1UMLUWetHvBRjGMZ8MXh7OnUpbiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKkMPKkKELd8xY653KhbXYyy__KrqnBE4L9sOhGA3N6QYHElHgl9zJ40j8m3icc1BfgieEY7BrCOd4HKD_7JKKLaMp3OtkZxBf3Q-I1eLKrzspJWcX5zJNHMN5dqmpWZi_1psIYssMBetzu9naNAW6KF2bJuaMJX3CP0Q5IxdC68-LTekwMjNt5aBd1XKfCBODd69Y39ABfnab8cG8kLXUKGLMJSd0GRUar1FsjTCl7ibt5DnJX7CBt1wEF9L9PF3Q_kuCBFYoD8IKo_Q8_sc42VE5zursNCQ9F1cWFjbCnbLCWsQmr0LjGNDDry62gnYGC409RWBOV8CVDhrL-XWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxfW-nFPgjfWozcwcY5GvuA09-9OhvoE5lRLuqRg59t7-iF2yzbKT5tBMk6QqBvjcGBXGQVi1C4yR744mmzvp5RXsdw8YABPcwb-Ac4v5URsPaDotBRNCtgz6Z2I4ujnaT0fMwSg0qYb1ZaA6VUtG_n_l9t-XQK1jF_qw8KT6iUlF8u6Yyp9dCtly3sHiYXQ3i1G74-FLHsYCLbZcvNJTCAt20TMaO7GoSPfNVkKEKpHZGdOnClqZGqDfqF2GUAqG1jnLfmgSh0UWJg0j2LjgRlyvcul1kdy2P2UQihXe9jN4NiDOcSN7pL8K_omnzkp0O-WL7SyX1zhilTUkZSzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZa-x0HUKb1IKfI5PK7bmy9jzWYRKDSfEssGnS1VrfAQRlUGbF88YVtUaNqZ0LipRBpeEkM8IPHh55gyzqq6BYSAV0P00RaPcgGTEKzSIjRr9ED4eUtbtyZZ1YmVMUQjxz6GTK5XyZ1clWw3b0XQnF_TpOGQkXmYoUAfXvRqK4CmxI54H7Z8gbWyCT0YEIaycHVDZx4iB8U-U6GmpOA_gWP_-yka-nP9lOh7g2uEs5cjpg6YfBxhcbsduwJ3mfdpjM3YyfluSObHXb0IEgM5h8LQ69lCCM51be055j7QbAtfLV0TTsPTqlo-ao834YK-IytzcOwWVBlvh62h8cpOsLrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZa-x0HUKb1IKfI5PK7bmy9jzWYRKDSfEssGnS1VrfAQRlUGbF88YVtUaNqZ0LipRBpeEkM8IPHh55gyzqq6BYSAV0P00RaPcgGTEKzSIjRr9ED4eUtbtyZZ1YmVMUQjxz6GTK5XyZ1clWw3b0XQnF_TpOGQkXmYoUAfXvRqK4CmxI54H7Z8gbWyCT0YEIaycHVDZx4iB8U-U6GmpOA_gWP_-yka-nP9lOh7g2uEs5cjpg6YfBxhcbsduwJ3mfdpjM3YyfluSObHXb0IEgM5h8LQ69lCCM51be055j7QbAtfLV0TTsPTqlo-ao834YK-IytzcOwWVBlvh62h8cpOsLrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWMCCMO8Knw5ZLO0IFrAJE_AmBc81rAq6f4QcRoUdPk8-Wu0i0NyURy12QW3xcKs4FgMjRm9hc7eL--1xaSnBuy92wAqNzB8sCoizVqOnJJ9R8aTwquZBZUd06dYxh0nAsL9JO3FbCOL8wHZ5N5hRXh4HYnDIniytMJEzO93Cj9lbm9Opfrk-yB1dfClH7etLjBPkBCVmV2-utU6osOnLkIS_jasUqNlwa_0FlvR3SZd2JOqWVAtCpTcEHvHvAC4f1giwCRWwNdjDKgokXlCV5y3tUclNXyJf7nEUXJUrQQaRUCXnwfPcKSyCsM6LoA-N84XwEOOSM1Vf8_842B-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=a0WkG0ZGHOhL7owufHoF-R0xS_lFc6RSV73GLSgc8FeVdKkD9BMmovHZ_tXxuJkFXdaK5gycBK-3c6oDQXLIk9A_FnJJpBIKHUb5PPRPmehJdGzN78xdSM_VEfaiwvPx_yMFttYtn3ElIrwdBMsjJXxXop3PQgslXN-F7FvYbRunJOf9EgEJKShX_K8IGYcfb3T35wcPAeIoSeeYId3L3YCOvkhrQAD6mEypNDTw9GTIq7F8hLhJ3WvB0hdiS_8F79MN1D2Vu12eM2VAvVLj-l2itj0k8z3VXOhhH-mBoaH2fr1GjvMvTv8chqOd9lvVYZpp7dz99wLUnaQX6gDbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=a0WkG0ZGHOhL7owufHoF-R0xS_lFc6RSV73GLSgc8FeVdKkD9BMmovHZ_tXxuJkFXdaK5gycBK-3c6oDQXLIk9A_FnJJpBIKHUb5PPRPmehJdGzN78xdSM_VEfaiwvPx_yMFttYtn3ElIrwdBMsjJXxXop3PQgslXN-F7FvYbRunJOf9EgEJKShX_K8IGYcfb3T35wcPAeIoSeeYId3L3YCOvkhrQAD6mEypNDTw9GTIq7F8hLhJ3WvB0hdiS_8F79MN1D2Vu12eM2VAvVLj-l2itj0k8z3VXOhhH-mBoaH2fr1GjvMvTv8chqOd9lvVYZpp7dz99wLUnaQX6gDbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBmVW0LOI7VCTehvNPomwXfCOqYtKZtv24JUXFRA4ipfeC4MrIMSnl6Ew6hFql5Ci9i6-j_TytczyCj4sGy2pKnoojsjglHJ_W6LxgtO9Foq9__cO0yHUav2OF7OYG7Uxlnxlgr-U-FGMiy2s6GaKczycasIX_ob7q3VWguabNt2-hNGxSHxNgVAsMEs5PsA6qpkP5wt9F0av2RYzLQczk1pmL-2x1nziOrPFcQd1Fa-b-msSsBgjQKtYuXcJ6kUtnr8E8V-MbFDgs_vTx3l0tYOKNcGOoD7xI9pUpXLGBzQu9G3S__JjyXtt-9TWQJ4HgJmXIU216Ou2mDpNP2Q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Out7d832jU1DXF83QNj6is5zxHr3ZytTQ2as7vJDbiIRZtjxZXk3x5venLuiwY4Q4ACX5QgDmH9YaL0u3uLxUpyItFon1lxURl0QFAWuGNmcjuS5wcr_d3kbWUAVOQ66RAIV-aRMKXfDl_Dv7Aa_Qs78JA0vynXLznommONo2efL_akqUnUP5xEt-GMfCClvOYyGym4crybBrzvbNXAoEasxB84VlFA5HYVVdpn-kkePjN7o1jFz-0u-b6sT4DxTD_TCwwYmK_OVIsu_bExpyQWlaSwq_Y9eIYhGGDvm7UkwrfINgsRE57dhQFIY1RGjVFTz6VahxaN01kX88_Qhiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBCqix48tfz_2CfztZpmoWxxnZoKDRvLXvzM5u4tZoC_-kM_bOKSymt6B-mQkYt9vhO0ffjrtFQLQN3SzMeR15aZJNzQ8wfsebgybE4ePh_6naUxn-IA0WTTddsPPW17smFzbWLkKgzNjq-qnoMk1RdNclVZ4NJlbk2HqWdI4ERIIezng2fbyW-ofRr6ELF60iBmM9P2WMRIyVeslMMWcXrMeiXzm2lksOSdg8ad_Fx9Y-GJ8d-Yp5g1B6F3yI0KTqbuDnKZgAnyTRmh-vQQLZJKqRgrBzZBABapaeRLpYhmPPT1uaK9ZPw8o_Lo4890JnOLEx_-rr2gPGtWnK7tTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji2279qBP-I9MZkztx1KUyx7K4KEnYMZBFbAZkm6s6LNLF3R25qvWRnEux3RL3ucWTMpUHgePkn9GOj302aEwKJwzUtG9aEtnDIMciGWlPzNcdidpEt4Cr8r0h5u4dGwDLpL-cWCSVcpxuboQoIHunKxJM8AXOEE2Jx_Ukah9U6I3nZa3SX9kVWqmFlPYjdEzkpYvXtEJmnjmADy50_rudIQQTlC2KU9hvX88tDwgakU4giBXALiLI_KYCicFlibxazbVigx1HWLn0gGam9XBzJxn_PQObkQG6sJ3mVtGpzCRw1Ap4CtK88goeKXXZWf9HxGdUZh0bmQuomHMnk-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPlRT1kvLqa-pPtHy__ReRnyyZXeAXy9ZVYZrY1GIBA0XLQeFXp8nizYGui3VHfAL1AJqEdAuK3pab0Gc7QCYUt3JWuECPaKFJJ3LWPEHABggHcMhE8nszk6ca_W3Xlx7i9uZIyPcuFuqT2BDU9r0UqjJXmvBbb8SEmVyjnKRowRxDDDOovdTyZR1KwCcRMk016I_tez_YSN6am5hLUYUDQZk2ey8XsgwUvvfyrNkWBDu2egQnEiyYD9btaSn_KRpM2v-FHfWESnPh8WO87hNRo5_zVetE5g-YsgV3DFiPXuduSeFxj4qi1h-jB33_cjEYOEPphS9DOHRqcpZDp-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0iH2bFSPX28-XxwOrHFngUyKhDQPsLj0aoDUoF6srJvMw2q7wsdudpouy4cPUy99WqGP0r8frTp9C47Y3CigOEz8QAAuSMdXXvMFmpikpjWh-ruYtI4bky0OXHC3_sWU-CyFV_jcob4JzaziJHzpL_qprwf8k2dfT4G3U7TS8LQXzXVRsP5LJ_5dksNRg6TzeBg47OZCjABd5mLA9XYObcNU89r9uYxYKwcSDKikSTFQ3_SvhJt9PVsbWAdcy2hDQ-0l6gHCemW7PXTrwMzzm_lxc27_Vyw5-vy1AtO-diSq_CnvgsgxmpwGT2M0PKwGHjKdIOeBpKhBndZWoqlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=SmWbuP02jwa9yhTFtchL7YM0WvGFOKNgNCNVqhL_HCvis1frqi3ckZSdxR4d-NUCLt7GVAbZptr3b8zz1X4Uzcq6pPBCAxlJRtzOq-L0IGtjqtUQXBcMnqo1EGdXDL_s6ITiAsObbJNN02j8ePvVBJul2NCYpC2z4wonfTxQiKVBad-b5aZl7n3qExvhxLDe4J7eXMESWxiqjmwA_yZgwCtJEpGr4eLQWt3OP7LFziXm4xlz2z-rqi0hFAiy_oKHH566mUyVbitKGzK66d_3aAnIQrgXkKMjbnJ8k4EVW6gbitLZMapwhm-Gl-dj6O0aJEaMxISPoYaoY4ULVRCyxLs_IvXp9aOjnOz-VpHBiAw1j5kfE0fVr2ocoGE1c5khuKA50Kc0xFCUmhJ57yMpC4MMgpxkzEOgL7KcICMHrRTA4zejo7Qcl-P5YMTnyCFWq7xizObShVn8GAzn9cPPOkBZwnK7Oz7cfoP1XuWO6bgHN88hWdrg-08oJth_gMb35_5ex67WYh346CfdHEhoerrEABI7S2iV0JSitdhnt2Kj2O-nSfFA9Fl7EdzMY69PQOq21zcGPTaUWL2_DCiKF2JhXcHnkkFkRH7YQod1_VYfWYr6uGA1QjhbxarS1RZiDZ5Sza9BQ1leFrm2ui2tUESM7wyud5m9hv0I3UpDMX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRi1gNqt7fZKNfpP4_J9sgJz5PI7wb9LQfNjOK2IzLSEo71YeKa3yHk7jGRx_QU027vJ2Y3eHGUFt2x2vb-1scQttoMCDneK_EBMzYZ9VGn-VdMbjQJimBu7bAO-NQDlIAgG37X-IeJrurgqEsseE9p4CVgZB_TEwWNYwSqv2Q1N6wvXzoU2U0fcG44iHxZkxfWHWNZGl8N3JUJCeLUw8lDOEjDsdQm7utWTblmCeD9PPNEbNYPl_SWvt4FuZZqg11Ykxi1IChucb7p-Ss2klFM6lq4ZG7PiG6PlVsMVNpDPiRDFkynrjDGMgJIHfLJ1fHxOSQbOvG3bX7Sn3YVghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=M-ZA5WEOu22uaFlokNH0xZAnn6S0tOZvFKOzEV9LLL7XEw8K8QoqkBLpHcBAhfIyIU9XtQVRfKwXLyBm_cgwiDRCgFkUcK_EM5aE5wnST0la3BaXPaTEkW-bGF28heH_dCfrZsBAyUkaTkzGsHKyG5xUwiyqmax0qN-b2LeKTEL-1uRjkgUA9x6cHyuj77P7e7PXW7dmsvTGFLLdLqMcrBYskm12ylO3FCNt1zUNMHMH9YCo8SKqrj5s7wQiRq_N6Z9VjbDE6AE6204aj8IAB9mE9nK43K_LQw1EYF3WPHe5H0wP_r7VDRAmb41ALZ7mcCaXgE8_7kU-UJIgFQz42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=PZpOjPAK7SSQl0ZntKnVyKbf5aKxUwsxD6bMAuUaOdeupwrVy4ZQJx6JFX4ioaOg0qGPMBhkTWADFWt0CryEkjoJ571-3x_OVjUxYYNeBmi-KbfvIAIWnC_SdOZ4TabjBG5pVaaYAk0meZ8ZQc7PZvqoPEMGHvjeD0ot5z7q3jGhdJp85ZXeKB_IPosN2M71NZJp3cyDwB21h4ZkBrUtnX47Mdl1vTd5syeQX4-yD2R9sucRsqCLEq-dPm1nLg4QtNs_4cFJVZ4EgJal-u_qhMaEJuITDzVTWxf6ioudA6miRK2da35ifwqchoYhlcUbBfaDFbWuY-rRDbMtwCoSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBNe8E5lPk_VZ3dWsi05q45E2sp5n8ea_HthLr9vmWZfEQd1WtsY14Acan0axWvJGcfVJFWvG61Pc2GmPgE-f-XpgS3ta-uX5CkbodjNsf7zYMg4zIdil2Vh7f6ww6uWGGq4C-8bUcBOS-kAPtrxiOjc6Bg7Nfnfdhtl8FS63vWfD_2MJ5lNIQDK33BkRkZSLdpRbrQ0yPzvHslyWVPmjKTKEwZ6vUbFS4qxTcLmyu7Fsq05hR1NeeVhIVFJiOkTK2q8OlGFAEZ4ScTcQCmpf9VK212e1239oLe5zQc6bx113FW-l6Q8CQa1RKLCxIDTo_s5efmFjOqtRnoCY4AWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=vbJwYCxzGGfGsueE__bZ1Y6WPbRo0qdwXiICv6h0Vl1tD6AqQUOaK1egT5-MVf4JgW3hjOj2NiKOH3ieMbmS-CRBqCW2EfCj3ObJ_ZruY3zWLN8RZyfx_O4GPIVPqiWxGaYxpzZLpJb615GwfjC4D06bw_TwoABmw9Nl4ZzCKgMpr0qs55Ht5orfV51Ev7Qj9lSn-P2oFKcJ6Yk2rZHBRP7d5jffbbBAtXv4j6Gt9uhTmF2AQgty88XTMtCQ_6Aji4iM_JxVKILqt1eKPgXTIhSrqE-2M-PHY6UUSn4aCW6oZ35BXhIJD9ybY_zB747ejyaQ-tsR3T5_9tV80naqSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm_P9ZEBOMs9wKsN1vFbwxjRrLffWfgnbY_d-1sBmuBGYXJG00gneeHJmK99Qzx6pTm0b0rufodh8IDVzhfpv9aL5hiVhgggyn6OKEQ0lzpVG2L8kVayagwSdlR2bDyklojavxME0hQvz3MzuvIsm6Fv8ZqL8la_EbZtCAaeGhTbDx_VApuGJDXr3a-wWsCjiRIs1Ai3devRIezxuuLtn_ytdO0CKwy3WiHATF-09mqznW08ruPAiZbCDIjTWFEpJZIo8H4Lfkp_cVUCuXUCJvnGfUdjhWwHj8I3zbpLZivTJ71rCJM9oaCShZ7et0boA8ipN0wYmmQ2BsncXR38xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=EjBmTNFbvbrhub_X_2qk-GkWOwSnQDyOM-yp-eiDfpRnAUCt2LIRpsV9SLi3n7zq0P3H4uf2GhC3P8KsM9mHS5g458FtC7T0_8W-q_60f3YX0ZcM8PeXXGbdInLB1eK2NG6lZvVl3sFwKvAzq0A9BDBQM9RGjHjPQaGrz2L-FVY4bmhdge_E9YUGDXQ6sTDqJMc-cb_h0PphguUJ5E85TuAtgX-T3gyWsWLqH72GX0itrIK5gvhXgD9zG6m6dTGEO2jYG-YRewTDujymH-CslXmjz6VbV9Y1xeFgs8ITwaLUBC5hxfRBYnCV0UNogXEMqb8RGxvO0LLZaisOLABcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=Qg00_XwKwtUZ0pGuuw_1uM5q5zreHyt62k-6KIHUdR3lup5mQMz6rp5cSyIjKLnGYO8STlF2ulXi0kw4lX3_a2_1ThauxOtNQpIzh7W9h_sp6SdU_2svz5y_i5gCOQeX9QoRVkTZap9V67V6rAqda7b5SWV0dqNgRTuLj-X56V6LeTm9TjQrMyj-27mc_ZdS6aD3AVDrfbrvJbvAHr6e7mOco-p_Q5HneNsIsAavfY4uj8NHzUw4CtxR-9bomlw_wEEii4gbrCuXRIWDjZsXReMBfOawvI14VKKGwWcYojUp_P93sKyOW5t-6uO2RZOiVtupJQaf5FzetApo8OgpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umyzVG54i-5LNigzlP--Mi0JkBegA_rSl_05mi-9AEeoVTkHA8HDX9KwhVpHEkkyvO2DvE-qtzb84WRt55E5jIYHRrspYw9EkIyDGjvimaforiciKdjyavPKe5TNinkRqRJLEO2dhO72nNmGbwxNoY8iHzVlelsKOGB98rpsPLpmajfKPZUzZVUwc0Iew2GuHJxfhDDT50ud3pW8i21gWsnpzuHeOG5ebvNUeq7dCQS5x5RsslgBSIHu79nBQPgkyEr5o9z0KDIhCDghGspgRMCKgR824WxFDAUIKXjWYR_yDdDX1IiBfUE4zUOenrP8MfdRxIpwasUU2WIKYbUeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=eDAEZENAJoI-m_4ZH6_m-oE7O3_svBZ3jUAwK2Gmuc-RL91u5lbOn2Ks_XRrg4GsouoHQMpz47h6OrbjkF0LhSw1egjMgCtYJgseMYlxfIXtMQVA3f6GjLuAPOyxNJZ4T17JRheLQ9-3KAfQ2NXCT0JLT136j9C9yrpgHwkvsdid4ly2lIx3U0WXgszOjhjNyqhU24Lbcuo132NE8pM0hdxJfyRxYMo-rHijSZJ6EB5peGqDAzjz_79KOYZUe6_xEIuUHFvhwp-EyGB0ig9vIUwqcxuk5As5GI4dLrl1UgjrtLo2GyFyw9ZpoWCJbUW2OftN28s7gysQKvlqjdsYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=WZr0xp8SmadnlVuVYduf-xJuIO_0xqCOzhzbR1NUPBRXw63826Lj5N5gBDouwB-9h2Zh0z0V6f4KiYBsMdzTlI8t9V6GHWhCYtbLwC4ctrhG3ccVfw8AH-_b-yEz5DVyNihMgHxvar1U3aReTGnWErEJ_Mo2qa8qMEuvVxfJOrCs7GBJo92PKpn9e9Yx7OBwva_sEx3vDSMQzRAN-WUAitMe37_OUHNk2OVLZK09bAmj9jnKlsaK3z8k9uZOqpX4g5o7QQhMbROMG8pFl_u1TbyTnQFcUuLKhxkXQCYPngWwZ_tg3UYScHa5oyB-NGM1HahenkKeS26HJCU2j46dMCufqPqH3AQYRimFZQn2uxETfH5Mbg7fEUZunBb0evpRS7i_5At2FYgod65eEIe3hSy_sFe0ahz-OggAZwM9wjHncp7vdJyUyvfRs3kL4dRZyzFXBV_J-mgSFc0ObAK9PYjSqv-a5B84KbeK61xGJgi3Xn2VO2bi9kWwb3qSfsTomRicLTOQeYjOyjuIhgDbx2BFz368aDL5di3wNp516JM-KCbADiBrVawpucJrRDLiVMDdX5AvVCNwrXXcEzvKUZrFL3_u4jTeuR4iXXvR87cQOMTH59d0-4KoWox1_cHK4qpIVec91wvDzRAb91txl6zB_XBMQrZnRJyVPW-4KF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=an5uMYE6srWdSSmw6hXVxvltlwxuUi7L5RSz3Ig1PTKfz6hoNqCDCOezmm75nGRKlbKc5_dZ7PIQOtzIpQiP-Oop9QIuFWlYvU_sRd0yRZBLP7bN7YAwyOuZbdzrN0ecSPdOwlhpoEAvmw-j257fhicO1zLRR9FVw0FuleXkqMGihZXkGdek2e2J4NINYTOA-fVfVdTql-eViuqyyKEVse60-_nTPfiMbhZr302XknT3fvbum3WZ5F9Wjwf-La_AYhMVyPztgxSsOqlXO9x69xDWcBDf6LsGgQO5LIbUtokY0pnNP6KcNv9L6gVUTBtotyK0l3i5xEyLXc9-cyj9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5xj_OlUq-VRosgAvjlXLCt762bo0BHB-tlQJJkc-m8S0bULU6jtef7p_C-zyFQa0rfGf0GLcU2VYUBVYjbKG_ZyvDxucHlqmZpZX8w18mWk8RP_iL-IYHsRTugsNtvv7M0p1FuUoVzKqF-l9Kc67KZzziWps7eqoTzWikyHW-HwEx3vvvAf-k-X-vqGCoLzqHr7DO_DchD1bkyvIXM9VpR3lKFbddgop1XONGyWmdHb2CY2Ge7YjuCBSeW_--5RWauYqR19xpi-Fao3cT9JBeKMe1IMuPBnndu8tqOgKH0AEX7bpCuypYSALzzIh-VpO9VWietQK0OgyrL0aMa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiD-eUyVOekC-xXFf10UdCV5gIz3-l_Fx1Z9lXamR-g1FgjMXHMSd9Dx_clxbNFhLi1F0nGXOI1goXjGSFC2urHac_oaLuESpRkp_TyD9ywf-mQ145gi7_wYiwFLm6sLITe2gFMvmr7K0oJk2-5h1Y-mHIQKA9CbiUAJ43rE7uNcBUEAY3irPIAve7rqRYo7pOPexsZOmp_JcIkPJMZ4rizMbYs6RHC_MW7mrw2zEssP8TSeq4QQA65jdcLWh1JoSMPfk682XFEWT0BTRHs8EaFBToPvYT0AEmay6xXqU3U5MCVS5-cLuL1cNSVRSlz9eJ0tZWC4XtC5HkBL5GsHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=ZaZEYzh_-MUzWfUUw1K4-058GTbofNdKCT1D4pMTnuXmGBhHxGP9D6owyVTE5h2tSRvpNS3r7ECHLuNbJ6JUwKPbNyHVUaDNyiZ0qmWJpy7BJsVX8JhU8Krd7O0wUC7hiPkYwWkw5k_rDWNU5yg23wQNL0n1q_WcZXnsx-G7PyYz9qoFOOCXg_MvUlV6ba_NL9N7aZ7WHF_HyogWm2_y_4UEahV0I_WBDMTG-CmCE3TuV5B-KxRe5ompOkQLx_BikQ_OtG-bAprPfDCV7WB1fO1zs2jQdpRnPUGyh2BhqAgmP89WtrgiV_4rWdyi-PZPW0oh8GYkIJqISORGBc-xo1MdO3MWLo9_Fd1lsRM3ZUXAozHXmXeWipvFx-sEvhLMvOk0osut46P6DK_A8-zy77hr6QnKJwILKl4hNrjcmPLv1G0qgGCX6zzhjRoQf7RCiyS11PiBX_nAGhtCVRvazfSK1zLttRJRwVb3XFMaS4lbvkPUmv-O9WXTt0Jf45GTT7yoOn2zyytU6uSHsaTfMC4oKD34GUlrDFDQJpzHX2aGOjHd6LBGblAT5XzpyBCEYZ5vr2wG2Z0ZQgYPtOmQGE4eAxdqMqgFh62jKFtY9I0SkpKSIuFNeJpNQ1SsabtU1qg8YemRI7YKvsu9Y1rutbkpQBPfgJgs84hxrn3u_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClkTkrriDr2LNiXkVc2-acuHd3NVQuC7PXKOwNw1efC_Ahgmb20jJglxfN-57QIQzJCvqAyYejmbq4kbz85hDEcyCima_gl9E5wMpZIfaapN77o6Lp8i-hn7jOShvTmCuCs_euExkSWtc6Xp35yQMyx7xWtjcZ2oB3sCeNsPUCc490iW7BIKQkBZjmE7ESJjP4Mm3EmTiwWovYZZj0jlv96rzPHUB8Hpy1PwFDQzeuOhNd-HykSFMgK9q8zehGnK60vFERmBs4F6crZf9zrgHCkV0Tz2Y84LtoIDFJ72CMjWGUSyLgni2iqkMFL13F26ZCQggvGFMHEzzM0Y2k_apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZf7ji4P2elSKJ1k122n-MKoatVIuxprC9Q4ZtHeTx6YwbrEYjav_OKwxzAYsBVm0tqtAFr-UaVoYI5K_nYwCMFH9mOZiisAnbOwu3LOLpzBYDaJi3eHuTWQLDd9CICPySm8KuX2IJhOrzSXFsiWLN8kl7FFJE87R-Lvr9yR-eFBdNi0LQwPCxEWoshRwE8xb2pD8JjcbwfL-97t9sdmqoB7s6x_BM-2h6bVaLSCwsIzsFrT4FwoL-ZJEB5nJ1l3p0O8qf4gUxbPvrb88mnoCUPh3lV2bxrOzr0TPSWguwiLDmOCgXNe0kBfaA2E_mlnY9LrjAfT8vmVmr8QwEeZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMi0dRIBdto8lbnFO1uS1i1XM-53CMrTjlFftfYI01OeOiR9-i3_OTE6YxObH1ta6twoAm6WTwdltksBIrxtuvh0ehV7IPDGFNxqqZIlkQD69F8RIeK3Ksi6Vok4jzSa3S5ku0gXoSmIA4ClJpD2_Tad5OVvrotloKMo0Y-eISLpDsCvW5_9jtkoHkB5r_fOI_Y9vZ9NHEifZtrWkNMysxhV9x3G2H5CBQnUoCjMnt-1H8j9E3OgV75wg8YWO6sp9aw6yL9xyy4pzyfEg8OoqcFcvkWp8yuLmCtoSZ1idul54jIs1cNW6mmvAVicY-JDnnBhfZTYKJ9YSBNn88Z3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyOoveo_Ju7CFdcYUN6Lb_trva6yFar8WRg3V_hdnWHXegThlw4N1ohoRkkoSams-V9mGDQj-gJgwGi_yArEeWAIH25KQ0qEKJ1Xicx78heHpiAgsBDDMc0cfYLyUYFcLiMEnIXnMD9_Y8ep3uY4MxFsmSB7AfpyWG6a1r3SNTyAooAHq6qB5JE-Bhn_scr6_uK5LOO9qTlfuWevpSsk_mwS_f7oWfVZIBiuKDvQOWk69qsw6lf7BYVzRc7bG3b1tKn59dFdn2lVP_Rj1Mf_d6oXvrJGvO4vlqzC4ev_LfcUxfqIgZt4uhGs1Loz2mcahbc11GLf-QwxX582CYEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TS2eWv3ucHYmQKyjUxMGzdv7FknQG5NujEhUIhg5dnncwR3WRcaIwtuDu-wKkSp1u9ulslk-RqNRp1Rc_zbIHfZjv3H9V3hfHZrHfFG0SlqOltuELSla5VfUgl3n49oDaacZHIQw4ov07NdfClcBf9CTnck1Fx8HM3B6ZxuuQXX9C599NHYHoEHL0aFoOSCMploCHCXd6pzuhqr6aW41apisZgnzKUvkEcJsq8_j0Kzh_wRR5OVBynxTzcJyNfYf0YguQ7DrTTZdlgd5b9AG8F0-qgf-29osBvSv5BwqYS-8VIUcsAcgSd6KgGaV3Lpps3yy5uy48lfpuiUSvn0Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcWzRMG2s3sr0-zQE9dxEcv544LE4h0AjqX3Nxo7CyMRoMFTM_LrVQLR528MPRV19JWy9fKGK0hGvccugGjnuf7qpGLFHuCH--xVKVe8V8ReJjT1lSXpjz4UvJs7T8wQXKmAYl5RYnj80yOv3ETVFaE4Rj8F8qtXumgVqW_uykUNlJoRawRK5Vc1RhSTLuPew8UR-gjCOUzMjhdRJjCqIne4mLCmC83PFv1H0WdY-ZSN2o0jVQsIlyT_jqNwPvVZJ-mMyGbAW-HOpzzePKZ-FHJAekNiv11g7kSbJ57KwjN6F23Z-aUtyJXXMtgUAHkMomddCcyOnJxuOr_NtONfqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=oFZavncXY-OB5Vssk2Zu8581kS_dS_hFS89LzkL-FvcZWXpPB1DVRkOk7bGEuoOXQZeNDThixHYjyrrXyGlRd2F30mC3PeBJxSivecPHmAkCFyIer0prqv2wVHo1dn8TA8tInQRmLTywpGt2Lpb-QqwPrSweOgQyFGh4DgravxnIU3PRVy7AZzu5l7Rfv0k20DKA3NDjN5HsoRa_iuGNSFCwtU8QyDaBFJRAAtPBOEcyzitL0w05J1-ydmy2spM9z0Fga9waHijFKIaHYrTgVtr3ggFZM1RlET2DoLyyWt3t6drCXLeUyS7gQG0fddl3BNN2Z0LKLp4KfeGGLluGVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=oFZavncXY-OB5Vssk2Zu8581kS_dS_hFS89LzkL-FvcZWXpPB1DVRkOk7bGEuoOXQZeNDThixHYjyrrXyGlRd2F30mC3PeBJxSivecPHmAkCFyIer0prqv2wVHo1dn8TA8tInQRmLTywpGt2Lpb-QqwPrSweOgQyFGh4DgravxnIU3PRVy7AZzu5l7Rfv0k20DKA3NDjN5HsoRa_iuGNSFCwtU8QyDaBFJRAAtPBOEcyzitL0w05J1-ydmy2spM9z0Fga9waHijFKIaHYrTgVtr3ggFZM1RlET2DoLyyWt3t6drCXLeUyS7gQG0fddl3BNN2Z0LKLp4KfeGGLluGVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=hDqTjUR99efC1ggJn1MnzfypjhRNhrjxgLgD47lxhJKdI6sOgS7wceSioMoVURUpjsOtgY60v3KosnwegCw3tFOO6P5l1l-vQX7U-IJSLS64LRpqKKNqqtWr4vqBuBUu9-bQ7CjZcYyPdGY5dJuRasOM7hk8mZEOxGuBrmCvbVJogQLzV8QkIIdzv09v4YIzB-gkQrLNTT7hGOikFO-JKIUjBrZ-rmJYZ1654luj8gJZ3iRQHeiRnpDVv5q2jAAEu45_jJjY00fX5ZQ1rcv7Gwwf9lDuQKMuf6_pBBy7C36t2DAYIYv6j7WeWRp7f8XuXSHuDM_m_Xn0LUjwypeRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=hDqTjUR99efC1ggJn1MnzfypjhRNhrjxgLgD47lxhJKdI6sOgS7wceSioMoVURUpjsOtgY60v3KosnwegCw3tFOO6P5l1l-vQX7U-IJSLS64LRpqKKNqqtWr4vqBuBUu9-bQ7CjZcYyPdGY5dJuRasOM7hk8mZEOxGuBrmCvbVJogQLzV8QkIIdzv09v4YIzB-gkQrLNTT7hGOikFO-JKIUjBrZ-rmJYZ1654luj8gJZ3iRQHeiRnpDVv5q2jAAEu45_jJjY00fX5ZQ1rcv7Gwwf9lDuQKMuf6_pBBy7C36t2DAYIYv6j7WeWRp7f8XuXSHuDM_m_Xn0LUjwypeRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=LN2VSiXF8lOIKoB4C1B2bBvq5fURk9jboUh-pEKxq8E1JBrXbl4sA93D-fFE-AY43UGY1fGCH8sdllt4VdZsaSRhtSIHhr2XkQpIMFwwWVA8tOVpV1EsFeWV9-EghoBk8aaRfG9FgYIytZrd-Ckc3qFUqBIK3Dr7rZR0--18YrwuGh-iqDcL6DVn3FR492-dOi6_i5Z9K5IZTLCPdRLLLYEfJq96_PFiH9fINKEmMwQVm0lRsIQkQLvZwCDPgdZ5Sc1Sdc5uxRXZKyzeU02Ct91KFoBRxrtZgfScDePX-XAdzmk0BYMSOsAfjr7Q5h3K5bg0MqguWwaGxaGjSARwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=LN2VSiXF8lOIKoB4C1B2bBvq5fURk9jboUh-pEKxq8E1JBrXbl4sA93D-fFE-AY43UGY1fGCH8sdllt4VdZsaSRhtSIHhr2XkQpIMFwwWVA8tOVpV1EsFeWV9-EghoBk8aaRfG9FgYIytZrd-Ckc3qFUqBIK3Dr7rZR0--18YrwuGh-iqDcL6DVn3FR492-dOi6_i5Z9K5IZTLCPdRLLLYEfJq96_PFiH9fINKEmMwQVm0lRsIQkQLvZwCDPgdZ5Sc1Sdc5uxRXZKyzeU02Ct91KFoBRxrtZgfScDePX-XAdzmk0BYMSOsAfjr7Q5h3K5bg0MqguWwaGxaGjSARwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLOKZfubDv5nQu519bmeYb2Pni75PZqtbHeLHegDBLXRaml0-yjHfeQKgpzxn9zw6W9l8vX7yJzKhjgxKLvFJziXC9D_lvPBGb4F0o_hdMiZk_Ihr5i6DE0evmj5I-sIXT2DgO2iIWSIBnWcF6mA6BpK9LPCqN3Y04TMpChYbTCsxMTkNAa8kUskDxnzDVAUaPnMmzP-GN2c_6blCiN5JlR09BPrOIt191BVgY0258kUyfHfD-a-o4c8sSWtZazRGyLqNw41AQLdMCdXW-iFQySli6AtxUECC7n39GXNpSO9pZ1xSJhJBgPLBJPVI7K8IPQ49FD1RFqQXAeaqFpJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=WGsqiBPF8U7lfqaIr2EU8tTS05dQ4DYJW53ahs71R6DrKYPt-CS8M_-9rapax7BspYcU6ylk8ZC8xIFpsy243a2G2B2F0DyVdTBRmM-xrgFD0C9Y-vSuHLU0JBsVpu4QerQAJc_mGQIHE9kiaB5XD3ZtbJzUVbhGyaB8-d4Kl1PTcOaY9IZ2AKuIi0j5YZFbPID7y91Sxvgmnmjkv7ta-uG6Zfwc4VzKJglDm717WgNCt9xuCRJ-pNdZ7QuAkk2tZ30SJTRNbtxUOA73tSt5BYU5UFJmDR3l0GZR9aBRNEAATTUIdS_kgBBIY0EGwzKIvrV3LTgS15L018zAJDuFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=WGsqiBPF8U7lfqaIr2EU8tTS05dQ4DYJW53ahs71R6DrKYPt-CS8M_-9rapax7BspYcU6ylk8ZC8xIFpsy243a2G2B2F0DyVdTBRmM-xrgFD0C9Y-vSuHLU0JBsVpu4QerQAJc_mGQIHE9kiaB5XD3ZtbJzUVbhGyaB8-d4Kl1PTcOaY9IZ2AKuIi0j5YZFbPID7y91Sxvgmnmjkv7ta-uG6Zfwc4VzKJglDm717WgNCt9xuCRJ-pNdZ7QuAkk2tZ30SJTRNbtxUOA73tSt5BYU5UFJmDR3l0GZR9aBRNEAATTUIdS_kgBBIY0EGwzKIvrV3LTgS15L018zAJDuFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEeWbrvaGZbj_CuwW1ap5wyrJYZluDc-jGDXVjOjZqoloV_DO2PslexGetk4xno7OwThx2YHN8U6_IMkDcXfuwWnS6hOyOUkoxImMuM262EOSZPE69Oyesvti12ydgp83Hng3QNPZzibgG1Kab23Si4aeveyxIwliFxL5D5qqDbI9WxHbco0pH__vzGOUF4IRz7AXG1OEuqe_GTApwfdDh2pIXzqERExHVXVkf2IAO_dkFzfdpHavXhMXkBLICauZXGAXrONt8b6mhEjRrfEG4ntzgLeFOVvY2quhqTgcYL0H8q6i0NoCkqzDkKok0JbalrvSD-INeTaW4eTLX02Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=Mq2nkF5mzWguvrwv69HkU8VU8alkcqMDloYnLlvCPHmrb73CmQXNUBfEW7xYioSkHlwFaL2wm_87RxsbrgKgtxzjW8k5mJWGmbiZLMUsn0S3y-FGtMHfEc0aWkC0atYAk22THXhCOZgv7sgMsFW1ZAZfXfxMhcFDnEfc7a4Og-wgw5TUqu7Kw-HxW0Xw_mhN65bzIwuc2L2m1JbzHs0WzyhTDo5-6ht9HQFf8cEiCYY9F3fwdX-Qp1X5vww5eYjtN7hiw1MW1MQBv5aMwreP1ujsruvdAGDP_BCokJlCsQI6jqd2pq58JZ6Ti-4Rnbku4H_nORWjRdNmiVQf6KBYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=Mq2nkF5mzWguvrwv69HkU8VU8alkcqMDloYnLlvCPHmrb73CmQXNUBfEW7xYioSkHlwFaL2wm_87RxsbrgKgtxzjW8k5mJWGmbiZLMUsn0S3y-FGtMHfEc0aWkC0atYAk22THXhCOZgv7sgMsFW1ZAZfXfxMhcFDnEfc7a4Og-wgw5TUqu7Kw-HxW0Xw_mhN65bzIwuc2L2m1JbzHs0WzyhTDo5-6ht9HQFf8cEiCYY9F3fwdX-Qp1X5vww5eYjtN7hiw1MW1MQBv5aMwreP1ujsruvdAGDP_BCokJlCsQI6jqd2pq58JZ6Ti-4Rnbku4H_nORWjRdNmiVQf6KBYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpvWtqC5p-wZn91GKiQW_oDlGA-j0I_d1VyVCamFM9J6B6QSBDh1Bq9Au7CW7fdHn8yGhIUQQwcAZDdy-0M_mfYuaRxjQYDetHevPAwg__5JchxKYdrnef8-9cYeu1tgxaY3q2QzHnI7IOtUMsaDich-juUOV_9W6ihcZ7UREADttK3o4KRF6s6kDkrSn5XMhoH5qHWCL1K3oZxcDiz6PM_PAyvR3U6RGD4YFKMjPYbvq1PYO-VYXIxLjN9ChMA0goketi83FA2_UtaOOLjbab75crTcNkOIfcojFWPFcJlfWn3FqKRGyBrSXFj6y-W2nk7u_gWKmi1DpGlbS5nizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S43ceedUl4mmZMdSCfp6L7IIptj1ZO2tILkci_B8iSJj0donFCa5POauOnTHp5EVDZCVOMY433sxYyu6aAfjWvfrRYnDrmLSHV-WskwujdBtHthyi60SG3L_34ySSFOOelkg_AuIyh4lb_ZLCGgyGsPJnAEgDMRfWGzj0jaApfDUsI5tkdHYrSkjcQ8TImsthIA_C_KL_XOYEFoPPIWJom1d3t0i8oB50a0StWmQNoJLFt__B0Tv1WZkRXQWhUojG9yKbW3abqirvvcUW-lI6_91jx_OM8Xhb1k8X-0XVqJkqpR9IWaj3mjWx02M5WHytphXiQ8HRB_9FxQ_gi49LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtiZAGnL-rPYxBdOq9DeT3mtdF_EmXekPte-udN574_lG2Z5x7a-8Wuyb_-8y87o8blSsZB_ZDQit6p1sSSEJ6fm8lwQbOm6gjdenuFP1SungesjWh0EWJgby6Ammphf4H3RmTsRkJqNP6uvRVxwUkba4sdbFh3IBDK4cli6WzTQ7oKlUdsQHLC2OjYYUKrElRSuiMhGhO2ABlPrnAG8zWBLlOIw_4pcdoVTNUsAToJ8gwZFvPOJ4dYYORdGwsbhQFEccL6mipOBxsC5vdekJ6uDxHDyUdgklPI90o9xjPOHpUbE84oPzRMl7GqVyvFAgaHUFhC02NlDl-tG06EcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkHJfdIROWYX9wIgGF6iuV1t17otyBkrKpP-duXiOpP7ckws5nQpBpQUffC427l4pDRn6psZYNkL64ffxQxmMRMpd8-UKjVYvyxWC575CEuFe_9xJCsQyxpBp-Vzoq0ysWhuxgbcaqLnTEERS5Qb0J9vPonR0aq8iu7l3YVidDggduRSWROXxpXE7kPqdwaf8qAtXp7YoTGQB0j4dlbl9esPnOHGQTW24WB8ipKZjV4al17OM74ghyM8XziyTIWVUj7YzudUqu9H5hNeuqCDUe3-GAgxEIpBxjaYiRU-t2hBjgs-dKDKq2Sjjqpf6lLAn4akdVsEWQq62Osmx2xOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6nn1-QPX3mcqeJU_VYYM6PB3DfHMBgn-TrOmuIEVbuq403I7OqDV6hLU_Jr7vS_sxiwIfIg1c5pfCzpHzP4wnHtqVwuDme8bP2j7ddMM4LuxC9-xoC4LHg3zZ1nBnJc5Df_K741MuUwH74a2edO1_0ADDk0k6hK8vzs0n-ZbivY--ByRfjAG7MjLWZRODfCJ5ViPLVi_sveWfmbgq0xB44Ok9KDSeLFxJPV5o72dKifW78tBqKAQ8UcoAzR5xdFA1Q16G2eIXhMGkIrcUaeB-fkmEm-0nfgqLUgzoMbNuU7tqSfbAbZ11fQ_LreH6iEhugql_TYUeX42DdDjDE09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QiGCxtcCywiv6GPYBhf7iJYK7UZe6CVAXiS6N2ddCm9MwsgpOn_-dp3370fBdsGjeIHvnrP2ozG-hq5n3cAvJMFzHO6Zp4LX2cRIj3JiuYLIiASZyE7v6f8VWEaUvXYHI_o0D7szO35VJjwO96GH5yBcOzgjorDi5FuSFUHTRTPD-WgUTIf7Oi93pIxP6afpKRLihvAkhsJUn7can_3p2ZQzsB-9Q2olrGjqHrg1xkHazYt0-oO4dNp3uZZLmFNZ8Gr6lD16eNR8Of0ICWadUQzYj_lO5xhSa29GjHSouCG58crwOD2OIONJwnBfhHYQ6a3gflCp0h8N3r68Bjrfnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0JCkD4lJ541GKa05JKdUI22j25EQRgRN1sI8CUp0C75P8aN3bc7PqdKN-bF8oa7B-ZNk-0zPSkeND7tlhE0Ll2Nlt86SKAhxkmiJgxTg8hkluffsftnLQqN3N3AvT9zR4svKOkmy66n437PP7cRsEITL_pkcSfsz7ekqDb4BZID_U4YN315cJHV-egxya3qIWjAlO75FjTVFbZcESTvrJZTWT1n4vodvJjH84i49R1agCe-zHIWF6YEWQs9mjZihMyH2NcMWH3u3LK-sliBmW5qCaOUpQ3hepqccsEDZgiYc-MeDbU0UHA5YOa6RqzBapLY8daOoEY_ZqULdZwWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TilnzZhBzEdqymJ9cdnQLmNAN6Ys9V0Wrzc0F2SG9sp7JhYI11TF8yLNrHRd3RUr2sQLr4itp632dxBpHol_I2ciskYSvot-wby1mqbUNefp3_Oz4ld27TBWD_fafPHOtcA3PRLQVvoPHyMcdVohyl2kvzCidxNkvNugvcO6ZHb9cLlimdHbJ39ff8d73-05i3vs1sXpYBV86TXw4ByeCeZFda_e27hqtPGdc3yHVn-amcQtw7pbY-lzLD7oYHzEXAs7u5llTXbuwlVkzQLehfIwKaeqvkSxkxqQHSQERlzuvcuHZ_2sk94tRy4S13mqBG9x_2FysoG59MvwaA0jsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwkqevbxBp5O0NU-1BMzWCapJkOGqbRmBRsZWkx35su1EygN06vDDl_HijBhtn7JFzatZoemh37dNQ3Y4EGZOUMVkk8VA3oyja4yy_H1-N9QHeUhYIntOBUZ050Fmgxx1u4Bqndk2Y-Ot-XrTILN7efXBZ_-FStOVa8UfS9tGgHqTjTkKkovym_ZDQjjKEGsLCmyuXZU-tkKBRH9rW84knxjTC6tXHLQxYq9dMKVnRRR3i2B3U522kKcxTBEhGhhOrisgNCWWxAsy37zX8bVDeq4ry6pyZdkG83h6N0WBlW_UjUABjsK6OUYzHGTJ0LdJY3Gb5X7CYRiTW2V6Ry4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5SqU63z-RAJRWWECAeg3PAHefXQEnO1YKZJale7ubJ-hHyRGfKdhp_MKonz3Wqj4Xp_I-oD2AA6UwHqD4-i8OFt4dgmInYJClb6tSuFBoI81YvJQI9zqSMeazYMrL-rJY-_f_BM7amjIVDllz6mgDmEvAqUQA8xP819CsbkYykVa71_hXaC-Gcic8EfiT5UZRIgbzPSbqIx0DbE86bGLqcsINe7RiYmQgiA3Dj2llB_0mB-btIHGaUTXZ4YzW2zBaJy_dF9i1SrgBgCyPzuu5I-AQEbgOGzZJZtSzoBngGB4qt21b3ipUzmK9B3ZaLh-OM08PZ2PZ2OC-g1D-8VWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQqr0E7LFgMThno9vvKw-LnOajec_nv_cC8UuSOqrtloNDvRL9FNXtobw4G66FVmg_GMn9bh4kD9u7yAvOWSeN_KX82r79g5CXkO8iT8ABlrFjBhT_5ebbJvgQzwKqHa0L7V3gJ4WD_OhGgWarihBF2ClvneRT2bAtKJGyI7NatOhTlAEbVp2lstnbDfqB2nFByviJqJi8oZXky_28IyzBlfMDSDv0wVlOshOh1gOPRDXA-3yo4A08QUAn1irqEA5Q3xDVGVyH9WCUFT1zXlnpN_oXIU5xmKTn3ja2SS67Ni1uYFoEExX7u0s7sxoqjVMAqIgStIcuZP9w3_e7RDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_PEwYlb3QNAu0SdMZTgJ5InXTFkQcCG_MkHTjo6BEmeG378OyqOYEGaqxzZ7v1Jbksmb_F51-zDsJi7VRAKCStTC4rcHLBM_dIoMtmxDSdWmkFkTFXjlykD6nsKPDJ9OjWsxg4AX1v9WWJT-z4AE8BEuvBKIMg-mncYY9aEHrnVlGZEl5LT8Syg6-rKVA18Ur-oOugtZ69YqpLyjsI9OB5pNCP9P2iTORis4h59Yp-eoQoARAJJW24qAu9HpQWwkEl53ky-nRq3RutUMdnLn4gVoM99hWpuEPNvlVFZkXhgzULMUZahIWx7BX2MsKXhHcgMnQlInU_XsXj6uUftqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4oDnyfnAtldugEgXWxGvp41DsFoxwuPvqZFlqxGMT7uUKNhnU3iJtGo4m8SWGzm5EqOfeIIGwkh23LtZ2AyA_fuCA7skubyo8iDxSpn_R6iThu49wodSTAXpvDj_eoAvUMMq856QDZn82tsBBexWsKYlnrlbsU5DXMRPCpRUOIBaph919G1-bfiyQhVob64y0aV8yQFV7nPHykljzEtB743AX8zxiaGp8tkTyfBeIul2-nvInE1Lus1G8uLE07m52lo_2aefT_kwn9XkJSE7y57CYbJ8ivrbo8x6uGmdQRD8we7i8kUgF5BCUXTpfRsy9i44or7svf4f62VnZVFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMSoX1Nawkw8ZOdanAi28Aj0FXbDgotsvxAhQ1KjGuR-iAIzSYp-bajXsbqupLKIfDM40ZP8ZbpmQfV9COGqAjJ1FUEylTMH5f8uN39H-hgb1iillqh9-mm__71FJccZa0VU7_pWOPuNp12dwZ_Pd-COzJ8RzBBZe-N_dQtDnQ_B1fz5faH71DgrH00qE8pt6NzCpR93R4dPvKWjDQXOLz96xe6s_GrvuVqVzqzicHWm8hqSSirwrtQcl06MRxb-MqFC56AhicV0rOXL53RJa-LzOTcNvdU9C90-Lwrb6T2QBbCQTiwWQZZByrUhTdsxqicbtA1o7W5_0a_NKVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhLoPX-LhR1R-eMdP9o6h5vXiWWzHAl6M5rG-_rJTldypHyZDOybDGUY04eATLL-juWmI7_adWtHNfFqvMPvKBgj9SToBCN6Wc4BLoQJSPxalaLEfZ9iT3Va2LJwAjBFf42PzD1MZ3FpEO8Zv6zQMiCJMbNuav6ElM2Yb716QBIXvpWTNYZSy_6zwY2tHmhBdaCco84RwXv5k-aQ_i96gtivz04aEFVQRWRygFFaKNkc7ZuuGqqqycVyGmWIwMaMET9Cl0L2oeQeiZSaG0egASnFkLigYBixfmRgQBQY6D7Qg8NGA4GYs2KKgnMgPkZjau-XwFjCDwoIPiKqIV4uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcTqpqYNqFdk-EPwJ-pBovk9HKL2LYc62_LETYboKiHLRRfKrPh6P7_QcfVLenPLbC28Pyan3T_C-m32EgOEoh-XUJNNUnQRFvuCwt35A3wPdn6h5xV84B4FFziiwj92NCyowzxDTTrVOb60Qgsumw8lyqjThTlVDgPCoBxyoxJ2bOGOfxy23DjnmuRMrYI57XkyjXvYlAZWa2zk_LzzD1liZNnGhoFo3zY15rTS5aXGjmCHHRxttQYfXZFBiWreShvAeWlQMhYlpRRKgATjfh5mzR6xnYRFnkEHAbbA67gQKgpHFoG_XjJRy6vkKuIpCunHf0VQR0fmE-iatJXlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adUg3mu1CS0LhnbDuu_ylueORCAvRZ91Lfn-L2oBfOzmAa__Xrn-3VeqS7CbcMiXJd9GgVklK8E2CLBbbJPR5-wCWTcceD7nigoDXkpS3QQPGA7U2AOWNSorI2Z4DewLmRvtscW3XJZAUdxtK-aO3ygT4JtCNeNaQB5sigS_DGRb1GeVT1gI25wdIOha7mqpwu47XXubxA4dGWDAzn79EBjIVHRYZi9Gu91ubhX3TfHvIrhKs7OOaMnuCFiwTVbgK96JZt6yBLEJ8Pl5Uc9uyAsQ9Yt9VSq0J_WV75PSo71B5vRvcweaqzDTvNRT7NMwR0z02Yt6G4Ujnlf3EWua4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLYCoUxM4CZl1PekRONdvbHT7S9yC2ZBp3Lc5_kFupxFmz0Geez6YbMRl488Y-VBxmduMOUOpUUBB3CNTFv2y9cMsbM1CLx6LJNsCPWKPkH-Yo074H1dTmKqYfkrnhcX8bPhWF0mCoItVi0WNBwn4taBbtgcAqk2KeTq1f02lfz3gT5g2KGnZjKlOQXahoD7ksW36wK8pVYKTS6di0aWxka2OJG5Rh_UzHz-0fSDZ_uhGMecXO7lTDHS6w4BKRc4FGItoYheXtb-HO8c6HnGZS1tOJWwDstMbTaVVK2mnUXFYLhCJEB31rTKmWj5AR6xhY9otH6Ar1RV_9up__1Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yz3UWgd2FqXshZKiOhNMvGEmCkTSFSVP5nDrYJ_N_oRqBdG1DigRS4b4pzJ0z0yAgzV_cVe3OBx1dniURjwWmD_3kj46GveZeZ52nfH3spg3e6GHeX4zAi_Vw3Q3Vt8hYtoiO-ajEVGJGq7rNYmCyb4gB9Vike5wAOCnAY4pg5cQq-u31s3YYDMubaQxcvqtMoQ-4u5sPaVBoz97RjT5AuvUaYQ9M7Nl_B2PAhOMiQA6Kko90uzP-pPDtRqrpMH9S4a0lwvKCeo72n1F-FspAv2UlGaLGHLxBk_ai_338sGDCIhmzd7u3QrR_qEMQWMnxBWs7yksK6FbsHJZSB4a_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUq1lIDKGWvfho9JIN2Uui3xA2RiZdtiLfqhifOuFa_6YLSUI4fujCvcLLGqe9BRxS6p8bx68C-DIoc-Id00YMEtJqZNJKgO_SZNOoih5aTR0HkGIlpzxW1am-C3y_LsXejj6uMzEP35knjG5DdoK0as-EIVnPFek1B9Rfa7lUI4NxarJ6ivxNvpgrW55E0aeEmc-cCzbuEvJyUF3L0jtcq9h3W_espH9qNNUnzJMM5h3G8C1ewHv74fr7V8B7_RbyYxA8bB_fmmDY_JOOESTwjFYjc3uP_j_6F4oVNHc20AoqrT9dyWjToqUYjgoRAk-MrboSL9g6iCXluXlpYWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlVeBk9OoShHV9dpJTR8nIrOXKMck690KfdGrRdVylGCN_15QJ9fOHbCiw3viiGs26dyvYbUILL76O4QzM4GQv_FI0XsTT9z9WtSxhKhMyMdTwKbqU8UpV0cr9nKwQgkHW8rVORm_A02Lpw6KJlgXW6kOyGhbVv40w8ZO7oYzea6uLJLNoP-YYZP7X1l0QEOgjbSsi9vD0C44LvjBZaBBxekJh2Hk08kOn9vC3jVBTyi7hrOyNolHrZWJGddc6vGapfl565pRDwMngOjCtvdH7h2X1fAcjJSxlFdwEoKbrnoSzey2zGukwDsnVo_jj0tHhPf-NRwCT_GvHQoI23sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb5Z_b5mZQXbIkywL9ySKICXQlMjLfrOyNBIQ6VFMkha4xRoqGnGLqWLb3PceibBE1k3qD2NWDoDel8R4LlN6wizbMRtbf7KkXNDVL-YgKMgi0iI1wd8PuXREzDV791o-95kOvrHRUd4YeLiY9SbGPQZ9tCb6MyBFGbclpKARMd3CQpDwyeyFhPT0EK1v7Sg8rIsQr0oIMzO3aBVn85OJcTR7dSjatu32uWc9aEAKgPJxG-0LXmrfhZ7szXuJmYD2agxtkSQ0O1exZUCZmNiixXHnaU-_lnYi0pZHoAkG_XMLpka676JiSXEINdmNYJ7fhCwNpYaK_3JiZNI2LhQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeuuyrEeDaLXZl0MxGxIkkUabb8h1KtEv2cqD-7jWkfjE2vP8WUwsx53svVtya2xICXH9zu7utNRRMv4H4fZlWpSdxNaT8DNMsRNqfD4y1WYWsqxTmSvkVYUvwg1qLaasFdidvY0AKFj7LRYeG4VhUx1oHjK5FwAgDvjP6CIbc8iN1EFVC0W0W08HA4sSXhwQCosxCotNIpHcvLx-V2-NCrqicgkPYw5oGxd-KFsZlTOgcuHhrm9uYwaGgBZ5ufOAICQA1z6b8qvt3eWM3ThdrCk3s_J_CcYHX_ZdtQHfCgQZ3RdskCbHTNGEdviDD0NC5grpQnYLrqytpA8lTST5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXKIgc-n8LqSpoFT8-U9AM4KFZdrixnWyAZWjki4dAYKeyKXucWH2QU62FKo7GjcvEaEDf708WlpEzE8_WOT1RpohbzefKySf8ZRLoPGYK-y0o1deHDWmEs30dWIQypkIs6hvJl4feoRSF7XfdOGUib7Pl3BI2K_2cqTd0UAgR1Mnev-P0XLLlAp4UFjU67S7ZtfjdNkvO0sBVvWzrpZhBKl8VDGZlotIJziPT4n9j40HmrBAJFX8083TQ86Ycy5U8YLphKgUe8C7vIOQ48PuZeiSl6Uo94e8f83Bpt72oaGDmzGcMxOK9MDLXjxSaHts5aA7fAmvLAdSCVjzDgsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4CF3Ggk4cA9AI6UNpjLoH9F9y69OQEAiK7ojKhxxR1rpjX62qArtApviWp0B745T0apayI3tUfXnIQTV4aLUy1KJSuGO0gvspwNr15ETCbYKhnpZRjziMqvH3_e3pA74U-vRUbxjOffrsD-51Eg045dAI87g7hrx4ge8mYspMu-ZfoHNEjGT7Bu9AqAPY5raHin_xhvWqFyEoOXiPAZjBrEjQJCGmiTjqkjsVccOxyh0Jezia7L_2ajg-3R0Yyj3fMdZkxZUG8puhCI0rlGo4J_cLqKX0k0iTVus7urPXZhzUZSiftcQumEzX0nMTRwqSmP61Kp-zAG6NY3reZ13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxRqIyIyr2SqB3zjsD_CRwlK_ba01dMZEvEhL3wjgiAx0NZiTVNp9ij4CpYehKbfrtzmbt1JFBrEOr3XqQmQC4klZL0v7Pg7dUti7_SaDJQZQKhcqhFV3z84xC_1T1YnzH6kJ2c_rUKTaxCuiLjXnMdYzw4Ic4EKjNk09S7N0Hx3xh2qzI0RnEemxwRpb3-Ic4vUuNqU3T2iWjVkesGHXQdfXXeNTJF1UD0XIASdPdEjaq8md1LLFweCquwx36dvg2LGldAPuA7U141T9uR5sDO4C8W6zSY9eLjv3EnFXn34SlZ6PVEx-5oIbIlOvBkofc33MJsHD76TpgNRwf3rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZwF63trvINWFwtoYjq6fKVJr5rwDYuyGgnCjpuRSnYT0gOo5PNIz6138Q_sDeuVfuDvR0NPzO4CO5-VY03liXDaab372UK0d_sc-W4YQLsvRjBpwZAzsOIc-dLr65_Jfe6UfgwblV1Bw4PgS2c_oQm7uXXxV4iKMM31dmlecPgzFLtIJ9xIGFx8nuy6IqvSbsZrWC1J5aSwvKnjXygKb0Mf0szyQbbvLF_YAL-WY3nQyIDkpBA_a2NkHhxdfsYOPMimeJ45EyeceJPLawchcAJIxEgxGT0ySLdpdadvE7GAx2aZHC1WAuTWDd4BVZSp3GfZSvo86bXKUsP5QsG1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5l2ku-yq7fIKnbEZJawpqkVOVfdgENTxGn2uAW8CmmCcy-ZWLInRnSG4jiTmtYxkNYkBLPPU7cLQf4Pffo0E77KrV__czWbXLtIksSGp4aZ-1u7crrb84LXniv5K8IvsRROPRVgGFbKIUqD8uRQaxL3li-jsPp3Gdzpy4gy906AVvWyzrxcpqmj5_FkaGnISlInZL_HTiHrF20gs1f1ndl7H4JE5mkrSUxxVKE9TTLelW9NkIXIXAP-A1CIbje8_jE7c0saFILZb0pLuD8wP-6l8hEdzMncp94D9E7SGwvV9-OuZh0ZBMHY-6OaLt5-h077pOVp_YRXs7Btk1JwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ea7YHQagoX2-gXdsidighS66qtzwqgSQuvu52JTQg2DOGc9hoAufxiCYPHazbLV6G0kaxB7waMNyg0_RV06XuOcMenpZrlsN8-UuEd4rEUNq3QJcn0UVeWjKHhJr3gQD9SBW8xSbcoVcVNdqieSV9IrN-vTNqZ9PlDBCFWVFL1RSeTn-dtT0Y2UAYO8oamHkUVtsxZ-gZGnyaZCwqB8_WvFXt-BATv3qeDVb_CxVhEUjPJQf6BsgVhXUVeyFlJeDqCk7AMauYl1WOqJXB9JQtr2Ncd2rdhl5ReuA8M3Mom4GaIYh2i1GWAqdTS44d3tpJAfuxpFIq3z7V3H2qunTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MISSyoI_GoMlcc1J_6TdE2RTXyA_06VIuVGU25vMOzes3VU07CyJN-utgLTK4gHm1MM4WQHY8Ojc4oFHEGVI14PYvzIRU2wTPjwazHYJoV3aVrn3WR2lj6l_XeVW5M-E0WI31xor5SdDntRv0RXcxRujoc9Fv5bZDjruHflwvXzpOsVZcgornaXemfZPH0rfV4b6_L7loOdm7z0AMsrHMCrN2Fe-dF0XVP58EfNpTgbckg9E9Zpzws4s7ZnOSHqdveLCB7u-JXgm2yEhf9PRE6JGYPL_ZM6HDzhWtvXcbfEsPqAWomJZMNkY04Ba2fVP-ZVtPKPSiVfQ-R0ZCl9Jeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdNMui8wydSiya7UtEJjAjOITeCMKjSAkpOAyTM45hOu0EIJdv4q9RE--7n8goiDexAaOBoPnKnfiy8yUxzzErjzHmPQsLV_H6pbG93uOo2zm2y5BKfIZ7wYcHBOkqcszWQxnW0vSr6u1sUOy_WRHc7eepM318nhfqqv4KBEQLr0UmHvhsMjULdd2dgffdzqJLPY6S9T5dHpoAdxeK4lEn0t5DGxfdalsU5qLo0tEHXfXhs99r7Pm_IcYvlvqa88f_kFgBiy9zWnqDqCCnJO8T_DBh-kdLZi2XmaP84CKoBTodOJV7EbG_vcnm5OBM4z0nQp7xulKkWDOV8geLCitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfoxI7P21drUnsObr3ZJivjvDGsETuax01P2TELMtNQ0A36voNdY2PSkivYEnvWP1rkFVFj0EtcaEEqqCT9rQ5CgP3Jhe94JgtCW5pBTHLRBuCyaIZGu3iHGnJ-MjTNSk85ZDGVFpPmeqp525X8nIa1h576zlwnLYvavCUaLwIjpyu4VmfXWMVCRjfG5YcsrhxzUBBTlibw58TCHga6e85HtgiGmPkLEn-0K6Z4BB9-lFlad1pbNSTkqTE3vOEshMT9zfU7qRWz0soLph_3yas03-U0OsThaXI2x7IAGV1PcnGKYDybFs7Yx6C-mg3-RhRZS6rsNkEsjeTexNGDhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3KerUiJwTfDsSJo_yxebwKqEUAEkrzNUjotdCABxZIkwj0PJb-YAzBbf6qQy8o87p_NrVRHF88iaiRuLo7clP5uah9UeJJfVpDfmpJ9Twmm-t7fJGmwDmlemFy3-dx_gSsHR5FhzjwuXryRVj93gJn10_0NERr5xY_L51EXmG13H53BfCLCm05U0omLExeJT_VeT1Oxc3rsnCNN-UHWAihheAk0NHBs0D33InkbO12x0gG7W0YSl5RW2dl6nXtmZ8oHEZSOdvfnygTvZ1XuHbRxYVOk_FgFDaM2jJmIvd6rAQ3asgqh0ySgeRCEaMILTXYs8_Oi-cqSps_whyj8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB1fAwfAslv3XBjt39AXV2KxiUm7yjn4hQI_JhmhlvrMT9oJnDeMdtRyRuL_Mdefpojaf4D9hhc4XW0VuTK_v6DQIKyBGsxPNtBkKc8103sEqPPFvIFv622Wn2p_xEaW2V93qU2fBjkTFeOGxlFmvZPLkKoMf0bWWsxzT0krRl0oJPD7mthX9ukyUT5Zg0TELX9Ceq1oXIaWePD2YEuXXLiDBvTTMmmSL9VQ0FlJva7hQRvqxoRbY_GcyTcoUOKRFtm-M3g0zdv0zhXxYlBVOUGiszLpQVYbSdepBS8ZIzSp6pu-BNqmX7w1UWRgthvqG68Q3zuLaYuZtqUD7kPFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6W2v_STVLo3KFBk-uJYhHm4NqTUgWYSDTaZD8cqUkfcDqyWiXAafneZu0mye4YMxb1W4OXParMxGzmraAg6FCMoMPBbfLFeuLGAdWQ0l0FieHV89MVVlJmjTl2uG6l_pfGWoHohL15CYXFcOK8G8BMUKKcFQcQU-J3Z6nliOiRPm3xaqyxZy8X9Uyq3DKcUNgfHfQjn4OLujP7yENQtAcXg4yeccDqiS3bPmLkU_CFuTFnbSyuquC2miqSdWZC-S__REYGn2hr_XzHCe-c53Lva5GhrPIg3_Kdu4IXrOfsk5Vq0PEEvbmvbgUiKfoV06KqQWaUeEoIzLhXIZKdZaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=mtXECQts8-84TsoOjRWvVA657OWFdq6koAmP0dqKIWME_erpewnRnNqCYWsZ1lYDdbPBoNyPuY362g1bMXHMLcDiJB7TF9tO9-viNzP8DybK_04YWUcnnEmyY38IyUTDz66z8znGOlZPgYKn3y_HDtOrFYsXH9dAljde_FsehRd-FwFrGqt2FHT3htpm6yOiTjFHt9BUcUsriBpvzOEwpYUJKOrcFFUjxiCWb-M1HN1xUrc232dccXw8W8OmZypAh1MLy4a_b__HTLIuqc-daviMCBxmopFK_PhSMwW9UyR4SIFYqP2llro7Y_o4r-VW038HTds-LET9xGspi8NV1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=mtXECQts8-84TsoOjRWvVA657OWFdq6koAmP0dqKIWME_erpewnRnNqCYWsZ1lYDdbPBoNyPuY362g1bMXHMLcDiJB7TF9tO9-viNzP8DybK_04YWUcnnEmyY38IyUTDz66z8znGOlZPgYKn3y_HDtOrFYsXH9dAljde_FsehRd-FwFrGqt2FHT3htpm6yOiTjFHt9BUcUsriBpvzOEwpYUJKOrcFFUjxiCWb-M1HN1xUrc232dccXw8W8OmZypAh1MLy4a_b__HTLIuqc-daviMCBxmopFK_PhSMwW9UyR4SIFYqP2llro7Y_o4r-VW038HTds-LET9xGspi8NV1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iERZ7-8X1Tx0W7SaDq-6xMncZ_SwsOxUcYh77d7Wz7cE8RWSVeM1NPkjnvEzmsjgb3yR1Z89jb_dQWKKpbqF_wE5BiZQ7llQxYIUQwAz5OKTyotFhab31vhaRP04Rs-_DzwI1to91qmrswFLCkOm3PaOeiGxxzBVHEm3m3Q9cPwUfP2lkji9fte5iuvNenGUhBWN-GdfYzgZjlpNCmmtlVojlyd2nFxoaqusruKu-KYwWBK0GwaZZoGienz41QBi5KbnB2wbMzXD40NDqfkzO395qOIoIRPPfmnz0WvctUIdf-qvejzRm_dzuHr1gqIVfBg4a_9xCGzcKtjY-D2Osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
