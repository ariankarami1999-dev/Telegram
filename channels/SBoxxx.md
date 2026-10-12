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
<img src="https://cdn4.telesco.pe/file/a0_b0c5kNdR6XVf6ZV0zDvj1_MQpr_pfo-Rk00OUkQbBtP5USHC07L6nJaLrfK1H7QCGxm-1dGb6Q28UffXKFFT7ez5v5PDfjDx3mKKBbJYx5Kwm83b0i9WlJe5DDNHbkOuiaPZ_3GnyBDDLaD2bC4DDO9b7L8sv3Fu6vQgfxtyLeCoHSLsHLTKHMrHqk6YBiMmsGHy3W8No4mHQf4YtulL8UAmFkvBBcwIWuuhSrQBp_4xCyHBsNYY_7eJ_n3OXN5uV6-AFmExlUi4KQaG1jNMQHqaIEStJUxqz5IZtnL4dO6387zUXhbkx98QWqrZEDTwqHdddF6YTYzRmZhiYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-21643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrrF9agRr4IH_fqf6SJ-HuEBSW6J8qAFZNKqJKcvmj-1_4AVzm0Etma4RgBqdMSqOSF_LDmvyfOp-NHUqIIn_xLCW9tZzMsbVRnx-oXntiRZhpBom57jlYxJw87SssCAlxM_aySXLvy769afGY_o11yhXCAV5jDpfqAuNWCcp4ZxdoKaH14bJ8iMSyeepYWOaAYzp4d-TEQKzNdZ6P2fy7VvgBfsmRukXLJx3Zfup-yCqfqD3ktt1cKa5yjMx5oL6s0VRGOmHI1HIDn8B_guMcZERm33LYB1lTt4KPazLZsEFuqpujzbq3xq9cIxMrSTjl2GOWONnI4owLKSykMM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران هنوز تمام هزینه اقتصادی خود را به جهان تحمیل نکرده است
جنگ ایران و اختلال در عرضه انرژی می‌تواند با تأخیر، هزینه تولید، حمل‌ونقل و قیمت کالاها و خدمات را افزایش دهد؛ بنابراین، آثار تورمی جنگ ممکن است هنوز به‌طور کامل در داده‌های اقتصادی نمایان نشده باشد.
تداوم این فشارها می‌تواند بانک‌های مرکزی را به حفظ نرخ بهره بالا وادار کند و با کاهش مصرف و سرمایه‌گذاری، خطر رکود جهانی را افزایش دهد؛ تورم غیرانرژی، انتظارات تورمی و بازده اوراق دولتی از مهم‌ترین شاخص‌های قابل‌پیگیری هستند.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/21643" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ در حالی که به توافق تأمین سوخت دیزل با مسکو اشاره می‌کرد، گفت که اتحادیه اروپا ۲۵۰ میلیارد دلار به روسیه برای نفت پرداخت کرده است، اما رسانه‌های آمریکایی ترجیح می‌دهند در این باره سکوت کنند،
او همچنین تأکید کرد که تنها در منافع ایالات متحده عمل می‌کند و به اصل «آمریکا اول» پایبند است.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/21642" target="_blank">📅 17:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
شریعتمداری
:
درصورت جنگ مجدد کابل های اینترنت و فیبرنوری تو خلیج فارس را قطع میکنیم تا علاوه بر اینترنت ایران، اینترنت کل منطقه و جهان قطع بشود
﻿</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/21641" target="_blank">📅 16:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سومین تانکر در تنگه هرمز به دلیل عبور از مسیری غیرمجاز از سوی ایران، به یک مین دریایی برخورد کرد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21640" target="_blank">📅 12:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21639" target="_blank">📅 12:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
حملات پهپادی اوکراین به دیتاسنتر روسیه ترافیک بات‌های یاندکس را تقریباً به صفر رساند
▪️
در پی این حملات، حداقل ۸۴ سرویس ابری یاندکس از کار افتاده‌اند و ترافیک کلی شبکه به شکل چشمگیری سقوط کرده است. این عملیات در پاسخ به حملات موشکی مسکو علیه زیرساخت‌های فناوری اوکراین انجام شده و کاربران روسی را با افت شدید سرعت اینترنت روبه‌رو کرده است.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21638" target="_blank">📅 12:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♨️
سامانه دولت من در پی درخواست افزایش ۵۰۰ هزار تومانی کالابرگ مختل شد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21637" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kek0vv7_mkdi7H6HNYyv_X_nkMQrrQ-REiEZmSs8z_yQT2pVYUDaw0YbvPcIuaYo0-Y8_dgIewJkDxojfnc61-SMM7dV0DGMIQNso-E9fJN9BTmP0tBUQk7WEysFIwtaKQ6xIB-Wi-iqvOsPTpdpKh3eBULfiRx6G0SlzrClJ2dPLYypt37klfPnFc53hyApfBGzJBOJeIR0koiw1JykNlhP_mmYxwv4f4wSv84SXOTQEW_09kNvDJVXKoc0jNYLsfGV9ISzsPoTV6i2qtXdWv5bx-wMlvNAkDgyMIMDSWhpuwfkVo_hwz3nU8OvwhmUQKGAeLvbTFMUQGXNX_Z4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
— M15</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/21636" target="_blank">📅 11:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlE0eMhKyM6IXXYuF4GaLsz4mACxn79OIBD8-4ac9JDR5hwEWc4mwDRBIiFTnKOS_zY8W4XQH-jkVV8WlEgJDz38JP5C2f-R2b8P5GM4gGXASecNAVQ2V79kptz9GXLlsTn1X6eRgO1Kjxvo_Xy3aQjK6R1kxyvxI8aHiYBIutD4fkjBUZoqdkasDCRyjY6l12GvYATaMsnyRyz9PZmL_vez6wJFrDivpDq-Nisr9WjmzIqLzwtfRl0l23tim-2l0IAG_F2qFPLfZx20J21Pnan1p4sPrMAu18lMAr92KiAhnKKPBFosKNA6oJENHJEQGpy9MZaZEtgT1SRurDIgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— M15</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21635" target="_blank">📅 11:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC2S-tz8bpRI_okcmcVvV01TS83YkQuLCCTATSKZ0qEQWuvzR0v_UcYZCF9gp6XG8NDvt8Y7sxlIeg6bs2zaEojl0dXEdzOzKnmv3dfGfz2j12rbgH90fnGt-w3DZPnviJr-2R84gPVWEB5cANbvDHjX0I10vGKbIoOJhvyhSTMpJYGPSCZtwFpEZ_KaYQfWmapww7uU33SkgJF-rQj1EPoUKczAmF2M3xH76i93iZM259ZOaUqH1hwExOayfI9v7f9J2hc4aQZh89zqI52bG_rosn3Ggeem_R8nZd0hasVBqa-8DXvOTrkzoIVb5SqEm3G_yXGJrK-1R99wTbxJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC برای امروز نزدیک به سطح قیمت منصفانه قرار دارد و سیگنال خاصی صادر نمی شود.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/21634" target="_blank">📅 11:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkupHZEGQK1-H_77_lOCGlnz4C3r5Fxds2IIA6opOj1Mh9P5LmApEz11AcXWrKiaY6tPg3NIUAP73KT6We4cfPkouA7NU1XJZqgVh70skQAekK3BxfOjcpwdbgoCPUMdVD36KIgkth-wKXMfFAwjYtIsQ8xWURxkvpqsC4jWLa3Ed-kfyfeAvFaUJzTkFg3lIGYfYAqQRwYFqgofrlpCuVEvKguQAzU8KiG4gtLaX8piq-Qe7ygRROzqO9c9ylXu7KQZ5XeNwXeLYXYo6xvJV5XRmV2gu23qEhJDcXUXfQFTeUnHE1VINmWtMZP6MWi2xzaEnQMDovzhMTXpIWU_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21633" target="_blank">📅 11:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اخبار فوری: چین اعلام کرد که حملات حوثی‌ها به عربستان سعودی را «محکوم» می‌کند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/21632" target="_blank">📅 11:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار‌ است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21631" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اوضاع یک جوری است!
زینب ابوطالبی می‌رود اما بیژن مرتضوی برمیگردد!</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21630" target="_blank">📅 01:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-vimwEEe-4Gx3O8K7IEtLRsFMJTLn549Bi_HSY-wu7U-BsjjN7bj13oerUjC-ZDjoE2GvS8RFKkK1_VKaElM1X6epKzh3PUmNNOSweZNEC5rI7d7bj8M_EzpMXfcQbZHZS_z23h3xoaplTwy2s6nAFscciByd8fsR8BopQ6nLKB-F-sBGq537BLa894k490qAx7cw_RaChzvAWoBjMPjJUiQ6MWB0Q-5f-Hm17CvcyBhhQhvO3j7mDDU_ZNz9Pizjts1QaYinvCd57bJhtJH9wEBYmBq_hZ-JJCJk3PvIUDBdt8KEvubZwaQXMZ3vxIleMCnxwatR6iG2BLr8cxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21629" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg5qIov9--EGx3tc16rb0wd-MRUKbgGJ8pfanbaJH1aNt1xWlowZe8kqUcq7R5PPK1q-mM8Oi6hAyED1tjnt0ZlmWeKDJaJBa56rl1cyo0NIICdpOx09T2kxcaSQBjPmnr78JzS3P2shaNCZ0BHjwxcreKZVY5CVwLI330dFdDxT__eJ4pU1qEBG2jH11jFo2HxDqsGC4iuMUYK3xfbRX9x4AfsUvwqg-wq-pvHB-QITE4tX_eVwah_iIvgPXxT5jCU3cokP2TG_Q7PrDnIkBvYZX4QkH9S_w0nIPZ6sVKCflzuap0zIWfHa0014aIUSC1n9h0Y96IJ8z1Xg-ef6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کری خوانی سخنگوی سپاه با استناد به «سلحشوران» اشکانی و ساسانی !</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21628" target="_blank">📅 22:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیروی دریایی سپاه:
دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21627" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.  رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21626" target="_blank">📅 19:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محسن رضایی  رئیس‌جمهور آمریکا، ترامپ، و فرماندهی مرکزی ایالات متحده (سنتکام) متهم کرد که بر یک عملیات قاچاق نفت در سواحل عمان، با کمک نیروهای نظامی امارات، نظارت دارند.
رضایی ادعا کرد که قایق‌های کوچک نفت را به تانکر‌های بزرگتر منتقل می‌کنند و نیروهای ایرانی از چند ماه قبل، هر شب، به پنج یا شش فروند از این کشتی‌ها حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21625" target="_blank">📅 19:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1WS31dm8TcroYxyTEAKaKX4ptwCe4cXd4WcVcrXu2OqOxrChHvrzjUE9gK0vVSUTjK8UK3UOHrOMZal1Z8C2krA8YtjS2XqiJTHRtLLRqukBnz2_Oc_ebz4dK-vzXgTO-WVS6rwBzUtG5VYeqWNLrNnVjo5Cw-82Yot6MIvPc-bbKKl2J7NbesUtknu07vxPjObqCXTibd5Nl3eOnCwutb5WMFSCNLIXCQ8nsiiuIY5VTewD9kzob4CzJv5ndJFVr478WwlrF2IiRNfsEkcz5M67pL8gyvK4VpXN87VfzyCxrQ7_32XpG_PwmAdK7umWWU3txEJZqleKk7H3DQFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ دال بر آغاز «آتش بس انرژی» میان روسیه و اوکراین</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21624" target="_blank">📅 18:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله دوباره حوثی ها به فرودگاه ریاض!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21623" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
سرلشکر محسن رضایی ؛ دبیر شعام
:
تحریف کنندگان تاریخ برای تکرار شکست های باستانی از ایران آماده باشند</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21622" target="_blank">📅 18:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
عزیزی ؛ رئیس کمیسیون امنیت مجلس
:
کشوری که ذاتش با استعمار و خون ریزی است ، هخامنشیان را که خالق بیانیه حقوق بشر است متهم به جنایت میکند</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21621" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هدف قرار گرفتن یک نفت کش دیگر توسط سپاه</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21620" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شلیک موشک از تهران</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SBoxxx/21619" target="_blank">📅 12:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:   عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SBoxxx/21618" target="_blank">📅 12:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری یمنی YNP به نقل از منابع آگاه:
عربستان از چین خواسته رسماً میانجی‌گری با یمن را برای اعلام آتش‌بس، بر عهده بگیرد</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/21617" target="_blank">📅 12:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرده است
♦️
شرکت SpaceX با یک قرارداد ۸ میلیارد دلاری، فرکانس‌های رادیویی با باند پایین ۸۰۰ مگاهرتز رو خرید
♦️
ویژگی این موج‌ها این هست که به راحتی از دیوارها، ساختمون‌ها و درخت‌ها رد می‌شوند و گوشی‌های معمولی هم از آن پشتیبانی می‌کنند
♦️
علاوه بر این، مجوز ارسال ۱۵ هزار تا ماهواره نسل جدید را هم گرفته تا اینترنت ماهواره‌ای پرسرعت را مستقیم روی گوشی‌های هوشمند معمولی بیاورد، بدون اینکه نیاز به خرید گوشی خاصی باشد
♦️
ماسک دارد کاری می‌ کند که به‌ زودی کل شبکه موبایل از روی زمین به فضا منتقل شود</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SBoxxx/21616" target="_blank">📅 11:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سنتکام از هدف قرار دادن یک کشتی در حال حرکت به سمت بنادر ایران خبر داد.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21615" target="_blank">📅 10:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21614" target="_blank">📅 08:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/21613" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عربستان از ۱۲ کشته و ۳۰۹ زخمی در پی اصابت موشک به فرودگاه ریاض خبر داد  سازمان هواپیمایی عربستان سعودی مدعی شد که در حمله موشکی یمن به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ تن دیگر زخمی شده‌اند.  ۴ نفر از گشته شدگان عربستانی، ۲ نفر از بنگلادش، ۱ نفر آمریکایی،…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21612" target="_blank">📅 08:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">۶ کشته و بیش از ۱۰۰ زخمی</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/21611" target="_blank">📅 08:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنان عبدالله النفیسی از کویت و وعده اش برای حمله به «صنعا» و پاکسازی آن از ایرانیان و مجوس‌ها!</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21610" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video.mp4</div>
  <div class="tg-doc-extra">1.6 MB</div>
