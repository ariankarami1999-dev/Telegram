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
<img src="https://cdn4.telesco.pe/file/t81a61ha7dw951owfe-wfSmRb9ArlCuFugppRJp3lToPy1Kddk_m6kP_ADQy4Jf6-nBZDGs9AAUICR0xxDtRbC_vLH29K1yN8RzLgbF5WCQMVqV4JwUvinF_IWroRHPpt8wIMBC_fwELPtEl4WRw9JQ8qQbl4DCBfFKTTfbK7cKQ133McaeC46uG9yhWj2ZXLJ6ej5PMiD29mTZ9BIa4LAoRE83f6CK5XwcvAenRA2MwDDeajnCykUgIGDFDQ4_23qP-Yjlxz6sh-t_1plwtJx06QqCtmhoRK9gbn50wAshSdn2i9RAXPx4VDZw3PgYNMMi_Zps2LTLuPrT7pn128A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to5Fkj-8eOisV1OJSPxogOLe3J6SknYGweLu4gkblOM1SHQo0c0LKwaWnZardh5orMlN9ovHLqKnhCOvkDDdSXV1we6kyHXe87wu19ftrlmIkEXTEqNBRwu9bKzveeFj1UILx3tm9jNlE5RXxD0XmkC1MOkk1Ir6QSjlUXyXhj1AwPOxZAPYZk25FEzFeXHbIlsreaaXhfTlWchHx-vErSYCFoEHx-MmS7mHesGccfPfhO9Lye4wwirVJ3oNMi1wL0HB3gmnmFlwCPc5UMcb8NNQ6_iqXQ9kSRJYQHAI1weZCIebTPeN0gPNEfnY1jIfVB4n4-T1zsb9KQOcJloZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo_RDBCwe2NzzLGkGc7-8BvxaT-Usq7AxgPo36WHEFjVaYCl7YFFRLWEv9oHhEYq93ruXK4pgDwFSZhtRJd5BwngEE9lSgLUBlOE20QJ1vMZda-HY5AMMmO9H2U9KtFgAyh6AXn6unq8vyi2B4hsH3nJWTmSh96F7LBeeFOMOUKyB-sIrDkPKhLDWEY14fFJ4tBcjNZ2qkVHOywHE23sWOZFqsawZU-bqqLYqtJ7-MaEtkKz1P6gfgRGiyOb2XYkZu99ZkM2TJXu0cJtDJOjqxUKb2ZVdRSJfkZGcpPaIAA-CR92Xc_MB5XoYLTkbK9tJQSJbQf1zLq_9-dzRGQCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoCDMwdKPSjlUPWL7adVK9p911HEDUwe-zNqDGSPyBQtGIblUPtr5f7XW2B2nsFlP1JDpy6baOFOed7VCO9q4-tLOuvJ7s0Rjg8T9XDCcYIeb_Egji4_oM3DI2hHhTbdeEQ0S7T02uxS2V76a5-kcPYpn-ezl1ljVneKcTQW3f3tGXnSqfV2Elq8-07YuUbPQpku2eHpjst2KNOnDktMSxd8LiyxjFYum4Irin_wkWjBljphzEpveaonOaVlzjjolA83HWPPri3QbOxwwwRnLIJc8s_sS4W9guthhyQptEi6NRv4sbSRgMtd6hElD09HMAVYCCuPTUKAZrJpvoa0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHSC5VQGLLz7WH5RYJXweVm2J4ZaMMrl3pGC6cCaafLu3kSfMasZwVkm7sdJCGMeKA8qvAdxYv2RFJJk1c_x0uzrjWPCr19RZhExdRBtJgudbdmndQv2bTFJ_wTrtyJFN2ljdyIpYpOiIgoRxa8yVPB_9xiTAzvqEdMMaA6fF-0OGp8bwOwotO5aqM5EhZNHSWqTZw1-Oa92bCQi2uQ8XI-CqGeiTi6i1y0BhaZHAmBnHhH31QMXIXWXkQJO30jW2xriNjT84GsATNzRyuISPBgBWRaeN_A-cWPnq-CNzQ0489N8Z_6PxaGi6XgKqsT4tgR3MUxJ5-oRgIbDd150CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=lZIN4n4ImoL5J2Kx9bMsieh-yhmw4h4mNvrGvcdJvS9tdpYTygFKlZ_TRolbMDR9Q57KXcpnF9brXXsMpe0HmUmt4445quzYQtRSRZoWXbJg0OLFq2vOfcAyF106hlv5ZRGspnnaAgZuadwtObxCt5JGK01hAPDJcwoLmLtkFTynMbFAeJAVtiZtAXKtwmnaqNGLnNqN6b9Juf-D_HsSWgKFy9c-y_V_EG8bGUT2A8U7Ha5h10mb3NGcdA5BC7YJkzorHLCBmupW_a--DSCfta2-vXLGcU37-57UJmP_MUDNpudSCNXRzhZVHsZUZce0d6rlKNdDQgiaZlxIrH-KFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKfTRWJJg5DCs6mITT3Ntdcai-Va53n6L7YJzdKe3WQvLtDzQUsjQw0ZhwKFAE0Fczj3oq0jRJYDJKVQq1Cu1dxoJIr0nkz_s0oXoeey2th3sSvHsiPew1FbltP68IBA-9tbd2t3AKyoFjmFRt9hWD-5OqUyO66mmCbCjLQpv-TZYCkIVtP--fSQgLMh3uZvdx1j6JJAlk1xJd6to5nsOXc7DEA9EJyq_1U1orDj6AUu4Xe582wbBm7iEpJd1uxafwmibK48SYC4wmk7GSXFGc3zK81qtHu1ZlMFc2seZZhySH72IqQQlJEE3Fuk2gQeXO6Xf7CWc0JxF3QHyLdfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_UNC4P5iBhAWjrjbn8o8zt8AF1VCD-Sq_IV07mibhsoWbUlT_UvEJ3tBJ5109EqWIf2qvpHQnJOT5ztGURTzjYbRdTViTxSpOUKsFxTj5qG3nZFBzc8JKP1JWRxNlN_RGrK8RxGwjr2eSQJOBBf34O9XWMN9zTwuG2fKTIrFb6VIkqfDLyZNY5UVIzLP7ALnyVU42J6xFeJfeNPi-jCuGzD8VwJI6HLzCRdq6WCzTChat3sMKINX0Id_-M2O3czTeW-zkCdE4GDvcZaxT2Bq1KY2nQXCYJVROfYVDQsQfhDi-PT9JvOa-CA8N4OUnA9-uiM-YaI3vjHa07r_qnfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyWIvp6OCl7OmmrxjsFDOEzvOGXHU792AE7qRGvtZ0QJzAU2n_jQ1kkXQ4FRD-E48ekKIA32a2E1b-74Rp8wQKwOfUWdCQ6rMxRtxQRNcSqqLouwfR7h2rl3w8yvepm1CCclKHUi2souH_Lhgi7kxMED6pqM__YUi9wCXXDkBCsCB2FB3RelDH39n811GKH3CrRZHQ84we5-2W2Jmmi1UOdhd_P8QtPdCKyCJSwMEhEDfP_D324zFgpv63Zbcb8FrTsfBytcIRCrbJR_v2sQwo4JRqBUSAHN-1ZHG60HGBwbFdATEZ94GH8iqCkHEjN86j8vNQqEBI6Il8Fm-xaU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=vxIn7tLy4HRdKDIMNPb3DsWcOXKQYFaVg5f1E7DGVHIHbYtFrJkNLueXdVnD3XM8xPcosIxlGbmrf6unwcqfZ6Lpda7gpIUKOCQLZmLrQDYs3typteSFiUUrmVfHcRFZsOzUu1aW_peengL7Ov_rjG1OB5ujVMVf7UrXzKMyfKqKSYbeMkaCXiMCITBjDMgb7Tz10gUeHOOpIpAXTIXRen-D9R2PkZWL1tvkqMXaFri1Co0pjyek9avcOUP-0PuysGr4PiQk_JZf0HsvBykrLH0TMW7Yem6ALZbPEKKDkMTWQt2RU_PbPMwiTJh0-0-t7o-dWPtYAIidVazb-zFwFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=vxIn7tLy4HRdKDIMNPb3DsWcOXKQYFaVg5f1E7DGVHIHbYtFrJkNLueXdVnD3XM8xPcosIxlGbmrf6unwcqfZ6Lpda7gpIUKOCQLZmLrQDYs3typteSFiUUrmVfHcRFZsOzUu1aW_peengL7Ov_rjG1OB5ujVMVf7UrXzKMyfKqKSYbeMkaCXiMCITBjDMgb7Tz10gUeHOOpIpAXTIXRen-D9R2PkZWL1tvkqMXaFri1Co0pjyek9avcOUP-0PuysGr4PiQk_JZf0HsvBykrLH0TMW7Yem6ALZbPEKKDkMTWQt2RU_PbPMwiTJh0-0-t7o-dWPtYAIidVazb-zFwFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMoL_txJovA_wf7xb6Eklj5MVlJZJj7zYjitg62l55qvJU-SmTcnFsRJHg5KagI5hZj8NESYR3wy3w1vJP_Pxr7wCeYxf4wqpdikG-LK2gJoLCRytqsoOASv-fHlxbVO9C6IaazH25Jm299gvs9KOPnyg67m5UdEEj1auuTlsLX97we_ftp1qArvvTJB1-NFMSH80_EZ-fZBpMrbVD6aSvKtwW4ydkIuHO0uje89z61K4xOKm60LiN4clwgCooHaOWNgLci9JK3UfL8IO5IZ_LKJicEBLya1IP0gqz0qOD_tei09lh9zgnauYSl8PoDR6L04zanF-sjHHBKP6TbZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyL-ohdiVxnOWJQwY2PGxei1vnSxixHmio7LpF0z5MtvILZJoKqjMSc3ti6MkUKjDGzAFyPsXl6i32T2eptlwhHCKbA4tRSSinqHKnC43L-WlOfl793iTcDyamv7CVHRCQcHO291OYYodvO1OUQqjq1Yq4S17MIUxaU1BcCHabZuKT4sihjlrHwIbg0WO3_5gr1xQBpQp5poUNJcM1EwAsDeCHOXNHXW2P26eLN7dK6B0zw8512keqbh8wcc1cLP95M3x5KdocIqZMaqxuYys4EdgvpgtdJnNV6tEhPZl_pCsFOxmoC7b0yTtKzwa7nWtkaBg9JctMjMRKnokQIatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk3goMFE4DHUIrNM-wJaEn3nHP25gxYcxN76KAGbMK7vj6KmAjoZG4l3rO3iJ_gBRIka90D7C75QQ1ULWgrqNjlIMlVJ10lAB2ttGUoB2Xjh7gLExR3SNAM9tqvOGkOlIRI90C8Ct7pVK0l29mVdQ8V8s27jj0ADxeydyym7Fa9AQf2-JDoD7iBnDv9LMNbjF9jL2C73cWTQ8IlTBuIqgpMDen41BzCdUwvJ07cYYw-HDSZ1aB7obnQK7C69BiOTB9LzUxI7Z0oz4_4vt_jEFBUWc-Cal0f3AOxo_3964wivDILlfS-Mo59ict6HtpMBQ1DAN_jnJMptGrtqe726lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6mIYG3rfG8_Isfi8XXJSVUgBHctdP4XkqqY17_moElxukY_S719EIj6btyhJSa3JzQxoRd50xh6A3Spr8KRCBjDvzVVq2fSVOFLiy4d1xcjvn1DNxZQtR7y3Fc27kT3O4hQocwgEjdMfZ_3QzCcrFilXFI0luWQ3P_p8hn9EfMdDe3bQa0Z52ZxBzTWDDEOt7BXCL7S2IwmH2ZGIEpa2LKcjvznjV-NxvegUF0zHMMToL-rqC7crNOpB7SS4b0iDRd2oxyTZYTGbH-TVCpUfGmN0k3gB_bseVomvvH__vlQc1i1el6NVLiuh4hG0ETAtISTBg7KtsNknET-_e9Vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma7MNF0VUXczy6sf_bi0n4RViwyqRBAt6bPC8Iq48qpvrNYuPtNuAccnGv88f3znSLHhYyUzNu530IW_tUd-o__oslvQGXPQkE9C9CKQQMZ_I_7nH9DIQqot_GsH9z0vw3oM4hEBKhbbo3Hjkemj2SC9m7Vw4vJK1zLX-1L0yHmzd3ELkReTEnFTCuOEHzv_AUzd-plc3JgIAGtmfgigewpM_7azvYWc_5okdy48ZTrx1vfSMEw4ScBkkgT8W6ePU_aBvHjxjNssRS-ul_t-PKOAdLYz6JzBvGzO_0NdUJpXQyuaUZNpjlJnEPPWvArpaGQuQGROpje86qj-b7FpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMjMa3yC6lGMS4j1SkFPQD6nQ9sHEBfUzSg0-wokJ0eT27owlKrVfeBXz13zQjgEl0D-EJl8c9BIlD39AXRKT3cvx_dpQTSerxauYmzShLg7b6qAIDOLOQevwKq_FEWTcR4OryPjLO7ALxEqmHLWJAS6d1WyxxoH4rTQR5FQpikJoDXSFIvU4Go_PhcVzdU7WECGL7rJ6O5Y-RYJYkJVVW72DibkUD6ppA0NEBg-kXlMddE8jQhRKaFaMADhaRgxvwodDnspS7FX9Q9KztqHE5vqcE1eEsh7Bn8CcUpSMRkONDp4GNokjYuaTIOILWfbX8_lpWxXrZAt4eoJDkwDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=L2HL9-TFSqxzeo1TGOA4e-hEJZL0pE0prf6gp4YLSEMcaE_ToCvpGLwCF09zaS4D6NrO-n8a0M3g-PU1ydKvWY5NR4ceCTxA7-A2wfiAANbLhFrlvKaBGtfn243bO3KZQyueFTn7O4lCWw4C6jiP-HjYEQ78io2TLIf2a8NeOVhZmUb4k0TJLK_6rONF7-hDh589B9vaaUNOyHLsE-g4U8mU_3MyPm7_seC8PGP2gDN0yJ53TfbT3LvxJkhZ-y1DyrnMaD_pnA3taloQKLFG2joIy64c6PO1dHckq6d7WbndYCrWSRg-YgGuY8ui9ZABxw439jgLhwRG0HW9lEzSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=L2HL9-TFSqxzeo1TGOA4e-hEJZL0pE0prf6gp4YLSEMcaE_ToCvpGLwCF09zaS4D6NrO-n8a0M3g-PU1ydKvWY5NR4ceCTxA7-A2wfiAANbLhFrlvKaBGtfn243bO3KZQyueFTn7O4lCWw4C6jiP-HjYEQ78io2TLIf2a8NeOVhZmUb4k0TJLK_6rONF7-hDh589B9vaaUNOyHLsE-g4U8mU_3MyPm7_seC8PGP2gDN0yJ53TfbT3LvxJkhZ-y1DyrnMaD_pnA3taloQKLFG2joIy64c6PO1dHckq6d7WbndYCrWSRg-YgGuY8ui9ZABxw439jgLhwRG0HW9lEzSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACpJR-r_-fYc4UAWRuuPQt2ZrKDp2kTtGaqOrbRGApBGV5W03YLCsU2cQ4uO-EyWTpeLt9fFYSkV1l4XG3KlQtnYkkaOFc1dje5WhTr99MB3ubOdXHuk7_HL13whA9fgoZUbNBCMmYudvxKgLz8JBgrNv3wr40WLzjl39AEe6rK_1TqdgcCsqoShCN9bx4Vwg7BXf4ArgWYIKSTW2NWXJtJPlW6XVSkPlBVdTy9wKcUb3iU_-3IdUffqV015zY0z4HshjdC61W7Fv6W5-mVt0YrB-6Wp7K9yFPyP8gqg7tpiB_LD53Hl2uKYNUZu81T62c7PzdJmQdOkOY_2gFOY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eR2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24119" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU8AkRFhDxnPYfhZLcx44unqc9WD6de5ohsRv_F6-qnpKG_WC87sqZdyuVgec6f6fS83_XR92Qddy5kHb2CUL70EOFpLWigw1Bhj7XdlW1rWqLF0CChw0tP-Tpge9JZWr3ANVQfsImQ0mJpDFTEntsJJnNXJdkiw3E4412MC1kz-KGhikuJ-v28Bc-0UjVfRU3p2krMa3l33SsI-ZzzErKJMN8gdN_wMCbXKxDSLEyMWereqAvHVG7VUh6cL7cpcueZLnIeffxgbPepnXtObKI3U_87HVNg_wH5ycIvgLs6kya4ouxjaTx8L7bYvyXibL1NnnUOUs2sv8BLrOi6hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D93rUp7xRp69qCZuefgkWb5LVbbNAllr8E9CQH_NkdPDPf84bhXSttIl1bKzZKQoFyjKmKx9dQDeB0S0BwAkxdStE2bOs1ZLzGik_yKH4gu8By4lDVrg2f_rTtKCYvYhe8N0RrQ3EHMZcrZ4sU4WzChZ8SwXElVANcYek1UUXd1etdAXzq73CFt7Eg0jVCizLkRUtsxMiTYA3e4QsAu1vuwfDyT8Fcr8tAwBkTxjcsyfMQe9TutTqn4OwsesbI2Z8QYPFZhETtt_-oeThvJjVjBMgrfTnIBFDsSUFiLWmfYHbRazixrZ3XaX_8XltklPxG4alqtXBYEtN_BlOP1Mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cj5uPYBKdHd-v0WqrbCMaqRvfDPFVajL91fXTerCCoXfp6uivnOkb9eS4zsSP0fy1AvTot-gNOb9rIuvKcMe8ttAuW-DAmqTlgpLK_SVy1BxLu92z-fRszzLvcT4k-YZlgdV7TMUNEGk0IifDzJ_LAXn3sqx-PLbH8ksie84ms9TO9DWM-MpNQ_Nxa2xReakTyOcQdVz6uAa0CwmG2UNgljFufEE2cP2HKLomlsPZAbd1rnuIgyS6FPvy5zxV1YtXxh2OS0zGTA4GLwY-Qq9nEnve0iJ8gplh6p6o74b5wlQ4dj-aor2epcQDdtOxploI8InNBrVsbe2gnAedUteRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=KsU_TcWRQdk5pamTFT23MLedlcFQTwSCB3ThSfqK4t9g0cohUXuIVClCiEuJbx1OXC99aGDH0aVF63QeLzdS8ltFWfCeYkKuJ1uYJw_PDDTFuM4ZFqNAVuXEIYoFrZ3iWwhUe9v7mGgio7N1RyLWPDQUuEYl4mswFr288NgBu2Me_qXRUo6FYEpUgzt6V8TC9P5BfomdxasWL_66xuLYHMGZw4_2D18RaxQS_p5gC0d9FjESsw68ziKppnAFpjvqt5EPTM-lv6uBQ5N796iTfrGQ_niHCWDHQuPF-K0YPiJhdH5gb3tLWVfOc5A8OyXH_gOlx1Oy4V03tXhVlF9AXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=ZQy3q-XB7Zg0XrpB1Zoj5EBf9WHreWZZUOGGBSQkJIxvGrFcWSixGd-HDabB7_NfzAtcgcaNOdR0HsTq2YDP5lcUnswSvrDN605DRpwVMR8Uea_YtaGoMIBY0ppHGxHr40HrQDirM6r17uFtLWPQcm5fGznzx8tbo9_BLXjrbIMU6yzS3IxkBu8S3s8ybpNFaIygVRGfYMxNaO3W9KQXLjK_aH1xuXmUmd9O1YBB9VAFIug06lVzEfZD4vKbWSWtpkmrpxQohqwnzC8G7fnJTloqWUbKD2m4o612k2tgZkT7199h6yxMlbu2ynQN8zxFPvX9epFuYoyDOwANHvS_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=ZQy3q-XB7Zg0XrpB1Zoj5EBf9WHreWZZUOGGBSQkJIxvGrFcWSixGd-HDabB7_NfzAtcgcaNOdR0HsTq2YDP5lcUnswSvrDN605DRpwVMR8Uea_YtaGoMIBY0ppHGxHr40HrQDirM6r17uFtLWPQcm5fGznzx8tbo9_BLXjrbIMU6yzS3IxkBu8S3s8ybpNFaIygVRGfYMxNaO3W9KQXLjK_aH1xuXmUmd9O1YBB9VAFIug06lVzEfZD4vKbWSWtpkmrpxQohqwnzC8G7fnJTloqWUbKD2m4o612k2tgZkT7199h6yxMlbu2ynQN8zxFPvX9epFuYoyDOwANHvS_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT4abD00-rKD20N919Zaq0aXHCRKEdmdeWxEdgkLD-2_bRB7dxpiXMpZPFVrbFDlGkMnYYJULtdlvbkrWOP_Ip5fTlVAZhNthVO24kdWajU3FJ6I1v2SfKXcao2nNCvCSLMWquFpt_FtKaj0mheDWt2J9KchJNlLGKDu-O3H-GgzL_svxPGoCwJpxFKO3L104XWJuREVj0UJyEdGoe07AmE5_Ex5LKXYNTVkAM2yJv1fJCE-YYOacuHVAKrxBDlyLmfQ1xc1Z86cp7m0oBeIxDAyUYiBZlUwW0vctNtVhCA40aKb7cIOAs-v8rQ5axM2ER6v_ZYBHEtQ6DAcIBGBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQLQIjE3c2EygDGY_N4gttHHnrpfJ_gCbdkoJG_9QaF8qK4xMK5PSey66ohf_Q3XDBZZxbbX6TtsalsEt_oKhOv15UlYpkbNF5HA-lBflsGFpRPCEDvRTOBl9Wv_OmD3r_gXxImLA7sGZGTVYPVSy5mpb7e8goV5KlrM-84pc63_99glmXdeRePMSEDYVWIiuZ_Hn3p1yZ5N5saDlP7PI-e55XWqFOp-wtOnlThpDvYriv1jeSek9gkay4kLE-AdE10P6gTd0k2m2IBKxe25b67EvqVSysiA4wjr3QOZn2N12AJtTKC9S36qRpmghz1pgPuI0l6-WgnV8iayqkehiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7EIFC4m7904qOyBYPb0ap-sPnhqxOQiLtrZrvJcWumudgrHOgHb62G1Tn1nJ9mOBEpS2uHuskrka4FE6Pw5zlzY6XXudh4iI6DYKjLdzXLgQyqvw2FIW2ue8Dz9P53us_TpLHLlVhDZpmXfxcg3mk-5Ng9XssaT_acFzYKGCRlH6fA3WlIimrrHHu-7mSs5FRAwGAgODRg_iLDPXyCujCjnY4-xOhXXMolCV_UmDVSVV7qNl0rYN9g8IGtm_9VGKzki4qgzmsFNY2W60RPimV1_aOUcSgQLnv8hv0Bs8OHAllQKyODJ_1bgtpAlaOLDOuGGWyoiadPzI4Oudi3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvO_IpUGxCu8xTNBDFk6WoGBwjmkaV-9WTF7DdiPRjTPbGXciLpBPV4_syADgF0UBJGUHhWQdetBY_ODY2PPcBpDTCvQ4hbwZhANLDcQawJiMWx4fNC5zSjwxTDxWsacJq65KIvl3obp8lo0ll-onl42aCqcK7pdzp_cp9GHchljRtD412jQAdBEgLPZu3RLJDXwJMZiA72G946g5pDqPVIPTDdchP6Rc71wbqFNPX5qxUHvQgXxoyfFwNjm2kjoGwbvOOiiMxwVfURiZbytVeavnklJ3hLs1HhoPsHGj6tMKN4qwPmiUkR72si4USIFrrNS5J0TZ33ZmHkMhwxEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgANFirsfmjIbmZtHDbTaAygnKJsSXq8EwGOWtQQEDiqOyX3hhfoegJNr0_VpQLfckhRJYMfAVAUmGExHaaSEHtu-D-_kQuFAJpBpu8-cmrdV12HOYU8yOpAPFsRQOi1OKkCtV3VR_T2ZOBWXLiBn9yQGBe6Pfm37luva7BEYrRmV6d90rBuOknhqmFDFJ2UulAcFGkXeuDpzmtLhXAn2vzDcgKyeDTwcwmfHQHb1hUKUql76T59XHIdXZu-aWrv9BZ863bNCI5EZMfcO2Y1FGWGOUEYIknQekyKsOAdDgxDlHI3Y9BG2KRfHL4DID6bQUvhF5GGckarAnge1suQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSq12U6TL_NaRxKuelc4dlagrpJGrf_Z1P_hzhGJ_LRoPCjlEe1mh-VeDkeq4LY9aGOOkrjp10JCIob7OJMn7BVS1KJf8GjbDk7IWpeMsolutlXix0glcX1H_jmQ83FEgqmGZBL_k51tXHPBbBI57N6iZ8mrYBAtPv8Ki_IHW90BO7Tj7KWjelB7y1zB_rWVX08tfzTwWVOP1gKqU29uWyyqWrpZTSTnP3c68aCWREdiqT8x69jUJe9-yK1-Jt7Jso4EZrQLeB2eln6IeRpZIGNTFkr8rqvMhSg2zDFbdVUnL_gHV_gdP6BTQNyo0tv5WV3_lwdneBkO90izl8PhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLkqGufaL85nI0FeSB2RQ-s_-ibiXTiq7oz-ju5QMUw9kET9nfmUsGYN0ePKVyTnF5qbrJCmgy6XCETZoZgjj-wSNOhR6mdeaHnLe9IEwAKVNUsQDHvZRhkJVRAt6hLb3qUtnFwxgLpUEtxhkgXbZQl-ZaLWxR4gUxH7iwneXZGcWokIu0FDdQKIC1IuMUWW_AoP18Rxyqxmvxulq1knScjCVpSw_rnvV0N5WQSxOOtD0OfmVxvsheVNgL5KzWmLbRRzHq40E602u9TlI2utxOFvWx0KZL0jeBwZow0iSjyIG6_vuFjHwJQMFDPpE-KT3lJ4I7B47KnxtoySO03Bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=kpkNyjZUZ0i4L87M0FIJkwabJf1sVWY7ZW1a_rNOWEU29jrplGjmcoEoK_oTS5qDYSSHwepY2EO2o2PuQPuEcGHTXxoikRsVO_qJ3s6AA_KxwIld3TgXrEU4qW7x4qzwcUcxEcLVCtKGAqXSD7jqB7RdioNaXcdamfTcNCbL8g6H55NYFZf8yLxDjwVYsxJ05dd4djRJDUOzQddsEnQsvRYJZJvdgZnKYLeGa7ic1D-k8OWiofztQxT_N9S3HJCEbtqjet1iJWF43Scln7CV8h7nBBLF36qlCqRM_q_JqyELO6Y9GWASfyOAkIj6WU3p7oE-x9__y0-iliRnXxdc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=kpkNyjZUZ0i4L87M0FIJkwabJf1sVWY7ZW1a_rNOWEU29jrplGjmcoEoK_oTS5qDYSSHwepY2EO2o2PuQPuEcGHTXxoikRsVO_qJ3s6AA_KxwIld3TgXrEU4qW7x4qzwcUcxEcLVCtKGAqXSD7jqB7RdioNaXcdamfTcNCbL8g6H55NYFZf8yLxDjwVYsxJ05dd4djRJDUOzQddsEnQsvRYJZJvdgZnKYLeGa7ic1D-k8OWiofztQxT_N9S3HJCEbtqjet1iJWF43Scln7CV8h7nBBLF36qlCqRM_q_JqyELO6Y9GWASfyOAkIj6WU3p7oE-x9__y0-iliRnXxdc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsY7LZng9lHYzxvaxF3uA9fziQcYp2cXLzSikw84YZxEecK7WEhrxXmmKkR2tEWa02oE3NLLWvMYSB98xxoG4Fn82qTMPpr2jNkVNdfMPXMlWo34RkN1IFS5u7ncXq5APgaxok4HehTd7Bs3-cSSbxDoUKgLrdsKwNxviHwBp32f5dGzQQmwYXMu2i9wqfvXYwa8cmgnxPrto7oPeVbwy2F87nLibI9YlnzESp2DLUwISWxOPqTBdrT_bYD_YXwew1h9wdcvraAoDx0vyoSpilAcD1RYiXWSt-fesjPaxPzl7sIZuH51onUYWnsK3zTk-ZmsXHLAI1XQ_2Xse6vA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGVZVM58G1JXLLSX8MyED2j9Lu-_UVLS8whr-NMJFyzZdp3UPuLn7xqeOvFubVBWkem_zS4vSJ9el82cT9djrDQqxXYKGlMH9eqDyZwsOOhvI5FDRGOXOEAdO48VBEXlpK-3PauF4vWw0xMp06drgeSEk91Ur-JbfZnvl9WQCrEe-BT58MH9mgss-91j9EyMhTpLo52mh5liiCLpISCooY3HiVoTK6KGv4s2b4qz0zVvAjDqznoFuH4-W_hDHNTFCF7ck-SwjusLmG0z1Kfy7HjrklqdhvKVdmdjb2dca9iN8On1fXGugq1_6cQ-IRigLwfXwynXtPyuqflTa7XCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=FsBXTiJv7r74wA0dOKc27c9mSizRa8OVqtM5t7ns6wXM2I47A0sz6qW3fx8-O9ew65AXs2_w48S4fTgiGf8ev1EyYFvnflO9ogSVZT1wul6Rz890-1g8dbqeltMK6Wqi20UG46URp1Eiuea069Zp5MQ9dUFKd-vtpun1WH6Syh1maLoBdzLPPnnGqGQ5esR4rkCE40AC8FCltLAMnE2C5OfwdYW4sQyavirBpmJQG1q85P6pD0ML6tFGblxm1TH-jVrGix8P7_LgPi9ZCb8-WJtsJcdYNjkFuOV7GJ52vvydJPUlIQt9J4NTERgDIsRTgiEHm5ruP75COqeVCfM-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=FsBXTiJv7r74wA0dOKc27c9mSizRa8OVqtM5t7ns6wXM2I47A0sz6qW3fx8-O9ew65AXs2_w48S4fTgiGf8ev1EyYFvnflO9ogSVZT1wul6Rz890-1g8dbqeltMK6Wqi20UG46URp1Eiuea069Zp5MQ9dUFKd-vtpun1WH6Syh1maLoBdzLPPnnGqGQ5esR4rkCE40AC8FCltLAMnE2C5OfwdYW4sQyavirBpmJQG1q85P6pD0ML6tFGblxm1TH-jVrGix8P7_LgPi9ZCb8-WJtsJcdYNjkFuOV7GJ52vvydJPUlIQt9J4NTERgDIsRTgiEHm5ruP75COqeVCfM-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=swztQrZ-1RwSIKD_DZjYIMAgOhccTi_dnln3yhuX9UNEs-zJ6aBqR_yAbCXkuSrVcnfuypVXsCARcPD0a8wHJZPzsx2eXW8TBF4z10rKiHz3CAygWliEgBCkQPVTo5kbUmPQvjAdWTEH3HcgW0gQfvEtXcB9Jj93JxzMFfnGt0zysTo6XrFkaDJQTLorCwjkMSIc6fOSvxc9sSsoLwXnMX666HkZB-H9RjsCC6P0bTZkg2zzNuIZR8SUWaFxwt_EgXTEHVTn9QsLT90JgNVbLQEjIk47R6w1EUbwsaTPzgb5CyCAQHK_BglpYiFREeZ7FAEK4yBzKY5ojOgKkhlWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=swztQrZ-1RwSIKD_DZjYIMAgOhccTi_dnln3yhuX9UNEs-zJ6aBqR_yAbCXkuSrVcnfuypVXsCARcPD0a8wHJZPzsx2eXW8TBF4z10rKiHz3CAygWliEgBCkQPVTo5kbUmPQvjAdWTEH3HcgW0gQfvEtXcB9Jj93JxzMFfnGt0zysTo6XrFkaDJQTLorCwjkMSIc6fOSvxc9sSsoLwXnMX666HkZB-H9RjsCC6P0bTZkg2zzNuIZR8SUWaFxwt_EgXTEHVTn9QsLT90JgNVbLQEjIk47R6w1EUbwsaTPzgb5CyCAQHK_BglpYiFREeZ7FAEK4yBzKY5ojOgKkhlWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMgNAPQ-Udews5dVFw_L5nqzcxiY6nubaudy0jhCe1equLiw-Gl_9tq476q7H7iC1QqGJeyvECqa2mFLNsGJFAvh6OyOiezIYW8m79nHkDjfII7jky6UyXMdAMIwDGQA2szjoIUNn4zw9i2OiFcXDr1uIK9r2N7d-2HQCH_KwG13h6JhIQyISvCDibvxQZt28JUgm849N1HhOG2X2x3dmRhj4xcyKsxTnLgQFNqc2avQP4SKAk_bjm_YnmA6-A6X3lEFJ8-MWBWCjIbTj1HPcWEzqD37zo4KRzMYVPsG2Untg5vAl0PpoX6Kx_NnULraAINXZ56sV0vRJVStkd8YKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peu1s81To10uCWrRmOUcc2mSSn78vrwtVMHZPvYVutexSRqBzkHaqVoN1chEB3yNsruFLTaTxw_xWP7lg9SZb3OvStBu-ZtiboElLFk9-VvcZyPyY7L_jtTlBhdau9sNHnf9Vj9Dql4Vcfuw1tZKsHXR7Z1y49rVXqaLVGozIlMrCbjX2wbZ8zACAbiriPDdG5YD6BLUATue3cWmrQ587sNgxOzdmVYjGJxCD7BdblR3b7j7YNNJvWUAg8t3kJmFGi_xqLEfywGTHUA6oa9M_hSbGpJXLuGzkdPggTMazeXrjJ3ehnoOY1yMLv7A-ogt6wozQpnaF-wqqBcbEB_68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb1vTGCsa1_gzRlkV9Sae877KNK6y2Zp10qiV6IbXgvTM8NMlQbDm2I3LhWtpTvXYh2bUdzGeB-mG0VsUbxhH9X8JRAAEhCK5oeh8XJl6XJFdaZeNbFbAiPzX8X7t6KCCEkJdVctS4rC9D0nCeb7ElRDc1YXhIRpCpBAc5LtLWgOwDTAseTUu11-S_lRBq4H-v5QUyrFkXYNkSH0AmmPr2TKHOw6jV7wwaVvBWmVgKNpH4YGHWjk3T9fAGM9zk7Y4dtKCm7m3WFknHJA3h0AXrJWOpTK3Bz8DdJCf0U2cijv1Uv5_dvy9CUcmKALLErYHhcNLUWK5jE6mkZejsuiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvaHdMVyO7ZLY2Y6LG_UXM7JsIl1arE5WOaRxhNiG6N7MfX57-_pVgihLN2EgBgg1kGlOWpNBHJR19cHTI0Xebjy8nIbov0yIvEMMsqmmyW12S4rhhfvWaY_aX9MfFAvBD0AQKhHWCgz6pMUq9Zisk8MfkohA-xvpxNXpV6uhzkUrdn0CxW4u1Zb1Tv4fdWQ4f93KOQ7XYgWAslQLyiZKEKRFdr1adqkB722L06WATJZGMoehiWQbmSRefR2e7JdD9BZgPXVxMOHOXm2kTWfd3yk3r7lX8lTcaCVS83XZ0MJdlTyelsmGh51F0UDf5PjuM8w8CGilWpxSZjH-hJyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaW6pdKfhQmz86Xd_DVuh6P7ifEiCXXHIMVgXI3ImPv_LJF_dFf2jnNiK6OfK5FbqYrbdAYfnMhKSYAF0jEyFX7IQH971Y3Dxi5T0WE_VYCvsMCvjbeb_LF77pEPQ9aTs9b-eAtYl-AND5Sgmup0AMTcRY3L1ZMxl11tRyGDVXCbTj27TTi5D8yS3KstG9dwfoMEkrb-jkxLzMiRToxSr-qAIidRHoknkxZQxOpQYfobZQdT5xylPHxWTmeIbGv9Qblim3ZYaUz_lUOEgkJbPtnIe-zoCvxLz4-DawcWtULLk96Y25_oQRygYkiqS0qPOENqsBrYnZN0YUFRDkH08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEm2iS0hAUC6AT8vAyeOWGjlUB7VCm-6JKY5vEyau-ftgehDyZeQN2CDZ7BBy4PVCiBAOAZ9QFfoAm43UEUr8O9zPFo3gLJMksBHpYkWQgsOQ08xoVr13qHaxH0BqrxeDSuEIOLHx1HOerFeOnEwqGIH9TVsMqBKZBoGLrTPbwc6fY6A-Mo_wscKMT5ywLMduyVpzMMDfV0SZlpuO0AVETj8eLv4fiW4D-O-dpJvCDY8rbO5n7AvcsqKrbpfyAUFqi7lolL85GSFNoivI3hCkCuORAKinCGCqCe3nfkaVcy787kCPWm1pvNyr65DrrkrMfM2bjAII70RAXZWJBzang.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=IHsf2aRRTp7V4fo5XF1hB__5MX91C9_cUGFD0RrqINATB6KgZVfYRg2A8l3GVK4UUPDj_QNXcmT4sEfKhOjfOawRGsvbSdhdDgygJwzSCI6ptiJz8g_98Xr4tisG53flYhfGjWDp7XYtm-8x-B_Uyo0nxd1nTMRsCVUTlF-SoFXYyr8-NM_ECeiKfP2h6ouu_10N6OqukgeJohIpH1LsWBXoJfrmqR8kHIw5IfjYNYwcDEaEKQeN0Hj6jcJw2Wa8JaurWXiCCaUsglnxU7CbvLboxiCh0hV0HzIWbtK9L43OuZZRXAPaIIjAvu7OkCe1zpwTDJU9m0MpyrulTEbDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=IHsf2aRRTp7V4fo5XF1hB__5MX91C9_cUGFD0RrqINATB6KgZVfYRg2A8l3GVK4UUPDj_QNXcmT4sEfKhOjfOawRGsvbSdhdDgygJwzSCI6ptiJz8g_98Xr4tisG53flYhfGjWDp7XYtm-8x-B_Uyo0nxd1nTMRsCVUTlF-SoFXYyr8-NM_ECeiKfP2h6ouu_10N6OqukgeJohIpH1LsWBXoJfrmqR8kHIw5IfjYNYwcDEaEKQeN0Hj6jcJw2Wa8JaurWXiCCaUsglnxU7CbvLboxiCh0hV0HzIWbtK9L43OuZZRXAPaIIjAvu7OkCe1zpwTDJU9m0MpyrulTEbDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc82WVHIN2psYLNF9PHcMGKvZEB4GXmO3nG-GnXR84ByzvmCyian1fMmCbdJoh3neJjxBVW-LIUP-uoWHAMpEvxmaI2iGEISpj42NwPICLm3GL_HFo7Zf91YIj606yXVXx7ICzO5f_HXGjLAGN4mQDaZdef-OeLdPVbxoLDZeHY-UhPChJcjXnRR77jJqOs3nsznZIG3_d-eYPQa5HitRHiDbu-Ht-L2A-f8f6rnHq5WM4NInZYSv4OyNKDJjFtusOov5FBgSrWcyMhgme13jdMrOowD7NS3u0Psq5-y-a9_94woinPDWq7Fj9iUiKbDYD2_37GKgcwSSxwj5oWm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um2_njqp5T_Ixq52Y0gwvzZhTf3Vp0pgja1MKZ2fDwaQ0_PKxnTSf9avfgDDS5LxfUL6L2FRv4mirN4b4NRFH2xAqtm1g2kbFkldgmUupumyqBPu9V6Rip81NWDnm8Pvmtc3wRrobAx4nZWyQnV5wx4Jwe9NTmk7E7EzBSA7xFr-pZfZW_8AfiVpFvM9WPbRW0w-kDyIr3Ll0BxG9z-PlB8Qaa2r661x-RKEheSuPxkJpNzwW-KJr2l6upsoT36Csly-p5l4mCtdw5fzNFCm0Sj28Nwwc84arTsnI6ZL4innz_WTRwQOXxo4lq3gIl05lgiMh6T0F6mk1zhYpp6vMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUq8SWlbUuZmxjE0bHeJs4oqYARf02fqANS2nOpKulch1zLzqSe4dLGWxFyJgKohzUnT_G53D09H89F-vBiyvYvYBTnwhnR51HdQ8efm2H3v0fyvQrcMnrW7vvOnb6TaRyQxI3_XL6upywhD18Gtvl3KG1_aqjWV8LDPb8a10ugxDwsbbXdlot4NEh5E9ov62PGl0nPrOQ64DNSwyciACgpcMzNS6Vyd1IbW5PYHakUnZafFbR5dHidR5QgM2dZISJ3KuPBTqhxK6vKNlNnv8xPvOMpoHtmNguE7HL-HG6fIQaRBC5SqoWfL0FmSfrhwTv4Sq8Joro90e7qGHFD31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sODJbI47tK4uUPtxmakOdewQ0VMYjivej9MPzKMTgY4KYoXxwzo13s-KGe3nq3z575tIfM8jYufmfAv8ZZthQbZx1oaSJp74WHfa8gilOWQZ12CNN8WtFqeo31e__OTxy_zHfHdt4vvr3Eheh6bRUBV6DydQuQAqjKl8xgBy2JS9ptFZ6p2grAU5k1ULWsYdg-4j6t8Su4aRGHED5tC7ig7W5uFvVi6y_XoOk5UjMRuAScn--XGhN1zR7VUBDUXXSC3OvP_QT-jMfnmsZCFOcTIHdvhrdhgAElhxIFfp5mv06_pkG0xrcqmOJQlK6stE9SfLOlAC0yfa7jx9GFrbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=UJG-eMOnO-oJQyrhgbnzUqE2Q6NezvhLPbzkFGw2Au2CcjWInI9TOvc028whKYZnWefXpO6sctMQov1JWHq3mOExlWJPKuoB4irTDun3Glm-NAxgAtq6l8p4CFbP0NnCBA4yJPhhlbSHKa1Bd5et1CV1RGDoisJS4DV3IuJ2f6pUqsIUSUo1QJf5Bvz5EKUh2bWClSvZ1_gzJuVgpvpTDZcxC37-7xlkNyNH-4h7-QPJfdy7RTnLs0UnZa-ykPanBlaaM_1dtIUXMnoufT62YoEpgrItInEq3V3HXoRbgEykey-I4TjHzKrHWJiUeK7AhdQC5mx4UGRh8-pGB9rS9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=UJG-eMOnO-oJQyrhgbnzUqE2Q6NezvhLPbzkFGw2Au2CcjWInI9TOvc028whKYZnWefXpO6sctMQov1JWHq3mOExlWJPKuoB4irTDun3Glm-NAxgAtq6l8p4CFbP0NnCBA4yJPhhlbSHKa1Bd5et1CV1RGDoisJS4DV3IuJ2f6pUqsIUSUo1QJf5Bvz5EKUh2bWClSvZ1_gzJuVgpvpTDZcxC37-7xlkNyNH-4h7-QPJfdy7RTnLs0UnZa-ykPanBlaaM_1dtIUXMnoufT62YoEpgrItInEq3V3HXoRbgEykey-I4TjHzKrHWJiUeK7AhdQC5mx4UGRh8-pGB9rS9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=ivrdrHOWHCm9UxC5qGgmfnZMQT0QKGS5lEjjL9sTCqAHfdsX5UPnX_cTfpAnciMZl2t8ZJia3dZ2Wm5mfnNs0XQBLu6x4Je8u8755OZfIj-n_DMgy2WiCPKSUm3T9MBVKuUpsyMxnW9--0hkGat17u-f3VDOVeUuPXb7UQj5JwEjxX8tGJO_tlsh623bc-rtiuQ8NW0XBK6Q2G5d8bkDlr5xQW3tn49uPHLoUebPQgNeU6rczqdGzKSblQOzhJz1IHbcbxWAI1MyeIc72oVZVrvC-Qi6bIrO3Qg3J_JqTIH66hiWUZow3ooKOyF7m4jDHfPNnxpgWajDmpimOadrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=ivrdrHOWHCm9UxC5qGgmfnZMQT0QKGS5lEjjL9sTCqAHfdsX5UPnX_cTfpAnciMZl2t8ZJia3dZ2Wm5mfnNs0XQBLu6x4Je8u8755OZfIj-n_DMgy2WiCPKSUm3T9MBVKuUpsyMxnW9--0hkGat17u-f3VDOVeUuPXb7UQj5JwEjxX8tGJO_tlsh623bc-rtiuQ8NW0XBK6Q2G5d8bkDlr5xQW3tn49uPHLoUebPQgNeU6rczqdGzKSblQOzhJz1IHbcbxWAI1MyeIc72oVZVrvC-Qi6bIrO3Qg3J_JqTIH66hiWUZow3ooKOyF7m4jDHfPNnxpgWajDmpimOadrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyeEJ15tD8uxB_UguU6mAuJKjOMr5C7WPw-QWKyy3dg7U3cjdQx5LcYaTPJqSlDKZoVp3efnKbiBGxTS3eE5wSeFwHYpmZ53rRyZpMbG6mROxoLU46df5lMQwpWlQUxZrGwEVFvSe-qSLiJh6AMTr-3ipKOjqVEfCXOeqEAKL3IjeU7UajHfJkvjdPbtMGhXttZVhxsq0I1yiVislIseInTzB91jqo9RqS6kYZ_YkqPPWEiDB5PrXg-BsGs9HQag0X8MLgZxPB3qNZYGJvSTWcrzhi7RRfEY924TeEdgJqP80z6U9-n8XzI4GXElBp9Ri-Wa_-vTm0XnQBmHbz5l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4iPkajZcGSb0_vUk_TAovHALy23aw3xd3K6-h5q91GLFyzQCznLlriNDl9EupiLmhqYmfdTTR9gKAYVI1Mqzr8WSFYQUXY9GO18xzg3Q744_IkTpcZaSLgIMWzrbDEewUVsJ7bAbOXre34uhDCDeffCcWlZas7NN09T2hOOD730ZpV9iX1nlhHs6V3IFfvWjDmV_ilP7BRe4h0Wh834I7jGiDCIhUkMaz8Ue4kNuuypwzUf4F9HCzYO2gPE2KOz-O4T9XmOd8yHEV_1jcXeWEskap96P0U5n8TN4FPWoyky4IPm_Aeu6fY1UThLdTcde2RA_hNipE2VjE3TKr6scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=TRJ2Gv8BkaDm-OI4ROQhucXaEzweWUG8yepkUQ7MHcWChnczWLEGhNwdgqLcT-BIOnNw92K3LLKX0cVxKq6jLUhd8LBhjOOQHq80d_KHP-w1084n9cr425Bm9b2t6nR-fsoNZyS0M9TdKUMPcDdDdPaOLQ8DMVzinGPVzA-tB6A-nHCmKqSy0KTXZEI4PmQ6ohbYHHKrP7XoZeiuxTK9FCgqehxZFv35ABdPV3V347JJtURT6_8Isg9BMLWb1RxhkDv0jR9t9B-Latr2mKoCZRfEjHfUowCo3vUpyJu92xNwDMaBE7GGpzaa27RUHeqbaYOcHA_rl8dOi2K9y88uWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=TRJ2Gv8BkaDm-OI4ROQhucXaEzweWUG8yepkUQ7MHcWChnczWLEGhNwdgqLcT-BIOnNw92K3LLKX0cVxKq6jLUhd8LBhjOOQHq80d_KHP-w1084n9cr425Bm9b2t6nR-fsoNZyS0M9TdKUMPcDdDdPaOLQ8DMVzinGPVzA-tB6A-nHCmKqSy0KTXZEI4PmQ6ohbYHHKrP7XoZeiuxTK9FCgqehxZFv35ABdPV3V347JJtURT6_8Isg9BMLWb1RxhkDv0jR9t9B-Latr2mKoCZRfEjHfUowCo3vUpyJu92xNwDMaBE7GGpzaa27RUHeqbaYOcHA_rl8dOi2K9y88uWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvWmrkNfxgH4siWt1PshEnBrnz1s2FBLke8IBHUDNvNMAlwcdCz-4h_KDOeiHH85Az6jDebGVZmq2_7iQ5IAyIhN9F2QJPI3RGKiFffu6uZyEKn9_MLXJ7pyYd-7D3kFi1ekbp-8GKc75jQ3BksU5Tlto2kALAoCmt5xOFP1nanFn9qdA-EzdwipUAVCIT2LDYSMyvWjA1NiR8D1tHeHIX-2uFIGCMqqZulcLuC8k3c23re1kzzqZDIlz65BiHEmCrxTW2bTPv1CrWRhUc74dMcYG-DdAuBKi12lhPR765qBtfqqOlM8U9Npw1bqrzs2lQLvFHY0-jevhC5LEux1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=VcJImAhlOOsfeO42AF9dw88286b-cDzZjTUkv8aXyA-1JC506FNQloesUzQ1pfpS4CWiUy7J6UHdgfsw9U1mLYq2DUJrT45FjgWBGfCS6HPDGuEZRMsqkx31VZGiqkX3OVJKbKDIVlkYFwvTVORo5PV-b3VFrQZHLwBlHrg13FCCfYh3Z82YUm7tcNwN0e86ATYzY0lFzHpJxJwa7Ym5ezYi_b37tbmOKF2sTicQow5I_8W0ivxafBXz1lZyCSqwyDThPkx68clq-wjG_HQgN5fp71udQDivawqMZzF9iJT9ml4wmH4tzmkwdLHVeLfqC_oQrfcEU_75Uehez4_eRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=VcJImAhlOOsfeO42AF9dw88286b-cDzZjTUkv8aXyA-1JC506FNQloesUzQ1pfpS4CWiUy7J6UHdgfsw9U1mLYq2DUJrT45FjgWBGfCS6HPDGuEZRMsqkx31VZGiqkX3OVJKbKDIVlkYFwvTVORo5PV-b3VFrQZHLwBlHrg13FCCfYh3Z82YUm7tcNwN0e86ATYzY0lFzHpJxJwa7Ym5ezYi_b37tbmOKF2sTicQow5I_8W0ivxafBXz1lZyCSqwyDThPkx68clq-wjG_HQgN5fp71udQDivawqMZzF9iJT9ml4wmH4tzmkwdLHVeLfqC_oQrfcEU_75Uehez4_eRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4LrPvP1HE93uQV66qloefxxrw9XUy-2Q83v5e-lxs0192s2s3-1OcKquqB_p9hJ3U_QnTYLHpUPIY94BCgyNMvMV8-9kTCKIdWrtLT_3wqGyELX6_OFE-D_K4E2Mh0nHm5ktUCRXX3SWRZ_bIjvXcNA_KJVoFcBGUAl8XYGX4u1HnXjsygOqmLoT03MhctBeIGUDSxAVF-vszP5dg8VQIT2AEf0v2WeMLahTFVv0uWxgMr8ukGdHV3HcGNBAjfpx7KDdHSqgU3IzKsn2Oa5HN_BKgCObZekQAQcBOQ6vyg2hlqoEubS9j9u8sbDhAt1F8bRp1e6q3G5jtYjoVM05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=fviNLwKRuLnEh3MSq4Z50zuyBmmIAY9fURYEHG1L3CNxRrqtr51ZvQaGZJxJUANLw03_TIJ5cSpXR1Ts7Lkw9F5H1QmuKQkZZWFI8xG0ieMGy-ewuraGzJgX9dVPHLOoHpiJfXZkt85F3pigAKK9U9Y8pAQ6mxDZ09kiuslBZjstVQFBw2i7TNnfcB-d0nUr7FT4IAwzzxNVy3Mzx_jzst0_f8m0LHw3vejpeShL7yrvdQtAFuYTWAhTZdJ_cEdiN3emmFiFWiOekl0mBM4ElfuDIHqfkLuHUUS9c2EF9XwVK7EktKabepxeco2NQQl-SYbVxlH0MIq1R6FO7vbcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=fviNLwKRuLnEh3MSq4Z50zuyBmmIAY9fURYEHG1L3CNxRrqtr51ZvQaGZJxJUANLw03_TIJ5cSpXR1Ts7Lkw9F5H1QmuKQkZZWFI8xG0ieMGy-ewuraGzJgX9dVPHLOoHpiJfXZkt85F3pigAKK9U9Y8pAQ6mxDZ09kiuslBZjstVQFBw2i7TNnfcB-d0nUr7FT4IAwzzxNVy3Mzx_jzst0_f8m0LHw3vejpeShL7yrvdQtAFuYTWAhTZdJ_cEdiN3emmFiFWiOekl0mBM4ElfuDIHqfkLuHUUS9c2EF9XwVK7EktKabepxeco2NQQl-SYbVxlH0MIq1R6FO7vbcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLdUqdH1M0uOxtoiY3EikX_iowqnyHTsUAbG9yctl0NRZ3eD34tallZvgItpgyMHnwy_sPQ1YYvT2YC4giaMYJsKzkRuJ6PO1zRp_ilSYk3IIC_Bc9I4RD5C9MXa-SBt_DerNYg0O2bWfwT1CSkbYGhd82KdsgScpNzPGDaT4Y794QjuFQzeOSwPTum_rWjrW-0ksNY4olBXYGnpQaEygXf9LVv4wMYSCmW55SQak-vcpMPq_3vlmaWJU2Pb2ssutU5sd8N6-uVycR6X7jhHuGLSh974sWOFTX7bj1RylNrKmaEHUNk0O6AdVA3hDEg23fIb2QJyWMvxW07xz9tRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR4k7wpY-2-18PHZIfKAHIPJPN59qgkxubkI_KHzEmZRiR3n7SAfPz-2jkz2qVBuNMEhez4w6Y9u_MG0fdPddxOpQmQRowHiiVUBr6fW6yKW_02DVVvXvH3GSsCD1PDWPyDslgfhIi8nicZZY4cEJoMf19VKpQMJgPdvlrREbcnUTLLdM9kBMoH1atVIJea7r4jRUYY_b2CfjUD4cTD8lAGJP3EONcjZ9TbXgYYvfYwp-GDImbr7cTceCfk6_ft5Ii60yQYDGuQbB_ZdMmUKnUqgLRTM2DbJw6C_7RG1PEwyzLvnmHLw82O9SwAof26kDM6ujCu5QC2Z6dPq19zefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚽️
خلاصه‌بازی اکوادور - کوراسائو ببینید لذت ببرید ازنمایش گلرهای دو تیم؛ بازی‌ای اگه قراره صفر صفر هم بشه اینجوری‌بشه‌قطعا به دل تماشاچی میشینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24066" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=sr19x3bbm3fw8ZWcRj90V05wVBdMgJqUQq5wT3Dc1gEhA4-1kXQZyVHhGGoNJQxPDi8K1BUb86FSxgAPfDJ5VLB8QnjnwpLo5UXkFE481i90om8KE_IYTW8SE2JtBoa9UXghmI-YZpBtQ11S5TQFwX5o_Ary3PI-ANMXgpvjpqfDvTgt0OhLMkPDSN6GVZtfdd1o_RKjpQ2AybVtEffqnqYfywwZJrDsqSjo89Smbf7F_lqE14_X8om2JGhKAwxtmlV6VtjrG8hJHQ1dirE_kAKJKVqbBsxG2OJkNKtSlMukgSSpcEsMgjxmgcYpBGdjwb8acFNW4nXwe0fJWJIM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=sr19x3bbm3fw8ZWcRj90V05wVBdMgJqUQq5wT3Dc1gEhA4-1kXQZyVHhGGoNJQxPDi8K1BUb86FSxgAPfDJ5VLB8QnjnwpLo5UXkFE481i90om8KE_IYTW8SE2JtBoa9UXghmI-YZpBtQ11S5TQFwX5o_Ary3PI-ANMXgpvjpqfDvTgt0OhLMkPDSN6GVZtfdd1o_RKjpQ2AybVtEffqnqYfywwZJrDsqSjo89Smbf7F_lqE14_X8om2JGhKAwxtmlV6VtjrG8hJHQ1dirE_kAKJKVqbBsxG2OJkNKtSlMukgSSpcEsMgjxmgcYpBGdjwb8acFNW4nXwe0fJWJIM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24065" target="_blank">📅 17:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXj2SEYI1j0F-mgO1NECL3RVAaXtFaEqmp6JqigLopiGdv_6y7hDWgSXeAWzjAL5mPTaHxM4cO8uzpubKMIS779w6ZMOfY7wa6hf3dTpuBHi2rZ8ypOc_xlcjjDVPwAenqXWVZpAqABnYo7sV5pclxeSlp6JouIdMpXMbEpXUKXa3MFLbm3IIop0KFtUmjjxHF4xK0W12FnGZVs7X5lpTQQ-N7vsr_S2snhg5smr5uWg383YIHXxnVes-2Sl_5xlk4mk8wicYrE944mYALiH9xaQVPY9RYfH6Sz0UBkzNX_DA_SaIaXfJMoyY78Tj3r7mOWlcYHwsNuWxxlgEDkQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24064" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN67WhJ1qFHplGe15MOgzt-D97B65Ezh13kt4vpaJ4wPPn88RmI565caDxil3Jky-uI-f1ufbB61fmNIGSV617oWnpGO09lr5oZeofJ4q1gB-K1qUc8Jqscl7eGhvS7WYcICmxZWIfIdmjrRXqdcNWbN9tdH7G8VDky10PAILYRobS3_bSJRER0AcYTSz5f6j_Pdd3tvJvRABItVV2ZapI-RdwodoF9dIdHOdeKTxfr_USOMj-fM8jNiLaeP_s1qpIR6VX6F0Vj-DbzOp0c9FpHtFLsIrDPj1umqPK6ufkpSJ12ZrNsm4D-VD82dXl6qWDkRSnATkbFYLMq3sc_KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 گلزن‌‌برتر‌تاریخ‌رقابت‌های‌ جام‌ جهانی؛ لیونل مسی به رکورد تاریخی اسطوره ژرمن‌ها رسید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24063" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFqrSHt6r6lC5nMRa5F_Q-sjAaTu_0K6cfxY_mV4npl1MRrGZ0aQ_BXFJzyMPGMUP2jrcDPS5lbkDwN5lEwcBQ29rk9xVMtPDKN5k1j-_gTD2gNB7MwJpP1oVL4wl9-pzj2WIq0C5HU-vczbULE7KDU3DTO14i2xQisu_INjHuw0zwc_mM5bn0pCZO0Kwg65NAP8_rdCJvJuFH2jauGLoutfzGpW3grpLJ_iQvgWZkdVkcEO7O0e7H5ehmynUx6qvEnsxXUDA-J_VbExo12CfSFNM89L0r4u5walBmkOcMLHb8f4DpiODeDiZ5N7AAjoOXEaA988DmOPA0HNzv0b0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی وینگرآلبانیایی‌استقلال با انتشار این استوری‌خبراز موندنش‌دراستقلال رو داد. مشکل پرداخت مطالبات این بازیکن برطرف شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24062" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=dfyLnVE-fYe0xTd6TsFqoEEgr4_XBs7Nz3i6CwyDw69v9eCFCk8iOHtDdOrDtJg5OXTGHGI6JSELaPY19j6mwC3Miy-PdMofpFAFcvc91ZZ5PgjakoTQaOPJNhJedGGyccDfHS1ycmWKQeZGEAKmmLHH6dtwEWFVulkP_--YIXhhPWt5j8bGpUVioCwtxHxa2FWm_M_wQcvo22yBYAA1wcRIelWkzdk3mY4IvTYPMmVFvfqlCffnb6sS6mpPCQTtbTKQhjs0_dKoA1TkAVYr8yKtiN0o-4lZ8L5R-pykNH0Ym9jy0kYPS-UJgIHi81_IlsUbkSkKb5TH2JkoGr5pUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=dfyLnVE-fYe0xTd6TsFqoEEgr4_XBs7Nz3i6CwyDw69v9eCFCk8iOHtDdOrDtJg5OXTGHGI6JSELaPY19j6mwC3Miy-PdMofpFAFcvc91ZZ5PgjakoTQaOPJNhJedGGyccDfHS1ycmWKQeZGEAKmmLHH6dtwEWFVulkP_--YIXhhPWt5j8bGpUVioCwtxHxa2FWm_M_wQcvo22yBYAA1wcRIelWkzdk3mY4IvTYPMmVFvfqlCffnb6sS6mpPCQTtbTKQhjs0_dKoA1TkAVYr8yKtiN0o-4lZ8L5R-pykNH0Ym9jy0kYPS-UJgIHi81_IlsUbkSkKb5TH2JkoGr5pUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24061" target="_blank">📅 16:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnVpkevHfgEaWngsTsiOe--wHnBZ4xZkeGFdsvU39iA2l5Z26KmTUHL_PIM6IdRvKT1EgLb-eudQm9P0tE7fOhqku3NnwXj7Sd1xuPzKe16FNdXl_xudds-zIqvE4c1DnUmL9SQ39i9L1MCrRlsqHizTK4AYsz3WEQoP1tmukNZkr-cgHzTmFw-nVOxj3R1xCNvlT7Msg2uJK0QZR_pu6ptGPdLgBKhD5BS1kaToeobxRPuGK_YpOWcoGVtUCFsqzPEA9D8T3gyHFwFOlcSFs7LCphiBcOFxEfnVBSsTBfpepTztw6wJI0gprhd-fiW_I_0PWMJP79uNEx3cMy6E2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqEB4pws_ahiD3_HiAiRmPsgiBKxD1Plwux0G-I6NyK0MEGT99vB1HpbxFaPb-2JFErIYqOkwHKtpifEkihxtCzk7xImGBRCKptf-eT8q86qHOmo571tNSPChTFnVIPZ9XWn1GUomosTndOUbl95nckVEfUH11yC5zYr6Sg9wq8H6r1mQjdK8lHz7cEgK3QffOrswipiDGrbFkzGIdJlng5mbmkp6839rujbOntuM850F5OhVbv9E-lE8vMP9z1h8k1xE4awr1n3xa2xY9wdjWvlrhH024KDjM1vG437-B84LCauLM0f9ngfEiXaFFzVR8CJSE4ppPhibIng3vMmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-jNB8Pu7WrB0dubW20ZWUxWgvSnjP984_yhcMq358K9dbGJaiZYvZ__GnUOQj6GXrv4ewGMY5h03_co4hpK2r_RmeP9MABGDVlXS_14QQaIrFwCd82D5UKNdnYd33XAI4qpLLwWPp2Pl2xjJGBY1Lp_HMT807keva3_pLuFctH0Y-Wxolm4OdoaJgIiuDcFJ0L8pq6jc8HFNA0OfVnjtkDObZckLuCYbsvURXyvh1PxH9qTDdvNRrEfhDkea99etAYmlgvDwBytZgyOooNlOSPYQ0GcgmSe8T7t6DInjk-YV5Ux4YuEiz_HSvqn7iq7wANGWsqJdDjllN_XlaKjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSamIJPz7aub3xsZW7SyTCq3cRAHKo1XeEF1Yl3PET_uFNIGXrydMNePXgM0eCGxKfvrJkAZxDh8YiPJJC9MckBpkR4xFC49sVUIrYuL_4-sJDMfbxABbPxXqinfYguMSrkoLgafDDAo35Yqz1mEnfqFVM8vNw89Ypn7ngxirYlDlk-jbkdOXuOF8xoahmULyosmi07Kd5U02ujLmVOaGgW9E114qz-jCYQEYqnY7a2-KgSvCy-cVNMWHUMdRH4uDcpY6Vq7C0BjfplUsyo4V6qlIHoHdpBYXflBKVcmyUHf2_DUnKT4NR8W_C7nJ-qCdo9nmJ7ga-mIBzEuiJPiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی درمورد عملکرد علیرضا بیرانوند در مقابل بلژیک: این سری خیلی تنگ بود خدایی
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24057" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=nL6GQ10Yw9sEyCLi-tFYf9ONgeIXRO1mz97BsB76wnCo6O1zwcWF-GetQSP_aYEGbzV1aZsnnOzzPlLXhu7P4SkHRtXjx2Gm8GcpK_Q3Rkll-_X6V9WE-dmQHF9P7eGhqGbVjOE6cHR4D_Y1Gs3wTahUBlVTG_GgqB13s3KNvLjBw7Kq8NBsLmyI3Yl2UoKiZ4mYkU88rHIhWAkYj9qIcBUs6FwD3Ln_bRlIoPSfWjHXUT7z9NNMt8xNiXWyz298tWbdVNhuQ6mEnCDCR1lhzqyDPvH9lLxpeGZBiAJpNbPkBd2Wz_Xvj2I5noFPYf5yNVBMUJ6-4LIs4fhRau1oVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=nL6GQ10Yw9sEyCLi-tFYf9ONgeIXRO1mz97BsB76wnCo6O1zwcWF-GetQSP_aYEGbzV1aZsnnOzzPlLXhu7P4SkHRtXjx2Gm8GcpK_Q3Rkll-_X6V9WE-dmQHF9P7eGhqGbVjOE6cHR4D_Y1Gs3wTahUBlVTG_GgqB13s3KNvLjBw7Kq8NBsLmyI3Yl2UoKiZ4mYkU88rHIhWAkYj9qIcBUs6FwD3Ln_bRlIoPSfWjHXUT7z9NNMt8xNiXWyz298tWbdVNhuQ6mEnCDCR1lhzqyDPvH9lLxpeGZBiAJpNbPkBd2Wz_Xvj2I5noFPYf5yNVBMUJ6-4LIs4fhRau1oVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی چرا اینطوریه؟
واقعا دیگه خیلی عجیب شده، یه‌چیزی میزنه به حضرت عباس؛ لحظه آخر قیافه خداداد عزیزی خیلی خوب میشه
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24056" target="_blank">📅 15:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei_ijLvwZ297ECXIazFiynqaoT8eAcpVMpwN_Bk7B6Tei8c3CgteIvW20Gb0lAdgB8mJjbhuZTKT1rNgWnB9ntwfhMm2N36ca8qQ5L7vH_BI2DrmDNY90OlZMCH_oYOHq_XyEtsnZo2MdAMmdspE5b0sDfJZcra_hsy71_nROOFvJMxRdDB07aQeQmILyzLgRREMKrhRF1D8GNQNkw9Gm8bg3fcd4bQDQmSqp0yW-o2fQARifFOtFnu99wHBzRzNFnzzbM9QqqRZOiG7wCAlcxlNFgS3ulNOsCFnT31AvtpyClOohPN6zkOxxk3bfnotCk55PYSHCasTHxbId32Z6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24055" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=lZBs0J3TmJB9dqbNfZuefI9_ffyVXzqIB852xuZ0834vUhzOpH1L6egtE9Ss4UTfawUlLuiu9l_BCxfHp9NGjo44lMc-feYAA7Xitd0yNvTu7A-0aoacwqehytBOd2Lri2_RV5QE4rNAlO3BTcP-prmYJAdOGvtuQlTMI0dBHjxXYXOLVVcT6uFKq5hSgunqKcMMogq9yRAQ-BDLyCP7gJZNiEoPKluT0uaZPSBEItwiYjIt6MYbpsNPuWRoOAnD3kAwCOmknyZEcQG7PprVGVJkpKdgB6G5oFA_0sfik8yMC0CmGP1U0P94bEp73QVLJjFtq7BXrgeN315tCjLRcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=lZBs0J3TmJB9dqbNfZuefI9_ffyVXzqIB852xuZ0834vUhzOpH1L6egtE9Ss4UTfawUlLuiu9l_BCxfHp9NGjo44lMc-feYAA7Xitd0yNvTu7A-0aoacwqehytBOd2Lri2_RV5QE4rNAlO3BTcP-prmYJAdOGvtuQlTMI0dBHjxXYXOLVVcT6uFKq5hSgunqKcMMogq9yRAQ-BDLyCP7gJZNiEoPKluT0uaZPSBEItwiYjIt6MYbpsNPuWRoOAnD3kAwCOmknyZEcQG7PprVGVJkpKdgB6G5oFA_0sfik8yMC0CmGP1U0P94bEp73QVLJjFtq7BXrgeN315tCjLRcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
نمونه‌ ای از وضعیت متناقض جامعه ایرانی درحاشیه بازی شب گذشته دو تیم ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24054" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suPFN3GoQc30dlqhKX0ry2yTdLrJ3pFZV_ytLog1V-5iA_X-4MKavRgmQcbqLve0YPW2GnPMU2qJz7ktsYXL75Rp6FUH-XvUzk_zGz2Mf4n18atrQOCh8w8-eLrlWk44oL3_2_uGNDr9mgds_cJrKkPN9Sm4y6g8uKFITH56E1d0U6YbJByr-G1zb0ckiJ4pOYRPUwJaF1uiCR0-3k-WEkjAK2d096h5PzUWX3BXYaA3suc5YHgV1yWGP7CLcDLgYioXaJvTcc_jFOVvsLvUqyINEqgSYNIgU4ePbVV3sTwVCXt219qi-_40JRW32Qm2e4ksyKTwJcxflxk3oGUyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
استوری معنی‌دار اوسمار ویرا بعد از مذاکره باشگاه پرسپولیس به دراگان اسکوچیچ: خدا همیشه خیلی خوبه... متعهد بودن، حرفه‌ ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است. داره به مدیران باشگاه تیکه میندازه میگه وقتی با…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24053" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNqnrlCu1rPDK0C570HrBYQO6BnCBzKIB_CoFjoTqJ1OGBWyFphqNSU4JYUJ6AXH4mhxCFymzc_axOZC8V4JoCoIJNrDzu6FWkjqxAxQBRZ9wdeO1tGQp7ihd5dQInxrj2Fncc6coYUWaEyx88a9FmBreTdCcHTLYE1JcL15G9W3YPuCz9xKvHvQ2IppAtjwXFj9lRSlSkJs-4jUIM8Wp2-L1zj9_Ypv0zI0XLbI4sp9PnuSigjaIdwLSnJnlL9UByfwb9iD5LimYlGzXrJMDQbToccY4RKoENOBVt31FuQZAh6KjTXb0KscKJJaPMmPdIWR2OQK34YsDRL-YROKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24052" target="_blank">📅 14:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_6tpW1HOS-8sTrJ2w0Mcgg-R0NiceGb3RQY_wZT8EGO-nR_h3o0m_7A1WTkilPAfir6DQ2xwz7gtS7HnrUQ1KN9Q5jpfLJj-HpKVPJcaC-pp-pJjsLK7WFoQigBlfNrW5GHdWdJzdG91fc2qWouToG8LRccI8XYzh1e5MZckfVLQ5H1yfoqdwoD7kINmHQQ4C3S8uFMwiBwN41hQ0yAKiN_Dx-Ss0Br8EM6e-ynC_rrmmJVaQd0uuM0SvxxoeD2AAG_XUrgmnDSXtib5YFEf76_lI9cVcS4CBnHOFxlg24qijrg27GFTWONpqIvE6HExxsKJ50vcTPHFZJHSdFJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
در آرژانتین یک دین جدید به نام مسیسم متولد شده؛ این دین جدید که پس از قهرمانی آرژانتین در جام جهانی ۲۰۲۲ پدید آمده در روستای لا اسکوندیدا درایالت‌چاکو آرژانتین درحال‌گسترشه.درحال حاضر 3900 نفر در این روستا زندگی میکنند که مسی را مقدس می‌دانند و به آیین «مِسیسم» اعتقاد دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24051" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚽️
از دخترانی که اطراف ورزشگاه‌ های جام‌ جهانی هستن سوال میکنن که جذابترین فوتبالیست کیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24050" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ_92GMNtTszkPTGOxqwHb2CvW93GOkmo3nJ96srsi05nThwggeGkcSmAsXeGD15fjOEEDblfuo14iRWQ2nrrnURi7XrqvScrS9RwBDscLuqc_aCCCv3GLFlHCYnLhOHgCLcAyjt_fTBWW705_mY0KHzvHnt2AgmsEd-OpHoj_jSnBJmWIdg8HPkaD8RHsjZyRuO6-chBUSqMKqjarfegLi7HeFA30X_VJgk-Dzc-h_8zGLTvEIow9ovVXWmbybrmbXJe8wWUgRY7oC6ZdS_xLKSaBNeyc8vtEt7MvLaBuF19P4ycUFKoytIgGIdr_du19KpCi-QqNwciK_iwDurKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ علی تاجرنیا رئیس هیات مدیره استقلال ظهرامروز با محمدمحبی و ایجنتش جلسه آنلاین یک ساعته‌‌ای داشته و پیشنهاد مالی بالایی رو برای 3 فصل حضور درباشگاه استقلال به ستاره تیم ملی داده است. محبی ضمن تشکر از پیشنهاد آبی‌ها اعلام کرده اگه با تیم خوبی در…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24048" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCQF2zHqSBH68aBmdjcNJxGcif9ABsdTkTzojEWSNlufgoq06OOuiZbkPZh2WqSTlrydxsZTZXFIRe7vSoh9BpP4UIAE9VwNSkN5AXKSldU50K0jg0d58wN-1M7ZwgQzNPdZ-LusMGgw7jrUYFxtzi0u1_t8QlU2uIP-DSUh__dqZ1eGtcpHT3s9AVRf3Ea1SKC4ubv3NM28gK6MtLvlS99CSN4LK4nV6zO6hfg4mxBukCrgJ0joasjN0_Rfdt2uw_P6dTP65-VR18Xqk-wJOJQU_5e9mWU5bqrM3oYIdRFtngwWwNsqAJUXcm9yv_3h6qf0ObkCEGT2Ns3KDdjpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تعریف و تجمید بوفون از علی رضا بیرانوند:
قبل‌از این بازی هیچ‌شناختی ازش ندارم اما عملکرد درخشانش در بازی شب گذشته باعث شد که راجب او تحقیق کنم. انتظارداشتم او دریکی‌از باشگاه های اروپایی بازی میکرد. دیشب فوق العاده کار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24047" target="_blank">📅 12:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH2bf8mwWqce3Ld8uyTxtDE6o4DRSPLsxnAlyh7asXNnaety5v3zoTx7mkVdOLGvMhrNtNJI4MPPhpSvkMeu_qugRIcUuEcdMWhvB9yyIZg15izd07HNuMGWYztvhCW8U0MLK2u7ThjSNN9Dd7zN_g5xzkMMrfMPlm1_fUIwoFTyvQ8jTXUgTTkV32EI6r_G2Yb1hCoW8DPdyk9yffHYLYxtEtUDgFrnSjjjc4lLeATPL9vz-ay3aldR7MMHHTKxNlhcg5al62codUVyMxAkXuO8-aSOMMcLltO446_eib7wFA8Y69EGP_cUtgwQCAnYAQuxlJqJteBtgWMlpcfMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24046" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYgUBGISZRZJSveGdnwVNRYgUwronU6Qxj8J7_chjiMRRHmQ9d9GEZYQaBQfHbJvLXh4MsXDmbzw1w7dXx8TC9ofZrfZVMH8TUCsWZOvC0QV1jI15gPYOrcfE0VqlPEreeQG_m0x0Dz86nuZVmR5dfuGWOb3lebQ_IOIKGjHNGBY6TwdgxaBNBV3CiJ-SCnvDfI6rapYyxvtKICw1H_U5d5gGCQfgAkfTIiOKmDpPpmb6Hi_qFardV5ewEllVlUp7r1vkMSLGozkDhBN4mdQ2IZ2hiGLPgSZuTWHNNg3Dfvulg5WNn7hAcAzC-fPVllE6fUfZBFR_VHVTNhydwQciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه پرسپولیس طی ساعات آینده مبلغ توافق شده رو به حساب‌باشگاه‌روبین‌کازان پرداخت خواهد کرد و سپس پوستر کسری طاهری رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24045" target="_blank">📅 11:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2k8tzKUIv0Oi7mP0KWLUqYOsJxqJ4FjWyo7zgjip6t9VVQEefurPSrzgSC__W2SqRWZe5pGc1mgBUXNt4OycXQjPAhgimOXVc6uqslqt_NcsYswzFlBtMCfCW6xF_hML9-ArIb9do-x6ul9Mpcm2NQngFSQOf89mPNqqkXp9qf5qkQVkNpBexSlX2mA3ORktN5-wQK4EtEMywdeBvmuo0lYeHMaFS2ArLX0qtKXiOHq53H6O2ShP8XyFYE2O2gq7e4YqlcM5-vgo7WPbMYSEHC2Ro1oQaVS3noup_avivCLFO_cJoXx-eUNxGroKSBD-QNogrfMdT6l0_K1eH4p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAQ0agxq1R1Omgu7oulRk9a7v7TK9BRXwdD0QpD_jwFTpAVrVr_JouYdr1ciUgbjZMs6Do8YNJpBF-RefXMNeQDKJYOoIeI5HroVp-wAGDq-l1mhWcfTcFS2XRntUxls93LchbL2-zqWviFlmToJxszAgURS4oW-2rbEG1ZXF4ZBbNnWn1mc5HdKx182TPTpt_cb-i1LanFPZxdg2zoH0P4_m14T5q_NwyX6Dn30wiR14HDG9FDiAAh_76aH9s5clYWUOOt3VrJZTeMa3aacgTJ_T-JXJE3eKsq0xi3fYZ9OTB0g6fvFg0hltk6YTo1bBqcOMhIW0CDVgZLENzfyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecassC18p6KPjWE5XBLKYbuimtFVFirDeuQM8w1uMHXwndNkPZkeaUQWm9dBukJeLcahi8s0QHVGaHj4AD6a-W2ADGAL_jQ5RWqeslJHtV37RZ2_1Jtz6tYLicm5ruNHXcntQ9RehEsq2D6lSs6BJRMLBEocGc6I3l8L2XFF_wc48ZGgSDgFYhqcOG06hq_TIZTqjjZYbr7OujmQZbqIs46oiSBeuyT68kMiYL6smiIrck6rve3OLlGb0F_Ko1szfsJc98fosnrGKI9lF2OQLWNUbeDwBdUq1ghWMCqt2l-YWEdNUvX9JUOA1NywX3NeMKiXx7wPsddr5uhg-mzTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2KeXGiAB8bbcn_mup4JfpPlEv4FITGgeWFdK1W7lNhlka2DzVHbjVAu6ki1pV4IIW9-mI0PZ20pCxLQuthbB4psaYWlwUPzXiuwZ8_2MDNSyRUZhWBlZT2EFNTDNjkzuZwOvcrkfI-wlbFGPb4w0AijubblbEFbXrIXMJnit3u02ZE8giBB28Nyc0dN-IZgEuWiOunAw7kJx43oWHI4qGylJnuqk03-6-aDfJBwvVI_vv0RY07d8gC6Xio4IMNcS53pNAldU1FKL6nUaAbyrDM8dxhre24phwr32yzciy20NvpG1NVta4VDxbHCQrdrlKOZc6QSs6BR1qoZWzHGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=ipehZH7CQwLcwt-3r3mmBWjRAwnYyc2cTAbYx-wUUBufrTQ7qADarnBKqqggYhItlWFx9dwx6V5VceEdUKsJJ0p9MKeanFsLCZS3g8pwXAmrjYcwn_EsW_tHUeIa0IBvS4lA5Ffkn0hcQhuURaFosfojAYZp9gnVhcGezy25MWUj-6xDMBEYqeGYZhd-JlKt7AYX4LSD5X5vBSHPdtap2O_oHR2ynr5WZIu9htoyTI5Y2YjR02JHOBQ5zCbk2gLk48--jKjIq40mypMAV4pcXfoIUA_y1XvRbYtyVT_i71o0mVnPRbcU9_KIaq1SMh5F9FHNwAnL7evwHY30tT9eUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=ipehZH7CQwLcwt-3r3mmBWjRAwnYyc2cTAbYx-wUUBufrTQ7qADarnBKqqggYhItlWFx9dwx6V5VceEdUKsJJ0p9MKeanFsLCZS3g8pwXAmrjYcwn_EsW_tHUeIa0IBvS4lA5Ffkn0hcQhuURaFosfojAYZp9gnVhcGezy25MWUj-6xDMBEYqeGYZhd-JlKt7AYX4LSD5X5vBSHPdtap2O_oHR2ynr5WZIu9htoyTI5Y2YjR02JHOBQ5zCbk2gLk48--jKjIq40mypMAV4pcXfoIUA_y1XvRbYtyVT_i71o0mVnPRbcU9_KIaq1SMh5F9FHNwAnL7evwHY30tT9eUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQylt6y5NaYc-88c_JIIrxxh8LqLOVmxHGM-sszecaDIuCk-dt7qUx1K0-MGMWh5BajK-oe0l_gW6EeJLPjzVKHvWNv34Gz7u7pNKu1j9bcD-QH27fsuIHUMByfddPrhNbUPmQZBtt_lJwUTeu3QXaUhku6FQik3dcMZxrlZn9IsbRkDffIqQm01NKTPTk4Nu4fcxS1k0y4y9k2z-IO7loxwyZsKBZi9xHh_kdO66m6R1pH4g90DBYC4ULGjzN0y9aspN5PxCHJ3Befui8Ly3ANvDfJ77r-iBNa-7so-AhIqCZmGtPz_vXK8kFjelg5QtDPdb7L06vp0xugcI0OVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6ibQF5VEva-ClAGtjMYYsw7-bZIDO7ZYs8g1B_kA65kkRwLjXRoYEhye7FxR4FRlk-0wRalLZ1cyyl_IFYg8DYCszZPbbidRjEKd_sflA_NNoR_5C2IsesTNul6XMhioR8FWPXOP7jOSdY_saud45fO0FZ5Y0mu_NgEGxTboxW7j6pmxhUp-55v5RGyWVwnKTWAFsrDPp-3x9wtJ9dFllIHGERo3-RF0GrxcsmZ3DbmwaN6D77nu-32qSssBQjCHR9LoRfkH9SLn0aJ_terUFJSrY2E_hwiCoAGIol9Q1RKDPDTKK9h1GnhTQIQzStWmXeXULH4cnvSKJPB2RUokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=i1pN40lZlUJF8HwJQ4jG1U_EZSZ62IZUBhDp8inzb5GgvidyZbW9m1SqarJ5mGYyr_kuDiwXm2s0XRLrWP1hpkBBo_l5t57ne0VkOVE0wQBDu9y5LuhaUz-ufE3VHxZ4mK782xZSgMpVQGXFAKlGoG1fVko8fswEaW-TlhnZzXC22cDVEsvIvewXwWKW2GFNJnYqrGIv0f3l4tCBaAzfuhv_jnssC2iWspWqlyV-fxaEPUBiip7BYFtV5wUzbzfpKTIGlj19MBj1bPf8P8mht5GBMdcAFp5e5lJxYFKtzyEuHiKYRqgzktImmaHg9rQE5k1yOS8ujuhpO10zY3zpbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=i1pN40lZlUJF8HwJQ4jG1U_EZSZ62IZUBhDp8inzb5GgvidyZbW9m1SqarJ5mGYyr_kuDiwXm2s0XRLrWP1hpkBBo_l5t57ne0VkOVE0wQBDu9y5LuhaUz-ufE3VHxZ4mK782xZSgMpVQGXFAKlGoG1fVko8fswEaW-TlhnZzXC22cDVEsvIvewXwWKW2GFNJnYqrGIv0f3l4tCBaAzfuhv_jnssC2iWspWqlyV-fxaEPUBiip7BYFtV5wUzbzfpKTIGlj19MBj1bPf8P8mht5GBMdcAFp5e5lJxYFKtzyEuHiKYRqgzktImmaHg9rQE5k1yOS8ujuhpO10zY3zpbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSGnOYE7wSRGjoX1_4_2t40YOH37-rynl9H4YfcY-0EsRXmuawyrmQRu6cLXLlJ3dGLVeCsftbTDij83BGq-oz90LZalrxDnzPOVg8o8Fhi4GTbFqZPlOXIFQcXjIcYok10B-36Q59rO3Cr5pDLXSBgIWqxZ0j2SjHW94_oV0xGJ0DgRtyZRTMrlL7LHmN3D1iJYhgJHykT5cX2do2k4eVCWljHdMx8qame0eZiJBlrVjJ10dc00UcXSqFmkZpPNwBxAPLrEaNWXkDw_eihqU5tCp33GHXPNnI8V3IDTsPsmT5sJEB1ALg_Io7cV9kiJb5UJdneuqugYd6wBtgCAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HsUigjNk9TnTe3okeVi2yg59PtEoBpjT5pR6qZVE_tybJgSBeOlF6BGeta2YC_YxsHLppvLooI9jhEy5w9cJh1Mk_18DlWTXwLRpXwZUY7oWVU8bu7412wWGrMprAU9Qdzhf_lblE53-8ipdEQX60zpWSz9BMH703gVzldin40Mgih82CLe-s_OYfxetelRLe8GYOxXTgUeVkdw8QBwCW5-q4EOv_5_n3kcxKITXvIbhFqIZ49N7nXc01noqQW8NeLKb65xh3QdB-P7Cu_mDu8Cri96apZXIamtpTt76fLk3PUodRSboLJ8kIGrgKOx6u7Fu4B7edDAV3q9W8Q2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از برتری ژاپن و اسپانیا تا توقف بدون‌گل بلژیکی‌ها در جدال با یاران قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24033" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=hhWatSmWvtsEMsApUjZjs1sZ2SIfmu-d4qe7941ppG7hea8ZN79ykrJ0HY1WRzpjrRqAAUmDhyhDMEJ-bivCSLK996JuQMqi4Ql2AHFICrsAaSxv_vdIAzKsCRGT9ZefKj42uUHCwv3BvSonZS8rVih1iidTjTJ8UzFwOd7dwZ0V7mK23WzZr5j1MHIDjSKr4o20F_yXk4qm8gdudjZwvGsxPQdyxYmeOc1A8ffDOxdK9N-JlPKTZvoa8ac4XEtIeNtU8HB2KkT3mojOfBCg01AWJLX7q9yOvFnFFyA7_xH3SBRzHrmSamLLFqM9t5e-Q6j2LN-vYf6_HgM17M-H_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=hhWatSmWvtsEMsApUjZjs1sZ2SIfmu-d4qe7941ppG7hea8ZN79ykrJ0HY1WRzpjrRqAAUmDhyhDMEJ-bivCSLK996JuQMqi4Ql2AHFICrsAaSxv_vdIAzKsCRGT9ZefKj42uUHCwv3BvSonZS8rVih1iidTjTJ8UzFwOd7dwZ0V7mK23WzZr5j1MHIDjSKr4o20F_yXk4qm8gdudjZwvGsxPQdyxYmeOc1A8ffDOxdK9N-JlPKTZvoa8ac4XEtIeNtU8HB2KkT3mojOfBCg01AWJLX7q9yOvFnFFyA7_xH3SBRzHrmSamLLFqM9t5e-Q6j2LN-vYf6_HgM17M-H_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms1a74pSQt1q10fVZav9AGUq7VJVwlKr8a50RFNAGFqnP0yL38el_GyHA6GnkriTLS-n7RS9-PXwjRtCK_VYHFNL8M0W-IwD4KSgLDxjwCeNHCUcBnSkMBHZ6RvnS2ueG5bRaSx8BZy01MCY2Rs544wlmG9DYAmWsVFvAYvEXqSpS5I7W3bBO9jw3J7qGY7tuR4YxKjcVy75_WImDGNeT-OsgBzUTdWG6GcTYfZTonbBiwiYuUiY2MD5n5mdrTUuNH0DiuNU5xvHuJVmM-34TecfSVtzI5hjDTuCz-pHr-dS2Ob_N8_KPPcmdlvT8pjyPGR9f2o9uRQTSizzIX_aAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI4nbtVAFOtBe9bMP48UGVoMC7gYdo8PBPHHm0kVeMcwmgN8weESeMZj-GBWKiMIiB3rn3YJUoxU-StT_j7Sc8RsN60ktq1AZih7paSeS4dbwcM5ECz-tQQIdH4_SHoyJeR-mgHuYEi6ZaCBU4Kf_cEm29GpaJ64yvdNhSNZgXxXYQtzagMLEe9dyVwcOfZiY3TvezDnf3bNM2p-Ar4ZibwgS4Jnhq9PEifGaTsPI9Ol97kbd5rKUWYV3ULG5O0bzBeWmEz-vbmmtrFDVbZxNOTweTQ5PBlhXqFzEKarldogGfDBP0h01reeVgAO6COBD-74N7kr-np8hgrQmZdu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTPEZFXTcBqhsbsHIS5fnFTatEb_C0vmZnwCGEz3G_mAQM2wlzgFvrn0zr0Unz7JS3I8WA8Xdl68inMy4loKS90u6igkhsXD-D-wrpiQzMvXtMBFZO-Nmi0KMNoh03pFhfdWNbtpsCRVJyeWR3aHED88oMk1dzTq_yeMzbQEK1LFj5iCSFetwmXtyCTVKw5V95ynmw-9iQZz2WEY_W5xMYx04c0sqanw5SY6uU3xp-1TNAOhKzQpUA1mlVDjfCxrEUf-M-aj54lXSpm6c-Xlh7Z_TuYkWzavNaW7u_Lwkh5zOiZZ0v_jUtMI4Fxs0Mp9iLP4-rUZwWWS09RiIJPCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=jMlMAO5GjnuZwdb2Le-vmwHWTggNuTQrIhcEfAYAXczpn-gR8cv4zmslmKHDbR792h-_uFcQQyYPEx95MnYuPgcP9KMNEosKKpAogG6y7FidpxyTGY4ZOPvtO1FUU3a-B3E6aBBD_ChXvF9TjpcDHyakLHWhNR5KUCjXYVlj9CvHWK2FrfOqtpUSO3QFGIaKFiTtePDZcOc1Ap8nvtVDRPUyJKJD9w841RkrxUvGELb0Rl2uj7Qx0XSM5unG9-xk3MPZB0mdfdq02Mh7CZwivJzKc__ZUMQCzs0fi2IMsOSkRkIKnHGxP6qb1ynCH_qqVHTWmjElkynWmbaLh0hVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=jMlMAO5GjnuZwdb2Le-vmwHWTggNuTQrIhcEfAYAXczpn-gR8cv4zmslmKHDbR792h-_uFcQQyYPEx95MnYuPgcP9KMNEosKKpAogG6y7FidpxyTGY4ZOPvtO1FUU3a-B3E6aBBD_ChXvF9TjpcDHyakLHWhNR5KUCjXYVlj9CvHWK2FrfOqtpUSO3QFGIaKFiTtePDZcOc1Ap8nvtVDRPUyJKJD9w841RkrxUvGELb0Rl2uj7Qx0XSM5unG9-xk3MPZB0mdfdq02Mh7CZwivJzKc__ZUMQCzs0fi2IMsOSkRkIKnHGxP6qb1ynCH_qqVHTWmjElkynWmbaLh0hVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=PNRPR-4oQ7LZxFBqUNzVH-cOMo0mhuzrd1bVbodyocHY_Rv2GRolh-pU31WqE5X0P4mEoWwPeQHHpIZczvANb-7qC8BEBHenowYz6IYZvXd-DmXW1Go2XTPANx0NwgVVHwEg0NntfLWfCKlS9LycdmC3LIVKTx_q4Pi6ikpcMp5Q8HzSYvHzTWlj88yZrXUDFfG-6nRY6rsNADZOMbRg15V8uLVLfHlJ589Y48jI9P3lJF1LIkRveDuUc5NWJjBVFhoTnlX8eguLr3BIgEnhlz25I6BhcFwOkFxFz_GqjHbqC_2e_vkhi5AYuw54oGfh507oNxFJpsBaPLA3F4QYnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=PNRPR-4oQ7LZxFBqUNzVH-cOMo0mhuzrd1bVbodyocHY_Rv2GRolh-pU31WqE5X0P4mEoWwPeQHHpIZczvANb-7qC8BEBHenowYz6IYZvXd-DmXW1Go2XTPANx0NwgVVHwEg0NntfLWfCKlS9LycdmC3LIVKTx_q4Pi6ikpcMp5Q8HzSYvHzTWlj88yZrXUDFfG-6nRY6rsNADZOMbRg15V8uLVLfHlJ589Y48jI9P3lJF1LIkRveDuUc5NWJjBVFhoTnlX8eguLr3BIgEnhlz25I6BhcFwOkFxFz_GqjHbqC_2e_vkhi5AYuw54oGfh507oNxFJpsBaPLA3F4QYnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6RUutCAJcSH6l8-MZ7sFPaWqBmlG0sbXaj8hYSCaWAiJtJPw3acCL0rVDZbPxE9aTWL_nQ-bzwuicPSdJxnH8ZmhDl5Np6gW2t6Yl-ACi-EyihVLcP53882YS1f3LbopJBmESR4eqn7WCjLp6vn2c6-Vd2QbHrMsn2WogMYxY-6O9hut0p90l7cqNMFai-vdJ8Xp1uAog75uk8LzbtRo5BrR7WwvFOBr4msosUItPNXKx8klJWu8bNJD7L2w3v8_BKEN258r6K_6W27gF5XTe06EB6H-yMxfVizpBtAKecJLCYcyH7IYzYkj3M9Ur1GLGLK7G-5VwYIEm6Pn7l3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tl8l19-QL4HUx3nXtmobOxXPHoQA3Rqgo_8hHndDGKGExo7YzZT-C6PyN08KhjbDUYdfHJc7fcHH5aT0-SJdEp-aHERMWlIcc79VczmKUXDHgRyR8l2Hr7CRaI5VpDHY2Ffulx6B1nj0H7tG4uHfApQ5vBSzfTSrkzdP9XrdULnVlJmlA-OZlh0nRasc1upCCEMVf_lw4uBrIcUYgDdyGj0qrwTahwes_ub1MZspwT4YtC05cGNY3lc_SewnM1XYebJZHeIgXFtkfEUlHXDdhVDrbSd2msg0mPhdaRaOiigeZ6EUG03tu887BHcWhFV-IAXPILaNgQa0u_tk1OsLKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
