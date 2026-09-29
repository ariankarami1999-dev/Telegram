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
<img src="https://cdn5.telesco.pe/file/gYXRjYA--e2f-iYQISvgNOt1GSi4kECofcLLbhuqh0lk06R26WokZuLVuZrLwJY2mbNTjHNkbifvFaCZYJUuwKiLVCxYmdcqruuHEkp68b1bYO8qJ8Z0uk6tHksQYPL3stfvHiVlFA3EuHKEsVd7PhAgeGBrhz5gf6YUJqFRnu7U8eyAJ3bDQKJrBryWBnxAv0ZkG1S22fU5JTKdb3WlUo3QR6pUgGLGeUUlJeGAvQRFUX9lBAuiz55hAjEJBmFaqoallDY-SZDXN70UMdsF2wHygizOcjHD4Ma5Ho8NH5dTyA-04mjt4ihwktRs4C_tNOYhUamkl8adf1xDuieLRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 397K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-107466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/107466" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/Futball180TV/107465" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYB-d8jMOXMJB8lR5kd36tUSQ9EyhrCmUytf9qw9C9s4B2uYg2zToFvfvaewy_czhRJSjhYNcz7BHZXysbJG9dzLlcBfA96377MzAAUd_oOZKAG4VgzblC9jbPswPLA-2WR4dS-_lnC66ijWO_iCN04d4fcPDEZFGONdK1guGpYANtqD7WyzVaHObGGhdbOGu3u2j_nHDLpyzCZbQbDgdpWp6giz-xsYqrKnRTtgt94EZgVjNjJG7gy84iBu7HzKbxFgr2hV72GyMP7yM7T6qAvvkSIViwcXIMUyAiEqbTfvSr2Vp7Jjb5QWycNl8YRdRiO8AG81AfbQYs04MWJo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107459">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
توضیحات میثاقی درباره شکایت اندونگ و کاریله از باشگاه استقلال
⚪️
محمدحسین میثاقی: در این هلدینگ خلیج فارس یک نفر نیست بپرسد که اندونگ کجاست؟ چه کسی قرارداد کاریله را امضا کرد؟ آقای تاجرنیا الان وقت آن است که مطب و آپارتمان خودت را بفروشی تا سهم خودت از این اشتباه را پرداخت کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/107459" target="_blank">📅 00:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107458">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
⚽️
خوشحالی فوق‌العاده زیدان پس از گل پیروزی بخش فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/107458" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107457">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری
باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
محمد
حسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107457" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107456">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌تماشایی مایکل‌اولیسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/107456" target="_blank">📅 00:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
امیرمهدی ژوله جایگزین ابوطالب حسینی شد و برنامه فان فوتبال 360 رو اجرا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107455" target="_blank">📅 00:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=S4yCl0gAHcBefV0-lDranY8EeMdvY3M4PFeY5iYe7kfti3w5CeVqDyHDv4OJpcf9pkOg_tycREUszUw7QUNVJGDm3UVaIwmPTFkHdoiyGE4mLyxgS1aYj8hDW8uD10zVVkGobXxtAt7a54PcBCn1j8E0WYvzbtdpRqFjU6M4Z5UU9RTDNg9LItJ40oAMoOjvfF28Zi1FEZmtF168WWe__FCIyzF7UUxWr748EL4nY9aQxCGmrBDUgZluLjSGi0wbPJWxSHbLKvgxFXyw3kJQ0xAxA1POCWvR8mpc6dI2GKaWAcwcQpfVYQs2UsEfJIROHgUWPvdNTLTNS5ygOEj__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=S4yCl0gAHcBefV0-lDranY8EeMdvY3M4PFeY5iYe7kfti3w5CeVqDyHDv4OJpcf9pkOg_tycREUszUw7QUNVJGDm3UVaIwmPTFkHdoiyGE4mLyxgS1aYj8hDW8uD10zVVkGobXxtAt7a54PcBCn1j8E0WYvzbtdpRqFjU6M4Z5UU9RTDNg9LItJ40oAMoOjvfF28Zi1FEZmtF168WWe__FCIyzF7UUxWr748EL4nY9aQxCGmrBDUgZluLjSGi0wbPJWxSHbLKvgxFXyw3kJQ0xAxA1POCWvR8mpc6dI2GKaWAcwcQpfVYQs2UsEfJIROHgUWPvdNTLTNS5ygOEj__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
سوتی سمی عادل فردوسی‌پور و ریختن لیوان آب روی میز که با خنده‌های آسانی همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107454" target="_blank">📅 23:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=BefdyXKSNs5N6tfaj6gOteJ1GQCkB07uzuKbWHytuJlkxJEPjZOTcROY2zwPWAzuJPUvsysrr2XS2eaHreXKQyKgKvpclD53989E6e7aN6_aiBtDUXO_Sf2cf_GbWhpfCz4LW6iX4NlefZoERH3vP8_0qP9Qimz1NqOwtjRmyVnqhayDY8HkjYpKK8D0iF69peo3MLY4Q8UZABdzodxB7ny_QJMM9mYKj-RX6OWMpigUgZ3JjHpQ71JUzJC0i5NVXVpffAg66SDqvmsmiU9rlIPhhgnFt6kbotymgp-R1Lf03VUBlpytHZGZQ_wM1itnixe2lb2o5jhUodSIldZfnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=BefdyXKSNs5N6tfaj6gOteJ1GQCkB07uzuKbWHytuJlkxJEPjZOTcROY2zwPWAzuJPUvsysrr2XS2eaHreXKQyKgKvpclD53989E6e7aN6_aiBtDUXO_Sf2cf_GbWhpfCz4LW6iX4NlefZoERH3vP8_0qP9Qimz1NqOwtjRmyVnqhayDY8HkjYpKK8D0iF69peo3MLY4Q8UZABdzodxB7ny_QJMM9mYKj-RX6OWMpigUgZ3JjHpQ71JUzJC0i5NVXVpffAg66SDqvmsmiU9rlIPhhgnFt6kbotymgp-R1Lf03VUBlpytHZGZQ_wM1itnixe2lb2o5jhUodSIldZfnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سردار آزمون: دیروز به زنوزی زنگ زدم و گفتم یه وقت نکند من را گردن نگیری/ انتخابم برای بازی در ایران تراکتور است مگر اینکه خودشان نخواهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107453" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=hOjEOLmU6QnJaeTDVxNs7QqL-Rx1pkKpBf1TnTR5uh0BB01O0oS0X-UxOQngeahNnK-hR1ro6zHI9e_N-Q3icdzu4RmGqAjAgKv9N_LLr7EsmwnhV4WQbPZENJNosDe2cGjoPVbpzl7DxeCvY7mQF0GawVnCjC3MI8JhDAJb6VWhQGgmuFSH6v5WrDDfwqYDrYNiTQa33tkbjoZN4SFmBwlF9H1-xmtBv2gM84hB2y5zxms6qU5yb5SvXcUqrvGFrD0SCE0TcnKjeJnsXTbf6aZ9NTDBx-epclFsiZGqR5I3dhyIBYn3Gcfjmu-Q5A5WtVSwecA9ZtoptXP75rWrnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=hOjEOLmU6QnJaeTDVxNs7QqL-Rx1pkKpBf1TnTR5uh0BB01O0oS0X-UxOQngeahNnK-hR1ro6zHI9e_N-Q3icdzu4RmGqAjAgKv9N_LLr7EsmwnhV4WQbPZENJNosDe2cGjoPVbpzl7DxeCvY7mQF0GawVnCjC3MI8JhDAJb6VWhQGgmuFSH6v5WrDDfwqYDrYNiTQa33tkbjoZN4SFmBwlF9H1-xmtBv2gM84hB2y5zxms6qU5yb5SvXcUqrvGFrD0SCE0TcnKjeJnsXTbf6aZ9NTDBx-epclFsiZGqR5I3dhyIBYn3Gcfjmu-Q5A5WtVSwecA9ZtoptXP75rWrnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های سردار آزمون با بیرانوند درمورد رنگ مو و سربازی‌اش
🟠
همسر بیرانوند باز برایش حنا گذاشته ولی اصلا بهش نمیاد. یکی اکرم خانم (همسرش) و یکی اکرم عفیف او را در زندگی بدبخت کرده‌اند!
🟠
خدا کند علی در فجر مویش را نزند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107452" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
جنس متفاوت غافلگیرکردن یاسر آسانی!
👍
🇮🇷
خوش‌قلب و خیرخواه، مثل ستاره آلبانیایی استقلال؛ وقتی یاسر تصمیم گرفت برای اعضای نیازمند باشگاه، موتور و خانه تهیه کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107451" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
از ختافه، ژاپن و عربستان پیشنهاد داشتم
🇮🇷
واکنش آسانی به پیشنهادهایی که بعد از فصل اولش در جمع استقلالی‌ها دریافت کرد؛ بهشان گفتم فقط وقتی پیشنهاد استقلال آمد به من زنگ بزنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107450" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
درباره رامین با ساپینتو حرف زدم؛ گفت برش می‌گردونم!
صحبت‌های یاسر آسانی درباره رابطه‌اش با رضاییان، اتفاقات جنجالی بعد از بازی با الوصل و پادرمیانی بین او و سرمربی سابق!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107449" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎙
🇮🇷
توضیح آسانی درباره تکنیک‌های کری خواندن، از بازی مقابل پادیاب تا داربی برابر پرسپولیس!/ در استقلال، از تمام لحظات لذت می‌برم و خیلی خوشحالم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107448" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
گفت‌‌وگو با یاسر آسانی، درباره واکنش عجیبش به دعوت‌نشدن به تیم ملی آلبانی: حالا می‌توانم برای استقلال بهترین بازی‌هایم را انجام دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107447" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=kT_tTrbEwcinMnJWABONMwgmka_-FHqOdPkRaQDjLYK65PfGwW4LGko0wo1gIRAmujcD3FZUQ6JTRsY_m1pWsGWUvEQ8FuseNqC3Qp9HHjhM5MGqUA6zvCqswt4Up2b_eVmLbzfqDOPpgB2exaKqYcGHfLe9cmnz-Ceou2bjAHSOc3QRjTv0K00shOFGg-9UkJkIuAda2nV4PYLtWyXB_FaWNDVI_VB59EvJmu0WhGGN1UqU2-6EUdlAakMm-Quh9WtL8rDGA_m59EdIYF353PRo_pfkSO7ZJEfNbmauDxiTSYFOWUh-mSB3KVmPpZg6UfWYlZDSdi__FBI3t6bj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=kT_tTrbEwcinMnJWABONMwgmka_-FHqOdPkRaQDjLYK65PfGwW4LGko0wo1gIRAmujcD3FZUQ6JTRsY_m1pWsGWUvEQ8FuseNqC3Qp9HHjhM5MGqUA6zvCqswt4Up2b_eVmLbzfqDOPpgB2exaKqYcGHfLe9cmnz-Ceou2bjAHSOc3QRjTv0K00shOFGg-9UkJkIuAda2nV4PYLtWyXB_FaWNDVI_VB59EvJmu0WhGGN1UqU2-6EUdlAakMm-Quh9WtL8rDGA_m59EdIYF353PRo_pfkSO7ZJEfNbmauDxiTSYFOWUh-mSB3KVmPpZg6UfWYlZDSdi__FBI3t6bj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حسین‌
عبدی: رفتن به المپیک ربطی به سرمربی ندارد!
‼️
خیابانی: پس گواردیولا هم بیاید همین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107446" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uysxGBWmO2YOjkEN8dWtoDaKaCCu79b5mZtj_xZvNhq2A89B-K6gzLjNLr1rQK-zgDXpNSgEvuau4ScKcc_R2XHXuepOGQ_HQQ-wLIiz5V_WbuPfQUchYYnfMraEqZkWHR6VaFFoyFmdlWyMClGm8g_4A9tTcqw27AJ8rWRLCTy8cnci6192GRoWUNC5U_2RVrqR_opAR26sCh9-ZrUBh7oQz684-odlFun2wHNlPADNnuen31_tNuOzs7g4SYpOGedPCRZbLIT_sC6dq7HCGUyFCiTR_i6nNaw6ZUpnOgffNuYDScdOlc2vKrB_fuY0KgpaUK7itHqzyGrpvQpEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9S3wMbJKYz5MC5h6dS7KJxXqASR9WGLfHC-JwG2Md0GuQudakfdYOon1iiszNdnTrIAWEKM4n2Lr9jScvZzE8nCTxD7aAelJsLqg2sFRilDXRMRtzjDBOAur6SN7nNYZ8uZA7LUwyp6gPfOSmd6buoo_NV6Jy-jZ7Buyxom35VEkUlBKJfds7qnmrDiTpMXsp3cmeghkAt2Z8dogrs5JfnqLdASc4fAQkqxUDgw-CntlU3-R76IVuIGZ0gNVk2gb7H0SUeua5hJl8sE0RlZkBJOO7rJbIaKupg7kHmxPLijUPkV87XScKJ_dGUWIoAobAVXaWsvbtbXO6ivFzqBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkjgRNs3vS2mFs27G-spAANYaZzTgMvfhbi2L8CxBKhcCHUM4JHnRhpAQ9gGjy2m-JRZjYqwTesZO40tGI_NydctK5t6AQ76b24wuJTDLfW-pJKRFMZQD3AKCHEqhuOrV2kQa2EzmjrJf1Ck6rIXxZBZOswGZGZeEoFDc3QIkZBoMOtgygl_I8MqjGxbulHqMzFBQfxiTsN41aSxET2kwTFZTJWnxhyncNbXs7w3q9fxAhk8TV2jo-qUd2xJP_4GSQiqKsdA0HtUAINkXpz4tgmWSBG1dbjaaHMJvUzcE5iJwiuKrwJ-0VPAGohvyQuR7jCsvrGFWU50tiz1SmmFOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
یامال دیوث اومده از عرق زیر بغل نیکو ویلیامز استوری گرفته و مسخرش میکنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107439" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107438">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇮🇷
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال : علی تاجرنیا به اعضای هیات‌رییسه نامه زده که جام فصل گذشته به استقلال اهدا شود اما هنوز هیچ‌چیز قطعی نشده و هیچ کس هم به تاجرنیا قولی نداده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107438" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107437">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RfyQEIMreHFMmZLp9dSTAjJeP4OnXKqvWjvjjei2DqZWRgr27q3NxqM8m__qT3pI3bcpFIDjQyWuibns9OJJcDkz-goIE_9o_Mj3mVJAOj2IqvFTooRCfq_KJosjQTF8-0uBUF6u0E2zQ1zeThYKchS4DQ1gCeavVPEh9YtsEfL263ve5tV6uape0lHc0m0CDyRm63Ln0yX83MiH2a7Wc5mjI1PLFCtriJsJvuRlCAsCM4Njhr-EI53OGpN3bK5zeKskbV6IS_xU2774yVyDEupz74tEj5WlMF1YTImHofIwrXkiHgBSXnYJjYaxLsQEVe5QYhGcrEhd50y0cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
افشین‌قطبی، پیروز قربانی و رسول خطیبی سه گزینه نهایی فدراسیون فوتبال برای سرمربیگری تیم‌ملی امید هستند که بزودی یک نفر معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107437" target="_blank">📅 19:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107436">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👍
ویدیو‌دیدنی از حرکات بانوی ژیمناستیک ایران در بازی‌های آسیایی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107436" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107435">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbDrOwZESMq39SV2O6_Ed3LMJi-N6OuvkAF-gmPfrTViXcnnVZ4bdhHHwuOSvtLLWENsfG4r96Vvn9VLAuR1J7Rgd4ciLP-UbkPwrQV0JkqxRHbJngvVOKK4u7xGkTV4RdBCMerPnBTQuOzkoZS2TAEYbRPgHtYXV4WXrcjS-Y2C8xOaQEsNrwMJAyuL8RBAGGHrA75L0QSjfN9aQDSii9n3zmmgLzyIRzqMxZo1TcyUEt-nh_6xEYbKWd74lakf3O2ckWNLgI19SjvUXpBmUaPnZVElvKf48NYqeYvOYwhhUbXb8RC-vvEtvZ2yxWV0EBvznDM45YYbbXIKPnBRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
دوایت باکس، گارد باتجربه آمریکایی، با تیم بسکتبال استقلال پیوست. این بازیکن آمریکای سابقه حضور در NBA تورنتو رپتورز، لس‌آنجلس لیکرز و دیترویت پیستونز را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107435" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107434">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
تاجرنيا: خیلی ها من را سرزنش کردن که چرا موضع علیه سه جانبه نگرفتیم اما در نهایت دیدید که چه افتضاحی برایشان رقم خورد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107434" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107433">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFmuXMEjICNeXVrIoxPRjduWboE35hNMVKwxh90GX9PAKpBtMjirnNWAAfViqSqUhiUwn8cg5EsNS2o1h-DheuRGjxWLwwcGwV7flLeaSlFEEFonAeaARcW-eXXK1wqSQxxdZEL2hi23huWO1ujxidhO8dzDOsKbjVKipRjYXvRZYdodMWPZD_8kP1vPFppvURrzfU-IvcVzHwHhb915HqJ6ECRPRZTdBqT8JqzixfMKaxA8BrIXteCvZLssrJY4jUd4SyYEfEUJolg1umyg-SAoBeWGQRTT6W-vZMtW0I2lowWeNkgKOxLYNUyMYVQPoH_5TVdCE295UmcbugZHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد اسپانیا در ۵ بازی اخیر خودش
🔥
🇵🇹
برتری مقابل پرتغال —  رنکینگ 7 فیفا
🇧🇪
برتری مقابل بلژیک —  رنکینگ 8 فیفا
🇫🇷
برتری مقابل فرانسه — رنکینگ 3 فیفا
🇦🇷
برتری مقابل آرژانتین—  رنکینگ 2 فیفا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برتری مقابل انگلیس —  رنکینگ 4 فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107433" target="_blank">📅 17:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107432">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107432" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107432" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMGX00fs3ZcZyVbHZfFx51_JCdy4ql8aN6WTpA8Qxm4ipf1e9awX__p7Hrqucw-oDW3f5LlILhx5XBKoOx1K34UjDKF8Flw0yo3cTKplTOZRfR95O0fJw6dTb2XEaNQQvcURurXvFwgQfuYOPVdUke-52sheMbWiBwQgRmbUe9yYHjDIkZl0TDLsOxDWw_Lbteq_m89oDzjqjf14i6taVLcFER0HiG3-XMNBmZI47SDtK2Lk3nsx548Vmj-4yOaC6fSiMMY8WW925qF3qT7ZvafPMf51xvmhw5ds8zL07Vj40H9aWxu6nKCmnCcf-NESu2iUr8HJuWNVxrxNtzun4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107431" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=vHI9hmW59n8osWbYd1bj7C2xTS58vm73ITN591f0g62XpMe_ReryOJgeRW18qm3jNFiTOCaut5P6RhZZ5fPGi-ORmPzN5TSzz--7AEj2oFiNZi_EYKvKgmyH76kVzI-1OipYn0hFnBAqC_rCNMDfkggLx6O_Sb4K_jhw14i3F4Bknq_bTQc0Ppg_2s0XQgrQ_JBadMz9zVQ9lLTGEbyBBLuwL8i9Iiht5DMZVsqhWO3dvbGPWB_Z_n27OJDETggh3_4jZxt_43tubTlgIKIUMpHGhYXBewXgrLuL5vp_LZT_DN6MqtEAzRtWaHEIO4ScEgK82rr91NIc1mEalblP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=vHI9hmW59n8osWbYd1bj7C2xTS58vm73ITN591f0g62XpMe_ReryOJgeRW18qm3jNFiTOCaut5P6RhZZ5fPGi-ORmPzN5TSzz--7AEj2oFiNZi_EYKvKgmyH76kVzI-1OipYn0hFnBAqC_rCNMDfkggLx6O_Sb4K_jhw14i3F4Bknq_bTQc0Ppg_2s0XQgrQ_JBadMz9zVQ9lLTGEbyBBLuwL8i9Iiht5DMZVsqhWO3dvbGPWB_Z_n27OJDETggh3_4jZxt_43tubTlgIKIUMpHGhYXBewXgrLuL5vp_LZT_DN6MqtEAzRtWaHEIO4ScEgK82rr91NIc1mEalblP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی پرتغال در خانه ی نروژ، در شب نیمکت نشینی رونالدو.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107430" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaMLohSfMu0yw65KmImTvdTzrkyECQMeSfkLJ9OUOvyRU4b1QZrk-F3jC2mIAkfZKDYHvtgP5DkGEcbE1-xk_2yol9sLuYUWpBrVLWxglIbgULTsbv24TVsv36ZWa4ueh8LEuWbFdZB41QRs5z1UjYd3_M2Q9iU4PRmOscfyhrLXxfTeLpzFRInSorc_4aaCeBmgoZO_EkTz58i00in2aphw2388ftfbeWLzIQGHTZWdqZeTBNYBFiPhcSDtjb33H8CH1GKXikW0h-WJAmuVfLpGc0WwFbBq6z9SBWQnBru-uLW3mESLtAwLSxZlCI3PL9QcglUvj4m22BWjaj0Cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عکس فوق العاده زیبا از برج میلاد و ماه که دیشب گرفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107429" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=ZOblQiYI21VFD_TlFhstm0OHDqf2X-gyPluT_GK1_PSJtiJ4a6KwTD03AQLj4UNabxmg5NjdMhE6k59tGXgXr8AsGjbANej9pPX_35WACKxQT9tpFuaGfiqX7wIKf66abLLTl11k4_EpjVwQkSK5grMoQ8jhIslGoWOilJ-yx8wbLtCYS45D0wTVIABH7YsoojofBzALNJZa45fOluC6-NxDVKS6iUZBxYo1lvKELZhLHYmaxWJOQaUOc0QyuIHJK8LLSPUSC-AdZhsnAUZwn_x7z_kTHHvRWgv69cZn_2346Q9aUp5HruhHMmw9W4lyK2shg5ZjdPDFIGXn3jzKWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=ZOblQiYI21VFD_TlFhstm0OHDqf2X-gyPluT_GK1_PSJtiJ4a6KwTD03AQLj4UNabxmg5NjdMhE6k59tGXgXr8AsGjbANej9pPX_35WACKxQT9tpFuaGfiqX7wIKf66abLLTl11k4_EpjVwQkSK5grMoQ8jhIslGoWOilJ-yx8wbLtCYS45D0wTVIABH7YsoojofBzALNJZa45fOluC6-NxDVKS6iUZBxYo1lvKELZhLHYmaxWJOQaUOc0QyuIHJK8LLSPUSC-AdZhsnAUZwn_x7z_kTHHvRWgv69cZn_2346Q9aUp5HruhHMmw9W4lyK2shg5ZjdPDFIGXn3jzKWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر بیرانوند روز اول خدمت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107428" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📊
🇳🇱
🇩🇪
آنالیز تاکتیک جذاب ژاوی در دیدار اخیر خود مقابل آلمان یورگن‌کلوپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107427" target="_blank">📅 16:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مهدی‌مهدوی‌کیا: عدد فوتبال ایران پول خرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107426" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇪
نحوه برخورد بازیکنان ایرلند با اسرائیل در بازی دیشب که حسابی جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107425" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیتِ ناراحت کننده ی سرخیو آگوئرو.
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107424" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUztCKqAIyFZ6pBjDi4LOl8ATfcpNLR1GGNp0trqy50-H5cFaR2eyy4ODK9fzlHYPHU16DCt0UD_Ub2f4uC7lQE5MfqMzGjpHqwN8bRHga-ldqwuUgu2hrkvcZ-CiZRl5j2tOJ9RqmzOAyM-WbP5_Vbn6EY8cnI8lqF55J1Vp7Q8Dw-0vc8sDzuS87Upeaqwis9SWOX9vpCA3VNnoga4j6nIag2Hy9DK2ypxLatJiLrxqm5vAn34cD02-mqrWsLeKbe9zjV3GZF10zAnap4Shw4zYRqT_TOF8OqEPOoYQ3rd55m4h8YdmJ9xILnbbNyAIxbvXdM9dX8Zq0HU2GwQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه آمار هالند و رونالدو تا ۲۶ سالگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107423" target="_blank">📅 15:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=tvOGtE230pDK4yAC6a3niBxmL0V5jQmbWFcpxCqMXdNhUBILa03YOBFodszbKeCRG0sI5Y1wdswOqJwSDsZTmVq-b_tRpLwRKsi2VAQVGMOwNAAjW7yCC0VnAC68T_3R6CIgteQmfgeQNfHWfkD2BfgDB_RnsAeTSGTJO8pJDZovO9qub4dLhK4CsN18MQvrpcrpNq7e1BNb_h5rJQ2aJ1Ek2SLk-qyEJ8OdgZ1Q1ChaArRzCsxth9Yo-c8zWqJrUUtfIaHGBqIRtIqy65PQEkJ71Yna5Wa6RjITSFIqIwfuwV46Y2rx5yxJGEDuFGeIQxEUtTZkfXf5vlEX5_2mVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=tvOGtE230pDK4yAC6a3niBxmL0V5jQmbWFcpxCqMXdNhUBILa03YOBFodszbKeCRG0sI5Y1wdswOqJwSDsZTmVq-b_tRpLwRKsi2VAQVGMOwNAAjW7yCC0VnAC68T_3R6CIgteQmfgeQNfHWfkD2BfgDB_RnsAeTSGTJO8pJDZovO9qub4dLhK4CsN18MQvrpcrpNq7e1BNb_h5rJQ2aJ1Ek2SLk-qyEJ8OdgZ1Q1ChaArRzCsxth9Yo-c8zWqJrUUtfIaHGBqIRtIqy65PQEkJ71Yna5Wa6RjITSFIqIwfuwV46Y2rx5yxJGEDuFGeIQxEUtTZkfXf5vlEX5_2mVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت  بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107422" target="_blank">📅 14:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1947c53917.mp4?token=ogGcROtN0zV7cvV1rtbYlAnbyUh7PDiMEoBetVw0Ev54U6m2Wz9R2Jli7VvNLA1eutio6wwWi0Gr6s5TGN_F9K3hRmvnJdxa2kRLH87wWFATfpnO5667TmOAv40QGnNecD90XetvFOwTdBXtUqUf_fTZcYT_AtKwACwZjH6Yo5XI6g6NT4mVe_GL2wOXfofiG3qIPREJWZ_4q6jc7ZCjOxxH98Hkb7XoN-iTumha2jUhz4jBr_AqT6gnTY8P1VlGRDkUELelNGezJin_l9eZ_DiBkaRx97WkkkivClGu-Je39grEHUkGDQbjCgeS8_5EJTUSWopt9V0A0wL5NTkKDLdBGohSVFmRvnOa4RiJdwXUNbvXq9sisLmT5SW6gI3vKSr8YI8gR8-434nA1Eg2fxchi6jrC9yNuNOI2ZQIa97xq8tIovDTZjS0L7YwYiM0uqC14Ga6VFA0fo2pkDo2b5bqtNii5lSSx7XAiDTT_q_bFGnsmh0nikUbIgkCeqAbGuFMdP38OoIKa0iVsMywA-C_Q9_0NmC1CfPp499-RAxhxe4sMCld5tfrJdj8uFpzJQmWhwwFJZroQ-scUpgV69Z6L8QIYYDpQrER9cYHjDm40thIjTSMQZXLazXRH2GUwat9Hl5RhB5J1hYmKN2NuzvSfcvBunrFpJd6gmKJupg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1947c53917.mp4?token=ogGcROtN0zV7cvV1rtbYlAnbyUh7PDiMEoBetVw0Ev54U6m2Wz9R2Jli7VvNLA1eutio6wwWi0Gr6s5TGN_F9K3hRmvnJdxa2kRLH87wWFATfpnO5667TmOAv40QGnNecD90XetvFOwTdBXtUqUf_fTZcYT_AtKwACwZjH6Yo5XI6g6NT4mVe_GL2wOXfofiG3qIPREJWZ_4q6jc7ZCjOxxH98Hkb7XoN-iTumha2jUhz4jBr_AqT6gnTY8P1VlGRDkUELelNGezJin_l9eZ_DiBkaRx97WkkkivClGu-Je39grEHUkGDQbjCgeS8_5EJTUSWopt9V0A0wL5NTkKDLdBGohSVFmRvnOa4RiJdwXUNbvXq9sisLmT5SW6gI3vKSr8YI8gR8-434nA1Eg2fxchi6jrC9yNuNOI2ZQIa97xq8tIovDTZjS0L7YwYiM0uqC14Ga6VFA0fo2pkDo2b5bqtNii5lSSx7XAiDTT_q_bFGnsmh0nikUbIgkCeqAbGuFMdP38OoIKa0iVsMywA-C_Q9_0NmC1CfPp499-RAxhxe4sMCld5tfrJdj8uFpzJQmWhwwFJZroQ-scUpgV69Z6L8QIYYDpQrER9cYHjDm40thIjTSMQZXLazXRH2GUwat9Hl5RhB5J1hYmKN2NuzvSfcvBunrFpJd6gmKJupg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: پاى حرفم هستم ؛ پول كاريله رو ميدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107421" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=dblWtPfLxDn5yKpaQMsH2NDfRWd_o84JYsKZ4MtAX1Ue3X_eqaCPaQ4XINhEauaRDBKeYyCWiw8qcEmrt0JxCS6Rsl1n52_2uQy62rvY0WJwNCUbskAxe8n5YFLm3ON9mk8r0vDvWAwSDpH3GCo8bbIO4MojK2TeicQhM9dW_eyfhutQtzuGG-6tIx50-2Tb-w6iS8xqnpxeHQM2hy_AYITdF5P7_NakiAiZgAFpBizXu3chhEprhtA6qjC9oRlsLfx-iengEaIdB4zETQS28-nPwDwU3Tj_zrL0cIAhwKaJMqXbw13WrcnIGf8ZnSpSB20Ys4b0hHUCygxl3MR5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=dblWtPfLxDn5yKpaQMsH2NDfRWd_o84JYsKZ4MtAX1Ue3X_eqaCPaQ4XINhEauaRDBKeYyCWiw8qcEmrt0JxCS6Rsl1n52_2uQy62rvY0WJwNCUbskAxe8n5YFLm3ON9mk8r0vDvWAwSDpH3GCo8bbIO4MojK2TeicQhM9dW_eyfhutQtzuGG-6tIx50-2Tb-w6iS8xqnpxeHQM2hy_AYITdF5P7_NakiAiZgAFpBizXu3chhEprhtA6qjC9oRlsLfx-iengEaIdB4zETQS28-nPwDwU3Tj_zrL0cIAhwKaJMqXbw13WrcnIGf8ZnSpSB20Ys4b0hHUCygxl3MR5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بیرانوند از خیابانی تو خدمت مرخصی میخواد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107420" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=M5gftEjO25f3-fMLfyn65QzJnEEecN4-iruYJD_xIycaMOdI5Emv6p4BOLiLpUrOfDGhWtT4-Xxi-T9CBD4eLGoHtLqGhoWB43VOXk7o7RNsGATDbG0W56hTG7vASpaKjJ2ybw9lwVvRBJHg8uT0E-vjZ413L2wPpGcteun_4KmXGjX_a_dwenkhoP6Yiu4BgMOUHAmdUnrUcS2l1Y9AqFNhK83xnke5HDeUc-Khx11wkIXfUkOjU518qCV2qAqUTKDlyAmuuV45oECurVpKqoV4iS02T92AOjHscECHVXefnYj6998uMDtbC9TGaYJ8Yh6QCrqUQUcBymmyX9ZjYEJBf70nGoMQ0Kx6rstRxd4ghMrlcuXxhNi0ZGusavfUfP0yABIY4bYPq4YxH9ToHDITTUJtJuhZSm_tilMoVlsInonCX-pat2xfVnhiFQGO6s4582EjuXK3HSMgGzli5-lBZU1oeKs3LmgfeIuk7cDrdqxUc37AlauenWyoJS6SxoRH48ePt2ks2phaHfwAgR_kT1UYQ6tQWAMpuGV9trhpxPZ0p5F5ntQ0JRwiSxlhazXA49JmVNlHRu6cZa41mKqL-5JZ_3xPPWxuUVVLaZYk-acfsZjaVL2JkkEBz8izHOUt1p-Evkccq5kcJTVqHKxiEV4n2KcFEBU1QIRQYQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=M5gftEjO25f3-fMLfyn65QzJnEEecN4-iruYJD_xIycaMOdI5Emv6p4BOLiLpUrOfDGhWtT4-Xxi-T9CBD4eLGoHtLqGhoWB43VOXk7o7RNsGATDbG0W56hTG7vASpaKjJ2ybw9lwVvRBJHg8uT0E-vjZ413L2wPpGcteun_4KmXGjX_a_dwenkhoP6Yiu4BgMOUHAmdUnrUcS2l1Y9AqFNhK83xnke5HDeUc-Khx11wkIXfUkOjU518qCV2qAqUTKDlyAmuuV45oECurVpKqoV4iS02T92AOjHscECHVXefnYj6998uMDtbC9TGaYJ8Yh6QCrqUQUcBymmyX9ZjYEJBf70nGoMQ0Kx6rstRxd4ghMrlcuXxhNi0ZGusavfUfP0yABIY4bYPq4YxH9ToHDITTUJtJuhZSm_tilMoVlsInonCX-pat2xfVnhiFQGO6s4582EjuXK3HSMgGzli5-lBZU1oeKs3LmgfeIuk7cDrdqxUc37AlauenWyoJS6SxoRH48ePt2ks2phaHfwAgR_kT1UYQ6tQWAMpuGV9trhpxPZ0p5F5ntQ0JRwiSxlhazXA49JmVNlHRu6cZa41mKqL-5JZ_3xPPWxuUVVLaZYk-acfsZjaVL2JkkEBz8izHOUt1p-Evkccq5kcJTVqHKxiEV4n2KcFEBU1QIRQYQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔺
آنخل دی‌ماریا پس از به ثمر رساندن گلی شبیه گل مسی:⁣ قبل از بازی استرس داشتم و سعی می‌کردم با موبایلم خودم رو مشغول کنم و به بازی فکر نکنم که یهو گل ضربه آزاد مسب جلوی آمریکا روی صفحه گوشیم ظاهر شد. وقتی توی بازی صاحب کاشته شدیم، با خودم گفتم امتحان کنم؛ درسته من مسی نیستم، اما شاید جواب بده. و واقعاً جواب داد!⁣
🥇
روزاریو سنترال در فینال سوپرکوپا اینترنشنال آرژانتین با دبل دی‌ماریا ۳ بر ۱ استودیانتس رو برد و قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107419" target="_blank">📅 14:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=A5ICiUTzwXdcWaQaHun6y4VMrZioRDQ7jkTi9OpnfTFcVkcQN9b9meoUjLIbNYmehlMNiA-6s-cJGom9sMl9qjj3yFYQ5i_e5-jtbWmSceSDKwLDWAWne4Wwl2PVvyA4iO4ai7SMOqoYJesUHhlPVLjJxsfnXWzI-5drlC7MuIA4jLrU_p59mq4NhQDChTDfEYE-uKDvlvs-Z7ZOE27K3j8OMozh62f_xnh1JphvG2uCeFTIJO1A7GrwmLF_6hKqs7Bn81ni_tcV6q1b-JZPABx0ayD4MSPu1K53wwdAYGxmQytmvMAQFFIZ-vo7p7jvHd0bpvVhofez_VCd6KHInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=A5ICiUTzwXdcWaQaHun6y4VMrZioRDQ7jkTi9OpnfTFcVkcQN9b9meoUjLIbNYmehlMNiA-6s-cJGom9sMl9qjj3yFYQ5i_e5-jtbWmSceSDKwLDWAWne4Wwl2PVvyA4iO4ai7SMOqoYJesUHhlPVLjJxsfnXWzI-5drlC7MuIA4jLrU_p59mq4NhQDChTDfEYE-uKDvlvs-Z7ZOE27K3j8OMozh62f_xnh1JphvG2uCeFTIJO1A7GrwmLF_6hKqs7Bn81ni_tcV6q1b-JZPABx0ayD4MSPu1K53wwdAYGxmQytmvMAQFFIZ-vo7p7jvHd0bpvVhofez_VCd6KHInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
سوپرگل دیشب لیونل‌مسی از نماهای مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107418" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
ویدویی از درگیری بلینگهام و کوکوریا دو بازیکن رئال در بازی اخیر اسپانیا و انگلیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107417" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا:صحبت های بازگشا مدیر پرسپولیس سخیف است و در شان من نیست جواب او را بدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107415" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107414" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifxups_JdCNM1qwdWccrm6P-uD2CnGMSWaFQhekmyE2EH2FKEq8LPXksFBsJTR-yDtrDSdHSG7YFeT71Euty9eNIW6MJoGTowQDI0DarzHWD-EsEaVxOZx1OchONzVaGe47CKjXvbk5VZ4dtt30St1yJ2FP225OlnROkLull8midtfl7rdzWF22pA5aHXzJfiksG80sMCL13qWo9iDEp311d6krlpqVMrPfb1yx3w48UYmyxyaL_dUdn_ozllEHDPZXScQRPdRjzvTAqGcJEfkGGHtlACoIk5RyjNEGTavyb3G3uBfEhwYujszx_BxDrNl6ir5vEpHp70mlQYY55hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107413" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVztY7hVfrKa6QC1YVdBxtS3jivW6Bq26ClYhR-33EeLGZLvc8d_uf7XyVqY6YC2vU1Wj8Sg8wzMMKZVWTOZb-nw_iz2oHaQByiIXLHvuOxG2cjilyexF8-i7kWA2pnAvN_gx3iozsMXhAsgJZaUeOZcZhJo-2QLqTs4GDQIhQn-ZBfDWXmx_kcwzQ6ldvB8baq3q9kOIQB-pQAQZQ5-D5yb6z1fjLqwDfxM3qH7jmWXTSRMxFgPNpLCkXs37qOu4XCXQ1qnB8sr7-_jHj16Zl3A65HXqOEgf47Xv8lHspQtuete1ZsDP_jGJajjqh2ZFvX541N2u4KSHeDhqsU24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🌍
آپدیت رنکینگ فیفا پس از بازی‌های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107412" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پرویز برومند در جوانی ادای جلال طالبی رو در میاورد؛ عجب تقلید سمی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107411" target="_blank">📅 12:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlBZLuJ33Nyc7o-BnNiRCBMXynB_6XcOFGsjwAG55bCJA0MEsdoiWX33qL_xiVJOO1P6Yg9VC9jvmIAUmlsiDTXIPqjcjkGRnGeP-WBE9IcgYlIwFgl6OCub20z94ehvN8lgddwWTfS7SKgANMR4CcmFQrDf5ga1RveqDMAV1itE6u6EJ1nts6ifxEGLVflKWkGxCFh12BTOFR3fXhyIml8BCmRnHz2BsNvmcUDlQ-cbYU8zxK-AT4L-5E0hC0yQZfHdfygVFCWAIM3Li_WvUnPStBQ9b1OXXNwozhhQWBoUMlcqbrPF5qVt511W8Ax2ZVyqO_fM5b1b5kPHGXkDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت
بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107409" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚔️
درگیری شدید بازیکنان در بازی دو تیم عراق و کویت در تورنمنت جعلی خلیج‌عربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107408" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
خاطره حنیف عمران‌زاده بازیکن سابق استقلال: هر بار گوسفندان را می‌شمردم، یکی اضافه می‌آمد؛ متوجه شدم خودم را هم دارم با آنها حساب می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107407" target="_blank">📅 11:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
با لابی‌های علیرضا دبیر،‌ معافیت بیرانوند همین‌ شکل یک‌ماه یک‌ماه جلو‌ خواهد رفت!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107406" target="_blank">📅 10:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
❌
آنالیز فنی از تیم‌قلعه‌نویی که مشخصا چیزی به اسم‌فوتبال بازی کردن بلد نیستن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107405" target="_blank">📅 10:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🎙
مرور صحبت‌های ژوزه مورینیو در ۲۰ آذر ۱۴۰۳ درباره اتهامات منچسترسیتی و پپ گواردیولا⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107404" target="_blank">📅 09:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScwkw3igrmQCQwZ4QZG1DDvn4mD3Jq8zvV6bicmAYDHi_rLUDGE8qQ_5DbHeNre3jIjjveHzdi4E9pWrIRT-ANNFPibvUbhokfIqsMLcwDvocLWhfh11pKzB0nlFtruzaEdUvSEf_2nkO_9Fw7zA7ipgcinJySqq3_tMmX0JkJpSymIYNfYQP2aZKpjHKhB4VwSssTTF5TleUFlKLOL5KQlh0r7cJ4X4doG4XdPIo8SmN6V83A_rhRFvV6Beigs553ISKHM-7mwLYhVZlMI1u4YWJApRKGhRbXKKvZnVUA-NRwXrrp3CSR-9wgS5aENESH_v48BoNatr1U1znvjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
علی‌تاجرنیا خطاب به هواداران استقلال: جواب پرسپولیسی‌هارو ندید چون مکتب استقلال بر پایه احترام و اخلاق است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107403" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO5SynNRraco1bP8ZTIJ7Q4uFtJ6G2Z0LeVBASM_CoNkYk0pJp5yChheqSWLUdedrSaGR0xcZ66ePeyBlgTij7lEYYqOoJK32ZZ3qLbM7ZkWLXDpkwqCUAzhPRrLmz_jNyY3GdqJcKLrY0TaL7d_cuSrYJJLCdpLCiB2TEL3VPaAdXWh4svxcraphdkYhMU9kEtkDbynwX9dAfpX1ZQoJWuYvJChDuKd5rkdGq-00h93GXQCEjLK869FiXNc-OxfpWubWour1b-Q22zJrzwXrGbIvfJYwh5iOupF85xQ6i9yQx_4GR-Ah2THd3VbOIkjo3yYKZC84Q_oRVu5tkd27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
۱۳ سال ناکامی‌مطلق امیر قلعه‌نویی در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107402" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
مصاحبه جالب بازیکن خاتون‌بم پس از گلزنی و برتری مقابل استقلال در لیگ‌برتر بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107401" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
سوپرگل لیونل‌مسی از روی ضربه‌کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107400" target="_blank">📅 07:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCDDIy2WTmghh4FXObUhq65jkO7KpcRfwCAUoxX0PHgAqlXj0FiaWcE2pZJUvaM8YH80ao4gLDM16VijffQ7Ebzs84G-HFQdFvsqH_r73JvBeECAMTB2bcVrdkF61sZ2jGmdshwco2bc6rWmPpMKrEX5lf546pSkvCGi56Vr5CI2vVP85RNx04A701jhZ3HItvfwaVoBdoXmxofKMMX5aCAoc7M9-jxPoB4unIXAFb4eKuREXa02GSXfv_HWaPh7pjPD7dJnR_5Wmnq4p9TVo-ZDv47l4wXUJEGWxH-ohmjOq8h-_tmGO_rrr6AwjtBpW5cB8gtEcscUwRCR9-rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ژرژ ژسوس در مورد نيمکت‌نشینی رونالدو
او می‌توانست در این بازی بازی کند و مشکلی نداشت، اما احساس کردم به بازیکنی با ویژگی‌های متفاوت در این مسابقه نیاز داشتیم. این به این معنی نیست که او از برنامه‌های ما خارج شده است؛ ما قطعاً به او تکیه می‌کنیم و ممکن است در بازی‌های آینده نقش بزرگ‌تری ایفا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107397" target="_blank">📅 00:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q26R3KWTiwiwTlap-PWdoVrFeElgRa_6wVVkmYXO8JzOj3CKV3RbyJMRDb2KM_vl3s2vDwc0jV1aMBJLV0tK1vu4_iQUJB0DTAOZq-4lt5eq8bXkJOtdm8XUrvV4AZxKmQOtKPIOvgpp0w65054yDPSzAxuiTACEhE_rCZanWEEPuFD7qbyXvSqORg0Vvwf7YMpUNg9PDFg4oB0qW52_D1Yh1tml9qxcEMUP69X-knAcG5CVMpHWkTDlKrjJ8kYmY3atBtLjB4n5n5g-Aq2ZUBskpezsTnIOzG6rKDsN1pFTSTGSGsfX0DgUZ0zezm3WD5NndTwLkdoTPE2cb1UjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
❌
آلمان تحت رهبری یورگن کلوب:
❌
تساوی مقابل هلند در اولین بازی.
❌
شکست مقابل یونان در دومین بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107396" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYCqJoVb1YbFohLSg3eM2ET-xj0pEqff3Gge9f6B88gn15IENJWl24uD-w222u1hgUUhH-Q90LZNJFOuTo2c0cRkYBnnEpvhYVSDUqwCuAy2gmuR6Ws5e2P8zvFcm66uJt2AJOUqyB4BqHBnxTgj9u0-SnUQt99zQ9ZaFq-YS_SDCRn9VEd0PlRdIye6thv7qXsMQlI7jnco-r3dxBCvrG-wRgbqOug2MyptspLf3fjRON8rmtdDjZrGz24FnwOJcVSjdUaMAfI66h1ImfAAy4jsdr9LY9YAwSggAhsnUJac7J0MuXoA8xiJzlVaocWcdFsIhNETH2iK5OYKWgX00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🔥
ارلینگ هالاند، [65] گل در [57] بازی با تیم ملی نروژ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107395" target="_blank">📅 00:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJRbN-F1NffUhG9Fgy9ztca1LARuWooI6uFpe0DyKp4Aq4o8gfyAq1O_DWD95Uxix7UvanZIYtYZPR-n7AcdTZ_LXBEl4Tb-XY6NjK62lft97PmM8Bs-8xdyJ0gMAVZogaIVtBjq98Tw7zWaPd5EGp0x4iiAiOHFopxFaXoHBORSN88vD6ifWHVUmLHtFmg1aRfNKGtTkCo_gMtFzdvdGFzIOD9aUtdwKoeMis8vxp3ab_VK1OjXE31P5ZEqFfDlBEqC-1zP2u5iQhzjSUSCDbU5xbJ3oJ_i0rxKyTqYomGVZhdZOaFGir1BanR_7pCcVGyofUiAtYOeOogcCU_sKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIY3Wpzvs9lbBRbp-y_fY_ex5MYm9znqhPHVtjR__UDjqrAcinI3ZuBj8mReWt4QZFRaJD9i_GCg3CtRPgs_oOXamVLpQyMmM1nBL1kuVlcYST_RVNLe4brVQXC9ElYmx5qA_tEudjcYXPA2oAYvD4A36wIP1JuwXZkg2zlZPOkiTc2oQsoVmxVCC6cW5gh2qIw_Lq4lQ8LgAlq0wPL7h038Bmi8Camw9g43oyPrVYscQP3dECRp0L1lzvQp1MAUr9tbOxnH1s-kjNtMzNjZSIaSpDTH7oqT2gGQENu4uKOM-Vf-g1nZSNPergZ_2x4y8J3b3M3nHfIr1_swXjZbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jG2u5IoRy14Jbsy_T4fufwbKgDNqvpbHi1yDX1KTj2xpxjVaXSwHzGnD-r7PZvt3hqXMaM27ThyNoAQlsX9ekbN4FR0XHW9GiNCV5X-HgEM3wD6J6DSb8EkkhQpAMq1s2DwjvoZobVHecrZbZRm68LeiV-uIumjf28E4GtZNB54jUDVq78cFsrBv3wLWDeHTFLydzdEpe6CpXyC9HalNd0u-0OTyzgpTn4m37LagN2vgef7sCYU4ziPp8qzjmi0LNUqO8Ti1DdZozNIpZ-LiCuUv0xLA--MV2J-ZzrulBbBvd54KiZ7slvrIknEO1aBflcov2f5XqbONgUJSnMmw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suc0MNU3AsBAy5JXxTlt0KPjI9pTsfNhezpPtXHsXiNUg_CMMkFX1Kr_1-1_th9KKCKrj4b6V5dDwjLztvTrIxbxB7gYyuqMSKNtpjnfukaq75HnV9qcg-HGIyTKgBcXYRxPRmSHZWXm5ivdBWqbdMA-Fu3cEfhHKA3ab5I1ODJgxHg27mas_Ao298b7VbZ-zuCyiu7Nu0eO0MBXDb95Er1nX7saS11iGaFUYot0AZMRohfvLFdGYqAArFsesoU_YnQpo0HK39Yn4FSA6k3xg_cYLsY-ylbkdqgqGeU10BMF4Gxp71VYUt9TM39ZrLEHRFzLxBCaMfMd9elX8D8lzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSzLkRS8w3OxOJwYGOPAOHFHsuwSJ4QkKR7RaZ2zA0EUNgatvkIpE4JKZaV22inxKR20VKjBSMzCnK1r7b8pElI_r93rhxi2i42AhYWtFqgRpK7BPM3L9Bk1bCnw5RZgt24xb2fW1t0hXhsTjwFPzcxkzJIi11nZSmMcazt33yG2EjitWehy1YdpYjWEBSGKzMVxL0pWPgNGNRx9209ak68kfX5epyQKNcUflcVJUMb8itJkzWal9pY6_2xgYFWkeXzgkA9FcxiCXzOcJMdCvGQsGjv3Cpq4rZ78iD2UYKpjo7pAVOZPO-Q83hxK8-ta1c1ddEivp62FU-6IiON65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=sRfz-Wj7njMHyrPIYrVHrqLJpBZVTBakaFi15FtD-0hYKGEZ76ZOtcYQnHPVZQOdURXqhb7sMb0YCt5BxkJ6JeAcqNehawV-TlKzHLSrFZF0ZrC-AdvwK1KbMkQIj7nYNSMo-04cMoBOcgXqWIIVDi0BlCJBhhk6mmXe5Sr_G0xHqN1yPDScgC15xGM_kicbm0GBKccRclQhtlL6UKLmXC71mG1WOvu80vx1uytXzsPB4lovPt_pnxHqRqrRt7sXFcuf8x8fTDQI2l0WovlgSML2TToJJ92PwybUqZZaam8XcbQpy8Q6xpD8XuC2Iq68Bd9DSBCK-Fh9eEV6YQO27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=sRfz-Wj7njMHyrPIYrVHrqLJpBZVTBakaFi15FtD-0hYKGEZ76ZOtcYQnHPVZQOdURXqhb7sMb0YCt5BxkJ6JeAcqNehawV-TlKzHLSrFZF0ZrC-AdvwK1KbMkQIj7nYNSMo-04cMoBOcgXqWIIVDi0BlCJBhhk6mmXe5Sr_G0xHqN1yPDScgC15xGM_kicbm0GBKccRclQhtlL6UKLmXC71mG1WOvu80vx1uytXzsPB4lovPt_pnxHqRqrRt7sXFcuf8x8fTDQI2l0WovlgSML2TToJJ92PwybUqZZaam8XcbQpy8Q6xpD8XuC2Iq68Bd9DSBCK-Fh9eEV6YQO27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzCjJCLOX3tRlNYxDKhsu5_Z290cml_CusiKHAnXxhmvSnV32n1ykIJjZDuZzEteyr7Fnab_mNheWymR_4pp6SCGfouDJvMii3LY4SFM6uagLFUyB_wTHflKXWg6J4xPoJAY0j5qpkqicCYAFVPegmvmg6HHg4fsPaFrBNZmxMMlfir0EwOhkvh9PCAay3X67WfIin5Xt2GDJjFylZ36uRMn66oR-cY8uBIblgl5VVgsw_OZq9q26ji9tD0jZLT4NbzYNMExBsjVvhj5JynkIkFH9sYIbOIOYdluMU4M-WQuLtJTeC3yQkYac-qE0YlkxB_8BINJ9UXzYW8h8y6GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiQTlSuIIuhbGdF-qRHLHxe1MTuK3jRnl5OnD-uEOFzlPpH_1IEM6lP9fleUrftBRW1rTquuMhPoLJlPY4HfBRv_fe6gk-93DBowZzxHrn6f9pU-yn31g1UubcHK_UFYrK2HEYI-_1-LCjzzPbVdC8nH6rxfKObuTjIKFc7wRabiRwH_2Z6mSmyAasd8Ry1C0J2eKnYqKXTtOE7rjA-GdeWFsqlKvLpUWBy2LrQMlAn1j0DoRS9iWzKcx-Ra9GIaz9eEJaDTlqrLwaJ3D1LjV3Ui1sQRyKo8a12UOWYYjdJUpWF4XynSqo8DmD96msidvqkSEf0r7xKg5TXaEAgrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه چند سالیه رویه جدیدی در فوتبال حاکم شده و بعضی تیما دوست دارن بدون مسابقه جام ببرن و حتی فاتح مهم‌ترین عنوان ورزشی در طول یک سال بشن. جالب اینکه درباره عدالت هم صحبت می‌کنن اما در روز روشن چنین ادعایی رو به زبان میارن.
🔻
یک باشگاه میاد به زور و با زیرفشار گذاشتن فدراسیون و لابی کردن، باعث و بانی برگزاری یک تورنمنت سه جانبه میشه و دیگری میگه جام رو به ما بدید! معلومه چکار دارید می‌کنید؟ البته من دلیل این تلاش رو می‌دونم. هزینه‌های بسیار گزاف و چند همتی و خارج از قاعده‌ای انجام شده که برای توجیه آن‌ها باید هرطور شده یک جام بیاوریم حتی اگه تیم‌های شایسته‌تری وجود داشته باشن!
🔻
به هرحال در خیابان منیریه در شکل های مختلف و در سایزهای مختلف زیاده. اگه دوست دارن می‌تونن حتی با هزینه من برای خودشون جام بگیرن و روی پوسترشون بزنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107387" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=v84NZI2_v8s1lwFqsjN2QbUPi4Q3NlBi5LgSkmZkoVP57EkbJPeKYsw1x0Z5meL5Xn3d6OHZp7B6AquE-AW6ZyIvGu9acLUElXHA6zOImL_NulBeJh4z-z-54kVk1S3i51wE1y-QkVpXeJ-cDRuVp5sz46kawdPVmJf83w7ZczycqGeB8GK9ILbs5-UIVmBbdufJ3ocqNqHe-_1cnarq8G6k8aSy-8jo5hgw9wWmGd2fgxMx6k2_updqnlUVo0hQUH8hEPHgkfQEa96zeI1TFFFWhkrk9BpufypT_9Y4MVQRjTO8Hi0ReDqfDh-zptjQW5pXpB6i7dfggw4RsK4daw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=v84NZI2_v8s1lwFqsjN2QbUPi4Q3NlBi5LgSkmZkoVP57EkbJPeKYsw1x0Z5meL5Xn3d6OHZp7B6AquE-AW6ZyIvGu9acLUElXHA6zOImL_NulBeJh4z-z-54kVk1S3i51wE1y-QkVpXeJ-cDRuVp5sz46kawdPVmJf83w7ZczycqGeB8GK9ILbs5-UIVmBbdufJ3ocqNqHe-_1cnarq8G6k8aSy-8jo5hgw9wWmGd2fgxMx6k2_updqnlUVo0hQUH8hEPHgkfQEa96zeI1TFFFWhkrk9BpufypT_9Y4MVQRjTO8Hi0ReDqfDh-zptjQW5pXpB6i7dfggw4RsK4daw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه وحشتناک ووزینیا بهترین گلر جام جهانی مقابل مالی در لیگ ملت ‌های آفریقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107386" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=WCE_bJvc7p4DYRkEzkOQTaMx_h9ki3WOGAWVTvK-Z-7h9sUiyaBwK6VwHghVnj77-RieGUZ092GC95yjpPz_E5TUagPnKIqTDVblaKYcmVwMhSVbJJ1g37kuPgT48DzIN6RyqImy5EJQWF19mXDeNHVAs1icjD_Sq-c_tAXlwAg44jMQL9jY7vHcLlsoEfeTg6Dj3NvAaMBkkn9LhnchqS3ka0hr4dsl8rkCQwX7JAdfaVu6yDogijJoTh5BRNW6Wpx5dF67Ctw7wlYMFyYWwM7VvcSnB4K4escNOAGKKGiluEtlbzaewuZVGJhEPFrW_iB-09ndP6aAUmARnKRLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=WCE_bJvc7p4DYRkEzkOQTaMx_h9ki3WOGAWVTvK-Z-7h9sUiyaBwK6VwHghVnj77-RieGUZ092GC95yjpPz_E5TUagPnKIqTDVblaKYcmVwMhSVbJJ1g37kuPgT48DzIN6RyqImy5EJQWF19mXDeNHVAs1icjD_Sq-c_tAXlwAg44jMQL9jY7vHcLlsoEfeTg6Dj3NvAaMBkkn9LhnchqS3ka0hr4dsl8rkCQwX7JAdfaVu6yDogijJoTh5BRNW6Wpx5dF67Ctw7wlYMFyYWwM7VvcSnB4K4escNOAGKKGiluEtlbzaewuZVGJhEPFrW_iB-09ndP6aAUmARnKRLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی برنامه نداره ...
وقتی حمید استیلی میخواست برای فرهاد مجیدی
در تیم ملی امید دستیار ایرانی بگیره ولی مورد قبولش
قرار نگرفت ، در ادامه به مجیدی میگن چطور مربی ایرانی
برنامه نداره ؟ امیر قلعه نویی رو براش مثال زدن اونم گفت
که اصلا قلعه نویی برنامه ای نداره
حالا برگردیم به مصاحبه کاناوارو سرمربی ازبکستان !
که گفت تاکتیک ایران فقط ضربه آزاد و کرنر هست
چرا قلعه نویی باید ماندگار باشه ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107385" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=El6ocTKvlbC8BH0tMf1nUGgkGKzQAldBZJNloTndsAnL9-w64Uyp0FWANGpTh3-GdN28drW8yo85TrDQR0ABqRv0DWGNOZPtgGPtXKFjtvs-ryi5hX1YIoL1vEF-04cxTGzDDY5Uug2G7iLKDBsGJy_1HCVZ-paDlISzm4lbEaNV57r-k7ppURKs38XDj9ad4bBUYsalLggySlOUYof_ALrpTANHAfXi_0maXOJFAfg754JhtEkxfHCCmrR1y6MAUPXIckdLEqdwRDd2sONQOwLInGPj8mPx7XCg59fB1lxY49175IJM7IgpYMfXuKqTfYQBlGh5tbaoWErVQaQe6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=El6ocTKvlbC8BH0tMf1nUGgkGKzQAldBZJNloTndsAnL9-w64Uyp0FWANGpTh3-GdN28drW8yo85TrDQR0ABqRv0DWGNOZPtgGPtXKFjtvs-ryi5hX1YIoL1vEF-04cxTGzDDY5Uug2G7iLKDBsGJy_1HCVZ-paDlISzm4lbEaNV57r-k7ppURKs38XDj9ad4bBUYsalLggySlOUYof_ALrpTANHAfXi_0maXOJFAfg754JhtEkxfHCCmrR1y6MAUPXIckdLEqdwRDd2sONQOwLInGPj8mPx7XCg59fB1lxY49175IJM7IgpYMfXuKqTfYQBlGh5tbaoWErVQaQe6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
وزیر خزانه‌داری آمریکا: اقتصاد ایران تا دو هفته دیگه نابود می‌شه
چون اونا فقط ۱۵ میلیون بشکه نفت روی آب دارن و بعد از انتقالشون به چین، هیچ‌چیزی براشون نمی‌مونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107384" target="_blank">📅 19:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=X5sf4SjxCAyLeEoDY8TzfomYJG3cJos86oC3tEQzfcKGww7cGzcjjQoAuiU43CApRRrXwfx5bTn5d8Vn9xuIZj5oheFI6EFSZKPAu8sCbboAbx04jVoAdTRfBBm62ejOD2cZn-1MtUXF23F3dLvztyJUGB34xa4yx0julRRAeS8wiXnEG5yqAtoH_nwlEiWdJ2P_GY6CKTulMHDPfu9JuU86juK55vqjxclb1JJkfd-_M5Q7dF9vXrQx_D6w8W4xZT0AqmT9roUwkmCoaiEM9OxT7CvJ0ZJSyKu39wiATvkSYk7AkA8vxujscleKgo8z32A2bAJ8aePTaq-_bHCVK5fXlLIaFtKZCht_Mb3Ej15i078kavI-DH-TIu0BkD3uoD4juggIB8GZu5NW98ch2FAxf6OukuEEXzuGB0vp5uEO7xjux06_qX4GQ0t1x6chJTn2Z8zKproFChrWBr_OoKSolOHtr3MaM3hy6ClyFyGrbL5ner1WtpT5LYcZWg6uuUXi55_72l5-5l0PpE0a88odit6o6jpUszgvnxSudRLE4e9KgT5eVD_16kjjWCQ_2S1Dxqt8PBA9ku66njUS_Xuo8aYUl5BxwKS1NgV-spkitCIx2c42cRUlyOVQeGPklP8eoVr0krQAFNky2jHVtPmL3h0KW3j1A2maTH0lwNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=X5sf4SjxCAyLeEoDY8TzfomYJG3cJos86oC3tEQzfcKGww7cGzcjjQoAuiU43CApRRrXwfx5bTn5d8Vn9xuIZj5oheFI6EFSZKPAu8sCbboAbx04jVoAdTRfBBm62ejOD2cZn-1MtUXF23F3dLvztyJUGB34xa4yx0julRRAeS8wiXnEG5yqAtoH_nwlEiWdJ2P_GY6CKTulMHDPfu9JuU86juK55vqjxclb1JJkfd-_M5Q7dF9vXrQx_D6w8W4xZT0AqmT9roUwkmCoaiEM9OxT7CvJ0ZJSyKu39wiATvkSYk7AkA8vxujscleKgo8z32A2bAJ8aePTaq-_bHCVK5fXlLIaFtKZCht_Mb3Ej15i078kavI-DH-TIu0BkD3uoD4juggIB8GZu5NW98ch2FAxf6OukuEEXzuGB0vp5uEO7xjux06_qX4GQ0t1x6chJTn2Z8zKproFChrWBr_OoKSolOHtr3MaM3hy6ClyFyGrbL5ner1WtpT5LYcZWg6uuUXi55_72l5-5l0PpE0a88odit6o6jpUszgvnxSudRLE4e9KgT5eVD_16kjjWCQ_2S1Dxqt8PBA9ku66njUS_Xuo8aYUl5BxwKS1NgV-spkitCIx2c42cRUlyOVQeGPklP8eoVr0krQAFNky2jHVtPmL3h0KW3j1A2maTH0lwNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
تقلید صدای باحال از گزارشگران مراکز استان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107383" target="_blank">📅 19:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Quej4QBNplaaefDj4HF-VkoFOGfNslVu_8Q-jaIpfHlVjxHoXgw5xBCxzd8mj69L6lMENrcFeQvuXnm19lQat8AA_D0U6Fxg0GQ_gDSelmfCA6okCjpb1OiYLlx2eCwcx1BskKQLbGEH9o6nT05MWyOZFLdmLg3gEKARwPK62J7I36s-3wYB65VKayrrKXbN0Z8FhDfEHika6NlCitWMLAAwTHk59M51DbgU0ZUbrGzYlljSgRRDplM3_kRFlRzVf5bxAxqj-59BFGkHYO7hKZLfgRVkFjpqUeLb331jAA7z0X4Sn6ZrwFFyOKPNAQ_9G3q3fVRpgE_XdIS_7iOLdz5kgwc2na4mOE-m_iOvUASFb5WFQBwgAD1uAW6FvORSH2uR6v2Z2C3cJ8NleKmUa78s-sYUYQ-6wMs3NJVYxQ9Vm1AKWGVq-ypt7HCP2OiJra90W0QP5Xqv2FvgTsaphbg6S0YslmI5ZJzRubILNtn8SxjH372UTanKcbr2YQVSTspIcQPIwgdpUngO27bheA3B5hB1Dtu5PoS6trgoVREcFIvrb-RSUBiwn_EMBgwYZzn2MhoZmpcHgIvab3I8ZiwM8uLtT_-rinfyUSfDejHujhO-p0sphpNpH7m3a5C2wm7jSeJHBP-2sY5k-abWoTYFbxMokObuTp7al2CuuDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Quej4QBNplaaefDj4HF-VkoFOGfNslVu_8Q-jaIpfHlVjxHoXgw5xBCxzd8mj69L6lMENrcFeQvuXnm19lQat8AA_D0U6Fxg0GQ_gDSelmfCA6okCjpb1OiYLlx2eCwcx1BskKQLbGEH9o6nT05MWyOZFLdmLg3gEKARwPK62J7I36s-3wYB65VKayrrKXbN0Z8FhDfEHika6NlCitWMLAAwTHk59M51DbgU0ZUbrGzYlljSgRRDplM3_kRFlRzVf5bxAxqj-59BFGkHYO7hKZLfgRVkFjpqUeLb331jAA7z0X4Sn6ZrwFFyOKPNAQ_9G3q3fVRpgE_XdIS_7iOLdz5kgwc2na4mOE-m_iOvUASFb5WFQBwgAD1uAW6FvORSH2uR6v2Z2C3cJ8NleKmUa78s-sYUYQ-6wMs3NJVYxQ9Vm1AKWGVq-ypt7HCP2OiJra90W0QP5Xqv2FvgTsaphbg6S0YslmI5ZJzRubILNtn8SxjH372UTanKcbr2YQVSTspIcQPIwgdpUngO27bheA3B5hB1Dtu5PoS6trgoVREcFIvrb-RSUBiwn_EMBgwYZzn2MhoZmpcHgIvab3I8ZiwM8uLtT_-rinfyUSfDejHujhO-p0sphpNpH7m3a5C2wm7jSeJHBP-2sY5k-abWoTYFbxMokObuTp7al2CuuDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⚪️
⚽️
چرا تیم امید همیشه ناکام است؟ این ۱۴۰ ثانیه از فرهاد مجیدی را گوش کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107382" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36187cd975.mp4?token=LeuvW0XtIVUeOCislL2dEzh1cEkvFiaIcLxeoLc6ZMdt2XAbv8mDa1J1-d_TRi2eEscLVbBTDg3yW9OMWfp_2LMM-rlOyuqcjerUGRX3RoHKlZ97x3Fr11Gj57zbC9GF6ud_V_FUnNAWtpmfpP-XDx_W7OdGRGbFAsj-WsMNYSTirhJdl0nn5HNe7E9oz8-TrdtRzJE-CbIfwZNzmgtoBMJwQnMT8O_SjVAMsOZauoMKyAuCVDWDrVO1y9Uj_TgbzqiVVNyfDX4I1qTDO0GMc4bbFPVqeAsXPS1AhzskOu93ZEk0kDv1m2n_lNDwbVvNJ_FFk8eorG5UfkDCqO6j8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36187cd975.mp4?token=LeuvW0XtIVUeOCislL2dEzh1cEkvFiaIcLxeoLc6ZMdt2XAbv8mDa1J1-d_TRi2eEscLVbBTDg3yW9OMWfp_2LMM-rlOyuqcjerUGRX3RoHKlZ97x3Fr11Gj57zbC9GF6ud_V_FUnNAWtpmfpP-XDx_W7OdGRGbFAsj-WsMNYSTirhJdl0nn5HNe7E9oz8-TrdtRzJE-CbIfwZNzmgtoBMJwQnMT8O_SjVAMsOZauoMKyAuCVDWDrVO1y9Uj_TgbzqiVVNyfDX4I1qTDO0GMc4bbFPVqeAsXPS1AhzskOu93ZEk0kDv1m2n_lNDwbVvNJ_FFk8eorG5UfkDCqO6j8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
محکومیت ۴۰۰ هزار دلاری استقلال در پرونده کاریله؛ آیا تاجرنیا طبق وعده ای که قبلا روی آنتن زنده تلویزیون داده بود، مطبش را برای پرداخت این جریمه می‌فروشد؟ آیا دیگر اعضای وقت هیات مدیره، طبق گفته تاجرنیا از جیبشان این خسارت تقریبا ۹۳ میلیارد تومانی را می‌پردازند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107379" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=SQ11bz8U95EzMZvbkFaxjkV891o3147Q9vhaeEO5oNPiSCjQsSUM6sIiIfKjIBFnLc_XqTApK5S_iYQrARDXVxkIPR8FL7vsoMQdQUl1b5Cn39Jpi2nq5mDDLYWOfe6EKn7w8apYSUPN-Y8D-cOcBEEwYX2qaUd050JVTuLGIi9znRRv0o5jV17KW5Kdf5CqpB0eqkuwSssSlUKDZRHuq05V-I6TnCAjZimoGHTq2Tk07QC4z8HWwEHVr1VMOFIoFx0NrEon7VYDsw2W5NERh1kBNdb_1jMtuIy805OxqqNYKvWCrfeCmf1doSYVC3gNHaQoGsZesYgUH2arlKDntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=SQ11bz8U95EzMZvbkFaxjkV891o3147Q9vhaeEO5oNPiSCjQsSUM6sIiIfKjIBFnLc_XqTApK5S_iYQrARDXVxkIPR8FL7vsoMQdQUl1b5Cn39Jpi2nq5mDDLYWOfe6EKn7w8apYSUPN-Y8D-cOcBEEwYX2qaUd050JVTuLGIi9znRRv0o5jV17KW5Kdf5CqpB0eqkuwSssSlUKDZRHuq05V-I6TnCAjZimoGHTq2Tk07QC4z8HWwEHVr1VMOFIoFx0NrEon7VYDsw2W5NERh1kBNdb_1jMtuIy805OxqqNYKvWCrfeCmf1doSYVC3gNHaQoGsZesYgUH2arlKDntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درگیری شدید سوبوسلای و بازیکنان حریف در بازی اخیر مجارستان مقابل اوکراین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107378" target="_blank">📅 18:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=WN2SW0wqTaSngq_KF7zCYetTQy3BHq9JhQITrlbIRoc9dabL3h_srONTUDSrL3iI2js9YNGlPCoGk0LW6rQtFGvF1gvdptIOMqglEmtSySFAr1oww-UazUwMFl3R9yjR3hHQYAwp-DMGzs5JMD0BeZIFCO1foZ9A4jHmF3uvwK2rczGONV20WsOovlNBHw1kLDY5loKWvwNPYrTCghKS79MXHfsms2bOWlYJnOvsCXOPeR_c69hUNhBWai1Y4HBHHY79b2s2iFxAesF14wleJy2LrMGo6u8Bds13bj3BL7E241wHAufquzNS2LW7uWJH3_k2DAbHlT0yOjh1lJxVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=WN2SW0wqTaSngq_KF7zCYetTQy3BHq9JhQITrlbIRoc9dabL3h_srONTUDSrL3iI2js9YNGlPCoGk0LW6rQtFGvF1gvdptIOMqglEmtSySFAr1oww-UazUwMFl3R9yjR3hHQYAwp-DMGzs5JMD0BeZIFCO1foZ9A4jHmF3uvwK2rczGONV20WsOovlNBHw1kLDY5loKWvwNPYrTCghKS79MXHfsms2bOWlYJnOvsCXOPeR_c69hUNhBWai1Y4HBHHY79b2s2iFxAesF14wleJy2LrMGo6u8Bds13bj3BL7E241wHAufquzNS2LW7uWJH3_k2DAbHlT0yOjh1lJxVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گریه‌های آرش‌افشین بازیکن سابق استقلال: نتونستم پول خوبی از فوتبال در بیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107377" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=eyMyLy5-Gu5PX_ppCryMuzjzWwxIeSi4ecSqyrJUeX-OVC4LYWMQVJ_eOxQrpw0oATY8BzaXTZWADdhzmNo8h-RYmhDSfZfFwKPJslRnrAQdmND3pcxcA3kREZjX8_RVq3QA3D7QZ25qGJTN8hi306-7KcS1VOmgI0GuRoVms15JEoIpMiIMDxkhmydl0y2ZXcRRNou5BhLfwfWnC_hSI7xRCOvC8cxigN6L8V-3nX_XWNK_rjrFIe3cUbmj5zn56My7yp3k9eJ5JCVNKFvAv0pkPxAlpeVeg2yiUhcd_APEpF1XON3xHX0d5zeXAC2c6QkKLyGZkQK0zLq-yPF79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=eyMyLy5-Gu5PX_ppCryMuzjzWwxIeSi4ecSqyrJUeX-OVC4LYWMQVJ_eOxQrpw0oATY8BzaXTZWADdhzmNo8h-RYmhDSfZfFwKPJslRnrAQdmND3pcxcA3kREZjX8_RVq3QA3D7QZ25qGJTN8hi306-7KcS1VOmgI0GuRoVms15JEoIpMiIMDxkhmydl0y2ZXcRRNou5BhLfwfWnC_hSI7xRCOvC8cxigN6L8V-3nX_XWNK_rjrFIe3cUbmj5zn56My7yp3k9eJ5JCVNKFvAv0pkPxAlpeVeg2yiUhcd_APEpF1XON3xHX0d5zeXAC2c6QkKLyGZkQK0zLq-yPF79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
افشاگری حجت‌کریمی عضو هیئت رئیسه فدراسیون: قلعه‌نویی قرارداد ۴ ساله می‌خواست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107376" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=T2oDmf279WT69tOcFOP5CdYY0pxS3QyruEKhpQMDjqlvQ7JVgFgpgKyiy2PfkCptfPmvQi5WxJYVAjKBNhnf1phCqcWUS3DF90qELsgq0k9qlGzztsb9G5CJkRRTKwtyLqxqZq2rpAr_UKGd8hnOPsiR12tsWBf76hWPhBxRI4a9mNnbqTtWZ2ipebFdf8jmJo2qq1vtGB3rMplwdbTcch5O6iq8k7DOLOUsaYjekBYSLys1nHSItPxG86Pi-rYI561un33fxmKJRJafo7fVdU_jBOtxONyJOAaByeWPHIy6tsbVQuHqSsu3Q2UDSbyXdNfLPpmZzDCjYG9whoo6fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=T2oDmf279WT69tOcFOP5CdYY0pxS3QyruEKhpQMDjqlvQ7JVgFgpgKyiy2PfkCptfPmvQi5WxJYVAjKBNhnf1phCqcWUS3DF90qELsgq0k9qlGzztsb9G5CJkRRTKwtyLqxqZq2rpAr_UKGd8hnOPsiR12tsWBf76hWPhBxRI4a9mNnbqTtWZ2ipebFdf8jmJo2qq1vtGB3rMplwdbTcch5O6iq8k7DOLOUsaYjekBYSLys1nHSItPxG86Pi-rYI561un33fxmKJRJafo7fVdU_jBOtxONyJOAaByeWPHIy6tsbVQuHqSsu3Q2UDSbyXdNfLPpmZzDCjYG9whoo6fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=t_ohtE601aRld0cTOW35WN86bJddfYCp2KMzZZV7PqBzLWa7srxVp5UR-PYLW3cTvYwUCwGuJkKB4aDLaSMb6H8w08PGx1UGPKd_FvpKKfWnnJ9QY4HcDjkXsPOBB8u1gvGY7j9IGqSLQLHdPZ-Ym9VxJvucZRvmT6k4rFMKspMSpPLeRGGKqFLAYnb4HLMxolH1w_YX5rvhxQFHvnl_MFNNT2IaLGh3tA2K3YOL1WAvV6uC4ub1BkSdjqHOxby4c9GC0yWNRURfAQrPSDQoZnGArWfTHaeQPgH2R4ae5ZSAGbX8bucvQCQxgvUt7F0OKBLYMArKJ0t7dmlWesXDOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=t_ohtE601aRld0cTOW35WN86bJddfYCp2KMzZZV7PqBzLWa7srxVp5UR-PYLW3cTvYwUCwGuJkKB4aDLaSMb6H8w08PGx1UGPKd_FvpKKfWnnJ9QY4HcDjkXsPOBB8u1gvGY7j9IGqSLQLHdPZ-Ym9VxJvucZRvmT6k4rFMKspMSpPLeRGGKqFLAYnb4HLMxolH1w_YX5rvhxQFHvnl_MFNNT2IaLGh3tA2K3YOL1WAvV6uC4ub1BkSdjqHOxby4c9GC0yWNRURfAQrPSDQoZnGArWfTHaeQPgH2R4ae5ZSAGbX8bucvQCQxgvUt7F0OKBLYMArKJ0t7dmlWesXDOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHaqVwdZo3IqgD4oFQyLOjTx-Vawf_bLNWebcUbhAzdhmbziYwKBUJKGbmOx04tWw6PjQ63EOiAL3EVLGI7ojXt62upZKWkTNfzk57Wr8U7UBFt-N25WLgfGR4r2hHOAzJKJuKZlkft8o-b56l4QYCWFULV7AZnhHVYphbLKqe3kDz7T6KgJUO0AWd-o0oBh4S1KuTF7vX4FiyUmnH_Eo9i6DxOsEy1N7nKELvajTPToklPW2ASf_jmE6MYAAwMlaC2OyMHTJqMPavOyKXws4Y3LIM6VMTUtbKqKfdNDxJMjccBAQtQSp-LErVUPgzUsnhlsN4s0gl_GLPxCCYvpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گاتزتا | روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتا قرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی هم یه قرارداد با الجزیره امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو!
هردوی این باشگاه ها متعلق به شیخ منصوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107373" target="_blank">📅 15:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=WzY7SzkXoBKDQNe3Dyfk901MvdNccC9qnLSMT5lL4xXiIOcPIfgbyvK8l7qoj9pO9Kf6NsonQcDLwR_ncveiVIg9ZD55GTvddhWFO0ys2bgR1zF1HbeMiscv5AJlV_Pqd8XivA0msE8k0gBVstRrFx9TxGVbxTsBBtln1ZRAA8WwgQTwgtx5jRRBmwcvOtRHSO9yj2zj5mSbwFtjulgblv3UQqLd5-Sg5Ed__uHCS105agXqztyFEFIpVUEkkRV4d4KX90O3OtpqszF45QvBhI1SOyazsDc-tzcvSaLlagtOebiYjOfzcIihYgiMftfbKeuKN6-zgR1RWEd3QI8kUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=WzY7SzkXoBKDQNe3Dyfk901MvdNccC9qnLSMT5lL4xXiIOcPIfgbyvK8l7qoj9pO9Kf6NsonQcDLwR_ncveiVIg9ZD55GTvddhWFO0ys2bgR1zF1HbeMiscv5AJlV_Pqd8XivA0msE8k0gBVstRrFx9TxGVbxTsBBtln1ZRAA8WwgQTwgtx5jRRBmwcvOtRHSO9yj2zj5mSbwFtjulgblv3UQqLd5-Sg5Ed__uHCS105agXqztyFEFIpVUEkkRV4d4KX90O3OtpqszF45QvBhI1SOyazsDc-tzcvSaLlagtOebiYjOfzcIihYgiMftfbKeuKN6-zgR1RWEd3QI8kUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یامال: این توپ طلای ما رو بدید بریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107372" target="_blank">📅 15:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=TJaMGhuMOyCXwV8Ldc2U_hBckv1yLtYdNYklngNOEbo59zYCSc_kwfSA_t2-tbqIzuzrGfMOFK7Osk8l2BQqBzB42CvHGZaGQ9_uao20r-Bxijorbz33dU2w8gfNkaWdQ5EuqDbkUFbshPhdDBo4pztTfvtIuqX1bCkKhNzGAqxfHTSNDK6kKH28nGGI5RLTREuctpA4f8e6_6ZvOWdBS1h0J2yXdOCoafDbXOQgdaiRoB-8R2CE5G3v8R4z57-l4x8vIgOkRRntR8C7tcDxgD4ALz4n6EtjOkzan5IfdT04ekM5WB9UeE5__9FugTyvi7nuj1JbnAMxQ45jg-B8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=TJaMGhuMOyCXwV8Ldc2U_hBckv1yLtYdNYklngNOEbo59zYCSc_kwfSA_t2-tbqIzuzrGfMOFK7Osk8l2BQqBzB42CvHGZaGQ9_uao20r-Bxijorbz33dU2w8gfNkaWdQ5EuqDbkUFbshPhdDBo4pztTfvtIuqX1bCkKhNzGAqxfHTSNDK6kKH28nGGI5RLTREuctpA4f8e6_6ZvOWdBS1h0J2yXdOCoafDbXOQgdaiRoB-8R2CE5G3v8R4z57-l4x8vIgOkRRntR8C7tcDxgD4ALz4n6EtjOkzan5IfdT04ekM5WB9UeE5__9FugTyvi7nuj1JbnAMxQ45jg-B8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پنالتی که هری‌کین در تقابل مستقیم با یامال از دست داد تا سرنوشت بازی دیشب تغییر کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107371" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hD0WhZYeNxGgwYSY1HBuNW2mV4zAcx4QYnbc0ExRFu2jeiQusY_EmRh85IYP5uXvKNfkkIzp5akcHHY_xc1SLXfWlJBTLVXcIfy62WVrJ5CSN4Q-nXd75Vv4YjGmJ64yZfQwc0yI11rKu3RZBTvQyONLmyOk6XvZ1QDNM8sfhHSNhjRcjriP_I_EsAnileAZh5Re1gV67ivQHEStVSSupn6efXjgVhfIusjD5ooZ9Sndh7d_8hCMTZV3v4MxPf_FXjQTDe5RpKPhJV4v_6Mg5zKbCHnPZsPeHsGyV5tEucezqD9JJ4z5QdEBM3Sx5HUph8oxN63hrFaqqlyLvjvhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریشب نبرد منتخب آفریقا و منتخب ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107370" target="_blank">📅 14:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIO0gLGSSU2FqyNtPl60iTr-LOpD_R69BA4hk9qW1AgT4v9Tiy92hzYE0k6cu6n2FShzh3aX_PRPC7dN_430c9cceuUybJta65sDunkTwDlXzEmUXQR5wf4jF51hA5sjYo6Y5Linyt74SVup-mOhzsz_J5d-BrLL691pjO-Y5JyOm6DIR83qOI07aKP9ZLBmC7KvdfghGQkDXUeWI5apfOW6EtumiKWKLHHN4jVGPgk8kzLjJXrLvfmg7q5u5UPUVWECrt2peOPgXO-ULG0NUZvcH_HSiQjRWcp7Y2vuAyRMTLU8c_x6Wfy92fJAchTlKxH5ULRZiDs_SY3uYKW2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇪🇸
برخی رسانه‌های اسپانیایی گفتن که اگه سیتی محکوم بشه،‌ ممکنه هالند درخواست جدایی بده و با توجه به نیاز بارسا به مهاجم نوک، این بازیکن گزینه اول کاتالان‌ها میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107369" target="_blank">📅 14:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuisZWIfiVo4aMLoIg2lX8C3Ajs95jeTK3drHKD0bTg8GAqCTzWC3m8pntb-24iISeWIrMISFPI2xOlkxfIYrBDv4VsIdRfIDyvjXRKucBeUOXufBK1UIIE77P2dEGUCnQUcrNihB2Nwv5cFeo1DpSemAHInrzDJmhs0L9JJ74eD147E_9WLuTEnZHzkQPmCruHJ1hbhhw0J8tN31MzPa2Uii7GaV1-Zrr6UKTGANkU5p6tVM3FwDedFeNtdNFoiKEpL1rbzrV9TUCqYdFzuVexSATb2NsC6419TBUsAQfi9o1Oo-qR5X0aJGqC2k3N37qgFLWRxv-2AdGfBSZDoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇧🇷
نتایج ضعیف برزیل آنجلوتی در مقایسه با سرمربی اسبق سلسائو در بازی‌های دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107368" target="_blank">📅 13:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRqAogwzBHUYL2KMHPSBYlv6pt7TE27qV7Aq7uZKxG78xTHNJMwQ4QvAVmz9UP8pLn7SoMAUQkcwuo8Mkc7ltHceW6C0z-BhDthDdvASsDM90MtzC1RfhULBw1ziMZCbGXPMYzqgv5XuMr6joA0OfRhx-LcKY0cC1jrzenKqb7LweTAuF5z4BItr42YE31qmuMqIFrGaoOAlqGRY7ZvhOhaTh78YAi8Bxg4S46e-fT3X_IYS-WFm8oryO2pHW1YgTsBGlC_zdavIuWGbnSADrUbg2LAv3ny5ApO_kb0eJtDVUh487mydGm6-Y3f_jUrypDEOktfPB4jlRkzmDRcfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
اعتراض تند عضو هیئت مدیره پرسپولیس به شایعه قهرمانی فصل‌گذشته استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107367" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=W0ZDTQ-7Diug83nLuKmubwViixcUhrD627u_9nPod_Z5Y9C8s6oQEoE_Ipgpy-2gtiQt12lQWr0at8F0rjDWoGQG7FfKJ11PZ5gGfUAN_Ru_o_1jLPWHTh9Vws1BwKQLXMRaREhSIFWv-vd8aDDya5V_Ew_RvOvIbrcrKcaXCfMISTMx5Bh8rIKdcrxbnpEp7EWigp9L2X_FTfbiRyBXKt7oVI_CIJlklEI1IuR7SIbiUL6tOwLJ7Y7xcU1WtTLG2PXzd7BRrVNOfEMbJSBVeQ64gcSx1KEWdtFXdtQRoU12skLFk0bh5E1yBuRBM6wRG_4JeCNrdVZDumCgEcgD30xvyviee_K-3OZkThGNMA9MU9d8H2_2kD7QQm3vSBzaXTFnPVcR7R9vNO4DYMqBTQntZOlg19XkA-zs1I9NGBsIoxh8blvtIgzLcHYQJuugzlaiZkKYiEwQbqlGEfr9MLe7_fwrMoagJgo5GOKlkJQJ9OayO2RBszRFKrYQ-8PeJ0ANEnhCD2ZcGyqKebjPYpGJttKUgtrT9y5ijnQ3AUFxJWmChEWIXGdzaZG9pu_8BxVhQRQwnfu4z-NMdmM6lqbG0s4-6vvgUcmDtZQpKZ3yXT9WrpAGroYJm5XF7MZRNKI4gDHAz8I93U8dIhjdrk3jMGXQyiDBmx8eiHxjzE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=W0ZDTQ-7Diug83nLuKmubwViixcUhrD627u_9nPod_Z5Y9C8s6oQEoE_Ipgpy-2gtiQt12lQWr0at8F0rjDWoGQG7FfKJ11PZ5gGfUAN_Ru_o_1jLPWHTh9Vws1BwKQLXMRaREhSIFWv-vd8aDDya5V_Ew_RvOvIbrcrKcaXCfMISTMx5Bh8rIKdcrxbnpEp7EWigp9L2X_FTfbiRyBXKt7oVI_CIJlklEI1IuR7SIbiUL6tOwLJ7Y7xcU1WtTLG2PXzd7BRrVNOfEMbJSBVeQ64gcSx1KEWdtFXdtQRoU12skLFk0bh5E1yBuRBM6wRG_4JeCNrdVZDumCgEcgD30xvyviee_K-3OZkThGNMA9MU9d8H2_2kD7QQm3vSBzaXTFnPVcR7R9vNO4DYMqBTQntZOlg19XkA-zs1I9NGBsIoxh8blvtIgzLcHYQJuugzlaiZkKYiEwQbqlGEfr9MLe7_fwrMoagJgo5GOKlkJQJ9OayO2RBszRFKrYQ-8PeJ0ANEnhCD2ZcGyqKebjPYpGJttKUgtrT9y5ijnQ3AUFxJWmChEWIXGdzaZG9pu_8BxVhQRQwnfu4z-NMdmM6lqbG0s4-6vvgUcmDtZQpKZ3yXT9WrpAGroYJm5XF7MZRNKI4gDHAz8I93U8dIhjdrk3jMGXQyiDBmx8eiHxjzE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: بیرانوند برای آمدن به استقلال پیام فرستاده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107366" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1582f31111.mp4?token=H7Iz_qHvAi4ML2P586e9x1N9noblwEdm6Icr3kbcX4-GKWd-gb4lV8TMhKYSNIy0t6LRKziSX36SbtwXWxqiDugNbhX-8WtLApDKLz7SHVR_mfKC8A9zpiJ5679IjWHr-QJarq0-hR0NzFeXAGLbaTeAkU9uNo4KDw2NeISiDd0GiKFcvEj4reloO3KCX5pK_ZzbaE4tUIItXCfatw31e2NrpMUVQ3396RRpUfznVWbQoUG0Q3zfxVZSA61q1S71hhQfWFx7QScNt6J-Z3esHLCazsoGalP5Fop4IheqLDF4xwDeGzDFcpA2qtcpsFWkJfH4Rjmt3C4sAZhzNy9JNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1582f31111.mp4?token=H7Iz_qHvAi4ML2P586e9x1N9noblwEdm6Icr3kbcX4-GKWd-gb4lV8TMhKYSNIy0t6LRKziSX36SbtwXWxqiDugNbhX-8WtLApDKLz7SHVR_mfKC8A9zpiJ5679IjWHr-QJarq0-hR0NzFeXAGLbaTeAkU9uNo4KDw2NeISiDd0GiKFcvEj4reloO3KCX5pK_ZzbaE4tUIItXCfatw31e2NrpMUVQ3396RRpUfznVWbQoUG0Q3zfxVZSA61q1S71hhQfWFx7QScNt6J-Z3esHLCazsoGalP5Fop4IheqLDF4xwDeGzDFcpA2qtcpsFWkJfH4Rjmt3C4sAZhzNy9JNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که بازیکنان آلمان از یورگن‌کلوپ حساب میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107365" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=eFeH7scxunDHH70LCUz3_5UPJF9HSwkYG1w6LI-JSbd8UQKc63msrCWBY2p1_p-UaoxZKymJw4xRb75XzJogkho0oPxV1LVQGf26CS0kTce1f_Mo1wVol2sD4CfKQFevFTCmDzXg-xh0_4pBvvqOr5WsPM1g-UYQ8pN1wfM9t8SyGNUKqeUSA3ScaS0gK6ANSQti3Ru9GsW_5G916vqiv5hStY5ujs8wzvN8Y-Nj1bDNX-WXxPAW5LW_TsdDnUgTi1fUAda3oW3Rrn_8u5-1BjWPmK_gAiIK7cE1yS6qZcacjWxz99gazAure1MmoriG6V8FW1NhJ4Ftg2-eD8YlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=eFeH7scxunDHH70LCUz3_5UPJF9HSwkYG1w6LI-JSbd8UQKc63msrCWBY2p1_p-UaoxZKymJw4xRb75XzJogkho0oPxV1LVQGf26CS0kTce1f_Mo1wVol2sD4CfKQFevFTCmDzXg-xh0_4pBvvqOr5WsPM1g-UYQ8pN1wfM9t8SyGNUKqeUSA3ScaS0gK6ANSQti3Ru9GsW_5G916vqiv5hStY5ujs8wzvN8Y-Nj1bDNX-WXxPAW5LW_TsdDnUgTi1fUAda3oW3Rrn_8u5-1BjWPmK_gAiIK7cE1yS6qZcacjWxz99gazAure1MmoriG6V8FW1NhJ4Ftg2-eD8YlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
تاجرنیا: در پرونده توهین دسته‌جمعی هواداران پرسپولیس می‌خواستیم به دادگاه CAS شکایت کنیم که شخص آقای مهدی تاج به من زنگ زد و گفت از پرسپولیس شکایت نکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107364" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMg1QOORnFsvjglTQFJ6i7WKhgxRPYuNdSmstQslSibWcjqzssoPXdDskaS3GPJf4cRcU8kwozoz2CETAQIJhCye2OYO4LBanYegc1pTW59JYtA4gXTjmpN-NDIV1Q7Nhn4xi8hKs4ndRTnztJdi5SlwRX6_Hab2XG0ohaJ-Ru5VlXsdFxiK2Qyd5XrTPXdJEfj0Smzv2XRkCQ9iAufrgHiNZFECugg46goOv0IItLDwh-6WOzEtQBs4FtG7OfrLaA98Mnm7iT0Bq-Ih97AQYGY8aYWutV5T2aWB8KOlzy46shNYNupISVIPie14JDrgljIPeCPNG0H7fkkMHUUb4X6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMg1QOORnFsvjglTQFJ6i7WKhgxRPYuNdSmstQslSibWcjqzssoPXdDskaS3GPJf4cRcU8kwozoz2CETAQIJhCye2OYO4LBanYegc1pTW59JYtA4gXTjmpN-NDIV1Q7Nhn4xi8hKs4ndRTnztJdi5SlwRX6_Hab2XG0ohaJ-Ru5VlXsdFxiK2Qyd5XrTPXdJEfj0Smzv2XRkCQ9iAufrgHiNZFECugg46goOv0IItLDwh-6WOzEtQBs4FtG7OfrLaA98Mnm7iT0Bq-Ih97AQYGY8aYWutV5T2aWB8KOlzy46shNYNupISVIPie14JDrgljIPeCPNG0H7fkkMHUUb4X6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌های زده شده با ضربه‌سر رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107361" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vClxZVqJLwpmNKXAM4Jhqeq-SHSqmG_szkdhLTHDJDsUeTnlBLwGz9PTPSzkpdRLtu0yXQpp2cK7MpSrcvziX_NpGv7NKxlYlflm_E32n9X6yP7jlfXr6Ku_ebjcIgMoQ_gcSd6Y7ZKPD2bMAyoA_PhI71e-Fv8_CnycwMNSUz5z9ReAgaQu6Wd3maeXTQH4ZQiGnSFME4MSHh5h8A-y101XqCB0lhEXxQm4gSnNyuYa7GJccdDPOWiYVitzdDP8jS7YDDVAswdwQgZfghm-vDfqZoPT8uUxkjeubLeh9PZMGYPk9QDCOyGlt9heamxC46rm-bk1IVZf_27Wfe5b6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107360" target="_blank">📅 11:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS78iIb2Emt-uB95JTUZ8NGJ-a8V65mxnHzXP_xj-PBf29MzsU9SQQXL499w8qmvu5ezr9DeflKM4HxJ3PZTzCx7KolBYxdAPdsIH1-Juq2IYHHBV_8XQaLc4UfmJa6srDvS9KKiquMUukcxdv2OBbEBHlxbqKWWMPppzGO3R-jg4o-GJ1VnksZURztE2jENHRlvjlj6_H0C3H0-0Fs8XbY3NrfadK8idlRRl9orBgzSTlgohl2tg8FuksYML_qjs_fc4ty2BMf8iF59TueDYLELtx1fatPTX7fZGY3RF9XO2o8c-2TbWwoER40CfUvw7q-N8V8MA_mpy86DLgH77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لیست محبوبان و مغضوبان امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107359" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107358">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184858d60e.mp4?token=lpRLd2xumN8GkcDDJODvjwuhrvOq-n37ZbtTPnhzuxkiGqyWbj5J0CCQ-BGethzCvaqH4C3UDo_8-HUJwUlCWSa5RVV3Eqj5wvYbwduHWezhFkU1rPi-aP9AWya48J5mD32wItO6JaQn0s8QO1as3kCGiqHz7XXvlNI1nIdi7_85nMr2n_i3j66x13LkPd7LDgnyjXfEC70-mejaEOQkWuTmziO-oWsNlNcTgJNGimA6k_pKQUKIY3C9y5b6nN2e08dlBKF5hc8vb_UZR4gd4ChX-Wv42zMsfB85TXbhSqpAaUiyuUxdnGE3Zwmd0GAFBnlJ-Wig2AtPsV40W91kljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184858d60e.mp4?token=lpRLd2xumN8GkcDDJODvjwuhrvOq-n37ZbtTPnhzuxkiGqyWbj5J0CCQ-BGethzCvaqH4C3UDo_8-HUJwUlCWSa5RVV3Eqj5wvYbwduHWezhFkU1rPi-aP9AWya48J5mD32wItO6JaQn0s8QO1as3kCGiqHz7XXvlNI1nIdi7_85nMr2n_i3j66x13LkPd7LDgnyjXfEC70-mejaEOQkWuTmziO-oWsNlNcTgJNGimA6k_pKQUKIY3C9y5b6nN2e08dlBKF5hc8vb_UZR4gd4ChX-Wv42zMsfB85TXbhSqpAaUiyuUxdnGE3Zwmd0GAFBnlJ-Wig2AtPsV40W91kljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به‌مناسبت عملکرد قلعه‌نویی یادی کنیم از این افشاگری تاریخی محمد مایلی‌کهن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107358" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