</div>
<a href="https://t.me/SBoxxx/21609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21609" target="_blank">📅 00:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گویا تلفات غیرنظامی بسیار بالایی گزارش شده.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21608" target="_blank">📅 23:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">روابط عمومی نیروی دریایی سپاه پاسداران انقلاب اسلامی:
یک فروند سوپرنفتکش متخلف حامل نفت خام، که قصد خروج از مسیر غیر مجاز تنگه هرمز را داشت، به دلیل برخورد با مین دریایی از مسیر پر خطر اعلام شده، دچار انفجار پر شدت گردید.
این سوپر نفتکش که سامانه های ناوبری و موقعیت یاب خود را خاموش کرده بود، بعد از برخورد با مین دریایی در یک آتش عظیم در حال سوختن است؛ به گونه ای که برای مردم ساحل نشین نیز آتش آن به وضوح قابل مشاهده است.
نیروی دریایی سپاه اعلام می کند: آتش سوزی مهیب عاقبت هر نفتکش متخلفی است که بخواهد امنیت و قوانین تنگه هرمز را نادیده بگیرد.</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SBoxxx/21607" target="_blank">📅 21:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آیا موج آبی دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا واقعی است یا خطای نظرسنجی‌ها؟!
با نزدیک شدن به انتخابات میان‌دوره‌ای آمریکا، نظرسنجی‌ها از تضعیف موقعیت جمهوری‌خواهان و افزایش احتمال بازگشت دموکرات‌ها به قدرت در کنگره حکایت دارند. با این حال، یک پرسش اساسی همچنان مطرح است: آیا واقعاً شاهد شکل‌گیری موجی از حمایت انتخاباتی به سود دموکرات‌ها هستیم یا بخشی از این تصویر نتیجه خطاهای ساختاری در نظرسنجی‌هاست؟
بر اساس میانگین نظرسنجی های  RealClearPolling، دموکرات‌ها در رقابت سراسری برای مجلس نمایندگان با اختلاف قابل‌توجهی از جمهوری‌خواهان پیش هستند؛ به‌طوری‌که سهم آن‌ها از رأی عمومی کنگره ۴۹.۸ درصد، در برابر ۴۱.۹ درصد برای جمهوری‌خواهان برآورد شده است. مؤسسه Cook Political Report نیز پیش‌بینی می‌کند دموکرات‌ها بتوانند بین ۹ تا ۱۹ کرسی به دست آورند؛ نتیجه‌ای که احتمال بازپس‌گیری اکثریت مجلس نمایندگان را تقویت می‌کند.
در سنا نیز شرایط برای جمهوری‌خواهان چندان مطلوب نیست. برآوردهای کوک از احتمال کسب خالص 2 تا 6 کرسی توسط دموکرات‌ها حکایت دارد. دموکرات‌ها برای کنترل سنا به 4 کرسی بیشتر نیاز دارند و رقابت در برخی ایالت‌ها، از جمله کانزاس، اکنون بسیار نزدیک ارزیابی می‌شود. هم‌زمان، محبوبیت دونالد ترامپ نیز تحت فشار قرار دارد. بر اساس شاخص نظرسنجی‌های کوک، میزان تأیید عملکرد رئیس‌جمهور حدود ۳۷.۶ درصد است. در نظرسنجی اخیر اکونومیست و YouGov نیز تنها ۳۵ درصد از پاسخ‌دهندگان عملکرد او را تأیید کرده‌اند، در حالی که ۶۰ درصد نظر مخالف داشته‌اند.
با وجود این داده‌ها، نمی‌توان نتیجه انتخابات را از هم‌اکنون قطعی دانست. سابقه نظرسنجی‌ها نشان می‌دهد که برآورد حمایت از ترامپ در انتخابات ریاست‌جمهوری سال‌های ۲۰۱۶، ۲۰۲۰ و ۲۰۲۴ با خطا همراه بوده و میزان آرای او کمتر از واقعیت تخمین زده شده است. هرچند نظرسنجی‌های انتخابات میان‌دوره‌ای معمولاً عملکرد دقیق‌تری داشته‌اند، در انتخابات ۲۰۲۲ نیز برخی مؤسسات حمایت جمهوری‌خواهان را کمتر از میزان واقعی برآورد کردند.
یکی از مهم‌ترین مشکلات فعلی، کاهش نرخ مشارکت در نظرسنجی‌هاست. شواهد پژوهشی نشان می‌دهد جمهوری‌خواهان تا حدودی کمتر از دموکرات‌ها در نظرسنجی‌های تلفنی شرکت می‌کنند. بنابراین، نمونه‌های آماری ممکن است بیش از اندازه تحت تأثیر دیدگاه‌های رأی‌دهندگان دموکرات قرار بگیرند.
نظرسنجی‌گران برای حل این مشکل، از روش‌هایی مانند افزایش وزن آماری پاسخ‌های جمهوری‌خواهان و تنظیم نمونه‌ها بر اساس ویژگی‌های جمعیتی رأی‌دهندگان استفاده می‌کنند. با این حال، این روش‌ها نیز بدون ریسک نیستند؛ زیرا فرض می‌کنند افرادی که به نظرسنجی پاسخ می‌دهند، از نظر رفتار انتخاباتی نماینده مناسبی برای کسانی هستند که پاسخ نمی‌دهند.
بنابراین چنین می توان گفت که در شرایط فعلی، احتمال از دست رفتن اکثریت مجلس نمایندگان برای جمهوری‌خواهان جدی است و وضعیت سنا نیز می‌تواند به سود دموکرات‌ها تغییر کند. با این حال، سابقه خطاهای نظرسنجی و دشواری نمونه‌گیری از رأی‌دهندگان ترامپ، عدم قطعیت قابل‌توجهی ایجاد می‌کند. برای بازارهای مالی، نتیجه این انتخابات می‌تواند بر مسیر سیاست‌گذاری اقتصادی، مالیات، بودجه، تجارت و روابط خارجی آمریکا اثر بگذارد؛ اما تا زمانی که داده‌های معتبرتر و نتایج انتخاباتی در دسترس قرار نگیرند، نباید سناریوی پیروزی دموکرات‌ها را قطعی تلقی کرد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21606" target="_blank">📅 21:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در ابرقدرت چهارم جهان؛  — برق به دلیل ناترازی در گرمای تابستان قطع می شود  — گاز به دلیل ناترازی در سرمای زمستان قطع می شود  — اینترنت هم هر بار یک شلوغی یا جنگی بشود توسط خود سران ابرقدرت قطع می شود!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21605" target="_blank">📅 21:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزیر ارتباطات:  در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال 90 درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21604" target="_blank">📅 21:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر ارتباطات:
در صورت وقوع دوباره جنگ به دلایل حساس و حفظ امنیت کشور مجبور به قطع اینترنت هستیم اینکه در چه سطح و چه مدت اینترنت قطع شود مشخص نیست اما به احتمال
90
درصد اینترنت سراسری قطع خواهد شد</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SBoxxx/21603" target="_blank">📅 21:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21602" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اسرائیل هایوم:
اطلاعاتی که سازمان‌های اطلاعاتی آمریکا در اختیار دارند، نشان می‌دهد که ایران با وجود ماه‌ها بمباران توسط آمریکا و اسرائیل، موفق شده است بیشتر تأسیسات تولید موشک و پهپاد خود را حفظ کند.
به گفته یک مقام ارشد نظامی آمریکایی که با جزئیات این موضوع آشنا است، ایران همچنان به خوبی مجهز به موشک‌های بالستیک، پهپادها و سلاح‌های ضدکشتی است و می‌تواند به سرعت ذخایر خود را دوباره پر کند.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21601" target="_blank">📅 19:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21600" target="_blank">📅 17:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد    گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21599" target="_blank">📅 17:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انصارالله با موشک فرودگاه بین المللی ریاض را هدف قرار داد
گزارشهای غیر رسمی از تلفات خبر میدهند</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SBoxxx/21598" target="_blank">📅 17:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چه کسانی از خرابکاری در اهداف انرژی سوریه سود می‌برند؟
همان‌طور که سوریه خود را به عنوان یک مسیر بالقوه برای جریان نفت عراقی و گاز منطقه‌ای به سمت مدیترانه معرفی می‌کند، یک زنجیره از حملات مرموز زیرساخت‌های انرژی آن را هدف قرار داده است.
در ۱۸ اوت، یک انفجار پمپاژ گاز را از کارخانه ای در حسکه متوقف کرد
در ۲۸ سپتامبر، یک انفجار دیگر به خط لوله ای در دیرالزور ضربه زد
در ۳۰ سپتامبر، یک انفجار نیروگاه‌های تشرین، دیرعلی و الناصریه را از مدار خارج کرد
این حملات با تلاش سوریه برای گسترش لوله‌کشی گاز عربی همزمان است - بخشی که به تازگی در الفرقلوس افتتاح شده ظرفیت را به سمت ۱۱ میلیون متر مکعب در روز افزایش می‌دهد - و نیز احیای مسیر نفت کرکوک—بنیاس.
چنین مسیرهایی می‌توانند جایگزین‌هایی برای تنگه هرمز ارائه دهند، مسیر مستقیمی به بازارهای اروپا باز کنند و هزینه‌های ترانزیت را کاهش دهند
این مسیرها با صادرات گاز اسرائیل از لویاتان، تامار و کاریش رقابت خواهند کرد
اسرائیل، که از سقوط اسد حملاتش به خاک سوریه را افزایش داده است، از یک دولت سوری ضعیف‌تر سود می‌برد.
ایران هم از این جهت که جایگزینی برای اهرم فشارش در هرمز دشوارتر می‌شود از ناامنی در خطوط انرژی سوریه بهره مند می شود
باقی‌مانده‌های داعش با توجه به حملات گذشته به زیرساخت‌ها، یک احتمال دیگر هستند</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21597" target="_blank">📅 14:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21596" target="_blank">📅 14:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز گزارش داد که مقامات در تایوان می‌گویند معتقدند چین در حال تمرین برای یک محاصره دریایی احتمالی با استفاده از دارایی‌های نظامی، شبه‌نظامی و غیرنظامی متداخل است.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21595" target="_blank">📅 11:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚪️
کاخ سفید دسترسی مایکروسافت به ویزای کار دائم را قطع کرد
دولت ترامپ دسترسی مایکروسافت به سازوکار ویزای کار دائم آمریکا را به‌دلیل سوءاستفاده از برنامه‌ی نیروی کار خارجی مسدود کرد. ادوبی، کاگنیزنت و اینفوسیس نیز در فهرست تعلیق قرار گرفته‌اند.
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، مایکروسافت را متهم کرد که بیش از هر مجموعه‌ی دیگری از روزنه‌های قانونی بهره برده است. کیت ساندرلینگ، وزیر کار، اعلام کرد مایکروسافت و ادوبی در مجموع نزدیک به سه میلیون درخواست استخدام خارجی ثبت کرده‌اند که به تأیید بیش از ۲۳۰ هزار ویزای H-1B و صدور بیش از ۱۰۰ هزار گرین‌کارت انجامید.
مایکروسافت در پاسخ گفت حدود ۸۰ درصد از ۶ هزار پرونده‌ی H-1B سال مالی اخیر برای تمدید اقامت یا اصلاح وضعیت کارکنان فعلی بوده و تنها یک درصد از بدنه‌ی استخدامی این شرکت در آمریکا را نیروهای تازه‌وارد تشکیل می‌دهند.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21594" target="_blank">📅 10:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔸
قطعات حساس جنگنده F-۳۵ به چین رسید
🔹
اشتباه یکی از کارکنان شرکت پستی UPS موجب شد که قطعات حساس جنگنده F-۳۵ به جای آمریکا، در هنگ‌کنگ و در اختیار دولت چین قرار گیرد. این محموله شامل پوشش شفاف کابین خلبان با فناوری کاهش بازتاب امواج راداری بود که نباید هرگز به دست چین می‌رسید
🔹
کارمند مذکور ایمیل هشدار مربوط به محدودیت‌های حمل این محموله را نادیده گرفت و مسیر انتقال دو قطعه را تغییر داد. پنتاگون این قطعات را «غیرقابل‌استفاده» توصیف کرده و برای بازپس‌گیری آن‌ها با شرکای صنعتی همکاری می‌کند. پس از انتشار این گزارش بلومبرگ، ارزش سهام UPS کمتر از یک درصد کاهش یافت</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21593" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زرادخانه موشکی ایران ممکن است شامل سیستم‌های پرتاب سرد باشد
سیستم‌های پرتاب سرد در اصل موشک را از یک کانتینر پرتاب خارج می‌کنند، پیش از آنکه موتور موشک روشن شود و به سمت هدف مورد نظر حرکت کند.
شایعات و ادعاهایی مبنی بر دستیابی ایران به این فناوری از تابستان امسال در شبکه‌های اجتماعی در گردش بوده و در روزهای اخیر شتاب تازه‌ای گرفته است.
با این حال، منتقدان ایران اصرار دارند که این گزارش‌ها عمدتاً توسط طرفداران ایران پخش می‌شوند و از تأیید مستقل برخوردار نیستند؛ که با توجه به بی‌میلی آشکار ارتش ایران به ارائه داده‌هایی درباره توانایی‌های واقعی خود به دشمنانش، چندان غریب نیست.
اوایل این هفته، سرهنگ‌کل محمد اکرمی‌نیا، سخنگوی ارتش ایران، اعلام کرد که تسلیحات پهپادی و موشکی ایران از ابتدای تهاجم آمریکا و اسرائیل پیشرفته‌تر شده است.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21592" target="_blank">📅 09:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پرواز انبوه هواپیماهای ترابری نظامی آمریکا به خاورمیانه</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21591" target="_blank">📅 09:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from(تحلیل نظامی و اخبار جنگ) MilitaryToday.IR</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNV3biDBUurDe96et-Ir4oUil2kvVj0M5TF4bHy5uZ2PpcLWQreMA-ZWN-WQQ-GkcG-XhjN7kXGiLc7zmL_Ly-UWb6_8V3ClB2P_OvRA0Zv_Oun0Yr89JAd0hnjo8s4qG30mSVZD5p4FxjE8mlxAmDoDUvanB-B0s9AJTqcqoz7-lxmUDL_4y0IsLlnC1pLPhWMEue8N9_wTkDJ8_boGkgdAv8Qxznl7-hxeMf-1QNwn3ImWGwEAd7T2TCe1A0N-yERu9Tlv6lMgCp1BtWAFEyaTsRN2UZ9kp3xJLO52m39oxKTjvkErTym69Fr5YVDx0cCyTaOAncZYqzLct_-1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
افزایش چشمگیر حملات مسلحانه به نیروهای امنیتی کشور: 12 کشته و زخمی ظرف 24 ساعت (15 تا 16مهرماه) ثبت شده و هنوز بخشی از تلفات احراز نشده است.
Leopard
✍
@MilitarytodayIR</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21590" target="_blank">📅 00:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ngnjy-uC4p4vXjGchMuXZ1hIDtuythiiWWaVVPxnzb_-22PYWubX3R8vUTnLn7TkZ2FD17LNvadwSG96TFGkwOAzhvmNo3R05aGLZJWKLjr0pb8Ln2KWSlTLGbhZtHjZQQIXfvTQKe2b7Ll29TB2qyRWBy8YuotrVrHd9LXgLjJwzwHkMXJdl7ZTYdSn66s2MpyL2t1vNU994mMqzCnKGYqjhurUWK6cqd13PqNWZmeB3tac-3TvYrrcG9bQWVRzmt5E1UFFQi-5sL2s0AQWewwl8WOUSjrk-zo7klU7BpqJVA7gusKH1As_yW8n32SdNOrisk9lIPxHcQUVsEXPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم عکس تانکری که امروز سپاه منفجر کرد
به نظر می‌رسد گاز قطر را حمل می کرده</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21589" target="_blank">📅 00:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قشنگ آدم حس می‌کند یک مشت مافیا با هم نشسته اند خلایق را از جانفدا تا جانفنا بازی می‌دهند !</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21588" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چه بازی شد….   طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/21587" target="_blank">📅 00:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQhy1HddBXOnti-qLPtTM0_o5pNZckofAJ79Hjbemz1y_M366d0GkLDMtQqJGqwXKkcFmbY_jA5Sl1pDdR-4SbHNKJ7ZAKtlFwwLgvzf7anNCbjNVF6VaG14KzaE6aNLg3XfjLhxsqt7LWQf3EWjPwR7x67QVDtN6vUJ8F4-xjUDxi6KPh6vI85AO0zl10GTm-PSYcxKRcxIYZzNMbwINLCINlYgLMSMd-VQWG2_Tv1y9viy5Wszj8jJU9c7bfDU5I08BhwgpVWgf0CXbLB6pVuI5JVn4o92pAe_XFweezpSBM7RLe6cn7MHYdyzHOxAaU6Rt6csyozztZ9sU3t8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی با کمک هوش مصنوعی از حرکت اخیر روسیه</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21586" target="_blank">📅 00:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چه بازی شد….
طاعون روسی؛ گازوییل روسی؛ اوکراین | ایران</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21585" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله حوثی ها به تاسیسات نفتی عربستان</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21582" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خلبان یک هواپیمای خطوط هوایی سعودی دیروز در اثر حمله نیروهای حوثی به یک هواپیمای مسافربری که در فرودگاه ریاض پارک شده بود، کشته شد.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21581" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">افراد مسلح یک خودروی هایلوکس حامل نیروهای نظامی را در منطقه چشم‌زیارت زاهدان هدف قرار داده‌اند. پس از این حمله، نیروهای نظامی و انتظامی به محل اعزام شده و گزارش‌هایی از ادامه درگیری و پرواز یک بالگرد نظامی منتشر شده است.
تاکنون آمار رسمی از کشته‌ها و زخمی‌ها منتشر نشده است.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21580" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a21MeXyJDZ4M5L7FZjez1cwphpT-LwAQsKkpr76uL3pbjOowGWCklSi9yA46q-SmxVEi5DT-09uVty1CtPlAsy2vKc-QWRsro4L-TXp9HUpja40Do8fmTzC3gMW9OEpGOv0FCGtKW7N3X-tjFzkUYQIXKYAybH4ybMmefxVHMc5JzIY863ndOMePKg_t8Cyy4IryL4lXJHXWKradGI3oxicjFzY5K95904_b47wXft07s12pubKXKmwOD_DRhDI57QH9rWvU6ycxs_PFPXDYN5zXd_8GyzttJDFPoafriexm505pDmf_q3kbJ5fccKOG7UcWRfNc_oVht0jvzQEFsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای بازار سرمایه و ایران.
کسب مقام نخست مصرف تریاک در میان تمام کشورهای دنیا رو بهتون تبریک میگیم.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21579" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHEmou-KqORu2AfvU2GB3xwHXSl-R1qCL8F6yGlXPKZ5F5hZujQEdUvlSZLma16M0w0Fmi2KLk0-TFnNKwvySLZa5VzEStixtQ3NU9UwqNZn6M4YJfCbPlQlbKHuUK698r2cdoppQGGAzJdXSWyp_Y0OJj1CMyfw91kQvoqogBXzGDqSqRm7dEW6MzncUySdykFPQzvbqcReqRTPQTa1VF0Oujz6PqI1bE2gufqPvKot2UcAfsJ3zcfCouZH-8rn7QCQ43XCTzHptphOTxYe13I7dk68wBjAoKeB718LJSQkqzpZiVsaiSWrV1bgqDmSkxbkTJa_OQfdelZEDrTssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21578" target="_blank">📅 11:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwSPd3ARJjTdyakHnPfmFgEZmTn1iD6fLJlXG5juKxDE1I0TNbWUlxx_M5vythtZqKbxTwIHVTJeg4-yGsxAhLAb9xM7nV6qjXaNIaD1ldypAol5jO56reFrL_4YUUD95tuibwXu3bG5dyqyHyPQKpGYndHS_kRPrYZkMoJjrFkdx_xTGTzz-7QrRyjDgZ7oKFZkny7WU2WDv6vJmSDz4-zlvrn4OkjzN_w2P3hGsCXhLT7jJrp0AQKVFAbaoOsukSNbKNqMmOxdeBPEwz3IG1_Vv8GgK-iYJfCFf6-27UGNceYomY_jDglKYjrstC9V_QJCkbX9kf_by5DM0ra7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.  در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21577" target="_blank">📅 10:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyi3k-fWH_sKTLDtpZfGC9Awe09jn94cWldOkAYfjt2OhgHsvEZ5TLkoMg-wX2u8UaAjqEcnfofUMWeBpJnPz5fCRxXbUJTuNOMrO4LDIw_6FvO2bJW0FdXU_5NqsIwsuYALly4_X5kdF5kp9S4DIlJcN5fl6plplANYg8D22arl4eTcOC3LasqaN_ULSG1841WAOcQIbfnKOqKd-l0pq_d-nVHGQw8ruW49ArhagdTvSn9oe6mm_SLAfewxkzr3u9uN4FdTDiAUGkmoMqASvW0tE0VAbnsjyjGnBSR94uMKsBu9HiwOprEQJgQudx4G8UCbDbnKYN8r639xhjssDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC با رشد سنگین طلا به محدوده میانه نوار ارزش منصفانه رسیده و ارزندگی خاصی نشان نمی دهد.
در چنین شرایطی بهترین راهبرد، انتظار برای یک اصلاح «عمیق» و سپس خرید است.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21576" target="_blank">📅 10:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9D5d86_RXMDvf0Nj0SeOeVz3PsCK1c887P4Xh0gCmY7kFofVAWCmPlbWuh2cM_Pc_y4oeDtSWv0f6GsKIHZzkB-YwNLUqbdJ6whhZAyEM-PtFjSBXTrm6xhuPp0FnMXAR3ESN7K_Qj85hoxFeRcUjRfflQxakmj3EbNyEb4VwNLydHmKEqBvp0bsUOc8GePHuJBxeaMJvBkoeg8Bk14EaWs_Dw1FMZJAbmILA5Mz-cw77wAdzTF6zbV8HrvES4XJaSOqbHa8uVFzOhqvcTFc7YX3k5jNlsupYoOPFX7NoYGca6lDJSwwaKRyx7qtSYdJVeE8Ysi70zgZ2cLeLuovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی + تقویم اقتصادی برای امروز در سطح نسبتاً پایینی قرار دارد اما رشد سنگین طلا عملاً این مسئله را پیشخور کرده است.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21575" target="_blank">📅 10:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21574" target="_blank">📅 10:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
کره شمالی هزاران نفر را با هویت‌های جعلی آمریکایی وارد شرکت‌های فناوری آمریکا می‌کند تا از راه دور کار کنند
این افراد با کمک هوش مصنوعی در مصاحبه‌ها و تهیه رزومه تقلب می‌کنند، گاهی هم‌زمان چند شغل دارند و بخش بزرگی از درآمدشان را به کره شمالی می‌فرستند.
این شبکه می‌تواند سالانه تا ۸۰۰ میلیون دلار درآمد داشته باشد و بخشی از پول آن به برنامه‌های تسلیحاتی کره شمالی می‌رسد.
علاوه بر درآمدزایی، دسترسی این افراد به سیستم‌ها و اطلاعات شرکت‌ها می‌تواند خطر امنیتی هم ایجاد کند.
﻿</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21573" target="_blank">📅 09:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پنتاگون طرح ۳ روزه حمله به ایران را تدوین کرده است
بر اساس گزارش نیویورک تایمز، ارتش ایالات متحده گزینه‌هایی برای یک کارزار کوتاه و شدید علیه ایران با مدت حدود ۳ روز آماده کرده است؛ این حملات به سمت مخازن پهپاد و موشک ایران، تأسیسات انرژی و سایر مراکز نظامی هدف قرار خواهند گرفت.
طبق این گزارش، تیم ترامپ قبلاً ۵ پیشنهاد برای عملیات‌های بزرگ علیه ایران یا حوثی‌ها ارائه کرده است. ترامپ اکنون پس از یک جلسه با مقامات ارشد امنیت ملی که توسط نایب رئیس‌جمهور ونس در کمپ دیوید رهبری شد، در حال بررسی پیشنهاد ششم است.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21572" target="_blank">📅 01:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: من هرگز ایران را برای بمباران لس‌آنجلس دعوت نکردم، رسانه‌های جعلی این را ساختند
او در تروث سوشال، «اخبار جعلی و مصنوعی» را متهم کرد که سعی دارند بگویند او «دشمن را برای بمباران سن دیگو» و لس‌آنجلس دعوت می‌کند. به گفته او، او فقط می‌گفت که پرداخت کمی بیشتر برای بنزین برای مدت کوتاهی، بهایی کوچک برای جلوگیری از دستیابی ایران به سلاح هسته‌ای است. او توضیح داد که قیمت بزرگ، بمباران سن دیگو یا لس‌آنجلس توسط ایران خواهد بود.
این چیزی است که او واقعاً در یک تجمع در نبراسکا در روز دوشنبه، در مقابل دوربین گفت:
«پرداختن آن قیمت کوچکی است. آن‌ها می‌توانند یک شهر را نابود کنند. بگذارید لس‌آنجلس را نابود کنند، بگذارید سن دیگو را نابود کنند.»
که پس از آن گفت: «قیمتی بسیار کوچک برای پرداختن.»</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/21571" target="_blank">📅 01:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ستوان سوم وحید عنایت از نیروی انتظامی امروز توسط شبه نظامی‌های تکفیری در سیستان و بلوچستان به شهادت رسید</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21570" target="_blank">📅 22:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">همان گفتاردرمانی همیشگی ترامپ است. به نظر من هیچ گفتگوی جدی در حال حاضر جریان ندارد و همانطور که خود ترامپ می گوید، فقط زمان حملات آنها شاید به تعویق بیفتد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21569" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:  ما در حال انجام مذاکرات سازنده‌ای با ایران هستیم و تا پیش از برگزاری انتخابات میان‌دوره‌ای، به هیچ وجه به ایران حمله نخواهیم کرد؛!</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21568" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Jt0UMGMz2XiiJ5s-U72vUOZDgfXqs0h1HvZ-QVP-rDCYB9jPE_TYlldytrIhuUDyjq4sxJpKNlz4IcM5t3OXDnpmEmNccupLQWprXIOSefIsHPZuYRvSMRBm30glXB6GkD_D40RfG3NpLAFweBEKBk85uVKXXMHPLf67mShXD3iu-6YGQhv34HHL2q1HqgHgzASxsKEf0OZHYKcycoKpxy9Ue83Rk6rAUY2prFmfAttxIIVKoRU8bZKKbXwaAyKmM-g4jloh2Vb26pK-5-NYpC1xh0htjirsNLSdKypjZebehakYmMzVe5ClbGWmNbuzAOafyHcEkfFFyuBf7aXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش کانال 14 اسرائیل، مقامات ارشد سپاه پاسداران انقلاب اسلامی خواستار حمله به اهداف مهم در منطقه طی 3 هفته آینده شده‌اند. آن‌ها معتقدند که ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21567" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خیلی شبیه هم بود این 2 خبر که ولی خب</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21566" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21565">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21565" target="_blank">📅 19:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21564" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ اعلام کرد که هر کسی که از عبارت "هوش مصنوعی" (AI) به جای "هوش برتر" (SI) استفاده کند، توسط کاخ سفید به عنوان دشمن تلقی خواهد شد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21563" target="_blank">📅 19:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKlgR6Y4vJi4KI54Yey-XmcEfHpz6b4qcisd7wJmn6js5Eyw8L8T24nYqqIkHF5yjIiRNCgbNku_TsgggzteX-1ANcQh4NpbaD1_gXMp6uBlDNbGuWFfq7hKt9LQSAqkFtk8x9aDuSJN5Do-a9SRVxsQzyzB0-Ztygd4lpMlR0Zzan2G2WgK9l4kH1htVgmMjLxJIDPARnFukXy1O0f0Tn36fkwiY0Ql_JPSuktPb2RmdOCikMywYMC3fBstDB9YtlKYB70rqrHmgAr0nYogvTJ_MlZcZ2PutwYT1CQgsRGUBj_BUxYQw4JP6277y1LCO998hIBfiaDszCoeuijkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار حرکات 300 پیپی داد و اکنون دارد به حمایت اصلی می رسد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21562" target="_blank">📅 19:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OynIQvJgA00KTI47M9lqVZOuYga2GssO0ec5jBnhSUCkKBtrxTonzdJNBAlb8tmMeRlXqYTCXHX_A6jjDzO7Nu_NOCeL4JpW20VZPXkf22aEhBgFCyaXOjK_pUHD1cY7S3me5EtYuzuRgtvs0ej52nCtQw5p0KO4cNT4iX0gouD5NId2GIeVAIE6C4dKA8L5CJVt0jtpcSvYyRyM9CsA3enchXgSZQHisWKHzJfX1vQGwmtkU6IVNWUWs3lott7ShpijDi6hOuxf58L8V2jFM5mm4rlEUcCNfHWEsswpXeT-5Y-3qN1LB7ZdwJGt047F8FE5HaP1CnJNkeT3NeHRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21561" target="_blank">📅 19:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21560" target="_blank">📅 19:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyuFqPfNllxhyKV_3nRC2Wt_Zu_ZSzVoqZkHUK7xNYD4Z51mg5pqobSIbicQ0WwTWv3J2Lxv6DODmYYaWBoDzX_MYx9DitCd2o3o27qGyzY4UO50LiGpJ2cCbn5sOX2kmQj7eXbF9yhSyz3U4eWpE3p-z9Dv4U3WEDqK7HetAAmbK8xXn8Hne3y4QkWcgQ7hnrhWKGlJIkjtQD6lYQphNVvyDMaH2Y2S1i--UnccUQ7emMXJHMh-QvR3VXvfAjj4nvVSARDcnY10dknt8V559uptpq9EuGlrZUSr04rN8H8nrsSIYcfcR4UNCk4XTtBloTvjDIIa8nrBW0JnlL9tSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21559" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21558" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG8k4y-wdNuRASCFyvf-YejowOQYA7zhz5XKBheoqIZlQlTKKKiH6KxzxwRWnrNfrZWF_HsC5e2QXxX76WeTOxhta0QD5thsENa8GObhiJNiUM-s81jy2d7eycknCg2JKDV0N24yQZWHs49LoB-1GcW5YfjRbtFMfAw33KvrOR602zaRpTEKOpnLX_qBoevAQlO10ppMgs7E0XW_l9Qm-zvIZJW65VWkxpw53cjU7QIrpCrouPI2rts-gsMu5DZpk3xcZTUgVQx4VmhMCzZJzlzB2Q61sjCjE0AfkWsNufL5dCCA5TX_QOu6aluMUQShcmJVj8G5yr5Kp653UWHtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21557" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.   ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21556" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دود سیاه در نزدیکی فرودگاه ملک خالد ریاض، پس از حمله حوثی‌ها به پایتخت عربستان.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21555" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPeWzoMTfBHxHErHHeZXOXZgK0f-f-jhHQS0VP8mwsW5OjPRKZROxsC5ZEvveMjQKwFk0YdPxTr-ifyQLZTkadeCx5xSsSn4uKv-ZkSfKA9ephvXy6V2A5UKrQ7ChXr_1mhuBXWzx0aaSJr_xUS1FsnGVB2pLntgi45QNwwxg5R3NWHmtIKn5GaImY78RIv4xyg8tymYf4oaBfik9FmOZKlCVpxI-fpKT_FHN4mRIAr63AV_GNyv0SMlVBwrl4X6EyB-zsV1Hl7ymNZ-n46vJEwWLhJi1UhsEuW1K0L2olukLmBPJaAWx-abLTkX1mkApzYF2nzg9Q_ZylDk7OVnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک هرمز؛ آیا جهان در آستانه یک بحران اقتصادی جدید قرار دارد؟!
شوک هرمز با افزایش قیمت نفت می‌تواند تورم جهانی را دوباره تشدید کرده و بانک‌های مرکزی را به حفظ یا افزایش نرخ بهره وادار کند.
تداوم نفت بالای ۱۰۰ دلار می‌تواند هم‌زمان با رشد ضعیف‌تر، سرمایه‌گذاری کمتر و هزینه استقراض بالاتر، ریسک رکود تورمی را افزایش دهد.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21554" target="_blank">📅 15:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر    در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21553" target="_blank">📅 13:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صحبت های یک استاد دانشگاه امام صادق درباره اینکه چرا فقط تنگه هرمز برای جمهوری اسلامی به عنوان ابزار فشار باقی مانده است</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21552" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21551" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حمله تروریستی به مینی بوس حامل کارکنان نیروی زمینی ارتش در محدوده نیکشهر
در این درگیری یک نفر بنام محمدرضا اوکاتی به شهادت رسید و سه نفر مجروح شدند. اخبار تکمیلی متعاقبا اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21550" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4YFF-xpCDhpKoSy6KP0tWqLDJJo114zixngL_WwtaO34s_DRzSPnCm_bN2BaM5ODaU6XD8_wiapvv9a11_JGIVtMN5hd6WTF__hbLgbJHTLmr1UADCHQpRUhQABukUFFkFXAGFcT3DTGmRAk254RpnsF9u3VG7dby2vdBi4YDb4gYuhixHIntbWI_6vFRnMgxN-SmCu-UrB5AnznbayqCyOLsB_gPFVCyXfq_mVtz76VKQfYsy6KydC-ZorjNnt1hqCHMwhMZvCWRx7CMH3Ibz-JbWSmq2h82r4WWOMgpOk3KliCI9ZBGIeJcM2um8kaeiIbO8Martaza0e9uWs5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین محدوده خرید حدود 4105 و تارگت 4150</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21549" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIp84GrPr0CvcagLyHkDOr5EsvLbuvOeJXeZGlBweNv-co7G10xKpV1YXfIg6ovB1epQGC7hVWQhKy4BRcux-R6pEgpZAM7RgtjMBLd84yAsi8US7y3wpFXpp262ia1F399zEzoKJ0UDUv1iqNSP5EVyuc6z9darQqmLZga6C3eGSHqILoFF3vSyskKj2dfLlivoqFdX3saBcKIw0wXSH7TBGam2FZjGsyEePhXT6iqN-Rvzboa9_Vx8-D5fUN3vfjRJqeb4um5KWKzmcdHCb_30RAEv1n5vUD5BJPTbdVkx4xuLW37HF5hX2RS7um7TXTXPnLGsidKG0rGBllu6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده بیش—فروش قرار دارد و خرید در حمایت ها منطقی ترین گزینه است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21548" target="_blank">📅 10:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVYKpn6h9EUsxOuWnFQtoDrPPcpNN-N8PDOJCRZ8uxecDtX4LP-yBZchAAzghzEZ2wwVDoXoWBN4V-1eNgyg2Yr-4QNiGoJp2He8cF0JJ04tLs9N_OmDiIe8xmd5zXOHFUg4L9Gq77zltY5lwreIrP-2tsUM9wYZTWWUHqzqbfJszZOZyq9H2TgWir7LVYr9ImsW7DfUel3DzoZqunABPuD1WaOAxWTDHryeiNJqaMhiU-6_ixfPON_TZYZNK2P_SpMWS4erKpu4F-F-RGdpQdaC4QWZy4vIUYFzWfsAcW8OHw0BrhswcrfUkTIdda0m77M6Htm4KCS-Qnxypcxjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و خرید در حمایت ها توصیه می شود.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21547" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پنتاگون به سنتکام دستور داده است تا تدارکات برای حملات احتمالی گسترده به ایران را نهایی کند.
ترامپ هنوز تصمیم نهایی نگرفته و تاریخی تعیین نکرده است، اما مقامات آمریکایی و اسرائیلی می‌گویند حملات ممکن است پیش از انتخابات میان‌دوره‌ای ایالات متحده در نوامبر رخ دهد.
یک تهاجم جدید می‌تواند شامل حملات گسترده ایالات متحده و اسرائیل به زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران باشد که احتمالاً منجر به تلافی موشکی ایران و افزایش قیمت نفت خواهد شد.
مذاکرات هسته‌ای ایالات متحده و ایران همچنان متوقف است، در حالی که ترامپ و نتانیاهو، نخست‌وزیر اسرائیل، در روزهای اخیر دو بار تلفنی با یکدیگر گفتگو کرده‌اند.
مقامات اسرائیلی معتقدند احتمال حملات پس از انتخابات میان‌دوره‌ای بیشتر است، اگرچه حمله زودهنگام همچنان ممکن است.
— آکسیوس</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21546" target="_blank">📅 09:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران،  بقایی:
عمان با ایران بر روی مختصات جغرافیایی مسیرهای امن عبور از تنگه هرمز و نحوه ارائه این توافق به صورت بین‌المللی به توافق رسیدند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21545" target="_blank">📅 00:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران، حفر و توسعه را در یکی از بزرگترین پروژه‌های غیرفعال خود، مجتمع زیرزمینی آبیک که توسط سازمان‌های اطلاعاتی غربی و اسرائیلی با نام رمز "سایت 311" شناخته می‌شود، از سر گرفته است.
این سایت در امتداد محور تهران-قزوین، در حدود 100 کیلومتری تهران واقع شده است. این مجموعه در دل کوه‌ها حفر شده و شامل چندین ورودی تونل است که احتمالاً به یک شبکه گسترده زیرزمینی شامل ده‌ها سالن و پناهگاه متصل می‌شود؛ این مجموعه یکی از بزرگترین پروژه‌های از این نوع در ایران است.
تصاویر ماهواره‌ای نشان می‌دهند که این یک پروژه بزرگ است، با حجم زیادی از خاک و سنگ‌های حفر شده، زیرساخت‌های پشتیبانی و پوشش سنگی قابل توجهی که از تأسیسات داخل کوه محافظت می‌کند.
بیشتر کارهای حفاری در این سایت بین سال‌های 2007 و 2016 انجام شد. پس از آن، به دلایل نامعلومی، کارها عملاً متوقف شد.
با این حال، بلافاصله پس از عملیات "خشم حماسی"، تصاویر ماهواره‌ای نشان دادند که تغییری آشکار رخ داده است: ایران به این پروژه بازگشته و با سرعتی که در طول حدود یک دهه در این سایت مشاهده نشده بود، حفاری را از سر گرفته است.
این سایت در سال 2010 توجه بین‌المللی را به خود جلب کرد، زمانی که از آن به عنوان یک مرکز مخفی غنی‌سازی اورانیوم نام برده شد. این ادعا هرگز به طور مستقل تأیید نشد و هنوز هیچ مدرک قطعی و عمومی وجود ندارد که نشان دهد غنی‌سازی اورانیوم در این سایت انجام شده است. هدف دقیق آن هنوز نامشخص است.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21543" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در محدوده قوی حمایتی است و با تریگر می شود خرید کرد. (مطمئن ترین تریگر شکسته شدن کانال نزولی)</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21542" target="_blank">📅 23:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قرمساق کاکولد با بهترین تجهیزات آمده نیروی دریایی فرسوده ما را غرق کرده حالا کری می خواند!
پدرسگ اگر شما هم کشتی های ما را نمی زدید خودشان داشتند یکی یکی غرق می شدند.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21541" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
