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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 605K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-99251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست. گفته میشه کویت داره به ایران حمله میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/99251" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/99250" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRPohDOCtYTijLc0bmxXSua58o8wJZqC38Zl-o73-gM0AUZEvoSE_-Moo2N5GniFPPNIyIf6D8Xnz4vbytTfeVgJXgoTe4QPCNVqNShV9ZQIcP14lUVUJYJytcX8XMx0n06mrF5drAJNzWrjGQu4PJc_-ZR5eF86_4gatd0-PKpa4GyPcUkkqdvKzPL7awd8vH6C7R_FgSrdQ3pbmZLSOGpq_GW_4EYAGeEWhQw-yq6BM8KXgmEoJrnK9ZYCxRfCDbgTXh-t2g1E3rGXs6pXpRCciXGVNekpkQrgwytBsQUX8ZKLJ4j_pSjqeLKj4WmIOqc1StxzYIUxvdgL7SZzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/99249" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bsh0Y-44fBxmlwiPjvpsiTDW3GRVhB8vxvjIxrq7VGLjZcXo0MiYBIWo-ys2n95sOBxtmU181s7zWD_Yg_g3XMwBBamqlpQ-Ay6Kf979_WFCO39iobbeYMIxFfVH9Y5vkIeKxCmhUf9N22H8VS26Gwx26xmBiueyHDngKgv-qJ-5VbUnHDAlfREyQTllGmfmqyhvUlsbyL2OeMhkXbaIpM1INwasjxX7AejJELSoTbBsny055tY2kD-hMfxsFwbiXLVc6uUo2fq8N4M5SdgjzslRtIZPldAx1ieY_QmA2Dfm8EXLRC-ou59Gd96J7NXT9HEZhqvWQvIb4vDvoGrd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب فرانسه مقابل مراکش؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/99248" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9IyyVe5K3GzykM2K_IbX7BCOf04Nq4tT4uhEQDwDaC1XY4fExgvuig8bbOEfVi-Ug3ak_KiT2fFZDjdCRnJftZxoSe6Ca5sr4UD0Kj9z6v5e1lp5C2ELopleSiG7PCb_eNsq_FVGw8iY7ltuFioEc-8fbRNAX9ocwsJhGseqCi95ns4SI5so0b1u9B-EDXy_iAWcrpRrIS6kbHhF4rOnOGlhoYLfiDLgVUWIAR9Jg1iRTS1c0LY2DypnJZivuzNlLD-xMCeAASWzPIWNA1rwWO1PpgabV-Y1hPYB-cc_EHTJojn1feAZw1Ne3RB4lcA83jzPJNCLHaBJoYi-IO-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر لیونل‌مسی با توپ فینال‌ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99247" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=HChWGI2bMHhwh-UNCmyfVv7AgQ6FvjHYa-Mw9R5IN8Xcffm4HUo9g3WEhNpvLk-jCsbLI1uonwosBbZRv57QZYVmKkQ-B1oZROPdbslYthi0R9k4RDXfgGC0kicGMbEfpqlROxEDMv7ccuvXcVjxkhW4QukeeBHpk1sBUf4w3j4PjyTZEkIFmrPruo9tKO5x8NbeY0ZIWFQ2nhQMQ5UZudR8cNeUaUx81XtwM5pu7XizBgX-ey91xvl0cG_6Y6qlAQ517yisxvP_bbqMUck4FMqBf8jwrD71_eRO7et05v3WkxCDz9toHhAEVYTs8w9rT6nb8KlrqWvNAL4Mjyk7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bfe433ba.mp4?token=HChWGI2bMHhwh-UNCmyfVv7AgQ6FvjHYa-Mw9R5IN8Xcffm4HUo9g3WEhNpvLk-jCsbLI1uonwosBbZRv57QZYVmKkQ-B1oZROPdbslYthi0R9k4RDXfgGC0kicGMbEfpqlROxEDMv7ccuvXcVjxkhW4QukeeBHpk1sBUf4w3j4PjyTZEkIFmrPruo9tKO5x8NbeY0ZIWFQ2nhQMQ5UZudR8cNeUaUx81XtwM5pu7XizBgX-ey91xvl0cG_6Y6qlAQ517yisxvP_bbqMUck4FMqBf8jwrD71_eRO7et05v3WkxCDz9toHhAEVYTs8w9rT6nb8KlrqWvNAL4Mjyk7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت رونالدو فنا تو دایرکت امباپه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/99246" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در بوشهر، چابهار و اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99245" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD_UZ_e2hwzDkCyq8eBK-4CL9pVRA0g3R6lprSYdJh5mXcRtOMAMdtRY2SDTVM4lyqYqsRDFwdv939FmLADWoNZXvFZfQF19sK9wTgGLfS2g6iemlRKD8dy0bxWdtRSmVgLTW5u7Ew9OYzkxwA1ldn4DX7gmolyy9bzfScYiNO-v8XShWRZhzKRjHGCkchelrk2QrXAHoSlWSvLsEUxNVhK5XIWh6-CfPiZ4_btsrAGHDgk16GGk8C_9rp9oB8K980YEQLJ2TNp-x6FoJ1GBGwnOqBRamsjPmjyJQADJyJgP99mS43Hya7jRyAVWbul25H8NR8XadvnwdDTqkZhcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏆
دیدیه دشان امشب با ۲۵ بازی، رکورد بیشترین تعداد بازی به عنوان سرمربی در تاریخ جام جهانی را به نام خود ثبت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99244" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg_hTSzvK_mOnwOJGgdKdspsQf_92MimUVWDIaedmLWMVTc8sljsi2TSg7vCO0k4ALdhTeSNwyE1fgBjcQI6WB8rB4QzHYp4ZGIH9RiN7n-kqYyKwIgcTj9MGz69Yv7uJfhZT_ZsAfWqMm5JhD7bxOADz-axYL7hadcjfFGrw0cRPoHkBTy4MgpvRHiTc9VBNzqU_t3-CcVwWV8Phav5MYboIKrJiMVYGzSAH5ATQbrtigHfSVf5avB6NXLAKrH0rgrr9JKkK1CY7cLaKUyCGREEn39OuUazoFP4eQ1IQyioqiEc82sRvdEV63hcDbp7GcBB6in3Gh7WEXlRflEDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: باشگاه چلسی از عملکرد آلخاندرو گارناچو رضایت ندارد و بزودی این بازیکن در تابستان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/99243" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVk5lcNguR59PeOMsLp2m9vLw1a6iGV-fMbwyaqI9ToxH0CclqRDnzpp_MPz33E516rrTqL30YscBb-Zk1u4j_6pMtjtLkuRHaRBlg-LPss82mQxvHPsmHJXfejGZ-trtGyQOfpJQ4Qla2uHr_LeJ9F__ful96DkMrqdnuJ3Sg7PrpkwU-_0qMs25WKjRwh5Z6CCNnn__ekmWZccAwZOz1VCjBI1N0ZXBLvGwSavCAGcfA6qoQDF7WD1y4lFN4ke9T5drGWnkCWGJjlNph3WzuqaGLiTXOYibRdiAJiVUKbG378fTmpC7UBJyOvVPKt2O3IEKa052CnDYl1U9IgYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B40zaVLX1Z9pYsgw4aqeu48luvQDpu5uX_NICdsBUJtkmON34uM5bSdY8RSlPPGY8RsfRB78Oqa41n--1EFYaNXEdkHOkGwc_VEs_fowji6CmsdgTC4dy4PEbwkFdot5K6DUcCRrWD1Yqj7Xr2TBT6Uopvqw2nbEwQ6pUCUKduVWwYLNotfGxe5fozRjvjg5KA9Z8MnVTuksEAzf857iowj-pDbLavnwgqdrWpobAKLUO1hkHQJfO3vtMe5kQorSUCwThwceVO9bIyzUH4iE5Q7U2-UgmAse1iVJ97tobatkfjwiRJF4uRXCGy4oPeuMz8dgLryQK42Tz7nU6CQVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای مراکش و فرانسه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/99241" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1PdFxcTyJz0foYZ9kYhZ7A2ayVYIKmRULgieaPdZ_k9oa57h1cebc455YTbuW68fm7Pw1EZMvQ116Xm8S3j6411NZa11HN9KS4hkvFozV80OJHMCyCJx9V6_oDIRYVbOqfQ-3HzBDCBf2WEH-6rnEvWovZjBuWgR2ZD2Fnvr4Jyftg_YzB5Zo40MtRd6QH0hQed8FoXgxAcDMzRjPhJRVgT_0EtWoR5Cemns7WbgENAeZ_gIjWk3_NTOq5xp3kO96IrWJHnql9bXkiFCeRTa8kcBmhyUs3DppP05_zCYDtn2Dld7d5jr79GqOuBtk8siJOJhDlKSN_WRX5bAJjJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔵
ژابی آلونسو درباره چلسی:
این یکی از بهترین باشگاه‌های جهان است و در دهه‌های اخیر موفقیت‌های بزرگی کسب کرده است. افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/99240" target="_blank">📅 21:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALNgGIFdIAYcxzmYKf6vaC4AlUjlnFNWAfMQHo3Nh8izdBjCUI_9ICRDnvVGhLcevo74M93jXeupjzeEQZmspIJQkmyj25_oNXi8mcJ0QrmPWGWUhRoGZuK2tGORQWSMQgkd8MurhfPHVAlyEd8-l3pGCzheH4fES5Yw-IipIV1YIcl-sncoL_plZ4UMoWG4TcNIbTN9tSnz8nhZR5M1fHzXVHNxgF8yzItmMr7Y_najTQwlXw8diqzqWZ3STUJTUInjDrhPg0EnQNZhCck98aByxNTU1XhHbFh03v8925yIWsrvdCDBokU7EfNeCdfaZ0hV3yMz-zwi_XsSoYYyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏9 جولای 2006.
🇮🇹
در چنین روزی بیست سال پیش، ایتالیا قهرمان جهان شد و دیگر هرگز در جام جهانی، مسابقه‌ای حذفی را تجربه نکرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99239" target="_blank">📅 20:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMP86KSnBVkYWffmgy4bM9h1_82iRNKm8_xcjzzBHjI77mvakJ5bttgi-8FKOFWxFDgzqu4_tUSzH26X-Hazn5zdyk1AhpGkMr1-Nd0WfDC3xdnBp8Y2C567fsza7ZZh2tUteAwG5y4sDorCsONaFC_P-yEBsqahUA8Lzs6YGt9NK0WAosCZhzWy8XBQ2lW7VlIXXG8AoF6FsOyT5gdVNhoJQQBumeJG8YLqaDLqkFeSeGgLA_r8UQQ_hQYpTvYvf2AnLrlizafkzQ8pE1Wqw3OTdXyVzKgSQZ8Er9PvDZhmoRDG5UiAcZJnuAOUUbW2m1YLJNFKHYeRkNq1Ev5e_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
🇦🇷
نتانیاهو: راستش رو بخوای، مسی 39 سالشه و اون قبلاً هر چیزی که می‌خواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی خودش رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99238" target="_blank">📅 20:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJOE5q7awPifyKLD5F-NdPS-Wiv-RKwbXkHiE7uYrphktNdDHfLqfJKNvsTxvQZnsZB8TAR-LXhix4rlM20vNzLMPbdVjwRG2z6_FoqoGHbYsWS2VGJhVXIaeeUA86fNsT6czcpMHeftucEEzgI8qGmaRbkjWf5zfVtnPqKzSmkzVjygpyYdHs8N4bl-2_k85xSQlOtcwD12dVpvcZWFEvSI3LkTIirW3n4xIaZ6VeUbSoouA7wSC7iUET1yTBh_FrtObVW11NEaScn0IMwKfpWmGZJl_YDZCroISCSDLHr8Yz3jUiCHELpYFtCp1T36vrJvDfrqzJH99yy5jCG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
کارل دارلو گلر لیدز یونایتد به منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99237" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNydCLkvtR8tqTH9urLeoiYITM-ZpkPfiBieKYpe9wWc3-4qYFbEb0SHuzYdRwvOkkyVoPPw1pUFjfadf8t2qW6pSsEyWIaoUshYBeYw7CdjzUs_FrtUivWNNEWfUBmneIcIRCzP0FOcgMYE0USvJRnaVRVNQUL5RBw2zWGHRBf875MC2TswUK-rZ085DVzzAFfGka_vxrzpIYK4EtfvTlyJdWsu8V6zI0mfV4qA3IQ5flGS5ETnVrv2f38dIr271ZUqeb4qIv52jakb8tu3ujKImaChEaWn7oVutgyH9JPGrS7AU5ZNGC6OjzEjI53pu92snhbWjPBD46ycC1PtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتامندی نگرانی‌ای بابت بسته شدن تی وی تایم نداره چون همه سریالایی که میبینه رو روی کمرش تتو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/99236" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9MIMzoVj7p7qyAc68GNqtg38zOKsgDG-vkR4SwlRQr_birMdGFipyjj946fK7n5Tp8hfyqd0aiufr86KUMkwlvSpyoRt2ua3h1WkPkAbs9EOroojWFC_-FlaVMpueevGRqZ63Ip3tNUP4QaOdkn4VDbjyg9w7H95-4YMb2MssC1ZnKydylliakBHbXX1D_saABtNHUsUYtS8qM6kn7zqH-mb4MCFrnQv47JtcjywbQa1kiK0GqPHix2Bzi7vzyoNhGm9JFQzLhg0B56H1B5ZFjeT3FZN192jyvkw7neL2F4XHR2-4PUQUjrBOjQKes1W1z-OJNBWQqbEhk-AmMOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
ژائو پینیرو داور پرتغالی به عنوان داور بازی آرژانتین و سوئیس انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99235" target="_blank">📅 20:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcN17fWIZAqG-aZQu1t9sZe8ARlKwMFWMpXFfwjGxf-Qr7kLXu9JwW_acobhhYjFm9oJvpAdw4bjEs78Bw8pDJfxp82U5nlsoxOkyK8TmPu2AlGQhtEjnyVN1wKsAOm1stOfAwfKtBvpOnN_Tt-y0lPIXKcHvX7eM_4wxgz7eq00y-YC1I61ACZElLmOJPft4PwC7xHYjf_e0eqbLlCmi3PCrjBu0ZOHV4LG3dLfOGPqNB5W2EYZyeVPgroJ4rbKczPSSJcf-WCrDIBTAqzOW00GAbG2vQpqzDlNfZSUsNP0TEQmqtZC2LhvnIVN0tL4U0xGBFb63qcayUcxE6ktXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بی بی سی نیوز:
قانونگذاران یوفا خواستار تحقیقات درباره اینفانتینو، رئیس فیفا هستند و ادعا میکنند که وی به طور کامل کنترل مسابقات را از دست داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99234" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریزمان تو اولین بازی دوستانه برای اورلاندو سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99233" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-q3YUKQNHCeWjbIxh63sjVNn9y4Hcp5iB51Cm5Wk9NEpixXgnb9CFyMnxSgGdqz_Vvb3-8ydJLMnpGkD4mMQWMnuxkSzHBrJoBdh7PjoM0RaHYDtPBiML5SjNY-ChbMacZ_c7XFdmENE4sfeyqlk7xgNG7NF3Ddk_ae6WVBZjgPADseDR1nqy1uh7LIuQ-D6D0GjAPrqC42C6FFkwpCukcL6u40BUg5H_6-xNDNtt-yZhv9-aBFq0DXBFOVcd5aedH2ulVD1r2otur5X6RRhkyQFlT_auaYRYTLoMZ8uYX5YqCxrLlr_IuApjPSHZy1-Fs8ca1gQDvBQJ3hNWp5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99232" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال قطعا یکی از بامزه‌ترین و کیوت‌ترین موجوداتیه که تابحال دیدیم
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/99231" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzgwGbGhv9X3KsbjN9L36qOcUZXenqCSQH4kITAAbhKDfQ65sdpgomNAYPv87cw311geIy3Y3rkDcrEwXH2uwUWmrXr-u1Amzar1PArqR73t4Re8XVBHu8x8ZTyjwXJhA2ryWZ4m3fsygqDSj1KhsI9tYYmFZE-gtz8zp6MATUac7oL4YCxthbjFhWZnF794WGh6AsMOzatq77cNjJv4MSgfBKu9HH069e0PfzNVhB6lWeZnYodxcb5DsKxKE2TmXk0_p-tozUoKqMhyiWuitCKsOKh3_SyZIa_oc2gtE0UmsoU4mxbf_MVyVNt1z_BiMPjvSHGtOgX_E2AA9JtB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
لوییس روخو:
باشگاه بوروسیا دورتموند، پیشنهاد اولیه بارسلونا به مبلغ 20 میلیون یورو برای جذب کریم آدیمی را رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/99230" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg9c-qXofQG-SoZYIlT_dJR_iRy25UKnCk-T8_iqQiv8YtHM6qXA85j7CrKYkcqP-OKfqep_0jARvQlUxh88axburxIfp6mpiQX3kmbY_r9C05EOivQyW4Zg_FmclRWehvBEFCqulNhYTP3vexf185Y7UrNj4WXpE0S9nX_ozHLLkBBAsTAh_A2Rv3o7TDcAfhzptw7m-kxLzrc8fSaxhWkyELjKaJt9H8i-XIXZQxWw0RhoKyyC95yB3wSwe_y7S214HBvbCT0iAQ2J_ymLB93Gi82UUBmrE0Ec03DR2Qmrb8ZXu_m2fnd-OTSRYHx1DocUJnGzhk8o0jWBQSNoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
#رسمییییی
؛ کوانسا به دلیل کارت قرمز مستقیمی که گرفت ۲ بازی محرومه و علاوه بر بازی با نروژ، در صورت صعود انگلیس به نیمه‌نهایی، اون بازیم از دست میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/99229" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzvsWEoWuH8WASo46RI2_mXfpgmfSBkDgADFFrgD52vwJ6TMJisibcyqs1oNCe8hv3PcofRm3kfGvsFG1T3uAgo25GyxVjbu4guIyR7lwtZhDBKJPYzxq_Kqv90X0IQftzyVr-_mIw3jbNJHbln8Zgr9TZQ_-nULf7cNoqkvuEtRpL1A4QD-vlR1lykHLbOlcfwlV4BWWEUMltYYGswex6lT10xMoLlfJfyjHUMXFDFSkhoKNHwJiGgZaXbrIE6bM2yBwIt7nFPQfoomX8fz4L1sT2KmnZHOlfbBgfhbUZGuDzA4-iHCYZ8VXK6AbEAFMS_ewBzF6N-xG_efRhQxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛
برای اولین بار در تاریخ، مرحله یک چهارم نهایی جام جهانی بدون حضور آلمان یا برزیل برگزار میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/99228" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-UE0yM1HwCX1DX9a97wKBk7dUDmMa9yvx3P-LiszneChi0Fg4do-QCGm4kZDhGI0GBOty9syo_uNhcmSMGg5tfHdR1SJdhgxbuJ7vRgpm9WZz1zhpsU_GekYfVfr2Kr__Tei2Rv0WU9Cmdy7eBhAqcRS0PB2zG1qhWsRy-_KLr9AiD3KGmWONJVNxtfPIBr4QSB9DDN6QaueExRkrHd1uf0wZP87AhTLifDJ8VCISPpGrHM6UKKEUYeDfjF_Vv10GUxSYRZnFb7DUJ8QuOEnUXcMJROmnb04XWJ9kat6TB2kGs6znIl9_-cun1IFw5PN7k659Fuv28IRczR4Bumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/99227" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXClwSzkntCEzuc6knHrskKA--3yqty86gLgHMQ7UX0ykwq5oXkRJcsczejvKUXIZ_4h2IktyHR1lMc9ZnGhKz7qM6gICh4dCREXAcCE6L5M2yT12rXxywyb85jBSZSzrpzF2COEvUernTTCCsc0L9fhEVuNcuRFd8HfhQdhVbLg5_bwkvd4-1alXLCOyW-3-RRp-4WVUtYxoUKYduzYFP-NcJBmC11y4sHXkzNNOFP8TWC_x0B7iQMmx20eas2wKyUr9EiB7nCURnNPGaiOlfF1nt86rbrvkCPcPNoeg5jJ4s4gQ3BEsP5QfEiuaeUkzcb3qHREaSrqks_x1Kbmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔻
یادی کنیم از تیم منتخب جام‌جهانی 2010 که با قهرمانی اسپانیا به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/99226" target="_blank">📅 19:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvA0RcHD8ZsMfWh34_xrRjCVDM-iftZOnhRle17JzPsjMepGEXb6e15W-Mc4A1_7Exvtdx5qpXPiN6AlEOLUgZ03NkaGICkN0tabwckZy-hP0741ajYt3WBqBJMR9gj87IFI1qbUX53xYn2qxGm_nu_7pivVZPPGiO06_J6JsUQeVEo4j2xDWc1A0BkX2H1GX-cNq9VX9F0m09uGnHwS49M6CzkrJcIpeDUncqLmutRxwhAYlmWG5WxY8j-k5Kw5MnbBJTgBkzmM7Bbg5XrjHcACWITH20gXNyPL5ofDDDyTYfXTezOyPQj4aLcRF5UcwALmjbzFAUN4gidv_8q5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پائو کوبارسی:
خودم را در حال بالا بردن جام‌جهانی تصور میکنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99225" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99224" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99223">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP075B2GhwedAweAFGdJcEKtk6ZtJKlRYsYW6fsKbhSUbdFhI6eUQk2EY47XkdRz3rLdKzjCXJm0nBXnk06y4EnEKtl_WtlgXnhzrQRHmTiO_UV_9FWSOheLAZZYtpzm1v3vgOxOzyF7ecMn12dAC15SsEx_xX5fFg_yrQTfp19s5gJGw4NPMqIfXY4xh7w6jcY-dbTFrRWeuP2mepWt7hwcEcq9K_wCvTMZatGPjmKrjaB8NURPvzoOeOnSVN-g1fQNmo44DoCj0Ce64isOkG31E0T8_Sr3lpgT2XKZdNZhTrn3ENZdMfrH8AA_U4p5VoywKqlvRanlqVzHoYLUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99223" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK-Ht3pQgOwSZMyAApsHc4kRlc-gDFXSNYVb2vlBKpNxSOXklv0Ts5X4_Iw_4PdDnWeOu2WwX27UmI8dVh80-g9HUvpmZNbEkpAZ6hOaHkyIhFHLVXYCmRi7npF6Ou3utuqjgcNG-_dQgMHJnfhNxni2ANWx1CgdKaIFeALL_p6C056q3z1aCiKDXXkpgUCkTd8f5xOAC5cSkcf-Pz4PjAFwtjEy4hteXJ8C-qrLv6LVDVpMKZ2rC99ieFljEKFwgy5Txz656Gah2BnTaPn9UC7DRgCcbtof0EGz6WDnHYhr895rugbSCOCExa7qYoH50UWqij2bkuHXdUu5wBRLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfAXpWji_4-qUzahIEjtH2gMI-ldsqgGBrM4pFVn_z6KaUnnd2PFG2I1HuB05cx8ia6Bgr6JQDwiwAvwgKd9XrqOXjtRD87nGgKJFmYgXB0ucOE8pgiq5XsA_t1Z29zOIDWE9Xe7dOeA3bApuHa1eGo7bbuhYgN4OB2CB4fzH0HkGL98g90rD5uKAyPMaCv0Lerc3r5pW0GppjEpPs4GVkslIjlyyubfdfoqvst7ynjZ_LHSxta4SMo_mPithCT91-tv74hupJLtBF85BZVDJIp-GXjSOt7ae6qInvQZDyj1eVufwmnHXSsY85QyicMlP9nS02SaTRlYMR2baypS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0iJMXWUF_6vPlJ5QL8BTc8N3hHfLvuIAGX888HGlKqLz1nVTzVEqqumxDZ0eBonlYIZRfvbGZzbXGJUnqSPVHRsevHXoteFwkXWuS5GoVbkoI-MUDv-D7BOfOaS1ew7GBNh8Zelbrc6ST6F9eoc3EjbNhtkFqsevGEqwbVoirUqXKeTIxL_jt-nV55aujr7Z7PnNf3aQS1SYxVbAhPdlFXlNjYID5dNjF4tdlmMFUfTHJSRy_3xMafarCwpUfock5zr2VP6LXF5rwzjDpSlZUi0PmEIaHAsBs10b_0iEpbMu8VLD90cRdQvDAeQImxkSXaKjvSCtXMAkzARqpVvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9OxsnKpcTG7kc8Nl43WrnJC59faAJtD8vNR3gMJM2_dW9KR6KAFTl5KRq9fqYAvei8TL78BJWEpK-GCI-ZNKuTWUoXUfBPJkUpQr6BoM2w1W8oyYlbjAVK6286ihnpk9qH5fWdf6QTIM17eRABBspsaVdQF1vLU23g6ptjlm16g23OpxRtpDtu398aZgJDhvz47rlz5bL4oB31jr3m1JXAYYT7B5vXM7cvyFmylKBd8b0run2bu1D87OC6nnFgDl1QlpknhsIbNnh8IBs10XuJDNZ3-oFaTdku_m1x82wetzUYbjPw6vU_e_ryYwD-l-OS7rdOAYkPOBaRESVVWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faylKcVJAGahovOVKv7139MutAiaIn_urUE5Slm5G3Xd8dPB9GsRUpCVqILTOuZI7ubsnlU4GixavHNCxlNRnDrOnDeEqWVwqLzGQBk_7mF3vin1mzO-Z_DNSWvb3s-OAKj8Zby1CiDkj4Bk8Ksj-GIcA7mnetb19S1ImCG-LLMiedmVRMWcIRu0ck8IRPZWlub-TC13Nd-iNHBxY0o8wtw1zggmHt-3i2IweeZAW_XJaxLvw8ITItWSbsN6Q8ixLgy0sgkf7PQjHVjIgPS3jlx8ZW4BDlNC-1lf27xZmKn-AdsS_CHW0Gey7kTtuih1CBqt_7R2eLV-LJISnGGg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrR1WAx3qRdTQF79E15wDlupPKWhhjOJzcWtJNHNP-vGTZUBipLZcfANB2j-1jIS-GEkdZerh1AZZSWHKQWBu3MmGv067ALVs8sJpr97cgM5Q-JRj4oIH-R2zBN9hR4op-4cQg8cJC3eVAmLblWAW4cGuYV3GH9ZrFg-8wP8R6Let4_t1PdH6-JwxEUeM70xW4c36JEyWHSmSxe4B3s2g7Rd6TM2GcD3g4mFIGjlwZ8MmZaQGqfDmyy8iVekEDaeyDEPj0_Qh2IXvSD1hZ26QjBsr1D5Q7PmLzMqGIvsuqQY5Bcvj_wziypsNzJLO3MPJj6IsMxn7Vpjslb9mCojzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HANMN7VFg3Ee0oD4ITHKsBGJJjbmHJLpk8AFUKRJnY6DxUdIlLhqmtp8RfnaME6VTr7BOBhWflOEdT297AhoXN4mRbHxUrYEkR7KFpbvWDK48FLEQ08oMU3ulhS-y5mHri7Ez5sOuVdZJCeMUcjTaeMUIRS4gaOi9lRlLgA5BWViMI0cMxmps3dfhromcxScRgo51HOc7MgNiZmM-G4hAkuu1qyRy1kqok5BTBL7mU0IF5eMXgguMeQkr8xsVwBJmhYOJvKrr0pmeenygkonC6JoYhFLgPYzzQgKDKuo2tMnXH1ZEHtMM6OskxAuaztRUfNkgCYVsjQlgDsyoofVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7K7uRx76iOf3WmsK213vZcJ9L8IpiIkw53NalOUR-5A0wCsa5UBVClm66HuyT1vHw28XUFCxc1zPBIT7fMhethVYhHjgfc8THQyPYa6_4egUqbrJ5jFFnXpdqMxHzxyVUamqi0A0QHPMBgh_sYZDObCBUWb18GnmJ2MHuk4rJPCREvHAvY3wcpeTZDa3rlpBV0dyNzhtOQRWyhEOBs76Y4hhP65GR-E9GQAzfvyFnJRZBaDXh2h1To-4DdpqAjwUy8L4i_IoPvncaF1coMImYHzHG1BGSdbjuZEEY255U00-ReZ3-o4Au4mFgkHg2REqRwpyQeiZYivPpbN1vVaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0pTRzjnFShgRv999Q18jSXWfbOj3B5x5k1wN_Mhwgh6TNsUZvrGPto8VUejHDf-35x7We6x_KKQMi6ExbOi1k6Rk5JZ6hHFViqdh5CQHOmAww_FUm610YesXIDG8rwNTWkg7I-zPS8ntEoDHc3DA1h_fM9i2opYlV2Mn8JjyoXDaHF1fKYtJMbyNo1tDSIjA2Artj18bHtwIvH5UUGkY0LwIniL8MFXI2fGPzlqdWl8I4Y-6NZMbkfkzoGtWZ4CfJk3MkwnOVTWH0Scu4w5Z0s48oI4pftXX1xfwSIJFxsNMF64Hiv4shTkTAu3koblUBJfHtWQG54HCJ9lHJ9QWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تتوهای جالب تعدادی از بازیکنان فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99214" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTinFVGuXyqawpGs91k9H4s81wzBeIN8gFuk-p2Bi3QMGvQJ-1kGbJ2Qm8OVJNvO7tO3nnzufaexHCCOBbzze2eIFEDRR3WsRv767wrCBeLKUQgvfZFl5JkISMeZ7_NIHhrJH6GO-sErknLiGXwIAbIGIDpOgEvmnjHmsgId0kkaHqXAIHCwwnwEwAzvJVd3E5og3fct1XyNx2FogNCwflSv8DGhcBLP0T1OIXJqyPdXzv7JijdwDhFvfFzRd_EKLLW75mTeMiHix4JWLCNqGT47DFoDxsM_oTsKcnzYWJpIxFD3G4hYaOwSAFQ9wMcHS_53eJ_A1t8EfNz2w3uf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لکیپ:
اتلتیکو مادرید پیشنهاد خود را برای جذب میسون گرین وود ارائه کرد.
قرارداد 5 ساله، دستمزد خالص بین 5 تا 6 میلیون یورو در سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99213" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9U2qvY_MoDZhNVeXhGqqAJU2SCgxM4IqM3MlQ4Wj0h-WVR2aR-89Mel8uduISaqEPutthKwOYAApS-CTbF2MvF_yPU1Nnx0GhL3axDmXu1j9S4ru3ntR_5_zBV4516LCpCbbAB025AJKSzkUrBhp5rpfjKAq5qdMH6P5sL7OD7wr0LLmmXkLhHvFpcnQuFTbUYJgxMzNK1DvWL8q7WsEFiSB-1vJIP9SNuEDfjORojHfYe7WU343XswLs8Lh3Pg9xv3yKehpxtZ7u50lSperqe431w8UIgAZIH8bzyKjyDF8fYEc_OnHO6uELbO_ZP8R7LSDwnpVsCaMVD7YAA90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لحظه امضای قرارداد آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99212" target="_blank">📅 19:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99211">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UybnOCAXZg4p2y7CiZp6Psh0uJg5aT-27A536czbRBYbTESjEmTuPdSo5J170PixkIOdsa2YGSY_FjG8__1gfuzW7zQhiMOmg49jTuieFxC0PVfNcoa2fri1sssplX3qVRBY8gBOh9I6chW_KsuhStFhjgTu-5z4N3jqERhkh6kyHZvxcILYkIAmEG80k7E9oVkSTnylPMmfpiLXvtZ2ZGB6B3PvuLhMXRmx6MaPxelPMNA_uMh843yEkwg63ojqIBi6fd8HIbM8Mxfsr8f0A3Qa4Kn4-eVBPss1-726FD7liQtriMTfdw-fcCjh5Lu08xH-wsb5NAVfdOlAtEH58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه لوئیس رسما به عنوان سرمربی موناکو انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99211" target="_blank">📅 18:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ می ۲۰۱۷؛ بارسلونا مقابل ایبار
همه‌چیز از دست رفته به نظر می‌رسید؛ موقعیت سوارز از دست رفت و توپ به وسط زمین برگشت… اما وقتی توپ به لئو مسی رسید، غیرممکن‌ها شروع شدند.
یک حرکت انفرادی، عبور از چند مدافع و ضربه‌ای با پای راست؛ لحظه‌ای که دوباره ثابت کرد چرا مسی برای ساختن جادو به فقط چند ثانیه زمان نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99210" target="_blank">📅 18:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx6roGt84sMVoOd05R8SmvhpNZ1ZUXdpLo4BpOdH7_ui3K63M6TE83oNJ7mtT6_MDKhicfDBCSmevizc-8mlawgb0QUnP54IYAN_1ZXc2As63gRNlyht1lNCXFq5tOS98gYpPStG1cZQGk6WsCO56tA77t8_2G7t0PilPZAQe65E0pANAyox3TmltX7zA9x816-o4-YCNEuHZCCqtXwigmlOsodk-JTAFKWr6P82K4ijToy50Xtu8fH3RIzcNWv_ES1yXQx3bH5aKng36vHibx-T3GJbje88EyVmEb8Q3DX21VvcHqljpHs2YkXesxmVqm1Xno4ZXPosRt4Cz-KMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار صلاح تو دوران حرفه ای خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99209" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZxb7ncoLFcR546yxYVe0xQazKsLgKQN3OI5S00F0sNJ6hFsUjalMDO_eolZijfbW_1DYlVNVU9QoAM-0AzMVFUg87APp2Mcy_PBRPpsb7xpMCwLFJtYE9oddVpbXh8J5YWHfkmhq1g0_KYlQ8EvwNEJItgrlpmU4vX6OtFdfc9fNP8CsZlV5Q6-YnM7UnSzexcT4JstCSF2qBi8AKa9okanyl4c3HDpJHJCBnxhZzckC2jVGRdM_-OUr7Q-KbXc11xqQX6_pPKO-vpPePQpRHjrKwi89X07MgmF6Yq8XxMzbT6yJSKx7fm2MZa9mvOtdP-vlB98j-oY2-419NNPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه و ست کردناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99208" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=GgfnRf-vIYdYhpo5x92z1nnogyKPTDP_vmr5yfyHmxrJ8wY0EjvbUtpr8PhPR1dzyW4YORmIRp7QFMRymDoP_dxxDDNz79LCyFeIC0w8JXVkRedOQ_4TcdygbOV5_MiPJ_MvOO2GvIXtgW7_7uTvcebecMg8XDCSj5-fC9dN_F_M9q9b_fYgq4DfAyECBYL0aZxgEBgNoUkijn_GSC00cJjQuJjrky2CjzTAoGa86Jq4vlyO2JNCmrhhKa5-Qs4zKwGytqMWZ0GNmWHGp9UM8n5vsW3yQlhkGm20Cq0uOJhNpAZZEOpR0u7pnwqQy9NZRP0B9tJG_KsO-9VpSusBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=GgfnRf-vIYdYhpo5x92z1nnogyKPTDP_vmr5yfyHmxrJ8wY0EjvbUtpr8PhPR1dzyW4YORmIRp7QFMRymDoP_dxxDDNz79LCyFeIC0w8JXVkRedOQ_4TcdygbOV5_MiPJ_MvOO2GvIXtgW7_7uTvcebecMg8XDCSj5-fC9dN_F_M9q9b_fYgq4DfAyECBYL0aZxgEBgNoUkijn_GSC00cJjQuJjrky2CjzTAoGa86Jq4vlyO2JNCmrhhKa5-Qs4zKwGytqMWZ0GNmWHGp9UM8n5vsW3yQlhkGm20Cq0uOJhNpAZZEOpR0u7pnwqQy9NZRP0B9tJG_KsO-9VpSusBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99207" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=ZXVlok5kBEhLQS4-JC0wBtxOOO8RbHdHVoOBn7Mzs1XSZXwd2vzNdD8gCkwcKUDA5_PQq4b4CuICPx9ZXueuyNqmA4Da12QWucKQ4KJ2dwyiNVFQr5-jktPmZA4jE2dNlN4IZp9PXHEwUOWCvwl3Te8rnIOzJhXv8eCyh1nW_ykvjnt4ArLCfTcT4bq3Uw_di_K4fIyty91NbNGYlV3y5mfaSK0EfbejgAVZ_z9wQaAczuVd65u3z1VFED7jI2RolSUfMEJgizOI5Sp_dkt24lLfQ9IamN8re1ZpAnB6BKycPc3YlpFFbSb4nRiEjFG6bMSXjAyjTmF3w25L83HD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=ZXVlok5kBEhLQS4-JC0wBtxOOO8RbHdHVoOBn7Mzs1XSZXwd2vzNdD8gCkwcKUDA5_PQq4b4CuICPx9ZXueuyNqmA4Da12QWucKQ4KJ2dwyiNVFQr5-jktPmZA4jE2dNlN4IZp9PXHEwUOWCvwl3Te8rnIOzJhXv8eCyh1nW_ykvjnt4ArLCfTcT4bq3Uw_di_K4fIyty91NbNGYlV3y5mfaSK0EfbejgAVZ_z9wQaAczuVd65u3z1VFED7jI2RolSUfMEJgizOI5Sp_dkt24lLfQ9IamN8re1ZpAnB6BKycPc3YlpFFbSb4nRiEjFG6bMSXjAyjTmF3w25L83HD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
تعطیلات دروازه‌بان کیپ‌ورد در کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99206" target="_blank">📅 18:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=QD3i-zGpvS-EUv91_sMCqnM_GTrU9qT7PRSrWdW_R6sPrekidmQD3Gqx2F6uvrEeZMo926obD6I7t-BtTou37l_8SiJU7fdht-7bKVc4vjatZQWEXsX4uvWIvVnBIoBcZkfQ4m1sSi4IM-v6x0vVci732wuRNs9PPRhwsR2i_YRRPLmZ44ZH4Hp5w01hYikW2ubHok_yNnTMBEHhWjbtuRLhtV1aDHqtFLO_IZnTUPpeD5uthXWiFzqrMHufnBk77WQWp8-zsAJ-zhdAl46Zaw0Lp7QC4NcEPcV2WYbhQ9qfnTpLsEgEWULx75sDWymUEDnHlViH1yaKtHnMQin5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=QD3i-zGpvS-EUv91_sMCqnM_GTrU9qT7PRSrWdW_R6sPrekidmQD3Gqx2F6uvrEeZMo926obD6I7t-BtTou37l_8SiJU7fdht-7bKVc4vjatZQWEXsX4uvWIvVnBIoBcZkfQ4m1sSi4IM-v6x0vVci732wuRNs9PPRhwsR2i_YRRPLmZ44ZH4Hp5w01hYikW2ubHok_yNnTMBEHhWjbtuRLhtV1aDHqtFLO_IZnTUPpeD5uthXWiFzqrMHufnBk77WQWp8-zsAJ-zhdAl46Zaw0Lp7QC4NcEPcV2WYbhQ9qfnTpLsEgEWULx75sDWymUEDnHlViH1yaKtHnMQin5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر آرسن ونگر در خصوص حضور کلوپ روی نیمکت مانشافت
: کسی شکی در مورد کیفیت کلوپ ندارد. اما همانطور که بازیکنان خوب مربی بزرگ لازم دارند، مربی بزرگ هم به بازیکنان خوب نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99205" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=T2AikyZ8foG6jC0mSZy27aqgrp4-nRxZPqmidYMTexlBctfqHsYDLOv5QVcItWP1lvudyIAEj95husH1GJYqLOW45q5Stl4d02FT1VQ31f4AIfLM3eKLq2hVQmZykQAEVtL74A6LFcZsNLHR5fPLBfqH7dSJfBFfELegzj8hQ_EdmIvqq0QcwJA3Wdh-9J3C4t37MN-pb1HzNnFGFt-jyhqlKNW6ne4578VRTmitTJbFrOqr6aIKRLXS42h6ZOA-jJI8hano5oTNI5_InOjmkkhtDJCQ069ArMy2NbOZW8jtKF2KsOZMjgSP_zlSfYDenX5Bz606JYeGw9dDOKwihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=T2AikyZ8foG6jC0mSZy27aqgrp4-nRxZPqmidYMTexlBctfqHsYDLOv5QVcItWP1lvudyIAEj95husH1GJYqLOW45q5Stl4d02FT1VQ31f4AIfLM3eKLq2hVQmZykQAEVtL74A6LFcZsNLHR5fPLBfqH7dSJfBFfELegzj8hQ_EdmIvqq0QcwJA3Wdh-9J3C4t37MN-pb1HzNnFGFt-jyhqlKNW6ne4578VRTmitTJbFrOqr6aIKRLXS42h6ZOA-jJI8hano5oTNI5_InOjmkkhtDJCQ069ArMy2NbOZW8jtKF2KsOZMjgSP_zlSfYDenX5Bz606JYeGw9dDOKwihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
نظر جالب مرتضی تبریزی بازیکن سابق استقلال و تیم ملی در مورد اشکان دژاگه و مواد مخدر جدیدی که فوتبالیست های دنیا به راحتی از آن  استفاده می‌کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99204" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=ltlcjqI1f6QjTfKJZU7m1AZwV-dEk_KuKZt9OkEZwm07X96DDwax4Q_ebLAaHQAjRXOpNXC_WlvosuJw-7guMAWNQzyw5GQ3ykHOCO9rw-6G9ECzfHHIdyDM1gpkiVdnsEkwyeImyDyJEkq5D7NeJHnq0TWvuTyHV2vOBaQFEXryQAEzvQ03qEsWPYpKR0nh0mCC50H7_-aXG4wK6wi5rmNQ2pXxZKs7HZokao9nExKG-2_d5MPkjrPAbXeFqcKalFq3_ISZyBxNOGPU8U6XSce7GLEwWrvz5LWvN409JgtmuSlzBwzFZMOMDUy_OxUvUfV630wh5yiK9kOfPLz-0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=ltlcjqI1f6QjTfKJZU7m1AZwV-dEk_KuKZt9OkEZwm07X96DDwax4Q_ebLAaHQAjRXOpNXC_WlvosuJw-7guMAWNQzyw5GQ3ykHOCO9rw-6G9ECzfHHIdyDM1gpkiVdnsEkwyeImyDyJEkq5D7NeJHnq0TWvuTyHV2vOBaQFEXryQAEzvQ03qEsWPYpKR0nh0mCC50H7_-aXG4wK6wi5rmNQ2pXxZKs7HZokao9nExKG-2_d5MPkjrPAbXeFqcKalFq3_ISZyBxNOGPU8U6XSce7GLEwWrvz5LWvN409JgtmuSlzBwzFZMOMDUy_OxUvUfV630wh5yiK9kOfPLz-0TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🇳🇱
به مناسبت بازی مرحله ¼نهایی آرژانتین مروری داشته باشیم بر بازی پرحاشیه دوره قبل این کشور در همین مرحله مقابل هلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99203" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99201">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0rBqNS9g7UkyxHchK5-13phBBWVtcNnLUTKTogwD_fEO29Q2vSoP0EinngNtKOrotJEywDIbONrzHXs0dID7beRNTj-WdabOsw2dp8agmE5ZDqUsVaDrJ9MbVMa5ZQCwXm67TSh87-T6YoLNukTofhZKsK6zlfWA0wK5ng9D25ZMvHORhe8Uu8sOA4_XFgKCTZIsKE4qDk8aAUsAxf62TmYKIoxa97H2pFnuShHudOcNQStmB2PdW6sDTav1GkpZeTZ3w1A3CAF_816dNJ3fMspjYzMVaZX-yL_XcnaU0vaNoVNUuCbpv5GCAEtd2OdE9C6DZq42EA6DNldRdHFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSpmav2h0_ogr4OuNOdpIsiqpj8_m3K22dUXRwtj2erJbRs5Zex97O2RuKq2kbP9lH4FgC5VPpnqEYUrifte17Dt7ZzY9bhYhCmAx9FVQZAQ6hfLRXwXBYVkad__pGdFzuFmYCBQqCUn3Thfwlx261zZpZzQArRA-I2nCpK5tjTrJAt8CYvXJso7X3KdVfne3f2B7VeYTpk6ZZBQtE8SzK0nl3N6K15W965MQ4yh6KapnDVX8Hjp4pVdR9sjDPjNtR5u3rz5E6q-Q9JbkV8Og2DGFup9s_FIcQFr3Pxlj45moqlwe6WrkeMZ5x0WboHF24wAyqDtKswQIRGWgj1hEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
ژابی آلونسو در جلسه عکاسی به عنوان مربی تیم چلسی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99201" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99200">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039d015f28.mp4?token=IGisZ-Ks3eVnpYIlI1Vvs7aDkJG1FQGA6-iCaw8lxxVBqQtbw1c9WFKRQ3ALm6gHiLblDug-X1MSrZS3uP37vZ8neUAwHnCU11WQUGvz7qelmeFQbdpFOfbkR0XJL2gwEKHo1euw1QFQ1yFCwD1V_3EK5kjI4Os28lsnjnEciNjguJFrM6tCzVKSgkSINknsS4w5VpKSp8TfP7MHQk66-Zb-wmgIfQnuLlDkxbZZZJeXRhrVMdzuHp-eAVR_prCJKpuqCQYvifu41yNHjxJC5j-9WCJl0B-xdhigkxiTI3I12jIG0Rw7JVZDjck-2KATSLqm1KDliUa7a_2NEPAMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039d015f28.mp4?token=IGisZ-Ks3eVnpYIlI1Vvs7aDkJG1FQGA6-iCaw8lxxVBqQtbw1c9WFKRQ3ALm6gHiLblDug-X1MSrZS3uP37vZ8neUAwHnCU11WQUGvz7qelmeFQbdpFOfbkR0XJL2gwEKHo1euw1QFQ1yFCwD1V_3EK5kjI4Os28lsnjnEciNjguJFrM6tCzVKSgkSINknsS4w5VpKSp8TfP7MHQk66-Zb-wmgIfQnuLlDkxbZZZJeXRhrVMdzuHp-eAVR_prCJKpuqCQYvifu41yNHjxJC5j-9WCJl0B-xdhigkxiTI3I12jIG0Rw7JVZDjck-2KATSLqm1KDliUa7a_2NEPAMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
رونمایی از ارلینگ‌هالند در آستانه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99200" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99199">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDAt-tizkxSaAtbYMc-FA3j4H_wIQ4deeo9bYa-aopUG2NCuF3bw9GYb1vS1UO7EwGXoaGk-CaIEWs5EoWvDR5OjfXAA92qS82e8opeJK9QJEEnle14yXa8gLoOcDlyxtGfqpPv8oCKLCaRJBo3n4LMd-exv38MV0sNQPMvcrgjlf29H16QgQ-HuaK95QQRqWw-Z2frtYi2LkgMNvbR6cGQiieItzJlzyRVRUZ6amvrZnOHn2tPa5O6LzWKv4KMZmtGD9noakdEUaLjdAIiF1ravn4gLy8QgIeWC8gHa3MrrpleEZbFsL7GBGa7RJy6AvKHWZS596r_olnvJBhKaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
باشگاه گالاتاسرای ترکیه درحال آماده سازی پیشنهادی برای جذب ماستانتانو هافبک آرژانتینی و جوان رئال‌مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99199" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99198">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=uJBSuSgUPMkcQ13eo35lihykepV4Mw3V9H-1qRsZJA2u39K8yFlOwlQyT5MxIXRzXYx_i0jEqemPBywRzGMZSq5JdE2Cztgaoz0zow9a28qRF6SqUQLTWtAwZk0DPFCLOYnj4hB5dC_3I-FBTcxxcc5xUebyBVkbg6s8yDCzNMdcXTIUrLDpsGGRCjXGRe8QJaVgCgtbk2F_Y4YRmRqkVUZyfMVqNEqod1nVTvBuF-JZiHORbzLoFOWuNaf3RFlFuNYqNO6tHkJqMaRdzD9hkolNXClw8FkyV52b9r4N3jVzCoUkh-oQOv05ozfr5K7VEuSzeuFq_hKOIr6zjTqSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=uJBSuSgUPMkcQ13eo35lihykepV4Mw3V9H-1qRsZJA2u39K8yFlOwlQyT5MxIXRzXYx_i0jEqemPBywRzGMZSq5JdE2Cztgaoz0zow9a28qRF6SqUQLTWtAwZk0DPFCLOYnj4hB5dC_3I-FBTcxxcc5xUebyBVkbg6s8yDCzNMdcXTIUrLDpsGGRCjXGRe8QJaVgCgtbk2F_Y4YRmRqkVUZyfMVqNEqod1nVTvBuF-JZiHORbzLoFOWuNaf3RFlFuNYqNO6tHkJqMaRdzD9hkolNXClw8FkyV52b9r4N3jVzCoUkh-oQOv05ozfr5K7VEuSzeuFq_hKOIr6zjTqSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
👀
دوربین اختصاصی لیونل‌مسی در صحنه گل‌ سوم آرژانتین به تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99198" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99197">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAtroArWrykKbFNcxqWaUGQULBlr5MzG8QaIepLmIzVnYJHFzhEWW6jSVeAeKukKCz7rzkQrPCqd1CJkhczpddCWM-Ky5bowLLf9EIMaiMKccGoQcvnlc6xZIxZJ3xltIBQ8pRcUGB6NxMYpnqj-3hGBOzKrRy9ed8N715GSoHWXuOIn43TFXLBbChtyIffJ5bpLXwmsxq0xiLnA4jMtrgnPhYae5i9j8-TNEEKukzSKVAWARLmSyNk1z7Ks44qgA8s6G3l5wosnrMVqloF_gm-kIVWRX_ErrbzWCBoxQehIUTBXABxAPVl3g_LqbYK8DvVpJ3GVAE1mvw2tOi5fRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کوبارسی رکورد جوان ترین مدافع که به 5 کلین شیت پیاپی تو جام جهانی رسیده رو شکوند، این رکورد دست مالدینی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99197" target="_blank">📅 16:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTyoV7IWJyA4ll0cMDL-cIg-pLa6HS61Q6TOQhzHD8LiS8MgVmYzCc5HigC0D-QgnuREwYV-s0PJyJAJfkBj8JWtI0P0ibzMJKWr48tLvkFxR_BRFnFa0o_tj_fcud_6RYJ2qRUgH8qADVzfoC4QWUnLjg4xept6_JQAsgLXz4NYpOzeki6R1wKZRbpc6ETJuVZ6sEMUpLOGcNNsgsO7EUabnRfRBHR0yF4-tstokbVZX2iyETMDsfy_Mub3a99nH5lSEZBiOPkN5excvnX_8VmmnGdeVZx05wtMRypmrNCN54r47lRe5w8kYTAxygBj6__qydxdLHVciIe3MVBv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99196" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99195">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=bVH52dX8V9_WXmBd7c1nSMhkCAmnJqb7WMZSbNlBWvM1cAEPYnnO_yuLdIvBF2sA2ZhqmXJlR9ANgUPIViOksvRHx_SHF-ek0QjU6sNfiOPvxSkTs-J23VKga84b37pdvDcKyPdbCtAGkQPcNa_OmEhW94esJ4SDPDeJWRsdYsPqreaESaW-5OCVqo1GKdyxwlHmX9L45ebbv5IKb_1O_YEXDP0jxjZqinLbhC3lDfTX48JyC6zX3K03Tf5Xd6m6iFHxwE5Y-e3wJcvmz8KmO31QZR-trHlR4dLFZpB3CF4k98hZ56HeBBQzvaz-_KuOzsQVwPUwW8IbdfapxIsyJ0_3qg1F-jdiRXpHq8IZfEGTeTh2u7wk3BgHlajQkE0tS0ZVIQR1gVOzLsPS1xQyxBxJZ1QP3MCZ7106gWeDXwNOY6N0sx7oY9vAYMUlKxtNB4D9dqbmLoQErAwSJbkAoZra14bIsh_MkF9EFL-S6j16idAfJzp4e_GkSYrzoWCzgNN3ypU53NGOp94OSGQsLATG2Vd2DXogAU1s8a1QvAtqhiM9IIM6lg4AeJKH5dC5dN3Io0bmZBH-PRKuqkgeQbrs1MxV9zmvBYfCHT3IKKWfxUBxMCLAByMNGyslls80ba9H26bwXIAb5_zDoI6wuiQuMqr9pwT10nvFVZ4brHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=bVH52dX8V9_WXmBd7c1nSMhkCAmnJqb7WMZSbNlBWvM1cAEPYnnO_yuLdIvBF2sA2ZhqmXJlR9ANgUPIViOksvRHx_SHF-ek0QjU6sNfiOPvxSkTs-J23VKga84b37pdvDcKyPdbCtAGkQPcNa_OmEhW94esJ4SDPDeJWRsdYsPqreaESaW-5OCVqo1GKdyxwlHmX9L45ebbv5IKb_1O_YEXDP0jxjZqinLbhC3lDfTX48JyC6zX3K03Tf5Xd6m6iFHxwE5Y-e3wJcvmz8KmO31QZR-trHlR4dLFZpB3CF4k98hZ56HeBBQzvaz-_KuOzsQVwPUwW8IbdfapxIsyJ0_3qg1F-jdiRXpHq8IZfEGTeTh2u7wk3BgHlajQkE0tS0ZVIQR1gVOzLsPS1xQyxBxJZ1QP3MCZ7106gWeDXwNOY6N0sx7oY9vAYMUlKxtNB4D9dqbmLoQErAwSJbkAoZra14bIsh_MkF9EFL-S6j16idAfJzp4e_GkSYrzoWCzgNN3ypU53NGOp94OSGQsLATG2Vd2DXogAU1s8a1QvAtqhiM9IIM6lg4AeJKH5dC5dN3Io0bmZBH-PRKuqkgeQbrs1MxV9zmvBYfCHT3IKKWfxUBxMCLAByMNGyslls80ba9H26bwXIAb5_zDoI6wuiQuMqr9pwT10nvFVZ4brHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇩🇪
فینال جام‌جهانی ۱۹۹۰ میان آرژانتین و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99195" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99194">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99194" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99193">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99193" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99192">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e630de904.mp4?token=f5WcZK4fR53hjYBovJjw0J63YD2eXJki5rMVOcytUpOd0JIMyGcv8jpU_785OVJkmY6i_H-nRfNlSlPg0ODAbDrwIGrInf1HHaF8dC-z-ocRg-MTyGNBXmSOkysLTuejGcrpTswmcjIyedO-N4ynDbmTic397RkwJiapNSmw2eDVFE_xjLIGCCKggmiLIc7cYbF4y7wWgdGhIJ8sXPYWU5wCv279XjmDWyCx3yt7_efHhTGljZna_Z0dKBdjbBWxFcCfX5jVKxESExm_-PDB6ghYvXsytwWNCx9-O3qe93yoRJAu4FKin4_omx6TSM8VeHKBhOIMmoSOewKhsftWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e630de904.mp4?token=f5WcZK4fR53hjYBovJjw0J63YD2eXJki5rMVOcytUpOd0JIMyGcv8jpU_785OVJkmY6i_H-nRfNlSlPg0ODAbDrwIGrInf1HHaF8dC-z-ocRg-MTyGNBXmSOkysLTuejGcrpTswmcjIyedO-N4ynDbmTic397RkwJiapNSmw2eDVFE_xjLIGCCKggmiLIc7cYbF4y7wWgdGhIJ8sXPYWU5wCv279XjmDWyCx3yt7_efHhTGljZna_Z0dKBdjbBWxFcCfX5jVKxESExm_-PDB6ghYvXsytwWNCx9-O3qe93yoRJAu4FKin4_omx6TSM8VeHKBhOIMmoSOewKhsftWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام یامال به رونالدو در تاریخ ثبت خواهد شد.
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99192" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99191">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fb637797.mp4?token=bNG0MPB41JczOqJaeP8FP2w2KeP90c8AY_Pe0ULTvAgDVrwHHNG4pqTt6AdoN5_CtJtzJ1zn_tujFMeY187-eKYFlSTgesT5OJlze63GH5ttIIrQOB5e69r-M3ssrUWYuKdCv3yIpqhpne3102qxGn3T6HC4yBa_ShQxPqvKX-YdJUklLEQdY09iU79IXTv_HaP2216PF_9Xt3meb48lsjX1VgCrchu9OEAWOIW3pFr-Yk_RjYUxF2gJgQU3j6TLQKK1Z_8CCFPc_a9hRGadvHRvuDp9xSOOIf-J50614XPT-4sWeTS6WPPfsav4vhZm9oeLk0TgnCpYZK-whxwzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fb637797.mp4?token=bNG0MPB41JczOqJaeP8FP2w2KeP90c8AY_Pe0ULTvAgDVrwHHNG4pqTt6AdoN5_CtJtzJ1zn_tujFMeY187-eKYFlSTgesT5OJlze63GH5ttIIrQOB5e69r-M3ssrUWYuKdCv3yIpqhpne3102qxGn3T6HC4yBa_ShQxPqvKX-YdJUklLEQdY09iU79IXTv_HaP2216PF_9Xt3meb48lsjX1VgCrchu9OEAWOIW3pFr-Yk_RjYUxF2gJgQU3j6TLQKK1Z_8CCFPc_a9hRGadvHRvuDp9xSOOIf-J50614XPT-4sWeTS6WPPfsav4vhZm9oeLk0TgnCpYZK-whxwzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
🏆
دو قهرمان، دو قاب، با هم و تنها
🇦🇷
🇵🇹
تنهایی کریس رونالدو بعد از حذف پرتغال و مقایسه آن با تیمی پشت مسی، بعد از صعود آرژانتین
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99191" target="_blank">📅 15:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99190">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPm-XngwJ0A-6YA0exNCykWMHmdKijEnjh7CuE8ddULcqpbXpEuwuyRc7daymk991r2GFjacWe3MXlD216OhrxYITo_5OBHIO7UTY-Boxf4FVf72y7pObM8WnTzPpaBLxL57S5LJ_s7E7Tndc6m0NAw4SapbWobPzG7bEgwLAdREoIlGICD8aAJ9B-YiRPBK_d3rM9jjo9cT2MQO1wF0UXbu3yNrNGIlvJza4YOfza-1M9M9j_c3YE8wRdnWTGR0yp-0UPyaQijA9XLMBPzLpZ-w0jDCDPW7aROHRIMX8djT1triHSZOZbb1qNohI_QlBWMRS3eUdvkiOUWg_oVMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99190" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99189">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=JQs0X597_YbpZ6ZTG41Gyvbg8hz_U_k4S40pf4UDiA2PsXSzmSJUB42EIXPWmB_mPkSUMGIYgoSmxUMQTwQKU_xfvayPX4uZWoQDB7auv4ACEct-FSlbcVeZfjYASis-o5Zz6Iv5kRtTGB3Lk6xi9RkBLqqa9jS1gGgQqvug0mXudMBpoRrgxWCOyemAp9brKZvj9VAt-x_DGttMboEtq_HZdMrGWbIiMRsiMOOKXuAkO6CcyK9KhXbbdoA7YbZcC2Lytu_qI35HUTc4STYKyzWwa-3tLqqMCg4ktxscJ-dF03N8_OwerFAjyjBAMFkhBmllE0Nj6MUS9GUQd3yVIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=JQs0X597_YbpZ6ZTG41Gyvbg8hz_U_k4S40pf4UDiA2PsXSzmSJUB42EIXPWmB_mPkSUMGIYgoSmxUMQTwQKU_xfvayPX4uZWoQDB7auv4ACEct-FSlbcVeZfjYASis-o5Zz6Iv5kRtTGB3Lk6xi9RkBLqqa9jS1gGgQqvug0mXudMBpoRrgxWCOyemAp9brKZvj9VAt-x_DGttMboEtq_HZdMrGWbIiMRsiMOOKXuAkO6CcyK9KhXbbdoA7YbZcC2Lytu_qI35HUTc4STYKyzWwa-3tLqqMCg4ktxscJ-dF03N8_OwerFAjyjBAMFkhBmllE0Nj6MUS9GUQd3yVIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
از کودکی تا تاریخ‌سازی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99189" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99188">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=Y0txdV0SNlVAWhRlMN0LRWl8r11RaY_1vqo4UY0Dz2Zn4T_DjiQDutzdka21YhSx622MTJDCSafbuDOI2OZSAigYMDxabmij8woSAd7Qt9-on0xKy17ABzudY5lVZ_ukEhINLHDJd6lxVnV6yFU3fuJC5zvTldfjhsI44Wlz3GdKUgbm7KH8WiYMdm7vW5my9qmqYy6QAGpy_u_ArKvApu3oam51myCAakgHB_Fu4HlEBTlvbpid_qYXDYVGFMOCnho8KgN1DgUO7nk-BqJLda-npz324XHMsSx1st1Evm7TRxCl-Dp6qaWmPowciFXwb7D8BTbVcqnWu54mE-V1Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=Y0txdV0SNlVAWhRlMN0LRWl8r11RaY_1vqo4UY0Dz2Zn4T_DjiQDutzdka21YhSx622MTJDCSafbuDOI2OZSAigYMDxabmij8woSAd7Qt9-on0xKy17ABzudY5lVZ_ukEhINLHDJd6lxVnV6yFU3fuJC5zvTldfjhsI44Wlz3GdKUgbm7KH8WiYMdm7vW5my9qmqYy6QAGpy_u_ArKvApu3oam51myCAakgHB_Fu4HlEBTlvbpid_qYXDYVGFMOCnho8KgN1DgUO7nk-BqJLda-npz324XHMsSx1st1Evm7TRxCl-Dp6qaWmPowciFXwb7D8BTbVcqnWu54mE-V1Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
حرف‌های ژوله راجب فوتبال که محمدبحرانی از یه زاویه دیگه برامون تعریف میکنه. جالبه ببینین حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99188" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZvjcZouvZGGUkOgayHVy3LCP--ff1dpepKnYht0xUiGXvQnN9gzbfFNMCsalcaAHh2gdp6koy1flXtfp243O4cKito4bg2ZkxABGzr5BXj-U6H_C6Mj1PM_nAtKO0gH4bY7zKG873g4xZoQ6iAl7-WL7Vurw7JDt5uvI-ndVU5sjcuLLuN6mi3DiFB8kx3im1n3hfSOCUaBHdodLhSUnYNiOV4rin4G2mFH3j_dlH8qiLTSrL_Qjej_hMRJf-dOniIB5J5ysfNP0BHxXLyYnkH1Tfpj6nTGPHcJfywhv2msssbxN0yCLyPHMD_9mkAL9IXBg4mLrXD6lxxbmRentQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNTN91lNuwqa8jrJXurqWQI6n_oXQ7qVf7hVnCAIB-p0A3BmZfrCoB_uSBWiB7yt3jMEsjJjRnvODo7VlP3uub68l4KkZ8Qhu3Ag4AwTdaMzGhwOFj3c6FQpIuYfm5UZ5BcBT3f_IHaIK0YUwh2NuNp-dwX0wM7KdrzmCansHv5chTA8R_FZ0G4W5UXp3tIFUpl_yw8CvZFsoCMu98qljQl0-TiC-bDjdy_XhV_YWjyKgoOXwBafsyLC-7MjOrrmQqpL-PG42OrObUqZLXtXQwPMUzvoUsi_jXhwNAXEg8toxV7AtJRnBwks2EbFonhtrwR9y-27h4RSKWfVpC-tgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت اسکله بنود شهرستان عسلویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99186" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش ها مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99185" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فوری؛ از اکثر شهرهای ایران به سمت پایگاه های آمریکایی موشک شلیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99184" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=Ou2pLzDJgq2GEZ5kfq9EN6IWSe8lykENbJ9_F2waE1ptjxld3Wfy71WPbaURAvQ6r2t69BoXDQG6VQgItumiqskLil5v9363oeB1eA_5FiOWBPRHeq-MomjV4viMM24eV294eMe8x9Ijluk0jF1TUTpV-HEhKLYTR0RytR0dk8WC0orme3ZotiKvtCb13VjXHNwnscccYmmmcBVIjXQR04EvdyicKuNyGVrtFFzaMcxfyUHolJKEeJ08JBRmOFp6yuX-ml-AGbJT350w-FgCahnXhXhwdWA1ZSfEufezYSMNepQDFFckBzP0qyBSza4o4eG4LnJvAuH2kgD5BArp7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=Ou2pLzDJgq2GEZ5kfq9EN6IWSe8lykENbJ9_F2waE1ptjxld3Wfy71WPbaURAvQ6r2t69BoXDQG6VQgItumiqskLil5v9363oeB1eA_5FiOWBPRHeq-MomjV4viMM24eV294eMe8x9Ijluk0jF1TUTpV-HEhKLYTR0RytR0dk8WC0orme3ZotiKvtCb13VjXHNwnscccYmmmcBVIjXQR04EvdyicKuNyGVrtFFzaMcxfyUHolJKEeJ08JBRmOFp6yuX-ml-AGbJT350w-FgCahnXhXhwdWA1ZSfEufezYSMNepQDFFckBzP0qyBSza4o4eG4LnJvAuH2kgD5BArp7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
‼️
نمایی از سرمربی پرحاشیه مصری در هنگام اعلام مردود شدن گل تیمش مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99183" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99182">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlS-kOPRxIp_GWthCzvI8Xsfs68xgnZeAqWwkYCKTYj7bXhHZAsRTvwpzUZWwQ_rjMB_0DJHFgsYKZUAQ7WqW2_f9G8puOR8Pc5wPiVprHLCSrat9pILfi5C-lkMa1kx1T37VYThgDMiZWH7xanAm6_A_WNUbR4L2zCTynMudpqWZw06PBDSwd3UpYzEPnP_Dof1inRgyR9eNdrT2-W7thscLYBJpUAYjBlhsLboEhvFworHc5gcf6xfNRLja4ligji1H1TmCiIlz3L1jCVHXzM5Rg7FIjpwHd7d23lHnEeUAga8-WjS70ZNrmwIW4noT7ba4tUc8e030T7r9rnOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه امضای قرارداد ژابی‌آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99182" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99181">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ یک مجموعه صنعتی در کشور اردن مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99181" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99180">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
از منابع خبری عراق: چند قایق و ناو جنگی آمریکا مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99180" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99179">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ گزارشات از شلیک موشک‌های کروز به سمت بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99179" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99178" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=slKK-Li8McrZoeWhk3dbUe1u3gjdNKhmMy3-1cdMn-47CO_sBoEXc3F9dMmv_Vp_d1zf_WqcBsu7EVIWhdn2KiWGDbYQqPM6dVPvEQBFlWyDuSkfrxkDNJ-kSZH7c6dDXLaijzhrpmDzwU6jrjUMHGh43f1oqruYTX82kEIEtromOU__hMKSKNPcc9rO1998rBcSyn2JdiYHXvB_0KFvJc38DQrXGQYdLq52cQW3IPMVL-GgnpUjRwY3reHrjVxgJE0_lRKWsp7Rok_nf_VRJXF2IA0D1weteVIabWpEBU8CjSIzxtvAUCgh9xA1Hkhd-wgxdjylxnduItn3kNn7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=slKK-Li8McrZoeWhk3dbUe1u3gjdNKhmMy3-1cdMn-47CO_sBoEXc3F9dMmv_Vp_d1zf_WqcBsu7EVIWhdn2KiWGDbYQqPM6dVPvEQBFlWyDuSkfrxkDNJ-kSZH7c6dDXLaijzhrpmDzwU6jrjUMHGh43f1oqruYTX82kEIEtromOU__hMKSKNPcc9rO1998rBcSyn2JdiYHXvB_0KFvJc38DQrXGQYdLq52cQW3IPMVL-GgnpUjRwY3reHrjVxgJE0_lRKWsp7Rok_nf_VRJXF2IA0D1weteVIabWpEBU8CjSIzxtvAUCgh9xA1Hkhd-wgxdjylxnduItn3kNn7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری
؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99177" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99176">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
❌
🇮🇷
گزارش‌هایی از شلیک موشک سپاه از نواحی مرکزی ایران به سمت کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99176" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99175">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اخبار غیررسمی از شنیده شدن صدای انفجار در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99175" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99174">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIZhVguwNrNIHbHMnY3-dtIYGmWrnMh1cEARgfAr43gnZAfG2tygk_89KbA5k87qWHDlffNU4dZB9iAh-CV4gSWtxejXyneJHeu-_XKhiHXiPH-MUjDsr2KHVNFxtzRUWhgnbgwz9uKLlnZhgPnKGGBiiy932W0Y_bbqGY5CZP7eYnUyf4YQIdK0O3foWe9ccvztyQGk_GxTDQ7lNdo2gJoggOLIRh-NzUpIk890PNPCXPViAizrWGGCM9gkBppytNek29h_tq3JBOac-wVjwLSAUCmf6aRja2kHnYySfEgD1HaRn-QHM8mX9pxgM81n3zBm2IYhqWj4EaiVsy9odA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فلوریان پلتنبرگ:
نیوکاسل با فرایبورگ به توافق کامل رسید تا یوهان مانزامبی را با 60 میلیون یورو جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99174" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99173" target="_blank">📅 13:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO8MDZO1so6XECvx_J5Ls3chM2P2-el3-03APGvT_4FGHTExFaXaNcE-lsT0YVw5pZ8QNidbsVfwaYDI-Zro_sLxFWCwG6u0fgjoxF8yt6M05Lklkt3GRbzKHNYkox8v_erU_v8AURpzzyku_Am0DlTUPTqACa9g1xKK6atQR-LPF0FR3vZAhdjvRGsDwAnaYrxOBD1Hmj-HnPO_dZKGyXXtnCIW_I08Jb1tp06J9ZlyuG3Ocoq_wxEH73x4Eb_jGQsjaITLecgrD8elPV45hxmQkZmR9N_DYoW0-wx_6ZuG8mjFZPgl1gCeKsN5xJk-haR9jiImZVz738ZdCZe5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بهترین ترکیب فعلی جام‌جهانی فوتبال تا پایان مرحله ⅛نهایی با حضور علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99172" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99171" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=LddNUsz-GSgsJB1LNMbUJAB99yZX3fxh8Yw86B4s3EYG7TzObDklB1ZD4CGGXIyfpnqY2_qV0nNAIqEFwVkoiiTsDq4XjEQIIRuyVTKa0vkuuB0AfNPw9jDDo3dLrQ7YoZy7kFEZkJWZyb17dp3T5LHmaXV9c66GM1x1I89_IwJUWH0sFtnOBzTxIeOINiTZGi_1g7NKlDE4hT74WqrZd0ynFFlU--2QgxfB9qi675jyaxKvYOzASDgkNUL9aVHNmCa_H_pOwb1TgzI7pyXfPBpH1RyAK_-kpqgEk2Iql27r5ELK2yT2qstCMJy_ZMHNWboTa6WsYAbcPVMbIUeBtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=LddNUsz-GSgsJB1LNMbUJAB99yZX3fxh8Yw86B4s3EYG7TzObDklB1ZD4CGGXIyfpnqY2_qV0nNAIqEFwVkoiiTsDq4XjEQIIRuyVTKa0vkuuB0AfNPw9jDDo3dLrQ7YoZy7kFEZkJWZyb17dp3T5LHmaXV9c66GM1x1I89_IwJUWH0sFtnOBzTxIeOINiTZGi_1g7NKlDE4hT74WqrZd0ynFFlU--2QgxfB9qi675jyaxKvYOzASDgkNUL9aVHNmCa_H_pOwb1TgzI7pyXfPBpH1RyAK_-kpqgEk2Iql27r5ELK2yT2qstCMJy_ZMHNWboTa6WsYAbcPVMbIUeBtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👀
هواداران اسپانیا در آستانه بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99170" target="_blank">📅 13:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=LYlhaDZbOAiNyq_-UepdZ9ZuEupwrs00eNXg8r22HhdqHi-kNKA3oIxZgxMgpA6MGU3rfdceB_v1Y-5gDbLEeJuCOgQLE54LouuB6awbPS1JI9TuXIUijdTrD_cDe-zUnYs-0-DZU5PKEmkpeQZVoBV_p2TS4xQTzpMGTZNpfPSh2CWFoZH5BMwvZASgbrDVpUwU4RXfaaw9dzvQ-LQWCsVX3T2wjlruMCTZ1q5mvPEh2cZhBC37xdc48li5Jg1KPScYQzSkKRcuxJmapAYEwLWCFYlQA8yL08W28cBJWJ5GWiJRya5e2IEEjp6lOPUNOlViza24PJI5nxp4K6OWuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=LYlhaDZbOAiNyq_-UepdZ9ZuEupwrs00eNXg8r22HhdqHi-kNKA3oIxZgxMgpA6MGU3rfdceB_v1Y-5gDbLEeJuCOgQLE54LouuB6awbPS1JI9TuXIUijdTrD_cDe-zUnYs-0-DZU5PKEmkpeQZVoBV_p2TS4xQTzpMGTZNpfPSh2CWFoZH5BMwvZASgbrDVpUwU4RXfaaw9dzvQ-LQWCsVX3T2wjlruMCTZ1q5mvPEh2cZhBC37xdc48li5Jg1KPScYQzSkKRcuxJmapAYEwLWCFYlQA8yL08W28cBJWJ5GWiJRya5e2IEEjp6lOPUNOlViza24PJI5nxp4K6OWuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه‌ورود ژابی‌آلونسو به لندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99169" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFut2In7MkEv5qceCklSOvHKRa2IiHU4eqaMc4aK0VN5zQ3sTAjEwxnEPFPl_gg7JVfLv4TXxJBvod0basrwTrZZVWoM3VbUwyB5rWT2gd3g3lZpYalHjmibi2Qu-PpdrUwLR4UeblTgI3wGMiezpG8_8uJc9yFKPW9DgCHHviZB4wsf2qTguus5CTAuMbr8p3hsV1PoIy_rzRh0GnBq1Rmrq1a9Ys6ctylxgQScyG3FkzZfo8Q6S-LOmi7giBfn8rJmC2fIs5W07K01Yu6nopmHL6kOHrD0a1tD650kWmLuflgAofuT5DqTPjC-tERC1L_NKIKhWV6YvyZ8uVJF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
🏆
کولینا رئیس کمیته داوران فیفا خطاب به اعضای تیم‌ملی مصر: پذیرش شکست از اصول اخلاق در ورزش است و هیچکس نباید داوران را مقصر باخت خود نشان دهد.‌ تیم داوری بازی آرژانتین و مصر کاملا عالی قضاوت کردند و از آنها سپاسگزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99168" target="_blank">📅 13:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99167" target="_blank">📅 13:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99166">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEtjosDN53JOYDHhwe7UHCbQdWWVKbXW5D9QYgQwFAW2oKzaRJsYtpkJct-kgSYirfpVYNvq6ruoXvi5jkragE2V0f4VrWcalkZFMWOXDBX4EtVoQFnTbMCQ3w2iVFujAZocaJzf2cmtIxPzip8B_5d95AnQkIM2VMLEeJ13fWySv3K4OmIv75wwe0ujO5rxMZXUwRZFArB00PFAl5OuvuN7JxxecxmhAWJnKWryYtFxkEKFyb7782B85abHGFt5ePJ8gIPzh5DnoZ_NMItj4yhgBHUxnTBTHVWqFo4ij1kfFx8zVoIgJuLdrMCTHy1790OfKbdNzgR4UNddaZ_sjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99166" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99165">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdksigObukHOv1xAhZMg7XJTsxTmVrb5CyBmoCud8-fFjkzgt5vK062pdREwiwk88EULBGPrKvwd6lvJsMfHq0biLBkN3cyW6qFm1LhcDgSpZWm4pgsReV2vmuEe_9MelJbXUJX_3BIEi-MYMrr422iIuM6yMJ-nhHrlVibmIpn2OU0zoGKy3jxql5xQGZ6X0HEUMl2pWweDwzaM3u6rZ0nqIe67zw770ZQXnO8zjV9x7xwnFYCtz_fBijEFdpe-n63ZOar1RKJyyQpKE5WRAf449sYFdHX8fllKySKwgoptaj94X720UDTgFSCCz0G_HUxdMm8jxyACd6CCDIeytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
هشت‌تیم برتر جام‌جهانی از دوره 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99165" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووری
؛ اخبار غیررسمی از شنیده شدن صدای انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99164" target="_blank">📅 12:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇵🇹
این ویدیو یه کم حجمش زیاده ولی ارزش دیدن داره؛ تو این ویدیو به وضوح یه تفاوت جالبی رو ما میبینیم؛ کنار مسی، هم‌تیمی‌هایی که همیشه پشت کاپیتانشون هستن و تحت هر شرایطی واسش سنگ تموم میذارن در سمت دیگه، رونالدو که حداقل در این تصاویر، تنهاتر به نظر میرسه و آدم احساس میکنه فاصله زیادی بین او و هم‌تیمی‌هاش وجود داره. دلیلش رو نمیدونم چیه از شرایط تیم گرفته تا تفاوت شخصیت‌ دو بازیکن، اما یه چیز قابل انکار نیست: کریس در پرتغال اغلب تنها دیده میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99163" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99162">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=eMFn42NZNkmLQZad0oNozgQQtO2gwXnoAVJpI45McZGWfHm1VWvAgeE3670MOe4WUMTVWb-tl5egQL1pCdKTIseaoquhuNP8TYCILYYZXSspvhqSiGHmkXp5LLfGzzu8ZjCIOF82PGK-mecnG5VTXEiXHs2Epa-bYUjbZbqW-MJa8KGu3Fe2CDfqmOKVfw2OxNzwhZJ6IML8PsL6eU3n5ydDwOJY3BQLTx9PpsA9ofVBGFZ67cezzq0aRuiT-FFW2zDr5CdzVDyaLwyqDUn7A_4F5IPTrvETJ-3KbNZQ7_z-6x4rMHZUUItKsohDO2DHHjlCqIRh_2QVf3RM4U9g2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=eMFn42NZNkmLQZad0oNozgQQtO2gwXnoAVJpI45McZGWfHm1VWvAgeE3670MOe4WUMTVWb-tl5egQL1pCdKTIseaoquhuNP8TYCILYYZXSspvhqSiGHmkXp5LLfGzzu8ZjCIOF82PGK-mecnG5VTXEiXHs2Epa-bYUjbZbqW-MJa8KGu3Fe2CDfqmOKVfw2OxNzwhZJ6IML8PsL6eU3n5ydDwOJY3BQLTx9PpsA9ofVBGFZ67cezzq0aRuiT-FFW2zDr5CdzVDyaLwyqDUn7A_4F5IPTrvETJ-3KbNZQ7_z-6x4rMHZUUItKsohDO2DHHjlCqIRh_2QVf3RM4U9g2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط کنفرانس مطبوعاتی براهیم دیاز دو تا از خبرنگارا دعوا کردن و کنفرانس متوقف شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99162" target="_blank">📅 12:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99161">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3DAuB5hJjCmFfefXL3-oZ5cOSG_voJtBNJwBbwfnX1cQgKNoYTNkC95lTbY77TBU1Y_m9hMwwlYOyZyhEH5QWoG2TGb_UK8nNj9Mj-WSz7HTnmMpBUHPACjEgQ2Hh05VShQbY083cD64PR1dmK8J_nj4zj5BPg-66ANgoU0Adk71QeqyjzkjkwHUBX5noxde51JOrZ9TSOk0YCMPkVPWg2OTQ_wGPvJW_X9FTqqqxJ8NtVGTqn4l1cqajIcIypXtJRBi0_hrHF1vl9UqQLz8_EIaxtEDqLczv4ZesoE4qtbhwDz0XOjOdUg7AIgBzVSBf8HzgPR1_3jXcDdc0Lqx3EE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3DAuB5hJjCmFfefXL3-oZ5cOSG_voJtBNJwBbwfnX1cQgKNoYTNkC95lTbY77TBU1Y_m9hMwwlYOyZyhEH5QWoG2TGb_UK8nNj9Mj-WSz7HTnmMpBUHPACjEgQ2Hh05VShQbY083cD64PR1dmK8J_nj4zj5BPg-66ANgoU0Adk71QeqyjzkjkwHUBX5noxde51JOrZ9TSOk0YCMPkVPWg2OTQ_wGPvJW_X9FTqqqxJ8NtVGTqn4l1cqajIcIypXtJRBi0_hrHF1vl9UqQLz8_EIaxtEDqLczv4ZesoE4qtbhwDz0XOjOdUg7AIgBzVSBf8HzgPR1_3jXcDdc0Lqx3EE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
Maradona.
🇦🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99161" target="_blank">📅 12:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99160">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=nHzj9Ooa6EhAgkAgVzXJiPtG5SaK9GEvDhA8IPhnoIyBq4sQE5DaHlnYXM9wv-8kUt-2WRbsagIL9T_HYYT21QXpo4VD_eBE4Apj_GH8vpSgXQ8ngOkJmo0QqfFhJfAf8w88ArwbRP15BSm1tQxbXL7kiPmT-9couz2umz3pk9Oe1_NspPwYhVWS76A9ccsP5-o1y5n9mMQhcHXuNF-XGcTKBphyNg5OUswhdgacQXgXo2fL1umqyHzB60bVv22zAJ3Mhcbaz5X96uZIbETj0C9bY7_HouSfL8MekBmJI1atol_3QvHQlLjBjhUFobck5dEk0ZZCiiWJK7UM0sarOrnYFp8qAxhSRcZzVaqEKWgBSUgNN7oORsaxO6BWl5XhZ_oG8vypBSOylLikL8GBuJihw3GXhoh_N0E8qC28ab1HhLlPYt6ikjN1nnuBfizsCIo86orP9_hjIh-_HD-xTOMRPIiggt-S-ncM4g2vwDQDpvs8Tvuv6PkmuAqw_8XJfBoi8RDP2twzZn0r-dkjDgLfAsck2FpSR3rJDdPiPU57BW2RDNj_D4l2wbn6MxhDD4XBBKdJhA3jnQIwnTGhv-UrK0AXCbyGgUmYLGWiNq8B3SIhYNy0jnKIxmCpuZY08ITS2N2G8HWh14wy5wRzt86engJOB1SkJy59skWgZlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=nHzj9Ooa6EhAgkAgVzXJiPtG5SaK9GEvDhA8IPhnoIyBq4sQE5DaHlnYXM9wv-8kUt-2WRbsagIL9T_HYYT21QXpo4VD_eBE4Apj_GH8vpSgXQ8ngOkJmo0QqfFhJfAf8w88ArwbRP15BSm1tQxbXL7kiPmT-9couz2umz3pk9Oe1_NspPwYhVWS76A9ccsP5-o1y5n9mMQhcHXuNF-XGcTKBphyNg5OUswhdgacQXgXo2fL1umqyHzB60bVv22zAJ3Mhcbaz5X96uZIbETj0C9bY7_HouSfL8MekBmJI1atol_3QvHQlLjBjhUFobck5dEk0ZZCiiWJK7UM0sarOrnYFp8qAxhSRcZzVaqEKWgBSUgNN7oORsaxO6BWl5XhZ_oG8vypBSOylLikL8GBuJihw3GXhoh_N0E8qC28ab1HhLlPYt6ikjN1nnuBfizsCIo86orP9_hjIh-_HD-xTOMRPIiggt-S-ncM4g2vwDQDpvs8Tvuv6PkmuAqw_8XJfBoi8RDP2twzZn0r-dkjDgLfAsck2FpSR3rJDdPiPU57BW2RDNj_D4l2wbn6MxhDD4XBBKdJhA3jnQIwnTGhv-UrK0AXCbyGgUmYLGWiNq8B3SIhYNy0jnKIxmCpuZY08ITS2N2G8HWh14wy5wRzt86engJOB1SkJy59skWgZlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
احتمالا بهترین تیم‌ملی تاریخ ایران :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99160" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99159">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=uqnXq8pkrg7vhlfwKNp1KroaprWt99glDvim7hXEFcMqU2NGMU5sewobCN4RxvI23DPcpppycRdqUDddbOX7311cppRE3sD1xy1e2H61aTWy6DCh3rn9N-oznVEE6SGDj0FTxwsjNzSH9B5b3kEl2eD7uNZrdYwb6W1QrM-MFO--mVCrggVozTfJfizr2UGW49qlBIctJJ5u9W2JbPbZmbo-XeZaCH28F_PCv71SmfKJukEAORS8sPrgo0HVGnlEUizkBReLvA9cHXCSPFy0XtHcwu3xajUaQRKcfAV9t1x8suDTQbLe-qDAcvaqwnbrfIQfrdQPxqQTixJxVfbwDqZ9wdoShFiKB_7C0D635INhegaSh1DTroevPthdkSwKvX762Zt9uOvuUBG1q0ul912LJWreUBPiuPUI4drL7bAi0AaZ9JsadeDR5HOABgLn7kPATc8lccjjR73tzXgE-_56W5Ac-TTvbwex4O_I2KyvH6lgymCCk5L4JQ1WVSbbZF1aKyNeb8Rhsu8nuyiY2fForSCm_HAqV2vI1VbWrXs26CjoLj4JVa8-WtFba8vtJNOkYjefaWG2-kdjWBur2bKjXFBxh6k1ETTAfY-caryICN3vfxK9mjSd5tiGehPYFAe6b0EHJT0bW3vxfaodbS49ximpMBKtUNqW5dixLeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=uqnXq8pkrg7vhlfwKNp1KroaprWt99glDvim7hXEFcMqU2NGMU5sewobCN4RxvI23DPcpppycRdqUDddbOX7311cppRE3sD1xy1e2H61aTWy6DCh3rn9N-oznVEE6SGDj0FTxwsjNzSH9B5b3kEl2eD7uNZrdYwb6W1QrM-MFO--mVCrggVozTfJfizr2UGW49qlBIctJJ5u9W2JbPbZmbo-XeZaCH28F_PCv71SmfKJukEAORS8sPrgo0HVGnlEUizkBReLvA9cHXCSPFy0XtHcwu3xajUaQRKcfAV9t1x8suDTQbLe-qDAcvaqwnbrfIQfrdQPxqQTixJxVfbwDqZ9wdoShFiKB_7C0D635INhegaSh1DTroevPthdkSwKvX762Zt9uOvuUBG1q0ul912LJWreUBPiuPUI4drL7bAi0AaZ9JsadeDR5HOABgLn7kPATc8lccjjR73tzXgE-_56W5Ac-TTvbwex4O_I2KyvH6lgymCCk5L4JQ1WVSbbZF1aKyNeb8Rhsu8nuyiY2fForSCm_HAqV2vI1VbWrXs26CjoLj4JVa8-WtFba8vtJNOkYjefaWG2-kdjWBur2bKjXFBxh6k1ETTAfY-caryICN3vfxK9mjSd5tiGehPYFAe6b0EHJT0bW3vxfaodbS49ximpMBKtUNqW5dixLeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
فینال جام‌جهانی ۱۹۹۴ میان برزیل و ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99159" target="_blank">📅 12:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99158">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99158" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99157">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiSWWj9e2lsmyl-ASfbELmGJSODCOFMrCtBKSlOdEoO8u-nmCKpdaB6NZ0VjYloG0HmZw-HKsxskIposSp2j539UA6-9nXCWy7R8TdcrrqmduvbIcQg51JhQRVrPjmFh5N3Cit9mSs63eRM08yn93Fa51_AmcVnT40fvzs71rfy5-VDT3kUkTGb3Fl4b_ZbT6hZ8_rHeh8cSU5jwtJPyn-eA6wf6T0kkJBIABJ52i2tOr8wzZcLO534_xZTLRH8RtSyyb7YQtNGmdKeN8tNiAHXU0shKvDpwf_TsXvk_2SJT0Lm0uOc9K75k4qrb3Nrz8OI0zahYIdAZF9k5Vr5Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
❌
#فوووووری
؛ اسماعیل سایباری ستاره مراکش بدلیل مصدومیت امشب جلو فرانسه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99157" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99156">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99156" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=G3-wBa6XK7_zjOokDAZq9IqLapwoSCeB0KDuAQWcIzjxV2B3_PAwzZjZctxKgcLpTukWQHdzHheuegcObNwucyOiAw4pvwGEnypddhLNhlWogwHYIJsVO---0zvaZnD7qjWd7CHqV2ST37fZ-pKXqPL6RG4aDOK_BIwyRBvnoAhn6aFy_kSiTsFfp_465GkR4Zea3C3M-6rts1e-n5bbO09vD-Qr2GJj6J00JxZm6p7QCWqC8qFJesaNJum4l4_zIQJRtPi9MaX7-6GtvQz3cVtNaLa1zb3WP54Ir53G-AD6oPPDcNbB3Bb-qxon8StLA_7VOT5_fI2ooF7gDD4-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=G3-wBa6XK7_zjOokDAZq9IqLapwoSCeB0KDuAQWcIzjxV2B3_PAwzZjZctxKgcLpTukWQHdzHheuegcObNwucyOiAw4pvwGEnypddhLNhlWogwHYIJsVO---0zvaZnD7qjWd7CHqV2ST37fZ-pKXqPL6RG4aDOK_BIwyRBvnoAhn6aFy_kSiTsFfp_465GkR4Zea3C3M-6rts1e-n5bbO09vD-Qr2GJj6J00JxZm6p7QCWqC8qFJesaNJum4l4_zIQJRtPi9MaX7-6GtvQz3cVtNaLa1zb3WP54Ir53G-AD6oPPDcNbB3Bb-qxon8StLA_7VOT5_fI2ooF7gDD4-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇷
🇪🇬
حرکت زشت و تحریک‌آمیز بازیکن آرژانتین در مقابل چشمان محمد صلاح!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99154" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=XBwLZkttXIhdGiB5JZGAWxfL0ws7jhS7AcnwClVa6v7FTPQwdilsxpkx7j0SU03yH9JHVuv3nC6ktN5DeMrpWKZaJ5LYMZPQ2C71sc_bJWxUQouGtasT8Ze1KhpLrh5XZSDAe6JtBTBhfSYTDCNzuEcL8lsVLhEwTniEpgSvaSyTWPmlG6R4AZ75GF2l1iNxUrZALh8Q2AA6OfaylGXjMCrc9j4ap4vLBjTyC8s6Q9OcuCYypHcs1t74V51bLJpToiCnVwEqZvojqQY_qODsNfpBGmBIlZPrpUoYcQZGLyW1nN4NBuZ3VvkareEa3OxNHjpwuu44Uw4Llbfh-3-cWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=XBwLZkttXIhdGiB5JZGAWxfL0ws7jhS7AcnwClVa6v7FTPQwdilsxpkx7j0SU03yH9JHVuv3nC6ktN5DeMrpWKZaJ5LYMZPQ2C71sc_bJWxUQouGtasT8Ze1KhpLrh5XZSDAe6JtBTBhfSYTDCNzuEcL8lsVLhEwTniEpgSvaSyTWPmlG6R4AZ75GF2l1iNxUrZALh8Q2AA6OfaylGXjMCrc9j4ap4vLBjTyC8s6Q9OcuCYypHcs1t74V51bLJpToiCnVwEqZvojqQY_qODsNfpBGmBIlZPrpUoYcQZGLyW1nN4NBuZ3VvkareEa3OxNHjpwuu44Uw4Llbfh-3-cWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو فنا در حال امضای قرارداد 10 ساله با تیم ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99153" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usqs3B4qnkEu54bA-f_2SSLIaCo-BgApxInH5jLcs64EYSNronS1MdYysmD5G2wCC2fuAa_X0l39ilUySlxJsOnGGjD4p9-bH8P7LNp7yaMD-wdgETicmuMgcgYczFeh1alIrZZJuOxX1iFZ30L_ys_UwmBallOYFpVUgFrj5YyvC02AAzBRnCIhIsdQMmYOiMmxR3izAdu4Mc0nBTXgSK_I7KIFY6zDwIKMGoxoMgob7KkvVgF48sHQzr9_PyR_UGKGxm5ILeXZKnRFDCw3aJEntzu4-LDkq4uMkLMfQnOByDDM80lkP4KlU9cgS7L_TneUzp5J3i6rn_cuYU7mRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
#فووووری
؛ هانس یواکیم واتسکه، رئیس باشگاه بوروسیا دورتموند:
"ارلینگ هالند علاقه زیادی به رئال مادرید دارد و این را پنهان نمی‌کند. به نظر من، او ظرف دو یا سه سال آینده در آنجا بازی خواهد کرد، نه الان، اما به زودی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99152" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKp-hTEOtJzWfTuQbHTi-SfRfK-fTWuqbYfq0VihbZ33yi0LiTsGMddgQOGDMFaZnHcXKlOjOyYwN68smQwOFJd9QYuJBmHmGzR2oi1BrwCJbUC6eLF847Y43jQfevbQBtFhkCfk5TlkPNkiOqRzli_8xe-k9YiYdRvysLduI7D5PyG_gf65mXiqLvwtZn-ktD47zn0jq0_3ZV5JV6y8XutknaY4n8bWKtrOcMvsjH2kJAzBOOFUVanDF4v6qz9xvYOX-6IBcr0c_tzCGsjc3gEL1xXnAJ8IdgB--x3H-vHVb9iXF7PqRd-vt6ybcgrPGa56OjoJ8hbbyWtLlRuA9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— نیکولا شیرا:
- باشگاه آرسنال و برونو گیمارئش به توافق کامل در مورد شرایط شخصی رسیده‌اند. قرارداد پیشنهادی تا تابستان سال 2031 اعتبار خواهد داشت.
🔥
󐁧󐁢󐁥󐁮󐁧󐁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99151" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تنها چند ساعت تا بازی مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99150" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔥
مرور ده سوپرگل تاریخ مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99149" target="_blank">📅 10:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=CxJYOnzJTr-jjK7rMc0g8y4yAHbCnYfj99CXibYxPeU3W6TcnSbGA5cjLU-nh4HpAF54Z6Kcj2jaXe4vIP1gttuyVO1JOgfHqY5kzydQ8d5KQRNTXusqLupjoKdO2sOX0tv9o0nDEryl9pbX9-VpOIadDEKWaK1mu3AkHpVjsqBqYb4w7r4od81DalvjJHlUKER-sUI_eO8rFjE98MQ-DuxQaUPoQkkH736mxiRROwNMtbfpMgAgahBvs2z3_rjLBfunYz6nd84cJZ6qWoS0kZ53X_xcU4rs4NKvZrUax-bcKnCQDLKBdwcUM_qXwwr5IeTvMFDbYnl0fRbLjFkhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=CxJYOnzJTr-jjK7rMc0g8y4yAHbCnYfj99CXibYxPeU3W6TcnSbGA5cjLU-nh4HpAF54Z6Kcj2jaXe4vIP1gttuyVO1JOgfHqY5kzydQ8d5KQRNTXusqLupjoKdO2sOX0tv9o0nDEryl9pbX9-VpOIadDEKWaK1mu3AkHpVjsqBqYb4w7r4od81DalvjJHlUKER-sUI_eO8rFjE98MQ-DuxQaUPoQkkH736mxiRROwNMtbfpMgAgahBvs2z3_rjLBfunYz6nd84cJZ6qWoS0kZ53X_xcU4rs4NKvZrUax-bcKnCQDLKBdwcUM_qXwwr5IeTvMFDbYnl0fRbLjFkhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آنچه در بازی آرژانتین - مصر رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99148" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeiCaD0H3-_eGmicVFYtM5kgwKpqmCLjTI-1PLl3GEorgLzuv1najLZcuEtYos_HcpYdzAuoXJ57f-0GXbq5908eyDEh_wzB9r0Dsj1pFWAbfKN0Z5oQyabieKbpIpmSQfM7AzTvecJIu_UWxVQGCxfvivBcvAABLf4JnmkL7kp_66T0BaXmJS89UGl0kf6SQfYU9El5GutxOd0EYB8JZeUrc3PVN8TpQ6WIE9Ctb1cL0EYOofP2zJLgkmbcrFZ19wskgpnQsFr1SakyhLT464nFNExSXd0SU7S7Vzn-iOvgTMqgvTj3C5NT_M1zDMB6qzGtArB4Y_Ae-bSChYOVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99147" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=Nk5qduerDOM3CZ4leOBSuNbd-cvo2H5xs_-St7tE0FcveN5GS7Hzqs7b9neVg4H7h6fO67hi2oYR_bKRZAklVoDwW2I3ae2rPMnlpDLCxiirGnQK44HIGf9cYHqg3Z-ERLgTwecl8hAHMtN64P2DE40CEOa3005aPjgAxeKrmr3xZW30ExHM61hzVCrW9XK8FvAP8ewUr5iIu5ACXkyuia1iVjx8hkKFFCODKsCcVfw8IJfY0kpWngiqPHMNxXajOyh51k-G91pJVsV7x4Vf0CM9lV67i0HRPkyvyLsNiv9QhpiIPct6McPcGqZrVhna4yBk9NxBNUiSXqd9h6imqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=Nk5qduerDOM3CZ4leOBSuNbd-cvo2H5xs_-St7tE0FcveN5GS7Hzqs7b9neVg4H7h6fO67hi2oYR_bKRZAklVoDwW2I3ae2rPMnlpDLCxiirGnQK44HIGf9cYHqg3Z-ERLgTwecl8hAHMtN64P2DE40CEOa3005aPjgAxeKrmr3xZW30ExHM61hzVCrW9XK8FvAP8ewUr5iIu5ACXkyuia1iVjx8hkKFFCODKsCcVfw8IJfY0kpWngiqPHMNxXajOyh51k-G91pJVsV7x4Vf0CM9lV67i0HRPkyvyLsNiv9QhpiIPct6McPcGqZrVhna4yBk9NxBNUiSXqd9h6imqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
شادی عجیب و غریب خانواده آرژانتینی بعد گل‌ سوم و برتری مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99146" target="_blank">📅 09:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=GA7vCUKonOx-XRgzyMo3nI0nrvhtoZ9usmXp_NeZtr1Q4bmXfvyhpVzo3emYQagh3AvO7yizeTcBMvYwmWPOYNlSKGnNWSDsr0CSa-RLyPBaALyDy0bWOtTCsmwNZF5Up7PEl7n2q6Fs7_gSQoOBG9UCejk0Po6rJ9QLa8FLLZvgiKXqn6n9eZ4w8GAJQozq-MHq4c-BfjHuuBF5JCoY9koqDYWaNUqZi_bAn7h4KMQJ4r6x2T1YjL7quoAdZnAhPFi4xosU9jNaKZ3KILLNeVQK-VvboNjJl_UcEjUVt3t3nJomN1u5-JZUEkXg9KkkZ5qX-LPdKgTujLuSnSku4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=GA7vCUKonOx-XRgzyMo3nI0nrvhtoZ9usmXp_NeZtr1Q4bmXfvyhpVzo3emYQagh3AvO7yizeTcBMvYwmWPOYNlSKGnNWSDsr0CSa-RLyPBaALyDy0bWOtTCsmwNZF5Up7PEl7n2q6Fs7_gSQoOBG9UCejk0Po6rJ9QLa8FLLZvgiKXqn6n9eZ4w8GAJQozq-MHq4c-BfjHuuBF5JCoY9koqDYWaNUqZi_bAn7h4KMQJ4r6x2T1YjL7quoAdZnAhPFi4xosU9jNaKZ3KILLNeVQK-VvboNjJl_UcEjUVt3t3nJomN1u5-JZUEkXg9KkkZ5qX-LPdKgTujLuSnSku4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباهات مشکوک داور بازی کلمبیا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99145" target="_blank">📅 09:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnRmVx8GLiQojJxDEoLQwV9USYRs6ns_NDnXe_XrSVT8LDuQX8RLoldUjtSIM946PUQ2ZBDqgamaLU5YXeeDcUjkbAe6GFonv4nGAdKwBZoMAZkWz_y4LUCQi9om0u-GKOw7-FgQiWMDP--uzNaIz82HdXDi1ps9rrOvzGED-F75o9Kqt6g9lq5wX9SStwjZUcRQiVOso1vL-SQU0xFmtrbyJS_LoQZcZK29lfiUFXHPBUaes-Q3QcBN5o0rQAPDRlehBvOYpKL0iHp9-vGiN_-FckMWTKub9Ez2b3KKG317QL0yizfqn3FcRcNPYCbH5-nZdcD_AlyDFaWeiRnNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgdBenG_RFOxxMoVnaAbsomZzxVjX51XDT3SgeV6C2CSd5XCHyiRNDmMkKuJplhG7yeWIy7LNRktSet1rNwMccOvOfgE4WaqrLGCmKFXe4rzWjpD4ALb1dsYD-gCO3jKmFY8WxwCn4UOr4U9u0ccx2a5mpq2gUlXCX29t2i7GbXLy9nwVXH7IoYC9fg7Q4UQ-NqCE2ecv6BzQWsNFwsw3ns4VkZYrjODpZ6FHjZOKH4xpuZHQWd5FSzVS90YZq8qYStJFUw1SaT3yVfRGgR6zii06ih6lNxUniBszbMd1JiGbtBwm12a6k3ULk_cA8kxW9iL9pKd42_kKyTqmLk-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=B2h4ePsehOlOj3rzsotmhvJ2DtieHYlqWEvLG2yq11z6cdiZYMu-8ydq__ZuwlSslW-D-u39LX2v7Xiro5j8OeYPIXIpOdqunFkBTeYuA5gBXY7tqIDxyOKjClNCkDiI4uOI9G4HZQKev1ZUQBLEIMyVghzU-2deurIRBsJA9swkmHtNxsr0QhoiZUflPGR_YWrSoryWdNy16CSvXpeVestJxp9jzHqcHSa00D9XNypkXs0l7yTOtfbYlSQybFCIDHoHWWT9-ojrt0Bb8NyhjXBg4qoCVY8LWY6ID_-GBv89HqHdP0cWd-URYTF6DVaLI0cjvJtT1dlGkPxU0nsjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=B2h4ePsehOlOj3rzsotmhvJ2DtieHYlqWEvLG2yq11z6cdiZYMu-8ydq__ZuwlSslW-D-u39LX2v7Xiro5j8OeYPIXIpOdqunFkBTeYuA5gBXY7tqIDxyOKjClNCkDiI4uOI9G4HZQKev1ZUQBLEIMyVghzU-2deurIRBsJA9swkmHtNxsr0QhoiZUflPGR_YWrSoryWdNy16CSvXpeVestJxp9jzHqcHSa00D9XNypkXs0l7yTOtfbYlSQybFCIDHoHWWT9-ojrt0Bb8NyhjXBg4qoCVY8LWY6ID_-GBv89HqHdP0cWd-URYTF6DVaLI0cjvJtT1dlGkPxU0nsjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
