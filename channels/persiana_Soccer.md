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
<img src="https://cdn4.telesco.pe/file/ssDHd6s_djXWaajl1LAI4_MlYBwQRQj0VEKv7ISYDGdPUG6qgk9Lgai81jzGsn_Pb1R9Y5V1l9dcjbxKBOVkHd5XNfBA2vDtGD-hlYylTk42MVg529VS-JocyhaLU9j_0EHoIrYF1FIwJwuZC0JEKAeKI6G6UZ0zHGsK5532HrenFI8lvDgjR1sX8nYuRjvRjQU7BnpP5YY6uzNFcqY0oldsiJm1uSQp2X4ZGnCp3-nk7EVeHpRMkleqKvbr6p2S1xFTthq0X7pUeBQmNy5fnzlUpn2Ez5_ak_9SBPQLAndK0AcDOVYRD1p9XpIjLtwcvP-Yaz2uITSF4YrFftZlYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPs8G2Yq7HRDTeNSdYLy4scQRUwWLWgpfMDlcZaeTkNqyOI5ZmovhashKfPh912SaPTN5Tt4ITK8JJvXpmvsQ73k-aYySkGEyM6VKHqY3rlNYOUkekU9HQ4cgqet92V-ceBIG1CQqFCA0Eh-MBK2bJRidO_Z-MRMhhXsJ0UHMaQPDOPyXQIJ6aOnjoSrMbOY0JJI8Y0VXOWPMFQE6Ws6tU5YxJR5wOmQDnBOnjpeHzfxImpH6Z8jK1kk8xjGNlfO15IfQ1C_VayY1KAMgFMtkXoIwTwriLukFBjNCWhGvYow69v4owWqbTNAd5LyvUzP9ObYKMtUBNF_sDRH98Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gltS5vDvv3q26xpnaIgcg4vx7_2JMquWe50zlwzIm_vVm45rdAbMPeXqJSyQ-FPg19tj_yGV-cvXra45dLxfDs8CVBmoTlKSbtcCC2oCkKOz0PhDOvaL0xFalS4zay8ohzg_ZZ4j_F1WxTVl7EY3Aa4HoTDHHr_UdZhTpPJHYyV-t5eA91Lf7LCopOHj_ZNs1yNDF9_HcSnFoxPCCvZPJbcemeOSAdIFTlMAMAMhlzVcQwNk_PmuIrKhY8qaJcTe0x8VWXG_0dLGJthf_Ov3-0uk9FGn-xs9BK4TBv0jheKEmBAMJ43UgB8_KdtBb4jVEtmv4nAOHqWE9ivo8Te73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8lU2ZwNTPwqTiVSFe2tZlPiZoRtNesbp8vsTKCNLwb2Hi7bnNyBnHKAm4GEfQVncoy3wHB3G5H_G2Q_PfIc3HtqSWHGN9ToekESWk4oJGb-e27QfwwX55NEJodoHg0PvJQLST6jL7mIwdnDd6mijFb9tAwwxoqzYhUgj1e1CUeNNBGADOpdrWCi7ZTN9dXKp8SDOnpeNy9tCwrfLQdSYL_WLeGJjWS6GF-1X7r9uCO2pW_Cv_IdGn13IC5YVYn-XNrlRzj9sOvVl00xw_vpfKIjmjCyvv1HL0WdLzvXU3Pw7cxq1fvu9CdR9Qs-HnGtSFi7G7S0FvbnqpadD3pfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axVROMCD8NeKUqK02xMFX6nVwyTZWnKpX5k2D2VQlbIgMju2dNVWXsNWD5hfTnYbQ-pEQASbSGZY23xO_Zfw236Hi0GdmL0V36VD4xVtZdaMi7qQ4iEw-gOZxqxV3Uc4n_VQ3xC0fIBgbjb0ugduzRpRYApW-8rIGKtcKsgvyvTJoUjGrw-gti2q75K1yY4e5Pd68lD1UhOTSyEasJn861ghCBWsfM3XQUK7v8itWrzGVFulG3fxkbPMimxw_kt0ictOJWhtzubwiREvCcC9lsiwiLIpPQ5Rb30UepqntQnyQHEzEPr1HzQTAdgjr6mcO1Av7hxl8f6XYPfa9uNIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWgGzQMvpHTfOPmyyoH3X8f2GywVEyL8vIzg4hjgPzaJARPJpFQWRzjaJXR6N2qC2I0sxW2T2FVH97GI4cdyKAXEOb5keNRt6x6Z3jkryr65E-ax-lLo7fOWypCWI6lBasgfsv_5wb5yPMBX6-6_2DxaxZcSEoDqxB1ucpH4TiMdvmyLfGLk8EJkvONJhGtMsi4Zn5idBCAA7TiBltnN5qNpwzmnCpUGrbsn1c26Evm_PeJOgtdwe2Czrd3-6GMAeUVzceJ6MG9Q1skxBonlz15tNx7mOaxV6UDyUzw_2RTfHo59TYuhpEARjk7BjEYOFbvEqXQFbOgKFkSbbJ33GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=kr4V1TIjMvUARbfyNyk0oQCF9o2zyyNRxVXvnUfsxxCP8Bu6BxQyHoM0mjXdissvFdTimmbenptIdQvRbe_D6qlHvnQtvWDSRDTvr2fkvzX_fQ3ciXfd8JiwEXdo_gmvLoEApiK2oUj5VHxuF7tsFP_hzv9VOh4JfFncUjtiKNiCWtmQhQYK-CvV8e61Ke_AuwnUbKUOSDZerg8wyIs0Q4P8W2KYE1sWM1hi7GdPClFKJvj8fO9RQx-K79f_MmMetiLZEH13pdaenzf8IAkAuWudfrwrOLB2U_ULzk3gRRSm7MRQSQ_Me2qGC-zglBW7Wmwzoyy194rzR955eulm7ywzbbQMMtG6A3JL01fIPx9kjw_PR0df4bdyjb2FOl7faWhU_Iy8gYZd63AUGKUErYwjQhO5zLAjtAo-aEG6iNqlaIcJom-p7CS9ipQaGiy8r1M3MkkKPuIJINcLO0DGJnMGSo_Tnp52OeT3NgUbKKmSTlVRef1xfHkYtozXP0pELsEmp1E_qoe1UCn8jD6lc_ofoGEzjyIuAekvhNEjXrnVV3WfX5_85sQ9Nag2mREGMdp0WWdfohrRwxSMj4lKS9oWIm5y8yFyVtUBXJpV2vwG8VE9is7o87Da5zbSi2U2aINyHK04AT2l6SN0XrEJrKNW_xeHlK2FGMGxHeEQUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=kr4V1TIjMvUARbfyNyk0oQCF9o2zyyNRxVXvnUfsxxCP8Bu6BxQyHoM0mjXdissvFdTimmbenptIdQvRbe_D6qlHvnQtvWDSRDTvr2fkvzX_fQ3ciXfd8JiwEXdo_gmvLoEApiK2oUj5VHxuF7tsFP_hzv9VOh4JfFncUjtiKNiCWtmQhQYK-CvV8e61Ke_AuwnUbKUOSDZerg8wyIs0Q4P8W2KYE1sWM1hi7GdPClFKJvj8fO9RQx-K79f_MmMetiLZEH13pdaenzf8IAkAuWudfrwrOLB2U_ULzk3gRRSm7MRQSQ_Me2qGC-zglBW7Wmwzoyy194rzR955eulm7ywzbbQMMtG6A3JL01fIPx9kjw_PR0df4bdyjb2FOl7faWhU_Iy8gYZd63AUGKUErYwjQhO5zLAjtAo-aEG6iNqlaIcJom-p7CS9ipQaGiy8r1M3MkkKPuIJINcLO0DGJnMGSo_Tnp52OeT3NgUbKKmSTlVRef1xfHkYtozXP0pELsEmp1E_qoe1UCn8jD6lc_ofoGEzjyIuAekvhNEjXrnVV3WfX5_85sQ9Nag2mREGMdp0WWdfohrRwxSMj4lKS9oWIm5y8yFyVtUBXJpV2vwG8VE9is7o87Da5zbSi2U2aINyHK04AT2l6SN0XrEJrKNW_xeHlK2FGMGxHeEQUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=IqPA8TVEx6g-783o2d3-F213lbR9-U0WnXtkvdXd4HXWCzMbCp_gtznwRKWYfZ0eVv0xY8OW3l6bX6rsCsN0jVA4capsZWh_-OZGW3ZzH3OA29Set4oR9xshZgxpo8OpLBYmEGxymOtLbdv5MUTIf18rjHhQTPUNGMC0hwCTLxWL1WLNBV7liWM4_VCbsvxKJW4y9ae0KFKSHXweLcvlgdRjUcWdG5dLD4ALZorOUqlssIorKNih1eorYjbEmk2oZNHOl960Fh-8yM7PBuy2cV_emFrdkhYL6nnnUdX3VDs-VXvke6l61sFUuFNY8gXHbPnUEiROZsMZaWMvXsIyKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=IqPA8TVEx6g-783o2d3-F213lbR9-U0WnXtkvdXd4HXWCzMbCp_gtznwRKWYfZ0eVv0xY8OW3l6bX6rsCsN0jVA4capsZWh_-OZGW3ZzH3OA29Set4oR9xshZgxpo8OpLBYmEGxymOtLbdv5MUTIf18rjHhQTPUNGMC0hwCTLxWL1WLNBV7liWM4_VCbsvxKJW4y9ae0KFKSHXweLcvlgdRjUcWdG5dLD4ALZorOUqlssIorKNih1eorYjbEmk2oZNHOl960Fh-8yM7PBuy2cV_emFrdkhYL6nnnUdX3VDs-VXvke6l61sFUuFNY8gXHbPnUEiROZsMZaWMvXsIyKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23333" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vidXV_BxCLVUTCnTA8QAw3M3oBtgO1SXojPrt-nAuWhoF7qoPJtVIeAI-wTuO-NmWWeGCNQagzPTYI_7Yzr6bX0VQRZ3HT1rivGjkfES4hgts1xktKtIISsmXHGnaocK27PrUc79kKpRsdf0JKf__Hic4kAnMv2al86e3HrJ6DrjpPUJb72WGCQCx7leFfdl2dAhsDuKJy5sNwKh5VlC-uktAz_XvB9dIr9w3uitrhMfAl3HG_TOa84eEyWnQvLnjNjqH5_3TuD87nqwgn4VBnJtB96vUka2Ic_XsVCtRZbtwNiW8USTgzLwOh5Yb3zvV917eCQl5QBJZdM7jqPIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWFXhxBLoBNVCbXGidluNF6Q7V-ICGwkmSb7rYCGiG54wHMJboDdVeJwz6P3kBk9iYvwRJebr7n4wvuifERuY1cfRGBMMbgHCZXDhz1ROb61I0NtAT0P7GtM9E-bUZ7qkwLwFklgp_LeFNxOWdfoRNcIF9OEgRiw6b8Cssgqz1d4bz1ngJfJX3fUc1hUwzo5NPrp8LBlb7AfLWmfzKu0BS-uQJH9KG4GA4Tgxp1iEeVG2fB4ePryA2d_AWME29Ey9JYxTBBWBSn-j_k7CuBV6wDOOcNyA9sDDMx_iy9_Xn27Ryt1rk0lRoYd7akj9jpttb4cbxcCtiXjPlG9CoRZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=Zi5xXYFp8Hk5EwosB2l6GjCXcRNktKXYKdgyfUyNWxEIyTEggqN2AcjSuqzzdbu2-it-E7P2OldMULKIioeulso2li8Y12noqE-E0Z_IKwxOJejxhJ7RpJVT8qbWbU4JhAn2znFs1wUbEQbnCupSuMJmPA0ddJHHZUPhS2sBbrXX4ymd1iRtQaBzANTwUf-0rd3qRxkP5Dy9s7pSoFCgBah4j_wQxWwI5xdisucLBuw9McqzrO518A6Jwysb4juCl8RhyK5KmkhII8diFzX_cDUJ_be7Xq7lIdjkI4zbo-TAt5gAPhVtdW4C6CkLNusGg6-kCmztHJpfFw4ftJS62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=Zi5xXYFp8Hk5EwosB2l6GjCXcRNktKXYKdgyfUyNWxEIyTEggqN2AcjSuqzzdbu2-it-E7P2OldMULKIioeulso2li8Y12noqE-E0Z_IKwxOJejxhJ7RpJVT8qbWbU4JhAn2znFs1wUbEQbnCupSuMJmPA0ddJHHZUPhS2sBbrXX4ymd1iRtQaBzANTwUf-0rd3qRxkP5Dy9s7pSoFCgBah4j_wQxWwI5xdisucLBuw9McqzrO518A6Jwysb4juCl8RhyK5KmkhII8diFzX_cDUJ_be7Xq7lIdjkI4zbo-TAt5gAPhVtdW4C6CkLNusGg6-kCmztHJpfFw4ftJS62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=AiiBDcLwdQ2UDwoouwHOq-vInAIlr5g08fYQ0olj3NeCxp0gkV62ldpDL3pp5zmPn8iYm3SbMkfHmLxewCrrCo9Rb7aIdhyIWLfET3ZX7JOyHflTz1cN5ptA7HeXX7lAKpaTmS9AOb0CeiVvAgquppzibXlwkX1vo4kLl-rWt1CooLqMnlSfGwx5EhR5uHGfpRcqeQXYi9rRFm_go4cOdDhfWi7GwCC8pw4SPYJ2HIdfiYLWHm-6jyBf8JxcMplY1-nYkI1CUqzOiTLZoI_IYA9vIcTWUi8-_78woPz_8oaPSJ6vOZ7DWB2s6h_uwOXpA9KZYPbrUp8YsNigYWewMGvozEJvBfMScLglHnZWDUn0rAul1rEKWaSmrWq9UK4qJzbzdka7Tk3ap3Wl2bdRdNm-qKWD1ItmscirljAC5HQoACHM3fNSrllPGsPOMUm-LVMQiVHRmLjro96pTj6iUbccX6o6XrAx4li37QRz3LRD81nIQQMoYlmxCOhsrphQrXsTsIM1tzRaqDFNBBSUyndgawotypV6Gy4WYtyM3-bBzBhMX5YRRpbvrF48sXcmt1m9M9jqXOMbdhd2g46Xk2Uv-T4E06Dto_EJcENrRExqOk0i8uFsaHePi41Zto6rBFDNyi28Y-N5q8jRfM68t3qXfTM0lKTgRvscIQitpw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=AiiBDcLwdQ2UDwoouwHOq-vInAIlr5g08fYQ0olj3NeCxp0gkV62ldpDL3pp5zmPn8iYm3SbMkfHmLxewCrrCo9Rb7aIdhyIWLfET3ZX7JOyHflTz1cN5ptA7HeXX7lAKpaTmS9AOb0CeiVvAgquppzibXlwkX1vo4kLl-rWt1CooLqMnlSfGwx5EhR5uHGfpRcqeQXYi9rRFm_go4cOdDhfWi7GwCC8pw4SPYJ2HIdfiYLWHm-6jyBf8JxcMplY1-nYkI1CUqzOiTLZoI_IYA9vIcTWUi8-_78woPz_8oaPSJ6vOZ7DWB2s6h_uwOXpA9KZYPbrUp8YsNigYWewMGvozEJvBfMScLglHnZWDUn0rAul1rEKWaSmrWq9UK4qJzbzdka7Tk3ap3Wl2bdRdNm-qKWD1ItmscirljAC5HQoACHM3fNSrllPGsPOMUm-LVMQiVHRmLjro96pTj6iUbccX6o6XrAx4li37QRz3LRD81nIQQMoYlmxCOhsrphQrXsTsIM1tzRaqDFNBBSUyndgawotypV6Gy4WYtyM3-bBzBhMX5YRRpbvrF48sXcmt1m9M9jqXOMbdhd2g46Xk2Uv-T4E06Dto_EJcENrRExqOk0i8uFsaHePi41Zto6rBFDNyi28Y-N5q8jRfM68t3qXfTM0lKTgRvscIQitpw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8lNXny4QshOp8GKeNBGbJlvZlE0jLWTr4iyUA9w-6Z3M7FGNqQ-r26s7qc2L4YncWvg2r8OceKnm-2ypEQGk8LE0TPjYVwJsyn-dTYFmddT9N-ZlU5IqUUBT0H0ZS0t9PUrwt1_M7GQcqbA9cZutmSo__3J5G1QL03g_BivH5xh9a_s_soUS5GV-sLE7XGj2HkRWX46tpkNSkjN5g4NU0X3IAMtCFPyRTSm0M5JDH8oiuFV7XQ2L2qpkDSHSYpwoWU0K9ZAn5mkvcfwtVdkA6N1Ka8T7QOuX2rvWCXV33ABMO3cFWRaSUTYP2F7QhkM2_KvQwJD9a2ABYLJhe-5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jannjw0ZsIoHL3O4M9Oujoka8bgKhGgJI_MdRP87zOW7_FLbnu3TtEaKKOozPmJXvM5aNfRri0nyOMM5I2zlb3g_4i1LZekulUyFX-gThXwUEYbUPNUDcqR-xcminqcrZqTQ9duzM8JUMZdwwhZMC2rwIJvtlRx_5xs74BhDljG-NKg0ioVPrdhPLjnlJ04WJ7jvqaOMDkru8mVYu5873x-NXNLRrpQfZ27ukZnX7HgcOleRhEZcU5Lm5sBYLfkG0HUAcQvGQQh_HTtbUlex9kzGKVg2FXv8E-a2ZLcTf-pt-M6SKf13fIrDWVSR3BL-fmbIlulLeyzrXTO5bux3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nH6stHv_o0F_oSMyYd4rKDDBKEUZLYOQjnSwWBrVAXYgYMOYD0YRhJeBDA1QLuWpibtN25d9StZ_029zlJD-q4-DyM6TzQj86P6PtTdvR4A_apnfRS9H4vUdpwpt8JD52WGMOizhdbv2kAZA82XgCBcjFb5LASWBBig_tActPbds-Jrc6IN61roKIj-NDGBkPqOVEO8Dza_D2OGKyG-RyVs84yv-ijbhJi3CsLuGLoxuYUjFKNUCafCU-LKCGEA4tggfgmlIVTmPhxmNG2hMxF4B4TP7LHYa8D0DgLQWh9uii9zPHm29x0pPdU25zfm9WPG_bycuJ4U4-67nLYNtPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0LGHdFbG1iAWhew1nGr2ah7Tg0GpN_NLyd8EmdYO8m1xmg2jqfFVTdk3Y0Cj1nmbqzoa6s6jdFfBaxJi7TDnfujkcrhJtiG75a-foZchIg33bsUyU5yIo2rEXNlpLTFCURbdGjxdAJMot9hUGPY6kMts4X5l5ee2efnrO8LN6auO8ND57gX9GSX--lxW69kcqSKEbVu0tBiC_asZUU9orEh-b-76laIhNd80bN4cAgByguinWGJ_ZAX9XvX-dDGEYVa6msCrJTKgR7KT_99hFGFn2D5wrF9DLR33vOStYL6qoDmBBLJ8F6p-VX202OfsLVcRffr2w7PkG6uIhVbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf_zA0UakYS1XNQROrnRk-MSjyTYAieK86s6FV-VqNndXh30BIoXYowzM5aQPLrG6hm4tI-Z7v-U6vEBrFM7uajFJg3vlU-tpxrFbNB4ltZ7R6rvBhZ7gjxtc_fvqacmtkO3SsZaPbhFOq9G9BHGHGyX3jrBaEi5WO-Epu8yqhicUzMTba4DEJ8aCcrgGm0nizT7hfqvbaHat4prC9ifToDqKtZQtckW1KbBXhPKF7F1EASUUEZeeMGWoncdUoGXFuEZ8vneUVkGvFXj48Kd-_bmArfWozmeyRkiJI18P76Tjl00AUBIRTogHexy6Oi9iTMrynI1B_Gf8EjPf6hr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzthCDx6slHgdv6Wh6hkCZqJCKvyD-Ixfwrb1S4C3ANODnr2G5j_50VhiCxek_MUSfZJaQSOiSNKF_FQmyB8esRTlluAOgp2TIEjh_rrIwGPqd4IW9q0-b6dN0cJ6PBXpRakpXVopWcXLESnUr3cqHSGKNWdL1sgYo50CqjlchH2Ti2Fu0c9-5sm9fcCRkeuyn-xxb7h8F3-8iWgWxtpz53yOtXSaReAVdfzVHPyLpZBdVVKjWOkVCRLTzwCiBSIz0j_ENl8LJXAV191UbBNkLVoc_AcDuTfh0IptkCg93gAKr6uyIZTRp-jIWJBHNveAheHJyqiX_E6QpWniM4UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWmGbjFCv08HXly7ON7RCpRnWbockkMxkvKoV7zwGtdYUb-g6LixBbqJi4dZ9LznoqjQnqqsvoIOk2-U5uKMhW0btIqvKnD48ExJbv8jmZw3dgBz68zszlko8dLpz6tChtWS41QR1nJcIG3zHMYyZDTK9DIUzVLo09mjJHPe6YmdCDT-aeDTp-4Y22llxpgBs9FHQ0yTgf6sRZSHH4NqsCitbaP9J0m2vOyPpaqPEqxPQOuHw5O4UO6WjamIha0RrKVjSZ3sth6cUZy_95RWWmB5mKUkudFcrtKAIN3LQAq-TPOvHzCI7etjYiuoQDJ9IURqyNNEkOv2sa7eMqrovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K621DDLouvopBxfi61jgtqZxd6w6VmddHHMySdVtLW539ZR1xxW8n_TyUd-Y7AjOFOh4aJ83vC84QGJXlVcMmatmJRTk2VHUXUbYcfeWXotuc-w2_A1Hq1nZuZHP9V1NEC-FjdcToPLJsN7ujf_uzYrq8nU86Y1nimXink8rxeoH9mfLAmAfl67Ej3y1WXY4ahf32l4DoRvUvre4T7yidItM0wFjLjWav-d2YjuicosKOyguox-GQCw3uCa8lmQsnBFH8V7tszd_9rlmO_Y8OUmOyoWFzp4imjrNNIQIKZxxIqBrQJo5rXafwNZunfAWdO5-sixjNFrRjbsrtACAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwTyjC2R9Yl3HPxzD0e5MS2pAvU6zJKeGp0F6iQphnDLQeYAAcZdWzBHZEmjJ_OHBeyMI8HpXGGSeeywV1-kkcUZM7dd6VRx_YnP-Zqu7TGyh_-WjiHo7KfOqYwtnT2yg8jsJ7flZ5m0XAcCFeFfzbGXTZZphbfqIoj_VoFlXK7sX-8HCS08-v_W6H9e38JLCubElwKE_FK1B8qDYh-7Plvl3Z2O9lNMZ-dzogDt_l7EjQIZnoe5VaLWtXCo3wmP-VQseTFIkU20R7mYucw_V2zttPZMgrIyKRYFNQbV_ftdw9ERkUpHd2WQckn2H64_ELvOUahXOMoZeEpr0MCDkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1VkY708ayw_NLWrsn_yCeJoVO2LzZDbHLoUFzzYuNIEcaVlbOvPZ2Sl9Ra7H9JmQ6g9Dvn89XI3cwSWHQq2OMQ9fROpKlX1WL_sWNZj_o1K1uCKxBDJ8cx2hxDJOlT9siRLWquvHaIDCJXgoZQSz3Cp50f6hmTvwE_jIiwRNGKQVP9Yb5L9dJyXI_k-4wqiPP9IpJkTc4vpeICQnD1ceU4haABJ8lJNqQ1aaFt9gcF7TnpVrJ4vV0orfVEuOHEdb0Uog2oAHnUxP-d6aUIC6QdS159mU4zdx7VwM0v7W2SdHJxVXsVJnOw8jgDRu3TXI-9ba4nBiuc_SjHvM5AgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPxmdVB2bYlpiMwcG9hbOKhfGzbRAfxQGRuoDRL4xp21NzJ8OLFpQgcXOJgLDuqUbuSoYYa-knt0DwL3Jyaq71hUpz0jLhtlHGI0iBYQzYTafqc7Zn0D9wVtAeaj8iy2EQgWYfaVwBYU9r3tcJ9Vwe26XqZ3z7FVDvk7dPJ44rKhO9WmUikqb4EdFaIEsrBWZOcKACtdo5vx-foSybEl7R5pM4x_T378_eldUxB9UY_2d6FcTOU2I0Uj-Ve9JD-qUExasN-pUL_3Zk8wOFfbZc7C8lERW_cLG88jPWsmkZ1McCrpYs5d5_jSlWDI_4h0HEW91sMpp49yyZxeptC-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1ab9p7dev3o5hUfXyKO2zjj7R2CxW_fYR_A1mexqQ_bx_i-LyeHj-GAHd22Huc1xfjaqqQ4S-o0hkqQqsv79AyjuB5KTSTVfZBDaCmEGuwYuT7HmfxKb9-p2WrmLDZQS8jC4ZO-hC6K8tuVk-TCsKDw6K2HMF-Pb8dHQwr-F_vcqd9qGhyDEwVr1fB8-wvHy_2uiZ4TCKASLgybIgkkU8AqjG5qxB1qbt0DBBZFKrCIwRtJ_MUelY7dWkLCYyGvSKf723l1yIdLVYhpziyHBwhTtWXaBho19o557t7QPzfsxiLz_oDQZjR9VzpZrFJxZ1BmqW5Gyhi7uvV6e2Jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ZUdA9G9S95p6pmUTuCFYPZi9mJZmw0s0L-LS6rBYrhQYveC64Ez0fhw5c2LH_uZfVCeAlDkQH1bEMVfpZjzRe2co474uKlDM7CVj7hVXs7XtfAHIFFOxx4Q9JLlqymHOMm3nj-db1dsQD31XxwyEY5whxVDrn59m0nmw3csh0oC8mFbuDK4sg-wnAuE-rJORDQ8rBUUNGKVyBQ7wnuO5Xv9df-ra_J58kh_zzXwb1WwsQoYHXSzoV-7t1lYzvtX7y8Y3UW1PWqsuzIigAgktgLXWHvtYmg9dJzKjtT78vikXRUTDkVYB9BJ5upmcBctFv1Mizj8CZvcGmvZoi6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5kPEWe5Cs4SjDdxENl4TEpYoHxFv15_VPK8DSIxTDMqucvuKUitznbWwfzm88F9B7aeGmOaWWTihyBt8dOLrOx_l1nRga_IMIjt2pZimesOvnQ-17EiiScVrkzZPwt4EwDdoT6JxXewaOYn2iYF1BFwPoUMWiYYGZA-egjQsj65FLel6wEUwF5TQHM1xF4YOs5uC9t1eDQT3NhQ6O1Vdf8OfvdvTaT4lLxs-QqSqY-fDTGNMVSNQx5ssP4Biq8DsraPg2orPcRXwNLpucMz1cFV6Cj0IDXVos_jBzscOzxR8no8KqUNctqxNu6h3JbHjLdnn-r9QgGxT2OGqqVRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTBNkGYUgi3nqCMLTlnhHz8hfC4bo588kcemZe2PLHYe4guWEPh1k_rZny1tsasufFd93GbS7y6ZWjXfOWYM_9QlNl1A0D4x3aIj4LpDMtUpZh-ZQT9u8hIKx9BvhonAzb0lW8CjPdgVPnCNlOWxb_IXa5Ei344xtwtZ_6TRlvfkCfv1c-TVxIgfxHFVPbKtPYNydOtSwVhtnCSOJgJrE57pRTK3d1vtw9Ce4gnA8vqmwMMxAxScC6yB89gv6C4PFeeu_fhBMOgNCOlrfOLkb-SHyecKuILa5uAnRRQsNb-Du_A3DE1BJcIlrgAfbar8XBgTs1Am9J8uuNBU5Fbh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoqkCNRlTmke0NEEwLaUUxDxxTgQjBoAndRMOHLbtw9gSyPHJ85Kr1OQtS7Hd3N1NEaFKW8_-bUmFarT97yC5OofapapTHrqBsrpQgjn14dOMfGH1d2MMiNz6AJGos6tl3dWEfsHAQ3BzAKh0D--cc7mjxLOkByy8NT_zPIxiZy0x2Hu7kb-0z3BuGhYhIhyfRfprHNa68z4SaeDiHaCpVBq5kqV_L6c8o1ZQt1GltdVREHp8N_OSYU1RTwOGUJKX_JYjTuRo_5Dqk21HLscEQYy16prFnSowNWizFDKh3DpVy3O6rPrvPw5ouJB20qC6tf4x2Jxt6aFgzId17IW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrl-uNMaiSvWeI3Kw1yYR3SMVcTg_fIyOYBhh8aEf0zNiDf7nUgaWflNQ-WFmYfj9Fmw_gn_JI7TOWbrQr8W0qsK5YFfSQ0Byx4sMV4pE8PvYKH9RQfi1mBVW_x97V_o5YjB-hV9kibYFgjisWdB8MgSn75gr-aEKvA5d9Q4s_Cics3XNzGPgx1GplTFce76Yxh3_nC886Tcq5S4byrhf6svGIj40LcqEP8R8Am5vrCHdo2bxcH3vexFzY_xKMNaJqXoAZtyZ0Z0Wr1aXGTBhXi-ytcqrIR_EZ3e68uFAQde5U0QkKAYPekN0jCXJm69yRuhszQAZNfkqZNz21vsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgxPAv5tVJkOhlZE468VOR4SF-SPMgT7vt_dR4OBouYqgKGgvsdLBX_Uotmp1EY9lvyQKnKQeggGdboDIzOUe4br8rZX6wuUPN3jZ-URMSSVjQwaOn8vBEDILLm3t8mm2qbc2Ce964atVYIKjE4Ca36zZ5yblot8IJdjRr3Vkw68jK5l-vM1JB3wxnYTku8E-nTKNu11Al_hpiYLiRQdbSf7kmv83pXPYuFNQwDg4qkMaQ43p4Td-uvteMOzFbCiPqE5n7aCzkc1fyVM5aMiyu4WBcumsQ9XfaBsio7rVaNto38nxTY9PatrX3ORfjkHlVQG-mBoB-Fj8tbiYbVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNqgMmXRqFL7pSIkWVgVsjtJR5pOCqjvEULw0R5NHO3A3de5n3frovK5_LWii17I4AFuU8sipxvqKvpM2hQoHA6ko-QjElr_Dm4VecUvtW4gzDV-ZPbsn6grw6ZmkQvduIZwSDw00J02alvByEswfzavBQ5gXXgGjLBnZH28sTZCbScHipxcT6EedrEe5SBfFc6fYW8E8UwKhUm_o0-T_7h6RWVkYF0dkov-21ukKMZ62BDliBoh_at-ghTS6ZpNTzGSr34DiAA-djPT8WFznUpjuPyaA22M9pcgZek_fxEJGMonpGSZHzhGR37F_QTzeaNQOBQ0XNKQzFmc-o_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDY6d-v3lkO1D8uQAywztmSAMtRZpmQvmy8Mbvf21b_TmnJwmE3uqxKXeWPE0FP87k4SZfb7V8cOaGKxR620guTuckpFsrr-yp-QQiffYsvNrb9bOErk2z4lElAVN_XIlSTi387uqubGAFzCwKO4_kGcPgYT8sBSVWwvdv6mCVZgaQ0_CaoPbxLQq9S9eGAeMb_dZnLTgh4kvuXYQLaZThPpZ9aUtElofl31i5IypDWzeAwo-fdfrp4HVF9JLoim9kXKtLhAy9e3r6ABRxcWU9iOKgUsnGWO2Zgk4f8_54kTFm8rRyfWY6JjbzGAeLr6ExkAwmnlxtGTfL2O2qYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjA1qL0Ntk_uVzwY5W5vnE4tgNGfncDUxzG4HJNuab_cZxx_rouj0oYJRDC4DYjT5pqkeFWgkv9_H0d7azNtJ_9PJLtz7LGexHJ9Gypai0U8JcOzjVJyv8BoarrEWPrCZiZvX6cCL4ALTKzPiN1wsPzg-e664wcxSRDcKWvbYyJvbE0JJM0obX4Jc9aWKmX4UbqZrOEQShq4nUSeFHwifpA9owbxUUNYwDNmcnBPElTBAGffpORPUKIwVuaiDYjriDzhvYl3VnTsffSTqvf8_FYSsGN65eKhlpOOWZH4qs-rO5Ck2ttIMOTVW3aHzj99as98LlFdbzrPbxQHGrhg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz2aNl6B7zkEuGBQ2DcLVQy09Nt7AC-oDhgXoA-ASvnhAR2GBGt6xULDjNGmoPigv3qu0EP2afxSOaU4sdnIgJz-7_wqYGmaqdVbdVwKpFpAEnEx938SalljbP0RyJlTJdVdi-Nrs6gCfdV3U9MxVRX25hQY4H947_1U0TlAq5rQ5mTsSJixgsiNO_txstMC1VmePx0VqKadt8vvFGOPoh8g4rSELDx1LrWHRgAQjnPKu12qGRbYBxeR8CdyMGXvr7LwOWBKm-eAdAgUfTXfjx2cL_QLNtzmbW3QMIs9RZUG_qff_Ffk0mUZScA5kGgMeUxK2g2xY7XVw4OpPsFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf186UZeTroH159ws62VF4IzpN4yiqz1f7jgGdVgxBFC7QmsRUMw36yqfPko2keXaep3PleGExBTFYuGMvx-MAI_ESG2rVXDU6bG93EePfIyR_DszXqtmyy41garAKTJxUHx7gz7Ll1re4ZwVzshdb2f1-bcCst_STN5p27ExqNaZjgbzkA5dVnWLTnA-qJd4JaThjJgdpB7f7lvveBQ2r8iP5boaaR6wmNkk0fxJg_5juQW7XYIXxm--Bbmefh82N3413T4TCXSX-Q6YvUtMKAqPsgjDT5g8NLLRBvpHO1KA72sFUHQicURVdjd2Tm-87ATgKD7yWoTagFHWaTOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQvr_JHzJK9U_BqI-gnq7Ryxiwc0n-hJKKCp1znbROu_cNhOqITx7LpIB5RsmWVmNOljURBUlx7eqA-QXFKFMto2sEjZx8VRn4ReO7091gsWxT-mQ0N6YXKYG06VAyuAM5mQsFt_K5iPBJO7wxxRL5uzas7vw7kaRTUWgyRKfWomkJWhtd0F4qohSEI4FpbNluZXMc5Civokl2gmd5BtvKRGLEf5Xeqfjr20Tk5B8TUxjizoCme8YC178Pv9WJ2RWTjrfbWOYYn_NYEtL6jA0S_jofOjG1nZfxqUTUc1WuX-maO8gJJpLzBXx74gbAMD5J04Vi2L_kP5KqLLuXpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EayyDHbwUp2Ti0oyMgZahpe6zbfI5peFzWXGweiNAkbSNTDltVoYFh_21BGqPAwVdkzw6NzXqDDcwowATSFIjJ9R7h3iuk5AiPA7fCMA6upU5NrtO32_WSxyKr-t_UbdMZ5OdauyV40VIbBZ_yvehyBuzIiJK6dLl1rh-U9na2uLp3RgvErR-FkE53RasDiGeoK7FoMdX4yCZKJRf7Vu4Q6eI3tPSPCG17alYEp7-6qWFLCVxdY_yClHzWjBMbVDmO5Hn1lyDmgpKRVZamqNdACcSRkqiOqTUdgdhrL6P13Ksp-4rltdciEai_HxSB918HwhPW2EVY5vbZ3bP_j_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5d5FmErc0ypnl0SNWSBppAKhEETLbTwT_fbH8q5RNrG0QlXmruQt5I0Zfivtoxg_TicbuEtivJkCetSxqIaQHQ27QsLi9voO4vZuTwPtp2by4VDHx87gxmCxuafVygwItQaBoFPS4DPnB0MGzrJZb5Jp3J4K0k_fOFXeWICRs8Lgs-t6VEW54sy1tah9C9Fnx4_3e4nKtez9R1XmLlhzUsuCSjsMsH60p4yRKV6x3VWjj_J1N4I9LP2ekx8JVIBEyZ-XHbrKmJKszlML4Q9N-6apsJwGhWX87RgzioQrLy6ihcFTvlQM342HAm-TFf-bSDMsS4yBDofbqiqaO4A1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJ07fZMpjUqIa4BsUpcd8Sy7O-2vhV30kgm9Bn2x4QGBRIGNU8BcFKoGabC0Dxyp2a6y82YbUIXJ6aF7O1er5axMTZgjtsxZfpz69ZIkl5v63VJU2GS77VV_-FHnbI9dSu5L03NXrvzpaOF_n1oOeEaOKdmm1u43LEaXBYFzFam6V3f2m_NBOoME-gTcT5iUTAHEvS0I58MxpUcW9YkqMpp7ypgHJpNB0GEaCY4ZgEjG8WHpAoe2qWs7IqRC1fjlchDVIgRSj0ntmLDDMncQYLhS-1Gf86kZNLzpLvgZrXzaodnYhp7q59MRTtE9CSlqhmp1Sog_4ifd33pZJ5lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJky9QgM8mtY1dn-aFQCQJ9cgChY0QY4CynLacVsCD_6DlFUI1Bkumr2jV86JbvMjgrvd9gbM8cEi8_t6AuPsJ-xmeqpS3klIxQXkDrboX6yQ1jSsJJvoROfrH9aq9VlY3g7cT-QJA9lmypgmt8bJId2-wF54ThkN-l8pvzsW6MoOfKNr6qHR0hozfCPJWjCQ8Dfwf37pVqO2A-KQ3tGqwmiseh8SjwN43axBPj1YH9LEzW9OSyYC0MO20ADd6gnaNL6gJq82HmWou_jnymgYksam22YR8lKNh1EEeC-byFdBixo3ZSVhBjJhJ_96gQIXp9RkVUSKscBCWYHp4fohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=tCk5nXxlqu5xX4q5UNXTNGaEia9TG3bCHumHGdt_L8CaGGyF4AqhFiPG17KILPdRXAIe13EccT1zrJM3IJKKH9hSEY6aRXZgpamIqZVt5uhZjDoTyPh8zck9u6ZowcpwkRQIZtHe9Xlnke499QP77426s18bkJcXnJCVu6Qxft533C1Pi4XuDdCObADPQDLsjuHbWtqTQrBfgCAppx9Xgch487gMJ9NOsKdIPZsjF6sq3J3goeM8eLmZEMftPjtgSx3uRtVUcTv_FF7df7PCSpDQkjJ8oMgdEJCVbrqPuaFIZ2tbJG4Q0wt5MxdEW4JwUFGghkYhPwX4DdXNJpJ5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=tCk5nXxlqu5xX4q5UNXTNGaEia9TG3bCHumHGdt_L8CaGGyF4AqhFiPG17KILPdRXAIe13EccT1zrJM3IJKKH9hSEY6aRXZgpamIqZVt5uhZjDoTyPh8zck9u6ZowcpwkRQIZtHe9Xlnke499QP77426s18bkJcXnJCVu6Qxft533C1Pi4XuDdCObADPQDLsjuHbWtqTQrBfgCAppx9Xgch487gMJ9NOsKdIPZsjF6sq3J3goeM8eLmZEMftPjtgSx3uRtVUcTv_FF7df7PCSpDQkjJ8oMgdEJCVbrqPuaFIZ2tbJG4Q0wt5MxdEW4JwUFGghkYhPwX4DdXNJpJ5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5MxG8-1ay2_jYJ3ecLyLzaprZerQHfSHzjrYALc8i8vym9On5Q7J27z8Lr1amVUvSTlHEcZV-Ij9M931iHqmfp5M3XeDMeVDMGyZ7fXsj_ORQ_K9nPH2Wl2x5M9183imujvGBgmlQxaEAbJBew9riRfJXRTYjxywAQdDNNxkzIu_3Ugp4WQe2IF1WL0hkvQksFymt9IMXvHw9NnCsD2Z-GN-B-JM7K6KxkvKnrvz9iCgEeUxZozj_2IGNBXbJx_azVt6C-ci9exx-5lCQ5AfymaZzKyLQeJB4brYz6lzJsVyJ0LEaNrxPdrZ7Z_wtTF7UmOAk5hMRkvJdY-z35Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=RzXf3wSdlXoXDwGM1stdBIIh5eKAYYzt-fX9u_nhy3NgFaeQdjiuSFPFnbhuXHixP0O0yNwY6yNjwj0Mih13LwSXM7RGk4vigmLUADGp5b6u197EaoFNBptJbMsr4FVTzZTnh1KneN7FsX8L9RixCwD0jNJtlMqd-TxqxDlOXdTkmyAsEYzkOVSK9uLEbxWm4BLfKPF6tNQ23CwMTbhvenabF6lJeIssd-kxUHULPfC50gff-X7Ud_bBPY8UaXxUrUND9kFBn0RH69-VSoA6R1Do6XUVa1nTMH3DT1rYV3DwEj7wcufGphIpLhuGkgtI7ywbTcqiwOaZTbCwqmc9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=RzXf3wSdlXoXDwGM1stdBIIh5eKAYYzt-fX9u_nhy3NgFaeQdjiuSFPFnbhuXHixP0O0yNwY6yNjwj0Mih13LwSXM7RGk4vigmLUADGp5b6u197EaoFNBptJbMsr4FVTzZTnh1KneN7FsX8L9RixCwD0jNJtlMqd-TxqxDlOXdTkmyAsEYzkOVSK9uLEbxWm4BLfKPF6tNQ23CwMTbhvenabF6lJeIssd-kxUHULPfC50gff-X7Ud_bBPY8UaXxUrUND9kFBn0RH69-VSoA6R1Do6XUVa1nTMH3DT1rYV3DwEj7wcufGphIpLhuGkgtI7ywbTcqiwOaZTbCwqmc9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=ViE2FITiecf88E8qRjueL8zyJcpWJcFi7c1mWCI9akRoLl8HVwLp7lbkHmwb2ensBFSPYKb-13lzEmgzzfqHI77VcsoCM6nD35QjqWznM5gbzcr5uclxDtfC47kIHI0i8hmCzYYUtHsVTF5323B0lyv6ljzvD9ijLbEMYnI3_kN_grORskGFIHHT0JhDQsEIZ9OTuqjvMNKRnv9E9byBFWBFFWY3QXteB66lh9fRz-dFxyEREdP5uhSvhs2MAfT_gwEXgV_IX3fJjK8sy79EAimxk-Xota_--nwwTTERvoM-CFvwF4av8Zak6mbzQoIME5yE6sI4Qj0Fnc8tofeHtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=ViE2FITiecf88E8qRjueL8zyJcpWJcFi7c1mWCI9akRoLl8HVwLp7lbkHmwb2ensBFSPYKb-13lzEmgzzfqHI77VcsoCM6nD35QjqWznM5gbzcr5uclxDtfC47kIHI0i8hmCzYYUtHsVTF5323B0lyv6ljzvD9ijLbEMYnI3_kN_grORskGFIHHT0JhDQsEIZ9OTuqjvMNKRnv9E9byBFWBFFWY3QXteB66lh9fRz-dFxyEREdP5uhSvhs2MAfT_gwEXgV_IX3fJjK8sy79EAimxk-Xota_--nwwTTERvoM-CFvwF4av8Zak6mbzQoIME5yE6sI4Qj0Fnc8tofeHtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB0hZJFoJ4n8pMATbnWbylTU1YTMI9_q7t7StBH7-15iJrM4D1XkIevA2xs13j9y6dmCHNLZV8u8FwT-4HBR_VZg2R-lZxiXvERHnJF4A9d40hxYWgmbWAbPlcQ6UvDkEJWj3t8TTXwtA29WVcWOKNhrJZpbBURnKRHQzqcnQbrkXMTA6Mpg_onN99Gk21DXjXmZdo4JDQviGo1DV39OfJsgyF-4h96PNgUePimCsMQpo4KNl-gnfOFrU_SRKN7QUORX6Il07seLtpewV7VDr9y1ThnFw72WcHs8M12ZxXAFBUNa-jIwS8uOQt194cCQxjK0F0Tan7lLVG8BsHPK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=T5ao2llbyZiPGMwE3VqgSzUeb-oRIxZnaLmyNasieqxjVdEmGfCWosyJf688Ove7EHEdScp65TEb5BH1WiPMuHd8qnFzGlHD8bXl1WHW42yY6mDjm0yYi3O0gxAdV4Qalw7_QABgQHS-OQxxNZkaHlG2N1aLjxLGt73LK7gmUchX62Zxx58NH4_yTbv6RWt1kcoG0CnS3BO94Og5KdwEWkubp5JBxsGa7BCWISG8JzPubrnjzsL2XnwtvmfWEPOsGxBZV4Uv9mBWuinYF2OfE8S3os90UWzZlFt9XsbipaEHPgGqvYBvb_htdG5052iSVhKDgMclYMZA5BXo4jC1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=T5ao2llbyZiPGMwE3VqgSzUeb-oRIxZnaLmyNasieqxjVdEmGfCWosyJf688Ove7EHEdScp65TEb5BH1WiPMuHd8qnFzGlHD8bXl1WHW42yY6mDjm0yYi3O0gxAdV4Qalw7_QABgQHS-OQxxNZkaHlG2N1aLjxLGt73LK7gmUchX62Zxx58NH4_yTbv6RWt1kcoG0CnS3BO94Og5KdwEWkubp5JBxsGa7BCWISG8JzPubrnjzsL2XnwtvmfWEPOsGxBZV4Uv9mBWuinYF2OfE8S3os90UWzZlFt9XsbipaEHPgGqvYBvb_htdG5052iSVhKDgMclYMZA5BXo4jC1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-hWPOu__jH17NegyfPeRV9bbcn2b9xBkhcSQk9P-codw9snTNaKUo-27oVsB4qBoy3nXLC-9HXnBj4adZXNWF4TVBd6YguBjpP-BAhKvdQeIFlTr8colTgn-TnawSk47xhNufr1oLP0N0F-vVuRXz7zbn0yGHq08Vr7dUSIeIns5K00bsI9PSUFP_REQFM5MhXxsQWUJHAbq-Mn_CQnE9GN9RKEXYvejoEGXOL4xO3HhgPSg7io9hJ0CMLecEvaYliqnkAu3UE7zoXfleeEprlPcbsPK8OvJk8Rz1gJY0Gdf-E5z8h2AtNlLNqVHQFiyHF_tYJVdXA9ckynS5uzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=hSAbXYkQFYypKhQLk2a0BbsuogoFrGyefqh2mzaPx4sYCiSg-2CpsfmGIOAJ3AYEduWjTyO2M306LDxHNPs4P0EF5qY5W8GZiiCk3No9HjDy-P32qCuiyTQNNufUFsVlU2LFvboksC8bkS9xcFyjTuwTf69IN1YsCTFD3oG5hWk8mFlbiYlA2H_MLqh9dEWxhvApeNY3m5jPil9Kn-f9d1nFEsmnZzwFELO5Y5SVbUhsFB3hrnJ5hwu-q8h12pNr40aK1770aJULl-XM7j1NzIH8wUnqW-QhnzY2BCz6J4t2oIfc6PxozgATusAw5bMfNXGWWoaoY4SNRQli-HAkXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=hSAbXYkQFYypKhQLk2a0BbsuogoFrGyefqh2mzaPx4sYCiSg-2CpsfmGIOAJ3AYEduWjTyO2M306LDxHNPs4P0EF5qY5W8GZiiCk3No9HjDy-P32qCuiyTQNNufUFsVlU2LFvboksC8bkS9xcFyjTuwTf69IN1YsCTFD3oG5hWk8mFlbiYlA2H_MLqh9dEWxhvApeNY3m5jPil9Kn-f9d1nFEsmnZzwFELO5Y5SVbUhsFB3hrnJ5hwu-q8h12pNr40aK1770aJULl-XM7j1NzIH8wUnqW-QhnzY2BCz6J4t2oIfc6PxozgATusAw5bMfNXGWWoaoY4SNRQli-HAkXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKJ92CP-65_6UphlmIQlFUMnRCH-J7lwP2793IDz1tA7lvrCQcslnoHgaK5stVkBR4iqtnM6_L2EmDmSHfs-e3HiRMcSJbNDqoKAAcpSF89BPAhqM_cy5GFdDetiXpwpvjcqmezVFrGgCoMw7QOInkjrtqEu54oiRi4t5hLzDHs7iOTKHWj-ldzuPdp-fEM05wTfFf9CKGtr2gCQ_JX7O7wyk1yLiGOFBIDJdX1WeX34X8aJwEWveTuCMCeecwmjLtIBH5Zeg7K6EnVOlQAcPjKZofJ7LilYXU_0DsMVROxI_UzxAq1BDsK_n5QAiwY-VgiEMjSKjvliZJ2l5UR5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce-68lLqCT5ko3swrgjkJpNSRMhjrFRkLK2WIdbtBVqz0up5-X94gFfEK96bj0mNCMNcZomJNswAtfwaZuCd2tYpWeIGza70Pc6XjB6SRwhORjLQvaDbIpoRR76z4BnJTOrGJ9hpINEwXbrGhlo52ZO_e27gGZ1OlqwqWWt76wzpN7x0bAVtImUkyx7IlD2hZZSnQQh05_HjKV-N2iMMzucqWV_yirUjGB-Tj-nylbs5OPQV-7JfyIolpkM6QInbiip1vyrz75hhwWF4PdE7Qb1SEOgN9OQgUCPLIBJZCo5tpCCmd1diFWNme3eBAmpj4GfmOu-xkKE2bvGwgl1nyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=AjLg5YdAnbeLkwzLrwe44K6xPU6GIo_FCt8K2yN4aU0mlG7VSfuoxDn73s9yiOtUsB0gcqhuhUcqO3ewUXKmj9iGZOGLNsVV0zgS6cklOfHID-nvque9TqLUHA2KFsnQfrKianfFKewiT0QRjpvbDs4X6YD01Nfovvroo0VHYmBfMpvztG3Arwhn3A7U6f1tn8Ie6wLQCO_Hl30HxQ6g7JQW5SLlbNVbJKQ0yHDq3xjutI6vCk-ZCwioVoeABG9jbTrEUdtkiWh4pmQJxAWYZo_5Lszbz8-1z3nag2-hXm-eMCy8tNh7jSq7hDX4CZtA6gtOohTUl--e8KiM0W8MYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=AjLg5YdAnbeLkwzLrwe44K6xPU6GIo_FCt8K2yN4aU0mlG7VSfuoxDn73s9yiOtUsB0gcqhuhUcqO3ewUXKmj9iGZOGLNsVV0zgS6cklOfHID-nvque9TqLUHA2KFsnQfrKianfFKewiT0QRjpvbDs4X6YD01Nfovvroo0VHYmBfMpvztG3Arwhn3A7U6f1tn8Ie6wLQCO_Hl30HxQ6g7JQW5SLlbNVbJKQ0yHDq3xjutI6vCk-ZCwioVoeABG9jbTrEUdtkiWh4pmQJxAWYZo_5Lszbz8-1z3nag2-hXm-eMCy8tNh7jSq7hDX4CZtA6gtOohTUl--e8KiM0W8MYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CncsB0jw39UEjLJNnjBzYrMgCQg8X_FIrLeP4mMCMzG9iKCy5R3LwzyxndB--Njo2mSQ_P0csfUnbcmpU4q2fNfx_y3Y7xKRJVFx-E-FIgYKoyPyAX6BbpGEeUNjNM98lkX752-ZWIr46PDUiFR4CHttoYLkZOiQOSTnpJMC_9nibiL0DjDKcPD3FXf__t3YWtB9BdSLJ5REqyUYQ0ErKL-v4gnkRUj9ediK6llcNpp4c3QpNfrvVox1a3-hFxbGEHMdPGa2h-jj3yHXIc-30f2krsuFI2Zrrr-qqgeWjlDBWLoJUw8tw4zLIz5aKOVp13Ekb5hb6jz1GyFoYEwxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjbdWxdXjCFNQ_otWPOrDguXbyjtDfRSNj-S3tReujqzYP26q2a0i0VsFl3Vsbh0zThVYHw_peKDNkGoWqUIzKjWwe61ADqMuQBeTrfx2-LM2dJPVPpGNaMQdygGsO1TMtpoWVkZf7etme0mrPoRGERPgyGlL8wjgeFfPXI8YYI18-UZgRUVeiTLHr6C_b1LTPcKUoMMUton7Kx8kwFmgdrkP2GcXA-dbPUM_zsp1KqjmWGOOb8y7_1qkJK5oAnq_Ufh6U5qrLSVQs9nwR62dsgyaPg8j9-9Kj45wj4U0tOb5ZPCvTh1uXkMPIqyeaa9sZczyTya1stkZam2LqBJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=KKfJTj6f9OfAB2I3ha8jlszqy09uhbIMrlkBT6teEEDfAEnidQIhXYLbDpZ-B2gfKiohsfwD-umIPVs953iAmjYPqwTQp6eO8Lc4AkbykB9A3t1fwImqMsa-2AL0EvIWUBepXpE9dOKBZPAj9Alymii5Qjj4uMyDAyNuMf657JLPOC3vZbuF5FsL-RrgtS_NTIcURME_NigNalSkmuo-p7n9lBCbNNehJw3hwwcapzIPrQl6sL49zvYX8z0tI8J9_E38L4TukcbzhDId74jVLf5Umkl16eNWR5fixgcJ-l4kdlnbHbRcaZ9UIi38TCK6pPGNgIo8ZY6ia_XnUXf62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=KKfJTj6f9OfAB2I3ha8jlszqy09uhbIMrlkBT6teEEDfAEnidQIhXYLbDpZ-B2gfKiohsfwD-umIPVs953iAmjYPqwTQp6eO8Lc4AkbykB9A3t1fwImqMsa-2AL0EvIWUBepXpE9dOKBZPAj9Alymii5Qjj4uMyDAyNuMf657JLPOC3vZbuF5FsL-RrgtS_NTIcURME_NigNalSkmuo-p7n9lBCbNNehJw3hwwcapzIPrQl6sL49zvYX8z0tI8J9_E38L4TukcbzhDId74jVLf5Umkl16eNWR5fixgcJ-l4kdlnbHbRcaZ9UIi38TCK6pPGNgIo8ZY6ia_XnUXf62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9S81HseGJBfOXv6eMPq06_quD0P-8RuBf0Y6APScDBf0J86YHsxbt0kNNLH5x8QJUtqCBvDD8sqws89D5iGxSqZgkiFZutdf-breNXLQujaNG9gLozk0q-6TMSGgAg_JSiXpPJ3Ghc2H61tNjcXBwzTs9oxJFvzxWmG6GuPij31jaT3I_ttpPsNfZGxVaMB_bwAAyy8CgTZKq0YeQQzhGLGCTI9Sl6dIoS3M8j5CjoWUsVLSSbXHkD97-1gXxx38GXwcWPFar3Ag48nGg4C68wyAPSmApMmS3VEzk8P2dtr1gVFcKm7MghT3IvXwaeJ3ElwBU0SkjLrqlmzMzGWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=piOPuW_v15IKYm_OtwHIWGkvTc67czICXTE4_pJw9XvKQY_NYSpQBgDj7YKmxEI6pa5JZpDsnQnFKRoG9rlVh3WxCLZtHrVnC6bSmWQI5xqTb9WL6Ja5P7rXldUdoRBCzEdwFuj4vyzp8POlXfLvWlO1NhYZG3PTA73EOtGenNb_dj-7kOaO5RmkPpai4oLrxDr-9QCG7YUL2G1uv2MW_TIRVbU3aEq3CMFOZaHAWqNhA-wEyzsVdVf3FxILGg-BLojhLCKXp2Flsm5jkIrCy-Yxum2NEZRIHqUk9HNcLClQpPpYWBiuGP-Ij7jVZRlzsJC4sxLQv4Kuano8TQPyZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=piOPuW_v15IKYm_OtwHIWGkvTc67czICXTE4_pJw9XvKQY_NYSpQBgDj7YKmxEI6pa5JZpDsnQnFKRoG9rlVh3WxCLZtHrVnC6bSmWQI5xqTb9WL6Ja5P7rXldUdoRBCzEdwFuj4vyzp8POlXfLvWlO1NhYZG3PTA73EOtGenNb_dj-7kOaO5RmkPpai4oLrxDr-9QCG7YUL2G1uv2MW_TIRVbU3aEq3CMFOZaHAWqNhA-wEyzsVdVf3FxILGg-BLojhLCKXp2Flsm5jkIrCy-Yxum2NEZRIHqUk9HNcLClQpPpYWBiuGP-Ij7jVZRlzsJC4sxLQv4Kuano8TQPyZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN1SZ1RRZCQeK-sTJr_nj3t_X4ECMxWFzQfnUT-YfHa76711F1qvUW4JDWYGz-rwYfS0bdohlFPlpnNKXL-0uPFRQFdmE5Utf2FQ6DCG964FhkeA4hKbkEwFYlOJZ4VeDEF89EBXa9QX7VUzx_GO-6kXojGe2cnzHPRp8QlFVt06p9nXCGBMNdZW_ZC2DY6xGGWdX7iIs0FKp7IptVITY84hI9huNi-GXPbbWCv_vrgtKoVajnwVIztxwai8eFOO-DqYa8SD8cbLlindEsQ2-IxubfX79GXMmG0GTJDFDrFf-tmhe2J1io6RIdca8Xwtd7Nu4dUUK0QUBGinq_JLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=Wc1cJAZRJH7ld-pFVwxoIeVNH1WHWYM7daMtv9xG-APU547T-qEC4WWRi6RJAw3IdETV0faz1D5w3pwLCgYNafGvNs9TKOwSKPJEaQ0NrWGh4LUe78lL-Nxk6qo5QV9uxLMrZ44iWuLDb66Vm9QouKBr3dSiQf_dVIBFdv8DbciPly7S7pYdL53qp96U2ugNnAJgJB6w2Z50EP089Lp26MM2KU6YnUdHuc-OSHDenhwtt8U63MmEBDTJQkr75tozBhHUmlOrx4c6dzxKqwxZIwjpiSdiFff3pnjKTi11PDu8qI1ohpH_X0L3q58FleuXEnBlPzEjs4dLad2w_6ndhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=Wc1cJAZRJH7ld-pFVwxoIeVNH1WHWYM7daMtv9xG-APU547T-qEC4WWRi6RJAw3IdETV0faz1D5w3pwLCgYNafGvNs9TKOwSKPJEaQ0NrWGh4LUe78lL-Nxk6qo5QV9uxLMrZ44iWuLDb66Vm9QouKBr3dSiQf_dVIBFdv8DbciPly7S7pYdL53qp96U2ugNnAJgJB6w2Z50EP089Lp26MM2KU6YnUdHuc-OSHDenhwtt8U63MmEBDTJQkr75tozBhHUmlOrx4c6dzxKqwxZIwjpiSdiFff3pnjKTi11PDu8qI1ohpH_X0L3q58FleuXEnBlPzEjs4dLad2w_6ndhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL0AmCtj17iv8JsoypFjUeRWW0aYQRl9aS45zKgTZzahByEI6gRqIy8oiu2pv5cY4OSfEVRPvsrv7XkaRLAZHLFkqmSNcmD6P_yLZH-KeZFwl3nfNnPA53qH5WGMZm_Tn7YtPIAja-JtWCpxbfrKjFAGR8H_M8fxiWFvAASS2AmNXDaERcVmbOg6u3xp1JlJwlS3O8QW0l3Z63LAaNyE47gWl__NZ6MGmGkp1gDE-GV1pr2ZLoTKM8z73lAPYhqoQZ-KnkWYlPSCGOGfQUa0a7ilwiQdjV45yq4276Uk_vc6Pqg7XrR5TN29S_5a1teC9J7F5NzGkJKVpqfTLwNGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=KF34WZSdL3QNCJWHy_bmR0PJ7YbMLocRrJkWaT-ePfiaA6k95Lj_X52zPs2-5CXx0oDkhLAs15zXqYaRRdDyPPleQH7jDIbRHLVhjLIYzfF-3IQK-0_m5DU6YWT5yP3DzhkNlARmsr_j26DzBSaNRQ9AJ4Jbi-rosz2eTM3TS68zO9ZZZqh9rOLSDVbg7fPW_X8qsRNu9hacLVF5CBr2NvvDY1L2Q6N8782TlEclGbwAnrbQXRASQB57dkvW_-b2ouVeIl6DDXZEhVLYCkxdyseAae2S7aH16hHAJzEOa4SknbVIi4-tmZv1sYezxepwP1szx7y8IxRgLG7Bz6UW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=KF34WZSdL3QNCJWHy_bmR0PJ7YbMLocRrJkWaT-ePfiaA6k95Lj_X52zPs2-5CXx0oDkhLAs15zXqYaRRdDyPPleQH7jDIbRHLVhjLIYzfF-3IQK-0_m5DU6YWT5yP3DzhkNlARmsr_j26DzBSaNRQ9AJ4Jbi-rosz2eTM3TS68zO9ZZZqh9rOLSDVbg7fPW_X8qsRNu9hacLVF5CBr2NvvDY1L2Q6N8782TlEclGbwAnrbQXRASQB57dkvW_-b2ouVeIl6DDXZEhVLYCkxdyseAae2S7aH16hHAJzEOa4SknbVIi4-tmZv1sYezxepwP1szx7y8IxRgLG7Bz6UW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEQcgVSjPUA_KWCwF8656kA7lvftHYFjxd9Rf2x38whUiAEok9Shb3Lmvl0PqpmoObxTPhze1Jg1CaXfa9qgQJHOWJWBl45Ke-Lr_Ec8Kt-VXQazfVO58SM0YlQqECoMJNny81HB-wlxrFMxfKqlLAujsxlY5k5ff85ln2YVmHJBa_BrV66cF6plzm8gT7OCPhDtyMtDRmZGA3wfUvFAdWH5_wxL-ux1hPauY1Kxo3Yfbpn5MllLxxa8V5T3cgahHhdWP9wXm32TYfYU0Ah_csip3PLqKiCTCK4zGMoneP1-H8NqN5GCPH5KZGD-43BZJYDfCJMfEgscVHZfNOxHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bX65Y5gxhL72285NZhv15X-NMilQS1u96_G19lgQUgVh87bTSN845NFh8roU0Nh2hapLE87Llrq8YCW-Fl2vCI3PQ5SAZ6hl36t4chk60rke3ua-o6ABeKgFzKtrNWkVIbDIwLc61PPbrgH_sDcO1p0j2oS4oPIBtTkpv1RsLIzwt0nzN-4ZnRWJNY8oFtEdfbpySGAPHcx-Ds0qera5XVHrh2gmjgWg0YG-KM46YE_ErHE82z0CyUJrdbBLIMwrBfm5ymlxPS8zdwKos_M5BuXUj7ywE5FoyuQMtYZASEbZQVMXFQUuqLutGydPqtB-T7mu379PG_hpTfr0NTNIKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF7GOvyuBjnUETAX5D-hPalE-pMhezmZ_GM0rBiw6qAPFPJ1iNqGLYvEvB1p5dQZmxAMAR6vvCF9EHPBkJtKFcriltcfVoY3_rMu7mUPj3BzHKgwLvl195f52S1CwlukW80mMrmWqaoUiPglJ7fPI-KgSf1RwqRlI5p0jMhk-xM278MlGLKgIzihmNQJzw9CDlHQuKnZFCJk3TwJBflAWsePNoDIwXJBdzqwdp_uf00K9cTOtu7vPMJNLHwQqF-ZgS0tFrOASCteUCoUXDEoKNCBi9PvaEFRmjpXY9Ah3Zg8qPrhC_WNtKAoj2ndLpgEtml-rAOiGMwnPKD6K8COiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKFzzptnbKIyMoDRYPeeMowmCsGxZ7M0T6fCSEurW7lRpPEkFZQDIUcke_5XqCUJj9DljG8Bs-UBdeUaWWeh9V0AoTgIkutE9WLOWmoEps_unpfscemPsTk6jQq2H5HA6RMpCjX7gvderH6B26vlLkrPdcFD148V4gsXz5l7eRlJZkiS1wNGN2sr2qIuj4nE7bhzJp9LwPa-73EyEtPCLrSQ3bWLOA0gI0-Ovp2Kbmn0wubaNjVUYYdNPOyBKcyj99P66bVinqPhBGCAclAHqZQ0XYSw4pHHiJgQFdD1sqplfLHeJZm_3q2r6QAgFogKVL-VG_D5JMuQ0jmRwjMh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=h6BzU1Uc0AgTPD-v0haj7d5jJ3rOwQOZLUpaL6wPfCxPoenBDjTPme6jF6t5AvtZaNW6ej_Pj5dA6QMH3uNrRHF59p7EyyBiVfN7o4CSlKn38bksenJ2KbuT9hxu0Lt2XucrHRJYXDyfDfPrvO4CKUtD7o7c54c4GKdhLq-4iGiz5ojt0_pxyAQP-fwZc3SBTmua5MirgiCyqVtZ_MtdnLGC3h3zssgia7YYepPRU0-YA1X02p1-50I7rkJIUgQ9WfPJ4jM_L4Rn2CVUJ-s4b32FP4T22KlN-awYjLAydgkjv5QEgyZ5bpRKESAxnpsQ-lQgl_IpsyNiwi0tcteEMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=h6BzU1Uc0AgTPD-v0haj7d5jJ3rOwQOZLUpaL6wPfCxPoenBDjTPme6jF6t5AvtZaNW6ej_Pj5dA6QMH3uNrRHF59p7EyyBiVfN7o4CSlKn38bksenJ2KbuT9hxu0Lt2XucrHRJYXDyfDfPrvO4CKUtD7o7c54c4GKdhLq-4iGiz5ojt0_pxyAQP-fwZc3SBTmua5MirgiCyqVtZ_MtdnLGC3h3zssgia7YYepPRU0-YA1X02p1-50I7rkJIUgQ9WfPJ4jM_L4Rn2CVUJ-s4b32FP4T22KlN-awYjLAydgkjv5QEgyZ5bpRKESAxnpsQ-lQgl_IpsyNiwi0tcteEMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWhjZs6VJKPLWql0SUs9-3-GO06D3PLUm7new5Y9vubEtCZH5KIrt6ypNzojh5MB0HZDM6ivvdYsL5AuG0_iIy3_TFqq7teuRpETWe1MHXtVMe6FsvMOjhQvu5uxd9rnErXZAQXMKZNEG16m4D5KGr3vbOD4heuiwUvIrExwPcx4uHfkCP-dP8DykyeD4fzJAdYXBIob3Gxne10ViQfApB1q7DZ_HN-BM1H49pkSUZJitlyN-X9dZ_yXFhEHVANL1NnM3zH5UqTklgSm48DcySkSPAb-HnhhTbRl6Zu8WpbVIcGAqcrar3Hhb3K-DwEbgdTAAR36l-_o3ZIXZZipvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl6SY0fHEnbEjkx5Y593augR2Ez6gxsu8WXD-3YkuojjpS_ds3zr3E-JtUxcte2_38krhHDayafE_rbY1wzRMNTq9Qr2GzRt5ZjoGMFQ8uxQS5gcIcxODd71uXgV1V0Bt0P9kt6kEzJeq5B-C8tx19LUDfia2FCTpkrE-fDuoVSM8oj0vsRvPG0hD-RvzZ4753Byqpox-GXht8xLXxkV_hEM4UeztctU0vAXUY9GXpCE9MW9cNLAxkNyN1f26aBWoBQyq79JHd6hFhQAOkq1mqF6aLm4JuHMaa1Vg4NQ5KSCMP08UtpVDUvPrrAHIl9a2V6xy7CzJJs2IxTEyjrnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS3AnZQ9Ed-URMSPylelooq0RvzyBy8-Innsb8DcgdvCS4JGrvsBijNQI3KVA4NOb_cvQgzi27AgQBHCnceyyjHWsh7bTGl7T4ZqaHjU2UzYtpUhfOzJ9-1ENzPPFW4S2jmyAHfi0cP0o3s_TxX8Og8EiuM93x3ZnL6fYXmZeoZaoOLz_P5VbvWDP_lFoonBs_KDODG7KlMX6S81qxWZQK2xqF1tFW2QtLTnEpku-cOYsGFFpK-dtrzyXXg-9rezTV2v1rToCJaVlDhQEOWk1deaqmEGSoVLhwGT6jpGHCEjnMirgMyEMIwducxKxM6qShOsJL-afJbR64BCFAleqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=pTlz5-RWqvZdDJnp-v1mrSFoQJvs8CzToBPQ60GlaetfxCEqSBXurCTfZDU5PdC2DuqsZvs9LOrncfho3w7Td3CWzeJTEaii7RMmG3SE099neP5Xw2Wm_BQXzxkm0bbmm7Agk7INgoeTkG4dQrF11orngX9upn5svhT1N_xpjQzPiWXyvDpO3RA6SvX21sbAXBxjGz-Mi1UXxRGUTs-PFiC13aTGoXxybt08Umw6ldCc5LpsJBLVoFA1xg0T1lGqttOyX2lIwZBrijZczsbUGtWbCSRlkbiz9Ozf9Mi6yVX3EgftYheqhC97aSPvKCkFRnDiudSTTTSsP5R79RZpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=pTlz5-RWqvZdDJnp-v1mrSFoQJvs8CzToBPQ60GlaetfxCEqSBXurCTfZDU5PdC2DuqsZvs9LOrncfho3w7Td3CWzeJTEaii7RMmG3SE099neP5Xw2Wm_BQXzxkm0bbmm7Agk7INgoeTkG4dQrF11orngX9upn5svhT1N_xpjQzPiWXyvDpO3RA6SvX21sbAXBxjGz-Mi1UXxRGUTs-PFiC13aTGoXxybt08Umw6ldCc5LpsJBLVoFA1xg0T1lGqttOyX2lIwZBrijZczsbUGtWbCSRlkbiz9Ozf9Mi6yVX3EgftYheqhC97aSPvKCkFRnDiudSTTTSsP5R79RZpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=Xm-UD91bTWLGTgOR4XY-6cpK7MFTsYimn6k2Jeejqv1SvulJOQfUMwipvb7O-7oWl-V9hD7PjE9MUTYT1IdHe5-TpvzASSoyrrcbmNdXEwjJNJU_eMoN2jdjewX8-DbnpGUZNVNR6Ht9g8G91Yh7X73vY7CWGB1IwxI7Ir0X74wWenu9xW-Na-C_t-KgR8nxMO__3ahX-Qm7Mb6CGNJmr10W1EuYQgPKEYQ45Y-S-ivwpbdZ7K3YmT6f20vCPEkq0cASxty2584CHmebS4793KAuo4dL60dJzaFFfnlWSJ56E_K_nSh97kvAerLPxtdYkzVUal6kTz7ys6BC8FtmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=Xm-UD91bTWLGTgOR4XY-6cpK7MFTsYimn6k2Jeejqv1SvulJOQfUMwipvb7O-7oWl-V9hD7PjE9MUTYT1IdHe5-TpvzASSoyrrcbmNdXEwjJNJU_eMoN2jdjewX8-DbnpGUZNVNR6Ht9g8G91Yh7X73vY7CWGB1IwxI7Ir0X74wWenu9xW-Na-C_t-KgR8nxMO__3ahX-Qm7Mb6CGNJmr10W1EuYQgPKEYQ45Y-S-ivwpbdZ7K3YmT6f20vCPEkq0cASxty2584CHmebS4793KAuo4dL60dJzaFFfnlWSJ56E_K_nSh97kvAerLPxtdYkzVUal6kTz7ys6BC8FtmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=kLKY1TTPCjPd86gQ-v44TtHzjX0LCeF-lCiYIIMAXzd4wFhu3cD0iLsrXydUiK7XLwlOCCpYtYcU7-JNG_YqNzDxQHUNIAiIQtJC73CMO7lsDCQprtPQar6ZsxXDTc0W0QZdt2NYSsiXucIvVS--i3zqIpeD7mVws5ZIbb0P0vYffcNIzeSYJKNX5WhqRI_Imokl2n4RiuF0tCp1Iv6L9PYMfhJGnxfWKcmTFHWKI6YHpzd9ulV4bFvJBmpFe-i1wv5s0ISBXXMoRaqB_H11fpG8siiMs2JOBriCdS51S9ZEUjghBFJSDUKsQW2JSOO_CVN-Cv6K8Lz_DvEIeW5lIRGYc3oViVph5ctuhuWl-PwNvXzcywYVObkNHtXPJLpXUPDCbFmVL8NGsoyERnC4ifujAY3MlRvvuECIC-N6PxOJCjHyLHBQi7Xyt0XLWtQIPGB7xJx0tDPOY6bFTY4Mq_yB6ONcHrgOdLJl0OX1SlCJXm0jJSElNRI990JW1qRZwdmCd_LfBdoh6-7v_JpdTkOyZZDTNo4uZzE2P6n4pjQzkVq2D5eNtrXO6vgsDqg6aE2w85i-leCJSZ4el5wI35yWlnApLnO1pdcrMso7ZdEjod6xZ48nhHcT2VAShJvOkI9zkoOAochB1PMlLcjeF9tvWE8wTl8gMOg3vyF4Jt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=kLKY1TTPCjPd86gQ-v44TtHzjX0LCeF-lCiYIIMAXzd4wFhu3cD0iLsrXydUiK7XLwlOCCpYtYcU7-JNG_YqNzDxQHUNIAiIQtJC73CMO7lsDCQprtPQar6ZsxXDTc0W0QZdt2NYSsiXucIvVS--i3zqIpeD7mVws5ZIbb0P0vYffcNIzeSYJKNX5WhqRI_Imokl2n4RiuF0tCp1Iv6L9PYMfhJGnxfWKcmTFHWKI6YHpzd9ulV4bFvJBmpFe-i1wv5s0ISBXXMoRaqB_H11fpG8siiMs2JOBriCdS51S9ZEUjghBFJSDUKsQW2JSOO_CVN-Cv6K8Lz_DvEIeW5lIRGYc3oViVph5ctuhuWl-PwNvXzcywYVObkNHtXPJLpXUPDCbFmVL8NGsoyERnC4ifujAY3MlRvvuECIC-N6PxOJCjHyLHBQi7Xyt0XLWtQIPGB7xJx0tDPOY6bFTY4Mq_yB6ONcHrgOdLJl0OX1SlCJXm0jJSElNRI990JW1qRZwdmCd_LfBdoh6-7v_JpdTkOyZZDTNo4uZzE2P6n4pjQzkVq2D5eNtrXO6vgsDqg6aE2w85i-leCJSZ4el5wI35yWlnApLnO1pdcrMso7ZdEjod6xZ48nhHcT2VAShJvOkI9zkoOAochB1PMlLcjeF9tvWE8wTl8gMOg3vyF4Jt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIQxLyvKoEd3iiKxHeeTEzaMg0ogNifardACixxoinREFnoiqXimKaJC17-WVj-wV4NLwwXsAGzkPeKDNrmQAT4A4AiK5hjiffnA2bb-mNpqOHGQpqiScvHN8_zwzr1I-X6IGKxlgRYQxMymvBFwcRrMFiU8h8Ra9H8MeYmG4ipbbvw3U9rLKDb_KxRhagZeMSmqZJH738mqiqHQImpS0uE942NHvVuAnRvhOPizwc84Qz7w1gi5o1BRm8kxC39M-ZXlnC5Av0_NsIcLiocsIZAWzCDM23wYvey_xj55LLvAwDElA9mfd4BE7aDihuoC8Xngo6ynY18Kk5UtuFYi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=mg9FhKUYYTW1bVEapvM3hDSIcmNlDKBajGPPjUPD6oeNx2VfwOmPpyW9Gxt4BaKzTI3qOJSJjqKrfrmn2KdYaip_MIxqlLoF1gXqF_kpCiMZQRpRVCOu_3ZTCcY2wvs7LwHmD2pDQZ_VFHIvrhlep7oOB0bbes24OLLCQ-Gpe-r9rCDNgM086Tlbadn3bG6nWAA-cL-WSGBqvqAGDGv0oEwWBJ3dA6HCwwQGcpe0rOos-TW9C7hHpfY7yGYGOttjY8IqzeRvCjIEelSW9vhFEi350E4gjKAEy3q1YEo6ucVScBe7eSUld3mj5sV6TBVFFO5XR9sF9PxbB5-s_A_WLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=mg9FhKUYYTW1bVEapvM3hDSIcmNlDKBajGPPjUPD6oeNx2VfwOmPpyW9Gxt4BaKzTI3qOJSJjqKrfrmn2KdYaip_MIxqlLoF1gXqF_kpCiMZQRpRVCOu_3ZTCcY2wvs7LwHmD2pDQZ_VFHIvrhlep7oOB0bbes24OLLCQ-Gpe-r9rCDNgM086Tlbadn3bG6nWAA-cL-WSGBqvqAGDGv0oEwWBJ3dA6HCwwQGcpe0rOos-TW9C7hHpfY7yGYGOttjY8IqzeRvCjIEelSW9vhFEi350E4gjKAEy3q1YEo6ucVScBe7eSUld3mj5sV6TBVFFO5XR9sF9PxbB5-s_A_WLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=j-bqnTieVo_0usto9beeyqrMTUyvv69wOnw7ZOLhowLKkra169KdIZ4FBDIdrvx6n7XfdbAGs1VwmZQq6sp1ZJ_aibM9aNW-KFOKzDZKPnzy98GXzlCtxUMDymde1w22Y5DCXjgbxucqliQvR7Fd2Y81DAv4Gxjhqu-qW4Uq5TeU35jQJSXjpAuChTp6m5eGrITbGBd3sTFiZHkYOwiEFupkZIPRJoDtLCMlejcCH-odXbwcSnk5-bLVEJhjCWnnrUOyvYpC67Fs20FEn3kQ3bYueiT0-iiSp8ZFBV8fDrFW_Iw_9h_fXpVP_uPLu6WO5VQlQFV9vAQFv-zm1Z5Voy8xJYcCyGT9TfIb5SuMxyw1nihjXkP-OcWNbYKIcrVx6Eg5ymztRJ7WxtUnagZPjN0ilx-f93ltpSW9IW3W3_CGhAFIelCjvjFblDYt4mQogOjXtg5v5HPWaG49lv785bFg_toPgA2GIgf-UgLThO4nPfl0hOrZzSH11GH6LCWb_ies7U85YOGVDHLFswOjp1RuguDoT4clsB4nW5nr0HweTm6pywjZg66XgJwjwaBky0IdFx3wjZkujEatkgTvOJNVIN457WL3KLwZhl8nd6cmGZzUmE-FmMNbhNP77XNBS1EQ0BXk1IzPe5F7-P18U52AlORyXl_j8ni3QiaOa4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=j-bqnTieVo_0usto9beeyqrMTUyvv69wOnw7ZOLhowLKkra169KdIZ4FBDIdrvx6n7XfdbAGs1VwmZQq6sp1ZJ_aibM9aNW-KFOKzDZKPnzy98GXzlCtxUMDymde1w22Y5DCXjgbxucqliQvR7Fd2Y81DAv4Gxjhqu-qW4Uq5TeU35jQJSXjpAuChTp6m5eGrITbGBd3sTFiZHkYOwiEFupkZIPRJoDtLCMlejcCH-odXbwcSnk5-bLVEJhjCWnnrUOyvYpC67Fs20FEn3kQ3bYueiT0-iiSp8ZFBV8fDrFW_Iw_9h_fXpVP_uPLu6WO5VQlQFV9vAQFv-zm1Z5Voy8xJYcCyGT9TfIb5SuMxyw1nihjXkP-OcWNbYKIcrVx6Eg5ymztRJ7WxtUnagZPjN0ilx-f93ltpSW9IW3W3_CGhAFIelCjvjFblDYt4mQogOjXtg5v5HPWaG49lv785bFg_toPgA2GIgf-UgLThO4nPfl0hOrZzSH11GH6LCWb_ies7U85YOGVDHLFswOjp1RuguDoT4clsB4nW5nr0HweTm6pywjZg66XgJwjwaBky0IdFx3wjZkujEatkgTvOJNVIN457WL3KLwZhl8nd6cmGZzUmE-FmMNbhNP77XNBS1EQ0BXk1IzPe5F7-P18U52AlORyXl_j8ni3QiaOa4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=d9svUqgpu0CNNqrK5tCW5c60VLnXaSSFAejCrpuRTS8zE3-Cc4Y4dgr404rh_DdRhwqFzjuLRjyjqmnQtz8y99ioChPqlvfvmFI9XtH3Scgy-MjeNT1yKR8OE2W76CnuEMaIIXkmJXNfAj0eTxGyrumBv2-OhoS4DJwmXxxeRMAFNeaoApYlNwMgkmh_mx7ZpmIHUWrHsmvcuqzkIauUqfYbVSszBDSYAgf4ZPxUXLH7Z-2Hxi2_8M9a0tmXWkSCDeAEzqhe0GcG_o6B0ZxM6HWCuMbE5huBbNg9RsLIeyy1mtHvleKpHzFC6AH7lcCWI7fWkEY41Fm16YmiXhjxyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=d9svUqgpu0CNNqrK5tCW5c60VLnXaSSFAejCrpuRTS8zE3-Cc4Y4dgr404rh_DdRhwqFzjuLRjyjqmnQtz8y99ioChPqlvfvmFI9XtH3Scgy-MjeNT1yKR8OE2W76CnuEMaIIXkmJXNfAj0eTxGyrumBv2-OhoS4DJwmXxxeRMAFNeaoApYlNwMgkmh_mx7ZpmIHUWrHsmvcuqzkIauUqfYbVSszBDSYAgf4ZPxUXLH7Z-2Hxi2_8M9a0tmXWkSCDeAEzqhe0GcG_o6B0ZxM6HWCuMbE5huBbNg9RsLIeyy1mtHvleKpHzFC6AH7lcCWI7fWkEY41Fm16YmiXhjxyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5jYZ87MKkWV-dkb4HAcMetuNKUPF-z-PeuWfMw5s0QDbjNqsxuaQwpoDoqpQII-DtPLGSvzSz37kqdAWn0QxLLFjFR8K-9WTpISl-THPabeu1OklgIBYidKo3O4Rrjb0pHWNCsvZjlv93FvZO9vbqLGZ5QL0zA99SM7IHQZHiX0pozdGZpPYc6Bga_Q-Xm20lfJ6tGbhniMDH-cICYIsfaJa6b_Vb9W5zkQS4j8cNMqX0Z63_qEuChg3oRPEYdnuqQxwmVf2PXpGFCkOH81hLb9mYLrMwH94QYMMwrE8x_NU4GiJr6VHp_ditLMPjRE46qlcThnxEnlM3uCJdFUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=a_7PfYgkztZHqEXHEPs8VLxJs40o2it1BJ9LbKn2KDvS91DWl0ZbPdma7CKXhNLgkBjhJEvmXe8vIxqnoFLMc_pYr1TawM7Abz1XZhrJQ3nU5K1M7w7NSxgTMgzwEUW4rodpNpQEEZCoLwjBZc-8qKzt1qidF9_i7ca17FH0adAQt3GYlQdgL74_HRYY8vUmPLNOO4HXoMOMxQZN_K-sQah8TnHRh0uVVC_wxJ7NQ6AH1eLKf78j8RNHtkSq5CcTw_fewPJu3N26gdkXpfZuyKatRv7cnuNB5RCAdRPGv4qSaJlaGDCQ7e0EoJPXMIjrvsSgoyAOeP25VciqFF-FDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=a_7PfYgkztZHqEXHEPs8VLxJs40o2it1BJ9LbKn2KDvS91DWl0ZbPdma7CKXhNLgkBjhJEvmXe8vIxqnoFLMc_pYr1TawM7Abz1XZhrJQ3nU5K1M7w7NSxgTMgzwEUW4rodpNpQEEZCoLwjBZc-8qKzt1qidF9_i7ca17FH0adAQt3GYlQdgL74_HRYY8vUmPLNOO4HXoMOMxQZN_K-sQah8TnHRh0uVVC_wxJ7NQ6AH1eLKf78j8RNHtkSq5CcTw_fewPJu3N26gdkXpfZuyKatRv7cnuNB5RCAdRPGv4qSaJlaGDCQ7e0EoJPXMIjrvsSgoyAOeP25VciqFF-FDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6aSw5x-16qg2Gw6OW3qhTuQCz_nrzs1jPX3-J79j34wFPrxNI74KE_R-eWwK2VyW_JMP59kjI8MDmP30ucvrT3zGftWeWAz-aZJLpNONPLGahUMrK9s8zr35fpD_Wx4MMILZogQJwktigtwvcQqHZCR9ckCfZp_PNq58eZB-d_IaZr0RAKiL4zK5HcBYjqbthalm9jCXKmX9aRfjSenUBKQ_c_mXrq0m7BD_kmKmjEz9MzVeQtocAoj-qzTkvOOnYY62Rqdk9rYn3SoYrE7mqV4u6Q6Qe3NDfNHPjV8s9RyhlqRJsKpaEP0wIT_JxmV2eT_5iUEYGB4CTggfNJPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjwIWmH-ZTQpMrhTFnDTx7esgM8f_s9zIYNcRAtmMxALmB7mRsGZ91g5sboyTYizMsq38nLXSbQj3I5Lw2VpOzU4nEC9fBOL_EZm1ht6bAGf20j8kUAxV_PfEtO0AQi_lJgizFtdmXHEEmC1p4tu3BDCpoOH-X2A60ZzqaZt1F0bqSgUF-XDz8U-f8WRmdD2JtZgoMevNPopZAGxEskszFasJao4v4SN86dztMAIn91TFUNXzLAXUMSl-sNF9e-6uYgd8EEqHqHL6nrlE_beKMk6S8xcB0WMPRU6y_I9yJ3hkwmkRnORbgiukOe2bVTxSlG104VHsrr8RGRRFvHu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pen6kabMQCrauoHAdJRWV7YEEiOxkWs9B-kciQV1GTrh2BoOjrWR39bRw_p0tEj0IooKzUBCudaWMBRvkGOiHT7_LyQoutneypVlYc9Kpj37x4LJqr5LgFjNspW9o-KdMl82kGmk7spaLGeLfKbmAkkBK7WSoaRwHo7sQafXeHKHYGhzaAkJXtMFtBPLHMUuDNd2KJUXpBe3NAki0Nt6Adb9fUDF-DCM0y8GJAADrH73mwgf4jLvfQTVIT81Hqbv_HczyvVYzqgtBoBR6WP39FieBO9ZG1IpV7Vg-vU_Dwb4hycElVZx-Vaqvl1k7GdO-CCegs1GSaW5etk6Ua6sbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=FJDr52l2Ea_zHZZRCO2qsQaNUlpsJhob4cur84JFhP07-AH1-DUSMlG_sZ8AOzMeIXBswy27ItxcOwLUresgqGpjJAKa30p2cAn5QTc6LDEfTYqT025T49rGbpyLdDHEYBRdvcAbYJ5T5vzVslIpoPLaZtguswMVgNoN8Scylpcsl_YjTJqyqq0q-CNAhiqgUjjRnv6hTRB_vEINJIaCWwZ3SS3mvfanvD2D6BNIBmWID5gOoPhDBguqXnbHQDRdT0YPOfKqyhatsgEuKt5udlx7IkGDOtUuJNzFG9RHhLiBPkIk31NmHPVD8C7UyKob7k7Tcayd8hL_FqzMS6x2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=FJDr52l2Ea_zHZZRCO2qsQaNUlpsJhob4cur84JFhP07-AH1-DUSMlG_sZ8AOzMeIXBswy27ItxcOwLUresgqGpjJAKa30p2cAn5QTc6LDEfTYqT025T49rGbpyLdDHEYBRdvcAbYJ5T5vzVslIpoPLaZtguswMVgNoN8Scylpcsl_YjTJqyqq0q-CNAhiqgUjjRnv6hTRB_vEINJIaCWwZ3SS3mvfanvD2D6BNIBmWID5gOoPhDBguqXnbHQDRdT0YPOfKqyhatsgEuKt5udlx7IkGDOtUuJNzFG9RHhLiBPkIk31NmHPVD8C7UyKob7k7Tcayd8hL_FqzMS6x2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=baDxGOD_vBHI5Rt0RZCkoUS3EtWIS9UJDkaGIJvmjHOQt7afrIuBKxcjhFpgpzYhPWK0WLmxMX5Jnm11aelMw4pcx7agdx8MCxOK1vUHllCUAJ-SJQIXqmXqTraqo6A1YA4eUfhHh08X62uEZMnQfsbXuEDr6O5Kkg4Rcfw0O5DeYwDIwri7fomc5IA_nyGXFqG0JojQZI3iufrOVNMSVFBMWZSqRXo55AEenRv6PO8me_25m6IRN-KtwpxNXSwghBIDuz5I9zYytnF3BkRQQLUH-Cx76aIAbBzGusesFWcKTRj-UjGW09IMLlNULiW_sHE5F5-JWEtdZIx2pQLcOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=baDxGOD_vBHI5Rt0RZCkoUS3EtWIS9UJDkaGIJvmjHOQt7afrIuBKxcjhFpgpzYhPWK0WLmxMX5Jnm11aelMw4pcx7agdx8MCxOK1vUHllCUAJ-SJQIXqmXqTraqo6A1YA4eUfhHh08X62uEZMnQfsbXuEDr6O5Kkg4Rcfw0O5DeYwDIwri7fomc5IA_nyGXFqG0JojQZI3iufrOVNMSVFBMWZSqRXo55AEenRv6PO8me_25m6IRN-KtwpxNXSwghBIDuz5I9zYytnF3BkRQQLUH-Cx76aIAbBzGusesFWcKTRj-UjGW09IMLlNULiW_sHE5F5-JWEtdZIx2pQLcOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqslq05K6bp78yyDbMvy6pZyj9-RiZaeKN-tZnTgRWXTTRgB0bXouhrhNFLqMXDpO77R7Ekv9koqrDkkywHJxLHN6XipyDoykhZZ6o1HObCQ1m66o35nWk_-zggWA-WD1VhLk0VJ_p7L9TYw1YS3ixA1whs4rRcNYCO7vtnmOP2PtlQrtRVK56BWc1nd4vi-QMsjx0vMjErXq5KXqusQkAVTucjXBi3SSZvHEbq6HHiLAibmJDix5r8sHSK3A23uTJcAgGXTpnW24F1NMH0vpIih9pT4ewv5qSJBC-wFiMuQIE0AMj6-Osa-KyJwxIjGjTQi8jatSt4-SaHM7qiCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7zMyaaW8Xk1lIqEqbSJBc29UuPO2VJ-n2b--ECCYcNHw7Iqa6DMvnY5TNqbCwbTfPQohpcEo8iCVdE9bryEzN4c2qeOk0lOyTxzOM1EwrdiNg8xp23983zfhtGI3EML-qRPlxKV7_RfaDJTPslHdiAO4sQSVaU8mJBgV6hfBDlVg39bF-vg1iJeuCklS4tpkzc-gYkcaCg5nfxYiGkhZwBEb6AXaH81Rw-yfXuynDTpUp5DbQ3R0RRM6RtnVvvCEEQmGe5CMsH_nOETQlEocCAaRFDzB6h9jlwEV9CzCioOVAPTuNentlEcrVkuJ-mlSTCwW4c5Dsyyb2iysT3Gcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txEytWrGTlm4SKMUncQHaTlhrb25Cbdg50BhZrYgPTPrhbgbTcyHgI8m22O1qzLu4hA7YEjtpOZasbuV_9QiPSdfBxso2VavO_lGTUOGLGLD4gglDwHwWKiDSzeFmby0nWbOYgAeh45JF4Tkk-B31DSlnOhVJBXBtzPC_lSpZnkw9gDyfGV6SsDF-slh8ySuA0rFHdB-H7s-f9m205mqS_ne4pcCb1ZTAuDP-AC4EmRvtdwYUIZtIXkvlRfv6l8cq8ef6LnT6cQdy0SINXmWhWxzjl6sieHGcFllBUqSyxdk-pEU-JoAOqd6qL1xEzuAxj_NWupN4KP4ALA3_pJCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
