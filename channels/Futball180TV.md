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
<img src="https://cdn5.telesco.pe/file/gykUWV9XQUAdp5Fx016ugoCslTVVqdkFyOXxBLquj_Viia63rMxXvTnjrMv9ljaeEOmcuJUn8JbWb9ZfFO_YTFiD5q6TQocY4hy5QHS7x3srDT_tDN3Mh_Vv4wWh2KY3ev0HKy06nJuQ3f-93v4vMaX7h1Qb67crqMVNMpBduw8UzFMm0UDOzI8Nn8juyXGB797GlFwlkABSk0xHpWxXdsP9JwfwVPBK6YC9nLMHkoUOFc3xJGzcH1ZMshbCJMsm1VacUf0R5qDT4hNaksgXUPYdszyi-Usddt9gbG_4kDF_StvhSibv6DNP48i6ToN5Dzq_W28j7yzOec6UXpQdDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 383K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-108585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/108585" target="_blank">📅 22:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/Futball180TV/108584" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گل‌اول وایکینگ به بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/108583" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108582">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
به نام خدا و گل؛ گل اول اتلتیکو مادرید به منچستر یونایتد توسط باریوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/108582" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108581">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگلگلگگلگلگل اتلتیکو یکی به یونایتد زدددد</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/108581" target="_blank">📅 22:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108580">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بایرن‌مونیخ یکی از وایکینگ خورد</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/108580" target="_blank">📅 22:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108579">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/108579" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108578">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برررریم سراغ بازی‌های امشب لیگ‌قهرمانان اروپا</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/108578" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108577">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
خداداد عزیزی سرپرست تراکتور به مدت ۴ ماه محروم شد
‼️
امید عالیشاه نیز ۴ بازی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/Futball180TV/108577" target="_blank">📅 22:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108576">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnaksNmSrqLUMKVrbinHkRWami6w77umYZ1MGDl7nul5bv0aLpJCq_zb27_1_biwIRd9qEQk6BgzJy73AZ7AN323FbSUbIqTFc6ET5wAIQGCgj1SGN0oVvhnJQcqvc_O0jUO8uz6Xg0rLE694TUxRMiBeAWSTN1dn2yS5HVRstJPFwrFKOKUi17ylTJJxbalPDDoJSvPB2x5axaQqU3PRmPlJqn9hQtyZgC-TPpAnbtEj4UcYUxjhRiAbdPi6AFysrSIguMniHs1UM_PrBKwHEfRgiGdxGDa_fTo8aafVLPBMLII794l2YJJc5rwAvLIjeFl67dM8L5peotSq-lZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال مقابل لیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/Futball180TV/108576" target="_blank">📅 21:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaJ0DGBh2SvFYNh_gXdzenrzuVXBQM1luQHOoFLv86cfEzmFT_R3gbBDcCwyLMxrzdkxhNTwgiS8Dk87EHlIBP9dF1aTjwXlSxKVVaphUwvaBbGwecXxCQSNl87htBInFTN35YkPN5Wecbfo9UjD4_Jkv8pI0gvPFID8Fl2hw89XFkFSfhkOb4V001GsxgRcpWkvW0weYSPd-Zf-KoWRT-VFAz0nbl-kQhOpmUA4FO-vHJkE5NhcOYpb4l5wV2rx3P0ia7wRuqRfwfas8BXMAFPjmTBDrrtw9iAW0ZTEE2Ck3aovz-Run4AuXNa4Lcy3-8GVkGDb9x00z7t_yEgmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
ترکیب بارسلونا مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/108575" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13c928814.mp4?token=FxWwu65w3CqnStdJ_zEaCYTqhSGEcdnTbOMLlan42jb6Iwf39XuB4ayi-YiQVAZ9yKNwQvkbXT1cbrOES-TLzXfH9w3tjhC6IWS1dC_5pAC3cMZX2Q3pfYcEedM4ybimKAqUhqArK2iKTr8V-F7FjaLkbZ2vaC-AqlsvOtC-25bKwLSWzdaxlyruvzMqXrqZk6A-C6mbYXVTqADsXnEgQ_xJ0UagL5Qk391HLMkoUj0-2n23oErufjN_I9vw_T16XQ5g0_InAAQg06ep8gzZRw4hKttPxUnb0mWIssEr1J3BmLuCT7iUVa68iGdZUe2XAjY1SjHNeD5LrfA9Y90clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13c928814.mp4?token=FxWwu65w3CqnStdJ_zEaCYTqhSGEcdnTbOMLlan42jb6Iwf39XuB4ayi-YiQVAZ9yKNwQvkbXT1cbrOES-TLzXfH9w3tjhC6IWS1dC_5pAC3cMZX2Q3pfYcEedM4ybimKAqUhqArK2iKTr8V-F7FjaLkbZ2vaC-AqlsvOtC-25bKwLSWzdaxlyruvzMqXrqZk6A-C6mbYXVTqADsXnEgQ_xJ0UagL5Qk391HLMkoUj0-2n23oErufjN_I9vw_T16XQ5g0_InAAQg06ep8gzZRw4hKttPxUnb0mWIssEr1J3BmLuCT7iUVa68iGdZUe2XAjY1SjHNeD5LrfA9Y90clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
آسیا محو تماشای یاسر آسانی، سوپراستارِ آلبانیاییِ استقلال.
😧
🔥
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/108574" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg7t--2paRONAHuAgPMaWN8cIqX3OYT4g_4CduievUEQm6R_yu8xj4d7-Vy-eUKK3eyd28QKj2ZZgI-ODQOAQWrsUslUpGm8eVD63qIFaQrdQD6hiCHmzY8CAjjAsyxJGtRwssQAylQUyAVPtPNiLe0oDCYc77NLz_E5Nrh8q6-rDNDqXgxm5U5vELec2oLQz31Cy9JxZDHXD9l-x6bJ30e0tdmMrqiWOySwyHzt06mjUb2ekoQtKZlchBkiFXUmZgRxGPgUTIQYmyVhRKpeZ6ZrY0zJ45xImwqDxXXg4hLx_jC1REI7auGQ0lbsjFTiwuSpH6Z_Gq2wzCuukzdGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت: دنی‌اولمو امشب مهاجم نوک بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108573" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=TuDEBfZpyl-iUFZlxoiy4z06WH2JVbJYHXRbUt89s-HFerzDaFWtDx2UiB8J577CZYblRbMHaUwbEu0RGpci8dZJE2iTntKBRojFHHsaNqJLkD723_EjIU7XLDU95f-ldDvU-UZKX-s24H8l5rFjPDyst09AtfQ2D-sdCJ-TZrZ7-qg1ujRBP-CEYVcL5HoM-bj1Xo9Ut4rFiLyy9iEDKbxnSvzep0jzdNqR05f_Pkyel1CEn8yxYe2WFmq05aG5V94XYKeKkrCJMZqMMBLsYjO1Z7wgHW0msEpHnPdpsvkV6LBXGrrfu26d3WcCffPEJwpnPqUVFNwceHHd4YeB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=TuDEBfZpyl-iUFZlxoiy4z06WH2JVbJYHXRbUt89s-HFerzDaFWtDx2UiB8J577CZYblRbMHaUwbEu0RGpci8dZJE2iTntKBRojFHHsaNqJLkD723_EjIU7XLDU95f-ldDvU-UZKX-s24H8l5rFjPDyst09AtfQ2D-sdCJ-TZrZ7-qg1ujRBP-CEYVcL5HoM-bj1Xo9Ut4rFiLyy9iEDKbxnSvzep0jzdNqR05f_Pkyel1CEn8yxYe2WFmq05aG5V94XYKeKkrCJMZqMMBLsYjO1Z7wgHW0msEpHnPdpsvkV6LBXGrrfu26d3WcCffPEJwpnPqUVFNwceHHd4YeB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108572" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=R81tn_YQMLDRd_roYppTc20vGpDWcQ-Gr9OfUk1VHBcQIjPZfvoRhN_N2RN4GzdqNMq2h-TBo3hcR0QubTRqd_OzTTqenui94ISg1pQqSqBF_rbQXh06x-y-KFZxGVz4ZCuEkUiR-VrtKvs0OmBBfq8ECDGFEA2NKRVJ8Xr_pj_mVwCTUu5DErfkRWq6CoUbBI1718u2APw0FW1IOLYTQtTNRPqfpnu186cmnf3oBBKHV4jX1lF04-p1JuvRKvSrEotLowHO8I5wxGgJgSSqv2tAioeSwKh8HEc3tN9hjCzhLaqS8gUyL57gjdutxoEix1K2ahe5cQ8a6BfllFYIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=R81tn_YQMLDRd_roYppTc20vGpDWcQ-Gr9OfUk1VHBcQIjPZfvoRhN_N2RN4GzdqNMq2h-TBo3hcR0QubTRqd_OzTTqenui94ISg1pQqSqBF_rbQXh06x-y-KFZxGVz4ZCuEkUiR-VrtKvs0OmBBfq8ECDGFEA2NKRVJ8Xr_pj_mVwCTUu5DErfkRWq6CoUbBI1718u2APw0FW1IOLYTQtTNRPqfpnu186cmnf3oBBKHV4jX1lF04-p1JuvRKvSrEotLowHO8I5wxGgJgSSqv2tAioeSwKh8HEc3tN9hjCzhLaqS8gUyL57gjdutxoEix1K2ahe5cQ8a6BfllFYIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108571" target="_blank">📅 19:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باند سفت‌های استقلال از یک فلافل شکل گرفت:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108570" target="_blank">📅 19:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
روایت خوبان‌عالم از بخور بخور در فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108569" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
شوخی سمی ابو‌طالب با کات‌کردن آسانی و زنش و احتمال کامبک: واسه خودم اومدی یا چون که یاس شدم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108568" target="_blank">📅 18:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds83LbkT-jb-N6U3Ru6dP9Gq1W6TtAkjjIn0i8FHv16vNbuHVfWsC_cFH0tkY46ZQdrW9sFQ7LqY6c7IqEZhD0wWymPaW9qJB2-1dLxQJAciNKz4ZOe4qyPt7ZXNYblctF1A35v14vKPZ4xyBzVEF9SGhgglPUwTgIXQU043x3MwbzpK8bwXapGVgXM3NxjRfjCyqcRGpfNlKC4jdbUg22HhxTHHAIZFXVQxGTk7eqTdIWjJiH_BawGGv6yJ6knzEnQsDlxdcUus8NNt0DknSfl93JjzBUERCGzlku_3Knvz7Ju-CZl5qs81tq75vBWYTOkYrj9Ak--A3j2FYx39Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
❌
لیونل مسی قرار نیست در مراسم توپ طلا جامی را به هیچ‌کدام از برندگان اهدا کند؛ چرا که برای این کار از او دعوت نشده است.
❌
حضور مسی در مراسم توپ طلا هنوز قطعی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108567" target="_blank">📅 18:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa1WngsGmgnCl5xVRCH8yF99Qv9AKRP4TbiQX-x9e9PTqDW5ZMF9cGfHx8NB_34JrRRXWEdYW6O7pxC4KeJtWuxE3Ng-At8yJGxsJxYgWtvfcMcwjWYN5RWu5-T3QCLu4VjLrp6UZV-ORmD5LWz4XhgMGqZQhtpQTrUpkfQxNBZxhGKz59cJe72ogklqKj5ans6FzhsmFlQ9Y2nsBgK6YUu1mDXPVbAxVu3FvFAdj-RGkQznTQ_2YNxXYca--EZn_rivUrdUG-5znx1S7k_xHc05scPMytsyjcTE0dzye0nC1t6t6AVdlky-yvSoTLGib9_YzxPIYBNABo8MA95pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیگ برتر ایران|سپاهان فاتح دربی اصفهان شد
🔸
ذوب‌آهن یک - سپاهان دو
⚽️
گل سپاهان: محمدمهدی لطفی و کاوه رضایی
⚽️
گل ذوب‌آهن: امید لطیفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108566" target="_blank">📅 18:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108565" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108565" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6fF7vOhnjGBvdE49YjNi5Z5bsPFGoZDqrwul9g_ckRUBZPMHttHPIpeOimonKhEOuflMCBD0SK2EZUJy8x__qL3fvJkP-ZuoVw4yh-yWqgMEBSzJH3iLIHrf90vctY2LiEDtIpBHKex6-p3LtwYBI3sawbaqbqMNykq4i9yiYYSxCBUM9cZ1igo3akplisDZ_V7-9jB5ylJh_siuzURserqnhusAiVsEfvbLS_6R7dO0_1T484RRaU9YpPcT1PXYOTkwZ7LQflY5Xhwf3r2jm2BRGvEJsZnQsZKjXN2urimCIejsNyeXR8pw_RNYjqKYzSIBIOJLk2OKYr3xJQzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108564" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19588c007.mp4?token=W79oLmOYM5S-ErAcmgm3eL0BS0Nls3kPAYe0IGtAGVBweOY1Xk8KS3xl7h32Mlm6x49Is4mx5XNgb7i3z-LL8awggtFfQ1NwtIv7ZBrBnOoFfFJSM9oY_zV4XAG9pdOUnPNWG5G1XOAZLKK5BDlp8kpRODxrmKM_6Pxvaa_TX6T1b3reKRdN2S419xVxXOsVxWPR7PthlARXw9sBHqVCa_UqkC-MHbsYHvONpGAyheBjfyGXG0_ZFQ1oA87EUv3Sdz6BOtTCtrv6AEw_i25d0sXL-VuPhIUd-K-AEY5Arz0HLiRJc3YN2yTrcTzZLpiqOCFoer33nTVh4Vu56HqwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19588c007.mp4?token=W79oLmOYM5S-ErAcmgm3eL0BS0Nls3kPAYe0IGtAGVBweOY1Xk8KS3xl7h32Mlm6x49Is4mx5XNgb7i3z-LL8awggtFfQ1NwtIv7ZBrBnOoFfFJSM9oY_zV4XAG9pdOUnPNWG5G1XOAZLKK5BDlp8kpRODxrmKM_6Pxvaa_TX6T1b3reKRdN2S419xVxXOsVxWPR7PthlARXw9sBHqVCa_UqkC-MHbsYHvONpGAyheBjfyGXG0_ZFQ1oA87EUv3Sdz6BOtTCtrv6AEw_i25d0sXL-VuPhIUd-K-AEY5Arz0HLiRJc3YN2yTrcTzZLpiqOCFoer33nTVh4Vu56HqwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
هالند و یک آمار عجیب؛ او بر خلاف امباپه، در تله آفساید گیر نمی‌افتد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108563" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108562">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=LIbZURTB0ZmOMcPik7bmZLF1pZI5HgkXaQrHoYphKU8gJd2EYLTRclLb47bWc_9A3c6KGoWS7ERKM5YrdONJ98tE_x0TLGEz2qoAKZbmyY_h2bU3zJLdtlXL7huHnGFkjKgM7NNsM71NU-c7XF8T2g942n0gPSZWDw5blg_7AjQCx1TsKsYlnI4Zs1FwILvEE-hfAg25ZW3cnwORn0zq2OcMmBxNmCzH1iXQyj5IKF2sh26qf0f4MNTisfISjDgNl5Up_W8D4gbn4-6VU00PjmUdhzUD_HjGOEEnY6VSBplQV6KL0mbOk7Ao6WnsoTO-k9OkbeMwraab4Iu1-P1YWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=LIbZURTB0ZmOMcPik7bmZLF1pZI5HgkXaQrHoYphKU8gJd2EYLTRclLb47bWc_9A3c6KGoWS7ERKM5YrdONJ98tE_x0TLGEz2qoAKZbmyY_h2bU3zJLdtlXL7huHnGFkjKgM7NNsM71NU-c7XF8T2g942n0gPSZWDw5blg_7AjQCx1TsKsYlnI4Zs1FwILvEE-hfAg25ZW3cnwORn0zq2OcMmBxNmCzH1iXQyj5IKF2sh26qf0f4MNTisfISjDgNl5Up_W8D4gbn4-6VU00PjmUdhzUD_HjGOEEnY6VSBplQV6KL0mbOk7Ao6WnsoTO-k9OkbeMwraab4Iu1-P1YWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ده نفره گل زدند
⚽️
لطیفی دقیقه ۸۴
ذوب‌آهن ۱ - ۲ سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108562" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt0H_3KLPouuoXmKT1wk0bhxkw_8DM2vLNdBDjI_cZQJIJdZ6nPdZ-lSlLjkTiazjiGoSql0C37FF6DfSYOlCN4I151VhRsvQYJ3asHeZM-aYbkgxedFyXrbLfJH6tpFOHmEt0wptfWuCHd52Zn9v__EZBXNYNlwOA69Xf-EegrRrc0ZlzS-1NGmfLLpZS8BwJc4M3SVy37WCX1Trgyb8Ph7CFRWSN546g3gJdHD57ImqgoX_IFQ9zIZdLyEY2S2q2OEy_H_zVw291Fzs1WtDdhRiDaORiUxLx9zIx6JsVXZJjliDjVdotoC8d_ZImWBueFSwRtP1hYPj8U838angQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نسل جدید خط هافبک منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108561" target="_blank">📅 17:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57b850047.mp4?token=E1snnVJIsn7S7Y_Hd2AHLo2wvCpP7Upk_OJBxtgJzgC0SaqCqYF91tFSxmmMykTmMYA1FKpJi-mHclMnAX3WSPx4PIHKxtAyOhDYFJZNA1okp6i3H0cHqHZgKRicAnXmMkjnMb8u3trw4nMAnZ7Iiaoj1lyn8ZOmtk5XwnJPhwq0z44w5v9uoYThvqVZ-juSaB38S4y_KVJQzyfhNX3LQx5zRl6F_91AHS5H3_lGGCna_selh0l45eI7RT8Hkwi_Lq_BwmfV0HqlEyxx5Doj-9jk-We90DAWaKpUI6drsux24IfyEqqCwj2rAE1VxvXqVKMBBYaIZhCcBsKbrUx6IxRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57b850047.mp4?token=E1snnVJIsn7S7Y_Hd2AHLo2wvCpP7Upk_OJBxtgJzgC0SaqCqYF91tFSxmmMykTmMYA1FKpJi-mHclMnAX3WSPx4PIHKxtAyOhDYFJZNA1okp6i3H0cHqHZgKRicAnXmMkjnMb8u3trw4nMAnZ7Iiaoj1lyn8ZOmtk5XwnJPhwq0z44w5v9uoYThvqVZ-juSaB38S4y_KVJQzyfhNX3LQx5zRl6F_91AHS5H3_lGGCna_selh0l45eI7RT8Hkwi_Lq_BwmfV0HqlEyxx5Doj-9jk-We90DAWaKpUI6drsux24IfyEqqCwj2rAE1VxvXqVKMBBYaIZhCcBsKbrUx6IxRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صعود تضمینی برای تیم اسپانسر داوران
ماجرای عجیب صعود آرمان آفرینان به لیگ دسته اول نوجوانان با حضور در رده هفتم؛ دلایل فرافوتبالی برای ۱۹تیمی کردن لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108560" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=vJeOLzk6VFCOBpBJhh8KnoNVuxzbE1fcvPMmjIYFHFWhODOEOKG_s0xgQhR8GlqnKLEXUiyw1idW1d6Gk1in2O23n0iOrpKNPsh27u1cTEl74W1PRgfjnYVui3_ZfMo2nEGnSLtkiimH00o0s-c9hv899oLMZt6nGNLr7OxdtUd3ASqDC_bb998Kcmx2bl1Qr_HpcxGVEBiHSXXngOZp2A9HmFKUzph8rNsfD-O9Ql0fGcpY0BhYS2NFhc_cO480GCNv6mcouDF5ScF-3aX5vy5ywBm1pAD99YRHrSkTgT65zpBrwNGlnh9dSllL0U04dS-FC31EU7wKFdljRo7FOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=vJeOLzk6VFCOBpBJhh8KnoNVuxzbE1fcvPMmjIYFHFWhODOEOKG_s0xgQhR8GlqnKLEXUiyw1idW1d6Gk1in2O23n0iOrpKNPsh27u1cTEl74W1PRgfjnYVui3_ZfMo2nEGnSLtkiimH00o0s-c9hv899oLMZt6nGNLr7OxdtUd3ASqDC_bb998Kcmx2bl1Qr_HpcxGVEBiHSXXngOZp2A9HmFKUzph8rNsfD-O9Ql0fGcpY0BhYS2NFhc_cO480GCNv6mcouDF5ScF-3aX5vy5ywBm1pAD99YRHrSkTgT65zpBrwNGlnh9dSllL0U04dS-FC31EU7wKFdljRo7FOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
اخراج محمد حسینی و 10 نفره شدن ذوب آهن مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108559" target="_blank">📅 16:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=MBeg2rGxQ6L0b-bGOagMngUV7dDwIWc5q736IZ6ulvznz64wt7WWkouwCM53eLbLm1xH6ie4UbdWRqYQV1eebOOoOyTY9mdcATqdt5Hliepm9twXBmEMbYf0ibzase4l-UdzRtbHBmqs7Dnqd3qzNaccwwRo7JWB6OapgcNEn-CyelrreOC3a-4PDpJq95CQnPeHqK5puATYi9fyH_tiGjGKNS1D_OwJ1Je_5e1JDaOAl-mnoktIkg_T4I3TcIj0c-QePg_qzWnQRdtLtZAAI7AHDpN-8vd0w43eJlLagyTbZr4r6VNxP8qHItejeGkSdsmXz9R9JcyIpNjv0sKVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=MBeg2rGxQ6L0b-bGOagMngUV7dDwIWc5q736IZ6ulvznz64wt7WWkouwCM53eLbLm1xH6ie4UbdWRqYQV1eebOOoOyTY9mdcATqdt5Hliepm9twXBmEMbYf0ibzase4l-UdzRtbHBmqs7Dnqd3qzNaccwwRo7JWB6OapgcNEn-CyelrreOC3a-4PDpJq95CQnPeHqK5puATYi9fyH_tiGjGKNS1D_OwJ1Je_5e1JDaOAl-mnoktIkg_T4I3TcIj0c-QePg_qzWnQRdtLtZAAI7AHDpN-8vd0w43eJlLagyTbZr4r6VNxP8qHItejeGkSdsmXz9R9JcyIpNjv0sKVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | کاوه رضایی '23
ذوب‌آهن 0 - سپاهان 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108558" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108557" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxUUGEQTnfE105jB7F7EfcQDNEFPqdjMgPUQq8v0BdJv8ZYMtTNpVX6lNAV1ZJULDQoVOIdHlQz_jpIbAVtrOb00ubb2IFX4Py5bTB0oOvM0EElII1G9L9nS3Dj3jm9VtOeejFb4q9pnYQldeJS9xdnrbx9xg3WqJ14QrxEUl6agh8zAUAHSuTrQ70AUgULZAtB3Nq7Yyym3OyBv8i8xsupwYGrl2uf5bk2m3CgLkF9hi_CpQ9QGpm2Dfp1aDiQZif_lZwViIFTkuUdhH9E4PdQ5a-38HiDaoa2mcl8v5ZGIF0d0RM8xEJHsCZa9EbMP15mWQRqmxalZRpXuUQJ8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108556" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5299108b84.mp4?token=jC1ZCPFwS0x5kvmO01vnhrfFoHhl8UVvZZSLCkRcDRAK-TLP0cafK0kd6qcR6y9sG4s7rANCWW57dYObrA_O-jY3q2W2i51SVZY7JXQQGFZgti_ZgXtYWZNvzAyoja5RxZTmASgAkVJvpHfJFFyMoO_mgF8BIQx-ugtoCEFvoPooMgxJmUU84Gji_8MzirzZi5siNrzdRR01EKk3zNkswXAcmbWkqYK3iEx9BjMk_XCFhUTLagWAI8F4z-Zjfy7bRP59KcF3myzyMbFzwPuWGK7OzVveVrAOqfo6LQ3BN-dZTLKkiYENJCBbEiWJT-086vc66jneSNXUD6X_T97UTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5299108b84.mp4?token=jC1ZCPFwS0x5kvmO01vnhrfFoHhl8UVvZZSLCkRcDRAK-TLP0cafK0kd6qcR6y9sG4s7rANCWW57dYObrA_O-jY3q2W2i51SVZY7JXQQGFZgti_ZgXtYWZNvzAyoja5RxZTmASgAkVJvpHfJFFyMoO_mgF8BIQx-ugtoCEFvoPooMgxJmUU84Gji_8MzirzZi5siNrzdRR01EKk3zNkswXAcmbWkqYK3iEx9BjMk_XCFhUTLagWAI8F4z-Zjfy7bRP59KcF3myzyMbFzwPuWGK7OzVveVrAOqfo6LQ3BN-dZTLKkiYENJCBbEiWJT-086vc66jneSNXUD6X_T97UTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاهان خیلی زود به گل رسید؛ لطفی در دقیقه ۲ گلزنی کرد!
⚽️
ذوب‌آهن ۰ - سپاهان ۱
گل: محمدمهدی لطفی '۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108555" target="_blank">📅 16:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263d796f58.mp4?token=Y11-FeahSbfYJfntmgNnIGVEpNv_rnl_9sYahy4c6pFxIMS-txsfNhTIf7i3vfglppBJVw_vrbKfpiRDZsscOC-VsqRque3PoWGp-jjNf_nkUQ9CiE5Cr_Ksg53gc5DVoVkd-_nBNTt82oem2OA5TtgXkQhR5PBVLshwcY2flha10DmhdeV705j8TTAD8jpS2uOQ09TqMip1rPQ-AfUaoCir14FwhU6mtY4EB8K7uG_C3yQ93r34a11UaSW0677wepgh8QkSAxsgBcIYFMJUB1yamNbo4D_fItLNwwdkX-oi4EEYkL9VtWzvQuLLGxcKqsVPk-ieCfYvIposIKZ7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263d796f58.mp4?token=Y11-FeahSbfYJfntmgNnIGVEpNv_rnl_9sYahy4c6pFxIMS-txsfNhTIf7i3vfglppBJVw_vrbKfpiRDZsscOC-VsqRque3PoWGp-jjNf_nkUQ9CiE5Cr_Ksg53gc5DVoVkd-_nBNTt82oem2OA5TtgXkQhR5PBVLshwcY2flha10DmhdeV705j8TTAD8jpS2uOQ09TqMip1rPQ-AfUaoCir14FwhU6mtY4EB8K7uG_C3yQ93r34a11UaSW0677wepgh8QkSAxsgBcIYFMJUB1yamNbo4D_fItLNwwdkX-oi4EEYkL9VtWzvQuLLGxcKqsVPk-ieCfYvIposIKZ7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇮🇷
مقایسه سوپرگل آرین‌روبن و یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108554" target="_blank">📅 16:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=iDniCI2O8sGForq3Bin-R-nafcabvTxBy5Y4RSuw64_YtvoSqzt225135ktt1eIvt34_B3G74VRX7SFzL-_GQex7tSvlbRSlFOBbY1o6DmCKNz4NYtOkSczisO16HIEOm_V3uoB_2BPH2AzOgK6ZQOuRHMNk9pXxYdquycn2HJeTDRIec-c_VI9vDqP5B1DDJ1XjpxIwPxPdnDwWOes_npev6pO0xWNqQ6sQuJShr2orfKkLo8t1hNbO6z0WajTPVEPzXrgoJWuz_NXXjF0EV98z0-mob9yo1f3q0nwiKL5HNffGjG9Vsgm9_jsmE7vlSV9iDhHHxjbie9mvHSG4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=iDniCI2O8sGForq3Bin-R-nafcabvTxBy5Y4RSuw64_YtvoSqzt225135ktt1eIvt34_B3G74VRX7SFzL-_GQex7tSvlbRSlFOBbY1o6DmCKNz4NYtOkSczisO16HIEOm_V3uoB_2BPH2AzOgK6ZQOuRHMNk9pXxYdquycn2HJeTDRIec-c_VI9vDqP5B1DDJ1XjpxIwPxPdnDwWOes_npev6pO0xWNqQ6sQuJShr2orfKkLo8t1hNbO6z0WajTPVEPzXrgoJWuz_NXXjF0EV98z0-mob9yo1f3q0nwiKL5HNffGjG9Vsgm9_jsmE7vlSV9iDhHHxjbie9mvHSG4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله مجری صداوسیما به سرپرست تراکتور تبریز: خداداد عزیزی توروخدا بس کن!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108553" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xdsc5nKQEnzlEKdwfqVOtpURPe7Mq68ihfiyIvW2XLYQ2T6k4P1rFM-zbW1-G4MWgaIs37H8x0rpuUjCdyQmqZPqc9RW4BQeN31uANvuZLf6CyK_yVG5wwjrOYAYw5ZjEgv9TzIGqpF9MY8kx3kFdoqBSui8sxUUa3Zb746niicDWXyZKSOfsXirA4Hp5AY664YuYvpkYUaTi09WTxHlo0MT2gFusIsll94O9BunYykiczmiLtrCMlpwCLUv7z2CPJAp-V-siGZ07MZknAy9g0qfA9sZsDzhHqrNVleaddbXJbrJlGXjoZfCpQgBz4mv5Mg8p0DUa8_vlminZqGhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دانیال‌ایری مدافع پرسپولیس پس از طی کردن دوران مصدومیت به تمرینات این تیم بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108552" target="_blank">📅 15:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=UzRXy01dv1srVA9Ux2BvjEEZEgiYD3cPE2IdUBZnM_OKh49HI0dQhGEj4P8HN99VdAMgxif5rFbvPBMBDV1HlI5re_6GPEt2bz1LSzrvBJWiOTliwlsvfQVXr290dFNndrzrTTM_eo3awOpSLn6gLoivDO0h7vlqZCSNISyQ908C68greGUyBlXM8-N84sd3sRAFYHsOJrT61xYNjPVPWxwVSNk_fD0x9NET56PJmh5YAV1B4rMeqj9lWnA0oqm0yH8bc8uF9q5QIla_WgT55acHV1HKCKHeetEazywPwFWQaRtpUODKZvOO55XLuKfN-PhxyDV271D5zc_uJiPyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=UzRXy01dv1srVA9Ux2BvjEEZEgiYD3cPE2IdUBZnM_OKh49HI0dQhGEj4P8HN99VdAMgxif5rFbvPBMBDV1HlI5re_6GPEt2bz1LSzrvBJWiOTliwlsvfQVXr290dFNndrzrTTM_eo3awOpSLn6gLoivDO0h7vlqZCSNISyQ908C68greGUyBlXM8-N84sd3sRAFYHsOJrT61xYNjPVPWxwVSNk_fD0x9NET56PJmh5YAV1B4rMeqj9lWnA0oqm0yH8bc8uF9q5QIla_WgT55acHV1HKCKHeetEazywPwFWQaRtpUODKZvOO55XLuKfN-PhxyDV271D5zc_uJiPyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سمی‌ترین ویدیو از حرکت زشت وینیسیوس
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108551" target="_blank">📅 15:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=kNXlf1zxAN-Z3aaE76Xw6qIXnu2HuFPDZCjqCGz1_97345BIot1fCavbBwItZJCkylbMSJNf1oyDc2hurtGNi00ab05PBLoI_Tksq23W-OPNpCma86SUN2zci6K4PTZL9Kg7qNwdWoG2-YA9i-Gafm6Spy_RArRYqOHQCmbPS7e75cJ3Tfggya4a3H2GfdC32DSemdimM6XpMLA-kiw5ergRX4h8FoHEd4uv4LuuDr5yGcNxjn6JPqCoefb_TIgnBtVLjiFDaWdt3uov-awAKqp96lsvNixkkEfWUO8HB7D5967GJLlTDbIaUKq284veO_V205kQDBS19Z8ur7JWpEZMpN1XeZz4PWBelQJTs3X2IQxo4xw9Y8Cd7QA6lDLqkFjoBJJEM1XhcRp6V-x0jsG5TXa9fcMkx0uRNy3KfLrWT6ZvAj29L2cbE1I9OoT4VfsOsxjVbTe5BGz3tXNIyeFlmfMSMSxSpFJDNt6v5zURIS2j9KZSjoypxGhZFyvRX2LTQsMvsAbfhvdf4Hud0Dd-g2uJxIz7hHmgk8xdsRS1I7cPeBRdaDDyKmVgNfeGhUf2uUx0pBJvNI2oHl9HF_DHQ_TIUDzBP1PJ1z44oypxm7e1PGz7KiYm7bte_8wEcfiMmz0p352THO7cY7PUV264kzMu15RSEuQ0oJRB2oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=kNXlf1zxAN-Z3aaE76Xw6qIXnu2HuFPDZCjqCGz1_97345BIot1fCavbBwItZJCkylbMSJNf1oyDc2hurtGNi00ab05PBLoI_Tksq23W-OPNpCma86SUN2zci6K4PTZL9Kg7qNwdWoG2-YA9i-Gafm6Spy_RArRYqOHQCmbPS7e75cJ3Tfggya4a3H2GfdC32DSemdimM6XpMLA-kiw5ergRX4h8FoHEd4uv4LuuDr5yGcNxjn6JPqCoefb_TIgnBtVLjiFDaWdt3uov-awAKqp96lsvNixkkEfWUO8HB7D5967GJLlTDbIaUKq284veO_V205kQDBS19Z8ur7JWpEZMpN1XeZz4PWBelQJTs3X2IQxo4xw9Y8Cd7QA6lDLqkFjoBJJEM1XhcRp6V-x0jsG5TXa9fcMkx0uRNy3KfLrWT6ZvAj29L2cbE1I9OoT4VfsOsxjVbTe5BGz3tXNIyeFlmfMSMSxSpFJDNt6v5zURIS2j9KZSjoypxGhZFyvRX2LTQsMvsAbfhvdf4Hud0Dd-g2uJxIz7hHmgk8xdsRS1I7cPeBRdaDDyKmVgNfeGhUf2uUx0pBJvNI2oHl9HF_DHQ_TIUDzBP1PJ1z44oypxm7e1PGz7KiYm7bte_8wEcfiMmz0p352THO7cY7PUV264kzMu15RSEuQ0oJRB2oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رامین‌رضاییان خودش رو چشم میزنه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108550" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Gb-X875jYknWo6WIrsCdInBb-IgxZVEtyw7bPeyk98PfmZ6U7K2wagUv7CiAbM00DUqoEene4MbwNOqtjT4P3_Ov06lq16I3ZGvnaxKWeuknvS38ic7avObkxhep--CYhQF6L1yFV6DaKK5GLOVfaSALi3z1DPlpo1cPW1G6BF3lFX0MroXqbSwN7pVRUBbBGkAv1y_OgcDEQiVAzZKVhPdde--nXY0itJ8-KhomfLWQ7G67C413aEsBHFqSCQZsZ7qIhqlt3Sr3U6hbxZvPNC7O5MjB95PEz_iefGRSHmWq_abNb8hlvUU7QYSdK_EnNdK_GxDE7wzSXfMOXwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
بهترین خطوط حمله این‌فصل فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108549" target="_blank">📅 14:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZu9vW41i-ZhJB5JjI84u1JWXJ18MhgK-cJ9E1L-K1e0KNr-ah6q06RFp3D7xx-YZhHDafgpZym0pfScd0PYSEpBZaJoKyRcLQ-jS2r1nLsJI9cVJ40IOuIfwi9aRHbrotPt3BjUaP3VA03IXEDsi6SdtXZvxtXRS2F0kqG3vdW01z_DYuPSuFlGT-IqkUDX4cgFfohcrZLN_m12ro_JBkvqNdcn_vlKevnLBtG8uqAPoKD0FRVPkCRLpSowbLxgLr1QjitarJzRn4DdPAC2VkDuWO7x2kO9jGgwNp41iQNJ1aLymXO3S2cKJwDFk-M9i5e3D21mxeNLGjFpiSPn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
محبوب‌ترین رقبای ارلینگ‌هالند در‌پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108548" target="_blank">📅 14:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbaca5bde.mp4?token=HRSSQN2lw_qDato1vACxU9s_ShnDky8y3lajsl7tKnmc0e2GWWNpLXv1CM0oM7MdeSUDDTRRowQ1Sig3Mwv9dUodxo275u1N2LasGo_JQKaE-pj4064x7KX0cgglI5S_fu9C1VOGLyYU_Nqy5rk7k_HjDfwbE_uJNJ10gk4sHfFxx5Izeq6z6tQNV7ZweU3YrVIc89f-xv1rLwuWRXHRCWAa3tq1IU4fjo7jYaj4c1kFMO1wCDW-K62J_M5AjHu0LNNfmJqyChYV59nGg5MSf6fXdKX3Ck0l-Gt_Fdwmz8e7J1vzcAUvYZ_pvfxUzSKgG1kI2M-IUo-krIRbj0GzaHfB6ahdFXMy9aeUlUkzfRKpt3lpaYzmXZqSIljQpCqJNGixXRd3wAwvrv3SaJ28LqM-kOsUbQ5fYhqLWIr89eqBXzfH06d4pv10_ClSwkLaTsP6_6cTGptKIKP0p6Erql3sDmKFeXhrB_NzUhGmgFwFkJFuEE3iU6v5MPtuOacruXbFY007ZF21hpCg6z27B-WU9guWqUV75fxCrzgJkYoHvZyLr63YYTWGlTYm-9WvZd-EoyX59ET59UZ9YFgvPuHkl3OpXLUvvJjYB-z0Frwb1BTT-L3s3wQeqE7n0SF8aXujXEGPcQK2k2RkQIne8L1zsAl7pHg3dCWWpahL6cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbaca5bde.mp4?token=HRSSQN2lw_qDato1vACxU9s_ShnDky8y3lajsl7tKnmc0e2GWWNpLXv1CM0oM7MdeSUDDTRRowQ1Sig3Mwv9dUodxo275u1N2LasGo_JQKaE-pj4064x7KX0cgglI5S_fu9C1VOGLyYU_Nqy5rk7k_HjDfwbE_uJNJ10gk4sHfFxx5Izeq6z6tQNV7ZweU3YrVIc89f-xv1rLwuWRXHRCWAa3tq1IU4fjo7jYaj4c1kFMO1wCDW-K62J_M5AjHu0LNNfmJqyChYV59nGg5MSf6fXdKX3Ck0l-Gt_Fdwmz8e7J1vzcAUvYZ_pvfxUzSKgG1kI2M-IUo-krIRbj0GzaHfB6ahdFXMy9aeUlUkzfRKpt3lpaYzmXZqSIljQpCqJNGixXRd3wAwvrv3SaJ28LqM-kOsUbQ5fYhqLWIr89eqBXzfH06d4pv10_ClSwkLaTsP6_6cTGptKIKP0p6Erql3sDmKFeXhrB_NzUhGmgFwFkJFuEE3iU6v5MPtuOacruXbFY007ZF21hpCg6z27B-WU9guWqUV75fxCrzgJkYoHvZyLr63YYTWGlTYm-9WvZd-EoyX59ET59UZ9YFgvPuHkl3OpXLUvvJjYB-z0Frwb1BTT-L3s3wQeqE7n0SF8aXujXEGPcQK2k2RkQIne8L1zsAl7pHg3dCWWpahL6cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
دلتنگی همسر هادی‌نوروزی پس از فوت کاپیتان سابق و اسطوره‌ای پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108547" target="_blank">📅 13:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81a66e7b1.mp4?token=Tl9wTT5DyKW-SkoABM4tX9g_nC3XppdwOenBMi2stD1Qs7xOsmLMbzG-8nTmIm76-jmkREaKw8a6UfpT4stbY-NH5fUg8k_m6GMHznb5Z828vZS6VyFw1lWjRFZjWZ_xZ3mD57aBa94vARKTJqtmVH9oroN7tTVWGOPIzsLTB_kP9wgBS2Fq-iOX1U5K1QbyMJQDYGXy2oW-RU_hVQGrQooEoPGWrOos-5g-uZ9TrYO06OabGqRitxe2wJko8tMqMfmhFxrW5g-bmQfW_207YJ91p8p-ALTWgEOXijrWGjy1XkQDQxoNdSWgNK9yU_40kvrm4oNdF54RvSE5ZWB7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81a66e7b1.mp4?token=Tl9wTT5DyKW-SkoABM4tX9g_nC3XppdwOenBMi2stD1Qs7xOsmLMbzG-8nTmIm76-jmkREaKw8a6UfpT4stbY-NH5fUg8k_m6GMHznb5Z828vZS6VyFw1lWjRFZjWZ_xZ3mD57aBa94vARKTJqtmVH9oroN7tTVWGOPIzsLTB_kP9wgBS2Fq-iOX1U5K1QbyMJQDYGXy2oW-RU_hVQGrQooEoPGWrOos-5g-uZ9TrYO06OabGqRitxe2wJko8tMqMfmhFxrW5g-bmQfW_207YJ91p8p-ALTWgEOXijrWGjy1XkQDQxoNdSWgNK9yU_40kvrm4oNdF54RvSE5ZWB7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
محتبی‌جباری اسطوره استقلال: «من با کلی مصدومیت بازی کردم، اون با یه مینیسک خداحافظی کرد!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108546" target="_blank">📅 13:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab7ed9c6a.mp4?token=SR5odQD2AOsDMjaXnbdta3oOUYHqMGPi72CqqpMNIJO2hSb7nvrrxQNPOLLZe8f9-kRAphc4h_P7P_nuhBzGLnmtIbZjqu8OsHUibtd1lFO4Yyg4G6fRaRzQbusFdN1lHkaFrpGlJb8S75dLSkZuBcqRO_gWBZXD0h1s7mThhtTpssK8taAYsIrKpwqfbCLHMYi3rcFoPp6bl0lYgno9EKHcYTzQs9hmnaj1s8WeqULVMX9F04_fMk18TIj93ua8AteCTyzLU89oOmNInwbAmQt0nvn_sJdJ6qMaaLMskEAdRfn7I1rplbKcz9oJZcpQM_8Qc1b50nTaKua1Dna5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab7ed9c6a.mp4?token=SR5odQD2AOsDMjaXnbdta3oOUYHqMGPi72CqqpMNIJO2hSb7nvrrxQNPOLLZe8f9-kRAphc4h_P7P_nuhBzGLnmtIbZjqu8OsHUibtd1lFO4Yyg4G6fRaRzQbusFdN1lHkaFrpGlJb8S75dLSkZuBcqRO_gWBZXD0h1s7mThhtTpssK8taAYsIrKpwqfbCLHMYi3rcFoPp6bl0lYgno9EKHcYTzQs9hmnaj1s8WeqULVMX9F04_fMk18TIj93ua8AteCTyzLU89oOmNInwbAmQt0nvn_sJdJ6qMaaLMskEAdRfn7I1rplbKcz9oJZcpQM_8Qc1b50nTaKua1Dna5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
جلال حسینی در گفت‌وگویی به استوری جنجالی علیرضا بیرانوند علیه علی دایی واکنش نشان داد و گفت: «وقتی استوری بیرانوند علیه علی دایی رو دیدم، خیلی تعجب کردم. به نظرم این‌جور رفتارها اصلاً درست نیست؛ علی دایی اسطوره فوتبال ایرانه و همه دنیا فوتبال ایران رو با اسم و افتخارات اون می‌شناسن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108545" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1646f8600.mp4?token=Z0WuEfS4Qa7wNrbrCLsEKaoia5T1qA89h3nPh5Ij-jbLciciAiye899n1-SwsOaeaHhIKK4w6EllBC-2ZQ03ybDSw9i3jVTjEyBUPRw7o08Gkm2fyPt8lB2EAaPDdoLIaQ-68f8y3wCn_TRp2Ui1Pp1A7c3zjPzgeOjAshbCtdXrRofwpMCWLoVOYylL139DaScdp7mfr3_4sXBGqlBaZ4sR5k6NsumhB4VyBlHPHOcLqbG7bghCth2SNddcvGvgohj-dwqf2-_PCPczfScdJC2h5g_tALKqo3XciKg5HTr9-dJWzZTppuNuncW9UjWfCu8SKMOgyuqC_6xSzz0M2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1646f8600.mp4?token=Z0WuEfS4Qa7wNrbrCLsEKaoia5T1qA89h3nPh5Ij-jbLciciAiye899n1-SwsOaeaHhIKK4w6EllBC-2ZQ03ybDSw9i3jVTjEyBUPRw7o08Gkm2fyPt8lB2EAaPDdoLIaQ-68f8y3wCn_TRp2Ui1Pp1A7c3zjPzgeOjAshbCtdXrRofwpMCWLoVOYylL139DaScdp7mfr3_4sXBGqlBaZ4sR5k6NsumhB4VyBlHPHOcLqbG7bghCth2SNddcvGvgohj-dwqf2-_PCPczfScdJC2h5g_tALKqo3XciKg5HTr9-dJWzZTppuNuncW9UjWfCu8SKMOgyuqC_6xSzz0M2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دلیل جالب تغییر عملکرد سامان‌فلاح در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108544" target="_blank">📅 12:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa0bb0abc.mp4?token=N-QUfWtnOFeCSZ5mHXuvt0aaXynJDVsyvATgopPTF-rd3rH_NDPd0rNpFCbr1ygyDfnyZnEgKIk2VGFaXsKdckZNqr0KqYIRtacWqVaANJCS8AWp7F73lHnhlJgz3A-NWnxgB9iTvOjwHCP-KE1oz5FslnMTca7OrR5OvVcpKIiOKXy8k5rxGm1qB8b4LhBQXBe68vQkI4ScE0UzZZjZ0_A7h3nX8K11l5hfIFgaC-AelSe30DzdRN15Ko44EgU00NxGj5pQA4m6vBEYAoEKdZ-QLZA_KtYOxDKED7-HeBuwsBzRZD0BjKxNWs-tbXupHBXy3gHGKn7OM0yCe97AOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa0bb0abc.mp4?token=N-QUfWtnOFeCSZ5mHXuvt0aaXynJDVsyvATgopPTF-rd3rH_NDPd0rNpFCbr1ygyDfnyZnEgKIk2VGFaXsKdckZNqr0KqYIRtacWqVaANJCS8AWp7F73lHnhlJgz3A-NWnxgB9iTvOjwHCP-KE1oz5FslnMTca7OrR5OvVcpKIiOKXy8k5rxGm1qB8b4LhBQXBe68vQkI4ScE0UzZZjZ0_A7h3nX8K11l5hfIFgaC-AelSe30DzdRN15Ko44EgU00NxGj5pQA4m6vBEYAoEKdZ-QLZA_KtYOxDKED7-HeBuwsBzRZD0BjKxNWs-tbXupHBXy3gHGKn7OM0yCe97AOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
بانوی استقلالی پس از برتری مقابل الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108543" target="_blank">📅 11:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a065c7f48a.mp4?token=inaV2PqG2DuQI8l9i7JuDcn3q-ujNuaQsCPpypXeMkDDZCCNkUBy14wV63tIgHjiYENnbMqZbYHLtciAy3tboxbi8NQEIguA70Yr_cN5WcwS_IxFRuwQsnN4AMDBCENBqBQXwhZcYf8q9RwNJhCUNuynJQvixM3GaADU4M-BlrzmtRwx0vYrVmM5CCLlKmS43GXxu76niXjAvJ8dQ_B2932n8l7chkkwVC_lZAC-1AHp_nyTxM6kMcscbdAAcrjhy2FLiY_kOnCTpyRoA9ogNOGVSGhuKRG1kxGhwHmRwbGopuNTGVH7EKCRfI6lS4EDSHOEJ8CDuj4-bekT6e52sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a065c7f48a.mp4?token=inaV2PqG2DuQI8l9i7JuDcn3q-ujNuaQsCPpypXeMkDDZCCNkUBy14wV63tIgHjiYENnbMqZbYHLtciAy3tboxbi8NQEIguA70Yr_cN5WcwS_IxFRuwQsnN4AMDBCENBqBQXwhZcYf8q9RwNJhCUNuynJQvixM3GaADU4M-BlrzmtRwx0vYrVmM5CCLlKmS43GXxu76niXjAvJ8dQ_B2932n8l7chkkwVC_lZAC-1AHp_nyTxM6kMcscbdAAcrjhy2FLiY_kOnCTpyRoA9ogNOGVSGhuKRG1kxGhwHmRwbGopuNTGVH7EKCRfI6lS4EDSHOEJ8CDuj4-bekT6e52sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
واکنش‌جلال حسینی به درخواست بیرانوند برای رفتن به استقلال
: بازیکنانی که از پرسپولیس به استقلال می‌رن یا از استقلال به پرسپولیس میرن ممکنه بعد از پایان دوران فوتبالشون  خودشون یا خانواده شون با آسیب‌های جدی مواجه بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108542" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108541" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108541" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTzwonLnWYFiFdVRZXHlyphSUO43VGQMxBMoVzWU51BIr4SGl3evO0cOkSSO8FxDBK4N1pOCcyFQYV1n3myo0mYBocJvlBH3ciHClElLzHj1OXxA975LNCiQsSzMtlG7pu8efWgKe2_cO9etw2dyfvnX2HCevO7fmp21IPCkRSTrlNFJi8NA4aM0--yGIPouua-Fuy0Jxc2MnDSXahX02X8axsuzbtvlv3UETWx_PYW4ZyDLzknfS7KT-1nMbCWZEUs_ttGVt1dwR8RO19TUrzxh0kjCWromloX-JGn3UycAzTIw185BqLgf6cH0AP-n5QB7XqjZ2Muj5zOIrJ14YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108540" target="_blank">📅 11:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd558a4adb.mp4?token=QziYWThUdvXx_GqcTl12OWVux7xlR_cdRwk9CUX1Za-nM96GN0dHI_0vbgcn2KMVDzq3ljKW7NFHPNOLOr0tLAOmV840O1nHDf3a4QIKUAWwZJK4vkzEf9fOlY3jLKyaGGctAzh7eOhD_qr-hxISOinkDNEsXC1RID4EO_4c-QXWdbAkT-qdAyjFPjTHVZ3u1h8-SQ0aH-QOL53sy40gAyxORN6yK_VSypCKDXbQueSgEVmQ9uDAmd7Y9HMEUad7OnrOt8OBowgR_QvCIIJ3i5Z1h3tapWiYWgcDmWSXb5-P7UBJQBpGonVAEbcyhLa_75Y1Zwz46JTP4grIyE2ctA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd558a4adb.mp4?token=QziYWThUdvXx_GqcTl12OWVux7xlR_cdRwk9CUX1Za-nM96GN0dHI_0vbgcn2KMVDzq3ljKW7NFHPNOLOr0tLAOmV840O1nHDf3a4QIKUAWwZJK4vkzEf9fOlY3jLKyaGGctAzh7eOhD_qr-hxISOinkDNEsXC1RID4EO_4c-QXWdbAkT-qdAyjFPjTHVZ3u1h8-SQ0aH-QOL53sy40gAyxORN6yK_VSypCKDXbQueSgEVmQ9uDAmd7Y9HMEUad7OnrOt8OBowgR_QvCIIJ3i5Z1h3tapWiYWgcDmWSXb5-P7UBJQBpGonVAEbcyhLa_75Y1Zwz46JTP4grIyE2ctA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
حضور افشین‌پیروانی سرپرست محبوب سابق پرسپولیس در یکی از کنسرت‌های معین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108539" target="_blank">📅 11:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
کمیته استیناف رای خود درباره یاسر آسانی را صادر کرده و این بازیکن مشکلی از نظر آنها برای همراهی استقلال ندارد اما تا زمان اعلام نظر نهایی AFC قرار شده که رای استیناف به صورت رسمی اعلام نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108538" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26563f619.mp4?token=QpdBPxphcU2VdjapxjAg46CGL0bUIDYHjMj69c_ckwuzkdXVAs0guXK3uPxUVgqe8y2DCIwy-j89DwUHEzQHrgDyT7xqjx2iLIGY2xKdSYM_0ggDaxhRogktTLESajT7KhyfnpOMgIWjFyCR3c2bsQ9rcQVcA_KK8zZjEhTgbVYYI7nBMG_Z-OGWk1Hr6Xg-StklmUlwZExIqeCJdWhPUumlmT9Ae8sv-eZmasD6ony6qZYhafD1aNLgA4gN00UFgTmmVxwDrkepvHMtW-H8zwm7Th0ikoEbeR-c7joPZ6vy5gWgASxJZBL5Ymnay8bDR-AfBIf79dBqzdb2hI6zQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26563f619.mp4?token=QpdBPxphcU2VdjapxjAg46CGL0bUIDYHjMj69c_ckwuzkdXVAs0guXK3uPxUVgqe8y2DCIwy-j89DwUHEzQHrgDyT7xqjx2iLIGY2xKdSYM_0ggDaxhRogktTLESajT7KhyfnpOMgIWjFyCR3c2bsQ9rcQVcA_KK8zZjEhTgbVYYI7nBMG_Z-OGWk1Hr6Xg-StklmUlwZExIqeCJdWhPUumlmT9Ae8sv-eZmasD6ony6qZYhafD1aNLgA4gN00UFgTmmVxwDrkepvHMtW-H8zwm7Th0ikoEbeR-c7joPZ6vy5gWgASxJZBL5Ymnay8bDR-AfBIf79dBqzdb2hI6zQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
نظر عادل فردوسی‌پور درباره سوپرگل دیشب آسانی: واقعا با کجاش گل زد آسانی؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108537" target="_blank">📅 10:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd1a54114.mp4?token=eRLEmj0WGyQ1QkusLh2-PHBGE3s2qJPy3q4gORgAIWu54ESziAo8CI_p_EqcvI45hgkaoRWmTsLtO3oHSvNJDHfz0VXJdGxy9L8yVGGRNVu21voNOXA1Mg9HF-FKVuRHeGWggEFI3cl-tVoZvxSOZ7PGxQdeuoE9DTJtH3ubfPdFDBVRAVTg7UWL1W8yIwUSM471XhIrP-_bqICcBWSn7HDGHn30rNVAXOvdUMFkf9cG1-UuucLOktyfrja4E3KzXWBywKwgomwVjE_-OXsA9FptQa9YvwVPqpLRMa_j6jQXP5Fc5uYFkqUKm4KDt9ekj0flhFBQJYGpPCJO36mqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd1a54114.mp4?token=eRLEmj0WGyQ1QkusLh2-PHBGE3s2qJPy3q4gORgAIWu54ESziAo8CI_p_EqcvI45hgkaoRWmTsLtO3oHSvNJDHfz0VXJdGxy9L8yVGGRNVu21voNOXA1Mg9HF-FKVuRHeGWggEFI3cl-tVoZvxSOZ7PGxQdeuoE9DTJtH3ubfPdFDBVRAVTg7UWL1W8yIwUSM471XhIrP-_bqICcBWSn7HDGHn30rNVAXOvdUMFkf9cG1-UuucLOktyfrja4E3KzXWBywKwgomwVjE_-OXsA9FptQa9YvwVPqpLRMa_j6jQXP5Fc5uYFkqUKm4KDt9ekj0flhFBQJYGpPCJO36mqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سوپرگل دیشب آسانی با گزارش نوید استادرحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108536" target="_blank">📅 10:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ef2c6d44.mp4?token=TTyzH21Eq2vgZWyFSjvueZHY8kcagfS-MFV7-Of8R2ZxHxm0NZMwW5Mr8b3s_6gt1XHpOOnYD6-epsA__vGpJrwfWpDNXKLYAmJjhJN0G87YhtAu3GzfU4gmuG2ujIfQ2diHP7VS4b6SGlivhG4FQwltHU9uBAjjouMjMzMh2_fpxCN9_0_BvKOykDS0LcH7iDcywatfX68A153D04rVu8tEIjxHdyjUt_USdavwRd9kpV-w3mIaZo1aXoxB7KNculu_HH1DuvGqMOhwsT2JWjtwNE4S_ZPVfBzdyMKcWnmZeJnuM05GBiFWLMiDke2rFjit7VGqV3F3_p-ludDnkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ef2c6d44.mp4?token=TTyzH21Eq2vgZWyFSjvueZHY8kcagfS-MFV7-Of8R2ZxHxm0NZMwW5Mr8b3s_6gt1XHpOOnYD6-epsA__vGpJrwfWpDNXKLYAmJjhJN0G87YhtAu3GzfU4gmuG2ujIfQ2diHP7VS4b6SGlivhG4FQwltHU9uBAjjouMjMzMh2_fpxCN9_0_BvKOykDS0LcH7iDcywatfX68A153D04rVu8tEIjxHdyjUt_USdavwRd9kpV-w3mIaZo1aXoxB7KNculu_HH1DuvGqMOhwsT2JWjtwNE4S_ZPVfBzdyMKcWnmZeJnuM05GBiFWLMiDke2rFjit7VGqV3F3_p-ludDnkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
فلیک دیشب خطاب به خبرنگار: "امیدوارم بالاخره یه روزی یاد بگیرین که من وقتی مستقیماً با رئال مادرید بازی ندارم، به هیچ سوالی دربارشون جوابی نمیدم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108535" target="_blank">📅 09:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccc8c0b68.mp4?token=pSf4tAHJZao9Hr2w8S3QWziP00zVK_VjNiynFZMjEcB7tskDljHvQpkzCW8XRxRcR8hbFVPNPT15MVbnhzmkdG89NA7WnDDpEeSBXqgrI4ZCYXH_hQS0gDpVpXg3z724aN8zgi0OSMeC15QXQixiq9eNXFKy23WnS_GGu2HFQ8GORy9NE1MC4A0dOOQ1-aiyJeGV0VAtRfxyIIRDMCGEgf-0BNduQLPI24QX8uUt7zmLBRuE4LPTC_l7UseDpWr7ieEyGo0p-AbFp-Z-r4VgJ6M5XfnyjBJewt0LO7QM6eJ9uhDP8sYTAc8zTPvyJYeH5kE0U3qZ7eULzXPlSfwMfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccc8c0b68.mp4?token=pSf4tAHJZao9Hr2w8S3QWziP00zVK_VjNiynFZMjEcB7tskDljHvQpkzCW8XRxRcR8hbFVPNPT15MVbnhzmkdG89NA7WnDDpEeSBXqgrI4ZCYXH_hQS0gDpVpXg3z724aN8zgi0OSMeC15QXQixiq9eNXFKy23WnS_GGu2HFQ8GORy9NE1MC4A0dOOQ1-aiyJeGV0VAtRfxyIIRDMCGEgf-0BNduQLPI24QX8uUt7zmLBRuE4LPTC_l7UseDpWr7ieEyGo0p-AbFp-Z-r4VgJ6M5XfnyjBJewt0LO7QM6eJ9uhDP8sYTAc8zTPvyJYeH5kE0U3qZ7eULzXPlSfwMfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🔥
▶️
چهار سال پیش در چنین روزی، دیدار مس رفسنجان و پرسپولیس
- بازوبند مشکیه؟
+ تخمشو دارم داری؟ تخمشو داری بزار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108534" target="_blank">📅 09:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfecaa3ae8.mp4?token=Sje8-KJQhfECHQc4jUI1SbTiyDYuoKH57ATOH8OYjVdMyTUayCBv6oC4QDUHPps50OlQWcRrwg2TPDchrhEYyBncqG5aP-Ck1u_aXENW805MdsgSWkJ1K4ZK6fLCWuoMpJx5ue-MBS7yfF3nhZQ-HehHI7QcbcQ1uBq8aycu2o--kZOcy54vHmLNq37q0PyBvosLWelsGkmngjaW8d3DOqgaZ6zXJQOKyBFKvPmCEBNEnL1I8SlERFMwOvQiuv8Mu8Cg6AoAU-e4rpNMinLiD0kBche_RfAaCpG0GevlHzFl9o4Mf5P5iDZq3-2rQApHiTnFeNPxp0og-FZ_fYH9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfecaa3ae8.mp4?token=Sje8-KJQhfECHQc4jUI1SbTiyDYuoKH57ATOH8OYjVdMyTUayCBv6oC4QDUHPps50OlQWcRrwg2TPDchrhEYyBncqG5aP-Ck1u_aXENW805MdsgSWkJ1K4ZK6fLCWuoMpJx5ue-MBS7yfF3nhZQ-HehHI7QcbcQ1uBq8aycu2o--kZOcy54vHmLNq37q0PyBvosLWelsGkmngjaW8d3DOqgaZ6zXJQOKyBFKvPmCEBNEnL1I8SlERFMwOvQiuv8Mu8Cg6AoAU-e4rpNMinLiD0kBche_RfAaCpG0GevlHzFl9o4Mf5P5iDZq3-2rQApHiTnFeNPxp0og-FZ_fYH9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کنایه داریوش شجاعیان به مصاحبه اخیر میرسلیم: ولی تیبا هم ماشین بدی نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108533" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد. بیرانوند باید شرایط قانونی سربازی را انجام دهد. او تمرکز لازم را در این چند وقت نداشته است. حتی بازی با ازبکستان او را کنار کشیدم و آلن مربی گلرها گفت بیرانوند تمرکز ندارد و بازی نکند. من چون می خواستم بیرانوند را برای جام ملت ها حفظ کنم او ار کنار نگذاشتم. خبر ندارم شرایط او برای سربازی چطور است اما اگر برود باید برای او برنامه ویژه بگذاریم. من در مورد پرونده قبلی او هم هیچ توصیه ای به کمیته ها نکردم و هر چیزی که قانون است برای همه باید اجرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108532" target="_blank">📅 09:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0cb95d7.mp4?token=F6yI6hiV5o4fk2WED56_TU9l55hBKKga2etbeJFhlYH8QehZXFe-wkULKtJ-ocgjSA5kLNuZ_ei1KhOkoIKeldM3PattFQmaP7ICZMvqiHGg4aet1T_8WnVQEu1AxEE4wPmCIW95ZH8lwjArZ7y9qf6DnItbJE2JaR1XSohIWM2NE2oP9xJAlHCjH0J8e7-9bUHZUoPNtWKDz4bdBS6AYJ2J7DyP2XFyKfblHmK7ZGenfAJVyytoefqPI5U3nIl6kyVMtjGFBeYqM-HhtyLQ3EcS9AlQnkFg0JbLpF4wdg0kg2PNhTK-QjyVCOj7wureTnIOLjcRoZH7W53UpO_2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0cb95d7.mp4?token=F6yI6hiV5o4fk2WED56_TU9l55hBKKga2etbeJFhlYH8QehZXFe-wkULKtJ-ocgjSA5kLNuZ_ei1KhOkoIKeldM3PattFQmaP7ICZMvqiHGg4aet1T_8WnVQEu1AxEE4wPmCIW95ZH8lwjArZ7y9qf6DnItbJE2JaR1XSohIWM2NE2oP9xJAlHCjH0J8e7-9bUHZUoPNtWKDz4bdBS6AYJ2J7DyP2XFyKfblHmK7ZGenfAJVyytoefqPI5U3nIl6kyVMtjGFBeYqM-HhtyLQ3EcS9AlQnkFg0JbLpF4wdg0kg2PNhTK-QjyVCOj7wureTnIOLjcRoZH7W53UpO_2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دیدنی فرمین‌لوپز در تمرین دیشب بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108531" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=vivs1gWnNNw2f2DPw8qVnqngBqa9WUuQj7uKDIvApHQdoSJkt33BRtz27BkNwsMAxzzaJVCw5wBByN-l74DmOdMza710KumS3b8Jv0pReYwf7VZIIQZ6_b8fdsOrhn-79Tpxz1Cu6AXzz919fxpQS34TSxCpUkdCP8GQ16fucDou2HLZkNCgu9kyRUwgxQX8l6v75s9YG9nWihR9RBzQXXfuqqEAULYJ3EF833z3fikLCUQ5WEoEIsYOML6ZWIcQSIk-nVgYteGnQ9d9mpvE9WoFgoRBZBAw91k2xkXXKNKXGYdhnfwhDB64GB95R9W7wtMENRY1kwhmT6Ldlcxx6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=vivs1gWnNNw2f2DPw8qVnqngBqa9WUuQj7uKDIvApHQdoSJkt33BRtz27BkNwsMAxzzaJVCw5wBByN-l74DmOdMza710KumS3b8Jv0pReYwf7VZIIQZ6_b8fdsOrhn-79Tpxz1Cu6AXzz919fxpQS34TSxCpUkdCP8GQ16fucDou2HLZkNCgu9kyRUwgxQX8l6v75s9YG9nWihR9RBzQXXfuqqEAULYJ3EF833z3fikLCUQ5WEoEIsYOML6ZWIcQSIk-nVgYteGnQ9d9mpvE9WoFgoRBZBAw91k2xkXXKNKXGYdhnfwhDB64GB95R9W7wtMENRY1kwhmT6Ldlcxx6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
امیر قلعه نویی و پاسخ در مورد دلیل عدم دعوت از مهدی قائدی:
🔺
استقلال که از الاتحاد کلبا وقتی قهرمان شد بالاتر است اما چرا آن موقع آقای کی روش و بعد ویلموتس او را دعوت نمی کردند؟ ما یک اصول و چارچوبی داریم که قطعا در دعوت و عدم دعوت موثر است اما موضوع ما فنی است. ما دقایق همه بازیکنان را با آنالیز در می آوریم. آیا مهدی قائدی الان شرایط خوبی دارد؟ آیا بازیکن فیکس النصر است؟ مهدی قائدی در آمریکا یکی دو بار مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108530" target="_blank">📅 08:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fdcb8a6f2.mp4?token=FlpNkk6rKkRKd3Po2-oksxZVlbicxfCuJ7VCqM_TaaTJtqoQGF0sOHegCiIpp_GJAgCWtKVgXbeSy7Ms_fDadwfTaRbN1r8t6pWSV4ioOMIIJg0zYZZSCwWg29SNlcw5PTThn9Z8tZgFTeooXl8I_Equ5xdLuiYpkqLrTHXsT43ufs-8op-aiqK2dv51At83ymRCQwaktN4KQYJDRM3X_dIYSNYiEw86biE1myUoUlN0--jKR2RxcGhmRi6zrfSPdYkAvOkCeDW5baUfQcVwvabV5rG5jUXQVRPOpbZCHp8WYOn-L3sibVH3-LgGUDAuOI-bAxB__QhR9gT18_2Y7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fdcb8a6f2.mp4?token=FlpNkk6rKkRKd3Po2-oksxZVlbicxfCuJ7VCqM_TaaTJtqoQGF0sOHegCiIpp_GJAgCWtKVgXbeSy7Ms_fDadwfTaRbN1r8t6pWSV4ioOMIIJg0zYZZSCwWg29SNlcw5PTThn9Z8tZgFTeooXl8I_Equ5xdLuiYpkqLrTHXsT43ufs-8op-aiqK2dv51At83ymRCQwaktN4KQYJDRM3X_dIYSNYiEw86biE1myUoUlN0--jKR2RxcGhmRi6zrfSPdYkAvOkCeDW5baUfQcVwvabV5rG5jUXQVRPOpbZCHp8WYOn-L3sibVH3-LgGUDAuOI-bAxB__QhR9gT18_2Y7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
پست جدید AFC برای یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108529" target="_blank">📅 08:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=fnWCB8wiZDZCqoqEK86Ro3niPluyUstPPY4Iw-ieaxhvq6SllvzL7FkEbCpICaet_sehdl07nT0CCAU9QNyyHYl71EEiZKqsM0jPwLQk47MQeaXkcNjc_Dykolzxlsvw6biJv15F7ttvidM3352LjTNZVMaZhSmMYWuXglmxc-FIxEXHsPgtWsJJcVMZfmt_h16BULfvwGAos_YVanEPvNusG6TAr3S8zIsJ4Mcxfz0EH7IQQ2_jwmAOwG1VRGN3Dmlfbyj7NKorPOHXhjtL4b8K_F2_w70vttVm9NpolrhOnIoV3WLZ_UjR8VPtund0QiuLctQXPwWVY8S1jd-tWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c408292b8.mp4?token=fnWCB8wiZDZCqoqEK86Ro3niPluyUstPPY4Iw-ieaxhvq6SllvzL7FkEbCpICaet_sehdl07nT0CCAU9QNyyHYl71EEiZKqsM0jPwLQk47MQeaXkcNjc_Dykolzxlsvw6biJv15F7ttvidM3352LjTNZVMaZhSmMYWuXglmxc-FIxEXHsPgtWsJJcVMZfmt_h16BULfvwGAos_YVanEPvNusG6TAr3S8zIsJ4Mcxfz0EH7IQQ2_jwmAOwG1VRGN3Dmlfbyj7NKorPOHXhjtL4b8K_F2_w70vttVm9NpolrhOnIoV3WLZ_UjR8VPtund0QiuLctQXPwWVY8S1jd-tWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
میثاقی به نقل از حسن زاده رئیس کمیته انضباطی: فسخی برای یاسر آسانی از نظر ما ثبت نشده است و او هیچ مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108525" target="_blank">📅 01:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=fuGslbH0MFdLTAsqBVJe_K5RrvN4nWOJ6qwNlAM4p0vGF2lyhQ96EMIgqhvsHnVrtSVkYKNi7itBWOGcgk00JX6vmbe7aW6LFyVS_753PALoK5VOCG_hFFzWQ3rwPab5VL7nsyTYLlaIA2xlCnZTz5HSO3vUtX4qDOECc-IoPEKkG09jIqxrqPY7HhbEcyet8rCwb36blR3FxeAUbCXU0VJ53E9ej6NWMV949hE6IOw7X5g1KjAKKkJ_KT5ov_bsv4KCX7ujNz4JUEyci3N7haSUfXm5e9nTUpXHJcxQTOncKZZkcdE96rkDOCy1psa1oTGNsG965J-whJk5wd1f5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fda9a24a.mp4?token=fuGslbH0MFdLTAsqBVJe_K5RrvN4nWOJ6qwNlAM4p0vGF2lyhQ96EMIgqhvsHnVrtSVkYKNi7itBWOGcgk00JX6vmbe7aW6LFyVS_753PALoK5VOCG_hFFzWQ3rwPab5VL7nsyTYLlaIA2xlCnZTz5HSO3vUtX4qDOECc-IoPEKkG09jIqxrqPY7HhbEcyet8rCwb36blR3FxeAUbCXU0VJ53E9ej6NWMV949hE6IOw7X5g1KjAKKkJ_KT5ov_bsv4KCX7ujNz4JUEyci3N7haSUfXm5e9nTUpXHJcxQTOncKZZkcdE96rkDOCy1psa1oTGNsG965J-whJk5wd1f5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
برای درک بهتر سوپرگل امشب آسانی فقط کافیه از این نمای دیدنی تماشاگران ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/108524" target="_blank">📅 01:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1Ky9GdLP-Mbt-ue1xgWTEvrHCC-pkwTmOQSpvRhe1ZP9RyOb7UN_ThRmBmgNAgE2zLGNnLmDVcx7hbh8h-BZyeuVfsNRXBJ0FCwQ70m0g6spJT_1zsFZLndgLsuYF5gfW31mEfBof_ogDX4lES_oegAgo7SYbWXDUCSH7rZpUoHqP10krhvzLG_N9qo4TbhXmcEKjmPknaXrYgneZc7chgzoV79HUzSD78FusA-jgIRH3v_TWE2z7uZH4KAd1YtG67KX9-AKOj0z6dTMfJCDlAN1XvoHtQYsKHQXUoHn81e2FMxtQymXfUBwp5B4O1IRJb0pEWX602ILmymFzk3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108523" target="_blank">📅 01:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=HX5D-_mhPorlf-aJwR9bXe4YMcA8TlD6IUvXDWNaSwzsFQiGFZ5LXPCsfT2jN5kNtlnu1l7zQBew8wq-zIbVaDuQaLLtoK6dHUJZiL_UawHzWg09_cj2gC-nmQKl-F7OJw2ysnz5Sq9dvOz2mdeKU0u2cHKgnG7cuzozEoMwwopzYwvrnu4qhADLVQz3p-39rUTTjUxPMflVsERuOcXFLXvTkVIAZPILr64MBAXNbRFSyq4Qd4nIaDowbtzFndImrthpKy5QAbyOZR6KSS2-2kxddnXIf3_kF3AlJdqSZzyAYni7UyxZwUXUTu5A2JFPSfuerhQJx4EHbsrAZps56xailN0IzqtlTKCjz0w75dk3RcRXWhVGVkQryVx6oyzzo2zEjqn9mjmJoZzhAKfcRwYLXDaylHtxwslHt3KRWs_ZaF2K-07YLRvwRraEd8KFapNqBBsN8ks51hEYU5ZYhy7TMAOBYrUN83MZ6_ngRvhxVYnVx0C2jRl6dFeuMuTKS1sfS9AVRi96m3RTbw_Z4E6cCRZ-nip7f_DmenYIREFtIq8Y98T1m7xakCm06U7ot9w0jaS8pn-4bePr7qrvgx0MBm08eq_O4x91WOlHJukueiJbGXJ3IBdYS3azJOeC5RgHV9kEIyv1PFH58cMlKjAXisfsfGliw5d6wT3TK9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f09ab8993.mp4?token=HX5D-_mhPorlf-aJwR9bXe4YMcA8TlD6IUvXDWNaSwzsFQiGFZ5LXPCsfT2jN5kNtlnu1l7zQBew8wq-zIbVaDuQaLLtoK6dHUJZiL_UawHzWg09_cj2gC-nmQKl-F7OJw2ysnz5Sq9dvOz2mdeKU0u2cHKgnG7cuzozEoMwwopzYwvrnu4qhADLVQz3p-39rUTTjUxPMflVsERuOcXFLXvTkVIAZPILr64MBAXNbRFSyq4Qd4nIaDowbtzFndImrthpKy5QAbyOZR6KSS2-2kxddnXIf3_kF3AlJdqSZzyAYni7UyxZwUXUTu5A2JFPSfuerhQJx4EHbsrAZps56xailN0IzqtlTKCjz0w75dk3RcRXWhVGVkQryVx6oyzzo2zEjqn9mjmJoZzhAKfcRwYLXDaylHtxwslHt3KRWs_ZaF2K-07YLRvwRraEd8KFapNqBBsN8ks51hEYU5ZYhy7TMAOBYrUN83MZ6_ngRvhxVYnVx0C2jRl6dFeuMuTKS1sfS9AVRi96m3RTbw_Z4E6cCRZ-nip7f_DmenYIREFtIq8Y98T1m7xakCm06U7ot9w0jaS8pn-4bePr7qrvgx0MBm08eq_O4x91WOlHJukueiJbGXJ3IBdYS3azJOeC5RgHV9kEIyv1PFH58cMlKjAXisfsfGliw5d6wT3TK9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
آیتم جالب عادل فردوسی‌پور از کلید واژه مصاحبه‌های بیرانوند: درصد، دلار، ماشین، میلیارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108522" target="_blank">📅 01:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601362fff.mp4?token=la6vbKwwx-4OywaEvJPWNbFNEcFIElLI1QE55KwBHZFaa6wrXseuS7J6RZIqjrgEX1vu98KGec5X9Fsgi5cdbMyuj-2LbQ6mB9JdxA73TsZ-3WiMZXAWAaKNWUABi7xlNqIQ3-awyCGZGl_bSJGxvlFoHAAT8IgZU6LUrppJwfnGWURhPTC4o5B1Byi7JBPcTMjeWWRoSXvjJnzKe7V9oyPZVDwB6DcyZTKWE8zdrECpKZKq57a7Xuv3QSYZk9NMz-aaLMvo9-8cwNfagLtXqAo1JW36hFPk-OL399zpwPrO57CcUVR-ss6XvSTv2Xh2o85YteZlJTIHZ0k4Mj7R4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601362fff.mp4?token=la6vbKwwx-4OywaEvJPWNbFNEcFIElLI1QE55KwBHZFaa6wrXseuS7J6RZIqjrgEX1vu98KGec5X9Fsgi5cdbMyuj-2LbQ6mB9JdxA73TsZ-3WiMZXAWAaKNWUABi7xlNqIQ3-awyCGZGl_bSJGxvlFoHAAT8IgZU6LUrppJwfnGWURhPTC4o5B1Byi7JBPcTMjeWWRoSXvjJnzKe7V9oyPZVDwB6DcyZTKWE8zdrECpKZKq57a7Xuv3QSYZk9NMz-aaLMvo9-8cwNfagLtXqAo1JW36hFPk-OL399zpwPrO57CcUVR-ss6XvSTv2Xh2o85YteZlJTIHZ0k4Mj7R4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد سخنگوی هیئت‌مدیره تراکتور نسبت به شرایط سفر به عمان؛ مگر کور بودند که نفهمند تراکتور و گل‌گهر هم مثل استقلال بازی دارند؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108521" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله سخنگوی تراکتور به بیرانوند: برای مسی هم تیم را به هم نمیریزیم. بیرانوند که عددی نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108520" target="_blank">📅 01:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=dHHeTxn1RyV3p-vSM52_I_rwUsRIKOZv_RsFz-oEkgA3vOjlq6CFt5KYzFswlPTU7jj_1cYdsPKBT3DozIJ0jW_gGSy_ca-ui0nS7kutHOId4pPiTeHgzX7aA3leH2Ad19rX5Ay-Y0znE3atK9YgxsbfYJspql-93BI4Et24y-E0ZYHdbriqt1WYhhIu4W4gnbbCPvbgaA4mYFRQubxd9AdwZpPXqfO66Bb_s1GHfFIePjoj50Ob3POJwMwbD_gX1Ec25sEkLy3TrkrVI_fCZoCZjodbVUY63YK_410QQGpgqM1zqXJ3JbUs1qiiXT-y0d0Zu7XfkkmmQhw0izte2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab8a7b19b.mp4?token=dHHeTxn1RyV3p-vSM52_I_rwUsRIKOZv_RsFz-oEkgA3vOjlq6CFt5KYzFswlPTU7jj_1cYdsPKBT3DozIJ0jW_gGSy_ca-ui0nS7kutHOId4pPiTeHgzX7aA3leH2Ad19rX5Ay-Y0znE3atK9YgxsbfYJspql-93BI4Et24y-E0ZYHdbriqt1WYhhIu4W4gnbbCPvbgaA4mYFRQubxd9AdwZpPXqfO66Bb_s1GHfFIePjoj50Ob3POJwMwbD_gX1Ec25sEkLy3TrkrVI_fCZoCZjodbVUY63YK_410QQGpgqM1zqXJ3JbUs1qiiXT-y0d0Zu7XfkkmmQhw0izte2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🙂
شاعری هوادار استقلال برای برد شیرین آبی‌ها در آسیا مقابل الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108519" target="_blank">📅 01:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=WWWs0n7gkWaQTishVumYhsDyDz-_rkEt-ZehnuWjIgUpSVhStxsGRPFOekzNDzs7g1CaKO8blOKaPsszzPg0s6KXrsOLEGEuz-9AfZ_nx8SX1rBy_gP4n_GvVoR0iNm5NAAEg3F3f1wOBi-apRIoGSNFOnidDX4rWpHVl0bSpCjiAVHA1DiJy1NYofpSs-T_vb9a_---r8vDJdR_CCR4VnwOhrV8N4K6QDtwVt6CW89eielZBLMyLGRmD7Ulrh86XDftnRGIgjEb6NJlwIWjLCcmIp7eC7aX4ck-KRpw9nJJX_icvbVE2fQuy4AL9rYiKxpt8CPeonyWGEm8hEM77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a267abb0d.mp4?token=WWWs0n7gkWaQTishVumYhsDyDz-_rkEt-ZehnuWjIgUpSVhStxsGRPFOekzNDzs7g1CaKO8blOKaPsszzPg0s6KXrsOLEGEuz-9AfZ_nx8SX1rBy_gP4n_GvVoR0iNm5NAAEg3F3f1wOBi-apRIoGSNFOnidDX4rWpHVl0bSpCjiAVHA1DiJy1NYofpSs-T_vb9a_---r8vDJdR_CCR4VnwOhrV8N4K6QDtwVt6CW89eielZBLMyLGRmD7Ulrh86XDftnRGIgjEb6NJlwIWjLCcmIp7eC7aX4ck-KRpw9nJJX_icvbVE2fQuy4AL9rYiKxpt8CPeonyWGEm8hEM77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری هواداران استقلال برای پرسپولیسی‌ها: بروند برای خیبر و سایپا کامنت بگذارند، اینجا آسیاست و جای شما نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/108518" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBudDHe0ZF8O4lF8QBG3egeyf6NF-PZxUoCOBcx9mv9CaqjPf4Fv_-QwtZxv2PpWX8TlP2cQ91QB-xvjIjZ6RziU9SK1r6CwlNDT6b7YYozs2cjn2UcwJBVVsyuwy4K6641zDBmBlj6b_s81YJihQwn9bqQYz-0_oZpjtyk0SXCEzypqAJPbY0iQFVkNofycfPe1FdZX6xdEjeSyw0QJmqo-OeY9rVCjKxgMKSixwSf0WBTbVqpH1j5nsqtdBHZVKupRSeAp-5a47WbzTupC9wrI7MOWi3EqJUfhozK4v_ckrLtiYvHjwsKwnPGkKh4I8vo18S__SwuFtHLcegoN_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🇶🇦
استقلال تحت هدایت سهراب بختیاری‌زاده، برد مقابل سه تیم مطرح قطری.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108517" target="_blank">📅 00:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=C59ohi5edVgdBLKmnkdTodqfYvP9mLZqpYYC8fT5BWfOhTSz981AE4o-xHxYWyBf6AcGobDlOEud08L-R7PhZOdG3t5c4FxKKSGeH25SoNRX4gkzM7ScsGvHZBMJFzKsggmjwWfXcYVGfjU9ehRGgQKl2EOzMbE1WYQ0Pr5o_RMnK4MKgS88biIbBEbHcMjuNJ9gCV6BK0YGg91y8D_puLaX0o1AEGG_kQbMyUysCIVwoFnyyszrSxy2M9GVCEvzjq8zSaxKZbBCuPj35YN-G0FiVJ1csdiYeDYAh_FFCmVqOXk8q_SBDYHIhu16d01gbISHPFmJ951OikBxWyfXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217c826d5b.mp4?token=C59ohi5edVgdBLKmnkdTodqfYvP9mLZqpYYC8fT5BWfOhTSz981AE4o-xHxYWyBf6AcGobDlOEud08L-R7PhZOdG3t5c4FxKKSGeH25SoNRX4gkzM7ScsGvHZBMJFzKsggmjwWfXcYVGfjU9ehRGgQKl2EOzMbE1WYQ0Pr5o_RMnK4MKgS88biIbBEbHcMjuNJ9gCV6BK0YGg91y8D_puLaX0o1AEGG_kQbMyUysCIVwoFnyyszrSxy2M9GVCEvzjq8zSaxKZbBCuPj35YN-G0FiVJ1csdiYeDYAh_FFCmVqOXk8q_SBDYHIhu16d01gbISHPFmJ951OikBxWyfXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
⚽️
میثاقی: توافق اولیه یحیی گل محمدی و فدراسیون فوتبال برای تیم ملی امید صورت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108516" target="_blank">📅 00:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMTAkVdc85qnVotZeFx3hd1gTRrk1vtlTcv5v9v7CyGpeRQAVgG0p7gO4UhkSaxAajEq3j74jsEBsc8VgyitUOk3NImAyOM3g1rSWfpwbUfDuTBblE0HO_cSRS0yjMUtgMaHUH_jCTmVr6UMGpJQysNs7F91dxmuKRXjp3EbSB2S15qrmDvsOEmiFd42GJg8yf5UjsYwKC-PZVoOx0vOfCfdouPSjVl-tdgJoczEwpjeGnqgJNcxXicCt5zNqreBdVn7QGbpFZfUYU6w32ZDQ3jiFtZGL-u2KdV6VV5bwg--aUjoIBJwBa92zjmRInIYra71HFcNzXha9HrVooDrKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
🇮🇷
استوری کنایه‌آمیز سامان‌فلاح مدافع استقلال به مهدی تیکدری مدافع پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/108515" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=eMxA4XNfRTBGptjmi-pFm09IVFybuAlrwkBOXCJL2t2wm_rZ6liUs4N69IZ7KH8aa9Ap39BUCg02PRpokh7pRn50RF7FnNDAlxYf-N7DJ0IU7D8CSJReEA1sD1TkP-hr333j_Nw_21xsTrstbmUcpg4BW3m7zbTY3G5znM7LmnPKgTmpQapampVpPqF_jQ-qddapwIZr_HkduNvnC2yQDuX6Qw3Gikiw_kZQIC8KpaVHvjeNyqEJYCmb_UF7BZMzmdETVIvNwrTZ1LOKGRD2uGlM0kfW5XbyUHC5ZdvwRLHvC1Ae-_-DiQp7YIHqUAjV3cCJ-vjX5yvIh8n4bgR3oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648dfd6944.mp4?token=eMxA4XNfRTBGptjmi-pFm09IVFybuAlrwkBOXCJL2t2wm_rZ6liUs4N69IZ7KH8aa9Ap39BUCg02PRpokh7pRn50RF7FnNDAlxYf-N7DJ0IU7D8CSJReEA1sD1TkP-hr333j_Nw_21xsTrstbmUcpg4BW3m7zbTY3G5znM7LmnPKgTmpQapampVpPqF_jQ-qddapwIZr_HkduNvnC2yQDuX6Qw3Gikiw_kZQIC8KpaVHvjeNyqEJYCmb_UF7BZMzmdETVIvNwrTZ1LOKGRD2uGlM0kfW5XbyUHC5ZdvwRLHvC1Ae-_-DiQp7YIHqUAjV3cCJ-vjX5yvIh8n4bgR3oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
واکنش تند و کنایه آمیز میثاقی به تفاوت میان سفر تراکتور و استقلال و گل‌گهر برای بازی در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/108514" target="_blank">📅 00:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
پژمان‌ماندگاری مدیر رسانه‌ای استقلال: مصدومیت یاسر‌آسانی جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/108513" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx3cF4LXeWf0ICC27knYeXCljwLazKvbnkX36G7hFh1K4NRkxnNv6GZ98L2d61n4HXzCv6-2Cwr-z7UBZifkNHw-JrzDCTaYyDOcUKEJW924yj3rD7LMNmv3O1U9BLvnOb5AlG7-Nqq1OiSweQ8OVM9c8wFHKmwlp0krEU9XFUs9c_pgJ2gr7lTzLtIxocu-l6OlFgThvrC9fTaetdlKSZc4VjR0U7k1pfI69aM9BAXsncE3fJr0xEfh7bBD1ySR2KdNIJufT9xO81Kv9YWR3Fst6F7HUenp34Qy05RJ1gYC7_xf-gHHmJHrOIWdVpdo1p5AOj5Qlz3FdekyndSRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توییت کنایه‌آمیز استقلال به پرسپولیس پس از بازی: یاسر‌آسانی به شدت قانونی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/108512" target="_blank">📅 00:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
❤️
زنوزی مالک باشگاه تراکتور: همیشه گفته‌ام عدالت اصلا رعایت نمی شود/ یک تیم با پرواز وی آی پی دولت سفر می کند یک تیم مصیبت می کشد
🔴
نمی دانیم از چه کسی گلایه کنیم/ آنهایی که می گفتند پزشکیان حامی تراکتور است حالا بیایند جواب بدهند
🔴
حداقل اگر می خواستید یک تیم را با پرواز دولتی بفرستید به ما هم خبر می دادید
🔴
بیرانوند جوانی کرده است و رفتارش را می گذاریم روی جوانی اش
🔴
امروز شنیده ام که تیم های دیگر نمی توانند در عربستان هم بازی کنند این را من شنیده ام
🔴
باید برویم به AFC نامه بزنیم  و مشکلات پروازی خودمان را اعلام کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/108511" target="_blank">📅 00:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔥
🇮🇷
گل‌یاسر‌آسانی با گزارش عربی الکاس قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/108510" target="_blank">📅 23:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYxVdE17fKnT7rEPyof96VhOGAdSdYV3NIOwBq6C0muu2cCRPXSpP_RdGumF2PSY3lzXBrAJJQOxhJKj_Yhnca9SNTkZegwyHlq076nMPhRgT0QIxo4KmzW3rUCUXnVKEACFFB3zIFxu-Xe5QRmDVgLvr1YjaHc3QGzesSBMEFLLAJJ4RurxgwhQm-CtGQlhuQ5UYxfTYjPxnmg2lahQYR_yw5RK-mlGZebGVw__oqzComa3gpQpOvws1XfK9I7nerm5jTx5q1TAlFNpPKAVXP_Dr0uTvTY1X77EiZ2Tb4NvFX9yLmvk1FFuECfmNS12dEqpRGexvDRWuSZsF8fSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/108509" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=am7xKKChuaBJcbWZB44HUEaiKRaqkNgL-Qsywxia-41uIu5fzl1-YLP4iA3vY7hPvXTUAk-tEpWMX2CqPyP81-f3fWFFyscCVRnd4wRDhkugTFNK1trFg__npmxGsJ6FqjP0RHv9kF1z1anHvO2NLl3mdH7j1rGaaYujF_G2a5rlIJV9Z21Iy1ShrKPYZUNoUY1Lz1k0p5j4Px00GzU8befWHo0aSwwEsU3QW3Xfl4zq6ozQ3gFBa5Fz89QMHx50Hmxihf_DWHucJBE9KuVyWptkcqGXwd8kbFBv_0PGbAthTMJ5HstUmCVb3h7G83-CLO7NJK1VKfYY_Ts0_7sjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40f9d30d1.mp4?token=am7xKKChuaBJcbWZB44HUEaiKRaqkNgL-Qsywxia-41uIu5fzl1-YLP4iA3vY7hPvXTUAk-tEpWMX2CqPyP81-f3fWFFyscCVRnd4wRDhkugTFNK1trFg__npmxGsJ6FqjP0RHv9kF1z1anHvO2NLl3mdH7j1rGaaYujF_G2a5rlIJV9Z21Iy1ShrKPYZUNoUY1Lz1k0p5j4Px00GzU8befWHo0aSwwEsU3QW3Xfl4zq6ozQ3gFBa5Fz89QMHx50Hmxihf_DWHucJBE9KuVyWptkcqGXwd8kbFBv_0PGbAthTMJ5HstUmCVb3h7G83-CLO7NJK1VKfYY_Ts0_7sjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صالح‌حردانی امشب شانس آورد فوش نخورد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/108508" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خوشحالی اعضای استقلال پس از سوت پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108507" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frutUVdGEFU8ox_UMngj1YOAIErTr05S-0SXeb9Rp9htwZX0pPnoWkwNYXFTKAx9t-C9ZkPXcYVU65qfuswHzJ73kjlx9-xeb0XpxTK7sbEQXMyxGFqyOpC4tnWM9GDv63oPKSQk7CvfPqtx4tnhK1mi0Yl7zqm92V_nSwAcZWenFltW3APpQxOE2TJEiTB9vI_i5-71p7HCYmpBDVIHrzA8fS3dcUGP12TYfSsis66iM8TJ4oLnIhg8XdJpk1ByG_ZHG07AlZq1W4_kmu49FuBXsyQcwbnJWlhx7og0Dkug_R4EUiQkmD0OhbIjDiOuKaX5UK-NW5lVl2XqP9b-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌نخبگان آسیا؛ دومین تیم قطری هم مقابل استقلال زانو زد؛ یاسر‌آسانی با عمل به وعده خود تیمش را با وجود مصدومیت به برتری رساند؛ فرعباسی بازهم درخشید
🇮🇷
استقلال
😀
-
😃
الغرافه
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108506" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هنوز تموم نشده</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108505" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب دیگه بخیر گذشت</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108504" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">از کون آورد استقلال این دقایق
😐</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108503" target="_blank">📅 23:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بازممممم شانس آورد استقلال</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108502" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حردانی کسمغز
😐
😂</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108501" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حردانی ریده</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108500" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آشورماتوف نجات داد
😐
😐</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108499" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108498" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108497">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108497" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الغرافه زور گل زدن نداره فقط ریدمان بازیکنان استقلال میتونه این امر رو محقق کنه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108496" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسلامی هم ریده</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108495" target="_blank">📅 23:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرعباسی بازمممم گرفتتتتت</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108494" target="_blank">📅 23:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۷ دقیقه وقت اضافه
😐
😳
🚨</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108493" target="_blank">📅 23:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEbIczF2rmDQGv5BOoHwt9ZK6leemJ_WRLVjERpzz5cv4pWPImadlU_FDB7z7Xk6SfcY8cvIcHc1DUmcRXGOzfCAGY3-tdQT3LuWasJ7U1zDbU0QkK5SL8T0nKGtwRmr6l8TqB3dldIKFna2uuduOiyj7z306lKUBBhqPBYsO2KWboVYipiuQ45lFBYXdPyjADJhl1qpJIPC1kLucw3uUY5WDJZOeIVIiwaxkVJZNFB4zUu9hSpPLNVqeM5QzNiVw8XenJSq7SXdeCxhEUFtsUNnZZK5d41gRiEgXdLIigCpVmKUYNWm75vUh7E0w2QXc2XcUNMpB4vth2XZfaYFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العین امارات چهار بر یک مقابل نماینده عراق برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108492" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24051a9445.mp4?token=Mj-SmWvyhd28hliwTsyY2bL0nDMV_pbnOJJrqdKZl05_lp2T11XoHHldVFv8gIG5cJ6lpdN35lA4DHyzuQzZ5mqFM44LawhhDEtAjzL7w30Dia59mPOekVWKw09DdHJXqTtWTqbcqthWQtS5kZfVW-4wnD2CD4nWjPi59939Qh30EOkIB9tIuwIS3dyfEny41XI13bZ6RwrQs8H1KeYZP58wz1qoT37rFdfKqZV_6axzk1WpNZjdTTeBBwj_DJRxPuLy7r-MQlmKUyOcAiO-xXiDTxHTtzRDNPZsbu2CX_sdoMUUDxFS6hJJ-HqIbxB9a2J0rOC6TCi-F4WvCXN9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24051a9445.mp4?token=Mj-SmWvyhd28hliwTsyY2bL0nDMV_pbnOJJrqdKZl05_lp2T11XoHHldVFv8gIG5cJ6lpdN35lA4DHyzuQzZ5mqFM44LawhhDEtAjzL7w30Dia59mPOekVWKw09DdHJXqTtWTqbcqthWQtS5kZfVW-4wnD2CD4nWjPi59939Qh30EOkIB9tIuwIS3dyfEny41XI13bZ6RwrQs8H1KeYZP58wz1qoT37rFdfKqZV_6axzk1WpNZjdTTeBBwj_DJRxPuLy7r-MQlmKUyOcAiO-xXiDTxHTtzRDNPZsbu2CX_sdoMUUDxFS6hJJ-HqIbxB9a2J0rOC6TCi-F4WvCXN9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپر سیو فرعباسی روی موقعیت تک به تک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108491" target="_blank">📅 23:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سوپر سیووووو حبیب فرعباسی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108490" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=jCq9C0e8HlEqhaWH07qrUBv-qhGNaoWn7tR7Lzy3apOpA_5ky24fzickns8ITLctbkCC1iEWnoK0C4_yL3qgsHUZ7pDsqMHuHE0TOOJ7DkYQzY00ND8NIuXxgoRp6xCVE17i7sCHp5fist6Nxriy5P05VJtJEZ0R9RZJQOTVHcDPgCUhHYEds8dMcDi3L0Tybun_8nbDFMJMVVGC5_PUdyk0qkMyF7mrENBjcVtEvPBNa_hlD5x3rksa7cNbZdwPRLF1DNVsaE9imeSuRGM1HV6aH5PPZGvq9ySKoztIZtOLILJqqFS7mgfrhYJUL0Xq_DczmbokKrjuYkZQ4Hms5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1974c7b3a7.mp4?token=jCq9C0e8HlEqhaWH07qrUBv-qhGNaoWn7tR7Lzy3apOpA_5ky24fzickns8ITLctbkCC1iEWnoK0C4_yL3qgsHUZ7pDsqMHuHE0TOOJ7DkYQzY00ND8NIuXxgoRp6xCVE17i7sCHp5fist6Nxriy5P05VJtJEZ0R9RZJQOTVHcDPgCUhHYEds8dMcDi3L0Tybun_8nbDFMJMVVGC5_PUdyk0qkMyF7mrENBjcVtEvPBNa_hlD5x3rksa7cNbZdwPRLF1DNVsaE9imeSuRGM1HV6aH5PPZGvq9ySKoztIZtOLILJqqFS7mgfrhYJUL0Xq_DczmbokKrjuYkZQ4Hms5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سحرخیزان عجیب رید امشب
😐
😐</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108489" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سحرخیزان بازمممم ریددددددد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108488" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=QKI12ARdXy-lyP3qt7Vu_7YlA9SE2prI42LhL7ZutIaTwY7ydbpZRvFJDoDEizXEiI9Z9eFffj4kcdgvWhi1mxf55yK-3MNwqNaDJYPUEErklsBJWokKD7YQPawEfMs2x31m44nr20eK_OfMC3088PYBsay0L5KXB0n6fk1l6_w_EKffTfIdPvNgLsG5tt7QxvfjU0klIoIjqAXFrCNm858Cm1B5qhiy_KtDkPsJLc5-NuBJ1nysbBQ7DTwRM6fFsOBTNP30dCfEV-2IgxQg9npNR35Tkp5pjlBkfjbtiBvyR0pPnSz_DEGKOGdzj4shRa_e8pbAEisk-Jw_tQBanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=QKI12ARdXy-lyP3qt7Vu_7YlA9SE2prI42LhL7ZutIaTwY7ydbpZRvFJDoDEizXEiI9Z9eFffj4kcdgvWhi1mxf55yK-3MNwqNaDJYPUEErklsBJWokKD7YQPawEfMs2x31m44nr20eK_OfMC3088PYBsay0L5KXB0n6fk1l6_w_EKffTfIdPvNgLsG5tt7QxvfjU0klIoIjqAXFrCNm858Cm1B5qhiy_KtDkPsJLc5-NuBJ1nysbBQ7DTwRM6fFsOBTNP30dCfEV-2IgxQg9npNR35Tkp5pjlBkfjbtiBvyR0pPnSz_DEGKOGdzj4shRa_e8pbAEisk-Jw_tQBanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108487" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">استقلال کوووون آورد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108486" target="_blank">📅 23:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رونالدووووووو گل شماره ۹۸۱
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108484" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">النصر دومی هم زد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108483" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">استقلال سه تایم مختلف تعویض کرده و دیگه حق تعویض نداره</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108482" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
