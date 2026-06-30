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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 678K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 15:58:22</div>
<hr>

<div class="tg-post" id="msg-97122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💥
🇧🇷
شادی‌طرفداران بنگلادشی پس از صعود دراماتیک برزیل به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/97122" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
❗️
اقدام جالب نیمار در بازی دیشب بعد از ورود یک خانم جیمی‌جامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/97121" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4sGGoTLFEzdvltjZ8zWj8c_S6R5aWbUpwS9-vB_l9RXCKuuWcN0RGNA5wWTm79aTilkM0BRB5mejuLHOBr8tzUY2BVIGh3vo5LzM_JcdD5a-txhEdgXp6upJDNZqUN7KwfPnDfaS8_sGQq8VqBCzwsJMj-c46Mwn8WlECc-Y3HW8XzcYqgOap6l2XuYDK9Ue-vEuCP9ob9tcm505MVEhXXbKWnyt7PLfgGrNvY0xOSgyqMmVtHSB882pm-vuok5RpIMMklJ3DHQJoGVTDwL77HDuS1ZzkS73_5OPHRm90etW8lE-wTW6g2XL-bLE0YoxdVr38410oN_1VuAHO4ZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
- کوپه:
😂
فرلان مندی پس از اینکه یکی از سگ‌هایش یک پسر ۱۷ ساله را گاز گرفت و به دو سگ دیگر حمله کرد، به دادگاه احضار شده است
❗️
دادستانی خواستار محکومیت مندی به شش ماه زندان، جریمه و غرامتی تا ۲۲۵۰۰ یورو بابت آسیب‌های جسمی و روانی و دوره درمان است!
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/97120" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbpVjb3HRZBDKDYJ2oZdTjQxYxfAAVfoS_xDzbvRRNQef9ZaSiMWLtHJc2KBM9BiP3kHaxEjjRKBYcSq_Sh4dlAHaXHEARIrWFgORgVkMqN-1blm8IvX-pv-rX69xAR0rw37XxIUmGhJ5qqlYTqgIZ7JmnIlLS9fETVD04MYCcbOx8L3HACCf2esIfvDdPogwDkMSLD-QFsQzEpUWIPJN8zIBdcZgMxqdqyjrjZRTrSev5ASkclIQRsfChIj5AWc7giQXEvWgjIWAFoKCqXA6_hHMiJmbhOcJoNi1qN4VRtxKfSw8oaH-rf_Hdy3S_tb_zCALZSV6Y66F1VTu65Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حواشی‌جذاب مسابقات انگلیس در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97119" target="_blank">📅 15:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
طرز برخورد صحیح ماموران امنیتی استادیوم های آمریکا با هواداران بی‌انضباط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97118" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇯🇵
انیمیشن حمید‌سحری از بازی ژاپن و برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97117" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97116">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJKOVZUY-pUgsJRmqGQev-pYY0itSQIB0ag0E_WNKThK7A50Zqe0xRZCHzyasj0-QNXyIxLB9x6O87v-v5KqWEQjIgJblwqJN4015K0OwKb2sww2aROG6UZCGJ1BTlvBn9KJS_6LcqIWkoCkqF_3i1Ae4hTHzB7P4Ag_aYWbMtW6LDOaSKvEArHHCg0Ru5j6dMMZkUhbgWplFF5Q7awNA83hRXH8Kb15m_6QoL2CwEP9y9vG1I_FhR6ebgLgZ_tBl7v0Zd8Bu8Ge6pUoOL_wXI1ydp1tiiNSd-yPtUFV8mzbyVVy1Kdtx3cl7SaCD_IKPOGJMHRzSu3AuUq34H69mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوکوریا :
ترجیح میدم کچل بشم تا یه تتو از لوگوی بارسلونا داشته باشم، من حاضرم برای وینی و امباپه فداکاری کنم تا همه چی رو برنده شیم، تمام کارهای کثیف داخل زمین رو انجام میدم و فقط هدفم اینه به پیروزی برسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97116" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97115">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوشحالی شدید میثاقی از حذف تیم‌ملی ژاپن از جام‌جهانی؛ چشم دیدن پیشرفت فوتبال کشورهای دیگه رو ندارن تا به مردم اینجوری نشون بدن که تیم قلعه‌نویی عالی بوده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97115" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97114">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
آقای‌ناگلزمن خدا ازت نگذره که دختران سرزمین ایران رو اینجوری ناراحت کردی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97114" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_2MgLXZOh5kfxPkHGWi4GhtWw-f30Sp-RLBQDzM2rTC_DBTB8UAjGShm5M5KT5zsRoYDm2VPKErVRkC7-I37_wpv4Z0KdnvKbw5RJDchoI04oGW90V6SAruQMKDGkGIGf0fj8Fj_TAiu94XHeyOQ-_zcgT6yU4IZYlcA1PRjdI0AOi8DREliyfH-tYxKJsowcNS5mYnVfmLO4teiDdQxj5XGkL5LU83Un0-hAQPbdU7MaaFNghpyawzT4eHX4DXUyXbQ1nFCv4YnaQJHHtAsqd9Cv7wg4ZdmW41xviVcT8_psHwrESMjv5lJXSP5w9jmriQtSPUJl5ze-xyaNN0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oowxpQFzkdN0UVdHSdTYwT_T7CgelnwDk93BvdVMWElrbiGYrDLvFdxw2Xn6XN62UTILokqfdYn5MxuB75ZZlWEVWJIU0Cq_5syMvM-hbbhO66KNA1bkf9d_2c1iAOl5wWwl2G0Q8V9OMyOZmq5Nli6_kYzK_MSa7VppZLETBfX91qCkjYWsZQWVppmRsKJkI1qD6in3DU9aHhrNCRO9IMp_iXbGoGSk7i8R7yv_hLJA0PlhSm7vNUrKDEdQy7X_av-tIcP43lYmT9pi2dPKsduEGlm6Dg-MOeVbfyMfmQZ3ebu8PfQv28CrV7MySsU2fqkbabxq9YMMGRWCA7uYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDt7PILPWDS71ZbcQ2RXmIeOuEU7UgazyJEuWZvEvFBUfkpfQ0ITgDzGL4PI_98UNkoB1kn5spPwVhJn94_xUn_AbGbn5KUeeDMKxrd3CkRmOZf7E0tX3VW4C1vashFMeMsLccU1GA56-QhmtmbCKNiz_JpXzsT8Snnq9psblSuAWjBOXCIYHpXasGB-aihu-rrNc5FvcxwAvu2MS3XmBilM1_HUvKN5qsBfmKAvcIrguppyzjni8Z-PzngNIOCP_gNlb2osPUMBsrbOWVi8qJcXHLRS9qAdcBhLizmh9bpC8Sb6CE6uC7qKThfMYnkeBq_fyejvWtS6MmS4xrRn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXtDyA9_fWJJipoK9l0pU3-x9xScrRvOh6DjphGAwJjcNhlcleXR5m6VQ9lZKOx7qLkhT2wZF5C5pposyluqT1covy3ePLJvTI7sXCrkD9EbK2ShD28i7tNjwAXzkhTovzEPahawnm9_iy9926v60FET72zjHf2lW1KtwYBWgV7nZ7b6eQQ62MN3LdC4K9_YyNz3OEnN_Lmhz22UPZXFFYD01SLztmHxh_fMHCpOli2s1iYs_1GdgpAHNQ3hC3AtqwsFAnZonNww7BKotfcsg_dmkgjU3tQHu53jKJCxdx0yhP_ibeQzLzdeo7Fg40chj6dW5WQHarEExBMifimTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7tzDjr46ptABTY4s6WFkFKSXQGatA4Llh9U42Z9RJ_6xvyyOICIylPGy1Co-YTHIhU6qqvBercTKuNOXc0hfO7DOaBXeooK9gE9ClaniG661EgBjeNvjfsNU_iM0rgS_sa2-EXkF9kFQl6BJreuwYMeMSghmDal0btpfCpmExXmdmyhqNplyl6Or1WxOtg6snjaZ3kqUmDX09ODM2PqE5cQ2BXb7BvrION8ZCprrAoKfbcvZmdmD4hWTXAkjMDfvC_FJip79yQnX7L6uATIE_7dVY4i1F7eDx6exkP6VDEzQ4mGM46xQwIaHJRkG_6fCpb1EWmp00coJjFWi2Qbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwGsXzD6YC8eR2RWjZxIY_k9yD80Gx8rD4mWiND9YW49Hu-qV2owimqL-Q1KpzutHYefdLGOQ2u0aMSo70wi4G2APLRYNk4H43uIag1o_iGfC4djMroaHyO5KmGdc2i0Ao-WPJ8cmq3jDU8RdqSW_RfhbZn1npwtL_hNRUNEic68veu2Eo0C8TD_b2O80P8FTB21Bqu8HngdEajLPKgv9zGqbrPzWWJJCkDGdsk1aSVsBwWBDNrKOIfJWuu5LLbBR0vTILjRDueNS7_SNdz5u8_ASEciLpTe9Kl80BmwCoiinbVj5ZRkSfLvHWynTR-U-hn9C0X7f5cKEwJxKNdGhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcOdKCMD3rjjcYbKXHXEbbkj29WQKZaiaoMNSRMcUQQUdEUYILFsnc_PsFMbjaY9rG9c0xc2ijiwPnczmk32AmE0XHoq-2nSwC8x6z0JuRO8Esc8MvxBhWR9CuP0xpJPXCEU-s2Ckj0yhsqXUFQlQNIvfiVAbb_m82pePFbePBJtw2iTvw6gJhJmmBgpP4OJ6Ce_kQvZwYLnKYohg4As4iu4pmd0KSL8JQhpLM34Op03SdP2l5Qq0NsdrNVuEl1-rkaw2bFEd1ZerrvMtcLzpdOMz38QI2ZeZDZblLdzuqZgqNdOS5IAOTMEVe-4gLgIZdyvWdKsP5akXKFpFxzU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcC7SaNCeUEijoNnsK3LfyGIMkMDLixpfixCZXdtoQ7NC2Pt51QrIK125sDdczb5xm9syTvGVcI0LN-ktazaNCUMABaIp_zpnu7BUbZruMGszqE8Wl0ZJHmddf7n_1rgxwiyB4Qkd7ubjmRT3vUqI3mhKv30BGGlIlaM9Sy_R8y6DOnAhUSUAdApFyvcENIbyb_uESKi5C_16S_syeryij1FgUy3DUpw6RGYj4B2LKGClE7s9JW4NBh4FnKpQY1XAGGMrs59H9srWLkeVqj01mQu-Rl5jfu4IvDJ9KnIXgn8Aeyrh7Jsj55PbT23iagcrjFJ2i4wZhnl8ysAA7gtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCZcHAoy-9wC3EQQi9zMb-4SIpD5befDbT0qxvpowF9LjRdUt1Gob5r1owQOm_VKH47e6TgwNZe-wTRkaiNjsRfalszAcAwCmoATBHZUX5gUBrxnGjQ9jOXUh7Xo-zBHjbxgmFWfxxnKqfEy8AFuQ95NfEltKB8aPNBc7LaCZfhS5iEdovWU_jd155fcRG4QqzWX5h-LpxJti4f5iJg3WYEEnFK8bpkN02vxMeqIWX57nk4LYRcvwiBT-VinHUm-DpEGbnJVuWnN_Iksu8ewzq7FGF1cSMoq5ROK8K0T3Vn5MBPjczJE03D8dNzwmtmHmz2tICxdST9yMaGxrGsbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qze_jRWZ6NUWE-HLFAQyQPlS9zG13X0XCZaoMjBHzNlRkia4McGG49ZjfpKGjnViTQJblkF7kLy3dxG9NEWM5q-B-mJfk7TGpCRx5UBaIok8G_WzlL1j0RQkds7S_WBPqSLejODImgVP3kM2yjQyFS15AX-ELJJLUJllULo816OmbDvQRWc87qEnWv1tYaAAafX3sa9B9z9oxwKuuMqKzcHU5o730QbCACw7lPhThAuqRO7Mb4NbHkGTOyelQr4nhoqTaKMuRNAyvWW_nGUnidKudNdRYqPV4lbvZKfBp-HKtBl6Z3nqg9_2q-_50rMV_RmzsxRH6xTobCrl2b2Kig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThlxQKcw-xhQiw11YvOC1ZKOP-jkbhZ5wGSwS4LZMRKg5zpL9Hd_3ic-LAcJ-InpLuQHgyBuK9xh_nPElvB3OAlztu0_jcVw7CY1CqK8lQSvkRjVWshxes79-iUoGnJ_XIgNgRHi3Ovqpxf4-yzhIaBwu7qlmsd89pgUra-3c8dYlFz39CBU9wa0eL4G-ar3f-DCi4-c5U_KtnKnpzla1hZF3JPb31taHrCpQ0LuZaSqCEAvPCWhtI-cLSYEfbi0W2SDI_dExDQj9PcuEQf4b4elGW44bw_WsQd4joC2NV4Vd2lGIXsta6P2DjYloPk1TyWRLxkn4L8c78uPNp7CKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAzKXdhgggNMhW9_gtnaXXQ-pXE9pes0sCexohoyGbqW4f2AnRo9WbAvwliq_rHjoP0a7h9Z0MSKoqSWWNuc89b7X_lgWtvhfDxgtJApLXRiGrssLXbZ862yLHDiwWcWuDItUv5Y5AQt4_J1I7xhcBDU29prYT-hwWiK0bNnG9v5G4nnNjRJvYHq8EGBdK071zilp_xjQ03NWrHVfi-K-LR2r9-MpUB6GthXWe2tW7uDYTC9h93saRT_Bk4mWqwb8Z8Bs2pPaShPcpgEAW_wDmoRH-bbYPgAkECcGyLsYYJhNd-Frst0FDWtgYthgPhf01SFQ840FUPsrUnT72VMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97097">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnZRbm0oipLQabHXJ52KK01ySWVuqZaJWXd5ZHNwqetfV4FbVfi51JuXuGhhFPLnQwK_VGHlBm4AWtzmmJ_yClbjNfETyDFHTwCSlMWX7YMIjqWRm2I-1OxpyQAFeAusuGXoAzgaYhZWD9nrTYB3FJS5BKTPr7HpzVrECdMT72U1yDivLO8_JYM0q7KJpU7Tc7B9-mw_Aw-ZiAgPwLYbEQccfJ4GsVegkcCJOlPitA1wjFc4Lyg4hozFg9lZnAktHD_0xQRK17UVAkuxk8tTMUN6goxNP3L1z-b7Rc87mq34cOa4EYQsoMxsuoXZ1WdYbqzNDO8ZBj2JZaLVYfESJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97097" target="_blank">📅 12:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97096">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnSz0VWb2qXm4b0s5F3JZEBlgPzHZrMg_gA2uoNH9CV31uK-_l26We9cPIXa18XT1pO-IT810RLWZ_CLqrRTqu0MIEeISBLLZy0Ap2e3NVb4T832T9dGqcNciuDF1kBH_7JMeY0Kb_GW1bb_el7_cSM1GtidRRrsZRhiwoaZ97KYL68BOy-_9duHUDnz5I3-h8_78bOqcFwlD3iDgS4LHFBGKimF_R5rUBUVzgGSPHSLY5DRvGOrOmC9LOzmeTR4lUQ-lBr1TGf--BVAc0I4lTtEcpKAwaWlBZSkEM9N4O251Wj-CpYDSwmAPawjDnM1BowpIm6JNuxfuDHQZ-FYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇱
رونالد کومان سرمربی هلند درباره ضربات پنالتی دیدار با مراکش
:
"
من سعی می‌کردم تیم را بر اساس تفکر درباره اینکه چه کسی می‌تواند پنالتی بزند تغییر دهم. دی یونگ را از دست دادم، خاکپو را از دست دادم و سپس سعی کردم بازیکنان واجد شرایط را قرار دهم. موفق نشدند، به من چه ربطی دارد و چه کار میتوانم انجام دهم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97096" target="_blank">📅 12:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWZJRqeT6-zprKinpTR2QWrsJJqy8lySCGy61pfVfNPOZniK3a-U8JYo4wdRl9x0h_d2sCPeCkuvcKAsk5kN9z8cGaM5l6GLRDVDb1KUJWmSkzEqUaBiYdi510jeXj3ULj31hVSfMUZIo0t2GfD-Fwuy-tIfQHhiLGViU46uYmiF0PikZAVCP4BPcUlzSqWhTpXmRlsTQatKQl7LU8uUXf_ggf-sojge2Ycegnbs3kITVyEy3YaDqtuZTI-iicHywsAWqyJQ2dae5qaCPE4eM_aFkzmRwbrtyFL2djkGOVtoYSKMm8iTbTFTvRzvIZp8Mnof7mBe6AXZB5rYqTRoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3pWsciNY8FutrMQ0Vehu3q8K5jf3Bfwpj8cauMi1Og1bredAoqXhlZC6OH_fGM0emxA58eYsmVIelVQz-JbbmxcqMI4OGMEyDgcdLa4ZjWxuTO_HHgJswGNE-3sBpiNpQsxv_2wAzKBj20fCNL5EOopdDWfRH7vfhdkCaHPZDzVYThvwBqzWcZu7ooDA1hYEHPy4f9O6Vrs9ulpLIrWSn5KE5Ub2b0gqulzX3L0uW3X-ukTXUsg67klH3omr9CnIYVp84Zrxm7cRBApZoX6Pl_-anlL2Wd50LljaWSxAgE_0VyHh0KEjRrUajS1rKTHqxfPkPt79u03RaopqO24Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKUUgoUkr1TrjIkJrUinjdv9GnaG7Zspa9xdtB4P3NYPu0a1mfa_UQMA0MqHRWd3nBdrHFTGatIbZw-Yu7NaT48h-3zt7wZ_36Wspiv0r842t43OVZB6mQyFsUEJr61Fzg33NJZY01aCiDK0ca5mnSQh-0KrbysIMJj7-MKB_hGcAXu3q3sUu_aF1w492h6gnm9QEiqZy0MTgMJwhyqdd4H9b8sIoATafdS_VHkx0bKszd-VeDafubgPiSXM9x1MD5xMqcAZPf05-Nz9beClKy471IqnqHjLCXLhuQJWJOTjdCHAEfEVm21te9-NOgylwHMtzJPV51a7-dBz0S7RMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇷
همسر اندریک در بازی دیشب با ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97093" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▶️
🤩
حس‌‌وحال دیدنی رختکن تیم‌فوتبال چادرملو اردکان بعد از صعود به آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97092" target="_blank">📅 11:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_B-BiRZR5wfsFMD0IMo9CasS3D4GLnJiTEkExzFb7yF84DYs0TaenszUGlNWtTy9qlCMi5H2VSDj8n56v8CODsOi0YTlutfz_W8WlQdHR_KsxC1uZ0b-Qs9CenIWfxITazFfmj6mxbBqOXRJSzaTI-vf8ob7i_tsSOFQfwFdCHnkcXi8WfP4jwdpQ_KsMpdnH1DVkxS1MfeJvqb8xAug81g9X-9TrbagD1FOMzjaxfMAk70dcG54t-hei5DNuucr0WDuGfMy3TdDRBdLU7sDJr0lYQs9r28byKCrkMoPj9Um07inM3YMZ7vtPK09Oio_mK51Hppi5kaMDXiAwGuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97091" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97086">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjuSvJabqL4ZNGLs1-UdpnYPlYJ862OG4YNMDjGTNzPGF_e13eZ18t01ZvG_Uv7c7_fkmyut-FwSJQQQT-Wu5wQiiOHNIE2uVwZUd6SG6Vdk3ziDzuAfzOfphoxagiYPoTjsS1G878n-1TZaljSAvC5rGHXbU5ivYQaOm8VByMl3Cc59_BK2h-xtCeN9zOuFmsuDOe3ZsNGHOnPYn_l-OHqWdaGUlgT5Zdvu7L6kkl8-pi8SmICqfJNUUfwIGkh1xmBUNnq3Ub_06QOTIy0_FGh0s2PTjs2e9qP7y0KatleikfAWUN6fvHcyDbFYzX_pcpXe7Q5ZbNPwmWmGxomCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0tpJNvJi78OP5zNQRHWGdT9HxdnROH5RY-wn5Wxn7Q0Mh-F0OjknGm1RwdQbbGS3G1O6VX8nxA9ewt6dsLK6GlNBxjeBbS-xRzLu4shr8L1SDIsZoFMom1aTX5TrYfhcuSyDoOjUZwNZ4Fv3QAfd8xdpO3dobLIYtYZLvAsGdPPpASeD32Ct4IVq2SQYRQAky8_LDUw6LWuoeYkHJ1d43aBKdEtLpq4T6-UjWZgKp9uuoIvcTTUcprVblhMWyUucJhYl1fj5pnhZIRDFjVx7ild5DOt6JLALy3NbSL_0SCJWM6jLIgNYS_oRtg3PD7-WkKMITU46xvse0h-svXJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyd9d8x3978Oa7shNzyyHhToIDEgjJlCwq41_dKAfhk7gjyMu3DuGpP0ip6JHka1hmq2sZZWm1guPgLxsjfH1qt1Bv0ssuF5cigLvToLNRKJfVYadE8A37nhMoO6sAoSfRKM9-DBRCOVfymKBNCr-vDO-L8KDOwlyNUPhFHNdY-7AuSCxI7xGuNvJ2AMAGCfVhjF5nF6Zeyo4Q79LRw2ik1Wr2M76a9tgT2L68ytrDpGlDqt6mQJmET01CZlRx1_8_COKqz5zLyLelZbJmBvRzo11zaoVcb0LeOpqHCDL9iOzNx0x3jxRkhdAiMS3t6vq28T_DYC30T5HY7o3sx-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_B2vODfagr7_DuQ3-tlw24giusNarhGulyY3VwLJnb0VF5_Y4vjZwSGVbdeVyCFUAkQnKsBucwr_de6kwv0CuosevsWqW3DXANbrLF0QYxs2f-oW19qeYX1tj7gveWPkF2viXC1EHmPb7882iv28d71zIiJ-ryXNCI_syuAjEOaoEHYICxWOC-54rp3ZIKQS4oFPz064F_66BpzD-sKV5xqKb0dc3trzbAD0YolP78aZaK2SJBj21FsrVx1gALSTEJgC9vw6yuF2RUK-rb3c8k0wKypaFm45q3nuWUtUsi_9pXkPyQiDjpYTWZm0ERXhe9Ox4HqAg5G82aF0vt0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3twTBG2ye8zQZOEzvvjWzbpkJuGYNF4lKUGKBkm-_1BDwBe-va8v2burVM322raJAZLd3egKsEsPupgd-En_b0G7QrBPW2lsVFBYHM5OCqtIbJBMyM0QFowvGOKn7Cca5zXMUX1F3GKrc980lBjLRWsGF99TBI1nHWpi0E3rg5BYHuR0pF6V4c5Aiudh7ej8UEa5iMxRDZcAt64wc-WbCipzob_ayRrv5mpuXh-ERvv82TxRYbRVhsmx6DzCuRql2AAIZQyCaMYCfvXSvHBqcRHRKXjpEsUcTjBU79Ux07aEc3oCz-1Fl_u_ImTNncTEjTaVPPYk0j-5Ig0z6jHgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر رونالدو نازاریو در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97086" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97085">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=I1I6XzFKRDSjf8-kcyOXHOkAatwvzrvsN8laCcpjZT2iAsjX5np5_rHhKJozu9xCtAdSa18no8pNTSR2QwknJQ6rsFrgKV-u0ChP-tzHnyqMasknO01gt2MMLvPyBhiM4ZWUk3Mji3Y6WVzHLB9TOXSZuTTvVAuevHewmGfWbL9HNJYIAHiD3ia8KROykSJ4ymyAzLkNDycQlCVZPzdEbKZIX8HGOin-q4H-v3lKAhqIOrAQD7Rgj5npu5K210HcqIXpGgpXY_BOpwNREVCNzvPYeuZ2bwYP7HIJ_m4KI2hQ5S6bSTgt42y3xK6-rNz8bidTtnkEy7UNbM2x98R4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=I1I6XzFKRDSjf8-kcyOXHOkAatwvzrvsN8laCcpjZT2iAsjX5np5_rHhKJozu9xCtAdSa18no8pNTSR2QwknJQ6rsFrgKV-u0ChP-tzHnyqMasknO01gt2MMLvPyBhiM4ZWUk3Mji3Y6WVzHLB9TOXSZuTTvVAuevHewmGfWbL9HNJYIAHiD3ia8KROykSJ4ymyAzLkNDycQlCVZPzdEbKZIX8HGOin-q4H-v3lKAhqIOrAQD7Rgj5npu5K210HcqIXpGgpXY_BOpwNREVCNzvPYeuZ2bwYP7HIJ_m4KI2hQ5S6bSTgt42y3xK6-rNz8bidTtnkEy7UNbM2x98R4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند تو اردوی نروژ داشت غذا می‌خورد یهو‌ تو آینه خودشو دید رید به خودش
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97085" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97084">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=g8zfCwPMtU2i9NrgNO-2b5C_D3kOG-6eAtktIpOB8NYCPNJO2TP72S9APkFrcfO2-_SX_JuYn4F933BVpZQ-MKniONfS8wVSx9Chc9PVaq5oQ2_XGoDk12gT82zDWllQbWNDsYuV1vmBzjILkCUQTXgM2v5XN5ZT_GoIP-0_3GQjuU-zK_V-cmL8emEpHQzfJROHT_BWRu5lzPuNvxd15RDV_XIR5nzYDnE4C77gik5fs8oDVL0OLXfT4w_3drWHQvn_1qLJ8KCgQR4X1hqSfnxtRAX8B4ZcnJAhUL_015YZB_TwxQI4BC8KXW2BqozZWOkUs3ZOXqK2u0u8H60muQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=g8zfCwPMtU2i9NrgNO-2b5C_D3kOG-6eAtktIpOB8NYCPNJO2TP72S9APkFrcfO2-_SX_JuYn4F933BVpZQ-MKniONfS8wVSx9Chc9PVaq5oQ2_XGoDk12gT82zDWllQbWNDsYuV1vmBzjILkCUQTXgM2v5XN5ZT_GoIP-0_3GQjuU-zK_V-cmL8emEpHQzfJROHT_BWRu5lzPuNvxd15RDV_XIR5nzYDnE4C77gik5fs8oDVL0OLXfT4w_3drWHQvn_1qLJ8KCgQR4X1hqSfnxtRAX8B4ZcnJAhUL_015YZB_TwxQI4BC8KXW2BqozZWOkUs3ZOXqK2u0u8H60muQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
🇲🇦
خوشحالی سرمربی مراکش و خانواده‌ش بعد بازی و شکست دادن هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97084" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97083">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=ikWdOlNDvJ3Vf9eNCnRRROxrqMbqX8QfbJ-BrlmTTlSEvPTBRwDyRTcLnHrwiackUlFtRGFED-0blqYRy3fzsBGRvcnRoVRoI1dc8zmYewOHTDkIwUIj9Cq5UGWmzAu0uoLasjCsDNhMeFMmJUaVbLTg2o93X8cTuzOAy_DXc-gyMf6kbKLHQc9Xm03GBGB_dpthEYd8-npjosoryaHjeymRDMNCysGtASBYcKMgPFhqlP0f7A-kgiipwYSvHMZ4xUznVsaC_dwCMA7qnxRhc_8PNkgz39YX7ELTBuVnZrajdfCOVDWFKYsM26I6X1OOJo1FrIKPCAJ2plNJkEakIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=ikWdOlNDvJ3Vf9eNCnRRROxrqMbqX8QfbJ-BrlmTTlSEvPTBRwDyRTcLnHrwiackUlFtRGFED-0blqYRy3fzsBGRvcnRoVRoI1dc8zmYewOHTDkIwUIj9Cq5UGWmzAu0uoLasjCsDNhMeFMmJUaVbLTg2o93X8cTuzOAy_DXc-gyMf6kbKLHQc9Xm03GBGB_dpthEYd8-npjosoryaHjeymRDMNCysGtASBYcKMgPFhqlP0f7A-kgiipwYSvHMZ4xUznVsaC_dwCMA7qnxRhc_8PNkgz39YX7ELTBuVnZrajdfCOVDWFKYsM26I6X1OOJo1FrIKPCAJ2plNJkEakIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇪
🇵🇾
خلاصه‌بازی دیشب پاراگوئه و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97083" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97082">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIBwfCe1e0wgqPmlHt3Es9ZjwytfSgyhPLnrCckJ6Q2_YaM7VYrt2m3410_nZLxiSz7mMyeY8--IamQy1wTP8ELlnZDGXsf7UzdyRgo8YoBxi23eYPcHxtu-RRyvVNONQPcZOcRthRAuT3R7bHQujqUVZwAzEYVArr9Q4MqDD3sU_kgMKGgl_XFMuKWEr0Fe8ovPSijcJRWBZbpt6elTsJuHP9iKHeP-UqZk7CQSixbc4xCTSeudSpTYM8_cNghqwYrjNSxqG4gZsfgRD9kZizwrOeL2u3gAiXGLMAZFtCuZo7R0Vi3OI5gcAKdcVE79pa_pgk6S9u1OWlRGR-PCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
عملکرد تیم‌های آمریکای جنوبی در مقابل اروپا تا این لحظه در جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97082" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97081">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-text">ریا و دورویی برخی مرزها را درنوردیده و حد و مرزی نمیشناسد.
واقعا با چه رویی میخواهند در مراسم تشییع پیکر رهبر معظم انقلاب شرکت کنند و در چشم ملت بنگرند؟!
https://t.me/hashiyeh_news24</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97081" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=Qtv3aBzFccGQP9cAHtT7y5vhi2NLR9ugN4iZUHCi7_-KCR6YNCQhNuo_cTmapCVnci6fUPCAGGQm5h09U6Tg-q8YFihceS0-Sp2hixIz7H1gjnma6OtzIrB7KGwDBrWZrudcQqEpfy0qwCE9k4BYb08ItkyUOMBrqIgClndLLMdoO_-nErCFao0lmCiCAjWs6xlNmrftKe3oGEDYur3-sGdvsbob7qsVyQntPa6hovKkFp3TiQqnAFkwCoacxmgJXQfc4_sgQciYNz4XG1C6qz04WMZud8edCDqcvJR877725Q87ghBO2qS03SKdA0iuOsqn9P_zpJwo81v0LhG-cLhId-K_n5KAuFV1rzvhUuqEGZAieR3ytlhVuzWIZCvkdh16ES9vzYybullS64ckMY5c29GSCzhiDOSONSfGP7O6x2NJjxpzH9nhVcpss0JXWEO8AzcePjr4mWV7ho5NI9FbyL7ykvDOEofSIsqtKjzBjm-pSyjYLkIgsl6xrbcqxwz_nwRYuWtLe7Jzj3z24kbleCcueU6piuq2v17IBNrb_H8J8iRe_RQpQFOGpf5qi7YUpUFe3AU0O7ok6kYNpgs2xBdC0KpNKSzH6sr9SyrLt4Eta8AtJjJYvpXpKSZP53v2tsQc515QQpYtWIR3C7Fru5cFfeahVlYSnB3WCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=Qtv3aBzFccGQP9cAHtT7y5vhi2NLR9ugN4iZUHCi7_-KCR6YNCQhNuo_cTmapCVnci6fUPCAGGQm5h09U6Tg-q8YFihceS0-Sp2hixIz7H1gjnma6OtzIrB7KGwDBrWZrudcQqEpfy0qwCE9k4BYb08ItkyUOMBrqIgClndLLMdoO_-nErCFao0lmCiCAjWs6xlNmrftKe3oGEDYur3-sGdvsbob7qsVyQntPa6hovKkFp3TiQqnAFkwCoacxmgJXQfc4_sgQciYNz4XG1C6qz04WMZud8edCDqcvJR877725Q87ghBO2qS03SKdA0iuOsqn9P_zpJwo81v0LhG-cLhId-K_n5KAuFV1rzvhUuqEGZAieR3ytlhVuzWIZCvkdh16ES9vzYybullS64ckMY5c29GSCzhiDOSONSfGP7O6x2NJjxpzH9nhVcpss0JXWEO8AzcePjr4mWV7ho5NI9FbyL7ykvDOEofSIsqtKjzBjm-pSyjYLkIgsl6xrbcqxwz_nwRYuWtLe7Jzj3z24kbleCcueU6piuq2v17IBNrb_H8J8iRe_RQpQFOGpf5qi7YUpUFe3AU0O7ok6kYNpgs2xBdC0KpNKSzH6sr9SyrLt4Eta8AtJjJYvpXpKSZP53v2tsQc515QQpYtWIR3C7Fru5cFfeahVlYSnB3WCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی سجاد غریبی کسخل با ابوطالب‌حسینی فیس تو فیس میشه؛ سطح برنامه رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97080" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAOlPJ9tQj3fO-9Vm8abJ0yqBL0ewsziA0Esposz5qmnk0CT_iGQqwXp9IIP8BuSqkA4fE8eYdtqYEmQK7ncGcslmKtAx_cjWXGwkef6zzTvbvrz9RIACn8-mxBvuZu54QJuGyzuIMzeZlrutSeVfjNUTzC_PyYAxwU2gIDtgX_X1iQWRK4Jem9NMXlYVXXMDN6d487gcKJGZ1q4czKWjABqwy4bbEHvfDnlJ_oSB0THYDx_TnNNn_Wz7BqOmVQDuUV8KpqqGCbZ3f6M_Ta1k-sWeq9BszKTmFjap43jpBs18q61D4Iv7n5ISUVcAZjPJyW-2x4nUc7YJzBrePNhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری
#اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران از جام‌جهانی از طریق مهدی‌تاج به قلعه‌نویی اعلام شده تا خیال این سرمربی از محکم بودن جایگاهش راحت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97079" target="_blank">📅 10:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=ZC_QD99_oOzgEwXR0PFx7occOKX2Lm-0zyu_-DE0b3oSPVhlagdxPx3agSure799Ahrzz_6yhmCZ6rSfgeXsBkp2hFv70gaVkf9fwquNP8jLcM3sExsXiKh9LmeNFymS6fdKTnl9tPG-kUm6rVoAhfbpPGxqViee5UU1MoiNeR9TlcXeN83Ag6i8u_hMyWUBWILUCpV5GGRqjN9gONT79HMZNtNJZLzLtSg3YdZxl96zbgEPfTNvBju3A2AIhRQalDtAjStjXSG3VpueuxmPxQP4-dj2IJrCKs3KkrsGd1BrkREkEPWTqvL5V3rDwXA3h4M-AN0AWznhNIC_ziB9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=ZC_QD99_oOzgEwXR0PFx7occOKX2Lm-0zyu_-DE0b3oSPVhlagdxPx3agSure799Ahrzz_6yhmCZ6rSfgeXsBkp2hFv70gaVkf9fwquNP8jLcM3sExsXiKh9LmeNFymS6fdKTnl9tPG-kUm6rVoAhfbpPGxqViee5UU1MoiNeR9TlcXeN83Ag6i8u_hMyWUBWILUCpV5GGRqjN9gONT79HMZNtNJZLzLtSg3YdZxl96zbgEPfTNvBju3A2AIhRQalDtAjStjXSG3VpueuxmPxQP4-dj2IJrCKs3KkrsGd1BrkREkEPWTqvL5V3rDwXA3h4M-AN0AWznhNIC_ziB9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇧🇷
گزارش فوق‌العاده گزارشگر برزیلی روی صحنه گل مارتینلی مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97078" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKZ4PTn3GDM5-Jg9VBokuaANXztFGgCuKqZAwoB7KesFKNImA05I73iGei2oPtL0VQ9wZYJmubvuhgWCL5qdHS5-DPBw1D_J2qX3cm8CgvQBGXwwv7NL45qwTqJAzIlOIiO4G8_uHsIEImP_qItfgXYPlmvvKlwvIUsZsPuKHNDd6ywQ66zvwMiOFvZPNawJFWnHCSONZBK6835HG8acbts_P8oYt_DJd6NeuV0EX-DsTnt7_prGac6LAcq3ELr7Q-Du4QKf9I3wEqz8tutq5tVVKIxHQZsRpOJsl3ORUe9XAHOCQqTSnScveOdzhZEK0afwuPrRBmz24qLF3iEpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
🇦🇷
جزئیات عملکرد لیونل‌مسی در ده بازی اخیر مسابقات جام‌جهانی قطر و ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97077" target="_blank">📅 10:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97076">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCM9aSB0tb7qKrsYnyS8jZpYs73y3W2kSDkVaCxTUJGXGt399WJ-2GcIbtZobYJ_t2aOizOPdDkTCYzPtK5GslL18Uo-xyUvxxOV1QWr6skmedem2MmF3A4V58HMiWgkhxVhLSjEoUKnfpj0E_VGbgZZibx32J-nyGZQzG8dldjAx7amE9yZx4TBkAfF458OaYZmX-DTHbfkN4YR5jnweShZZiPWQGxpOTkt0llCFup5E1r8TRrFiiVrwLM0FGqS4sgEnuJkOutp9D-AAIQu9Bc_JrJ1CIhVVAmSdOOkxYfHiRHfyI5O_WnYEP_0t-0aaeKPTpZULTbYEnAHDQxDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
پاریسن ژرمن معتقد است بردلی بارکولا را باید با قیمتی بالاتر از 116 میلیون پوند بفروشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97076" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97075">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead284c858.mp4?token=tewKye7MGt8FzmHL87MyRGOBRC5fYd38IFtd1WoS6uFpD0fYBDsnx9kChRFHxQpCG2-Dw9kXW1NmOpZWnPPvAQbrrpJdJe1RPJ2lb6S-LlMep30x7kI0NkT4ogZonF_32qeDeNYFwr63yfWa3dHJxESEbXjlHMtWg0DaFy-HKW0mH00OoA2eIVjKsskDxAFTyHX-KG5kqOFlBzj-XhfiNBhO_mtPQisZjnOGwP-Ja72Esqe2SoLj_zkJJjL5VdQSCMtLvz-07lO6rULfxGDzWgbUwrGUbQyXSsGRGhgdzN2RbTiZS0O2iFSxh4rGgIfpzRtzAPpUTSPyP-hL_TysGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead284c858.mp4?token=tewKye7MGt8FzmHL87MyRGOBRC5fYd38IFtd1WoS6uFpD0fYBDsnx9kChRFHxQpCG2-Dw9kXW1NmOpZWnPPvAQbrrpJdJe1RPJ2lb6S-LlMep30x7kI0NkT4ogZonF_32qeDeNYFwr63yfWa3dHJxESEbXjlHMtWg0DaFy-HKW0mH00OoA2eIVjKsskDxAFTyHX-KG5kqOFlBzj-XhfiNBhO_mtPQisZjnOGwP-Ja72Esqe2SoLj_zkJJjL5VdQSCMtLvz-07lO6rULfxGDzWgbUwrGUbQyXSsGRGhgdzN2RbTiZS0O2iFSxh4rGgIfpzRtzAPpUTSPyP-hL_TysGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
وقتی میری میوه بخری فروشنده قلعه‌نویی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97075" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97074">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
▶️
🇺🇾
روایتی از مارچلو بیلسا سرمربی عجیب و خاص تیم‌ملی فوتبال اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97074" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97073">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=ENsd7KP08Jtxchxfiu6wV_gjzpuVpw7UB5jcVi4_c8OM8hYQotwad2J22zspLZRrNPPat-Zpt7N_N2se0ccGq2TnXgWmv_Nr5jnJS6-dmD1qliTQM652PEBb4EsqhfrDSnPf9n20JK5lSiAPROSwfrBZCQPSlObaFZ0kdnhKjbRLf4rHdNJo3zhSdzcAYCwrK6r3Zh5mPyXRtyuTIlK0sqsGiphlUZSSr01GE0V2mlt4BWQL0_saRq-UI3Fcuvqhe3iKYSyJij_HtGL_KZw8epiqFe5b1dwKp60WcZuj5SuLyenUA40pau72PhScxiMLHQv9_1IVW41Zzl8cVjyIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=ENsd7KP08Jtxchxfiu6wV_gjzpuVpw7UB5jcVi4_c8OM8hYQotwad2J22zspLZRrNPPat-Zpt7N_N2se0ccGq2TnXgWmv_Nr5jnJS6-dmD1qliTQM652PEBb4EsqhfrDSnPf9n20JK5lSiAPROSwfrBZCQPSlObaFZ0kdnhKjbRLf4rHdNJo3zhSdzcAYCwrK6r3Zh5mPyXRtyuTIlK0sqsGiphlUZSSr01GE0V2mlt4BWQL0_saRq-UI3Fcuvqhe3iKYSyJij_HtGL_KZw8epiqFe5b1dwKp60WcZuj5SuLyenUA40pau72PhScxiMLHQv9_1IVW41Zzl8cVjyIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عصبانیت عجیب وحید قلیچ از خداداد عزیزی؛ حسابی کلش کیریه سر صبحی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97073" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97072">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=JuQP9fmK2j9qeD60wY0SuFJmnXOSNzd_2v26u-DIZHj-oPsfeSQtrRA0smTSV7ecYb9ag_cnFdM7usuztvCdqA0WeJbtAWO1GXV2qRBUwhHYfKSRufLlX1g2jMMaDuyAhqvdIBoBXsCOCrllUTmNMkScTeTQWNY1qDDH_IWw4IPndM50MyOyLhPfpeCz1-qDocfWoz1JNBfSOrhpaQouVTSQFsTHb6xkC3HmNdmGuULGBdZ-TFtXb1NNA7E-Jd35RpIcRTuBhTiwmtJ9cN_zoQuiz8ToHlhAcHGe_4-U0i1hU59gO4J9tER9VFCGnSi461D-PJulfVadycVNcQClEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=JuQP9fmK2j9qeD60wY0SuFJmnXOSNzd_2v26u-DIZHj-oPsfeSQtrRA0smTSV7ecYb9ag_cnFdM7usuztvCdqA0WeJbtAWO1GXV2qRBUwhHYfKSRufLlX1g2jMMaDuyAhqvdIBoBXsCOCrllUTmNMkScTeTQWNY1qDDH_IWw4IPndM50MyOyLhPfpeCz1-qDocfWoz1JNBfSOrhpaQouVTSQFsTHb6xkC3HmNdmGuULGBdZ-TFtXb1NNA7E-Jd35RpIcRTuBhTiwmtJ9cN_zoQuiz8ToHlhAcHGe_4-U0i1hU59gO4J9tER9VFCGnSi461D-PJulfVadycVNcQClEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سید حمید حسینی سخنگوی اتحادیه صادرکنندگان نفت، گاز و پتروشیمی:
با توجه به شرایط فعلی، احتمال دارد مدارس و دانشگاه‌ها امسال نیز بخشی از هفته را به‌صورت مجازی برگزار شوند و فقط یک یا دو روز برای رفع اشکال و حضور دانش‌آموزان و دانشجویان به‌صورت حضوری باشد. هدف از این سیاست، کاهش ترافیک، مدیریت مصرف و کنترل شرایط موجود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97072" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97071">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🤣
وقتی زودتر از تلویزیون نوتفیکیشن گل دریافت میکنی ولی کونت میخاره نمیتونی سکوت کنی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97071" target="_blank">📅 09:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97070">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoMHBEgMsMVS3qSaChdzfD_3vF29vUe90-m62zW-cocp5LfdlopgivGtUvAICfCYnhTYlFHbssRDSdOxdyVIB4Q0tkFpnRrXjXoNg45P-MnInZwFylmud7iUw0K3QNK7j8GliViBXfT8xUaWbgUWmeT0CBob0KaxhTEbIwvIZMvG2PS-IVcp5kCJfaHFmVPHzlimc4VnUUzsKVAbrYqpGoGVC3Zk5lCMIeQu973Tw7kVOn3M3U7bsD9yYbF3FKXrAXKoibOD5WNbSGfRZg0bnqqRLa0ClVVbO77ouRFHKMPHhB3vFEpnSg1Oh-NIU46MkefCj5ZHWCYBDvUMpa08iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بوسه‌نیمار و همسرش در بازی دیشب
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97070" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97069">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=f53vin-FUrosUvR3FZ6PwxwcdpUCHsLIh9GVIW4GkR1K8Zbn-8eX9D4-FK3AUuEgJBqOucCN4GCD8YVO5mCrPeI7XKzDY3mu-1nz5jRQHCxkUHJfeoVZr7cDxY-tpY_3p4-sQ4GmkuP58tPQFAfNraTS4s71yTOG2UUklgTb9qvCyZ-5doExuYL_LCAyGBJ5ki6wJEUR4ajXSp1dpRP93Hm8UmfXn090VU3YJ9AqvpyRNjFhC9QyrSCLzuKJ85ZIkvmIGdg5p6lCDBhcnzDkVSZxy0hjveszn4LNV1FqVR7OAQeUvEJl1igcOMLaVt9XZ09h14tNqfhSUIebPfEQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=f53vin-FUrosUvR3FZ6PwxwcdpUCHsLIh9GVIW4GkR1K8Zbn-8eX9D4-FK3AUuEgJBqOucCN4GCD8YVO5mCrPeI7XKzDY3mu-1nz5jRQHCxkUHJfeoVZr7cDxY-tpY_3p4-sQ4GmkuP58tPQFAfNraTS4s71yTOG2UUklgTb9qvCyZ-5doExuYL_LCAyGBJ5ki6wJEUR4ajXSp1dpRP93Hm8UmfXn090VU3YJ9AqvpyRNjFhC9QyrSCLzuKJ85ZIkvmIGdg5p6lCDBhcnzDkVSZxy0hjveszn4LNV1FqVR7OAQeUvEJl1igcOMLaVt9XZ09h14tNqfhSUIebPfEQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
ماموران امنیتی فرودگاه دالاس این‌شکلی به  استقبال تیم‌ملی نروژ رفتند
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97069" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97068">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCuxG1pjk3Ob70igmN1YoSdwOC1zgKf1Fme_Dt9-F1C1PPwTutFYt8uyWwwMfre7pBJlTGRN3T2Z90At0XYU0pkwKuGJpu17KqFCjixlwI0PZoEfYTfWSH5JnrM0NtX_ZH45xqc3AClDzaGJMRLxks1-Fhg7wb_yTLfzsOHxjO0dUBXr1DwDndZ7yOrVEKAg_W5nh16DK2ipikuRlcTSrjoFh3U8FtRmP_YznWhKuublKbL7xQjUMKGN2fSNrwU_FPpEVjpSP_OuI6Ei3xpxt_-I5VOEDfJMwz9tOXsXpvgmz36lpAm-kG5FxCGKTccW6KFA4tVonIphxNBRqmZ3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97068" target="_blank">📅 08:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97067">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG28k-zRurAQdzbmE605Srknusg86CGCpqVggPV39BcpEAEeN4xuKl6XV3lJqqA4EvDPfjpBhFOm27dOC0wc3OSRzzBSXcRcuKMoxHajdUmRJPc3iNJHRwOYyG_SYkpIEPjskq87iNUK0ZSU7fK_qiw1vSmiEFz_CCXPvIJUeSgXy3rtEseXMgaTfNbIDIBR95hVQ9QXOF1hcb64WUI1-WVzMQuIHtpV_-1CEaoe-4hGWP0B_jxpgnJ74F4Cxu4KJuesapGzmL0raxUBxPhEVGyoPz1cRlO8N-xdxt5j_w5CHkHqsgJwT4qEaSZGNcUD3BUnY_o5_e0m_w-M3cwp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇲🇦
اشرف حکیمی [
🇲🇦
] :" بسیاری فکر می‌کردند که این فقط خوش‌شانس در سال ۲۰۲۲ بود ولی ما نشان دادیم که قدرت جدید  فوتبال جهان هستیم"
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/97067" target="_blank">📅 08:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97066">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNVgJPxizvBYC1rqaDvJL3vd95qHbdIKJsmrB4HYSvnCuxqRJwb3y7IUC2Vci2PyNIOVYFA-dCMjg6W4ZIAei7WKsGl6AX6kfvi6golneEsrojofhmC6bbxbOJgnNPwx5fL6wg3nTBJf8UxFveVgAHvgXlZJCEaK6l9byNgD7mOPa3lAGROQaOWQalZJIStX-A1GKwUclaTEaXsrwI9iIv2LbOA9jGCzt-5i_Y-V3AOTA4qM5aUPKf1bg1-g3NngNJgiAX2XT5C77Z1kRqpFqeXQ_z-eeKTZ215iA42rjIqUofLT2IrXGI0SThlgaxf65RMwq6dTrN6JiEnsZh7xkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
🇲🇦
آمار بازی حذفی هلند و مراکش
🤯
🤯
از 878 تا پاس مراکش 800 تا صحیح بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/97066" target="_blank">📅 07:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97065">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBE-KysWKPUbyn6mSwusotrAizle7yfC7YnB2eOyKVv42Eol7cYkCv0Bg2TRuueDDwgjQExKKbnRWx4LcYKqrWLulfPDySvuKuACkWTovy-QejS0_hUuanAJWX8uB6vavoIst85vhbWqT2ROyd_6ZETUNJdWAy5fmbtrjri9g6ktVARBwE_PXCa-hla455vqqRBzeV5JbGEZa79NHam9J4pwOUnsr7LckOE-HEjxXpPIs8CF-mPEPfG8iM_LR_ROl5uVBwRsEL5amrd2ItBlk1SuRqeg5ZRYsUk87g5M26uD6lkiIUHN-27TPNCp4Y7gbxAV7uQ--W2JbwmmnqZs3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
🇪🇸
🏆
بازیکنان حذف‌شده رئال‌مادرید از جام بعد نفرین‌کردن توسط ژوزه‌مورینیو
❌
🇹🇷
گولر
❌
🇺🇾
والورده
❌
🇩🇪
رودیگر
❌
🇳🇱
دومفريس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97065" target="_blank">📅 07:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97064">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2S0qMqKZ7tz727HShqSiUSwiUMEsglELzbc5XawwiCDLk0Nr56iTPCTUiz7r3ZnB6lbOni6sO78vZgQ5hbJ-Tdd_qnIfwJ6lL8oMxoMfg-3fipBYy_d6CS3imk10Wc27iKOoiXHwd3i_1xYLHjeXB7ShLgeaFjsVv_4c9YAMj7JPpuyE-6y4kqMPDwYQk7gWX3OD83MiLDm0S-hsuKtg28hzHxkR181OKzANhTAFDaB_vNDotbbFgYosLRkFbZxTTJtFFvgiblUcrRaGIj5q4A8qNhuyYHfuuRGP2BKTuGyRLFEF6yceCziS1G7OEd43ZzLrjcZtLEHtLgtTqhSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
تیم ملی هلند از جام جهانی ۲۰۰۶ تاکنون هیچ مسابقه‌ای را در زمان قانونی (۹۰ دقیقه) نبرده است!
• از آن زمان تاکنون ۲۳ بازی انجام داده و در زمان قانونی هیچ باختی نداشته است و یک رشته ۲۳ بازی بدون شکست را ثبت کرده است.
🇳🇱
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97064" target="_blank">📅 07:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97063">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es99UWCuw5j_svTNDyQyDIXUhAis3DBXfUNY66CiqUqfq1kcb3uCJCyhs2AUqL_Mmg05Ap1smIOUkmmE35jcs4K69RiETVJsoUdINuJvGtugU-ieztnVetOgC39euhNXsbduO5O32QSUJwEi6lN2leHPcwWiOwjplnUS_uVRwit5Yn6g7f3ti-d-DJ0TGGUm9PrHJucHpVqze4rDGFvUZr5LovdMIUxrigaq06-jUEG8LzCwLfFb-gBMudETZ4skuGp2wbk8tDsAO3PU_CpUAgDyzNy-xiJCJJ8dZY5dgFHbIFMc0d4K6QuKfaO5apdVHIYRysich49XFZg8_ODn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97063" target="_blank">📅 07:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97062">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACEJyTq8D2fpI0dTV8BH2FNzZhjDZplNCugr1ZvawoCgiVIwLG2JPZlQnIw5cbR6o5wdidpKKl9_A6DMFt5FRzjeom6hTWB8JFHgivE0ZWWjN7lkBveCkqoKJvKv7OVt-059uldOoRf8dKvPzwu6XsIVgYMOxpW87SxXPFA_r8B5M1fsjPM9P36xLWyKrYrNi0NiEvzSTI4T3pKnykeHQHqGwR3lWa2hMtl2kaqhBlvvZJRDu6UTkW1Xhb-WEfg5akuV9hvTlsWefjim0834QyX3V-OinOHd-R6nf3MhtrpuWcKNfx8sTtgQNJi0NOZRGxdykBH8qvhMrzkND4cxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
یاسین بونو، دروازه‌بان تاریخی مراکش، اولین دروازه‌بان عرب است که در تاریخ جام جهانی به سه ضربه پنالتی پاسخ داده است
🧤
🇪🇸
در سال ۲۰۲۲ دو ضربه پنالتی مقابل اسپانیا را مهار کرد
✅
.
🧤
🇳🇱
در سال ۲۰۲۶ یک ضربه پنالتی مقابل هلند را مهار کرد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97062" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97061">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDSL9O6fc2My861seG_-s--Lu18REV3TbPbNkgbFAtSP3IGwWnwTktLAAeku6InO8lg6Pgofx84wcLYveU8FXuds6_ZXiJ47btjDMNWsEToUESUY2ASbC-BzVZfqyetMCq88iUi6gSPU7oTkKQYzT7e5cTQg6PnU3zNIuArn9p_5nzMIziew_Wyfn03iMLuU4tM0wWx-QZCo_HxNJydXLkw-Dtc9sAzH40jTsPHDmPXg-jE-9UaAnlVla4MroXEqWSbiyeCnpcw45D65z64AKZvnyRLWS_8B2qJLr3Ee64jYbplerav8doRJK5U8rHzp-3KJ0NnADXQ79NKYZK7AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇦
تیم ملی مراکش به شکست‌ناپذیری‌های متوالی خود تا ۳۳ بازی ادامه می‌دهد
✅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97061" target="_blank">📅 07:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97060">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4km4ZN9U-vbd-Z3I-GEDaH_mjpSlvtt9k8YAr1gv_4xSefPn2gt_PQNAVr8iZZKCeN0H5IWnalrl71lwEXXrtYLKAj6fZU5AZKWT2V5Z51y2Sabc-IB2lvXwEQVb7l2dkZFGZIYShHpvlx-CC7VOQ3Eo_pTKvpHcUe4CLjZTSDF51P3Xhn9S4SMT958UggM8fUsNV4KeaTEDFwZ5C1mAhpRxfcLmpZIX3Ln5TFXP4bbkV1LyiXfTsVMfyuC8Is-eIwzoHjPw5YnZ_rJ58C3-l1CZyakbdHlmUe00T_IeDpIqToDe1ORnD2pNQW7yHG_REsPCUNkFTunkmoDDOEPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مراکشی که تو جام جهانی 2018 از ایران شکست خورده بود تو جام‌جهانی 2022 و 2026 تونسته اسپانیا، هلند و پرتغال رو حذف کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97060" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97059">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSROOrJ3VmLS0s1da6wFHeKg7bJ_SR67Ddrw4-zWWVxJXQ6NHc7p-xN8XAyxmYiasuTdU4QuPob3h7etxvzm9J-g98jIp-ihP9PuORBTI9yyuar-i2rSAbPQMqvSZPBOmeZTijX4W6N3vwIAFtp6sVEChmpjsGvwkYF0EaC-nOxuV6CrvV5ww2guk5Qxjl89d_8gYODLEbM-LBNRLA1c3cwjXLVT_OmUm__cUYFzfImDUiwWO7n-VVWsaQn_XRJ_x4Vhir2tVBrgZN4taE0zBr4NbcwMeULTQJTbyC8NV2v1FYPrCRAlAOsnnpo6Q61K6qlEvzdVjLesR8wwLLq1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97059" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97058">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh2uRxNrkHZtGdr-GsI-Tacd6kk0mIrk8YNKMcY0bBydiQD-hXzY3E9Ss6Hw9sjAM8j2b1ggfnt32EMGPQEO6j1pjPFXWLWNLg25npIET-gAlE-Am_Z_PZDp53SXEPgMhStNESdmOcfHAVpul5fe8iCg6WnC98DPtPtj0iGWoJ6EnIuRNml2gqRIYGyxANmW6ftDI_s0SXT8e67FKS6Jx4nhkQtiGVcvv8a957dBQvreyhux8lF7lzBxp3cijH4k9WAA-eYAnVE18vrzPrieIMry919WUNQV3qBnfSgQy9kql9nPC38AQ5KvAhNoz3QXC7creHftF7uLK3wZBpxQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ مراکش با حذف هلند راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97058" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97057">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گللللللللللل و تمام</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97057" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مراکش بزنه تمومه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97056" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97055">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بونو اینم گرفتتتتتتت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97055" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97054">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پنالتی پنجم هلند</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97054" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97053">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چه خبره امروز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97053" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97052">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اشرف حکیمیم خراب کرد
😐</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97052" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97051">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آقای کومان ریدی با تعویضات</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97051" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تیمبر پنالتی هلندو ریددددد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97050" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97049">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همه چیز مساویه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97049" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97048">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مراکش هم گل کرد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97048" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شمس الدین پنالتی بعدیو میزنه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97047" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هلند گللللللل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97046" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عجب گل کصشری
😂
😂
😂</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97045" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مراکش دومیو رفت که بزنه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97044" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کلایورتم تیرک زد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97043" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پشمامممم هلندم رید بعدیو</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97042" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کجا زد
😂</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97041" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97040">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خرابببببببب کرد</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97040" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97039">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">العیناوی برای مراکش پشت توپ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97039" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97038">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
🇳🇱
هلند
✔️
❌
✔️
❌
❌
◀️
🇲🇦
مراکش
❌
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97038" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97037">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97037" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97036">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنالتی اولو هلند میزنه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97036" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97035">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بریم برا پنالتیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97035" target="_blank">📅 07:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97034">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🏆
پایان‌بازی در وقت‌های اضافی؛ ضربات پنالتی تعیین کننده تیم صعود کننده خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97034" target="_blank">📅 07:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97033">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دقیقه 119</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97033" target="_blank">📅 07:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97032">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اوه اوه این چی بود گلر هلند در آورد
😐
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97032" target="_blank">📅 06:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=etoWBJXWSD5zf7C4NbnKgxDsouC2MwwQm4vdzroU5ne55vRfJv94LCKkTrwIXund0R5Hd2-FBTTtoI0S7MIXylfRdjhTzfJSMm3GfxtW_2ZvLI9PaR-iqB7_FvaVETjQsG3F4q2Fqt_P5397Haiir9t4RUc1sf7sFWOgjpP4gkrAIU82KdlM2quaIruucE8YgncPe3gQ-Sx8qs5L5uh5DpBC0c3Q5zRHGR25QtFAVHFTuNSX9_tl3YfsVDEVkPZ1vhOoxYQyQUtUFwT_Slo_mdHGvyNTp_53WaPQEGtHY_nVbz8ekEba0uRGAlPKHyPe5iCWwfLwbguFl4Pl72ea-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=etoWBJXWSD5zf7C4NbnKgxDsouC2MwwQm4vdzroU5ne55vRfJv94LCKkTrwIXund0R5Hd2-FBTTtoI0S7MIXylfRdjhTzfJSMm3GfxtW_2ZvLI9PaR-iqB7_FvaVETjQsG3F4q2Fqt_P5397Haiir9t4RUc1sf7sFWOgjpP4gkrAIU82KdlM2quaIruucE8YgncPe3gQ-Sx8qs5L5uh5DpBC0c3Q5zRHGR25QtFAVHFTuNSX9_tl3YfsVDEVkPZ1vhOoxYQyQUtUFwT_Slo_mdHGvyNTp_53WaPQEGtHY_nVbz8ekEba0uRGAlPKHyPe5iCWwfLwbguFl4Pl72ea-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللللل مساوی مراکش به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97030" target="_blank">📅 06:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇲🇦
مراکش
😃
-
😃
هلند
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97029" target="_blank">📅 06:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg0dHCBLuLWiUlZYtKhERY3Y7xLH9x6vzN_75z69vGHeb-_78xv5pNKcX_VYC6zYN-MrY2oMVs0JCWOhdAlstBSI-5mZ-Fwz9fhRKu4lSdL3M3Y3lKZdstz8YxdiJpN2aE_N4pUz80_gROPsbeh3lvtvMj_yKu2NiBUXA6-Zxf6RVyh5VqTmI72wz4h2fuXYp0O5LajLH4IpWU8r3U2ApO-ESOMOte8Xk30WSQfWdlyqbowNUvYWJ0BAmEkwLHIoudTJ7SlqEkrueJ0Ll774X78GUIkbtTf5l-leRNwCjl0pTU0PUYqFUxKuCesGz-ZIZ_Fd-eWxHwtrIm7JkW2jRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فن‌دایک رو خدا وکیلی
🌟
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97028" target="_blank">📅 06:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پشمام چه بازی ای
چه دقیقه ای گل زد مراکش</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97027" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97026" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گللللللللللللللللل مساویییییی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97025" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqjJJLQpeSk_5EMJqLehlGeJ-nAM8eLd9D7k1P5mPugopRmFh0dQq6dk3_C0e2eF6pzer-7jyqL0niW5Zh2XFe9EpF59TaTPAXcEaEuOdWOaxNPjDM6nQbe4ZSg8TthPiYdXxx7mbroFXuQkUH81NjdBv77PP9DAglnZ7EZYXxeL4-qiEKkrE4Jt9_mOI186pUAa2TUL78MIGrvqVwpcLmXRnORt6B2RuqJ42jl8IVaJOTKheEYXxEiAZdeobfn0BUYtxATFNA5XzB3gMpPEz7UHGIsWrnwU-x5qKyZMecUMk6kCEN0aUQmlJcYtQ5SXu4_B6n4FOluKqpr6jrcWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orld0TLhwMXF--1uyVzCL9_Z2xiKVbkdafZ91ZzWZ3asTsQk3-rUXimcGs6tNGJHnQDhCRMT3gm3-xYJ5qc2lt-ixxtOwEONr1Wkkav_RvT2dIrrfyFzrJ57fUpe0uGFij0qaR5EdrNC82xGT5-qR3p-shQzGVYq5wb9wt_Fy4sNTf84gsinGu8VnLlwl8SmmCOYJCelqdrgO3yJajvWYvJmYJG2bHFtxqs6WJZGdb7XSuK4HKXNbvVB20v_qRYfBH5g0FPk9A6L-iSc2oHem3rFCWVU0o2NzbNFYzZidYTkak_z0hvvHu1uZ1HLZ6wrYW0vxgbY7jdSpfeTLNz47Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کودی گاکپو بعد از گلزنی به مراکش به دلیل از دست دادن فرزندش نتونست جلوی اشکاشو بگیره..
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97023" target="_blank">📅 06:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=EcmztS9Bf5rYQq8h1JWoif8DP74E7HbgQUTvMhX--kYFKATl2WxwqEFvq4wgv240RGNVAKqNmfoXN-Mjjnz609uUKmFMLSKyu1Wx3VUJphc_sAdnfmGNZkWHxx__-t0fFkUY0rJeUay6P3PF7qjgcTtUTwxNzdg7vEyg_xojq9TwEsD5D4lcj3WqvvYsl0sfnT-DLPqCzLS3eP9gPWy0NA68QXWGS4C6jRIbww0gFcv5_Q0EQYldpZs-WCg9qqGlfCMLYfHOlvA0k3IqiPb32Cah2lxCkjz-ooVEWTEjrX8xrmgICaBxtoKO2_42jtqzl_JoVVDB2Fop9tHx6QwbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=EcmztS9Bf5rYQq8h1JWoif8DP74E7HbgQUTvMhX--kYFKATl2WxwqEFvq4wgv240RGNVAKqNmfoXN-Mjjnz609uUKmFMLSKyu1Wx3VUJphc_sAdnfmGNZkWHxx__-t0fFkUY0rJeUay6P3PF7qjgcTtUTwxNzdg7vEyg_xojq9TwEsD5D4lcj3WqvvYsl0sfnT-DLPqCzLS3eP9gPWy0NA68QXWGS4C6jRIbww0gFcv5_Q0EQYldpZs-WCg9qqGlfCMLYfHOlvA0k3IqiPb32Cah2lxCkjz-ooVEWTEjrX8xrmgICaBxtoKO2_42jtqzl_JoVVDB2Fop9tHx6QwbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل هلند به مراکش توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97022" target="_blank">📅 06:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خاکپو
🔥
بر خلاف جریان بازی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97020" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هلند زدددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97019" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97018" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=fHZ68casIyQXxUHw4lxkYwfOv57Rw0DAT3amwDzSy9UKOW99zhv7b7NLtMWN75UdtIwGETXeHT4cqmeXCtA4FzmaZS2as3hQi5gnCozFnC8yYFZ1i27NLPbv7l9d1On5OXmSSd6TMFU5-3rijgWaO510YpfPov7XOy2vxjKDcngi6qKjP3eNgfmhEWNC6WjxI4CHUHG8NMnKmhihcgeOu2Yu3G8vCuGOIb2fYi8Mt740ULYOGyDBlay016H8a0qJC49_ZoaGwg0Rzy7cx5phJY8K5ZPm34HntyOE20Odmq27g_RWnyW_vHFx58m51y2zrh3gJE7ip_07gB560aiYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=fHZ68casIyQXxUHw4lxkYwfOv57Rw0DAT3amwDzSy9UKOW99zhv7b7NLtMWN75UdtIwGETXeHT4cqmeXCtA4FzmaZS2as3hQi5gnCozFnC8yYFZ1i27NLPbv7l9d1On5OXmSSd6TMFU5-3rijgWaO510YpfPov7XOy2vxjKDcngi6qKjP3eNgfmhEWNC6WjxI4CHUHG8NMnKmhihcgeOu2Yu3G8vCuGOIb2fYi8Mt740ULYOGyDBlay016H8a0qJC49_ZoaGwg0Rzy7cx5phJY8K5ZPm34HntyOE20Odmq27g_RWnyW_vHFx58m51y2zrh3gJE7ip_07gB560aiYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔺
ولی پسر عجب اندریتدیه این فن د فن دفاع هلند؛ رسما تو این بازی کون لاله‌های نارنجی رو خریده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97017" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npwrFqsVPa8HMwk3s-Amh0lBDuXo23qQ6uFWc49Xd1YlOxbAkZyOnCyuZMwAtfiRHK4UXRBSKmAsqiHpPN6wvMK2sz5K6Pr2zhL7Kmo56g5n2iotfH8uFldIfoe9mzP8qG1k4xR8oKu-WbectF4OdnOnL_zIcU1XznLN_HBNkWFylvJQjaRwIheZZmnRTc6YhlAqgV9ybpeDpc9LiOF806m3EP2TnjZn8OoNnMidx4Sxd3XksDSzV5LqnZEPtrbYFCiIeBK6J-x6iHhOJp5z6yN0JbEFDS2POKvZontQcbTKlb57oPKDjxR-DfnVu9L_jpgNjfob8qZSg1sDdMZsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
آمار دیدار‌های تیم‌های آمریکای جنوبی در برابر اروپا:
🇵🇾
پاراگوئه ۱-۰ ترکیه
🇹🇷
🇦🇷
آرژانتین ۲-۰ اتریش
🇦🇹
🇧🇷
برزیل ۳-۰ اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇪🇨
اکوادور ۲-۱ آلمان
🇩🇪
🇺🇾
اروگوئه ۰-۱ اسپانیا
🇪🇸
🇨🇴
کلمبیا ۰-۰ پرتغال
🇵🇹
🇵🇾
پاراگوئه ۱(۴)-(۳)۱ آلمان
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97016" target="_blank">📅 05:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بریم برا نیمه دوم بازی</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97015" target="_blank">📅 05:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97014" target="_blank">📅 05:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎙
یورگن کلوپ: «اگر این صحنه خطا باشه پس آرسنال هم نباید قهرمان لیگ برتر می‌شد. اونا ۶۰ درصد از گل‌هاشون رو همینجوری زدن
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97013" target="_blank">📅 05:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGPtd6BoW-0cfeejyU493PRGyGZPEY4nUS2k4RGw-1P4HSiaRzjm-QCJAq7NOV_inzOfxtHhZujymd2UhT0FXMBekQT7vPxoso6tOfX3e62lz7wTj0lQUqwLzQ3Q4LE6QvdZNi-l0Exqhs2mc4G-ElubelGRE20k1Olc8C7Rm3CHIr6Bf-W6uSYJzVz8FZ_eE2Th8YZGc5W1H2hEoLUNJCl4GgCg-BPmXzmSWz1lMFnWZ_qxD-Lnpsojy6559JWYYDw8rBtUB-EOjLXn33pLOZtq5Rb_VZcY0_aH--JNpQnQGBtW4AJwwUdedvgGMT0hkEPcoMMayVTy3PiZgqSKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97012" target="_blank">📅 05:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97011" target="_blank">📅 05:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyERt_xvtGmI8T0_EeSi0UMBbo7SRsM7ouVx6uTXoD5jz2WTFtqGzwq6iAotgY_E2TpV3nmIHbGa2jRveIvmwQUiSBMnbLtEGYC8sNN1f0E3VweZK-X_gPUu_0Um0FVLLeWVoRzAn75tKITywo01o7OZa8tIa5WOJEPdjaKYAzPEkFyBmVOrYFScjQ6VCxkbAlJE7RLJwTFdyC5bE9i-AI77HWhX9OxNPyCcKyp9dG_EE03_4HfckCqdvCTvJ1Iby4mvjzdPu7aY-2p19FAUQ_lYEdxRQcxI21Ych-Hs8y3SZ5teVdnTi-NdQrQqusxFceiJ4-yVQcEAY3v8oFny3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه خوشگل مونتری مکزیک در جریان بازی هلند و مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97010" target="_blank">📅 04:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تموم شو دیگه مشتی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97009" target="_blank">📅 04:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کم کم بریم برا شروع بازی فوق‌العاده حساس مراکش - هلند
🔥
🔥</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97008" target="_blank">📅 04:28 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
