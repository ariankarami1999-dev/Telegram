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
<img src="https://cdn5.telesco.pe/file/ATROMVnxPMC5NtpmvHo4fvTSBY27R_jgdJyJxdRwHbjyGUIcdzJTyQS2d8yfyU5wdgM-ur0Ny5X4w9Oa_xzB79xZTE1umRa3Mezmo5wJo-9q-cLWkXr9pG8RtAAWtUVrnSDwye1D7tTFz0qS2LxQ6Q49d2AqYCNS0Lgn6vDGhje3vY6AsbnWTrMTvquWbMwCn5_XDQgleoZy1P04-3YTsFZZnJQkybScxHjrRLTju098meOPOQo7clwLBU5j9p-g5u7MLpr22ltQfydPUUcwvzjVWdgNMfOJOK9KCJE2DL2vii1G_dvBZ_WZHnV7Nf1jny7uP3lDrkokqL5QPMG0RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 588K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 23:32:14</div>
<hr>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUOuE7476kx5iUywdVAS8yz1rlfqJNpxg_ihw1cegi1DOuMzomljxaCXuLuGz2RuNg-cPomgacYtXdxmh8qHoYZ0scwh_3jeMulS5KAw15JUjhN-o4mTJtitxPxJ5jhmClNyvD0aQ2Pyfx965l-fJn9C44nrQzYIvxaL5xNM3P6N0jNgu38AeAHBCBG1QyPSBBlJHLv637q5PyCZrHkJn1my97DDvZyrztYZA5TOSfvpJfPyz8TIolMmP-QmyNcZR95OUPWBMr7mzxQ1xyI7gMZlolgsz8TSzkl7IiyziEFbsosJy49pbKh1hjPjb4g4pMSPQ4kvPNRFcuo2uSW0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZGV7sLR0FQ_SPQmGCtaUJZ0xR5dT38I-dKRm8_Ch6PZjiG1j2JTSGlBDGWLNj78ZnY6z1VvP1v6Bt9kg2QXqcxF1_MZKNz2D5f3x7u1tQQ4OTYWO_JXiyH0RIi4quacsZeAvEqpq2S8In0UupZIcylToRm5RdvGckO5hMd8OxTOdZR-Y6TuaPvsjG6_p79VGV-6F0sCDLOXx9yCQrCkJUV3iC8i0QCxUdQVUAEKBCraeeABJS4azO2gj6B-C7JWCgyYefUl3-lMTvVi-_Wy3pUdc8eTXlpAPJ9xEXb9yV-8cxnOe0y2KfXdOOguVkwwxYU2vWwTQHl2KbYgIHw3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFNbMsVbgRJMKG_Yei0rq_dc3IdeKYkR4EbPd5opsSKyQkriH5dSxkVQJIiasE1VFdgHFrbCNbA9OTgsdGnQ8mFmUjFDSxfvcNHyuOTh8ZvtQ1BBfd-1DwVBRSk-ascj5-g50Iiy1Nl5UwGA3v7a5-mmokV_Pn0ItPKUcD4MbjjeOjoSpZV2CSBuCCv0-jFoF3j06dv6EfjEMSc_-cW8xXApsmECEpHajxiOxsTPiijz1g4nzXzhvS7Vplq5Ki9e-O6g2X9d3cs74fdJrrLn2rINvLABxJ8mSBtx30CRtSZvWcF9OQB53YWWNTxZado0UVzPOJCTXOHTli_PO5vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCW3SwoacmvGhdWUf8ujg3zvCq1ZuB4ATgzHm6XW71ILKNEkJj92oYeloPzWZ8zSo_hJ3yIRfteYQcfdZmd_eYvdhKnRWvQLsXh23GTTeBGXccmntz0S00xvaacq-LubiRSwWJ7MxU0LOQxKEElgdl02rbs9N51_bZfYSVxfQwmT2-dezcMeMkMhCqBFzhT_n2VVewB48-swSqyt-P78jiGOdD6cqDeFKx30T3r-iA_S6Wdtgl8Eg5ne4g5T69HVOxxzi38eBCC4twSdlXE41rme53S7ulUoyboIFIJ2a2Os7yga5Jbbq3a8Agi4nwEOzHGjCZjb8aQud8NGAG178g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INaOaXen6rzDBx4u5sycL3sTbu0JGyQvoEBZRt9PjrA44RqNcadAAdA4NJxvoR2lxrEPgla8DsRS_e0yOtOgamlONvOzC7LuMPcdBgQprOC7gRmN4D1v-kk3fL8VArzbsVmnz8Zt5iP3dyKW_6YG8IdarqNDHcxB_6LvifVTBd2GniUCigYJTyaY_wqRFXm8L-2Deo4U9vJtdQEZbaAPmH_tKJDuKDzZHB5eW3ApMqznBlnfChndtpaeWKGkqpJ40AF6a9WydSbhdF27IjsxwKS6zT7pQ_fx_akVLIxsikx5RyzYWImYLgQTfEreNIoPt4MnYzRatiyukbjyklve9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRAbLmT4ICBZT4Fj8dve-AyDkEJJ_jrtwqDiX0szsXnXArMhmramo6ImUUj_pHolSWUDmUW06VQuAAq6FEns_stejx3IF8I4XKYGsW3CtgSQbXlrg4V5n-SS7Ftt0fIOeuZEfQja4zb1-mK7nxLB0DnJXK924BHhbGtML45T81gNhCrCyRbFrD3NQVoadOthvFMxytWP8PAQ-_u3wWRfK_usx-ytg-IVgZZQphCFlveOBQNpYeBN0tSuP26Oo2e_Gms5BOlz2TZmV0hjhcVpNmK3dkIsxm02rBuQX_-aJr-EVwj968AOuLNLcN_qhViBJMSHr9nkNMrInY6ncqpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1daixLyqf8gB16zaj5R8bcpDDiN1_i6SQgQAmD1alzN44DkxUoe9JIWxgA7HL3w5hGQPvqjsUjO6-C7vwWs9V5Z0TNe_l7ZS9JIlenef2fl5s9VJKnQmK8Ygh_8lF5DDyrvMKwZGizxj3jAmKogzI0d5IO8pjXBvGCwsBfIy_VxajCJ6WqljYu6it1ZqH-YalOP24Lp-by6qcGLMxdRr3GPUbODywTd6yJak5NOuCb5nq-4OEIcdLyctVCEVbOAIxg3Bbd8RS3oesIUqJI0gfUvZYujlVUzJbbOTaXKF6CVObwdGVyjPHx9A2173jCZr6zUeRGoBkgvu8SB9oOclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MouxN2bbdCHnAeTpTHZQPKSKNERHWyoWb7jjv8Df4Z4Gd1q2XcROIi_8FRMzza_ADXnwdoDDSs2h29SV89_p4q69EW3I-IsqWinCFRvuXrO3cbhezv0jw1Yin86MdgExX1aSSwqTKFYboEwX3JmEggzUFQgMePuiWqQFxSzgtd9-70wgIMVcbPHC7aP5gi1ScMeO5obRNlBaX_mOhRRrD-057kI_xwX1zIoWbskKr1NmFknVlhxzxC7ciQm8qngjdeDQowYiA3LHxqs9N38wFUgvNHg3a0PMSYYofNSgvhY1FkpWSrBPxj1mQTFHOFBSoyRgXVai3uH1BaT4uZR-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
#فوووووری
رومانو: فران‌تورس علاقه‌ای به تمدید قرارداد با بارسلونا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99855" target="_blank">📅 21:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwIUcETHtMaoc7paj7reqbRmzboUMdJDenBrKrpj9ihmQgGTRS44nRoIdf_3UOdFt3eQNVraJS3HXKsUXs4YBNr5yNCJir6z4eGvsGeY6BWJUvd43IL_-NCp8k5Ecj0qrGNm7S8ZimjD5Hdv91BoqKXWF-tFMmvv1mmVNtW-njyD-up8F9iXeTZmptjrsaew2CWknXRLM7JDCU5JoxLO2K3LG66T02VRp8QVN3xXPLMf3MlLp45fmXQuIKEIJLyE_MJ1HtVuTlaRDNHYhjEcPj0YJAxlqbFY72zpr6yPQKSjTMabIGe34bJjYuJU3CzRtODDw7wjf0SpzHdc9tPmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#
فوری
؛ رومانو: میسون گرینوود در آستانه عقد قرارداد با فنرباغچه ترکیه قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99854" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMmrLamz2PKKDv8mE2pa7A5jpPGPh3tm90Bs6-k97q4lTEtdfBkvvlB4pFlNKe5nyncvf2Df4ewf9x1BGSFXYvavtoPHYEiP7cxV54ysR54h3_P-Ve1YZnUnwTUvqo8VAzDLGD-Gg7UpbgPWvRVdKR-YHTcXBeSjyFXh9pEyaffLJ142iK1YzFX_5-bT4jsw8fCB3VGK2Eh2_-T4nPeBONKIuklblStLpUTzhEUJERD6QY5Vp1tg9BQY4mrofrqQPeGwhsOAlYa-jDX9efB3tKKI_S70amZE0LPTksyDsrsXJW-eBUgQkMjps2t4cewT3X24Ar3pgTfhRj6ndv56JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWVoXIpD-fGti9Z96FWqtCeMaSEQiQP_4SKqgY_aOnQiYqfjgXKS9vWvA2oNKa19KOe7WxRYuUG1xkl2go_0NlD1cwIPk3OigstvMfgjGQpjdGOhv5o9Jc0XAAJ6ifSZPXbLPOJnwBCg1VCBdIJw-oq8N5XzVLevA_Iy08iFdyhqYO2JuYUS1-0nCjuoS-iNyOBaHsgtwEcNCnPI0MQe-5vrjydc3dIKrlu9b7d6ZyL3P_81MI8CjbZucyTt9R4SDnCqQLc8oTOIHL6e2nG6_OlOEBiErrgh_H4BrXDTB3L6XFmCUmmXoA8ClbQPwdcVZ0qKKf9Jn4zzmPGKGHipMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSXcpr0bSEMt2DeWHMQJpHB7PbpuuKUnw4OeCGeOHg7do7qLCxu5bLuxX9u4joipo6pHgA4JDTQ0sD_jFDP6dykU_3kalky97zKRLZp_fKlMKGcnACeZ5lVyTMyKxDb7DzXprEQ3TrIHvTSEjArrrmTGWSEPIacYhHv1lPQDAXXktyslz0B0o9SF7Gdh7ijDTsD1NAe1LP8YMdkz9KOYC7f5PQ88_Md0C25KQSSYULvb6Ur27HM7-QvF-NyLi1nFRnfMEaXM4lxjMfZHCZLjOgoXYxTGOWsHJPqFq9nspeBvioKxFkCV6K57F2tE74IYdyQn1DrerCfVkSek70p-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین تعداد پیروزی کسب شده توسط بازیکنان در تاریخ جام جهانی:
1- اسطوره مسی، 22 پیروزی
🇦🇷
🤯
2- کلوزه، 17 پیروزی
🇩🇪
2- امباپه، 17 پیروزی
🇫🇷
3- کافو، 16 پیروزی
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99850" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qmMMW-BIAzvYKoEbJIM6RLJ6fZhgVPuDspHJHAjStKyoP5-s6VccQpOX-9LF_YOCjIUuD9L6lsociVY0H9sGOnJHPM8624BK3sQEm0KzdAt0Ov4Uw2ZQpkzVsyok8_qxTh6aabG0qQa4_WKUUXb5FQAbSP0bHuT5JUeaAps6rAm6NvyrA2NmyVxVkJrR6IBdrfdUK_5HvCApkk1SwPvOeiCQGYqG8OryWdf6m2sWupRnK6ZXqMgejwxlE3NUOLHpcsqQbVgA5W_397iSjlSZH_97_1gxKJAclpdIMIL42ntUZTspM2gP-5EAhBmd1HXry3f_4wd9Ns5AQ6qkm7Alhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi7tO_g9jJD9HoA8FX0Wlfi74BgtZV3Az_sEU2GmJJVDHuwrKLOmfG7W0oDfIi1HrDxS7CqJUag0Eff5Ptk3gvN1eUgeYRzkfm0iWlgA7hI8YrI_DisSScJg20i-wUaetdAyYDy6sL_yCF_nXTlwBHsUyrbjtcYm3OGUl1jSx3elj8SyvCREb_o5upatXlbrFkT-RtptJ6hsjSrp_5hsypPQtjOYtFiPp_dXK9gC_GXqQK8EqRZVbIr-r_fBEWkxyrqMin3aosYGAEVP3KRN6MIDd77rHX045w2IoQlbYw6ffYgCPne2ttMciDLHQXRrHEQe-ngNqDMN84zZkWy-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMG87x2zPW-od7fdtCCX6p7DDocWCL-ciPj0wv6F-4adI5E1Af8-W14MJN1FlPh849khu1svCCLu_updmHLwhSxgOrUurtBEN1gY5L9_xNt6WnIQu9Onwdx8LshlN1JXtLWAJOlvItFoSaDnzS-M1Rkdpi7ypi-ddJgu-F-4JTGXHQU60qqyvw15yY9Ox9OH_7c-sIWXDn9ok8gIqDcTIBqxoY5LBH0Pc3QpKlOJuwNm6AUTE0gkEUzYHvywZuhcnJATOI_ixkqmijvyFbd3yD0QwP4UXb5HpNYvBwOZtpK921CEFCGRlv86bhsEFrhvD-1MdgHABBSmWhOWoZICTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
یک تیر و سه نشان، فرصتی متفاوت برای سپرده گذاران؛
از اعتبار یک میلیارد ریالی تا قرعه کشی هزاران جایزه در جشنواره حساب های قرض الحسنه بانک کشاورزی
🔻
جشنواره بزرگ قرعه کشی حساب های قرض الحسنه پس انداز بانک کشاورزی با هزاران جایزه ارزنده و امکان دریافت اعتبار خرید کالا تا سقف یک میلیارد ریال، تا پایان تیرماه ادامه دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdXX5KNZBxHDQeaAUHCthstJbwtFC3CNB-ODvHm_T3tZzNMWr6Xlu5OngQYnvl_rrz8YdZnMn8Ni-00ma9xOcg3dweJuzDK317zHQG5wAgFVeUwBXUcfVGS0C93Xae32QniCr5OxApgBTGuHaNbmI6CqJ4AfmW3mpZZo9SPM_3Fib6MbkHM8HHKbhtQtjYVtZh4FZl45_rE3dNLAzz7q6-_IJuP6Dpbby05mDIKG1-yeRME8ZA7FeUOh9eg0BLABllm_OOHsX3UK0Aj9ibbco2CuhmY_651t3_reA6BvK14PuFPWKLx3yKDL1iJjYUnrB9F0eaOfaHhdDb66lD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXP0esg629P5skPBRwATsFyZZc31NcQ79bP6opgWO4AdJ9SipAt9DrgI-JtMTsEMP8v2GeL3M_TYEnepnag3zm0QivX98FJq2vWF06Pl0UlZH4Ig54aIbSIemHBL2HDMPTMnzFjzCkgs_YgjU44cTClpt90vqOCLD40HUK77LUc7DULn8Js3DXZW-AjZ3kLGYSw1tce2g4uwG4jS0bTNKhLEEg9hCR558RLnoi_UzsHaJuPa-otrWVvMDEZ2V0lZfYhve_ayt4Xeyqd1siLLOMoTYBMuq4g6zJIvUVVWeCEm2znzghzEO_Q5ftLG5X8y_FhvOnH3bph_rOG3fW2RXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaC_VxJUZj8NPvXgSA1-Q_6TKQ0GXP70Lq409_3Y4eOKpNzQJ7teZxDoN1qsL7IInNjBixyNY9CX3cZR6pUR4ciVYDDNFgPQElCnFV1IaksCaZkmWelnvk88uYaO_8KfYh2_eD1QYrlFTMTVl2eVC87SDRG7i65TOqgU_2B4JsmdXJWiQ3KXqOS_BKt5a17Nq6Wf6EhuGxd34XVsjgRttb_zmlTPZZ1ogLQvWTHSt8mt8cUlSne30E7vPKSnM0ok-NpsYtnuubHUdI3qUUHwbFE0pwHwBZi9l3OUApRpc5D34HK0Epx8pOJzam1UoU4jg8J-9TqyCddjUVO9671G1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-1EeXNMIqYJhfYmSh9yRSRXbadFfvxPoAXX1cbAqci9bxjRUBV9alufNWkthmSieEq4OdnDxTmYKJ7WKrhycVpr-IrFWvBKgnyICNOH8uIPexkRcu8B3c5T836gWfFV0qBXq2KU_5haxxZCkuDpehT0TJBkGEbr94AXrz9maddq1GtXQzURhZWnuIaRVFlbRmuxnNwqS3FcUnXVNkLUIQw-foOjq3B6y1z47Ngb1ET2Haj5d5RKCoLrB8f2zb32pFSnqwmYucBtgTJs3CnYHFDqVyYENp6FdgzsLw1fIoALjMSeaVrC1VnEOPVdR6SiCk2Zs_l14mVuLkDI_7m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
بارسلونا و اتلتیکو به زودی مذاکرات جدیدی در رابطه با آلوارز انجام خواهند داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99836" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0FP1JLC7WsJIvSzE4MAac12A_TGN7FhtmGRmlPbk0VCIOO85O5BSPhLYrO0-ZUiM7XrArT32b1aCZJRdsobs6mmE8KidTHnghvyokadWkKbRsPgSGiSnOjfN3hAz1r2XY5o1SnR3jUTjjStRrqr_CjQMD5qIEH1y_lFms5fP8ld4P5h-8lmLtvGzc9uDFPaDRzgggGgiR_acRW7g8QA-WhYgP7B4l3PKtkTLy9PBwGEJa5yQJGv2PWKBFVFu1ThAExHawLUUtBH3mbZBgSQUO9xVDh-78sE_o4BHPghrHnA5hV_kHCF8bWpKLCofS2rgVcbMfy2fIYUWesy9pC8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99835" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRFisJXaNfgwLtFO2S_0pCDcnzZBagdMk1M08ho6aicXQddeSMcjIbGLPReAZ0r5TNvLiU3iuqRosn5Ft8G_rIxWidhujd3xYXEfaP-puxSonCerHoDVf-Qz_aNyh4Ndi7jhjZIOw1PNziWf2i7py8I55ZsHw30VmEzZMqTnUh1sXBuIqVpDqOjNvk2Q7KV7IrbIwYUgekW06DakxDdCpiFRX4KAXaOKZjrW-w5HLxZGyCcVosIPLjNcTepZ8JupfPTaJfWhrGDJ4-L04hkE34-0Bp91yxovcibertjoh90D2QbK-HknSs0ACGa_VV0nuvsfqgZVg_RlRltk4Lv-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فوق العاده رودری:
لمس توپ: 712 بار
مجموع پاس ها: 638
پاس های صحیح: 597
پاس های موفق در یک سوم حمله: 170‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99834" target="_blank">📅 18:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04227938e0.mp4?token=qeoGY5yXuqowutzWoHf_wRYpDC1f9FNSbZdG84KHvYE92GcY4-AK8yGIhGLM3xEQBj59-zAUB0dxM37-MJsMFooDgj-CCsS5cS0hCcvd1pnXr7Q94SsTIm286WdZJ1vREIt2vASEKUg5mi6hgwmvMl-hY6GZrTupePFzsOaqumjBq-kU5irXl3nBJvrqHlVdN65vqr46T0gaFR7syB4AS-QVxMcks2prgeIPII_ofUf511P_tctIwPlm9IXl_jDB0yUxhFvM4S_QsUEV5WRS4SBBK0ESuN82rfEQxRvOw_BcRwQAwjR-skUC4zBlrv0Pcy9iuGG_aG7fPAq3EX17ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04227938e0.mp4?token=qeoGY5yXuqowutzWoHf_wRYpDC1f9FNSbZdG84KHvYE92GcY4-AK8yGIhGLM3xEQBj59-zAUB0dxM37-MJsMFooDgj-CCsS5cS0hCcvd1pnXr7Q94SsTIm286WdZJ1vREIt2vASEKUg5mi6hgwmvMl-hY6GZrTupePFzsOaqumjBq-kU5irXl3nBJvrqHlVdN65vqr46T0gaFR7syB4AS-QVxMcks2prgeIPII_ofUf511P_tctIwPlm9IXl_jDB0yUxhFvM4S_QsUEV5WRS4SBBK0ESuN82rfEQxRvOw_BcRwQAwjR-skUC4zBlrv0Pcy9iuGG_aG7fPAq3EX17ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
ژاپن این‌شکلی داره فوتسال خودش رو گسترش میده؛ واقعا همه‌جوره باید حسرت بخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99833" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=gNqsQKIaQkKkQJFoENbQrF1HMwo5SgN6T8JyIadvh3sPFmn0ZHCfTpNZWbGdHdLektw_vmWuYfwwVLxexxzUCb7N6uD6g3GApIFJ5vcuwy3MwBwBlXsYCQxBcXH3pcKAzuHJ1IUz9i_-_Q_gQBiHdSRYgOzQKj8yOL-Y0MEiuOHi9aUTMahgmSu-LveWR3bWKdYgNsR0lThlJ809SIOu8px4YnK4l69Rgge_u0PQZgjSxWJGNIm4DEmNxmy0ZP3OWgfKswfd3HIEqgGFctBxNHrSQ-sqNRsoYPJv-ftdb9z5WHOEo59IR400M4Kbxmp115OeYAhUCmSzyWKkHp8irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=gNqsQKIaQkKkQJFoENbQrF1HMwo5SgN6T8JyIadvh3sPFmn0ZHCfTpNZWbGdHdLektw_vmWuYfwwVLxexxzUCb7N6uD6g3GApIFJ5vcuwy3MwBwBlXsYCQxBcXH3pcKAzuHJ1IUz9i_-_Q_gQBiHdSRYgOzQKj8yOL-Y0MEiuOHi9aUTMahgmSu-LveWR3bWKdYgNsR0lThlJ809SIOu8px4YnK4l69Rgge_u0PQZgjSxWJGNIm4DEmNxmy0ZP3OWgfKswfd3HIEqgGFctBxNHrSQ-sqNRsoYPJv-ftdb9z5WHOEo59IR400M4Kbxmp115OeYAhUCmSzyWKkHp8irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ماجرای تل سر یامال و عبارت EGO YAMAL
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99832" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIgoZAwsYew4NqP1GKW85-TarUzbO0nAkx_oNoGVSY_RmUgvrmEymQCfC-hlnEFs42K5Wy2W0XNoLvFNjhx-EKahuBmwMOMUkztCcZ2jLOw1NE8Xmmd-JzkLfCyBbR7sl60vfMJ-Aa5VHCwmlVYJyWc4pj_GOlqJ6rCHVSVdFAlKLui4jGsB8_Laa9Ae8gPS3TQzVm4dD9ITWWgKl6SENV3ec6j68isRE0JppBHs33J0AoDA5Wwf1ti60fz8G6unbQ-iiB7GUyCXHGqhFXvNJ4wuYrYmTbkjW0d-7Ys364CXr7z2CbiBse-NzD6snHqpSNcL5V3y0ppLKicFidv64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
اسپورت: الهلال عربستان اعلام کرده که هیچ قصدی برای جذب رافینیا نداره و این بازیکن جزو گزینه‌های تیمش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99831" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=X4Fm36L01H2qtA_LynqXycL5PWjlMzm-c6JR9TZ4o3X0x9D7I-dgykj-BDGPQLiD3cWdhuePZO-mFUKzgReNbL5ZWdypAWmiAlxid4BSjbYOEuqRZ619nix1cvxVNb0biweNtMe5zx2U1zglfSdNi36ReDMCLpTAE7rLnZxWX42dwSs6mDyyxUTLIKCPWEjjWmwFDiXe83X0jbCown_0j0KFktHfsKDFXIj-2oh2NhXmCJHlaRx2JDBGbreg-AgoF9fFCcAj5IgIk71_j1_L1QIcGdwEtC6dEUKhg9063KxNzjwcYudZ7SyKCGlizv6lbbNFJNuIqEIVYhdB5fSPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=X4Fm36L01H2qtA_LynqXycL5PWjlMzm-c6JR9TZ4o3X0x9D7I-dgykj-BDGPQLiD3cWdhuePZO-mFUKzgReNbL5ZWdypAWmiAlxid4BSjbYOEuqRZ619nix1cvxVNb0biweNtMe5zx2U1zglfSdNi36ReDMCLpTAE7rLnZxWX42dwSs6mDyyxUTLIKCPWEjjWmwFDiXe83X0jbCown_0j0KFktHfsKDFXIj-2oh2NhXmCJHlaRx2JDBGbreg-AgoF9fFCcAj5IgIk71_j1_L1QIcGdwEtC6dEUKhg9063KxNzjwcYudZ7SyKCGlizv6lbbNFJNuIqEIVYhdB5fSPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇳🇴
هالند تو این صحنه خودشو خیلی کنترل کرد که کون سورلوث نذاره. احمق اگه پاس میداد شاید گل میزدن شاید صعود میکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99830" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=aB17fgPOjDAi0T5QhdKR9p5O5Be3X66QZT36r9oPIWyVWzXvVsKvde8g0uvpkFbzdGt4eneQtU6OakZezo58fh9nu3rEjTdn2QWX8TzrOzl4E3bCjX9VpMw25KX3jexPT3RA88pUFOvzNBAXf3Ku3qeoFME4JHtv_1Z8-nePQcg36IH6OVmIIsbTFEL2IWfyBvp4COmS69z679mdzKgUZKFt6NZ2N2VzB_KRHhJJ3wxfBcUS_NgIkAGuluiVHPKbNypJUU2rmGks9S1k2erYgqybSb_Xmcvoxks5WMbahMlVQbfuTwcszQBKm5EZLSNWBOuNXmn_Yx1w8Lzu3Ii_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=aB17fgPOjDAi0T5QhdKR9p5O5Be3X66QZT36r9oPIWyVWzXvVsKvde8g0uvpkFbzdGt4eneQtU6OakZezo58fh9nu3rEjTdn2QWX8TzrOzl4E3bCjX9VpMw25KX3jexPT3RA88pUFOvzNBAXf3Ku3qeoFME4JHtv_1Z8-nePQcg36IH6OVmIIsbTFEL2IWfyBvp4COmS69z679mdzKgUZKFt6NZ2N2VzB_KRHhJJ3wxfBcUS_NgIkAGuluiVHPKbNypJUU2rmGks9S1k2erYgqybSb_Xmcvoxks5WMbahMlVQbfuTwcszQBKm5EZLSNWBOuNXmn_Yx1w8Lzu3Ii_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
نیمار بعد حذف از جام‌جهانی دوباره رفت سراغ عشق و حال و کار همیشگی خودش ینی پوکر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99829" target="_blank">📅 17:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=OZ1dycQl23f2Zomp6keRxs5P0TY1C1eASfT1rpEUrx2e5RXBnhrOYAnbD3dTZPArAo-7kOWKxamnzFIkIL25XXhFDKYYArg1G-02ytdM6aAEqTfZO4cVn2TSszILvss9QiRPaoSKWb0s7gcFmLujSlqViOK-fT4RUCab9HzDFGCqvLj30jurnDJ7JUOfXmVZi5I94XLsQP-qZ8F2MdFvu4YZfNTUk8o1P1lsJ9nu2quzbjOWFR1o82P_GyYSZ8DQtGl8LjtFaBmaqe_R_G7kIMqh46hoOleMN0A5d6qvFtMF1BjFo3a4ro1RnzRGWEWUTj0vCYSZVOi6Q0rocaPxZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=OZ1dycQl23f2Zomp6keRxs5P0TY1C1eASfT1rpEUrx2e5RXBnhrOYAnbD3dTZPArAo-7kOWKxamnzFIkIL25XXhFDKYYArg1G-02ytdM6aAEqTfZO4cVn2TSszILvss9QiRPaoSKWb0s7gcFmLujSlqViOK-fT4RUCab9HzDFGCqvLj30jurnDJ7JUOfXmVZi5I94XLsQP-qZ8F2MdFvu4YZfNTUk8o1P1lsJ9nu2quzbjOWFR1o82P_GyYSZ8DQtGl8LjtFaBmaqe_R_G7kIMqh46hoOleMN0A5d6qvFtMF1BjFo3a4ro1RnzRGWEWUTj0vCYSZVOi6Q0rocaPxZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید آوردن تو ویژه برنامه جام‌جهانی غافل از اینکه دوباره برامون حماسه آفرید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99828" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=vgXnzr8oJD7oNC1GxqnhUikoDtbmNKyGBXbO7QN31Pe3HtqUB14drBotKbeODodmU0vw8KltbDAUXWiHPVqQJxRFz3cRcjQ8iw7iqSKE72QlH8yjTbohy5rmAXateqc5cOAJMszKPxMc33bHY7GHY4-PApCg8N3v2904vP4oaiUhRe2gQSM79uIEtoVHyYk00CzGGzd4hK6DnRzLuSNvfhnZTLn9OPDAUS986rGkfHBQSDIZLBzDN6M5TRmLq94LjT7KFzaIuS68nAAfdBPE7wKUph8XIrO2VZefDEONAtJ11kBcGD7SdY7qi4Dy9pTBJS0ZgsDlPq2yjRitxVXAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=vgXnzr8oJD7oNC1GxqnhUikoDtbmNKyGBXbO7QN31Pe3HtqUB14drBotKbeODodmU0vw8KltbDAUXWiHPVqQJxRFz3cRcjQ8iw7iqSKE72QlH8yjTbohy5rmAXateqc5cOAJMszKPxMc33bHY7GHY4-PApCg8N3v2904vP4oaiUhRe2gQSM79uIEtoVHyYk00CzGGzd4hK6DnRzLuSNvfhnZTLn9OPDAUS986rGkfHBQSDIZLBzDN6M5TRmLq94LjT7KFzaIuS68nAAfdBPE7wKUph8XIrO2VZefDEONAtJ11kBcGD7SdY7qi4Dy9pTBJS0ZgsDlPq2yjRitxVXAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
صحبت‌های جالب سیروس میمنت بازیگر سینما نسبت به اتفاقات تیم‌قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99827" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuY89_talK-cVUUrFS0fZomEezTLMwbbWqvZzjkRwfiaRx17BiUccXuxzk8nnjZEDd4JpcWI1GHl6Uord0FyYqAmcyK8MYSsgXUSLJskrWOgKaX3ukbE2OJVh3GDzAEHTtnyBNfDW8cjkPT4KejHhmCCO_4W_EJfpWVpT6bTJ2wYIjjFMSRcIEwGVNU8uyoXQsn5_dz9jtPmxEOncpEFlyYOFAzugsOArHOYvKmIDPALakhzGT-niEeLq6TtvHJX4iCZMRGfV0ymaUlelfxVUL7A-x-StAl_enoALuNUsYIj6tnrhtL07emzDf4SZX7uFkmOeHMjhlXq82yoXsllFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
ترکیب منتخب مرحله یک چهارم نهایی جام جهانی براساس نمرات سایت هواسکورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99826" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
ویدیو فیفا و انتشار تصاویر ثبت‌شده از دوربین علیرضا فغانی در حین‌بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99825" target="_blank">📅 16:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=iNNmK8ikGy5sHP6460G5hsnDCvvxMUrJXIHqQ9KQXufY1ePsul5eRF7yeP1TLRYNLjzRgfRuTtJzYgNF8KoRbiK4EQeYqeSBdAe-yj9WCHlR6IV_QxNT4POVRzn9V0NUlNJ-3IjJRLZP8GyoBzziUNNyefXTYyoV4m_yicUMQ6W6lXeum2uUsjMRLJHJabstRdO0qTrWYRvrGiSaa-k35mEYqOQNykQ_sf2ncUNkPh3Y306XmfvDnExezZ_ThCqbdKXYVewCs4BFPUuB3GjBLUFeXK7xyXDCM4udrFpS6-_TR19qrBHMvPircIxgXRcnntUuwm726Ce2kpxtPmcgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=iNNmK8ikGy5sHP6460G5hsnDCvvxMUrJXIHqQ9KQXufY1ePsul5eRF7yeP1TLRYNLjzRgfRuTtJzYgNF8KoRbiK4EQeYqeSBdAe-yj9WCHlR6IV_QxNT4POVRzn9V0NUlNJ-3IjJRLZP8GyoBzziUNNyefXTYyoV4m_yicUMQ6W6lXeum2uUsjMRLJHJabstRdO0qTrWYRvrGiSaa-k35mEYqOQNykQ_sf2ncUNkPh3Y306XmfvDnExezZ_ThCqbdKXYVewCs4BFPUuB3GjBLUFeXK7xyXDCM4udrFpS6-_TR19qrBHMvPircIxgXRcnntUuwm726Ce2kpxtPmcgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👀
عاشقانه‌های حسین‌ماهینی و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99824" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=J_vOLx0XEwr-SCHnCUUcLMOcIwNBnRJYIQurRUptp4emkZbHA5o_FSW-bOkB7GPtrp4IfnDRb0q-sk6mVHDCWcSwzbanKHVcjTj_JzujUdXzXCXmtGDzLE_k1-fb3I8cHJ6yeSYqmwn8wkcY2qUsN_qSGXoUYn4MU4JA1Fep-oFXyl-qH9Y2zrK8TJCRwP0xS-mLRqWyMiTsvgfzi3SnCHLls-VvzyH7SyQZIuvFHPlQGT3w9rkmfRvmKENF9lMn2Wmtrr9QFrb07VJ2gIdP6siHQEvcXeAggsyxViPi1tjffkxQXM0kLFtFO7SAMiqwxmcZ6jdxHDyY9QX0ulk14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=J_vOLx0XEwr-SCHnCUUcLMOcIwNBnRJYIQurRUptp4emkZbHA5o_FSW-bOkB7GPtrp4IfnDRb0q-sk6mVHDCWcSwzbanKHVcjTj_JzujUdXzXCXmtGDzLE_k1-fb3I8cHJ6yeSYqmwn8wkcY2qUsN_qSGXoUYn4MU4JA1Fep-oFXyl-qH9Y2zrK8TJCRwP0xS-mLRqWyMiTsvgfzi3SnCHLls-VvzyH7SyQZIuvFHPlQGT3w9rkmfRvmKENF9lMn2Wmtrr9QFrb07VJ2gIdP6siHQEvcXeAggsyxViPi1tjffkxQXM0kLFtFO7SAMiqwxmcZ6jdxHDyY9QX0ulk14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
واکنش دیوید بکهام به گل دیدنی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99823" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=eRbFx-crSbnyHhm--SR2YYsxQp11QPiltJerosEVVjg0_R4Jt_EXpb7gvV3_mRPwhlOrLJh2m3jPujLMRKgocgNgiHR2EXaMENiAcogKdxDvwtVitLyp7FiMddFhVJsOW_FTe7LoANywsXqnKNuVku-tlNTt23fdUYm9vsOkMnDfZGVwds7SU00GmAjXJU3EhrrSSpyS_n8SgXCHlRiDRW6rbfmMMCwtsHXcjMI4oLttkgTGMJlFDFGZXgwIPm6l4AVb0Sjs5544o8iBhTxBAecFWz7Wt7MC40EH-f3GJMHukq_gKmI8LbRH-dXAXfUdIOg7BOSI6N9dRvrEeLi1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=eRbFx-crSbnyHhm--SR2YYsxQp11QPiltJerosEVVjg0_R4Jt_EXpb7gvV3_mRPwhlOrLJh2m3jPujLMRKgocgNgiHR2EXaMENiAcogKdxDvwtVitLyp7FiMddFhVJsOW_FTe7LoANywsXqnKNuVku-tlNTt23fdUYm9vsOkMnDfZGVwds7SU00GmAjXJU3EhrrSSpyS_n8SgXCHlRiDRW6rbfmMMCwtsHXcjMI4oLttkgTGMJlFDFGZXgwIPm6l4AVb0Sjs5544o8iBhTxBAecFWz7Wt7MC40EH-f3GJMHukq_gKmI8LbRH-dXAXfUdIOg7BOSI6N9dRvrEeLi1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1K0BJfPgHl15gr90XlgNMvFFR_wBiwzH2LL_h9H0mEVd6yA188sc2gpkt-cKnoW5toBvsTEEqSaJwVHlA6rmEDT1iO3iXpk-KnS0VApVWnvoDt2C4ErFe5dDTLbBwwMuzReIbskuvTw-ryUO4ywOg9-09rzILbpNuuJQ_p1kTBE6nXLNL7bUzg1iB2qM5HN9AwYFnTiptzyD2zwiawE9uFet1RKvDBL_EJQDO9OziMAud3HEAMMQi58xeSwR9jEcqMHuRnwC9m50kgbNgBw42Qgc8mnVDbL-1ssFi5YJ1oPuM5CDc4Fvro8VYlUFNVcNnvagXRQuXU3sU_CmVDlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3RpseACGvVdXBIAn6iE2icDwerbR8Nlop-42SkblLo0TTeQ-T-apYBRtfkzYqypjErmGvh0CajErWRkRLBfbirU604qpKs6_0IEJf3DpjoR57xfto-lzMvMF53jF8zCJ-XNyQ4bQJob3KxhFrknQwLx6HUxUnQqvWU4vqf11v1O2GvIt4spkKJtodcgUIkQTnv79XPfkuPquXT-C6Nufi9l8xof354E3DkOclWHrQyp76qloo4EcIUyhrG3oDp1CTZP5qiVz4eF8XuA9RmJLkg8ALcka93HudWAPyMrm51kpdbEAIpkNDs4UPzIt31HJmRT9gAYHvZHjcybkbLMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3N9ZyLrw-wMu8kM7i6ceSx418K6CBMO1TJopARV8CeDs_0cnoncUR8FQnEFyHQl-kJXjrEAPApECKYg5BoRcN-eB1QgDVncYCHKUeXmTzcs7E0uoZODrxy00Jh5aZpQ3_1EnBKI6iWRPE7ZsPxq718wXiHRkUrZoquAbiHTxtWySkipaCce4OB5tmcWbGxebjWgZs4FsAVZDfLNpc0gehtofyC8HAxrXHDk5_KkmZyP9Uf7q2VkVjDYf9Qq97V2qPnMEsHFTcfy7Lysy6tMiVbjyv5cAyzBSn6tgyyoB7zcEU3-qFfxkyQnxLl6_fQkd5v0tbCUVAxUUuhAOjrVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMDAKpCO2mPOBuP_vwBDrO6AFQu5gYhyH7jiT44etRu7LQQi_K_cwhpX3WIv8p3SOBylTh6Lp-x8iZzpnvFWbDZ9487JiAEDuE8o2KDmww0gjJxXtZAz7qHQnOzr9SY9a9QW9DMHlqq6OMJ6eUxbn5bdjBfzQ_7I1ljWMevG_9dcuExBSfO51gdD0n_TfWVivLH_NqZw4MyEJXnWmFSFYVd-ehdyuMOtcG49XJJsD1-Cw6XxXBJSJpWE0txEH628p6mnJF1qvxkLf6EENOIxqqyH5Ywi7Mw8SdU8Bl1MvTM1ZoNzSgMg26Z--PBJqUnclQFjIiW_-PtTL42fkw0C1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdp1WCcB-R8Zf96869JTXZ27X6ZOCGSyqvnzJtBlIGWNYffSufbG40dPJhidZdr8b8ylZBs_bljbXtUVKD7XHMvhcRZ0Hu88F5-MpN4IW3V8IDmHRFjmgiRpA1kqm7yrCVEtX7SOV0dsxQHM0rF4M41NKhlLir8zXDP9wox5V3Q2ofPWQKxmAQzRO2VDcvr2nXpvRfrehRadDBneamvWJ7d0pjbDEfVVYa3P9QeofGwJFy0ImGON_1M0JVNsRgGZHVXoI4gtJKi6RJmh4Avecrbt1bxaxiJCq-QCS7n0Cz4pz0wa-aliNmNnZIOsD3hIHsINXVrloFe3Qq91bED93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=FZV-t4axjm-mZlu4Tm7PQfYhYI5WqWBWcDLMUwgXuzbm8ylCg4EHYWKpeISWEDxKHuAG0wYvOme8dUPhDJZ3w_v6yEjKypselUkFlWCCOiHppwTHrNzFawZMEk9GWvo7rM0KxCrDRzlOMf5BQZKo013vL8DwEqH683cw2HkCLqOSii9thmsEu4z6RjqxH2P9ePvzqx2-OaFV_kuw23r9B-AtDUt0JQIdkhbXsIbbtMNjrmKBMjAgn9M4eaPvNbrAEUq2W4cX-UiCSHBc45s6kSWPHvSC0v3LXtCPNuRlv71Ccr_QVUT9oujIdRR6PmJy3mRP38qSnBhO98xJOH4BXXy8lN_9Pa3VKOSnFV1G6KciRmi_Wa9BlauP6O6anC8HiQpmjkSaqfL5t5jHq-eobvHAxJQhfY4F_Dl39gm5LnDsknv1nN5D6qJeOfN64uswSAavi8dr6i9abnhvFrNDGYLvmSooeCXOajWJvIVQLaAbGrMt0QUZKqKf9RVX8N-3g47LdmCOQKwg6l9tZdrnyRUrQ4cN9bOInLdpCdhZTRVlr5Ueq8qSUHjCVeP7Rw_K1nHDa9ajGAy5c2mspcHVa0Ek2IGv4ZbUFFz7IOr0FT1N2ReKlfN-1aB27pHzYlzbUT6ZCQKJesRBfVR143UYgHR7YdbrVC_d15P-X2Y6OJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=FZV-t4axjm-mZlu4Tm7PQfYhYI5WqWBWcDLMUwgXuzbm8ylCg4EHYWKpeISWEDxKHuAG0wYvOme8dUPhDJZ3w_v6yEjKypselUkFlWCCOiHppwTHrNzFawZMEk9GWvo7rM0KxCrDRzlOMf5BQZKo013vL8DwEqH683cw2HkCLqOSii9thmsEu4z6RjqxH2P9ePvzqx2-OaFV_kuw23r9B-AtDUt0JQIdkhbXsIbbtMNjrmKBMjAgn9M4eaPvNbrAEUq2W4cX-UiCSHBc45s6kSWPHvSC0v3LXtCPNuRlv71Ccr_QVUT9oujIdRR6PmJy3mRP38qSnBhO98xJOH4BXXy8lN_9Pa3VKOSnFV1G6KciRmi_Wa9BlauP6O6anC8HiQpmjkSaqfL5t5jHq-eobvHAxJQhfY4F_Dl39gm5LnDsknv1nN5D6qJeOfN64uswSAavi8dr6i9abnhvFrNDGYLvmSooeCXOajWJvIVQLaAbGrMt0QUZKqKf9RVX8N-3g47LdmCOQKwg6l9tZdrnyRUrQ4cN9bOInLdpCdhZTRVlr5Ueq8qSUHjCVeP7Rw_K1nHDa9ajGAy5c2mspcHVa0Ek2IGv4ZbUFFz7IOr0FT1N2ReKlfN-1aB27pHzYlzbUT6ZCQKJesRBfVR143UYgHR7YdbrVC_d15P-X2Y6OJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوش‌شانسی یک‌آرایشگر در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99816" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=Sn4MvKg4PreeXXoZhaJOaCK9FXZ2Khj1YGi_tcZ1YxBedgrkgG0B9HPGlwv8b6SSHzN1OZnhTCZfVK4kOdSW4SAswE1IalVNBa0NonThMWR9m3S3VGcmvQiB8aAB6pFr1vQDO9TsiJBpuSFziqzOq7VIqrKiZNfOFM6tA63nS9hspiPEUiBqY-aKMT5gtGcY1qelR_tHukY2-_BLWr142wYHIWWp_DM8VY4e0IUPm3hObGJeCo562r9Oiwkkgqlft0Q5xc9bWOfZC1M9dxFSE_0YokzLpl97MxVubSvysDorVft5p7J43c2t7n-Ygd8LZm31DEEq_9VCRwF8CiiyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=Sn4MvKg4PreeXXoZhaJOaCK9FXZ2Khj1YGi_tcZ1YxBedgrkgG0B9HPGlwv8b6SSHzN1OZnhTCZfVK4kOdSW4SAswE1IalVNBa0NonThMWR9m3S3VGcmvQiB8aAB6pFr1vQDO9TsiJBpuSFziqzOq7VIqrKiZNfOFM6tA63nS9hspiPEUiBqY-aKMT5gtGcY1qelR_tHukY2-_BLWr142wYHIWWp_DM8VY4e0IUPm3hObGJeCo562r9Oiwkkgqlft0Q5xc9bWOfZC1M9dxFSE_0YokzLpl97MxVubSvysDorVft5p7J43c2t7n-Ygd8LZm31DEEq_9VCRwF8CiiyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف نروژ از جام جهانی به دستِ جود بلینگام.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🦁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99815" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEvHR2CxqI2MFPXTu9rbGcFcIvFGZrTLzXsXHPiMhdP3o0boPHwH1728T-N0XIH3yFw8Qc4SFAQ0oc_MxF7yM7PJ9oYV86yKekuzhC9ZWOdFw96KDuXmzVlmChGAFMqwtgpHbsBAiBda_IfHC0IP-rsDXGU515ZLjftHMq0runVNvIhVvpYSrdNC4QRTRbFUJUgARbnoYjl5ETDAYGgFvRRUDod973uA2trLcu9n6ndCOsQr2EA5kdjfUEVfWQE9eItRpUFEP75IAUC302jMBgnQ-xR7_fGkgjBrx73VVc7ecsdUUDLqaTLB6I_krBs55QsjTLiESJ8DpKeb39LwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از حواشی زیبای بازی انگلیس و نروژ
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99814" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=ElFsMP-glCRXhSpJ3J28vXMjreRUGgY-PzySDmowaAhzcx3qowQwgsA8b74_n7mAjMd9O_i-41V3gEuuFxZH6OaMmfjdzOdxLs6ZbqWeyvzf8S2WCKqGJ9MREG6lON8K6TuvKhszxOP-58XaIFpxynG8BX7KBdkOAjUITIsIAnOfF6lN878ezV0-LNiRY8JVkKmGp_iT-hd8MPTGofKzZ24kuLhqwNpYSpb-DBINRfHfCjYAOQTsmflodB2L0r-JSfHavsYKDLRFZKIweHzawmzXDT9UJNrxmOCeSZxPFrIaJNQKAgHacmFw4JMqS4HhWr_2fONt0YAG-j3PBEkYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=ElFsMP-glCRXhSpJ3J28vXMjreRUGgY-PzySDmowaAhzcx3qowQwgsA8b74_n7mAjMd9O_i-41V3gEuuFxZH6OaMmfjdzOdxLs6ZbqWeyvzf8S2WCKqGJ9MREG6lON8K6TuvKhszxOP-58XaIFpxynG8BX7KBdkOAjUITIsIAnOfF6lN878ezV0-LNiRY8JVkKmGp_iT-hd8MPTGofKzZ24kuLhqwNpYSpb-DBINRfHfCjYAOQTsmflodB2L0r-JSfHavsYKDLRFZKIweHzawmzXDT9UJNrxmOCeSZxPFrIaJNQKAgHacmFw4JMqS4HhWr_2fONt0YAG-j3PBEkYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
کنایه عادل فردوسی‌پور به عادی جلوه دادن شهید شدن مردم هرمزگان توسط صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99813" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🙂
اگه جام جهانی توی ایران برگزار میشد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99812" target="_blank">📅 14:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=ZG2hL1ro6PSqsLeBtaYew5ljPIKAscUZ45XcLuYlOjamF4wiaVTVq72w-rWCFG_Nkwgvfrv_4nN-f3a8Q_6ALKOV71LPO1AF6owZn29Cu5GDkn087sLSujEYJHf9u_zdNrhfgoZVmL6dJfx9oswwbGJwwwOsoaEArluNeNVCOad2tl0MCfvSCYAymgOQInb4kYNDedIuZI4LNNC8KiwAcx0nlAUen-E6uWjWZ_zJW6KRMG7_S_8FiPloUZNAdSnMZomtStJlZxtZe8p6NLX-h8ObkkSt-2ecXVPpZQZB_3-xO0NLfSyqxsYwFEEN70WtTKkCwMeoXKBh4GGFIQC1jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=ZG2hL1ro6PSqsLeBtaYew5ljPIKAscUZ45XcLuYlOjamF4wiaVTVq72w-rWCFG_Nkwgvfrv_4nN-f3a8Q_6ALKOV71LPO1AF6owZn29Cu5GDkn087sLSujEYJHf9u_zdNrhfgoZVmL6dJfx9oswwbGJwwwOsoaEArluNeNVCOad2tl0MCfvSCYAymgOQInb4kYNDedIuZI4LNNC8KiwAcx0nlAUen-E6uWjWZ_zJW6KRMG7_S_8FiPloUZNAdSnMZomtStJlZxtZe8p6NLX-h8ObkkSt-2ecXVPpZQZB_3-xO0NLfSyqxsYwFEEN70WtTKkCwMeoXKBh4GGFIQC1jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇫🇷
حمید محمدی: اینکه کادرفنی فرانسه بعد از این نتایج درخشان و رسیدن به نیمه نهایی جام جهانی بگویند بس است و این سکان را به افرادی دیگر بدهیم بسیار آموزنده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99811" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=BdYwhKmeFXk_2mMzW5YxXj8TUsHds70ZuupvSw7w0ICuqnHl2nTlU_pXo-zcDXmE94qFAvFwXhTNxzsst9XGZmw3RXHMfE2jHToot42SXljpBgei526TiCEfwni7mC8lh8Y_Yc3YwsgSLFzlz48Esf-9JwrznFplrHkCUcGHlo4DqbQxAwE5MqN7ip9jU7XEor4AmtMWiuXOmYbkG1uCgPViWbPUqncRQrssMVvJ3cL-KYE_8ZcpjYXfoNpmbapYCPtsod8R-nrVgV7IaZFtfZBqmrnU8djuY8LjL85gd7tcAqp5NxZKgQtXIuSeYCN-bZJ3m7hqWHLJfyOiSQbyWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=BdYwhKmeFXk_2mMzW5YxXj8TUsHds70ZuupvSw7w0ICuqnHl2nTlU_pXo-zcDXmE94qFAvFwXhTNxzsst9XGZmw3RXHMfE2jHToot42SXljpBgei526TiCEfwni7mC8lh8Y_Yc3YwsgSLFzlz48Esf-9JwrznFplrHkCUcGHlo4DqbQxAwE5MqN7ip9jU7XEor4AmtMWiuXOmYbkG1uCgPViWbPUqncRQrssMVvJ3cL-KYE_8ZcpjYXfoNpmbapYCPtsod8R-nrVgV7IaZFtfZBqmrnU8djuY8LjL85gd7tcAqp5NxZKgQtXIuSeYCN-bZJ3m7hqWHLJfyOiSQbyWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکثیر ارلینگ‌هالند در سطح بین‌المللی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99810" target="_blank">📅 13:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
راز جلیقه‌های هوشمند بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99809" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6ym-nmg_4wFVCIfW3kI_-SZTQom5WGHqtwuLUaYihk-EFGjcOlX9xkbxYTNx2L6-mri_yWmsb7esuPR0MgyjB380NyXVKfhuLapqelIufrlHoNySJbqgoRMoEoNko6M2a1TVb0O6KoQ96OqiXxiVIQOPaX57W9rW8VBQjioayJIevMbcTziHtbk4wETvS7DyvmypzapFrqIl98iZ7DQqPZbyVdhNnXBJHHefpzWPTAzIvnlC2cHEVUrat6HRJFBX2tJERx6FJtVbDZFahKwUyIBV5i6CKmng1MkX9sUcO_CkFxscaO_9HmOx_PoCvxNOP_-iDFvEfSXOrjBxGGlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
• درصد احتمال صعود تیم‌های راه یافته به فینال جام جهانی (بر اساس مدل‌های پیش‌بینی):
🇫🇷
فرانسه
- 58%
🇪🇸
اسپانیا
- 42%
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
- 51%
🇦🇷
آرژانتین
- 49%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99808" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99807" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99807" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5h1pJtE6YqM4aon-hMehU23uILwmDLWQDqNAUEo76AtCpKUv9E2CAY9eylSMmaBA_8iNLUsEamJlYgPDVN5TEU1lE85U5t7KSf9unPSRb6lhcpbkR2M50RU3TKrqkxTjrXH_2RLQAsULXozkRVCwkva9LMsrrhN8ba1TZIEA8fpX8kI8GSOpzraTxZ4QNC4q741KKk_k_ekYUPmfVtDJ_9CaiRvzHeWZhiL4DK5ElogwT2pVGXCexo8dQfwI8w_IKuvV7T9lTxF0APcGWxOMpt_wfRGCMZiH0G30hthpaZxzgYublbrm_HY4wIGcBm0Qc1ctH-2CZTl25LYoqHcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99806" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22252f139a.mp4?token=KQKQy42wTqVo7rGy7DgQe7vxRr2DXWQOUXoiPe0CdYC2WJaTUJY-6pU2vQx4fvaIKTfQhRc1PCjBtY1Px9Gqi35K_LUb6HOJ_KSivfn5zmiTYz27vWv-awMHASbXiZi29kROnQ348CKjQ0Deb_okwBC5Xeb0RCPOCdE0MTPIdqJhzpXQF4ydf1j1TeEtlfQ7xp_7yrj3arlhfrGEEnTansSZAEF--mqVnulR6dqORlbv4iVpXZq1P9wR1BZxwzt5k3VZ85eoQX8udjUAXmLPY80o7iSIxP8viCTV9E6nY6B8cEqPhY6ILMPzSfFy8yJ4T_lEg64wEa5bJ_gH7nfcbXk0CEb4byyfYxO1VHH88aUi5a4br_VtNL-ulzlqfo8YFXaSKJYFhmOXBkgi06Lx-nMw_94SWwvI0bqsCyHAWaMAwv0PaIFJy1dUHCH_tna1Xr_K7_wK3v32O54hRuCly9aKYW_q0pVrvtqFyFPMGQLm0VXmOZpFrceX7HbGI1QiUJs98JmUSRBGPMpuoGMzEuQqLVwYLSNbSd6Urk0CdNmTdLkXCZtr-HM9U_oErSavF4Wc3uzLQo4VtqVvXK0VrIBkE2PlkCT2Ih6MuvOQ_6jDtZSC8UNM52dg8GgT0rUMtiE8_p4JSLkAgldjQXQ-BDxBrIr21g2xuwNgjMvWgn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22252f139a.mp4?token=KQKQy42wTqVo7rGy7DgQe7vxRr2DXWQOUXoiPe0CdYC2WJaTUJY-6pU2vQx4fvaIKTfQhRc1PCjBtY1Px9Gqi35K_LUb6HOJ_KSivfn5zmiTYz27vWv-awMHASbXiZi29kROnQ348CKjQ0Deb_okwBC5Xeb0RCPOCdE0MTPIdqJhzpXQF4ydf1j1TeEtlfQ7xp_7yrj3arlhfrGEEnTansSZAEF--mqVnulR6dqORlbv4iVpXZq1P9wR1BZxwzt5k3VZ85eoQX8udjUAXmLPY80o7iSIxP8viCTV9E6nY6B8cEqPhY6ILMPzSfFy8yJ4T_lEg64wEa5bJ_gH7nfcbXk0CEb4byyfYxO1VHH88aUi5a4br_VtNL-ulzlqfo8YFXaSKJYFhmOXBkgi06Lx-nMw_94SWwvI0bqsCyHAWaMAwv0PaIFJy1dUHCH_tna1Xr_K7_wK3v32O54hRuCly9aKYW_q0pVrvtqFyFPMGQLm0VXmOZpFrceX7HbGI1QiUJs98JmUSRBGPMpuoGMzEuQqLVwYLSNbSd6Urk0CdNmTdLkXCZtr-HM9U_oErSavF4Wc3uzLQo4VtqVvXK0VrIBkE2PlkCT2Ih6MuvOQ_6jDtZSC8UNM52dg8GgT0rUMtiE8_p4JSLkAgldjQXQ-BDxBrIr21g2xuwNgjMvWgn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انشالله برادر عزیز آقای عباس‌قانع با اون صدای گوشخراش خودش گزارشگر فینال جام‌جهانی نباشه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99805" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=iQr1JQYyb0F0M7dCk3LnhSSBKZ-vNIleAkvSmuWBKSt6fxKpOUp_rAKH35EgjEcEsdVopNmnh3s05RbHNSdntLBVq_Lv4sJ_CRG3ysKS7CzYpN7WoS-gaYHgkCk6GzZyAkojjdBgKKeOev385kGALrmdENKDUdiKIx75f2ON1WxMX9U2OHscoNYHh12MQQHtHkADi7agTyQ2qjJETmHOVsmXkApxjDTYFFVNJbA7hrH0iQw7o2C9VaxMXvvUFOsmxmICeYbtXYWBEXPlIq9279KUkAgVHCCG1dsMbnkhYjtnHJhDUyMQJ2uax9srq7RJPZuIRSD4JxeH7MniISm-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=iQr1JQYyb0F0M7dCk3LnhSSBKZ-vNIleAkvSmuWBKSt6fxKpOUp_rAKH35EgjEcEsdVopNmnh3s05RbHNSdntLBVq_Lv4sJ_CRG3ysKS7CzYpN7WoS-gaYHgkCk6GzZyAkojjdBgKKeOev385kGALrmdENKDUdiKIx75f2ON1WxMX9U2OHscoNYHh12MQQHtHkADi7agTyQ2qjJETmHOVsmXkApxjDTYFFVNJbA7hrH0iQw7o2C9VaxMXvvUFOsmxmICeYbtXYWBEXPlIq9279KUkAgVHCCG1dsMbnkhYjtnHJhDUyMQJ2uax9srq7RJPZuIRSD4JxeH7MniISm-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
جوری که پیمان حدادی مدیرعامل پرسپولیس دیشب از حقوق ۲۰۰ میلیونی صحبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99804" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_-2RTclnSFpYCA2sXR_lE1mFKXAtGTP-SZvwbPsxYATmrumjRqH1O4v-SoQ3ot_oKGLQ3JqimizLqlO07ieGBqA4PRNxIulGbeF_BKIDSOyI7TqU8dpDE86LE8MZ3Pd6lboon95qIiVD7Zxiw3SECkDtF4ZpxyQogxYGoWhxAyHtVVoCU6zdrYAnfkVICYxwwGrp8E2EZuk0_ZQD0SBWDAYa_vZzTjgZv5ggFlm7ZwenaPAKBFZWwcEdKB1iZgbvBzy4Xwm_wHUfkHdD2r0ePEt-CnO78-rW12qfQ4lKsiViXj8rgn6R3i727JmjhzMpMTfKGv2mgBh0bFD6BPNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RajDpTS2bZCuHDbtlSAP7qHkzCC5zDD7E3rROsGblN7mWDK0KGk-1WHSzSzO6bCOBHlWzaAH6NYang1hzBvKRsatNDAUrwFSTQzPWdrmKRVZ_PYRQhj29LrQWM9jreStdJrTffLljHeyc6qz_YtNdKeQism7TnQgq0AVk9ekFKyBPB8F9zBnfxc7WozmEXMzfSr9slvOCb_Drler4gMDf_TULTQAtlNAaN4siwhNSngPwKnCkofll-p9SIKH2xdU4shV7x1WCme4sbV_fqrDpjiFJSxhpC-iCKst5nmowXMxesYHGp1cHQMbN3SK-GJYlKgohA0oIuHMMKcoCrB_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3iMH1oQ1-ZyepZGs1ZHazoPaB7CPvlPR-1AFyLjgVYW6DgONUgjxndbkfQaeFKBmc7NuylKmANRjUpcffQPWlpY5bQNnRA3sX423SmePByI9xoOThdWwitz_M26_sZBb0BnfGw3pMM-KrqXocUR_cLCfvcmo-waLxPqJU5lNF2XTJxJkD_xEMGBwf1kbGmntQHs35NViB38S29FmuFlw_9jxdYL6tiDPT9FuI0M6QwI2QL6DIVQClL7DiLBavJhENc7AZGUAw6aTZ_gX5OD0vQxu3czQRdJ_l0Bzq3CvQo-f1zAKzsb828bMXPfhPbnU3zNO2bn2sG1OXIWNglTVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوس‌دختر بلینگهام در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99801" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007eae865e.mp4?token=vq2L43W7IYsE5WUJUN5ZlwVndvTRR0pQt8LvyTrIxt51YKjflSC1dOukMuq9vPV2LMhwXhbqsPHzfwJf46KaRYYvwVyoSTQfocGe7u2yRhM3n5Vadg-FaC87v_PCsA03vQIG6uZ7O793SFwHY1NFwIV9icgIe7HdNRMhTulkUhgXxhIAV7iGeKrDQeM0zryNJcvnFDrFi0zhv5hq6bDoazx3KZ23nDLz7-ygTvNjKxidthgJ5pVShPSltos92zRHPUfKxJ1A7mC5SAqc9DSSSt-foY5soBh121Hs3jQrf4FXtOPzWtZo6jD0mm6s_gd3L07PiJwnbsNMIawbipsuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007eae865e.mp4?token=vq2L43W7IYsE5WUJUN5ZlwVndvTRR0pQt8LvyTrIxt51YKjflSC1dOukMuq9vPV2LMhwXhbqsPHzfwJf46KaRYYvwVyoSTQfocGe7u2yRhM3n5Vadg-FaC87v_PCsA03vQIG6uZ7O793SFwHY1NFwIV9icgIe7HdNRMhTulkUhgXxhIAV7iGeKrDQeM0zryNJcvnFDrFi0zhv5hq6bDoazx3KZ23nDLz7-ygTvNjKxidthgJ5pVShPSltos92zRHPUfKxJ1A7mC5SAqc9DSSSt-foY5soBh121Hs3jQrf4FXtOPzWtZo6jD0mm6s_gd3L07PiJwnbsNMIawbipsuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
مود طرفداران آرژانتین در روزهای اخیر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99800" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG8MWAuJ6_MmMWOYuix0Vr0RcMo5BVjQzmwPm6tN7EnwFVys0wlNv06txv72g9QjfpmKL3QXuKLkxtJZ-_SKPnqe6kvxslAp4q5dkxhmcp4Iqp9r__kn-onOf-DBc-5teYt1lymcHyDDGYcoB50IlLZlPm0ZZ07xaMcqz246oxgEkeuI03Kb5rUHMRoFrD90JVKxKz4IrXFmrC0Oy4VLR5TfGBvBO1sN5-QTQ7kscDXJdzMHGQWzimaiU1pGSq3nAhRai8DtuwHkx51Rx7bOKU6Nqhxqsl8e9sQhPjbZcbFRp9NiBntVmzYlG_Uci-NC-KoXWYeBTr_zWIrg9Ww9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hdepc5GgDhMXTQU19qh4JtWIH-q0CVtsPxdP-KOoMH7dFEc-mEy7EBiA0ZaZrpbFUtwFcCIb5zJIkVNI8kXVCo4cwrXaT21VWmun-DnDxjh-c8o2WUYUA1MtwTz68Vns3yhgs8QjA4s9C1dv9DEabDZoyt5fZU-gtQbHNu70vEdNlaRNwLGK2o442fEsVgV9jRA2HHfQTcKpyUppwcWptoecYtfaYFd79ZK8xp3HawnG6vIIgM8Dr7cJAnKhcgX_UoYHqH7xDiCew5TkbRQrhWjIXUOLcM6g3th4KAa8tbaBcdSTp5rTcIc9Ag5QK0EGBdiqCQVjnl5AzNVicBkg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2Jf3BxupOdV2mO4HDBmQ_I4fI41ydqmfLF4dvj5kfg5ZdqrZyERnjnwm7uUhYgTPhXDrPHj3Onv1JQmn88jG3NNwzmMjpU1MwRLE7FbasdJrtUQIuCnnMy9SjzctA7XvAhoQrK2Do9IkjNXnCDQR94qhHB2MP4NlZaa65NoNeUN6RL8hYWA8sB8nMYmkjpc9sqDa-xlmcqzGaMtMvaq4L60DI33inERn_K2sIcWXCveRv-XCW7wH25zFJbjI0xXwTLJnVLtfiWwJOmUwcFOW4SqwbAr_6mKv4LPVbeIRhVdIitVoqq8qjBU_81aYffOe8ykAXGlIwaWenrUCKFF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNav-f6NAm0VQQvcrlPQGcG6flA40Q6F71NPU30HnH-DYRayGbyACwQqBo_9VZpzcxd0oWcmenBM2ScK0oBzQwAnHLlVK3Sd_S_QfP4RZV4adVFmAVqNky1VaMtxMkl_tBNYFknr_GmXPXccl0tC2ywXDqup6QOlHwEpZWjp1KaUSP3ccvbmYDrocRiids8WQj3TVPL3_oWCgBThqD0stOMHhsBq8CN8a0vFlxFr2ZLFH4xhCyXKaT-XJ3HlDBGXpkFoaDMnCVcomjM1IhOGkXxViaipGFjbQOAhonDtgzva_Va-acsOKYw2EGGrnv-L-n_Yo0q9b-I60koaxKGgmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇦🇷
خانواده لیونل‌مسی در بازی با سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99796" target="_blank">📅 11:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
روایت حمید مطهری سرمربی فولاد از بازی در آوردن علی‌نعمتی تازه به دوران رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99795" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8IfPjNmmSB3lT3zjwZ1fWqLsNIsL8taWBsieGlhz57aLaHBdGsunt6mAOjqNKyzureKsAZbRvxx5AyCSKM5VhqPEX_CXyAXgIC7nOfldjpQE5mBAFtx6_1ohZ4LGsIGN5lyhOr1iKyVR2OgvvBWhSo44L37AW_ElqIvqsAvFA0KAYRQgmw1dUPNticEZJPMbUWTP4LawTdO8kFzMxDNJmjObZDAXKet3Dnygc1W0ceX6TBfRMbSemGgC6x4MLmQfCNyBGiSUfsYo5OlVtqb2p3pe6lOiCp9o7oLc1Mst-yVq8HMePuMg90dMmjnxLYPOzc9ODdkWZXzNFyv7jD16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti7pHQcucXbbLXxEuvUJ8jZ2dEVVD3jVPV3V0q8xoZKbjwhhYXUZE90thRDKbKQv89ZXXBxBoTAYY7eRdQjfVv0gCy0EsaY13-1Q7YVTBuxAk8VWbzmzcE6Ka914X3EAjbsxAjlMeHTi_eRcKwAAEp0_NNynTRHsYMroEDq0As6Vu4QqOcym3GOFldvIaMWOnC2wcR-_qtKmnMDpmNvOR9mU-z881ylnYmlTGfdeQHkoKjNdFRKdr89tp-n0x9i5xj51YeN2AXTNeIHyVGMk5WfbqCX0JLm0xChSkJmKMnorFhwm5LNej3azkezlYz6P6l0qjmrq1dB8-Gm5fu5mKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
فیفا شروع کرده به فروش چمن های جام جهانی 2026 با قیمت 450 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99791" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPxu9cAJF2c2ZVwZlm9CIaQ4Lq-p5PHC4AuOysErv2vfZFdvg7whGMKxlYMO5WH8BTkpGtFRFQn8NSRTTvE3taRXmJQQiaZwJX0kCoXMRilMhh_yA99PO5YQlh0e2NQqmqDG4XR8YdQ8Rzl7ZjFOTBX-L9QOQgteD-7zfMZqiWkGW_f-bg1kaLWRPrc3HF0WvA-4LvWKGovIN-mXLN0D7JheOwd7VG3zW6Tj3ul_XBsQs3MY9d1DbIb_m5ZPr7CaDwJ6dsanzKLXMk1JZXJsbNJw84mbMfoCwkOGCzuPJJcUft7ImSQE71u8A4pWGURjNCoNw9tALsdZiyOMfKs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">� بعضی‌ها فقط پیش‌بینی می‌کنن…
بعضی‌ها از همون پیش‌بینی‌ها درآمد هم کسب می‌کنن!
داخل
@betegram_bot
می‌تونی شرط‌های برنده رو ببینی، از بقیه ایده بگیری، شرط خودت رو بفروشی، امتیاز جمع کنی و جایزه‌هایی مثل VPN، گیفت‌کارت، Steam، PlayStation و کارت‌های مجازی Visa و MasterCard بگیری.
⏳
هر مسابقه‌ای که از دست بدی، شاید فرصت بعدی درآمدت باشه.
👇
@betegram_bot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99790" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=IN0IgqiYZ5d8_ZTdRH415iqmM1afYHPLRsv5Yyp_k57x-laCFLd__cjpwH4ouFolt4xwM8OMn_2pmbdCZzrUXFby0kWw5hA9kE7n6X8bmm88raw33XXPeAOdv1jg61l9ipH9OZoph5LGT8ie9_zo12Aslf0qKLMozz70QHFpze5RwNj5ullq9HfdAUBwG9J2ZB00xYzvOvWyHH-GXlXApqMpgjR4lKrXWcc3HLxq4x1B7ccbuy8GL80ZeCybcejFj2gam6jjN608yGCiHn0A-awQhjRytrfPTdKo1elUY3oBQifh51YaPZImzXwJbEg9MbA2Hng0JvnUmliRIv-y7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=IN0IgqiYZ5d8_ZTdRH415iqmM1afYHPLRsv5Yyp_k57x-laCFLd__cjpwH4ouFolt4xwM8OMn_2pmbdCZzrUXFby0kWw5hA9kE7n6X8bmm88raw33XXPeAOdv1jg61l9ipH9OZoph5LGT8ie9_zo12Aslf0qKLMozz70QHFpze5RwNj5ullq9HfdAUBwG9J2ZB00xYzvOvWyHH-GXlXApqMpgjR4lKrXWcc3HLxq4x1B7ccbuy8GL80ZeCybcejFj2gam6jjN608yGCiHn0A-awQhjRytrfPTdKo1elUY3oBQifh51YaPZImzXwJbEg9MbA2Hng0JvnUmliRIv-y7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
لحظه اعلام خبر درگذشت گراهام توسط صداوسیما و تیتر: به درک واصل شدن گراهام رو به ملت ایران شادباش اعلام می‌کنیم
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99789" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99788">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: به پژمان جمشیدی با تاکید خیلی زیاد گفتم به تیم پاس نرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99788" target="_blank">📅 11:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=LpucEoqlZKAVX8TCnDiGylK3xujvs132VoTM1FzL8FtIefjb-4tgpPTY6LIty0A7V53ot4rDFUnMMFHRo3rKjtF2eH8e41cJHwBYy2xevfPQX9U0VNxLglEfqmxCMAuDYRY-c2yhmRCMDAF__jAKxJkCfXTJxoNPLPIftZXhO4Pc8pFyVRhFulzNLABldwiOVZYyH7eU9SO2fhpKrHhXvbtHamorFEBJPEZRyg0CWP6Bw7BI_De53W6yBdg7VlFswv1Hsm4-NEp65SStwZ76VXqKo9tr38g2DPwD7iejMw8GxSY8Gv0MjuJmlLdrZuUfDZTNIu_Scwhk1-rVLKWVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=LpucEoqlZKAVX8TCnDiGylK3xujvs132VoTM1FzL8FtIefjb-4tgpPTY6LIty0A7V53ot4rDFUnMMFHRo3rKjtF2eH8e41cJHwBYy2xevfPQX9U0VNxLglEfqmxCMAuDYRY-c2yhmRCMDAF__jAKxJkCfXTJxoNPLPIftZXhO4Pc8pFyVRhFulzNLABldwiOVZYyH7eU9SO2fhpKrHhXvbtHamorFEBJPEZRyg0CWP6Bw7BI_De53W6yBdg7VlFswv1Hsm4-NEp65SStwZ76VXqKo9tr38g2DPwD7iejMw8GxSY8Gv0MjuJmlLdrZuUfDZTNIu_Scwhk1-rVLKWVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
میکل‌مرینو فرشته نجات تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99787" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=vC6P5AeUjPEy8Ff-oiWzux-VEFrCeKXWpgK8ouAIw0KNZXLIJBrpra0bpuDIEOj-LnoLpdRdY7Nhu1vsIdrCRmGRE3jDf7gtmCOqhMFpj4McnhmgrAnaWUEo5wBkLNVlbap29hQvASIQ7AziTi4M8PPo6bJ5Q0a06kiayJz8oKqEHDrQnYPvLjGgndwHaBFfzX_f7vxcn4-dR1lYjevErcn53v3D8QdpBlnAG-bBJvRV8w9VefoljMYPUroFVc6xhciiTEPJ43t83FcK6cwiX1w6poTEAX4bqLRi_QzzZPe0Tq9kaxcPXtOspNab2DiJ4FNvITfSAocdkCwZ9atKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=vC6P5AeUjPEy8Ff-oiWzux-VEFrCeKXWpgK8ouAIw0KNZXLIJBrpra0bpuDIEOj-LnoLpdRdY7Nhu1vsIdrCRmGRE3jDf7gtmCOqhMFpj4McnhmgrAnaWUEo5wBkLNVlbap29hQvASIQ7AziTi4M8PPo6bJ5Q0a06kiayJz8oKqEHDrQnYPvLjGgndwHaBFfzX_f7vxcn4-dR1lYjevErcn53v3D8QdpBlnAG-bBJvRV8w9VefoljMYPUroFVc6xhciiTEPJ43t83FcK6cwiX1w6poTEAX4bqLRi_QzzZPe0Tq9kaxcPXtOspNab2DiJ4FNvITfSAocdkCwZ9atKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
جوری که جام‌جهانی قراره به پایان برسه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99786" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiIAZ2VzHTKOxe3ru2vSPOeIgmclWUUpXq3plfxfw2VpNzwhNMePZ5LXscRbiWIjQOPBfLkQy6fMgmkU69Dh4udPqzpm8_qX_BvTVclHHiW1K5yX5Nrug9_Qb3p-waMRoQR-C5gmQAQOyP7y1POsW1J9FZNU4U8pfpuhp78X7afK5Qcsqn63uXPk_Z1z2mf_gjRjwaJVFXevykYfHCEg6igrCJ4vJEuK19bfJ6hwXwdXs3jfcH4zHA1j88pMvfTP9PuWjKc-iBnufgZkZ-W_w2GrNHgf9s0UHPHu-S5gZ7oWuWC3Jpqp8cXCRO6xFIFY6-zNYrfSc9s6RhkhQ-MhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqhrKzC45nPvQreMMg9oL-575aLiPVnnaE2Gy10LmTGW0BKQUK7yrmxRrfd2eN5rKobebBXWedUr0Cww9FQZWJ6Vg3cbqWmFd_FR_r5WfqWgUpfL0X7M_rmguj-z5rld_IhN0THNN3dSx15hxdO4v9dPDuUbtCAEsUCIpPjmobX3jMLj092CWAGhoqB8aMmoLMcv2bH55Y5Zx3SBDNYErDZ4iLvUUto2pBzBBGfpsW1gozfeEROHkCkGTPV08C686wnqBs2rjvq7iz8cJHL6wO1jtWBgMy9IeaYGfG2yG7qH26lzitS6yFi6qOKXXp2KpreK91_0mEbJZZ9ffcZYng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چقدر به دروازه نزدیک‌تر بازی میکنه مهارنشدنی‌تر میشه. انگار بیشتر یه مهاجمه با قابلیت‌های یه هافبک نه برعکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99784" target="_blank">📅 10:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=OSmXDnhM3EU3gk4fO6mMVKqOmwvwi_2g3G8-y4n3CvJSU6TZGkvdRd_2oFONsVPko5Bie6FeneLuF_F8ofT7RfC-MHtyK5OaWWziganwfvf6cAC51W12cN1F9Gs0YnUzupSnf43HaYlRd1v76DSjnZETs-Ui-Z7wLcz9pic3a09K043XmizPbCJZrq2sHfthkZHp7mtt0-QGIAK_lQcCwXD2yFODo8rc_I7eLfEOuCGAeGiY9znoRGOraTlriuTiRKw8P4PdMpLUAf3qQyvdldDX6tqpdKK94VADr50Gzax2L6Q0NqbL-wAFnmVlcfxx2b9TMOybCZKbR-nEXo22gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=OSmXDnhM3EU3gk4fO6mMVKqOmwvwi_2g3G8-y4n3CvJSU6TZGkvdRd_2oFONsVPko5Bie6FeneLuF_F8ofT7RfC-MHtyK5OaWWziganwfvf6cAC51W12cN1F9Gs0YnUzupSnf43HaYlRd1v76DSjnZETs-Ui-Z7wLcz9pic3a09K043XmizPbCJZrq2sHfthkZHp7mtt0-QGIAK_lQcCwXD2yFODo8rc_I7eLfEOuCGAeGiY9znoRGOraTlriuTiRKw8P4PdMpLUAf3qQyvdldDX6tqpdKK94VADr50Gzax2L6Q0NqbL-wAFnmVlcfxx2b9TMOybCZKbR-nEXo22gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند اینقدر حوصله‌شون سر میره دست به همچین کارای کسشر و احمقانه‌ای میزنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99783" target="_blank">📅 10:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd9vvxjkmjtgZFnnmkKQS32Cf8Py_ZYu2q22h0r2CU_YxAkVxi3xJBX6zvcJo4tfqsnppOhinci5oi7WuKXRTtYUXFPVqUwvEVMfbblukzZW1OWQZvgvE514REVpf-n5fErjkIny9Sz3L6VjUzIN_9EHdDVd2gUp0g9Rx5hWpfJa5okg52CKIaYm8RkfsC-vpX1OE7awIT9LrcivUENRVfLdV3b4JVgaThwe43hQvNSsOsi9uiYmveprE7hLCQ3vCp7D9DwtbQPG5sF7tL9FAhe1I208C5BeEgsj7RYFq5wCa5yloKrPB3aYCVRnjNPLUKSMomIu4OB1NhrvDbwS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام سناتور جمهوری خواه و از حامیان ترامپ بر اثر بیماری درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99782" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=SXNzfwwKsOWk4SOuctyKpokJos2CVClt7ua5HSzu3i2dkwt5tQsV2xrbIqmLM8WtNltSf3H9ON8PMs8GZcVBraSS8eXVpqyGCxvbzXUteKwAADbJGGykZAKfTD_bal-dfIwYvr4zWZ1UsMECFCwWVPCwlUpoYxhFKMUF0OpmFbEpYW4oz4Sf4npngHIKYTEhTzu5EVN6FqIQWmzgPfF6XgXniAGubA6YyvYFPiPAwOxHQeoLcfgQsMwbOoWQeNirs0WnEjlVly8Fg7OyYdlJYXm4bSoQ57GyDe4PVMuAtxkIYFRkbZqI99iMO71mEmbYHvr0OPmoXaxrvhP9Vdpf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=SXNzfwwKsOWk4SOuctyKpokJos2CVClt7ua5HSzu3i2dkwt5tQsV2xrbIqmLM8WtNltSf3H9ON8PMs8GZcVBraSS8eXVpqyGCxvbzXUteKwAADbJGGykZAKfTD_bal-dfIwYvr4zWZ1UsMECFCwWVPCwlUpoYxhFKMUF0OpmFbEpYW4oz4Sf4npngHIKYTEhTzu5EVN6FqIQWmzgPfF6XgXniAGubA6YyvYFPiPAwOxHQeoLcfgQsMwbOoWQeNirs0WnEjlVly8Fg7OyYdlJYXm4bSoQ57GyDe4PVMuAtxkIYFRkbZqI99iMO71mEmbYHvr0OPmoXaxrvhP9Vdpf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
صحنه زیبا در حاشیه بازی نروژ و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99781" target="_blank">📅 09:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=J4fba8Fnihs4gPokgYL0MKNkigg91T4qHNkZ5bko905BVZX-5USNCsZDB5eYROvFoDD2vmikolIjhB7A6dUoihvFjOY4cWOh5YaTy0x9tWQBfjpqIa0viuGNTPybpsDgG88taDwQqwlcG_6rMpRSrrPmb0xJ1rX8p7sAeSS0FhCftO1wCmN6otIRscdsbWiu2liuL52i_cqPXQQMWZKbQaFrbwf9t__zoie319x6Ivt8fhps_mniJcrB1DOn0yHhuTHMWNUqiM9TW_pqm4dMG_wtImzgGdPonJD09OCzO_arYp0BmPMlxN0yBqUVvMcM8C_1utQsnOsIECHKIHhuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=J4fba8Fnihs4gPokgYL0MKNkigg91T4qHNkZ5bko905BVZX-5USNCsZDB5eYROvFoDD2vmikolIjhB7A6dUoihvFjOY4cWOh5YaTy0x9tWQBfjpqIa0viuGNTPybpsDgG88taDwQqwlcG_6rMpRSrrPmb0xJ1rX8p7sAeSS0FhCftO1wCmN6otIRscdsbWiu2liuL52i_cqPXQQMWZKbQaFrbwf9t__zoie319x6Ivt8fhps_mniJcrB1DOn0yHhuTHMWNUqiM9TW_pqm4dMG_wtImzgGdPonJD09OCzO_arYp0BmPMlxN0yBqUVvMcM8C_1utQsnOsIECHKIHhuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
واکنش تند فیروز کریمی به عملکرد بازیکنان نروژ!
فیروز کریمی با انتقاد از تصمیم عجیب این بازیکن گفت:
«اگر دسته سه تهران هم بود، پاس می‌داد!»
😅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99780" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0TEFWCly6fU7ir75s1lZGsFeSRYAagzWNijS4U0a7mXnxAlC2dx5LOYc3jHxheRg_7XpJyQyvo5eknj94YCJ14LxvYxVzs-gA8rITkV1O0SXm5xe3JZLHO--khqMvGGWzlLp92tAIIiqmF8z-7Tb5cWIR3OeaDy5CfPLYG-M8z0Yh_7bobeBhvJd-qUVdVVHMOg4k2LHB0d6tQ0AdeKeHHpF2j9OWLIKv5L5tmQag5BkqNQem9aGXKeJWK3C4aS06v2vdXTMUmhHVqUN5MjE9rzQNvSTuQUe7keUZ8Sb_soA-9Z7pAVweq2Hb180mK18-MwAnWXYJcjlxOhqVSRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک امروز 1 میلیون دلار رو کانر بت زده بود، که تو 30 ثانیه اول باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99779" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=QuI2IbsYNSQzYFkHsids1kKhmMqOEeknWxm8KJ3YSQuMDoSZyf6LeMbRjYEGlj-AM4oIPBbw60YOUWf2iMdPkiW3f-6kVFJHCbT2kHAKNptXV2a7j7D5o8d08TciQZyYpIiyzNnTc57ldazeKe99biNcClnaJe-2qozBWqE9_wID7xRZ6Hx6JQG0HCsuIZeWeGyQEBIG_AU5qYe21gmDkGwQIJDsDT8tW5HsHiTf7EMbDaWJcuA-SLKVM56B9djwPpOAt4twmLQEyyxbKHnuGqODzml_zDeZx9K_igzTPSNx-xaN_eW6TPnV-0XtxQxHXZeN9Z5hdkfBCDiCyGwkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=QuI2IbsYNSQzYFkHsids1kKhmMqOEeknWxm8KJ3YSQuMDoSZyf6LeMbRjYEGlj-AM4oIPBbw60YOUWf2iMdPkiW3f-6kVFJHCbT2kHAKNptXV2a7j7D5o8d08TciQZyYpIiyzNnTc57ldazeKe99biNcClnaJe-2qozBWqE9_wID7xRZ6Hx6JQG0HCsuIZeWeGyQEBIG_AU5qYe21gmDkGwQIJDsDT8tW5HsHiTf7EMbDaWJcuA-SLKVM56B9djwPpOAt4twmLQEyyxbKHnuGqODzml_zDeZx9K_igzTPSNx-xaN_eW6TPnV-0XtxQxHXZeN9Z5hdkfBCDiCyGwkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در نیمه نهایی به آرژانتین رسید!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99778" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=nGRp9FX9KTQOn9ug_BZapxaOaG44yu7fMmB5z8cSMS0Y8k_Lxyd8qABH5zfeT2cF2gBfuZCuX_8_Aa9hTLkjHBkKTbEsNIT5uwWjknRpmdOq8oe6r3ec7MhxCuplGo4ti24-L-i0IqZsxF8WXa4e24frI4yjvmrr4Dd1PzFW37BYj1LqvcUyon4o9WSwC8VMbURabBoTwcg52FrjJEbRsFrRRqcDUPBKX8WkN0eiA6lK66tZ_o40RupoV2ijjoM6HJ6m3vcN9_q2QTxzJwHnEDO6zmPI8WbvOm1E-OJOCBbe00AtJlBwi5mdaS_yXvzi1rWOnEmlp5Q8Po-XkcU89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=nGRp9FX9KTQOn9ug_BZapxaOaG44yu7fMmB5z8cSMS0Y8k_Lxyd8qABH5zfeT2cF2gBfuZCuX_8_Aa9hTLkjHBkKTbEsNIT5uwWjknRpmdOq8oe6r3ec7MhxCuplGo4ti24-L-i0IqZsxF8WXa4e24frI4yjvmrr4Dd1PzFW37BYj1LqvcUyon4o9WSwC8VMbURabBoTwcg52FrjJEbRsFrRRqcDUPBKX8WkN0eiA6lK66tZ_o40RupoV2ijjoM6HJ6m3vcN9_q2QTxzJwHnEDO6zmPI8WbvOm1E-OJOCBbe00AtJlBwi5mdaS_yXvzi1rWOnEmlp5Q8Po-XkcU89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😆
😆
😆
مکالمه پاره‌کننده دیشب هومن افاضلی و خداداد عزیزی. کپشن اصل داستانه⁩
من از شجاع پرسیدم!⁩ شجاع بهم گفت! گفت که بدنامون خسته بوده! خواب بوده
😂
⁩⁩ ولی هومن
💀
⁩⁩⁩ بعد همون شجاع
😂
😂
⁩ گفت غضلاتم همه گرفته، عضله رو ولشن!!!⁩پاهاش اینجوریه دیدی که
👐🏽
😂
، اگه پاش اینطوری بود
🦵🏻
آفساید نمیشد ما الان بالا بودیم
😂
😂
⁩⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99777" target="_blank">📅 08:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU1mSi0hbQbATNLnZ7hV9DXg7QeGLyc0gRPnG37olSCijOd-5CZQw85YNWV6XAZCmfcQYndiLXR5xOjhsJXHVwq-6_WwqGgCFGMet0IPOoK3XyblRhsoL8N9GKG3AK_DGAgt6G5Rxy3c_9XBanmjriUPO-_vEsILNq_NPATJ-jSbieueQY_gweprzVf5IBIC48tyD3IwDLmkFgJ48HOx9Z0lDlIdnb4-5PlboT2AsJOtYY0gOSe3FgHx_0wj7MEN4ITfmkA1-vP_qqasnswrvbRpSBcYIQ8kWydMh5J27OIcOS150c9KpWY5WRE3O5Z7eQAOj_szMwawfM1zUXblYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی اولین بازیکن تاریخ شد که 15 بازی در دور حذفی جام جهانی انجام داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99776" target="_blank">📅 08:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mThI6C14MDzhJCvEOY19cYcEEnYlEpHmOj7pYKSkURLogxyfNKo9_lOeeStnNLmqwjLTkbY-HZxqixXVtNWRxNXuYMzYiV3FkNWzCNFRyxGdlz4JxFFZkdwrf9soTbf8heMHQ7LVz2t86fkrtWs3AG8VkFL9oUbW3dIm48aAdKL9GiS8VadX6d7Rnyum0cFfJKlwca_4Q0Xpec97TXkhooRSYqBq7kt4MaE0UMkS3co0Jct96Oxey8xk8WW0Gub6I2N5Jq-CdxQDrcdR--NNCZyyUEm4BsdzXO2JrlKehjb_BZCnwU8wU7tqVS3Ip_OOcV-MDD1BhcjroN8n1AP6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇦🇷
خولیان آلوارز: مثل یک ارتش پشت‌سر رهبر خود لیونل‌مسی هستیم و هرکاری برای قهرمان شدن مجدد وی در جام‌جهانی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99775" target="_blank">📅 07:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD9o-6sxVWeRswcw_NWjRJzjfPACyUrnKRq39iHwH6-iYxk2NdTYVB1G6FZJhY3hZMyjKsKnTpsE65RhkdyCXgiwdhYdeorqFS3M00clej2y-2ItXqT9KynUCtUDGjaghYcDlc6q_q8yb08UE9jbjbJqucWMFl_uisfx2DZ2kb3VvpH8mWjED0w-4ALiV6BufDbKc0RH7RRYagOILmbBKHPZ2BEw69YRJ1ISv6Ff2BTL2D9-d4YmbGeXn4gm1euJJgWK-qz-EH7_-Cim2Xuoa0j_Jd3GHcBL4NLTdqhijgZp_UKYBJU0HWTK_IC994-R-us-VII7ca715X1IZkX98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تیم‌هایی که در طول تاریخ بیشترین تعداد به نیمه‌نهایی جام جهانی رسیده‌اند:
‏12 بار —
🇩🇪
آلمان
‏8 بار —
🇧🇷
برزیل
‏8 بار —
🇫🇷
فرانسه
‏7 بار —
🇮🇹
ایتالیا
‏6 بار —
🇦🇷
آرژانتین
‏4 بار —
🇺🇾
اروگوئه
‏4 بار —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99774" target="_blank">📅 07:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMXVA58Qz4-37ZXzU1LnWCqtJ4loO51dJxmZjg7KIAEi5kxwq6rXiHCLsKmi8n90vOqE_JBu6S5eK0LjKENZkjEBjrNBBN1Cqad0phcoafQFa4b6dkO5KRNlxwwk9JwY2GaRGC8z1pTtxcJss7mHvDLHCTKooKEMmpu96rZv-iwvJqENAXEjtls3c9JiGXd5AClN__DDeDR4f_O4FFfK77DlEieXrLuw6G5RkipgUYeo89bi0i0U3nFlticweUYcva9Vm-yr3ed8gKJaKpaPjQVbqugdR54nsNc353wpApPvyqgZC-n0JG-VaC-vGuA21AgM_dslqtjPGSDmLVHRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
خولیان آلوارز رکورد مارادونا با ۵ گل در مراحل حذفی جام‌جهانی رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99773" target="_blank">📅 07:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuNhy4fIBLv1BL94tG4uJNI9bgvq6Mfj9ycyy79Diq6tfFTSyJg0b6ZTP8lkqLyvjo9glZ5zM7OI_3GFM_xSx3RW6eSyzFa1mN3RsnuGd8KMVGm7d5kSODtkNqcNTXiEkF40hgruPncwIT3qD-tLV1xVbVNat4za9idP-roaEJDBbdZMIMjqrZVvsuxGHRKlSLirQZzc-8ulXDHob3F6gewRUliX2ufyRWJ94weUaeg6s8fZ7Mzlaa3KoTnADSHJq_t8Cayl9qfE2N6NdG8U-ILe-pujrB76vCpEQsznzX79n5hllzT2-bzvFiu7UVJdfAl7qJuoo0pLsbLddViwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آرژانتین نخستین تیمی در تاریخ جام جهانی شد که بدون مصاف با ده تیم برتر رنکینگ فیفا به نیمه‌نهایی صعود کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99772" target="_blank">📅 07:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF7_Ll2ddPzPuh6Chw_pdngAZzbbTfKA_EilkkNlWTopOYOXtmQwBLWLDCdQTLckt_xa61FNCbGeJoFvNK8VUnjO7tYMmvsTEyO-ZyuuJklSSZWiGUnFYTYiFtVIhIC5pA1pUNK1dzqXpKCHyugl2oqQvLadESWP1og-aDzwnWgUvCT7-uwYMDFyERc_UTcCN49SlaVeoie1yEvi4O_ajDoRMKibW2K5Do0VrAV7FMgOpFnEScGAO_9oS0Gx3OkXjb4cXsvWGqYwZOjOOZ_cXIODeFbpfno-0nklVjtiU2l_kxFeaZhFYr8-SiJVEWP2teUovhLeceCJVAJmFKgLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
| برای اولین بار در تاریخ جام جهانی، چهار تیم برتر رنکینگ فیفا در مرحله نیمه‌نهایی با یکدیگر رقابت خواهند کرد:
🇫🇷
- فرانسه (رتبه ۱).
🇦🇷
- آرژانتین (رتبه ۲).
🇪🇸
- اسپانیا (رتبه ۳).
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس (رتبه ۴).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99771" target="_blank">📅 07:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=rWrtQXEa2AwrWeVcLdUk9T3Lzmbf2lILxwxYLXVZtszKoAb_IaK_lSjMGiZENezht008SvKZoycnJCgAH6pe7J-A8Yyk39rTXgSdN7AgzR-kRBKSB30m_sNjIrmBmh5iqXrVXp2GTL7dkRAe3ITVbKZU9fhjgFVyXamCUyjh7Gp4w73xr1Hqnt7vPMVlsiBe4BGNse1_A_Y2zUIwdDnRjZ5zTebrS6kE_-0foWvRBnuH8s3MvQT8DeU8qD2rl9JxgBXO0XuKCffKrBkCwZzLTTeT-8aq-PipmQYSfJg0J6AntCnFxllS1B7E3xps71bSWatiHUyatEOdNNqRZuKKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=rWrtQXEa2AwrWeVcLdUk9T3Lzmbf2lILxwxYLXVZtszKoAb_IaK_lSjMGiZENezht008SvKZoycnJCgAH6pe7J-A8Yyk39rTXgSdN7AgzR-kRBKSB30m_sNjIrmBmh5iqXrVXp2GTL7dkRAe3ITVbKZU9fhjgFVyXamCUyjh7Gp4w73xr1Hqnt7vPMVlsiBe4BGNse1_A_Y2zUIwdDnRjZ5zTebrS6kE_-0foWvRBnuH8s3MvQT8DeU8qD2rl9JxgBXO0XuKCffKrBkCwZzLTTeT-8aq-PipmQYSfJg0J6AntCnFxllS1B7E3xps71bSWatiHUyatEOdNNqRZuKKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی عجب کیری خورد تو این جام جهانی اسپید طفلک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99770" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkcSoe2sgwOiiRRt2AfODSYKGNvX6uS6doLMYXZDUT5plrXMYeYn3IyP0Fq0daYpzJsGizNx1qxW2FsXnZnixL1IvV7kFOsLVmI_GdcMK-vXSaBvbT37HAmSHMFt0L4tnreG9pnI9Mbbi0PBbGysAe2Fz-tU5NPVyxfCKsBm14GBpPu74ALa8rG3Ph0KQ4Prruj7A_vMklI0LdhMWhcomXl4Lcyg6n01hjY2DQ58AwIgb_gJH_cyrzkHjsUynySajLM9Ky7ATSCeuO655ldsXN1pOpcVB8zB1lVa6HrP_wCqjFRpQkCH-9cRP96VHa3d6NnGSRfMO_kZcD2RO3loTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🥶
🥶
قهرمان رو با ریکشن نشون بدید
🔥
فرانسه
❤️
آرژانتین
👍
اسپانیا
🤯
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99769" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99768" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJF1C9nmlaWl3SRP2Z89UW1HS4KeSPSHtVbN3nIYLnGR-mDtLV_EDDjFUsR40juNinLLh9mFxK7isTQvogWlRhUcMZaOcIthvHzBJISgeX5X0IDS7uvil6ZtuswhgJCPXY4ItorGZBRjoL2JUkZqAjhq5AkZ3wwy4WT6ZsrLNlnan2fdpb0V4F_trVz9PZGCd8k6LdTiMdpC7pFtxd2kSlk0huI4E56P_fYJ04GegJGpd9tS_PmafX5GcFZKAunJDhBiQ-SKWzXvAtUM1VeC0g5UOk0BdYSxABjxzEv0xeW0Mw3NeTB5V6MOBOIdtSQniQNQZIdyAlfY7DgYw-WCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
برای سومین‌بار پس از دوره ۱۹۷۰ و ۱۹۹۰، هر چهار تیم حاضر در مرحله نیمه‌نهایی جام‌جهانی سابقه قهرمانی در این مسابقات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99767" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMoZrbCo5rgiYJHwJ4DFSX2RkxFCS1cb1UmNhDEITlnerqATBdO9jwxBkkUvC4t1LmBaZQJNCbH2ojd8PHks02ma4wHFpmeJ_a4VnuB5E53EncSCIfs-dOCAPA4TIlbAqxlHzPmc178QfWlLqZWlrL_v4tmzhd0ZyPNICtMxUHVmENLbSSH5cP_iHNATD0o_9MszO7QPX0JSEE3o9ht87FC7OQ2Pwv7yaGRn96fGOTNoVwb_fuJXTeft98Gbz6nI_W5sDwyf71PLQr6x8bKEuBLtHve-NrAFRbT7ZtzYuYotW-zE_ebd7bRvQ4BXVvImQ1ttURXaWJr4rzpkWRDqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسو ببین یا خداااا
🥶
🥶
🥶
🐍
🐍
🐍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99766" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TNncQa2wsudx-XPakzZ1keO7gJj09HDKVWRO82uW6Y9_xh_5f-dkKgAocxHwR4wOV-rbOBGDEqkFfvKAaxMw77I006ANCJ9XCpG5lgSdzq6Tc0ELFB-Z7kTvp6Yo22Q59RplJ2kN-Uv-yJNGynpB5rGetZmebqOhEyC7MlB7EQrq_fdZTjvOTiDxpr-N1gqeo4Qzw4vaJgG7Pc0W-H-SqjygG3BWk22-RW2_EVijMs4eXMhakuVWz6LiYjn--_5LwJEbcldGfJUFg8iPi1Utuu5BYqJGaxqoFt5_dWsaSghpbx0j7hLMfE93PpQ28Z8N6b79aeNpd0OWoCMez5Mt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی برای اولین بار در دوران فوتبالش، مقابل تیم ملی انگلیس قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99765" target="_blank">📅 07:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbINAr4h9KKKfNx1dqRxugPG6Ofs927l1sJrzSxekIHCQs37ikkc8XD6VMy-mXxSKVzKfujpm44ltY1B3FY3gOWOvzvL8NLFsXPeWO2OE5xPd_USLhyk3sXrFlYSXWWRKoBgi_3PgDkhm9CqLJJ3Lb2DHVH9xEV1kmr_g5BEtLk8ycWEiug9nbwnQhHx3gDKpTVNMLIpTNv5pF6jA1EWQf_HlRfmzQbQzVOfH_dzWqiDfo_XM848HmOzFLhMyYul8Ts1OLDwMhl__pHc8f977LZRHXQH3WeCoER6eJNQJXP59fgTSxzTc4PDyjAei9OsLf0qAKapMr9JgebWh6vrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99764" target="_blank">📅 07:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoMRv2HCZ5S_xb2yDZW_9NxFju-yTv5vejY-QHlEvUQ2nmTxvv1SJ73p5GUzR4shvJZQyEq5Kd3LG3PlimavphZ2VdSbSDbKUdT5nQbWmR1X11o5JcU0QH9jWM0KgvJfJTco0apZXvELyE-5x6t_ZtrFKHwOBHZRzE3e3b2XYd9nTf4qS682u3Q2S5r0sPj3SCrmOoK5DMg4SE58N6CxVA5vGykbw7eNNLHerSNj19Ms0kvOmgc5_Db8OZ12QBUq1t7w60mVJi5Co3qeUrcRRZ6MA-lbf90IOKRR9X8B5vkRrZv0dU8oJix3Ar0qjmS9yMXQCpdduBr33mbTzZPPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99763" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOOcJygAh4ehkLRyPclgKs79W4WuYRgkNiRi_MxOcC8UJC2KJQ5O6GIi4Qj91S6X8056NPV8P0Pw7gP7wm4n4UJwJEYddtMsJa54vyNonQ-gWnPNBwQij4XcjCBZz_Q2JxB2rI_iq0LuUUkDdNrerKZJZK4vBZHpOqoNIyvvTJQ6Ax0bXrnMIaCnMrX8FVzjIg9Yqpe_05KCWjzW5WnXfdKpKtUO0myhdHfk4WoUFFqvJwMkNFJ0wT_QML6ASybJeCkjr3JuRQ4mV1_guwYAdL5obAzR4DcGsL6-0J7VkxSqretXZ8HlIjAjjLJe99KlrYdNw3KbdEmFKqNyORQOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99760" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99759">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXb9ni5CZkIrdGIWCqCdyeDh735nQEcRvMAv7ZI6TEL0QTcGpwqeZfgh-lTLETo1zKFy-IKyOpL8VhXdzJhB9tGSaigEWEtM1AfSEUMDxD5uFtS7rNag-nhPlZxcMecE58BW02AaZEbFvgKoEg6DdfcBIuu6b4tdE_VdTLhm7A6ZLWqgm2LSBmEUl4j2lF3U-g596HYjC-koJ_aA6BmIVkaHLkfCYz6vA41wyISx-9o03saQgoXRWvKYLhhL36K2fCERT3Ll0lpw9ciJR1Kt9JFCV8VyK2Qx4gtUUnaNboppJYp5biXAJ3p78Uce8epoHq2V-Y97xRlVF7VSZ_85Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
تیم‌ملی آرژانتین با برد مقابل سوئیس حریف انگلستان در نیمه‌نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99759" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPAKdIBg8MGQVgzArqKZsw7VSfj-4AnYhadNoA_W1K3KkaRlfWkeeLyReJBaSw7jneN6DuI0NpNHbweHB5BhPRMFW-HRno82tOS04n6kibF5iHUw26dBM7cylEV_Y3WUQS9nJTCaI2aBVWl3u7MpImpArNJJVVIhxm744BKynYvE76wPA4O7cYCepexDOje0vyzTaZKwXA8gnAefuAF31YnlxGrHGoSVpalti5Y9wryABVSyZ2CDGzfTv4lPx4KWPXBbb9HadNkonDc9uyW2PmDbQtW-YPqK_x9NyC4ZWVJzcb4tdLYEL-LKNCWKbMZMl6QheDclGIS7DokLHIXi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|جام‌جهانی برای کشور آرژانتین به نیمه‌نهایی رسید؛ تقابل با سوئیس هم به ۱۲۰ دقیقه رفت. پسران اسکالونی با نهایت تزلزل مقابل سه‌شیرهای وحشی قرار می‌گیرند
🇦🇷
آرژانتین
😆
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99758" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارتینززززززززز</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99757" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">لائوتاروووووووووووو</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99756" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">و تمامممممممممم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99755" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99754" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دقیقه 118</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99753" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE2Zc9qUvGzzjF1Ntp8_vEI1zLF0a7Vyencwx_dRyhRfub2mPxsptlRJW9AJxN5OENkIZik11icUeDtrIArptiqnwVBaTsmQrLqtsLrHj-VQk0yppvRpbz0pvwuBzUZxfnyiCdWvHUof2-u2pIJVhXrM5JHT-HIXS8mEekea59DBpiw6dm1sroFegTDikIbjg_J9Ko2pwaolnkn5sxUilhOiLgOr6T3chhyeGCPdJxkQ9BLCAYo_7GKlKdwFpzS6HzzUslb3Noq1uJb9QG4f8Se_G2zxHKRaSZJPuXMh1ypNprORosav2Ycj5nHrwaKyTk6Ughkclr3xyP_S_BPLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز توپ رو فرستاد جایی که غم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99752" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW2lbDwnd67iAgJ4b4FHBgJTCi4wAyLMifmkg5aKdaLVt-MLwDWG1oydZwrS0w2ypb5Z60RIudsh6kgz1DI-6xEkrRCYG9gJqFK2g859QZqQiiAhcXedPhtMjIs-IJmFSEjExSXKlG4uHyQHY8ef87bbKPq_aYNhRC-h-oAyKuABtKUxvgdb4nMAjizXGtQB4PTjxJe4cIYdGDn17AkfNczY_bSl_jh950yqI2ogMZp_6bHq7YXFiTKtWhy0J5MOVuMWqYW7eESYTy1LZjEcImnF28SHRn4mpp90yw5-60tSoZD3Ct-r18k7UUFgz5uCDKa_Zs6Od0kXRF7n-3jeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب جوی
عجب جنونی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99751" target="_blank">📅 07:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99750" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آلوارز از اول جام جهانی نزد نزد
چه موقعی زد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99749" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
