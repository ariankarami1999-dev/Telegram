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
<img src="https://cdn4.telesco.pe/file/h8btISsDn1lLBnJInvFEzvG-MizRLxLn-DJYNzR6lCIq1SJ_Gogt9hoksvToT_jpF10XBgH6ZcekQph0q0T6hq5bHDDC_PupLi2N8DlxkBd5gIkBdPgARpBejZJVTFlSgUcib0MEnvPfCNfs1H_qOgKtoxcIckseYIJ6n_H6X8bMLBe-WWeVmbFH9v-8qqmxnOAphMKBMUKvO10JA8x2k9GwJ4u5TYQV8NEe-QiWKY8tK77yusrURvSeh7e-ASoCaIENI4CcP01f9s5NB_A3MpyBwsfyfRcMh3WvuWaCUyb_hxSmpWomh6JqEmlHTVAmTtpLAXvK8GqNPLTRDBvmgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1PGFvjB7zxQTukSX7YYs98tO30Zjruvpk8nAodE3IRD8GU2TWe9KYMCm9viSTRIX8HIXfO_9cUu-bjbbCg9Z_CE3qAyqsIM6y55QZ5AUmsv2sqmUIUiYJZ_6N61LyBbr8-pOyhU6b1IKHuh1mIdPaZenPLO_gFGmGSLbaToZwCDoE53Jrnw-Wrmn7k5lGIKqwlDErwkhiAoW9TmbR3Q8TBM1Bgx7zWUYG0v8cDHlCmzrhRfl8UMJfHsKzTBRdOdNwroYrfTnq-YzEqrOULJzxPCpQOOjGObFImqUBHcKfLK3txyrunkwd3bvcZGj7AFes3USplbWQHi8jitSdGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MciWV93_Xyh9TVnzp3b5UFC5FpjtGSzfmuzE_RrQ2558dQ3zKY9_d795hvO_hDMe2Ysdvkqb1QToT9fJ1_xllOu0cr2LDEm9lEdkuy1iK1c0J9MQoZt4oabccmLc321ZXc5FziK9jl_nqFaR2g3PxKMJ6nc2WWVGCM0XVfKH5Lv_bShIDsFz7czU0trqnpFbA3Z72FFh3dQKpKZzsPxiTUSFbncqd74R5FqDeFAx1XM4--Mgg-Y7TLBZHBlmF1-2fB9mizsoRpUqBbwpUHXCkUuHtumMjblpoEmO92BgO5orzwuV6URbY4UFAncD-iQ1kk3YwgMKKx3bnpC34_SM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9XSkhRRRUUhda3yunVtVHrjBK2jeeGTz2lwu9XOEHcpu98qL6WASCEyI5u_XBUWEFx4bZ8tPrWjOpDp4Q2lJfe7KL3zpg__cgpfeJEfSiMJDZD766B8DkEruWao2I50D45QfBOqqDOvVNZzax3v-gS9Nmz9O4iE2WgLL8j5ZSybHI8VdySprF-osUJ8rHjVJg6u1DfdhMmg_8rcaTBnY1464h_AzqWGhLkCuU7XR7YECLIfJM8ZZbtYsLi408bqvEBttcO64zc-mJBQeBuGlj52MQgffFVzDEp67EbiT_hmkB-c31rCHMoPFc0jBSbnbaJXu1eCFyumExD2O1Ef-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvi9H6iEEPgl14X2kKtd_8EKcQGKkdCx9niQf2Vl-xCWCFNolhr0BkB088n5mfAGvZgdeXHuOBt10u9hGWDCyqYH_v63_f8QRRoGYeW2AnHtLtKLOymIimcBmzeKE-L4Flo0hXPRcnfKb1bBCgbsCnYv7dZOcnsXnnGARJkRzBHaz3EyT8qka-BJkq2te9zPuxHbY8xojpsTOr69RlnCpFkSQhe82G7oySiezqO_NkbVXIjKUAQlpz3vFiBmOX7r3vT0_VqCnkTE9NzdBPyZiP368W3qI1_oGfoklcar-ySD_u1ChxS9bhdBpTln0pnZOVxtRrpYXktBEnoVBo8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0PAFHpnngm7NME1YMMOI59LHVFpPFX9tGJXs6FTwyToil0xXyeKMplUwjTFTRaQpMYOslI5lgpI68cRhK88JNhlEje6piV3QvJ689cheKoi7v6uR7nFVPgZaSjfK6KOzj3Doj0P7wolK-lkRwzIe4A-RBcKsBX8n9EEq0Zvobgfo_SEr1814lzTkiZ106c-VcsMsvntiZMcg7coqCStbUcpRS2niWv2qFv3PkSFX5pB915M458COjX1HyAo0rZpYW90h9gS10Ua8hNK4YTAfhY8dbAKne3_m_08c2UbfQfPdo87GvDzhwp4xhruLxr_SNSPuA3fCbEnEX4bXYCPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCvasBVOObox-2No1ETeNiQfz7tWEe3fhGhs999oqJj2dZwDzEz1nN9xOLCg4Xb4wWtARaWMn1ax1fDZxPAwUalfUce92fvJKUnQtlMYPtqaDoEjZgc_lviqgFOD8oMlUg--BYIrV6FqFEcA397NJNDGEPezdJZ13_J1QwGDQYHQ3ssSjZE3ar4bZW3GngWvDyUiYl5DHlcMmpv4PE8m_HCfqWNGvlWlnWF-dJxgUzY7K8nCUdaFQxRqgwOV773eACDJk74PFfB4NesxnFdaLQsycpF8fqWaF6Z-XPckh_dOzLZjuSXk0pxEAaPlT2EX4JG9Pg1umM895RIvl86uwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4MKvVeYTgOxkhAjMSJTyrFTn55WqRmOKN6f8YVVSQ_YMWDVGpj_kzwr1gNoRkUKKL9meK3kSjYWWnQpbH5Tj_LhOE7mWMegP7Wr03ROc805I-QnbQGK8C_xoRZHUc2RVfmz3lfBWpH9LXX_juXodSx1G_hiMGlgn2JyBaUBDK1j6Wrd5H9EccDVnCUR0qZTpMV53XjoX8_bYaamBRDHisOoeqHWX_kPjxbomwDhQF5zl0Sy66yfRhLAJLfTpE9gFhUWxCggAZsq2A4v-XiW9QjmOIkDjPGOPYWwky4Hds2huZJfiM3isGMFB4KHHoym0R6L8MjkqgyOwwM5AJNOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23842">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA-al9cdXpdY2-Wh6wRZkglt9Vjq4DXW48IVgU5GV98XPe-aqLi-OTbSy3uscXVha0WtFYdF9X70mki0Yaq0v_cSjZXvGhUixAZJ0j40DLPPgfy0oa7U3KFKwsalmr5dZVVjv7ZNtmfg7PBkJPJ9USZzZoYU4JDcN150nsn32xjyrx1UShOG_yHYmZ9RkBSRm0KNRG0_peuGKxmlzomdlgHDPVTjuGS7N6wm0NzroPhfB-coNvKpw_WafFPgV9zJG2e0VTmXKVl2LEny_KUKQ2jurZCM8APprTXSnCd4_eMcnOk1uVmVZUngpMy4oz8BSm9hMefK3GuFvm1GyULbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
#امریکا
Vs
#استرالیا
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
29
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23842" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPnQojm9_6fWOP_GwAHzzIX7ia1sCoy2He6MX-Q77x9EZH02fMWSJhDJFp6jgL7LOKgAKFSNDofb9d9ImgW1_b9cKPRI9r5jSi8G1j4EAoSRxv24nz_eE1Rpyb92uSPM98UXAxt99nteSYv6mu3mmw_1Heo8MbHo7ttqtwL1segDAO4cOULQdmjdG5UrcYtfA-pG_2-9jin7WtjT9rNOxHsPIDPfd8j3lsU_VmU2EqUFxTtLt_sbpfYt2BKkPXFbdMk6YZ4Ijjwcl-RusX1YfcJBOZSWUPwvsk4HXBcVDfvNalsktZ_u8-VH2dCwA1ftkwjWK8YaafmqfNgYYLhz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJsti36wZgr_7DXLPKN9lgrz7vWC7OvMSxdpgFNrB1q_AGtlBL9BxzRbVaMihjyBuZsDSxbewfonNWdWA_HlhISt7i2Zg5eJqgNgGMhH-7tl_MTuJyvKDa-L5Uwyt5S6eHKXtBiQrdc3FuciDTcsNiA3yX0KLz0QI046LlG9akrG-uqnzGRTYS_cYlVGiQPh87xVPlFGkrpSMzhiRDAD1b-sEsr2TnDr1bFss-GKLHXk8JeM2NkUrCq8dn0eNNPx6E9FCaoGMmOPd5DN6uNipualHGb9NL__yct4SH4JmlPIYf48KCo1CaGtMF0iVCp1bUnq300BzsQ8OhOM2Rs2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfk0MOivTRbLCHvXVHV8BBTBjL6lGBDlvp1uC0_je-c5kh6vQ5ZD6PvjvUWpxrEUvyhTro7j-gJ3aJgcrtZ-9W0IZ1JPjCrp775l21maosoUlOpJSRuxhX49PNNrK2ZEFjhjZnARm-7KT1n3Ge-DM3bgZEHkxOZvi0EFFrF-ewgzI_Sz1SK6MGqLWfush4oySh79u4cCkySZ8_ESVlrLz7L9VjeoAE7uVAsuQWrFxUMojYeZ7Fg7-_VgXTvYal-fBEhIxRiiYrHbD1gue-W_Lwr2MNvSU8IrdrzUG1Orf5WG9xy44HWJvacAgvDLDeeBhPBETdSs8vjqFeN_OycDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=XgDiov-Vwrv-q14k3FYDDLaA3Nq3VUAf5TDQMCIWNT1yT_LVkevFIX-hHXVEUOqJgH7rYJf8nT9AXBYngJNhATfi2BeCaNUBmDniyOGT3kWgtPe2CdeFLMdYwwvu20XOXc9tvwPFE4XLgqHFeJLOgxqJx_Nvq514i2PKEZboeJWkZd1-0UqC7KApe4OwjXUD1HAo7Mulga-tZ7uY8xx2HBzm55YtxA_4XQ4u4HIPwBmpezTH9QzFQOHgWJrGCRUdN81W7WwZdb8beNxhyqSVSk28k1CiCyMmMDDIuFqe4tKVnFHTJm9xFqzY0f3nthJk81l7g20pm5b1j7nYorLGmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=XgDiov-Vwrv-q14k3FYDDLaA3Nq3VUAf5TDQMCIWNT1yT_LVkevFIX-hHXVEUOqJgH7rYJf8nT9AXBYngJNhATfi2BeCaNUBmDniyOGT3kWgtPe2CdeFLMdYwwvu20XOXc9tvwPFE4XLgqHFeJLOgxqJx_Nvq514i2PKEZboeJWkZd1-0UqC7KApe4OwjXUD1HAo7Mulga-tZ7uY8xx2HBzm55YtxA_4XQ4u4HIPwBmpezTH9QzFQOHgWJrGCRUdN81W7WwZdb8beNxhyqSVSk28k1CiCyMmMDDIuFqe4tKVnFHTJm9xFqzY0f3nthJk81l7g20pm5b1j7nYorLGmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF_d9S_bp0M8q5le6Hj9saXiEz3x9g5LwTWasd60ie_ZC4JcvPtGqK-8K__jMcPYGywos_KubooFvj5iRnIZAS2ynpHzAhJW052a9FBfzUoXtwDygOming0GwYoJe-PrZ4UiOR_9QP040PJzJX1VJa6IjoUSGccoJw1va4I2XlV6EtTJEdX5AIl2_1LThTYfnwXDK2QWG2KDCrduhouwlSYRaFdC8dTMqc38mW17_chISth1X9hJavJ1je2Sjw_WhDelnEBZdLnhCJmw43Tg7_gD-aAjwh7bJykp89DWSLhtzwv0uc34yss3nW7RnrD6PDHHMGcJH7xHQU6WcB68kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmakQ0Ue3LIAgHGstBbK5cQcuC4QkTjVXC3GRtoWTa72sog_3Ypoa3y4BCliY4-ep574qNh8vNSFbp8Rt7scWsBC4eE8AkU7YrWQkrS-NBTYOZ1XuY6rQDa82NtL3xs76THR_KRptp0bRso6xGqJHIRVt9qc6Ne_qN4ey-oAwxOpxN7ugWf2x80ijwDfvjhx_jR2Hc_wUk1xzYBzHKz9tPHSQBm6ZUOz-eJERTZ67NJm28SiOYzeZQ8CDimqoG770AlnuQ8C7WugIuUnTieIrllwXczWo_bH3f6RGSWkSk5lBmROnUdm7g0K5twYj5h7orGF8i7b4B2NcO1ZO-Gbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLCncAwV4BzYk3P3-lQhQ-dnRhA6QAZuERUBBMsDDkT-i1spW-EX1ekzDy0iwVw9hzro4CUeLRpRN0N54Y8V9gE0XsrNQb8sk7GWVX17ZPwRsWe0LPCuhwwJkEvlSKEnu2jJZxNZ0M-f5xuZd8acNvSeVaDZ9CdedoTK54h13iy06HFp1CRJtJ9UfPOgwYhBBlHkzSpkO9vcdFgeEGQr0Y8uxwsNFEg1y9x85wD7ufw1zObnjlyBNFqX9XKzplO3onwvB175VvDK4d201lw4oQql_gORlsS3OL8MEhnU0xEQHxBjHQMFQZHt7tLMRtbj1QgF3mxSaUAdE5M6OXZHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr-z1fdE6MUOoRzBBOZR9yl5tBlqkyZfH-4BqLec-6FmJLGpOJoA2ftAq7zsipKucbRTGWobkv9MKPGLG3GZzM3dTgim4PtJIIqYIdFLxYTsI0msLknV4WoNjJm31AHR0NuQ0pso4L1IgPemGR8ftmO7dW5PUTik6t0rdhHpmeteGnAOHN1nMz-vcHDFK8zBhz4ICwBTqZQY9DlzoqCMjTJb7TlAs585rg0JHwYwly6V38OZRTk--fx0vXTUfkoJ8wKrY0OJKp4W32VAHBwLIr02kMW5HUYC1IgVv632CFyvwzQCOpj24XERpP-aI1baFrf727qy558f81mFoyKVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgIb9tHTz3QXkvt9au0PAx2xWOA_aljJcJi5c5JSbPIpBVyXvH1JOlalrIzoqeEH-Le3r-dk1jRlVRvRC6j6akCgb2wKEwlKC1fDTEQQQfYcNXoVngqM9lvr35gewWnmf70w1uI0KBYE_Jklo5seN-3RWoiPwhm0p17bXRkGSkaFXSXR40oRPBVXVIm9mKpgrz1yf3RX8kao3xPeXEsY2vKoBQ_9N0M8sVNOyCU5bVNMOXzxZHEgRnd94JFhwxguhZ4jTbzed3RhEQtOWf5IT27KzLipJO2VMM6sC8BDnroLRTkZgmPUlCXLFnk1vvXK-AeHikI6APuLkdTsi_5fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1UBilSSEuLydW1x6Rck-aTmX_tdoPuc9XRGkhrA6LS3sJWxKMTEDg46sQ1Rm23h3LCfmpE-H1rSpQ7L23hblsZxl8XVANWaOCfgLw5KZscFNh6ehJNmxEoOaz7Ohm7b2Vmb4S0GmTnf7WQoc94vnAXHUGVfR9RnD6l7i7GVa9WQM9ILQtgPBLG6nr21T9hSTBTHbCKo7hQZ6A9cigoY715T2myq-GG7K_eWLcs4_dmNZ8ITDPwrt9fEN727IbdZ7YuLPBjejp3rBKQoJ1mvde5OJzUiWvxp8snGyNhe8PyEDJS4Agvgn6UsxOcjBBaqMFZc_edaWMVl4_AvePf_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWTMRwapRdWCPsKK_H4R5S0KNooaTe-u-TQbStoclmPSp0wh4bS4kJUR7wY_kUp2tomIn0GQnW57WSWgalD4SIDdokQDS0HYQACeNUDg2BFD3pRDgmKvjf5Ce8Y6zY8nZ9lHIvRnLQ0tHXLGzb3Zv1QL31pHmwsJhYW19o-sdUGwic9gt4g21NX9cKky9P1C6Q-ABZae7qR_4KBWQbwDAEd-yDzzomw59ic0LjSrwCLszehH1NR632C3bka89SlV_u8YNRKJauHdyjHmWJnVIRAo2OGvn6Pitb5kXDBSkz1Jv5gDaDkptatA3eVLCE75_fxJvJpDBJVrWjRm_mHFgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ2AshRo-MLORle_k6VtYUTDB-UILJi2lIrrhMowwjx8Uk8uX5kbt8aYgpWfD7VssbMuyJEYH-ykS4guifg5FTkQxsyce5jy9oLWL15swTmbNsF2vqezjF9w6sbAqtVjkmT4TKwnPmsCRYNY80EJqvA2kiumwcbkht5tnxNvpIMeoSracYVOwEYuIrtCTKJH9V6xHE6ZXnuPAs-uwVA2XbfSpzS41Wx7XPUY8QqAa5xzqng_MqOyaBmVXho_PaY4bV0EeEBKsCEsAYpGww-bBv4E03PNL0ycAHFEj-N-tROlWTkhNRWEbb4JXGwTYuWg-LlUIzARaPGnOV_XufPPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=QYoU8_5cGYH40Jr-A6wTT_YT50__lkWaO6wUKrvc0PIFVf_BYKwA6RP2gbpTWM-NMWlgjlED5aPkM3IxmQdi07vhDLscAEpumwiiPrW78ahq1nHDIPorluxUqJyhPIgzuUFYZVaq72QR2_N8z2XA0_EJ2Xmdrts2auxP_-BKv8zlp4Kv0-oypIn0p-igrbePV5qVJ0aIXJPlhQGnxkdC7NV_dCWlvz1_p3lAtEQ0xBTZWTUgeAAKownds-wqBVOhDK1NW3Esex0eORd4CetHL572gVQbUxBe9BITSfwW5BzPUMsFgeCHHy4bwlWoWaM93ZnzX2xCKYZueH1g0QLl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=QYoU8_5cGYH40Jr-A6wTT_YT50__lkWaO6wUKrvc0PIFVf_BYKwA6RP2gbpTWM-NMWlgjlED5aPkM3IxmQdi07vhDLscAEpumwiiPrW78ahq1nHDIPorluxUqJyhPIgzuUFYZVaq72QR2_N8z2XA0_EJ2Xmdrts2auxP_-BKv8zlp4Kv0-oypIn0p-igrbePV5qVJ0aIXJPlhQGnxkdC7NV_dCWlvz1_p3lAtEQ0xBTZWTUgeAAKownds-wqBVOhDK1NW3Esex0eORd4CetHL572gVQbUxBe9BITSfwW5BzPUMsFgeCHHy4bwlWoWaM93ZnzX2xCKYZueH1g0QLl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Wr-z_kYjYIWDMOPUzK10SV2shHXkDB-Uc3f_eI5UETZmsI9-N5DZh0abIZWFN52EI5nGUqRO2YyV0qQX_5Iy0AnxjAZvBkI34WdREjNX7fb5JOVPfb8n2qd1jfrykJJKS5hypiV3JiL5RmJbFMOJjNf_9lLirr3tbVlwbopxdyhBd9I0PyRV7a9-jA48FP5JYCYQ69zJgTie33FjD6pdqrqLyT1c2qosJByb53w-w1mtvMtnvPuv5cNinJTT_sdLmW22N9kBu1h5SB0ZmaPKL0LkAzN5o1Iae7Sh9t6fFUQFgN1Uvg4qY5ct22wdz5E3eeW7TtSYnMmMMrROKCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=a9rN6gL8eMXDvnWJBRMgJQBrhnp9smZ8uWsJ1u4ZFgDSMZL_oUsdXwaeom-D02szGhxOZdw3VOuwa7ikxueHnzEz0pPAyliYBzVzAzMBo15ZvoCi1qa2LCTMbFzVDySaTAbw2ZXBiey2L0UJus0zFw7GWURDq_2mmXqMh9lnpe4B9SW4hy_P1SGJLpRAJ5vjTO4ZF18KUQlZi89GrmhR8dioOwgSaf5K_Pb6lnhTimG6F4ULaQwZ2GbPeBAXIFFm2jJ75cSODdTpe-nSQS_jIXDWnr3HmkRAhdvNe5pk4f7XgRuz2xVikoxds38amMPDUyK9IuKz3fwyr5E9m9HiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=a9rN6gL8eMXDvnWJBRMgJQBrhnp9smZ8uWsJ1u4ZFgDSMZL_oUsdXwaeom-D02szGhxOZdw3VOuwa7ikxueHnzEz0pPAyliYBzVzAzMBo15ZvoCi1qa2LCTMbFzVDySaTAbw2ZXBiey2L0UJus0zFw7GWURDq_2mmXqMh9lnpe4B9SW4hy_P1SGJLpRAJ5vjTO4ZF18KUQlZi89GrmhR8dioOwgSaf5K_Pb6lnhTimG6F4ULaQwZ2GbPeBAXIFFm2jJ75cSODdTpe-nSQS_jIXDWnr3HmkRAhdvNe5pk4f7XgRuz2xVikoxds38amMPDUyK9IuKz3fwyr5E9m9HiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTu4Zb6Va0ztmYFh_tvDYAyw_nC3uFFskPNu5OtE0fb8rVV4m-oi4R5dljmTDqx1bl3Dc-H2pCDDeKqbWV175xs9QHWTkqMpA3__olM5xkC1Y2kkd3EcDpw-20pFq-CXhREh_I--gk_NdhjtesY_xAlXXe87tEggH_stCp3JhnaLKjy514rP96Y8A9dex2eqWl77-ILoOWuF7RXPRRzwZHeF5133N3dX770FKyFspGlRg11fDp8_nAj_tLj2XVN_84_SVqUM3Az8WyI6kX_0CiW2ZlklyDcGCU3joTJOTIcGu4URORfGLQpDX2uIlj3K47-CRwCreRT2Dqvqa492wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q11I4z3TQtVprnvbPuT6LHy1i53h5srpdnppq9YS6zRVCkh8LgPFa7YcFYWWuc_xcRY2_N5dExwgeBH5Z9LG7V1IQEbT9AT0DSRkWX-kfpkdRlzjaS_rxHcy0jfWDN2Jum0jGB0MY9L0crXB4xeSt_Pg55LN9d_Oo2ck4eDEc71DSCpF5C0jzxPF_nhB44Zg5RFdUk34lJEAbH-09axm2vSCzRBsz6WRh5ondP9HQdFbl1aI2jKgXAo1rKJ64Bfxo4X1rsUNtUG4yqddN6TnO7E1zF_8DnzXvD-9ovIMHm_4U6226VadHouhCbx95F34X_x4H__zqRtrn250pYbzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=WbYpoEXsTEYrqF1DWt9d9nkhPldM1Um86Evzq_EP7B4ve6kv4aS4k7ndd7_ino-KIV6Rliy_wVk0yM264TBq86ByDOEssX0kti0DJdcJHq0OYZ9CUDQpwr7UonaCRgWeVAoEx0ddh1fLHAGQ08tWqz_0Je4RN7A9LrOduXoR1yy3ks-4rQeQsKZ1ClvCHcbAcM0QTSfV7OEnVvO2T6qEtqM3noDNBS7nutxmN1J7fWWmB806a6rdbM29vZgYdci6mJbYuPFVQ5bCRGm2ZUEohjTXjZiQoHrs9K1GQYOZ2jS1dFCuXudV_fZZ0miDWeaD_YfvgZgsyJYVypvarFsEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=WbYpoEXsTEYrqF1DWt9d9nkhPldM1Um86Evzq_EP7B4ve6kv4aS4k7ndd7_ino-KIV6Rliy_wVk0yM264TBq86ByDOEssX0kti0DJdcJHq0OYZ9CUDQpwr7UonaCRgWeVAoEx0ddh1fLHAGQ08tWqz_0Je4RN7A9LrOduXoR1yy3ks-4rQeQsKZ1ClvCHcbAcM0QTSfV7OEnVvO2T6qEtqM3noDNBS7nutxmN1J7fWWmB806a6rdbM29vZgYdci6mJbYuPFVQ5bCRGm2ZUEohjTXjZiQoHrs9K1GQYOZ2jS1dFCuXudV_fZZ0miDWeaD_YfvgZgsyJYVypvarFsEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=FlJlxj-nwmeKxydcH13aDUDRZRXle6fVK_K5CSGcjC5jdmQI9S22Eqm2mFZ70rCoVdzWGqBpNmOZhJ3q-qFtRDV9MwxBMYUFg0zGcjhIYKEUT0gUjOMMu0QGCi5DYSakZf3TKyKheY3ehxJsf71qHyGya7wFX6BE_6mJ5Xti92XyT69SgYmfsyiWuvVmDLmymt5NLHetwg20Qt_-21D6w8DVi17AyfJBtq0LVuOa-ythiKaO7JxQedBa5kaJBFuy6Tmf0A0rFJHRYyUhFinsqjlBVx-EC5aay3URwJoP2RkaaHBPslF7ojbhL0eT7jtnKzxIZkBocEMFxNe2yJcQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=FlJlxj-nwmeKxydcH13aDUDRZRXle6fVK_K5CSGcjC5jdmQI9S22Eqm2mFZ70rCoVdzWGqBpNmOZhJ3q-qFtRDV9MwxBMYUFg0zGcjhIYKEUT0gUjOMMu0QGCi5DYSakZf3TKyKheY3ehxJsf71qHyGya7wFX6BE_6mJ5Xti92XyT69SgYmfsyiWuvVmDLmymt5NLHetwg20Qt_-21D6w8DVi17AyfJBtq0LVuOa-ythiKaO7JxQedBa5kaJBFuy6Tmf0A0rFJHRYyUhFinsqjlBVx-EC5aay3URwJoP2RkaaHBPslF7ojbhL0eT7jtnKzxIZkBocEMFxNe2yJcQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23818" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrergXwrwcNhcEWp_0LWq99AwEgXFRYCGsZsQeZEdXAf5BUFRQHejuAn9GlUErDcMUdckXx1x7Dm5wQ_tyU2accMlU84XdGy0ATlSWkatoHIaG7LBkfg2qSBPPjlqDmQe1yN5qYVUl5VeW4XAfSUauiuAe7lpEB3iObru9LlwwpHqX7cTnshwSz5Ta5HiD4LZP6yFdoVUYQsiGVFpU6u0cvDoaD-IUCiE7ULpSVJmXktIsSmI-G3KdWhpjmywdyMu_HWlWZ01DubiwQBHh4UbeGX8agidVH5CHvxHTNUdd-SYjdDsDVtmBynJc4OkZwPSBj9E6c-LN8I8jMbF8rQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=srJUr1FTwBwv6LF4AvlOlX1HMqSV73ZcTwHH6K7Tc-wAhr2cYsOsuAIlipuUzWC5-33iZgNmobOjac-uhm_CfP8UGr4UA5VIIWxbj1jlT7KeOWkHJmO11EvgG__5H-jUHoFQM0z47NphS2B9fw6Dcd0TcCnCAb7iw-xkHIZpwVX3hF-GlUiJ9IcP1k1gV6-fOSo5iuLFHgCnUDzv2aapG3pySi2CEiMAlAVM9FTmP1hDQp7H0mZ91jQdI0jztPM8BAfgAMYw4HzCJXTsXIIKLj6_qerSSMv2EPFAEh_0b3hw64KL5oj_mKP7wphIK23od8AdOI3AgkDx-BFFZenYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=srJUr1FTwBwv6LF4AvlOlX1HMqSV73ZcTwHH6K7Tc-wAhr2cYsOsuAIlipuUzWC5-33iZgNmobOjac-uhm_CfP8UGr4UA5VIIWxbj1jlT7KeOWkHJmO11EvgG__5H-jUHoFQM0z47NphS2B9fw6Dcd0TcCnCAb7iw-xkHIZpwVX3hF-GlUiJ9IcP1k1gV6-fOSo5iuLFHgCnUDzv2aapG3pySi2CEiMAlAVM9FTmP1hDQp7H0mZ91jQdI0jztPM8BAfgAMYw4HzCJXTsXIIKLj6_qerSSMv2EPFAEh_0b3hw64KL5oj_mKP7wphIK23od8AdOI3AgkDx-BFFZenYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=HrYJGVgRXo3_FJFLOT273JNq5TGwS_BhWcBPlBoYdBAGT81e2vIXVDt2NbOo2OKpIWs7va1JP0UUllYOhOaNIhC4dNRFKUMC1XgZG4bzKTXLsOqObe6hj48F0ALKdjUVRyfkgrJwdznJdoE9ii7ok3N9WK0iOhyXzAKMkHFZH7y3LbnLeVfWzbxAA7wfVVtdq3ggDrvH0EFEgPdocUNkP5GohA4PGx1xL_n1XGnT2YNZRlenWtQEPIIpYiq2Jfu9Us8up5a5Kx2lVZqRKW9roE2_L4NUHOPSEsSFtxED5wDZYqMsArzpvB_LNz9UkTw8vdGNVZMg3Lj6g7dqPr9NaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=HrYJGVgRXo3_FJFLOT273JNq5TGwS_BhWcBPlBoYdBAGT81e2vIXVDt2NbOo2OKpIWs7va1JP0UUllYOhOaNIhC4dNRFKUMC1XgZG4bzKTXLsOqObe6hj48F0ALKdjUVRyfkgrJwdznJdoE9ii7ok3N9WK0iOhyXzAKMkHFZH7y3LbnLeVfWzbxAA7wfVVtdq3ggDrvH0EFEgPdocUNkP5GohA4PGx1xL_n1XGnT2YNZRlenWtQEPIIpYiq2Jfu9Us8up5a5Kx2lVZqRKW9roE2_L4NUHOPSEsSFtxED5wDZYqMsArzpvB_LNz9UkTw8vdGNVZMg3Lj6g7dqPr9NaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTIzqSORO49JvEHCuo3jLYq5B_cADwAp9a0tcDmC8NbZ4RSCaerjDH3JNd56Usp7ZAUiOq9a54FnuxvERq--PO-wxwZ1cYjW8_vSWgcoAH4go87IKqDJyy3DFaDCxq3WyFqIMnLkdfdCFgxxk658bhwCp-CG5XUs0zp5uwp-hP4yk_YG2Ho1EXyl9UI78-G7lz4kZ5uD9jXFd72zlsFwVwAK8EJ0RzLPbzEOztMn2e5bqMmoDkmDqBqG8ot7NjF-GNQPWVAKchtGB8QNZgMnugAOPbRsmyCYeK2ySbQ9ucfAqJUjKOgjqlogkdE6aS1-L5HFzrnseUWfs4-lHlESOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5uNHsS0WwJJw0om5xGfE_7oVNErR92VDXL5Jos5ANIvArnvu9rD05cYgH8MpOfS1YPGMMzIoi5q34gE3oMFRkdUnQ6HQwYpM29CnDMLEjH_hcsaNYS3pukzLsLfAUPCdFQ-S_pNAnFe5SPdaHgG5ZGHKiD8eTwqkJ_N5eZCD6iJRlzq913PryYB3sPm18lju7qfUP3fy7OGRLmm6p8fc5IX-GMioqoUTFocRiCX3gXOPOEwwJzIgfXAwr6qgXH-lhXjzeF9ia3IwbDsjUhNgk1FLeM8rmMMZdNJDk4UNVU4I6azFY4vyMGIV98IQRuF62AaYpFfcXy7x9z1s3p15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=u4brvZJUT3eNSnypJ-X8nvDvk1zuTRyFXtDypepdYD6uUeN8r9ad6ShJES7xbVVsES8V7nW7OqIBnUS6BKqog-XLhi82bgFpe_xclsjV74kgoWTi9ZV2zloB672SeEt-b_BJTfZAdRxNhJZw-L-OKM9BhrHApIcyyDsu-t81StAm2-jVEMCYiNn4xXHYIZvvjQVBi9Z7eSw4xTPlgzd222PZRg8DkQJywTPLCos35FqbkvqX-mGQ29qhrgyhICZf_xfPi2KKei1JNLTtefDxD5XzIkFEX7MyM1K7uDafYyVGI_XHdcL2RFt3glfi9m-3j4CuUy7liFFjUMEzJAkTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=u4brvZJUT3eNSnypJ-X8nvDvk1zuTRyFXtDypepdYD6uUeN8r9ad6ShJES7xbVVsES8V7nW7OqIBnUS6BKqog-XLhi82bgFpe_xclsjV74kgoWTi9ZV2zloB672SeEt-b_BJTfZAdRxNhJZw-L-OKM9BhrHApIcyyDsu-t81StAm2-jVEMCYiNn4xXHYIZvvjQVBi9Z7eSw4xTPlgzd222PZRg8DkQJywTPLCos35FqbkvqX-mGQ29qhrgyhICZf_xfPi2KKei1JNLTtefDxD5XzIkFEX7MyM1K7uDafYyVGI_XHdcL2RFt3glfi9m-3j4CuUy7liFFjUMEzJAkTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUdoHuzWWhStZZBphsVjyA695mE8kBSjpFRr9WZgjzwHzvmCaYyJT9XHX4iJIVFKgeYKb_O5_zmO5fJLAbEvmDALVXEzVhR6wpJOxYMBoSEcTHiqqFnTaz0qSEW00qQQFn7cfAairkSR-gJt3jP1R2lMCsEXTy7RwENeTwDjaxAOF6zLcu-PPGp_S-k9ebQlVNCwM6CzRBO_1tkuC_wZlZyECMNovMS-bBHYPPzZOFuMA9Erabj4pT8h4UvT5XCLS3Cb_hyTneQrr-W4u6OqILvxSNvZlmfZlJ-n4bRv4Ag-cvRoXQTJYNIB5H2a_GDf0RYW8lY2BvYZ4bFqh9EIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk3ZcRDenVf4kNMeBBPlnJ1N29Qcfpa1R0-k3sMWIVoBQTlGlaUBwK7mC2XwdyI3EuucB99Gs36LMbIJhKKylh74B8vsWimHUmjxnbWnc0f9TfWR-ZFUYBeZRGBY1G6UnUBnxyLSlJdorsKiOWCuVmTUmoGSOaa6zpCsv6zt7K1vlDcjwCV_6vf_2RXuunP73afAj8lNt35iKwcMLRqb6bEsmJRij8VrhYS9WBPQf3f6Y7tZ-FaDUnjLPaEh2-StzddPVRW1_99VceChlDgjQARVliad9HTEh_AaJUa6T0mqSRRiNzskpU0GXSXeDfWAbvvEY9CzJzh-YIRDHZp7Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYhDEz_dTqOBfWglo3h6RyEzKA3KFu0tmIiCXy74Tra7y3HgZWPgNTds3WsBQ1JA9FcDcp3JlpC1YD8SwlkATiKl3QJARXWb6EXZ44UlQgRMPtj0zFUeCkZQ6u999lMFQLZ6DKozjnzr1hRJpKH-Ga92CIw-FfCtsWLIlgwcUK9TC7FiaAb8evCuL-j0Zwi8byP_k2lxhr734vqR0bDg8bVPa8aF_hpWO3LOUl-ho61MZ-fFUxdD7ZP5FLdky_U5haLXdEcEVPO2f9a_7ufhsQRpgEV2Mht4EUsGttD2pYmK4S-3w6EmG2UxaWABM4NpYoAWvN8H38DbYgDp_q4miQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oUE1kIRSxnM66nQtEipbDk3-3ayg3h6bcfgGFpcPy3HDpyat2ZrbKRmeMVsXro5AWxxey3D1PJpdKz_s4PeGi3KLwuL7Y7zysoXSrHYD9G_gUlLUZa7fIeEWpqclwq_5MRThiMcCSMEiza0OEBcFwlqdpp2vaomhAHngGFVaGJiYxN4cWi-Fw65AXYspo87P6jtU6iWfLgWNxQdqHKUBkgceYa-ls9c145PDiSCzwhqiMoO9L-M_BxYG9DhXLyt4dUzOYHmn9aFUOxXVGWHl7wE826KCzaSvFEFlo0BooisNJvJeEB8Ti30C_x0SWsjnqrBEufTfJv4dikir2JJwiaUS2eQ1RHioh7f-m74PdRHj24QS9L6oagwLYMtST3lMb7LCtzVDErFFlkxtNTRftMlJi2BXc32dKw2a0rFGt3gvcccaF6PbwLRmg99CMH3EWSysv_WB5-a7NfareZ-NJdKYJfmIc36mqUsFG2cIgRI0VhHkhdbWnJTtx69-7WW3ejDoAoUgYNcZb6caSu3OgJHq-o8UfXMC5Tg5ZFpYC-sJrzFc7v-Qa0dtFSHXm4Hm0IGTDx__SUP3P7GMupR4vtgV0PkCvpHYJjeSrPdnsDRby-_NO4izFzYaHGSeFPcImu97MEe4h4-0n9wQts1v4g-U9O80seRV2hDU1n8y_Ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=oUE1kIRSxnM66nQtEipbDk3-3ayg3h6bcfgGFpcPy3HDpyat2ZrbKRmeMVsXro5AWxxey3D1PJpdKz_s4PeGi3KLwuL7Y7zysoXSrHYD9G_gUlLUZa7fIeEWpqclwq_5MRThiMcCSMEiza0OEBcFwlqdpp2vaomhAHngGFVaGJiYxN4cWi-Fw65AXYspo87P6jtU6iWfLgWNxQdqHKUBkgceYa-ls9c145PDiSCzwhqiMoO9L-M_BxYG9DhXLyt4dUzOYHmn9aFUOxXVGWHl7wE826KCzaSvFEFlo0BooisNJvJeEB8Ti30C_x0SWsjnqrBEufTfJv4dikir2JJwiaUS2eQ1RHioh7f-m74PdRHj24QS9L6oagwLYMtST3lMb7LCtzVDErFFlkxtNTRftMlJi2BXc32dKw2a0rFGt3gvcccaF6PbwLRmg99CMH3EWSysv_WB5-a7NfareZ-NJdKYJfmIc36mqUsFG2cIgRI0VhHkhdbWnJTtx69-7WW3ejDoAoUgYNcZb6caSu3OgJHq-o8UfXMC5Tg5ZFpYC-sJrzFc7v-Qa0dtFSHXm4Hm0IGTDx__SUP3P7GMupR4vtgV0PkCvpHYJjeSrPdnsDRby-_NO4izFzYaHGSeFPcImu97MEe4h4-0n9wQts1v4g-U9O80seRV2hDU1n8y_Ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1wdUijXRYe8nL90XvFmnl-OaxOPt_LAQjJb4IKGifz0k-sjYvmnkeodf57CQtO_FEJ8gfR5G2CKeWpekMM7DCKqqJ-TLBe34arJPXBnJn9eokUC0WV7lMk5UVNRfvcsFrRmn6LI9-atxcKgEeuWDdN_FBHd6oqk_5f5kgeRm-ZnIBXJulAiu0va9m00wvQ2_5JmRSA_ySSNoioNhXEkS4MpCdJLFM1na-H3o-H3RwYrupoddVC2v5Uh1ij33_NVUji9czZhsNexDu0tjxKj_hfxOWefjcIizuO8q9MxUFursmwtiMVCipFYLVwwFxPiG2xvJV_Sr0aEEEimUrgUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXCJB3i-4JVnn30_54Qo3_kR2gJAHZWkOZGNeoecdvuXLEEtTw1-vXB6ngi61fLTAtldFFn1y_TVKpxArXbGJUQgtwRfo_2PqwUbOT8fP1v1I59WwV_87nDgKxlXaQfeiaxgdqL7I5QytX6K_7pfjoW1abg4Rugs4aTcNhuV35X5wiMMXnGZ6ZmhJWdZJI7y_yCI8Us0cIUIHxf6tYfHpoFYaJSD9V1EIGILSlaRPZuRRLFJN4v4eMV3LwooZB_-z6iL29kAzXVquxc5cg957OEYi18ROCn92Zm0Q4GevnrOKmrpiJ14krHCV1QLN72V0MdAms1WVp3tA8gKrn051w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=uWd_h7NhG0bEZPxum2oNuokuUCPqIbBTSZjO83YbXiosKUSprkb-mEZcBl_1EZOpcDBG8cP2pN2rHgk0TSWfqhBEwHW4WsDs3CB0tJJcCmv86f2Bowaq15eQwmvid2TR27TMpm-jVcWL94TuB4cVxIcTaZtNkL7jkEaWGW8byu974fKO6BJfHnn-rLf4-9qR3bPIqugnlWaggr7q1TdmPJcAf6ZzgXpl9JhzdLjNLlntD_K8LylhYPOi28Hc_BMPr6AriesWO2M5f6KjOazx5jw6VYvlmGsdX2yCMiEgbRuvmjyK5LnOkgSeQgCRKTAtmJZjJIFR-AFYh_xTmRS6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=uWd_h7NhG0bEZPxum2oNuokuUCPqIbBTSZjO83YbXiosKUSprkb-mEZcBl_1EZOpcDBG8cP2pN2rHgk0TSWfqhBEwHW4WsDs3CB0tJJcCmv86f2Bowaq15eQwmvid2TR27TMpm-jVcWL94TuB4cVxIcTaZtNkL7jkEaWGW8byu974fKO6BJfHnn-rLf4-9qR3bPIqugnlWaggr7q1TdmPJcAf6ZzgXpl9JhzdLjNLlntD_K8LylhYPOi28Hc_BMPr6AriesWO2M5f6KjOazx5jw6VYvlmGsdX2yCMiEgbRuvmjyK5LnOkgSeQgCRKTAtmJZjJIFR-AFYh_xTmRS6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkepuzYdYrEDKbcoqHapTRDyUdQv0wwhtTkcFL9kfYww_9P1Ol7CjrVlRlJTKgpOl9epulKwvXbyyb3J9y9vwIFb0PkFWggMeKuSMy8cQZ4PI7UC_uQoK5oICX21YGYn98wDiLuem2Dgkq38UL7y3e5-2aDuKJ2tMYafQAK9p5fYV_swGz8balXCC-6TxEIZ8YnGPdfktnvd-Wk6xz-sAInwoWKMdnr9F6VFwDohNA9UorqzbuGwwpuDuC7oBACT47VVSo2swauS_5HE5WvX72hW2u3zJoBAfxzsrdEbO03pXkd0y15MrPvUo42sVHlTVV3htETTTTBdKndmvpMBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chVD9GsY2WjIxmjzNgJeD5hh5ro0BdQfcseBr9JJAaWl50glhnIjURKAXWneTE1LrIhRui6eWdYKIv2p3Silgc20eTgCcyquqGR_NoaT-9BlFQzQinBi3Gj-ml-uw1FWiVBWXRgB2jf6ZwfAX6VZNm4A2rDiRyWzaI7QnX6Xh2JpiDgUm-oueoJcl4t5VY-5EPrfUz3TxyIUaJrnqhWGWmgO76Td_Q1PGetgcbyYI3fa_DBCfzSJ4zH3OgKrybyqUkd4pRoci7j0cTN2_tNutCXjDaxWi3eBuFbQ-N-lFIOOsIwkmCnyArbKm1D7t0IIYpXiRi6HCEuZMshaP5P8GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f77u0U2wuwpfVKWg4i_9YdtwtjCwMq7wvTWLI748-XMWR-6z5Ybuq3A95z6TbpUOa8w7LzZQKMwHlsThsR3-VFsLsLalcchZsNRUS9r4GbquyL_oNqAxVcY-fYFFtM1X1-JGcg5i9q11ibyNdf8AFhHcJ9JHAaLRT8yMOvgF3JRPcPmXluYg4m7gAs-HVPabRpZZBuYXlBUN9ACOsTWqqdxQnDxDTsbK521mm6aIBFr_NnZChkRpBWiR84XfVTlEE2dVQIhb8AHjViN9X41OMo2-SMmNoeDGTC4bC5miqnwBu978D76ibrFvwyZyT0K2IKheI_2gOWRTwMLvOO8_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJIsO4vJx3cQfhEfBDNKO9i5-dVypemRX60m-nLYISfvEb4Bd90Tg2ax_rtm989pQs67OVIHYsfWrLX_yBzJ_a9WP7t-nLQCpWnmP74kk8tH8yzWCDdT1nVcjLK_tbpRvGUxSpcsvShM6LsKKOHv_Wa_wLf-hlmj2QEfzyee4iWpLezRsUVs38QKaXrOIIZQo-Onzv-lGAfkA3jp2MTJFUMWLECAcztWeNy0ymhrBSfgPDNHHF2Mvwn_AGfuhdG5Wa6SD20ZwuV0Yfn1fqv-Q8FgEDCAYrpV1l4dCOaSMYLO0Z68lDSIp6VddPa49rXKONLNXxFN-80grW4-gDhZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IP-7xKUcsoYQEHg5heOG_UVaEjsv7yNxo7NKv_i046fCVkMFD27Shhve39fEExkgRL7EpITWUMZ7ZOQ1evkjFBuW2gjggVGSXRv7SblfbwmdL0qd9AWZ0gczUT_0h5_5boBLxVNZEaN3F-65F_N9tXdzNunOy6dtaCWIDM4EsDNT7DKAli0x98XuQUWH7T0-8AIpmUQsAT0sKBFmcrjHQKUBZ7uxHAh52Teq9ArzIXLTp-Een-BI3eNHZOW6t__3uLNAxZYtzYrv3SGQK2o056l6xXsCBmMVFBCC5zG9D3A9nAulBn4M6d1SKbqkuoCuSdsYmqgKAPNFr5niUfJJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0DGZ2UC_eRHCqRT5nRE6blXOKsmejlmvokY9g79f-FqKtKGj_zZSHR0IEEpb61NgdO9kyNszVfawVX2-6LXfS6Z6f4mLO44fzue-aRZ8LcgdmZ37S-3DPFaAMtyO1W47K6-5upmWVF3kxOB4QH9Q_yXCFZvt31q-zR_HLz3ibtbyMkbBXMlh4pjesNFhbmDiNMxs5ljfbQNOTx3PR4nHvgrCuJFjvp8fcN5OacJJYOq7TMcZ0X7jOI1VUKBQlsbsXZMfLJxqU3roAB6upDRaDjdk3nJ4aevO3HuZiFhNaG26oEGHhJ6ywPWKfttkt2YcSadLBDRLwWngOJMZG8bRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CenmUfm4oYfbabFa3iXG36AlcGH35mv8MOwZBZ7tiROYg2gF-EQ3ezCdAVm0YyVzC3o-GmFFTHP8gFt1HT3kVNTB4OO7uejkRxk3T6GJARsxAOdjTkPEonQASNMHNOml7ymX-f82TmJ1Rjgl6Fn9bUu-NtAz3VYma7hiWxUpZWEzuSChtde7H5FTi_7phJ-sPmz9qEHkkC4_1s4In6RmKqI-7VHhKe9TXzzVmKAYYKnflrr16EDh2WH0xk2Rd7HKSGTyy0cV20S5GdLhJh2g3lfvHWQx_wkQZyAeXKcI0j48vGwcFVMpiP54cdfIOW0W2u98rSXE5vdXUGWv61IVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKura9Wm1Z1-rkVucf_4xghcvFYVG0ZfOWFZ4H3Z7WE1OhNbTrTdpD91ivIxlDa2tJ1vMRUlbSIu4kYBKzmrokiESEi2h4thssmsAsGSY5xw-13H5kqKrgdpsRHYxF4a43eNLHUpAbonh8GpN1WZG0RwAaqlQjoifDF0dFvKLJ1OGzF-a67k3Mokf4iJz1g0D_e-BtKAbo7Ch3t_rtwzWGqNMBabOIre_66dJJhYDI9g6pavk9YFqFDbExWPlnhMYALSxoC42mRTYg6sjM5g1icMTByZw6xKbd01ThVc61YSp0o2Ici9ENOjwxWmRMKHUGWfKYl_JWcvFxDeGZIx8Cd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKura9Wm1Z1-rkVucf_4xghcvFYVG0ZfOWFZ4H3Z7WE1OhNbTrTdpD91ivIxlDa2tJ1vMRUlbSIu4kYBKzmrokiESEi2h4thssmsAsGSY5xw-13H5kqKrgdpsRHYxF4a43eNLHUpAbonh8GpN1WZG0RwAaqlQjoifDF0dFvKLJ1OGzF-a67k3Mokf4iJz1g0D_e-BtKAbo7Ch3t_rtwzWGqNMBabOIre_66dJJhYDI9g6pavk9YFqFDbExWPlnhMYALSxoC42mRTYg6sjM5g1icMTByZw6xKbd01ThVc61YSp0o2Ici9ENOjwxWmRMKHUGWfKYl_JWcvFxDeGZIx8Cd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvG9WZ5SGJQktCV6AChPTAa5laaQ-V-nis_vXlRssf5bWl_l57Y0tpms233fCqRlGb-y3fo_yK1NmL-bdl6k0qR_-eNp4DOlz_NMssXRjSKVdeNHOcUEZubQgZoY-OnvQydvTCBvTBh_aIv9ykZWAR-YLYCAF9e7pEJ1Y_m9wjPq0zXIpvjYkQoCBifAaIdkDUYe9tg6vUL1cUPnQT841SOPNYUAAf92UCqOf06ObuG3MaPP7D8CWa2ZKqDLSGgnFsn49GjrNPLJo4unkN8uy18mByQSpqIrL5e4aQQqL8IC4G-WLjtOZgTDDlPXsyZ0rKJmGAx9_zVMNwi11ekaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7SaxjlHUb64BLypEnJ6I2wkGjoCWXUyK9YUyE9_YnJFW2FIe6-KlObM3xF6tNwR7q4H5RvlqXYp7wMk4etA2ITwbi4t6VvWN358U98gveMye0EsXiHGfQro8eSt09EWlqg9LDzF_yaCyXoCyJc6al7yKlByPRh8lDu7vVW2lDBESxWqL10A3P4_8NOVrQLcOtDgK74I-jHXfPrMZnQC0Ry__Zo3LdchqGoRWvsG8gm35BGwms56TiO8o38exXI4JLu-6ScAr2twCACtDK21ptDG5R5fcRoEulUs2b97YxNcJ7HHPa7SXOOWUtYBocw9zhS-YUkOQsT6fSMtrzwW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzQjXuK5VRcaxFCrRl2xke8ZiN1NDR3T59cb6rL0GP6NgpYF7oWwYlMEGaCPqA-iDut882FHpOafhXOacGxKCtSHP18wByIokYdkbHKyCVcprRhjBnqQ5w7gjA68AB1trMqL7VImLEX-xNWRywWE0a4kIoLM9VhTcbX2ZHLPOXmNCAwuYur1wnM00mH82ZDXYtwmQWsYTFi2O0JynR8vueJheHPwxRTNLqF1tdFJN23erb99W5GbZdBl9fNC8hCi8yCsgRofCvvwOfQCT4NOGa02JhuuTZVi-OR1D7U_DUSHRyvV18UzUcMnwiDp8lfVxXg5tE33EjtKliUjivr7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1iqxaPanXUcjzc11v6IXIZCOjnyAkjJjhfyqB2Sos89OdaHdl7OBhO-Fx8QSANhLK3HO1_nZ2b3nMlu2MmoVJl_IKk73Wx9ep5z0TCGSUr4Gc3MStmQXTebyN2zL2E3Cls8lHmWFG_ZlOAmrYsqcZwNgXLs5usbFSL1hLKTFA7qkMSagovSk9tcLK22tNvFZDaPi8I97cSDQUxTvp3sJlZU7LT51BrEExbXurlsOS2DesBaYTcdYof16lvOHzSVLbvvoqrnuodxDkuhJiFfUlUsGxedhRapPjX0-5W_X5WXLq6PudbNlXHmpgxYku7P7SyX3sE-tv_hIv3pg9m1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lErjthpvnj6RC0QLQy0VQALrIEpC3dedOcaMYrS69D4oj0b8m_QgsssIG-nbWx-bXRudCqrce0RBh_fybJ1JKgMxAk9zJJQqIavyXQymhZetpzkFcbG49lsswMHLlf1xg_McYA6EOBvYaWZf7tALsRXvOFp__FLdQ89WKGOsO7wsI1x-sLzOV_Szq0Siewfo_xC2L62syVvvVWNcuFDO8kBzYbe3CBGMwcqCIHc9Dd2LFr2qtromCyA7ibzj8GQL2ilZePZTjy9S7oSAciFUMNCrXNR1fyn6G5sNoet4SrEs7OSZ7lnnZvGpUPt9MfnOvvqTbgVbjBKps1W_p5Dc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=CmkSpOcmslH-a1_aX9TidRzh_pRifdk1ijIF-uHlL2jeM6aYcrCn-cSQFSvDux84Q9qnnpUOl-_nzBDRFOU25Q1VTxpid5mMkkUHMslKtf__PhgztISCnuKTW9GcB-L5R1yb57eANdb-_C8Rjh8HRmKXWpNqp-zt6wGqYmTO36-tSfQ7eDfG7ci912v4jhQxOVX9RMrDqtm1_tS-HMlmy3RM-1iRO8d6V1_otbFUm_cUrFaX42AZ4LfObveQwdRmPtVNXWQUiTlxrTWpAP45SMxRm28JRUGWHqx9IwSKvbzgSEXtB7UA6lVA1tGsnNFT0O1w_R6y7phxbIOcVeb7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=CmkSpOcmslH-a1_aX9TidRzh_pRifdk1ijIF-uHlL2jeM6aYcrCn-cSQFSvDux84Q9qnnpUOl-_nzBDRFOU25Q1VTxpid5mMkkUHMslKtf__PhgztISCnuKTW9GcB-L5R1yb57eANdb-_C8Rjh8HRmKXWpNqp-zt6wGqYmTO36-tSfQ7eDfG7ci912v4jhQxOVX9RMrDqtm1_tS-HMlmy3RM-1iRO8d6V1_otbFUm_cUrFaX42AZ4LfObveQwdRmPtVNXWQUiTlxrTWpAP45SMxRm28JRUGWHqx9IwSKvbzgSEXtB7UA6lVA1tGsnNFT0O1w_R6y7phxbIOcVeb7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meXgkEJgAzZL5JO_iWB-YBSIHt84pYvY9AUZdRGwOx-wInkNP62X9XmUHY7vyqVAV-AEl45dyFcK8sQU-SOlaDS3gQzTphRo7LBRchVwofHxLwDdIizDxH7Ix1OYn_iHcLKdXqUeqXymrf19bVuIyU_jjRaGD0yymvK42Z4iF3mTwwGvKBUGRdb0MBKubnq92cvEuaFq-L6E2eknsaWhxvdQ7Ww6SH7c_J9yTMDTXK1Xn1hIVjG_IUnIQCiP5QqTO-Q-YXKRZCRst_2IuKRmPj5t1JY75-patR8ooXPgSxNUunWgCadPE8TIZXnqx2iHLGuoH4_MvqNLeCUw8tny7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdKBDA88YCj7a3E_TcUvVUEIbN5SYlvEtxkAvUP56Afyo9ie6Vn7hiRx9eteap7f5kCyrlqvgoWH8ngCwG_lefiROq9eXkL_B38SODR2CgvMXw23Q2Z4pp0TV9xY71roxzeKkPSuFqDO4WFLW-Ec6a-8JXgJLhXhTFIIrbie_9A1JPW8MI4znib_sLZK8I01TjNOhaZPoWOe3mdYiYITwecnxRr6m4oQdok_RJzj04Sk-tQI7-wqIN7NumanlFsotYfRhLn_7SkpbxiXqTdsZmUy61MfbpMtu76-S37Xx6alyAqGWmi6TGNa6R58AVpQ3DXTDLRFdn82P7c2KMXb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf2GMHbP6PMygSaHKMV4xOnoLaWsHFC9cl-3lrqo_jEjngey4CDr8R26zbYx_IlG2FGFMmYps3Aw3Mv7KhjvX-KaBmthb9s6aPEnsbPz2XDFeOmsYiGL4I0D4PBcmSVOBWy3d_GBztbgm4oxqaZJRjUIz2IQ13_X9dGh2W50DXdPyl2X3rpBOk5RLGrJyEyh63MVlp-17vphr9A6AYkzul7L4AYy5AELTJ0dS0aOStTNXOzn3huzzWQ1XKo9nb1pcICNCBMgMQx4a8V7DhLqgGCdPV-w2Xnx7CnfVxk1E7tEeyz-I2Ioqz6yfQa6TjZpzIwLRgjFOp4lgOTGnev5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHmcTP57K7-R5N2dNoM0i8j_dOppYmHONtGmlZgob2r1ZfWT-6isftfPft-cIDQsD8hDdSE3r9qNmjk-H5howOGhyGjORucLA9YCEgari1zwB9tqmp018_VjIGxdTusf3n-EB35KE2ZkzG8KYo1oEuF8JqItMjggQDdjmOXyMrnArh-2pCg69kcngfC5RQot4Nrn-wdpr9XifueTcztQknxaWJyhDHfy1pOkILltIz4Idim-StTvOXHh7JZTbVWg6k9qA1yM54rZp4URcQvzveC3XPUFY7tWWtjZfdwnVC4mUK8cI0JDbxx4wG8NUzAMAB5FPvFLMrPEkQhH7x6ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUxHaX_y-RtQP-N_Vgn9M2k4RdjEe6ctQSgu033lOswMGqmGdb_QCrMA7roALaYjw7sVpAfsyxxCVmL5vGzVTIQssNoL0A6CZF4Tlk61KUC7WA-QVIX04J1m9hdadPpSsxvgDiz3D8LadvgNaHKQciFUoPCoxt-msu47kdNXbXH7gNGAGZ9a86uXNCde_rfJ6UtlDEWPITjClCGJfuvPyEKo8gVZwyUlIs6oWvpRjO92PgJ7vz1Dp0gZxTQwWNTPZRubYnXASryOQFGLVtwVRHAbCzN4XAdZnGFFBiROKWTKpQp1zcuF6VSkLnGTSswCpW0IUzJEbZLF2gB91XPEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2yHmOEeZNIQdyxuCqxKM9INyYHBsyWHY_5Gc8Csn89XiMJ4yf2TDlrSDLd03_ZKRhhl-MCb8fhsuI82S73LnuT2OheBzp8JvUCTOpKVXtizplhE-ORxhekmJm8zv9E8Q-kXC3uKbKhfrMBrRHgpC0kRthOkocO-l2lzCIIbv7RnaU89DWvESBAFtY5WgIHZufF8Ne_cvPgaf04vQWEHjYDp9jDMUdCQ7-YCGrWYZEw_EJr_-GTvCIWfRgDrs7lhf45_SreL2bAJucYy4bDU97OMNWDj0tw2qu9F6Z4JK-DFXdrU4PxmGup0zyaurQE_vsaEeWjTV1MGo1l3kFJJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHSR7BIo6J8mcHkDkI1GfVx4vBv5PXH8c6GAlJlJlxHOlM4IUX6-wB6yjqn9Ktxhy1RknRpZU_HRYa-abqhTrFSPYZmOwsgAXp5mcsBYwJiID44CSiVhcsYR4D_oM6s1YEfDXjnIprnVJ3yP5ucDdD54kcslM3Xd5m79bFAaOpU8mRgqWNUxrQuDT9eoOgPSmAoTQDBPIfFk0xJIJ74AinoPuW3b7mRQ_9ikHwjhe3iCSNwQWXpa9-hgtHQBRVU5L0bWmI4tf5yNLoUxfsg03I50PIF6iws7Vf9D0D83eHZyalsNrLnTa57k-ya5hG-5kG4p1Ur9LdZr8EGJTHZF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3D-1-Y5R0LIwOdRs_qCJfi2V5lmmqw3vRIrMwvezsO6wZ8BayzQCs2WUaPpNTRl4f8qd_bV9j6CB23bHbmAZXnciSTEoaJFJBpzO8lkYlpuWzf4LWUcaJxEcfMyZpB5VQQjvjcugcdfu0gbPFDeVz0G_NpGDWJOCvTPTglDWBpV8um3GEAqIrnMAkKlywLBJgin_2W22DK7bdW_ELHBGC89LquYeZVLmRKNbjFSZURvibHvxFKMuGlp-Ae4I4u_AT6mWzR_XQuK9g1mze36ZG_ToZ59fYVama8BZRrAyBR-XYNIoqHpTT2uvqvKBKr485hb9vkGMWBsTBN5136Y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=qnu3XLsMlvEdaIxfx0f6D8IxfQO8bYBBI-ci0sF2nYNMIHTkJExqh35P0nxI9GmXE6YtJXKBkzniC4d74t6hWZ9ftBgCFhK3lmnDinI5PjJL45ikCvrzJy6tZcctCXgRVfg-kC6BoxvztxVicRvA8VzSP4T7ICq0-kkCmSJOl0K8-d_3ras0EwGTS9ute48t4J8b60Af99nUo3pOeIyUqTlJGyWVU7k1cSk3LqwGtB7DyAwgeHmdDOZifk_dTp6vDVWluHsB9U_zRYzEgyejtrzHeRJJhLlA-rIAEKNC5aIWhxlGL8VTrjSFHJGdFu8EZXdB0hFrJnBMGZv1LG-Kiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=qnu3XLsMlvEdaIxfx0f6D8IxfQO8bYBBI-ci0sF2nYNMIHTkJExqh35P0nxI9GmXE6YtJXKBkzniC4d74t6hWZ9ftBgCFhK3lmnDinI5PjJL45ikCvrzJy6tZcctCXgRVfg-kC6BoxvztxVicRvA8VzSP4T7ICq0-kkCmSJOl0K8-d_3ras0EwGTS9ute48t4J8b60Af99nUo3pOeIyUqTlJGyWVU7k1cSk3LqwGtB7DyAwgeHmdDOZifk_dTp6vDVWluHsB9U_zRYzEgyejtrzHeRJJhLlA-rIAEKNC5aIWhxlGL8VTrjSFHJGdFu8EZXdB0hFrJnBMGZv1LG-Kiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNiV_KevY0cqcpBXd5lWbI8sVvpQBB5yx35EbkVByjPmqEeiIwP6vu8HF-0RC3PjuqDtPtOo9vvyTD9yIcP1SnbMFHT5uKk-2NB3xW89tHiV1nv2jXWfEPdauY6by4WDbKocJTkjLheXtPLd67HRCXhe-JwETl4vMIydChCAXoN7DjWPthCtR_dbtciB5GiqPVIfduHQ2PegwJE9VBMTkyOdMWyJKRmm8jQo1dBei61tmrZwhBdcVEq4xsU7yexq6CnDMGCn5JE_-qKj_fxKLv2AsgcXP12ROR6AXVcr4QL1TcQOMEvbf_09hQ5bCFnueHXOT726_mvd5hxzkKbO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Z_wwUvMapsDfBk86HW65opJNRoRNLVbuLcW2TjpiisKU9bOrzNWm79H5Z7eUOJNJJRllkmbtTgkMZ3obGxm_wTvyhmSBbeamZI7Ree5KOHXaXuWIHhDyLaAu7cG7uaoshXdF5s4uB3WIGjPbqrsL2ixD6exfMiF6oGL6XVszo3lgywMIGZk-ruVTPkKHcxQtn-TkDaCVPTeoMOX4-7GjUckpUZ8VkJ6rPvGOW3qc3tOuoLvCta62QzFW3SjMYb6XBxNw1kZATvEfVHW7UdBfSyU-kvBycml1aR1yDmhTHbf_hymh8C8sxBS1WqE9hhWXzIbKV2amhqBi41imQSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA4Dcj3MRsU0HIlIbBuhRYvAIi26m0W31itH82LPZoA969JOoxxH5ZVx2qBlpyul0SYvYWr2OonVVYHR4NC4N1NPRTem5lzgGovu0XjGVIvYVSIH5b3uV5kk-WIjUp1GHNFdQtBcqGF73z4FoG3B7IcrBH_xrxFfrX8-T0W1LPwmuvYlU0ABb1HUHNuAWvEZJDC69FCNSkoieLa7KeJqDQSBoxkVbdz2a1kVe0wUU0KNTE7TsqAgkcMEQ7EpGOkELaPph88sRdmBw4dHAadhe-lrXsB0bQBMq5JBQ7HNA0NXR2W3HDlnfk03cePaNstRgHBwAVTfjvDoCpaqacCAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObUePC_CJhRuK5VkBZOS-7w0woyvrAi9vbHJZnM1a9Xz3JR5xBLQs_RBXR6YeL1IGky1_pZhl8TI1OxakecSLRSsw9FYtOWIwbtW7yHdktWKhufMTOi0w9xG8v11bK_WyVV8G0kVbc41SCFWbA5ltykZc3nERkbP4yOE49Wpcn-CaPtPumQFG2Kg5B-6LB0Iz1I81ne06je0dRLagPJSnERii0ZtcIATbSw8CUzvbqMbiQLa_f1YqaIyb8468WGEuyOWjE2pQfDd629MOOmEG9LnED-W4X3FE7VpfQAiB4aV9oXOYsx7r7Bq1Tjsd1LQZQcB3bmTNmNs_YPaamlYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REUyd23g_oQFIGoynpFPrnt8KLGH9PdBNPRzKbxZIZ4wlWucRVsu1tK5JrpZWQYM-ypHU6kD0aDEPDBOwk7C193a1msYNn-Laq4P15IhtUVcFvytmN5HwjAM9O_qL6fKwXK1ND8vLHSnBHnSlVzvJ9qEuFkC6byoiq8iKf5C7RJWTpX5oZQOyOHYSEOezoVUX6ZBamWd9FeNQmQh_otOiOyM6GuvfXc4Om8Xa8cEdgHpNGmKiVRZofir1EXMt90T3SCLRP0amPa051vU_nCAX1SFxAF96pvb-uFWJiEdtumaTyVqRQtLSb7juKi8VkdWA5lirKOY4M1GDr23QUOp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sme5TBfIQZDBZOfF1bqzBXJk5mf__uquNKqF7kTL91WfVK8mTVMQne8L5xh0oiQbSxJ0QnUOELoNBw9Fa_81fJ4k3fBuFb6XujbTR4L1fF22htIVeTWBz9tq2oD4xkWr_u3tmGrwbthzGUTwlHa00v9kqDTD8Tbx7uKSA-E8_4BsZxmRLF3z32uwz5yCFl5u5JxNZj2wptA4fGOst-luT_nqeHhy-nDN5UGFmPBgWWu8KdymqpffhwE2ZD3wygrnjKOQzdC2b0fPzKoox2lQniwaa7EsEh1F79iTmodTOOSjB42ROJ3aHF2ky9QvHKNtvhifuV-u2aq5LRrOI2hz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=QehBV-zljGfEhaI9kATMfMkSMiW6tKbOJSRdfT9XLwLXLMPLyRhdUas5oYhsfJDIfBNKzBk_8X4PBb_s_ebuHFRJpgDp_-78dM8dV6fDgpiYjqA09wUMGSXftiY2EvHT_Q_LZHNgB0qtn0JQG2dbRTFG6xPe_5Ztc_ESNM5OzVTrEh9ZCHnbbgD_eHWF7oWYnKbqCS8pwc2NODe8fSUGCuD975ZazLA9yc-O2hR-joDYzOERjcw7w38h7_Xpo-GYYs4OCeC1zc6nHMDV5uEG1w-vJEUL0rR2JLQpWNOuSMmvod-6zbGqgB1q0wkU9htg_YPz7JfYacfcmh_NPOwxtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=QehBV-zljGfEhaI9kATMfMkSMiW6tKbOJSRdfT9XLwLXLMPLyRhdUas5oYhsfJDIfBNKzBk_8X4PBb_s_ebuHFRJpgDp_-78dM8dV6fDgpiYjqA09wUMGSXftiY2EvHT_Q_LZHNgB0qtn0JQG2dbRTFG6xPe_5Ztc_ESNM5OzVTrEh9ZCHnbbgD_eHWF7oWYnKbqCS8pwc2NODe8fSUGCuD975ZazLA9yc-O2hR-joDYzOERjcw7w38h7_Xpo-GYYs4OCeC1zc6nHMDV5uEG1w-vJEUL0rR2JLQpWNOuSMmvod-6zbGqgB1q0wkU9htg_YPz7JfYacfcmh_NPOwxtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQngTHc81omem3mMN8RB2a4i-TxxiCfhSL0S4Kiz5l44pSsQyjdyAbrZCmV0maWQo02rUU5p-ioqiuStfT8z8z2NCxlEeFdUZcjVo2wQ2KBjcTGSnHuGIiAJCs-tmyAm1pgb5DHG81fbvl1OHo-06i3IGeuCF9YmKNA4g7a9Wgv7glxbf3J2vd06z28Q9stfLZG2us5GCpdJGuGbR22DFKiMavRQLjCI4N2yLsCOM7M1B3I4tXinI3trbmJ9fcXce3YA425LJTNN8gMBl17D0PfoPBYfd98zZt_WDRYeueyCBaqX9oSSh9b9IXdrSBx0C6zixtX4BplRuA9HgMe-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEUMx_u9VXYkDXtShitHv_pUOr9SGj0soLsBjSFGkLAa1iiqpsERW6yWYY4tRT1hTE4MBEvT1LOUimgtY_u1LwOI-MuDPU_xebim83q5jTFEvNZ78mtbTXH2xX1eZ5tcN50YAvGiCVR8lMPU_g4RYf4oNdpnrXffK0MUqE5qtdt6L2Osq7vK5fttHbkPQiIOGLEMQslpP56dPN47WRkqG_HZo9-VX9kF1ASDASwBkfgAZ9GQGYhaqqgMnFzfRPNcZQivpUa9Bbr3eNcD4cv1gQOwn-CmMAXcTG0Qj68G1DP4WI141AvsWWVHX7MbE0bJFG5D8Ynca0m7Dg6fh1ZvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAdn5jxtDWvCL9stWAwdUAabuoT-xjzgPWsoss3ufIsxx10CRMiOYK-HEFmlHEjwIGGy8oj0LCYogF6Qt4DGdn9NbS-qC3SFKsYo1mcoRkhOw4a0WQHs3Arew9DMSpfTiW1wJBeQdzyrETAGx8iJ4wdOy0dG0lp9V7ZaK-ZqBhzpDvVvYdd1AJoIqm2BsYFP_fMLpYSNYqDTc6jKdBqvfoVRLWYndepZuRsc7S5XsdgP5cqAjxCipfCPmYmJyuatPJ5rCmoC_vrnATxcffHkCmVjyqlDKumuyovujeM1voeo77xDTyIHUC_Znln5AbJXZQr9yH14fiX2Bz2RR5o-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0-Dj2VEjV-kmGdAiv6KU8ySglWVBWCNV7Z3wMtMXOD2IUTwUwd0wBc5_ll-bl7EE5kL2Bxk07183bggtV9k-NJMNCDsfvfx1z13wMm0mCIVnR7DbOzx-aRjEU2rPlmoQA8naKqbb6bwrpw6nbqjIq7qRuRRwnTopO08pa-fO6z0SYBl2-VXSHjl7DRM_KLkDkGLGwZ1-G4a9fhqVuJW83a2X-hksBQLzxYJkKsIyCP4AN-GqX66YWAKLpnE72oPGvTIOMKDmdLUhzPZYukGWbFkWvrdl5q0Pr_1zY0RrGk0O0vvEyyD59jcuLm2a9QVcxbNMqKoH2hGBpyuy_mj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz4kDgm0JDZXii7La_on0qtMTkZkhUV0DpRIwX22uFSU_RZWrxnY_B56TvorCPQeO3RMUU-xDkDVBbWLhqThg7cH-skp0EB_MHC2VrL6Bi8AFJ9ojg9KTncN4pEYk5HwnTyWnjkxOumaEGalc3Sqw3-cDmpVWrBS4l2FpuYXvO-T38bofeRP35M5LqiZhiYGKNKUpAnUrvmB3L3yfXyiK7_rOR3uxXNf9FBP7LCTRYYfpJZNoP84enGXal4rnVCFK_Qhj7cvRuBaZ34j3zAzEkmuI0yOZeUS65YEyCJpeB9dCTNQI4ECmbh0Z4YFCRusKeEPaUAMad1B0k945L6Y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghbZ9djH7uEYQzHnjRqdgdSaR9LzSIoYqTeLTaRXAfPTy3mGZidmvkNGNg_5Tg_uXleCOdQNHmZvraKfamJp4QpcQrbaZ81IF0B5R-i8utwSYPx8X5xA_JSvegxTFmbuIulb2ZL5Sy0reF8CuppOYJ-gRgRKsTEoCibGqJdH-Eizmd0V-pJhf-4lDCrx-qm6zJfo6kLQi-bU3hB190H4SprrZZAk95lGF4EcwWNZ-TnvSNhJIdHIV2zbJ75g7tTCIVQGELfZvgJIZkZiLTPCzOxhkjjUqtIaBUxYIQ4GN2fSbYbcgTznNpW1ZMRdz6dDWKgRKR5dHjuKrUYi1Bk0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZkqZp7Gk1LHYGLZYKCRPMAqDippQBLWUksobkeFcJFBkL5A2iDQGBR2MrQGNxGt0gddvagAbE2fZtRIY-W4wUXYVjnqJCds1ylLaqKWon_2Ac-IOvtS0Fe9URD5Dm3Kd8U4YhQlZlaKu0Y0HQUJ1J4-YUch-d8J5TEkYYd3708m2glGAC4Yvsn9yb7u2vC-526-omUUM6WhA8uJKt9IQdERizOnPpt30GUN3SzR8sNL9un_6sujqSBeg2W0qkqBHQPvjfwRkgBWYNSub4Az-UEkIvAvxMgMbbItaLS4M1etZUodyqOhTOJPARCo1EGNiO6dCw6T_ENG1R4r44LmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNfoqAn4P-ll13FgBBbg6z2GysMiI9jXR7IbiZHpMAHVOjhOJCtUVjKYXCooKEGGu8GPdAhMi2Di7HwuXQBhKhvmDc5m2jNUDUfKVQ3uNp4IAHzaV8dvutDqFlefgExGde1WybVLwHyWxQAbqiiwsQxbM3DK37sP__zAe-3QfLBoJqxyQCwnt95wl7aaBcJow4ppkZAD-DszON1LBc0b5yP56_v_MCYdK9BvPqttngbKcUyLRSfVDbUIjxTVBUNMUZtmf30wXGenzLQIBHT7WCoFMbmZJI6HLS5IxCgOj4Skk32JBO3OiG8POVBW3YFUbS52BtjbTOv9nq7EoYxevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhLevhHd2mWaIUSgLOX5kTB7ZjeElYd0XK9wF96tGY5maGfeP27FbhAwxIvDOnksOowLZx335M07SOWoec6ytvTKeEHLSPpEJuVi0jrUzztG_iQg6QhLN5Q6UcwQSCEJ7uhAsO35Lab5pOkdW9PB3znzkqWXH9Js_1PJJW0mRN8YpqUwvUGKVCRCEs9_I8C1LWSbe3BrB5D5zICYFQ5o1jwsrXchcwFKtceA6GhnKlhqW42GewWl01iPrvayZud63Ydu2PUGFkSISjVLKUcqOzm7zEbwkBQHJoKJD9A0iLggTdp971EnuAbam0lvUBSHi9DWpmIuBmu74gXQ5TWaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=GE7OkRxTNel7sdKLwDrzg05-_h4LI_RJUttR-zHiTOMaFro_zTJZpUXPz9d2XuMTJDAJ3d4zL2YPUsEf0qfsWj4Dx-b6cLYopO75M3qXi_ZhQ4Ckt-zqncavatvqhmta7C4yHfcGgZXhqnu-ydzj0r1sU-xWmPO806lrqbkzTNtx0baWCYYIM_OA_fMwI8UVU97_urd2Ahewo4zDuMHTcZKQb85zGgfPYKFHDWIjS6S1wrJ6Kj2uT4eOH2a8Js5TAjasGVkRDJPG3c1yWMGcIYyeZEhTR2zjHilyjdhiyp7HRUq5MCeNi7NY0yLm6ydKjIx--64LtKDQfqw5psblCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=GE7OkRxTNel7sdKLwDrzg05-_h4LI_RJUttR-zHiTOMaFro_zTJZpUXPz9d2XuMTJDAJ3d4zL2YPUsEf0qfsWj4Dx-b6cLYopO75M3qXi_ZhQ4Ckt-zqncavatvqhmta7C4yHfcGgZXhqnu-ydzj0r1sU-xWmPO806lrqbkzTNtx0baWCYYIM_OA_fMwI8UVU97_urd2Ahewo4zDuMHTcZKQb85zGgfPYKFHDWIjS6S1wrJ6Kj2uT4eOH2a8Js5TAjasGVkRDJPG3c1yWMGcIYyeZEhTR2zjHilyjdhiyp7HRUq5MCeNi7NY0yLm6ydKjIx--64LtKDQfqw5psblCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I590dLwns3jM2VEgurCsh3TeaDLoMGf3GWClM3NW6eebKMgEKZcIuKg206wmtuJNPMfkKoK4oE6drtp5kOb-3hAHSxCRtzSTVeek7l4lAqeZ7SOqgACgONrzfEQBzn75rcokogVKm7Sd8otcqrLZUD-Y2QJI3apV3pnfJO1W5q_x2b2OlHCL4iZf2GHlc5gsvScradjBOVJ75kSizcN2WNHrdp4xK_V5RsO-f3cNn32VHNSXDXLTXHz48RDgQODq4LxsHoBpkPAvQFMdQqBbYRkx57hY4pSiIaNMG_EogGQxhgkdAEh1aiOBf3mlP5aVbuDyMXHj_6Ypu0bKURtyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i14Mjkt9glODaVrcLQAzW_zO1cARmjMPX6re4eTVi0wW9k0Q8qeQ61uSZbb7cXsLgo72XF2qBiAPY9-snEBLQUDIANFh2Nmi5l5WhZwptylc5cPmflxFEoDBnUD1KyUUg44NEz6stYiCKa_8hOc1_DlP0wwfxqke_QV5yPRndDKQB1pb7_agFxCzflWx8Kg9WYIDglnVOSgLyTAp_U0BsS-RHWUsYUIR5hJDuvstlowK54qC_0VCy8Gtx63-RAbKNMtg32ipOhqsPYJfDEmufLB6u9BkA1DlwsiVjf0NKnMMXMEBgYFmokMol_f6hJhq4aWWdKK0TngjB6Gg28I21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS6qF-Cijxf3WlPZREwoScR9PTfx883BmGmCCVfKuA4AtETvroehxfEVnAi7oTIRLd0TLbJMD5PPvTBnxX_owfg2ME6izBsMOXZPIhLZ1Uj-Ug4hhitR7UWWBGitmFgFNqBlVM_S5gjlFL38ytBpPQluPT4TPDdECzDp-ebntjZCHUwnK2L719SIMArN8ULCDrm-erb3TxN2EbVGR1-leyzG9jt7wUty4IkqdwXSPopxU2msPOVBk9eM3Qc2Ddp6-e8coUKxTim23n5L9bFm6awtWNWBcA4P8AGn1q7WoJc-WKjusiucutrp1FBuDhFZyTgPrH1qsY4GYhxQyCxaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIOWwC8KqTM7pwQTvufuMwIQb7C9XaCCELnSQdU-tKon5xrRuaCFhaHLBbZyYpS_KccOPzxa5hJza8bEh0Q1-4u2F-LzxILMdClszBuEddA-6e9b0eLGCBy0v_HvujVY3GDY0rdsPh2iepNOJdJNKOgPG-PKzUt0tTAm9K5sM8C4b68CTLHl99lUGj65dheH7WJsfKPcwAO8EJ6CKJzK_orcT31xARG3nvJqNNMDQUbF96GWrpDMGp7AZf9B6REZo04HwzdyiAUk-BqWcdXS3dXzkoZPVY5ttFdBkRkx4GAShK_AVCOjXNaXoX6aqKWTpn20GEyhrThYA1F_2EA8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5QQMgux7lh2L_JnLy70F6kuEi-e5j93aDXwVzRC_LS7lhaQWx-erljo_PisgrgJSEUdPirEPzrtBEvN1RYmdWh0PiW3bHIum5-TLHgTEIgD8Le8iBYcbIRhRSLVYbxS5NWZUTGuhK2sEEeY3AaorvFfC5k8Kbk5ElwU2A4uG2czYbjIMVI-8d7IvShEOgGcP-zvzALToxdfvDQ4Cc7-L20z6ZKUVhmlhGgybMBK22u1w4SikLBtjAxeN2exTlBYr3BjNu66rim2cxd44ODPGCusfJ-AUdF0K0HK9U55dSVL3ENqKbn5Tf16Byjkwc1MEny-ugly-tLrQDpvqF08xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRjKWnvUY0-YVLAOpq2Zvro-AbHFuycSp1qEaumEj6pVTVVCC8dl3vDnjGs_f9eLwHPwYTeY-vi84ulta1k2p4TWuLyaUde4ZIcRPjAMnq0Ic0PT2AsjgX6Ll4JFYl5x1fVSQnOYwbnUjN00QlABibQyfP-ZwUwkXWLkR8Yv-GTS4P1H-tsBL4BtFEXd_eNkoRmKQ894CX9RUe5VoPwNzm-WBHRC7JmIO6mzifFOwPq8jXjJyw1I5YTqT_CG8HE7dQmIsndXgjU6VfqYRDOEF2tc5_P2Zgvm_pxHARY47CbyLim7Iv4Z0Hwd_qlpt0ZhFeKVIIsUL9A9mKMVQNzDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=psjUv7SeQ7DZ35m1iK2rjhiciN7nJBJdAya6hVSk_Q44gCUgv1V2DwOA3ptO_oB3fAtZkC0_rDsFBrNnV4OVrTxtM0wXm1oxkA6krngZe3csSNn0_OfxliCinEc8IqmKaOohusxzhst29lHfZ17zalew-EPLqvl-OLKmpOzKMSHTg4GWf5fzNzOyedcVgyJ1Gl8m5EGQ2jO7nn9gFWqorwlNa9_GlfPvsud38yDSRWXhU_sp7xfR81bk2OEgXJo0TzANBik8ftS1cMG7-y1uPANsHiUUi9VySRuUorgN-_zD7ZMnvizxPF1odmlOIXeqxAWo09Hkl0u3lIXjEIcu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=psjUv7SeQ7DZ35m1iK2rjhiciN7nJBJdAya6hVSk_Q44gCUgv1V2DwOA3ptO_oB3fAtZkC0_rDsFBrNnV4OVrTxtM0wXm1oxkA6krngZe3csSNn0_OfxliCinEc8IqmKaOohusxzhst29lHfZ17zalew-EPLqvl-OLKmpOzKMSHTg4GWf5fzNzOyedcVgyJ1Gl8m5EGQ2jO7nn9gFWqorwlNa9_GlfPvsud38yDSRWXhU_sp7xfR81bk2OEgXJo0TzANBik8ftS1cMG7-y1uPANsHiUUi9VySRuUorgN-_zD7ZMnvizxPF1odmlOIXeqxAWo09Hkl0u3lIXjEIcu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAbPbAWJk0zk0DDLvPpd81Pmm__nK4NLYsdlLJwj3kwXkh_0_B_h_n5VefUegjCRVMyhGzqxm_KAoj0jyT9TqxHp-9_TnkJVZ2GRvS9DuTd47_y_HJsHE6TnyTLdCVT3zFTU8bfvS_tlMgljwKT82C_70JzILoVQb0gTlHw4UUUmMLTjsNkZdFA8jq__-PrJ0thD4IoQOn9Zebmj0uM10fatFm9qDrWIFFsFvrYE-f9IOXvmdhxm6Wj3uhjCN76baCfdDnxFXCW9q2ndOpw9I2JowFm3SrI_A4ljcbR2s4T0lw7ryBrMPGA6zjSK9dZlxg4y867omaoS0pIlY_L3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cb-sJVM6541R_-RCWzVPFnnHof_Eg_kI1_aIK8C_nRKy7vFk60u5DCZdqEwrfTa_ZOMV6m81iHeENVw1bRUkt9QpBOQozk3D_AGdG6iV7WOvGdwGNP4MHAtCDs2UXsKlq3b_zAjkd16JBZOo4lsKKNsoDqOhi01fiZRYGY3J6BgCM2xyjsj92v1RnKJrePT74gmyKOPv3FrbyNjw6gfZXtEwYYZ-86xCI1lyta7ronM8ZxVAlZ3mknaE7Z35ncOb16oX_RzWKcRXTSZ8ZawERCPpA-dnVxYSP0f1pl8JatQrhwYyVTSyhhbxGpZDFVAYu69L45P2l75rSwu8HJnqSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqB2qVAS9GuPTJUzqig-5KVBsyAgoHX5J7_5Hqxq3Ii-LyMU1Uy1KDkq0OkgRigtrgS0ZYkIS7bpaBJAWKKLWsbDpF2TnjQKMdlofvKblThvIdS4rYC91ByyhxBhK3jijyGMWuMqL6HcweKEM73RmEKyPGtDG7cJ7jRxXvK2So4zGUC1auT1vUaFHLa7PSWT_OpnO972jeFK90koCgM9MtK96KCzoAosWTJy3kjhIbFVONT3cLH1dh1NNAlt1Ie6smMMZhDHQqqWnIjsHYZaWbh9LbGCT8MiZh0r25JdzeD6vRQeSQyProR8BfjWjM5mTnQAVTVvVn8_h28YcOIrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=tUaPYl9YjfF8pxI-03U9Nuac2G1zjtRhqkMvWhQTzX3aeIib_tV-bAbcyWm-LI1ZL-wP-QAWPKlQ2Qqwwh9nRdfH2-Ngrwp6VvlKQq2LecaUdh747CSIS9bpU6HZWZuNHzSvQZdJaDd3B8sJqBxw4rf7VSTMXY3lnE0AAQilMtJ9d4UNeLdIl_gWbiDsOw-ObBiX9M9Ud8r-4Lbc26VCc9OmGYwKSG0P1jirqfWQ-jp76hftZOfPmJKxobt56dZjSHo8ngYkTogO_sMA0gd6Acx1WfLMpEH3ltPyTWn0L264WHDPoTXHbTNNHMavWLidp7tzP9vswCloHnbrlVVTyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=tUaPYl9YjfF8pxI-03U9Nuac2G1zjtRhqkMvWhQTzX3aeIib_tV-bAbcyWm-LI1ZL-wP-QAWPKlQ2Qqwwh9nRdfH2-Ngrwp6VvlKQq2LecaUdh747CSIS9bpU6HZWZuNHzSvQZdJaDd3B8sJqBxw4rf7VSTMXY3lnE0AAQilMtJ9d4UNeLdIl_gWbiDsOw-ObBiX9M9Ud8r-4Lbc26VCc9OmGYwKSG0P1jirqfWQ-jp76hftZOfPmJKxobt56dZjSHo8ngYkTogO_sMA0gd6Acx1WfLMpEH3ltPyTWn0L264WHDPoTXHbTNNHMavWLidp7tzP9vswCloHnbrlVVTyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFG9HG3iRBJL00wFlD0uW-kv8z6NAatiCyiCzDWE3TREZH3Tx9QHh8O1cveafVGC2-3fPOkYJSJggt2Px2uTIWf33rc7tJcGG2trmz8KRhzdugOMm6V6ReV4_a-1BDc1HX7g7qoj_ldhL2fYsebmDcy5UGbFFUr-71MgRHFkOQ7cOJjoGlndwNt8QQF6_h-zGqOyKCEmW1Ce9stVT9IPTdNlw_rd9raX6gKZ-jmubbQ2XvWJqMU8ETNJZI52GHfYznLR9_ZTaAWwkA1E1c5HtqrI1Ke1ZX5b9ZOjQdUQ9flPC0ypVX7bvsEYPZg1m_3dIoLBbFiy7AsYj2pXgWZdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBj6N7pC9kIVXdTM5-XRoHkBHerEoMDor70ds84bI10d571_oX4g-6RpFYVHZS8YYvoxHUQ06JZBziSk_vLrgoqfwseZoKRKSvp0tvblPEBKOmbhcSFlszwHMqfpww8L1dDdXDVAiMiVAUTCVaGfX_JPJY-NCUoFuGfDg-AKvqemq8uMbLNx8mK1XQmtfNNFb1G0MKvNEheoZ6VOcl05mwBF3ngZ8T5mU3pMJVSgev9ILRkYPW3MPkCuDxwQrJFpTnKO8wqxNz4yDNlZDij6de38jhN9FPGpLob1HKuR8A5fTrKFKKSaUOmlCk0-MTTWgV5RoLw653kHIcc3SnUh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfK45dKf4PXTHC9TWxcHBxu1SeIr7O24ObZboXuswHvDIKeIbVr19njIRiSJ3f-HxAvfS4QXoNx3ckl6K5eZLaub67vm0NIliqtxWCat3CC64OZlq_EYrJnjz0oUuxq7t4pAISgDp4C4HirSWdrbEAthL36kIoHrF6g7c8VfKvNVPUkcGYYuYmBG1dP-rNTybtS_GwnHcaVNi6JNMlJ9rUbq8NYjh3HI_dCQJrmtfa9OzqLhuLoDzmdg6oHw-pCRjnselvp2V7ULcoeUgFrvriKZlyr9XEfOdXZmcQsKF0Ks44KrKaUONpuCQLG37RlBDI3yMmtZo5bzOkmPtY6tlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=V3TOZvzR0EIF3LvhrMdZjxI45_yjaORsrm10PLeoX5PI5NfJ355_LUwi2rCQn7ulJuxgJxHnrWPkekdTRtke-fEcxUiLvGIRhkApvWwOntgZzRX3fX9JqvMakRSbX2fXL0GZyVpRhKB7ZAkHrYJT0mxTpFTDrhK_OwAL0x9X9OxGyCFQiIKQcWT_xxK0iKzwUvkTNRORqWoRheGW_LyfslqlmwMRq1dQvCkb3er9qAGNDtAQYoHHHDDZsKlOGx3xj1Z0r1HFnQxg2Phw4STi1WgRWfk6DfkQNv8Kx4UjRCRs8NhlL0R9qh_qc9n7-2uMv-Q1RhXJiqBvQf1Vp2aa4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=V3TOZvzR0EIF3LvhrMdZjxI45_yjaORsrm10PLeoX5PI5NfJ355_LUwi2rCQn7ulJuxgJxHnrWPkekdTRtke-fEcxUiLvGIRhkApvWwOntgZzRX3fX9JqvMakRSbX2fXL0GZyVpRhKB7ZAkHrYJT0mxTpFTDrhK_OwAL0x9X9OxGyCFQiIKQcWT_xxK0iKzwUvkTNRORqWoRheGW_LyfslqlmwMRq1dQvCkb3er9qAGNDtAQYoHHHDDZsKlOGx3xj1Z0r1HFnQxg2Phw4STi1WgRWfk6DfkQNv8Kx4UjRCRs8NhlL0R9qh_qc9n7-2uMv-Q1RhXJiqBvQf1Vp2aa4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
