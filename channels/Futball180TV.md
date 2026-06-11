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
<img src="https://cdn5.telesco.pe/file/m7C5MkWIvgY_2OSkIc2S5LWwZzmxepfG_r5vhUHNV-ZLeWKAKULt7jwxK40y5OuFioqr1mKyhDXv2-Edh2SZaJRGXBprZElMeguQ_38XBNBVr9UxKE5JbnaOkNtqN55RaF1yv7UsJGihDH9zwpaC1BgHXo0nk0VDQKccryTX8pdNSgpv0Zp0EPsaiKm82K7dPmKyccU7OQ4_M3_1SCXloFJ78LSExnm0H8S6hfDk3QYYo16jS7it4HsoX-HSzhrI_CNTIr6LPObh0xCMfwi1I1qp3hnJ8vIo0uJq-7TwYpA4X35nREfBO1BcORgxfnbgBVgeKwVZLQF0ERTtT1USTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 336K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-92039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
همچنان از بانوان ایرانی با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/92039" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAOUk_xvuUWC803wCVMmw-Y3WV0eiooZ-f7-XakqVZjvdB_Ei1MNyffdqj320gA4-qjk81VwOOUuJfHVm2yWiBYGWuGk1tS7FIIBAcNXDwv54BhV0UOl5szfAViDV-o2F_l24UQqiwqddd7urrtcFf-06rDEBdAevTeeocSveV02h0vZhIS_QAoyJdCT4PK1nz8zZXlvYhBAS8MGbUoXws9D582l1jCIoR-1vcJKUalmBZsN0u8XHSuFJeZmUnoQu7HqNIqcDijdy8E5k6R6_fy4Uwu_mJFazAqnXw3I3sa0TN6ydydLUprlNyODWXGtKHdkdaNH8q6o3PheT0LNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم های منتخب جام جهانی ۲۰۲۶ با قوی‌ترین خط هافبک سه‌نفره
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/92038" target="_blank">📅 15:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td2Vq3a6clHO2qQJThPDiesHHVpw2TrNOxt2x4Oc_mFTaDd7TsQnFdO7CJgXstC0mNEt8VRP7iCLnihgfrzQTZzSaf9xzqpmx5IhyUBKlJuPVfwm_LKJT0O4q3SMwuSUcFO98EwiLI83PKGrlLfhC-40wJhI1fuHZ-IX0nYgMqAF2OWGHUgXRohpgjWCZVkFzxtDpPfm_o7wVjCbDhg_kPA7ut7jT3Rf5HswsCpDpeYwtxuBf_fAi7r2CZjss6_yw1SOA_7j20cAGRXZsiOmsHFg7ozluAgBY2A-PaDeNzBITYYyfM9XCmXU5YPj_7eIoZFzRXKkAqUrZ_sYP0XyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر غم پشت اون لایکی‌ که شکیری کرده هست
هر جام جهانی میومد یه سوپر گل میزد می‌رفت چهار سال دیگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/92037" target="_blank">📅 15:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✨
ورزشگاه خاطره‌انگیز آزتکا؛ محل افتتاحیه جام‌جهانی فوتبال بین‌مکزیک و آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/92036" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که جام جهانی ۲۰۱۰ بازیای اروگوئه رو میدیدن یادشونه فورلان تو نسخه پرایمش یه تنه کون همه تیما گذاشته بود، آخرم جایزه بهترین بازیکن اون جام جهانی رو گرفت
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/92035" target="_blank">📅 14:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDZKmeHScKqePK09h34Yitu3wKkNBhfZcEURgD7iEUFx7X8kmfWxBi-CWKZjzQHaTKlhuuVj96vXCDoSGoqfgGhfwoO640WUKBDtqS-E0ajIABwefglr37QZlJu5hE4QXz1EC13sawh18J6-N2Gg9pH8N3YlpgdGxlabvvtbbaE5lJUA-vPHayFPfjy-6cbNBr37TANslRiSNWKNgJ0bBUuSXyxrqOirjYCEb6F5zGAFeID5goMbDg7g4uKUPBeGW0cfZWkvLXG5_8bL1MT-ThJLZ2x4iViVwM_Gln3Vk4G5m4NUs660IR-uz_VFOOIcDCnEoHSTMU0fwyKo_4xP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نویر از جام جهانی 2010 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92034" target="_blank">📅 14:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0LOqq5mVYYGAheyo9Sec1ImUD_ERTqNj_rAAu53M0xZI4WHP3VXVBmucgEiAEBP-MNrixA5Cjvc9gdfzVyl-qkDIP63bJTa_KBjjwjvsUAtpRTkXIl9hgmw6z8PlDsZO-Yl1nj5QSmtiCcYbPHZF1AX94HzZ8mnQwktYTjYL8OlKPmMSr39SbcYEzvH5aekUSXTth1n1CY405NU2ZYXns79hRs7_8OeFy8LvHmd8eaVuEwTVv-mTk1tUmDH5afeYxUuhTWa-VCFEYAyOGbmZW7PLtMiN9WcBomlTbN3QdwKdL4r6PW4PZXY6TVN1NShLXfx1jrJNtrF9JMvj7wSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس‌های اصلی قهرمانی جام جهانی ۲۰۲۶ براساس آمار اپتا تا این لحظه؛
اسپانیا شانس اول قهرمانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/92033" target="_blank">📅 14:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92031">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdWVrE85iwLV5BIgdAJfZIWKY7CHT82l_DpXAB446aBcK0b42sulgYWIk1ieIqiA8MhtTe7eUWpe0W2iCDNOdcqnXijrIztAP6bEonHzoau4WzNP420SgruK7YzBiXPjzc_Vy5pSo6huJqX82OLPqcLIXHetD1t-CJ8YKJIrJ7RIdSaWv1pKclAp5v7NdU8rwn-uIQcHAfSE5ohGmUQmp2grXAIPQC_3VODbyUd3cc2fHjnTNj7IlPcRIHozAyN_2WqquOQHmULlcFmgyBY67hG9gaOOTdDvv04dxUczSEVC-gUnas_HC_Ok1CwsFuV5OgxB4lbBC69wpEnKowqVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtRDnSoeYPxaxi9JiuJZwsRXD5nc3P8zYuFTFxCxtxgF-gGinPY2PCqDfLWMrlldmAh1XFBlR_JnVgGtb89AD7MWXJPvREOIj2ezS31MZ6rW7-xbXHCW4f0nq2ffYYNQJhN07fCf_Zbquxwnojpo00Gh361kVvPvFl7ZPp6jSV4IJ8e2svRezo_F-qBeZSbN07UJn8khV4097KBRWnFOpNk6BWW-7r5mWG1YkczzbqCCi3pa3M59pgFD1Osjs6cWPaVfTmcdftmCub1WxTrnfRJT5kU3G-Q1sOKdwTnHHrpW2oOt34EHP1nIkcu31XKDDY46U3jZI-8eaHCfQ0ozww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکوردهایی که کیلیان امباپه در این جام جهانی به دنبال شکستن آن‌هاست:
🔹
اگر دو گل بزند با عبور از ژیرو با 57 گل بهترین گلزن تیم ملی فرانسه خواهد شد.
🔺
اگر دو گل بزند، بهترین گلزن فرانسه در تاریخ جام جهانی خواهد شد و رکورد فونتین با ۱۳ گل را خواهد شکست.
🔻
اگر پنج گل بزند، بهترین گلزن تاریخ جام جهانی خواهد شد و از کلوزه با ۱۶ گل پیشی خواهد گرفت.
🔸
اگر به فینال برسد و در آن گل بزند، اولین فوتبالیستی خواهد بود که در فینال‌های جام جهانی ۵ گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/92031" target="_blank">📅 14:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92029">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🏆
تمرینات شکیرا و تیمش برای اجرای مراسم در افتتاحیه امشب جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/92029" target="_blank">📅 14:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
ستاره‌های جام‌جهانی اگه زن‌بودن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/92027" target="_blank">📅 14:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92026">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🏆
🇲🇽
برگزاری تمرینی مراسم افتتاحیه جام‌جهانی در استادیوم آزتکا مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/92026" target="_blank">📅 14:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92025">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZ9eO7ztf99Xo5uUrc68ZcCUD4CaMR4mjGjcuocZbaLVLY4v-tBqpaZIp3vMAuXqc7KTX25zp5AJ_0-XMymjDt5HT8IuLUD2ZAp1dRht_3sIpgs83ftbmTVwFl6VQ5a2UAwOGXjeLjPoPxIIQFE9lBhNmibIvwAIIneBSitI0ZIfQ1vKwT9u87ozEZMItH3Xjc6o40_MJSNJWCauoAhJ0i3TQ-_Z0Z_cUOmUhhpXtWiNzy7prXyl0D-qtLggxSfiEnOwBJCNmLyPB6qtGcrIol2aBL7LoBE2PEy9Ju5h7nH1dydcavpFCdnQypOIg5j6mV7VhS9VCJTDJHJgfkSKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تابلو رسمی نتایج‌ بازی‌های جام‌جهانی که از تلویزیون نمایش داده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/92025" target="_blank">📅 13:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92024">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇺🇸
واکنش بازیکنان‌ تیم‌ملی فوتبال آمریکا به کامبک باورنکردنی نیویورک‌نیکس مقابل سن‌آنتونیو در بازی دیشب فینال لیگ NBA!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/92024" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92022">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
توضیحات‌جالب و دیدنی محمدرضا فغانی در خصوص تکنولوژی توپ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92022" target="_blank">📅 13:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n64-hMNgf-JUp6imbTsk95kyB8IqzBsuIesgi-VhdTuuFypbzgcqikvhfYV1guaK_gT8ijngO0yAKAC6ji-Sh523R-EG9i88i46Jka61tjJSfKCs-naA_9Tja216OIkIsd0NB9P0B9JomCZK-9aF-ffDrIpMNFpd1I5m6_vkTYiE7DgUosZya9dCipVwwRPZGunmWsbP3HCBNE_as3_r_w5xjGvdT7DFtqVGYzTL1FhWoqPbtubijby7iv8Q_8hBsmYh8FjqD_VgEdEth0YEO1U7bD4Fo78M5swAT-qny2V_pdotikmN6l5UdSHM3uSNUE02dd8WQu3UJuxxTi2DFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92021" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_53cufKO9TEZ71oD9CWg8b752WJqJcLAsrUKjSNh1ZczEuuBeuZjTVMJJRwtJJ4QQ4Hfr3Pc7tUZAtxZaKlPkD8DJmgOK0Cfh0TyRLhsDW0RC6v8IvVoi5q02AIKAkrPhYcL1-u93FQKwMFLrL7xDd6qNKYj0Q5WCQXNme1T-ETu8mp7pVGbhFuaJlngCMrnAawMRqMqyqNmPVf3UrFnFFGIn3tOktahhditEGO5BZU61iT1JGNB-eqF3v38J-dYew9wgwPZXWV1Mk71Etfutset06IF1-2riFk7VahfGZGJQyWukxYP9rgMA1nlatoYIAsg-v27wQU0Iio37uEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇧🇷
رافینیا:
احساس می‌کنم در این جام جهانی نسبت به ۲۰۲۲ بسیار بالغ‌تر و کمتر تحت فشار هستم و میتونم عملکرد خیلی بهتری ارائه بدم.
به نظرم وینیسیوس جونیور اون بازیکنیه که میتونه گره بازی‌ها رو باز کنه و ستاره ششم رو برای برزیل بیاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92020" target="_blank">📅 13:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92017">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3kc1znd3FvFS9EY4xLQvyYcl9Dh0_QjwZkeng_Jqn0rD_EcOxNnmu9n6Pb9IHCqs_4Y3fEynr4Qxw_WMjPH0niW03AmL-AEDeiTvVd23uceP6J0TnmnUQE4KxoMgkdi55aA6lx1T_UWJwVVI_L_UvTg0PskOpqFobPCl4w-6QVSxN6IC-Kpedrj54VrNKffeAAMZV5CbR--7tHadIoYfiB1kG--cRieyHFFI6thxmE1oDvLgiNi9H7x5fD7KHR91ztNtDkLWESsrYxdk1FLqHm0_KfcLgX-MMXFzGz26BlJLAWFQUmILi8zwa99KZbIHGhuF9GcG9p27hU-5YhzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyEylk2rM3-ZV9fk_ll4VOH8xjblwQpASfkRR8z0ks7Wr44-GNVykeZl7r-XQnhooDklKTGZvf1UJqGPx5kuIZE8LzP1UVY40u_oq8UDaLfEYDICHLs-HuKfJdgcWpQ_U0QHvfvdCkgTta0zbppFxRPm_g66_CMrSgZSp9DhjUzRlYFdJc1-axO89oPzIlbSsp1S8E-br7DI6rZDbc86L2IEpAVGYGxibXY3i807V1lBX1Hq41dk1xfm_y72jUgVo4t4FzaVwgAYNGLMwHYSuIOQwpEsda7sChh1Aum-7BGmG4UUX40ah9nuaYzlB2yqNzo4dmO7x0jWHlh26PSllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyQY1lMsG7jNA9nybKkmSyi9WqUsxYT_auPXOAk6w5nU9aSliIFQAWeE1c2BwcG0h6imfGrkM198vwABG3pY25KPi5CyQa2VfGdxorVWFFg_y6LSHw5pLBp-CjKG7FgVz4cl6dzXZnghATHzqTLfWP5qIvsww7hBhFebg7VG5Kt3lehjF9Sie6VofjlCKvKG3if7jGRtNRFzZEa3RRvPlKLlb3yA6M5N-siZDxqOJu1-OH3eqBVZzgK1sEPmS3zEuq48ziIwiTb-vr5USmpedixKlFXyEXzabEti9R0yww3S22Vah__eL5fVzBMmorOvJfopfZtpgkPqKZRG06qnKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شوخی‌شوخی با مسی هم شوخی؟
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92017" target="_blank">📅 13:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92016">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjOSvizLwPlCdWa93OobU8LQH_NgEXJL8cvcTf_sKkJBcIn9rSs7yo0oGQCE0smfyhwi4tp2E8mOjOaoL4L7iZBDyoAZuV-t7-fifbZQ0CyFO6_69Dya6ULiPa8KpT1qXKbtYA88X_Q_MWBsU9C1hJBWQTQVs0wZIRydb42pZdeQG07oozehr8GMw34MF_2EbK-JNDAOjlGXteVOkikp7DcaZ_5QN_eP1i81o3A-x8HnQZqwNJD95-lINMcy7Sdx8-aukUYB86iilicT3XiyWEG56FMfSGNrp4RJq09UOEbjKJq8P36htN2zKYRVljxwxdDkOKdc1ibTh60jaOtMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
👀
مسی یا رونالدو؟
🚨
🚨
🗣
زلاتان ابراهیموویچ:
- آیا این بحث هنوز ادامه دارد؟ در سال ۲۰۲۲، مسی در را به روی همه بست
🥶
❓
خبرنگار: یکی را انتخاب کن
🚨
🚨
زلاتان ابراهیموویچ: زلاتان
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92016" target="_blank">📅 13:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92015">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxAtSm_08DHa-fz7ubGBSelZ8oyaspXa6EVRgjUP0QMjNIAVumHroa1-TsZtzPSbbiX09lFmThjcnd9an12G7l48LrfSimZhdKMgJd4-vMNyGuh17DljtcjD-smuQKUFld1h9-78ZW4anmg3ihSBd3F3kWnDYyqD_ChRd8b3sQHAh6fUyBh4f4pv5rhqmDeBvEQtOP0D60caI2MyQ-9CeUr_K5Q_MSBxCh9Pw27Z4QQ9KlxjsLCQptJWcfCA5lWXHtBk5b0MHG781c-jVfL6JnpWhPT-PxISbZRdd7BQyJtS-wThgEPjZBNAVlLhYBaTgD-UioAu-eefiaI_Jyu0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
شانس‌های‌اصلی کسب توپ‌طلا جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92015" target="_blank">📅 13:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bogyyPYpqejOtbb9eHLH2AGLVE4Vp3-j4oZ5I_l1ybhLXa85b0ubXBBpdE4uYQQgXDM55JR19t4Nwtm_uRLVnFjqvpL0nR_ALey5r5rs7QyauLvTjhU7yYwopqPYtXqHTKNTDcY9ydjpBWDei1V5fbbG2D-AfWcDxiY55QYv8W3tAIPXjbaEFGyEqSSp5rgBcnaJxK2wngIHj1-Ut6nUX3S9WGGYLde2RJh2Llnx0_yyGnPCUPnq-A-I3pExy1rr9v6Ug8Boe3oTmlcGZA_kgHEn7lBm4R2oKM-aZVPYwAczP6oiqntn2LKk7vrqoBqeTli4El_T4Q-tjriuHhh2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcJhZhhGw94h2mUXfEoC0EUxZufm156H_hoejB26c9dMknBf0C4vRbUUnb-FF1B5D1S4ddDuAJ-YNAiYPThzgH722IO7emcCm-qROElWs-3VIm5rgK1TJ9ojVTYD9OP9KP19__wl81n5wbi21i9y8WZyJ2Dl6eEwxUfZ0jEwq-32m83jhX4HEKHPtXC_vQXRNWsbEClZAGQwvcz7UMlQn_WknT-K4avegPevKbTmLU-vxG7_Ab1IjBtZu1Me53mCcCjkxmlGjB10cVZ5MZDDHA7hrki-atYY6rqaPIDtx11mg4iVcayp6aXiNa8MGwZ3fkFxPwR0x7RIT-qC5axelA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏅
🏅
🏅
نظمی گریپشی مهاجم آلبانیایی روبین کازان به ۳ تیم استقلال پرسپولیس تراکتور پیشنهاد شد.
روبین کازان با این عملکرد نچندان خوب ۲ میلیون گفته میخوام
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92013" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsTXxOoO8EOD_NcUiNLfIBySVu6ys564-ZAXnDGkcc820m9n8m-vpQbZn-5_MwbPs2-XftbWn_Tlub7a-KbPRozvvYaJbkQ8zNxas2wKzB6BAi2PlBebq74d3AlYdWcL1SAZMvhVe6cQcyUZKqMseEbM8G82pOENO6-8klI9haHQTd1lAwchxOjRdlWKhAGaM6cxUqQK7yymSACwzgDuDClIoTu7nft1fO6wkTvr89I8FHdpY8hl_QMU-S-wsYqm-ffxhMc3leUxvqrJ7_56bb7UeM4GNzmu1JD4eVDmfqqCTH5WiliG2cGEn0XDAHPMzgSmPa8dooxzGZToixILHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه بانوان برزیل و آمریکا:))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92012" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhJQBPLXy4gXpb7mW48i3RrnwEloYdBK_-_D_oKaqGCz78eQniEPl0_8vr-3YaOYgRwfJ6mt1qGjUD92CI14sWVfIljbRElUhUV2FJsb38xg5w9plAYhWMR5Vsi0o395usNYaWY1mCesBoSlPxzWpAlP6-ai17_K8IbBlbc3ugideoRghxrbe16_uk1PaKqq0W_g5uEekkgPt_fSTXn_d8pOlBJLJqvBZqr6Y6pSDjh9T62qjhnVO8w1TePtcuvS8Em4pABxVr-7ZGH0QFnDd8CMruWB-8VCUqcIaJHr2LsyAp1vPo9DDGuW8V8loD7rKyCZOEfLcV5Ek0DPT3mnaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
🇩🇪
🔥
تصویر‌رسمی‌تیم‌ملی‌آلمان‌برای‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92011" target="_blank">📅 12:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
تاجرنیا مدیرعامل استقلال: پول یاسر‌آسانی فراهم شده و تا اوایل هفته بهش میدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92010" target="_blank">📅 12:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین ویدیو نسبت به تیم‌فوتبال ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92009" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92008" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92007" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAJfbQHjkm_QZxGVdgeRA_JNugjCqDCfntpVekY890xxWBOLP_oqaQKoFfS24UajWRCTYdtxsACfNRKn4Q4IvN7LiAkUzGbL8Cc_9M3E7dODkUZIwXKgoQ-9R8Fzw-c4RYomsc3_df5p56mVTcOjbQYxca1kLJ5FGpJ0tiTEA9SyYoRlWmGrdNmJYxRMfM-TdL47E7qQUoAG25dU5kNK7Gzv78HVNQxmJWHuBc2I1fFnLLGSiOOXwUYSwDVuLNMDo1s3uVQgS6ut1O9aaDCUN1Rp_Jt1LanW4mT65Ih3blsjw3_7GxzdRgZibnvm3dVxyRrOpZP4GsWTiHizAV7X9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇨🇴
خامس‌رودریگز
: چرا شما رسانه‌ها فکر می‌کنید کلمبیا شانس قهرمانی نداره؟ اتفاقا تیم ما ستاره‌های زیادی داره و باید مارو جدی بگیرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92006" target="_blank">📅 12:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b35afcdb3.mp4?token=eLUp-8BlvFk23XU3Kt5D5kWjx7lau3WG4Wy_qKS2Lp5Wty3BjeIJCCUIz_nCp0zMj8xZzP8Ca4GgfHig2LaC9f_sjIlt97AVR2RKiGtUwbAUYUVPP98dScn1re72REH5IHQBAkMbbntz9Zf8ehBU2gUVlwxy1lPXgfuNHOyQljFVSOLTDCP8gX_G4VJxR9RDj6_y4D-KUuTMvVikf5PCdHNesKFZXl5FNQwhsdaAwtKfMcihqwFIH_dFA5EIBTGF31AGiEOkMoJ_jE0xlsKyBja3KpgIlyofhS6FP9DdJFHF_5Na4Y71T9-UhtROP4TYd8A1ye78Id97XqwU-UAgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b35afcdb3.mp4?token=eLUp-8BlvFk23XU3Kt5D5kWjx7lau3WG4Wy_qKS2Lp5Wty3BjeIJCCUIz_nCp0zMj8xZzP8Ca4GgfHig2LaC9f_sjIlt97AVR2RKiGtUwbAUYUVPP98dScn1re72REH5IHQBAkMbbntz9Zf8ehBU2gUVlwxy1lPXgfuNHOyQljFVSOLTDCP8gX_G4VJxR9RDj6_y4D-KUuTMvVikf5PCdHNesKFZXl5FNQwhsdaAwtKfMcihqwFIH_dFA5EIBTGF31AGiEOkMoJ_jE0xlsKyBja3KpgIlyofhS6FP9DdJFHF_5Na4Y71T9-UhtROP4TYd8A1ye78Id97XqwU-UAgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
رایان‌سرلک بازیگر نوجوانان سینما: طرفدار پرسپولیس هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92005" target="_blank">📅 12:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EhofAJB56hQ7QjbQCn1c7xuoqwfj7-mpa4QsOvynXEBYdtqjusZHalO8ZqrmYFCAmdJ9jN0N3YuW2PMpt_ze6C6IMp-VqecRWkTR1nmy5c_BYV0PdfYEmYIe7CWz1xMmkKnmFS8etzvuMMwo-Lhy9EtxYcgoh5Y9dU7kbzhQ26A_lExqK8zAQI7BzE4PLePV0TjwsWsT7gLIs22b8kHEXmhAC0Mef9Ydq13QivcK1RYK_Jtial8MOueFRcCUycCSOM2OTN-jStWmYTHCgy9jU5gMRvO3nXNCGHKmfmZWt_GX6TH8dMuo7jyr5QSMLrCYD_dH-YwIieyOUulaDtAzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇽
تصویری از استادیوم آزتکا درحال تدارک مراسم افتتاحیه جام‌جهانی که به وقت ایران از ساعت ۹ شب آغاز میشه و یه برنامه ۹۰ دقیقه‌ای قراره برگزار بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92003" target="_blank">📅 12:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijQ_UuD8b1FKz4vJIwElsMGC5JT0viGXCrKM7qfNq5qY5Jw2k6zt46NRhQIeaJBjwntOfU5pRF-C-9JlTFbIHpm8z6XiGJB4Mdr2KIsisGdocUQtwezBBR_TInSOP3FIEpM_q9dEm9AqFCe5H2T2a95rgV_nPJFmNjiedbrNEPEIGBEKAU6Jds9568LB4c5yKKj9ZsbyJKuEjcMRptiuhz5dLeBDzaPpxxDkScsGe9oLzAG89Sa1_ADKrhfd5pV4cylKLZxS1biaWz5UxidGU3cxt7aZ1kpCJuH7IdKS5_E74NU8DEalr-lj_cHgIP4N2bm8dBQb4Mtt5Q36ucezNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇮🇷
🇪🇬
فیفا به‌صورت رسمی از مهمان افتخاری دیدار ایران و مصر که بازی نمادین حمایت از همجنسگرایان است، رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92002" target="_blank">📅 12:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LQPJy-RqIzR7M1nh0SkB2GzRVlU7AQtCWR_HwlkY2UEY1XTJ7ZcpQXrXx15YhoQOUv6y-Dhq-Cmi3OY5AisVC5w70GgltwWEQkalZiZz9Jtc_LVTfz-p564OZrD-NOg15NpyVMrE6tXmaGJTLCIlWgtsA-k8py7BApHkyn3J2Qi81kh48PD-4hnFaN7v_F1rIYZh_SF1EzOFCVOkicAnrPC_yNtqAj-j8jahw-kOjSTXtkux_ljJ5t3xZEXZRnj0K2IzcEKO0YZQ6NCAAzZT9anELaQm2dfaEomz2LeMNRSOcNYCkPqsYziUOK12ZL0fuIt1RRIpHpQHXh3c24JztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
رونمایی‌فیفا از کفش‌طلا، توپ‌طلا و دستکش طلایی برترین‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/92001" target="_blank">📅 11:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab1767abe.mp4?token=i2wWbDT9KYRx-9hnpzr8q9TVaXzsrSl5XP2XvzxL04x2zFnw16YapZy6t-lLUmWrF9AR1f2msk80LtmSiA8MkUVOChgiqW2qppoVFlNjBCdjl9N4V60EXylu5EXHWHa-WoknVCi6EMRhwhxo8f-pwqMemIA5nmSK69XK5fZSIqT6rNs1hhO2w2zFlaxRvtfHBUIlOPAOSoN6kc11EDh0vk_U8OJ1mSdxv5NpmPvPkwa4RRguthIML19Cu0rXIW94MGnhj71GacAOl85FGL4p9vpMeCQtOP7W11SQWskU2aH0SRmCnp8rtkLt8em5qtMFrqZJfs9pY5q67xXB49_zqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab1767abe.mp4?token=i2wWbDT9KYRx-9hnpzr8q9TVaXzsrSl5XP2XvzxL04x2zFnw16YapZy6t-lLUmWrF9AR1f2msk80LtmSiA8MkUVOChgiqW2qppoVFlNjBCdjl9N4V60EXylu5EXHWHa-WoknVCi6EMRhwhxo8f-pwqMemIA5nmSK69XK5fZSIqT6rNs1hhO2w2zFlaxRvtfHBUIlOPAOSoN6kc11EDh0vk_U8OJ1mSdxv5NpmPvPkwa4RRguthIML19Cu0rXIW94MGnhj71GacAOl85FGL4p9vpMeCQtOP7W11SQWskU2aH0SRmCnp8rtkLt8em5qtMFrqZJfs9pY5q67xXB49_zqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هندی‌های دیوانه‌مسی دیروز اومدن قبل آغاز جام‌جهانی یه ماکت غول‌پیکر از لئو رو تو یکی از شهراشون نصب کردن
🐸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92000" target="_blank">📅 11:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac930c836f.mp4?token=qooP_bHkDsHYNdsOhToruanjKAS8-VBmfpdS19Z_ZTkWI_LGSDkAluErgzb_UNBIlzKxYNgKifZg85ehE8K6WaAPckW-Ngogw7_KNrAIy2VLkrrEGZU1l9yv_Ilbtwit2nSGGw2HbBgWrWWLeW4oewnkaenjf29PHjCZ9dSPn-l5aa8M3bXGhNYLdb6f5ljZ8riTV_pxZFn4shWTxWA0LkLjMs5N41FyooUkL1H9RgHxng91tF4CDAlzA2DouLoG2xyorjyhCFoUn-Xfot5ma-qwzSHB9F5Rn5x3U8YeNkCscDJmxzERl8eU3DtzpD3lkCSJgwQGdcVntmaDSOSLtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac930c836f.mp4?token=qooP_bHkDsHYNdsOhToruanjKAS8-VBmfpdS19Z_ZTkWI_LGSDkAluErgzb_UNBIlzKxYNgKifZg85ehE8K6WaAPckW-Ngogw7_KNrAIy2VLkrrEGZU1l9yv_Ilbtwit2nSGGw2HbBgWrWWLeW4oewnkaenjf29PHjCZ9dSPn-l5aa8M3bXGhNYLdb6f5ljZ8riTV_pxZFn4shWTxWA0LkLjMs5N41FyooUkL1H9RgHxng91tF4CDAlzA2DouLoG2xyorjyhCFoUn-Xfot5ma-qwzSHB9F5Rn5x3U8YeNkCscDJmxzERl8eU3DtzpD3lkCSJgwQGdcVntmaDSOSLtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظارها به پایان رسید...
امروز افتتاحیه جام جهانی
🔥
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91999" target="_blank">📅 11:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJCZDnKppJTWeTBZJqttPdo8JeJGrT250u9izovetQNnEEQG1RAYYmC_g5PAh8NuEEEGHwx0I6sCEXjWlWDBowKII2fh8vVJNAXd8hsXc5B7lXvIboTo8k-7h1gQH327rpQNuSv2Ap5TYEqgxMw77NxvLzQS6bYVpYUxGIzyZnNo1WEFW5ochARtPXSY2AkNAQdb9a9u5t4d94NMNG9BDcY-soeqJNgPfN4F9jTeiw2W2dz0VhM0mTnqc4MpO53ij8LF1Jo9pwTq3BAM3R9by-8K-Wu5iRkP3f1QtLzOZqYH1aYszGtmkWoNyPaw7Xj1iulI1cdtOopq6oo8uyq-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال روز؛ آیا لامین‌یامال اسکینی پسنده؟
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91997" target="_blank">📅 11:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f7abba26.mp4?token=oeIOyPEdl-_hlhSpzOtJZ28bfU3cREeKIVNmQQ61GeQpqnlIag6Cv79882WvVApSb9QazvG73K-dIkz0Ke9JH9mMeE_SYtpDmdRJu1trJnkK0dFisOj18Nq6akjvTwnXQXHTbOJVtPsrXqXAdihajcDaKENAIUtzv-JlM6GA3nzUjg4VxiB9C5ajNp6jsLoZ0NSccvdyolEl_d-JxTFbOERuRTEYIn3Oi2jia1jVsc9iysXiLSNNqxDfwCv7dOTgaVGCCONuubO3wmAXaPMl5B1FuztgKWbHySQ3h7d1-4KdHYiRlR1DjGW2qnGc36a0o1-mGXE-SNpklaQWPp0irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f7abba26.mp4?token=oeIOyPEdl-_hlhSpzOtJZ28bfU3cREeKIVNmQQ61GeQpqnlIag6Cv79882WvVApSb9QazvG73K-dIkz0Ke9JH9mMeE_SYtpDmdRJu1trJnkK0dFisOj18Nq6akjvTwnXQXHTbOJVtPsrXqXAdihajcDaKENAIUtzv-JlM6GA3nzUjg4VxiB9C5ajNp6jsLoZ0NSccvdyolEl_d-JxTFbOERuRTEYIn3Oi2jia1jVsc9iysXiLSNNqxDfwCv7dOTgaVGCCONuubO3wmAXaPMl5B1FuztgKWbHySQ3h7d1-4KdHYiRlR1DjGW2qnGc36a0o1-mGXE-SNpklaQWPp0irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
تمجید ناصر الخلیفی از تعهد بینظیر انریکه به کارش در تیم‌فوتبال پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91996" target="_blank">📅 11:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6334d3e2c1.mp4?token=F8HVP5-3Ud8zdVa2sWhyodY8AtA7n8946nk4BjNc18ex0igb6MXff8nc5gJqSGs1P32KsA3LyuVPJ43AqEMNBGZexuuAkPruqqFNiscH7-LXvh1eKFi73Ny4bNf6MYznqnfkNabCtWs7ZB8VEflzZjPOdn1VR7rqBzkA5s4H9Vn_rSnOGB89JMSersXVYOp-QW-XSKnbWUXntFFHMb3JEdoOdPhpw6le7P1B5OIBk3TfKPcNaqnKYI_80W0ITY_AjxEvWZk1-2L6Q3ZzapfLr8u4Mxrh9ZNhwP3bhcK1kQBaE3YSp34PF3urwsd3XSsRvsUO35X7CnSTcbDGsiJbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینی رونالدو اما با کیت اشتباهی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91995" target="_blank">📅 10:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=oEj6HK_afSbUr2eMymxzjynKwxl6pQSFfwIX8W56Kn7lD3qKimX_Hy6lBYOdrsUGIGrWNuKTxVP9cLXoLXYX5C17syK2t_oIP1XaTl7Duvorr3wvAlabAM8bdocte5YqAP9Nnupv_hUevNop7qchY0c2cfgvQNATuwy75DvsefIx8Xgep2Ywu8uduYdqX_1iXywh6sNJkomvvPDIZ3rs487dXAYcIrG3oMjl3uzCcos-OwEeTJS47PonP6hUSaGR2ITYHc7j4nE9AfLSGEpW3_Ifw-u7X9rKvxJf34Zzifn1SVujNkQ5T2UpJfxlZCNAm47mgrH5iiBSjs7Vn74J_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ff92078c.mp4?token=oEj6HK_afSbUr2eMymxzjynKwxl6pQSFfwIX8W56Kn7lD3qKimX_Hy6lBYOdrsUGIGrWNuKTxVP9cLXoLXYX5C17syK2t_oIP1XaTl7Duvorr3wvAlabAM8bdocte5YqAP9Nnupv_hUevNop7qchY0c2cfgvQNATuwy75DvsefIx8Xgep2Ywu8uduYdqX_1iXywh6sNJkomvvPDIZ3rs487dXAYcIrG3oMjl3uzCcos-OwEeTJS47PonP6hUSaGR2ITYHc7j4nE9AfLSGEpW3_Ifw-u7X9rKvxJf34Zzifn1SVujNkQ5T2UpJfxlZCNAm47mgrH5iiBSjs7Vn74J_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رفیقم یه دست شانسی منو تو (Fifa/Pes) میبره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91994" target="_blank">📅 10:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=oWChsRkg4Fo5yny8JKE6T2hnhxpCVmn_rIjD7bsTft5oxQdiCwv3zTOh5iPoV1VHqRO8TcCP_8os4FuuIy8aVy0Yd3QgNXSryp0sNG_JNzoLb7JJEugfq8Cz_zcUB_dE_JxNBBqmvGAdIF6Od8Uq7y_zT8dhPD2fM6id8L9rtJ0A4zTySgu3vlUFQT_vEmN79sEDBj2azOh1PqcLvfXhT_QQMbQey7TvC3q27tz8XBSCFRi9Q2xpg1tc1ZD5Fd9jZitiBRkyYbRn-ILAs2rywmJmhYVIWv2U9z0bNNUzw65UVo7GuiSiGmpG-M-C9Y49O474MLsFyk90IQfxDnanWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92bd9318a2.mp4?token=oWChsRkg4Fo5yny8JKE6T2hnhxpCVmn_rIjD7bsTft5oxQdiCwv3zTOh5iPoV1VHqRO8TcCP_8os4FuuIy8aVy0Yd3QgNXSryp0sNG_JNzoLb7JJEugfq8Cz_zcUB_dE_JxNBBqmvGAdIF6Od8Uq7y_zT8dhPD2fM6id8L9rtJ0A4zTySgu3vlUFQT_vEmN79sEDBj2azOh1PqcLvfXhT_QQMbQey7TvC3q27tz8XBSCFRi9Q2xpg1tc1ZD5Fd9jZitiBRkyYbRn-ILAs2rywmJmhYVIWv2U9z0bNNUzw65UVo7GuiSiGmpG-M-C9Y49O474MLsFyk90IQfxDnanWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از مقایسه نحوه استقبال دو کشور آمریکا و مکزیک از تیم‌های حاضر در جام جهانی حسابی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91993" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_7QeTJatvN6EnShyZwBWasiN-a6vTV7A61Z0LNz8maoPWs268aa9zgW7f8fgT4F4YJEvI8j7kY8qKfFdSVKvsUTeDf6dn8rNvYkvKSCXtbFOx24nuBQI7XCBKI05fey8YrKaH3kiEh-l0V6WJZJ-Q3E83jetoF31gd21FyHop9J67DhHLzFiQUZZkQuwzeiudxNyDbwPyqAXtFBYv0pi2CZGXt3qGgO90DI2X0qxOn7AfmCtezmUBk6C3JKKFfZMQH-6_2aG5A5bn5o07c8piVHo2aUxkq81rtxW3H6RTl3chigCcJg6wtjMRfgKILt_ebs5txi3V4P0kdpKHjujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
امیلیانو مارتینز درباره افسانه مسی:
"اگر الان بازنشسته شوم، وظیفه‌ام را انجام داده‌ام چون به بهترین بازیکن تاریخ، لیونل مسی، کمک کردم تا فوتبال را به پایان برساند".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91992" target="_blank">📅 10:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=cLyVGvJ3n-hwLZ1Kb16CVsS4VI4kOtf5MUBVGPhH5We_wlHbkiwbulbAB0uB-YiEvWQwUD3M9mfg95QI7CbxkC6Gs8rvQk8JTiMSF9QOf-AGDDLdH_v_22oq9oE3640yWZUMnS79v-i5fi_zshFa_npLPbGh4gbQNQSxfNtnp5FkvMpaiJspEFp-ypZTObxa0gS4rRzoOjDX3QqE9EKssbNrZMj54EpXM1mgPxisIk4WGTUg5RYvv23HYp30N7zKa4879qPnDpUxuKx_r4CYqsJ4clb8Kz7s4CEZ3IGKUZRKbl1r0CEwh4ru_gRh1XSwLfSwvvgybCCQFhNWfgoddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbe9d6437.mp4?token=cLyVGvJ3n-hwLZ1Kb16CVsS4VI4kOtf5MUBVGPhH5We_wlHbkiwbulbAB0uB-YiEvWQwUD3M9mfg95QI7CbxkC6Gs8rvQk8JTiMSF9QOf-AGDDLdH_v_22oq9oE3640yWZUMnS79v-i5fi_zshFa_npLPbGh4gbQNQSxfNtnp5FkvMpaiJspEFp-ypZTObxa0gS4rRzoOjDX3QqE9EKssbNrZMj54EpXM1mgPxisIk4WGTUg5RYvv23HYp30N7zKa4879qPnDpUxuKx_r4CYqsJ4clb8Kz7s4CEZ3IGKUZRKbl1r0CEwh4ru_gRh1XSwLfSwvvgybCCQFhNWfgoddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهار فرصت‌سوزی باورنکردنی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91991" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860ae90c75.mp4?token=VFFfMmYFGjktztKf-mBpIiXtmwPpDNF3bYFXGixKucZMQ4rwEk6qUl32rkpxH3McnEOa7kVtx4PlfS3Af9st6GH3tZDO3dIprEbOBullNaPbDNFsdgkwpvQ5eC0avV6XmvNj8P2m8eBIym6VJe-JITDhODZwwg1FqLFO8DuQ0uWKkoLGI7E50i4pgRkKKfUx0P-a5y7w6uxFuDbHC8bDY4bNovmXeXVtVuwei4tbvmBRQ-hdzxHGsTVsOyXuy9gm-RW88t4UV-V7QtyzYkIZleWhXsScixSznLX8FOufr-5B76_D_yhaWz-_8ALtATcLVkpMCSNc3g0Kk9oF8QO8rYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Cherki Core
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91990" target="_blank">📅 09:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=h-pXp_m9DbJ7g8Etlp5WIOjOQwk9SA-cO-swdb1RqcV_YRWVnRgLQtc-ED8ApP63cukSB4RzZ2NUmhv3VN2Q7LVyOc5vCB7MEUrPmnhHlcDtEqt33EUhpErFnYC5mIQCk_LNkKeC4utBMNszjivXxP1NYhC41JzJrr3JKDu7tXCz8nEXb9W58J3sI8Uh0uJWOZaHC0YAvGIuE8ihZBpqik7U_8ckAIvWsb0g7T6AeA9W_mdBaWpq9b2nEYK3XsIvwTg48rNZcogpAj7BlsuMSwMXyDNhp20UuT1LhN_Mehd6RqnkfXsJlz0klL-x6ToQti4xnRDaOddkVLRvQy1yIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dbc39d9f.mp4?token=h-pXp_m9DbJ7g8Etlp5WIOjOQwk9SA-cO-swdb1RqcV_YRWVnRgLQtc-ED8ApP63cukSB4RzZ2NUmhv3VN2Q7LVyOc5vCB7MEUrPmnhHlcDtEqt33EUhpErFnYC5mIQCk_LNkKeC4utBMNszjivXxP1NYhC41JzJrr3JKDu7tXCz8nEXb9W58J3sI8Uh0uJWOZaHC0YAvGIuE8ihZBpqik7U_8ckAIvWsb0g7T6AeA9W_mdBaWpq9b2nEYK3XsIvwTg48rNZcogpAj7BlsuMSwMXyDNhp20UuT1LhN_Mehd6RqnkfXsJlz0klL-x6ToQti4xnRDaOddkVLRvQy1yIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
خبرنگار: چه پیغامی برای مردم آرژانتین داری؟
لیونل مسی: «هیچی، راستش فکر می‌کنم مثل همیشه، هر وقت که یه تورنمنت رسمی شروع میشه، مخصوصاً وقتی پای جام جهانی وسط باشه، آدم خیلی هیجان‌زده و امیدوار میشه. قبلاً هم گفتم، این تیم هیچ‌وقت کم نمیذاره و پا پس نمیکشه. طول این سال هم نشون دادیم که فرقی نمیکنه جلو چه تیمی بازی کنیم یا تو چه رقابتی باشیم، تا آخرش میجنگیم.
این تیم هنوزم با همون انگیزه و امید قبلی داره جلو میره و همه دلشون می‌خواد تو زمین رقابت کنن و برنده باشن. ما یه تیم برنده داریم که همیشه بیشتر از اینا رو می‌خواد. خلاصه که مثل همیشه بازی به بازی جلو میریم، ولی با کلی انگیزه، امید و این باور که می‌تونیم موفق بشیم.»
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91989" target="_blank">📅 09:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9iA8cAWEgJdwWOdN_RHddN-Vn_c9k2wK9CbKc_THI1DxM3SuKhAKxWVN-j3QMBZhgXiYpZSge3LQKiggd-SXQ8_mjInAzd6GaQeXpDviQ01GioX3qvGZrTZ9SAGkA_cZkp9DX7px5ZM4IsnJXZy6ElqRS46ouWlJQrG4oa-0hd0v76-JFBJncXZF4wo2zbfvpIt8Ut4fynOOoKsrq1hKZFFXMlGSaRcYtZ1gjaL0jnmiWwElOXOITIalmSmBkpNC_jUMieET_N-EIfmVRkBJ-ZqbE0dknoteIXP2P2CF9hxe8hSDfWi_DACs5jibV7xhhr7JJN3wR8-5i_3tCEGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل جام‌جهانی در مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91988" target="_blank">📅 09:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvMW_ivgZffQZ9g61QU26JDhVH8UeNVESc4mtej1GF9y5EazakY2eHHffuRreRClFzTqj_hnkjc3gvuaf9o18er829dpj9kikggwvcMT-m9I4hfLMlv4fEC7gJk0fdq1yA1AH8_DJ6hsSZ_NzvrOobdhvjVb6LhqQlsmu_wku9VPA3eQYQKQQ_91kttYAts0IyIqEClltDPYsfv6het9GxIUyxAJqx9xvzcfJPJF_6WRSnhf1ooCG6j9saWik12QwPchTg4pQVFUePlisDEzA6omNTm2jWvyXAsrzSuQ7fNQxWywdgNMJVpEb6oQ_RF2de9EhW3gztr4vUJUVjWOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4g7FYHQE9zexSMxlBVhLjYkPbJ4LYOLz8j2-9DtGgDIUTBd9TSKx7FTk7W6KbH4emzkbcQVbDkcgcNVmKmzsNxQqQGEqRN1s308Pb-bxe7CNJPyMHDnL26r7ezjCe5d920SvhHsVllXEudndJFPunkDXESS-5fRw60VtYsHTO_IgcjiZxpr7SLtgm-pqkGI7PIVxuMSIMo_ewAylNrvVfsamYa-SrnWAEwa0PmEmHgm97SoWr_PFFmwlWwjm1qFsi9FvSdAkHEC3Jwe623VEDzhxkkht8mTdXDlZ6sENybFlMdoHbxqG6NHHtkH4lwBQ3tjFsxybZHrpHHnFA6rRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛ آغاز حملات موشکی سپاه پاسداران از شهر های مختلف ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/91985" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=KCSCYvEmV6359lZ_NbCzKdgQVX_ICVYeG0kZu2zyPrvTJkWvjlIftgnau1CG-CszWPimtdWVN81pn_jt8gU7VMNouZY2Hu_i_ZER4QfHkh_XoRx3LWfIZhvjbCB748jbFCdZPUq0DCNKJf07gujpGRPvBsE0QmMO4rMvDkWm09J2qSAbBd6OMLR3zmo9TC5sOG5IdErZrswbAywQ0kDtNYiZ4Qyr-OgrME7UQaFqRMbDmrAQtRdtWHldSIxV7pSRE5yepofe3pxhayoxurmT5oTJvndMN7kl_dZYeaNN52NZaSwUshiNzsniErBONkKpbODQmdJNefKiCfu-u-X5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a7d93b38.mp4?token=KCSCYvEmV6359lZ_NbCzKdgQVX_ICVYeG0kZu2zyPrvTJkWvjlIftgnau1CG-CszWPimtdWVN81pn_jt8gU7VMNouZY2Hu_i_ZER4QfHkh_XoRx3LWfIZhvjbCB748jbFCdZPUq0DCNKJf07gujpGRPvBsE0QmMO4rMvDkWm09J2qSAbBd6OMLR3zmo9TC5sOG5IdErZrswbAywQ0kDtNYiZ4Qyr-OgrME7UQaFqRMbDmrAQtRdtWHldSIxV7pSRE5yepofe3pxhayoxurmT5oTJvndMN7kl_dZYeaNN52NZaSwUshiNzsniErBONkKpbODQmdJNefKiCfu-u-X5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سنتکام: به دستور رئیس‌جمهور ترامپ، دور جدید حملاتمون به چند هدف تو ایران انجام شد و درحال حاضر عملیاتمون به اتمام رسید ولی همچنان در حالت آماده باش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/91984" target="_blank">📅 04:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏐
🔻
پایان ست سوم دیدار ایران و برزیل:
🇮🇷
ایران : 15
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91983" target="_blank">📅 04:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
🇺🇸
فوووری از سنتکام :
عملیات های امشب تمومه و کارمون رو انجام دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91982" target="_blank">📅 04:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:   تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91981" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMhGE7eGorI-nblzOPZt5PbldAPGI4euxOBUY0I0jNCdX6HfAYz0PWD6mFqFPSK8a7xjKalwqQqlez4b354Kujn-Xd8y4VZdIMItdaOiabsRZLxLZA0GCXYBex9yjmHvOCdVpmsylwZp6tk7BWetJ80n6jn3csClPZlbOXR32A2Bar6mxqQtXTIiefXkuUEh3PneIm864gKpES-ctjbjuqvDT8FPwp6HzrOYe4VHbEKE7Z3TUhHZRf5wbJu0EcvlXg9mTi-8qOOEJxcUYR62Pmj8WLDX43ZJc5xmTrtOdvI9rdEJCoGy-WJCI5pZ1krEjZelIQi7NufAkK1jrM4RlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سید مجید موسوی فرمانده هوافضا سپاه:
تنگه مقدس هرمز رو ناامن می‌کنید؟! منطقه رو براتون جهنم می‌کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91979" target="_blank">📅 04:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993f547a79.mp4?token=lRKu7XXFlAHyOa25fWNGs35y-xoXElxgT8dXQ8lYQKJ9BVu89pVU5aRvSgDttF_9k3jEfdZl8NGDOda6D4CKi4a2EalYtiw54MbA3hb3M8Il1zdqTOBVQIUrPcL6J6qvJ3v2OJgfzsH4r5iV32uZP4B829Gi93awpKf8WSMn1Wx7LaPS-Q-n3Khem50e0ShOVo1QKn8C-kn-FOR4X-VW-kvJjdtg2HUAedhK5LhNKXDEWFk3diBDbyshxkKEzgFZKkFYmISaTg7D3MjbR2NqnRY2MBugmZiD_ZpLO4-YFGWgINMcv0-qfp2mg5AKdd6r72h1Yo2O59m18huX6ILHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993f547a79.mp4?token=lRKu7XXFlAHyOa25fWNGs35y-xoXElxgT8dXQ8lYQKJ9BVu89pVU5aRvSgDttF_9k3jEfdZl8NGDOda6D4CKi4a2EalYtiw54MbA3hb3M8Il1zdqTOBVQIUrPcL6J6qvJ3v2OJgfzsH4r5iV32uZP4B829Gi93awpKf8WSMn1Wx7LaPS-Q-n3Khem50e0ShOVo1QKn8C-kn-FOR4X-VW-kvJjdtg2HUAedhK5LhNKXDEWFk3diBDbyshxkKEzgFZKkFYmISaTg7D3MjbR2NqnRY2MBugmZiD_ZpLO4-YFGWgINMcv0-qfp2mg5AKdd6r72h1Yo2O59m18huX6ILHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در کرج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91978" target="_blank">📅 04:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-U4b99g72W2MZGcoumtxMJwlslHA-_wDgR9ySbwRXJVJgJLHI8YWJE1vTVjRZHyMNBk__ELQOLTbDAHog8dnJN8FHlHHfNEJKf_SYR3cm8hBgI2qpRU3Bj0TGLjc8Vx8Z-xOulIOGwIwADhlYIu2tNgWJvSpSlrksk8lsiGR0aRb32_KdLPHsXsOq0yep7zEC8Lx_rqpqgtZWiJ-mvFwtsry64cPTlAF-lfg5hxo92v_6ois6ZVNtqU4py2pnDutIXaYSMtbR99BNNJ7QgUyHKvjABWKV0CD-LjvjR9rUVumeAM5dWq2XYpQw7QCFbftAJ_Xrqeg2IdUH5zfCshjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czAe_Dd6jfOu_NYdvZ4rgmW1Qq6AC9NDCRXZE0GcCgFZtRFnBMsQSmwrjFXk220Q3BcR1pHXMKmesWWiymS_tqbQuwJnt5hDx1PaYbAw_ikqTHAXATJxvsmUC7WKO6QYyo_RmkSFWqFhB_7SGH8NtS3ywZ4JXTULGJSkAvuYJEuN5Tn6hOTdG-nHOS7ifgKcaWEkTN6eD0JR1zGDVsbtOhJ6gfJ6QoQAQAnQ-wsb2Mv5ysj6lS93zpTmU9Dflv6D7U3lVSHRqlkRpMZCdfwf_iMcg84CjXlluiDeSwXxpsorha7Ph3mMeslKlDTo3zqJpVoUEQSCEPH2eu1AkSkfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqacLj-e5oEdwlIiRb7UEZ7-kPmXmkKmmZTLrcVvoJsaPzvOhwgcLI3TxB36BSmseIc92FkHU1zScNbmn3I35qwvnI8cF8oksplxbJFnTJTa9RKP7YW0jjNvCS4lvMs94wRXcz3ER1qh4nm_Pjo3s-QMbfFCH0A-7JYaq2SB9Fo-oV2hEqJdDx8FPhnCZXjp4_r7O1JNwxFDSs6aaVfg2tVpZ2E529EytPDzVqEshBDP2QEj2hg173Jthme6GrKofycfUqEONuFwg-Rwa8-9qZzhj0Xghl-MFGue5G6n9n9K_Hwwk4PpioslguO0-_2m2uyqaBZJMnkXCTm-DLT2tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش مناطقی از کرج هدف حمله قرار گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91975" target="_blank">📅 04:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏐
🔻
پایان ست دوم دیدار ایران و برزیل:
🇮🇷
ایران : 25
🇧🇷
برزیل : 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91974" target="_blank">📅 04:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران : 21
🇧🇷
برزیل : 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91973" target="_blank">📅 03:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=ZnOlncIcwVrd4eXJ1j0qwd4GzeG6Svz5wmpfWnIUpLdurK-Df5FPY_YmdEIMb-D5KvfObgOPixkzcO7erbkIQlZ5_y9_iP-XPKEqrw15-H-NZDCri84Fy9PLHO306RNcs4xa7SZFC7kh_jHXbX5O1jM8UECEvTr2V0ALqX18fN_VSaAM0UOe4Q60jaHtjV5Rzyi1fel4cV3PEMURtukG15_u5ZGVgp5yexjtc90g_QFXYrEBZf_ZG13EdJJSygWmtgGRydRGmXNGw19LfZ5EbXbFOIDmT1g_DXGjHo4aofV9QrL9RVU5mk5YxHJWa46AP3WVaTt-7MuhtuEHlnXoBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd5213336.mp4?token=ZnOlncIcwVrd4eXJ1j0qwd4GzeG6Svz5wmpfWnIUpLdurK-Df5FPY_YmdEIMb-D5KvfObgOPixkzcO7erbkIQlZ5_y9_iP-XPKEqrw15-H-NZDCri84Fy9PLHO306RNcs4xa7SZFC7kh_jHXbX5O1jM8UECEvTr2V0ALqX18fN_VSaAM0UOe4Q60jaHtjV5Rzyi1fel4cV3PEMURtukG15_u5ZGVgp5yexjtc90g_QFXYrEBZf_ZG13EdJJSygWmtgGRydRGmXNGw19LfZ5EbXbFOIDmT1g_DXGjHo4aofV9QrL9RVU5mk5YxHJWa46AP3WVaTt-7MuhtuEHlnXoBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😊
کارشناس فاکس نیوز:
اگر ایرانی‌ها توافقی را که مذاکره‌کنندگان آمریکایی ارائه کرده‌اند امضا نکنند، چه اتفاقی خواهد افتاد؟
🇺🇸
ترامپ:
فردا شب حسابی بمبارانشان خواهیم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91972" target="_blank">📅 03:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91971">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏐
🔻
پایان ست اول دیدار ایران و برزیل:
🇮🇷
ایران
:
21
🇧🇷
برزیل
:
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91971" target="_blank">📅 03:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
بمباران بزودی متوقف خواهد شد و مستقیما با مسئولین ایرانی صحبت کردم.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91970" target="_blank">📅 02:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⭕️
🇵🇰
پاکستان:
میانجی‌گری ما میان جمهوری اسلامی و آمریکا به‌پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91969" target="_blank">📅 02:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری؛ قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/91968" target="_blank">📅 02:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZLcNlDtCBqJBcDU_vNI4ZfkScvkUcA2bd0ITz6mXVO2hjozdCOLIpE32-eR-YnYd0XRxogYPxs6E1T705hEwTt-ku-Xi6KNIRqAgAA5vzc-QpjKrhGW7rlzhgK2Sp0_XPqnpT5cAF4vj2VFwtoWGdX7FyvLAklNAO2o62DYbS3Nd2QVTEZJwerdcEws9NXMb-EENV7NgWgKwHtGonn_R0bgwolfGQaI--9Abj8iULJ6SsvpbRPfRM1XEodDtycdNg4fwXysYKhEP8KbF8EXyl9QDcXayOajtbP_R3BAZfaSOCRgL3ShknBOf1cspl_vEJwQxY67yoUgEnaFi8jkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
صداوسیما: تنگه هرمز مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91967" target="_blank">📅 02:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
#فووووووری
؛
قرارگاه مرکزی خاتم‌الانبیا سپاه:
🔸
از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
🔸
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
🔸
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91966" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laLd8zwCAbUZCv9FVU9FNqUhBznCGs1Oj4i15NE95HT68j1EvVBr17LwagubcUA2pkZMBn_MMbJEQD5i-naj5W-t99jKVvlQ9SwIO0YtbJsKehstC07YY-diCf6sdd62RrON5oKZ34ka9sGKF0QMVOxsLRTEECNRvuYdu0_zsklI6EhCPtjYj10TU2nIgjVj8tVVxb1cRCbI92iLEPd4YUj_mZtBRKNRY4otYzdcDktP-do6M5l5TapzdDB99s8eY6WMYewaNOeIZ6gLjLHUoUvBh5OkQsUqziLFPLWZ4sByF3a2wQDioITeEP0nXZxlOsGyFutUSzVCH8gs5DunBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورررررررری
؛
پرواز دو سوخترسان آمریکایی در نزدیکی مرز های آبی و خاکی کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91965" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انگلیس یکی زد به کاستاریکا   عشقم گوردون پاسگل داد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91964" target="_blank">📅 02:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91963">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
روابط عمومی سپاه به خبرگزاری صداوسیما:درپی تجاوز جنگنده F۱۶ به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91963" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری؛ فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91962" target="_blank">📅 02:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91961">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووری
؛
فاکس‌نیوز رسانه نزدیک به ترامپ: هدف بعدی ارتش ایالات متحده نیروگاه‌ها است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91961" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezUdENBxe4va3zrFu6kRf2CzecpUY3G8zbLJ6dn9QpIe0bV-PWrjN1b7D_NnmlIg5SajzPgBYZaVGmbEM66PZUr2pR_XUo0FDupaJof8zSWtws8PqjTu0bdeqAOArg0-uLLdF1OQ9RsGXTVHZxuaSoTfagGyjFDdjhWLl_7sFrFHEcUho8UVQbvh8zLC9nSw4NlPs2Xp75j6wjV4ziZbBSV1hp2LSEbsrbq4umnZBHuigymjTBX-JAe4ku72IYMN6WL4NmgZ3NMiqxYAvhXJL8g_IQ8VxVSS6TzjYijrUf-ctoM9dQFwqKRlOCs-P1701huIXTyFjqUbJA1xgPUoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
شیراز وضعیت یه پمپ بنزین بعد از خبر اینکه به عسلویه رو زدن شلوغ شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91960" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
لحظاتی دیگر تا سخنرانی دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91959" target="_blank">📅 01:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇮🇱
⭕️
مقام‌ارشد اسرائیل: در حملات امشب‌ به ایران تا این لحظه حضور نداشته‌ایم و در صورت نیاز اقدام‌فوری انجام خواهيم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91958" target="_blank">📅 01:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#فوووووووری؛ صابرین‌نیوز رسانه سپاه: الله اکبر. یه ناو آمریکایی رو با موشک زدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91957" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ برخی منابع خبری از حمله به پتروشیمی کنگان و‌ عسلویه خبر دادند. امیدواریم تکذیب بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91956" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
صابرین‌نیوز رسانه سپاه: اختلالی در اینترنت بین‌الملل دیده نمیشه و وضعیت پایداره. نگران نباشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/91955" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZWyzLkH34W3XVgrHP1pJX54L9S0z8NZXK1J_SbkYm2WVVANTAnSMdZQ-gx4Ap0iyl1Nw_Q_eQ39qpCI2T5PmJBJ6x4ikWkeFoakOogth0jRZJ7ccU360uEQcSES3DVsuN9u5n2y9BoeqiAUyRKyuWt4QLXvAoAUF0XaJEIjO68Ug28kUDQUEOlk6c2abqZWTg1T3-6Z4Z8LXEQkks9QuJad23CPRNVwve2i_dEaIQuHDqJX2HqiSG7VdDEtYifewz_UPc1IbqoBtdV9a_U0Vkumn1YP5efjPzu0PU_tvHAzC8QoQJpjBkvZSkOwfeerEtm6yfQPb0owsDSBZHVV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توئیت جدید صفحه منتسب به سید مجید موسوی فرمانده نیروی هوافضای سپاه
:
بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ
- فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ (بقره، 194)
- پس هر كس بر شما تعدّى كرد، همان گونه كه بر شما تعدّى كرده، بر او تعدّى كنيد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91954" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
#فوووووووری
؛ صابرین‌نیوز رسانه سپاه: الله اکبر. یه ناو آمریکایی رو با موشک زدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91953" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فوری
؛
صداوسیما: ترامپ بدلیل پافشاری تیم مذاکره کننده بر حقوق ایران در مذاکرات و عدم امتیازدهی به دشمن، جنگ را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/91952" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
💥
باراک راوید سخنگوی ارشد آکسیوس: حملات امشب به نقاط جنوبی ایران خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/91951" target="_blank">📅 01:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ صابرین‌نیوز: هدف قرار گرفتن نیروهای آمریکایی در نزدیکی جزیره هنگام توسط نیروهای دریایی سپاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91950" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
#فوووووری
؛ انفجارهای شدید در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91949" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی‌دیگر پیام ویدیویی سخنگوی قرارگاه مرکزی خاتم‌الانبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91948" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-poll">
<h4>📊 پوشش اخبار جنگ اینجوری خوبه یا کمتر بزنیم؟</h4>
<ul>
<li>✓ خوبه راضییم</li>
<li>✓ راضی نیستیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/91947" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
وال استریت ژورنال به نقل از پنتاگون: این حملات اقدامی از دیپلماسی قهری است که با هدف وادار کردن ایران به دادن امتیاز در میز مذاکره انجام می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91946" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ گزارشات از موج جدید حملات به بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91945" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91944" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=aKpguC9GegYuH3web1TJ7ie7YXEk0tj2a44bssQdYXmujVrpQONLkSnnDO2fdMId86b3Hx_roB3wbisv1LssjEDsUIMItCwByMM-OV1ENXu3qwSX4o848FDbL05deVze5uHgqH7nu8KOjEbOK-RGXao7EWUkFTWVQTPOgbQzV0CkzF2ORA98yN66srMvaQdCjqVpIha3XmBHX85w94PjZqZV3TWckK_sA2X1uetvCoGl-aDv2jeS6T_UuG3qqpor-fr3FFD56AbVWbuxEF95bVymjxw4lDclEl6Ds8RggnW7kyO_gJbZ-LLJLwo1Gvshnsg0kXNQ1eII7SYDuhtQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea7833987.mp4?token=aKpguC9GegYuH3web1TJ7ie7YXEk0tj2a44bssQdYXmujVrpQONLkSnnDO2fdMId86b3Hx_roB3wbisv1LssjEDsUIMItCwByMM-OV1ENXu3qwSX4o848FDbL05deVze5uHgqH7nu8KOjEbOK-RGXao7EWUkFTWVQTPOgbQzV0CkzF2ORA98yN66srMvaQdCjqVpIha3XmBHX85w94PjZqZV3TWckK_sA2X1uetvCoGl-aDv2jeS6T_UuG3qqpor-fr3FFD56AbVWbuxEF95bVymjxw4lDclEl6Ds8RggnW7kyO_gJbZ-LLJLwo1Gvshnsg0kXNQ1eII7SYDuhtQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جنگنده‌های ارتش بر فراز آسمان تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91943" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUZMCnjGDfI1dffiKDs-I2Bq0TKyrzcKqrcgZLbTQAU8W-ylkx2Tc9j9g_VNW9YUUkuW_RuI4Jp8Fxmz9j071fm1vPOp-6t5TG5b_TLDVRxY_t8s2D6trIDOqTugB2oOMLagJIxeuOzvinkDgaTfY5pYN9b0VWTFp5oT3nwnInHPx0f5nnuJkuGQA6qg0iZWMs2H85r8b9dBPqBcTGc5OUd8AUl_835giiOIzo7u1MiEqqtmssMn0EbiaLjBUygfj29isioPWszoFLCuGmk9LqCs2QeEjae6G5ARujJsd8zmJ4a71iffz2qeFRqx089F4iAzKso5xN8OQdTIsrd0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
Betegram.com</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91942" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ برخی منابع خبری از حمله به پتروشیمی کنگان و‌ عسلویه خبر دادند. امیدواریم تکذیب بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91941" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
#
فوووووری
؛
منابع خبری آمریکا: عملیات امشب سنتکام در تمامی نقاط حیاتی ایران خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91940" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از سنتکام: نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، چندین حمله دفاعی علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمی ایران انجام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91939" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kokUW2YJqyMvr6F9Luws4AlzHWDzhT3K6bUhfzEikQJh_8otgtnQElTlROcFOMo1Q16q6iVnpweUnO8c8UUHomfD-_6-rYzluCYWrdvw3cPG4ioPQmSZdXQiO0vXvwTVFsu8EYA7kFc60O_71vFWRkz4zejlLjkei87_J-tt78F5jSrZq_J7vqmyhxRQjMNvXOeQufK0pu4TzKXduvsMuSiJFt1W32IgDOYPiEQ-VPbDefCNh_Ne0SLr0DOKvbEpEXWWVMp_18K8EN0inQNEq_6NGwPIi18fGJaQejHLlELHck1nOFCkJ0QXOU3MZu_uvf51v8Y1Qo1dw4LjnWpJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از سنتکام: نیروهای فرماندهی مرکزی آمریکا امروز از ساعت 5:15 عصر به وقت شرق آمریکا، چندین حمله دفاعی علیه اهداف مختلف در ایران را آغاز کردند. این حملات در واکنش به اقدامات تهاجمی ایران انجام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91938" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فووووووری
آکسیوس تایید کرد؛ عملیات خشم حماسی در فاز دوم با قدرت ویرانگر ارتش ایالات متحده آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91937" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک سمت جهان جام جهانی یک سمت جهان جنگ جهانی
خدایاااااا بگم شکرت خندت نمیگیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91936" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فووووووری
آکسیوس تایید کرد؛ عملیات خشم حماسی در فاز دوم با قدرت ویرانگر ارتش ایالات متحده آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91935" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در شهر بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/91934" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ مقام نظامی آمریکا: مقر نیروی دریایی سپاه به عنوان اولین اهداف امشب در سیریک‌بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91933" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ اخبار تایید نشده از شلیک اولین موشک‌های سپاه از نواحی غربی کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91932" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2a236d0d2a.mp4?token=r6CFRr5-Me_DUGoyJ1m8wj_JHQLL5LWpTsgmt7uKSEKW1WdsqM9v6AQIvFVQR9FP-ULpFILB_MzHepXLdjgC8tavvrjnwBpxzIcUjcSPYW8Qlvq9JE4X0zWfQChZdauEt67xpqukFxhb4sJ-DyCrCBUBo1KaytOz0iSzUpRIOeaKef_LixTnywyqIyGSkhwSc4u2gVYv4cdbfHfLQSoHCXuLVuBC9pyuhx81ozUlA21csk1fB6McEFtfb1F-VCrsgfJ6qRj2m_yhecrw2JnVhbo8I-4yIJO9pUsxpgNJ3U3sv4UxLKMycLDieoyGnVW3ZSzXuGxyGUdPJ3DlsDDDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2a236d0d2a.mp4?token=r6CFRr5-Me_DUGoyJ1m8wj_JHQLL5LWpTsgmt7uKSEKW1WdsqM9v6AQIvFVQR9FP-ULpFILB_MzHepXLdjgC8tavvrjnwBpxzIcUjcSPYW8Qlvq9JE4X0zWfQChZdauEt67xpqukFxhb4sJ-DyCrCBUBo1KaytOz0iSzUpRIOeaKef_LixTnywyqIyGSkhwSc4u2gVYv4cdbfHfLQSoHCXuLVuBC9pyuhx81ozUlA21csk1fB6McEFtfb1F-VCrsgfJ6qRj2m_yhecrw2JnVhbo8I-4yIJO9pUsxpgNJ3U3sv4UxLKMycLDieoyGnVW3ZSzXuGxyGUdPJ3DlsDDDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس یکی زد به کاستاریکا
عشقم گوردون پاسگل داد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91931" target="_blank">📅 01:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ اخبار تایید نشده از انفجارها در برخی نقاط تهران و کرج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91930" target="_blank">📅 01:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ پرواز جنگنده‌های آمریکا از پایگاه اردن به مقصد ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91929" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ منابع خبری اسرائیل: در حملات امشب، احتمالا جنگنده های امارات متحده عربی حضور مستقیم خواهند داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91928" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارشات اولیه از انفجارهای شدید در اکثر مناطق مهم جنوب کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91927" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ حمله به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/91926" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
