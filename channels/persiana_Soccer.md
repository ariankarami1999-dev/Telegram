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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB1x6NC-iiRiczoWmmGgxLns5JJLd3cWL4b30emzT1TruAatRTMh6RFcxTd9PlTGObAdI8xXMz1iT357DV_aUi4V3sNVi6I0t7VYwh5kkrNkp1ZJGAvsyk4r7uOFxw7l-M53zIp0mJvuIXNiumJvu_mA0nH93Jl1V4NFXowQwhmAlonFpHzuA6GZznVuBjZ2Diyi6Ueok5hNC3NCHPNmXPxjioUofvPPFK9xwdB8i1TVErAeb22G3ra0FjKEd1-lvSfVMFmbY6Mgwa3yllm5oXVwCzl7cMUaFAepi0OaiA_as_oO614pOQmEGwLqBDkvM40rHr2KVJvLp0wJqUnkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhMIaw21gr57EMmvOSpQ9y_yPDVJY_ROmR4_wR_oEqoYM88zhBaSSD0hDNb_rnzbxzii_ZSW9lRSQ4DDQJ8LsMHUWH1R2Nrz2k6OaMxvEymIvZ4H_fpEmZcEGdqch4eiFFEArT-IeS-cFv1bmAIb_LtpnX_umiiksA0EAP40vclptE_k1pPYNw43tr7LfKAbzCo-aDs_NXBUNLbJqBB1Sg0xnitHryFCc76SHc7vVM60QhfVV0EwTwSvtnfa3TSY34QSjeR6uZzlvt2pHSAXNRtf4UulEgdQ_Gabvs2PJjB_ZwM7EEVH8WiKCygCuzOLP1557cJNFe-4SvHqxoqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXEYrNfFR0ui5w61Wkb88stMMMMv1oohBDR5bC6iLNGEhkx8zgzVW-Rzp6Q22H9rGuH2ygxD4GMnbhqzB8vxdhoKgEuVnoOMTAiY9M3qZipbQjabCa9QXYN6rsCggPjyAEbYYcYqISB1EztG4kd9whcWpNDfgGXArKhTT_w0f1sdUA-atAwIoELGPHeKMjtgaE29UUPcoeeSbMyaeqk9gt1EANLb5YlcMXD7471wjGANvt9PJgLGC_BxpRNTV7AtuX1SLGFOb6qB4vD5_biumWA3yUdXeXIX5pMdnIVH4y_4mGjp4ofvEsjC0ga60RjrqjhiBlGEF-RaKUE6-i2YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKzrWkHRvLs-uOQjwmpZnWZVq8TqwFJCkYvAj0qLnAXHychwHvYC3CNgPN09WKmS1E-X0CSEg2zyKR__WejJpBSSEuQbubG73vcHzJ5wS3PKegjY_muV8tzDq2oMhsU-1vHMX1loacscxl8IJl-zi-APp0fIaMzkKRuL2swLq0NoeQczM3nvzVNOMfFVlJ5NJf_CsLhdkTU7zewyN7064k6-fzTSeyNMoQmkTQELQzKgeClXj379aelD8F1pfpYSIHWcvaHV0_NhNj2yyoAEXtQo01zv5vTNMLtkNDcZlL533-8IX1G12RVWhiWpT7fcGHJGUJ9AEbisoTZYDOKh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmKcfckfUyMbgxUlIKcJczzzgxk-6mlgT27Z7RvSdJgwySqTgrTGuam9Rn_wZPnjngFGQfdTm-ymfbUujE0M7K9QEWBbKf8lbv6IL0BNfwhFedgVwfI9s1R75zp7njbESWJJcvGsFJkqlZU_Jrh8XlOlKRL4SDnG1_9WtX8reinsWx3Ji6AOrI_XrGsADCwmQMcxn2uRcYRr4VLkHco5eUwgRTFCs0hFaGFzNtIvrsCHBsWQ3h44d6uhpq47oNEcGzkxxgZCjscBXnHoUXusPwS8MQ7mzVR-JXPoyRHhOfc-olBsUCuPKbOjonwzjDx-lZ1zgpRIivE7ok_h0EckAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcNePoO5K3P52q1k5SEjSfLThauOiRb9-SQYl79kQMs2eo7cd3U-V9g0obA5z1KwV5YnIO--pEoUTfiBSTzdDSP_PO5N05UfBD_WhJlwciN7VfY3yW4lJoDcvrMWlPghBDvDxggnfRC-TMxEJXhgLxUK-SnOyJiAzQFtCWt1qdwtBEuQUKfuH5KBT8W1BeEiwZp7fqShVZM5OuOPza-1Fg_ECHOJaUImU_app4d8tnIa9JsD_V3ohU6KrU1XjJvsxXg3PMH02x7wKOGwMQLI4iyEoFsUhvinlBuEZMwUf_HPZd8sa_ILYgJgb8ZYaFkY7klGhwYbzYtvzDZTMAbQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv33PDrxW0R47Y8Z8qPrkS_vB6FSbZvLWiFeTCH372PMYKhttmjPtr2-HdMZTvJcO2MZ1kBpAmT7q6CtuAfSA2MRHx4X9L6aE8E2R-46ViGpMrzHiL_ghoTbxgqN0s5j_rMr3eQhJFpe1ThHO9WylAjYabuK2syuTY3a9KY3cqDxJ35H5gbbWSYdWEIgVi73Dtt_JtrohIC57kjmqp0QCO8riXvHk5DzwgLY1b2HWKCRYezAa9uSAtlYh9DzYSsdcB1Nh7mbowWbli1BGw8lQLjwnYql2hNg4zsNVAg9uEiCEcJbL-a07uab4NoQS39hre2Y17Up5N9M-EZjqD2Uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwjBJI36Bc_iEi2nKhajL7HokReJFnECTG2IHyfVHqjWbMQyQRf9DPIRHSfIcdEGacpe-fJ7MOTWRf-hhybq7fEpxvRJMeOz7h5z7LAcnZzEoiPuLvjbjYfgqChFFAEHVtpkkiXi2W22U4rbTXTfg_Yic9zNs618p7G5AfZPE6f3wrSgXuvxw_fZ8iSKU5Yi5Yn9-RiQdlHYYaPjJ57kMm_fbDNzQxncWkhxG250qAF3_rrnK4gCcLalgya9ZkkymSKyMSw_RGKm51wfw5usPhlkaxobgoPqw4eQR-jkfF8VgABUPqkYFhdo_VWTCsNaKSk-ZTrhzxs6g51IVbABTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es-YXevwXZ9d17ACmRPENexkVB_VCoqxcsNnVVaJ1ybpWxll2U3e6S0BCe33sMouBx_Sgo5usmK71e11Rh4UCD2j8O67LFp0B-iN-JY-xNk9v-YFL8JaT34m-JzbJ2ALJmkerzsk3Isv66PXM-K6rS7vA0vwRVx-Vmaln1UMjqv5tLR79N7h2ULsegOkPU824rxxeAsRXaz5t4kTbWuKRpiEMvzyWJcfRmEXlpl-umrLs6BZmY7eewuuyum5Mux2xbZoZu7MeiLsZ22YbsGFir774kM1gSDvu-5B5dKmFKtrIRbGTXS1YIIBI3BHeU_r0SNnGwixh2UkG6eiHJtuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGCRnOWdc86_ulxOrzs3flT2ObGGXaKa10lix4bN_zGXPiqjkLsl6H6fvCH5H2zUKfMTODjhbB-AU-VhRtwdeE0TU-wbXSa5M6C36FWOEt4H2kIrKKfcKXyON_lSYyNn7rsySDJ8CWw-EQfSBzwPJITEgLTC6Nur6oGoQi9eBPKbE05puK5-5ccPQF5w4kKUeFg7Ml9hdS7r8kjT7kvo5ZKsaGx5a0Sw2dlw5CwSxDucyp0QyKQ5-5Ev3XzgfJccjALZbE6PGomaNoNWEQWiHFfLC43F-kMqQ2x53Z4RVm7QR11lficx9kW48p0XsZm2W2CF2BWaY9LKHaobCmvStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4KVl68s9lyOpyciNuL8ExBJgyk96gAi2rT2C11T1Mi8aWezXHFDK-sp3Krc0GsBLSbmcTB_TmuUdWxrBRqSTCdl7C5wP2GeseANOO4V5MKcSj_SyaOYGQ6ZLHIcleMykG6LJ879LUQ1A8BuznKdAYoFDTQFERb8fPd5BJude81wrouyZLD0O_E8UDuVRPZWNvmsRbrPaa5Qrif9EOxhC-nwhk9abySdOYMcZv0JidSrUpquQFSqzwzyx6Yn8wr2Ww26bxoRMhnOAsbl3RGgsdqtYDzOWA9iOZjcSHMivc6mA2jdWxk-fLABArT7VRAc02h5SwfmIKguVCplho9JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAX__n-x_eKeIQpAqRsNKKOck5I1tfv_ZPv7hWSKlp-phxvMWinfnOg6d6Yc1zVvHthMY50IKqaQnT0Mcajen7JUhItNBO8Aqrs-iZ7jwPbQI3XXP6CKjhha1uQiiwrm-LihKJHWRRU_yg8PJUzGcsdtWqYKjZEv-PbCwyzVraQKKyshIVT-5L-AJbFV1ohMPjUNcejfnXOw1I54tZ0IQCpONMDd5dC0SmCw45WkEwUsTT_i8iIJwLbhE-y0vJdw410WS0nHdYa20UzZ153pSq49_Dt7X0ZE7Gb470oE8ZqSn4CiVCT4Opg27wEJl889JauXPdjeeA8VIs2bqECfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A62YeORBEqOd7lDyi3pTKs8q7wpggFWY0i22_qRN8xeEOmcZJdAyUPwsTdsIo16oZtk6gxLJ0MclufRyRbR-z-TnRh2fvb9PZPEXcl9AgtovuYSVRLXmjTeFLcReqFtgYFnMsIV8Sevf2nl0_pXS2lgZJXDzih-5xxuAiQT6KrBCGdQAb2nyTq_-_bWvZRtq9zdWymXoA61mmiLBZHNpnq4hQrhffDtv-hJJbN7ejN1BpW8prCCX6wAhHASUI0BYrmMQ1gJT90CARk-nxjL_bjGqTNA9g3GwpMMo5yzZ1Ye7Z5nymikCNClci4B_Y6_GgMILNzZ9Yc_BIlENFuEQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSH8-X5E43xJYN5kzNZJIkof-nwHRadEfjIQIQy-OfGkL49m77uMLLh5YLer-QKDNQ1dKEwnmNaAQgPIfTZ-Va4d4LAHsdDXZFqaCW4ULO-nz-XG6OUeadXUQkn0LRoAh6HZ9tWhiNyotCRpihxZxNVw17W5VEUfndVrAHuDVdJqQzBe5YAZdFmNW3ma-5IC4-VWMYiIckXPEMTUZC0qNZ4zqi1rIwwqlzdMQKb_Ki9Qyd7Jkmc3Dkwzq9nnnb1x71B8uAE2C0BzJ7zhaN9u6eq8EGEQn4iz6Jozjh31NapdtB1O0YPobNKz5aoNz1Z0MnezTZh5_LkMLi5rtfk2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpsuU0F7Db91lkw2stWe9Oi1uGV_k6s9laUJ9OmmMlqhsJjzfja4NlIatEIXuWH2TifamnKoOlOl3urojmvAtyumxGA02lh-esG5_MCOPDlPbExi_jwJTZJuVoTy0NqGhA_0i0ENbNBqcXgEwlXUTTB9ZaxO8gjqOfiUfPV-2XdICrbwDhE6HiKY5rGmTCdKav7rYAC_t0Ef8BdBIwf23vJr63Y_UiI2bnGWCoPdYP1ORxjFPd53_P-JfQOtVUDXzzM7QzaQMK4Oc1iN3K87HBFqrhwoJcDFyhJqPoiuC14U2wLAskpyd6SnFj2H0Lv5mYSSYdPgH1gnbUO0gnx9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRx6DIH98SCfcWdFxzyry_R0-UX5v4MM7is0wCZX8dV6sgR3JOxYeSZEvWS5CfqutlL4GqMcNoO9xbUxc3M5SFOhjtWO-YPKym5yzpSn6uQrSc4u4IvYlUzzgWOIm3UMBaepTz1k1-Xo6AYI_NCtsCvI84r8wQ2-TybsXGga8kGO9qEBbAr1BkVbdhwTqN5tN7Qfq0D_4Hh_V21OoIVD2qmp4PSyH15UY9-pk4_PYss-NjykoSQ6nh2-xmbOOuu9yGGr9LAW6iw_058mGaMkhpyvTsryUsF5DW5Urg9dYN3O9c5ESctEnSdSgTDjJdS47nENH8zoMn5TwEMbcdHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myzUStoTmA4XWTeQacdYUUh3MvLqOAfLx1BMDF4vwOZNzQU9UrB89mieu2EdnWvACxFVAP3n25Ifa-3f4tScqpnH5HIFzGnGcKG5wsMP3C7UEQ_ElfzJFdanQYJXFgPay6UNDPvOB4oPOoV9QKrOaxozRVGy7UKj5zijU2-FgE-Cv5huK8jODWMQcD_PQszwIcchyis5wDUa89sskdjEd-x4yhEDShQcHS-Gv_nS_DrLMpSIhUntxB1KAont1Iz0c6qbncz80XtqEgZU9x9uTI2wbrj9MBPLkzs7uc9055r2mpvpBHCyh4mDmx594MOHAWbmGvQm_Xn8567j4V9w-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRyiiMLQRUORNRe7mra8mPHrVFeYYs_HSvY7G9YluaNG394MzKMkHkXB0vY8xg23uWnR0NBGU4RzagmIkxJPxb5fshXUwTL2R0otSl2coC6UycVBSMDb8e40-AYNq6Lf4kbOk0J-nnJQRROWrecTMuDaojPEZNLc_BtR2_skdYYAH9eiY52M5mg6mjVW9lFRBhn_UmTqHAJYz89_EBROm6VNmvl_06OwCzwHvJ8_qmZPNlxS8lD-pZsNl9NeyzXTWDJkxKsBJ8ttfQTRYxZJZf1amuNJZenMM5aMBTpipH2099s_WAk1t5CEb1Y2OfSuRrhD-TnhtwN4FFjhBvDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3u1zFo5vR-nu97moXX_W_T-pUOU4Jr8mIUttzAbUXzBymIDkJRLpaihGSoZa7yA1v6_R4x3AaU-tf94EOgINiwdXu-ZfegvAtIBXacSylFKb-RXCNwfAe8jRB5x5WoHj7vbGotktPeCyx5GuvggOZ9dl15W4k35WOP5lycaOknpIhJdkIaXlWOTr3FgKjso1HKm2o0FF-zE7bGRjqb7_u1tYmgELHMvwqEVqRdBkPb2eAMiTeoLf03p807lIJcKPOK1Jn3ZRwLYtud1Nw7MxDNhNQBbRQ9RjE8MFGjd_h3NFtpNHU5OakMHKd6Ov5s6NdbaYPUCZLl_V9zZg7JsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw4qI7OFDO0L-eMgC3T55yIoPOKJhV_IeISOqGGTHL9yEAL8oLpr2Zbb9lscELL5mkfnc1TKTm3c_3ygDxWrMcVvfVme--gVlgX8-HtCw6xDG_GH1U38hNuwkeUjckCbIEf9RJy4zZOgsHxbv4Tt8DzA-8-fTFzN-FKYRqgGoMODYb4M8OONFEgyEZr-g8B-S3m9c4B9fe_vvEF6xAdgoOqqE2nQEYsTIExoZ-YTxl7TM8gEq0rUgP1fbCEALO25pn7k4tJTpmeBo0T0WCPfsiAEh-Kq39mvzjConGznYQpRzfFy41h9MsxUMbI7Gd3BkVu63zBmrSryM0IoyvVIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=G14i6ceSFQr_SxoRMhKMEK1xFLO5dq7w9Z79Mck_-ApMbU3wVgX_7TgXwu9MixkNEOkBa3bx42CdojymfAKeutdMrSxc6hbB2pgoj54O1YadkForGD-rVE39iDB_7AG8qD5GMrbPsR1ISmtdpnEmv4tbRiSb08ZpPjK1gXdIS1zpALJB5KS9oAA73r2V6VTfuLwCqyjNoQY2lf_v_bctq-1Jl-OohSZ24V9CHIh2NlumJ9WFHl0i2YdvHYZCvYUg8bQr52ufjnZZ0FIhTeW4bmplrZM6mCsdCxyE9R5zv3hJ_REZlPfc0mnVH4J42x6pO4cJNeSHw_sqSKbDfU6pWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=G14i6ceSFQr_SxoRMhKMEK1xFLO5dq7w9Z79Mck_-ApMbU3wVgX_7TgXwu9MixkNEOkBa3bx42CdojymfAKeutdMrSxc6hbB2pgoj54O1YadkForGD-rVE39iDB_7AG8qD5GMrbPsR1ISmtdpnEmv4tbRiSb08ZpPjK1gXdIS1zpALJB5KS9oAA73r2V6VTfuLwCqyjNoQY2lf_v_bctq-1Jl-OohSZ24V9CHIh2NlumJ9WFHl0i2YdvHYZCvYUg8bQr52ufjnZZ0FIhTeW4bmplrZM6mCsdCxyE9R5zv3hJ_REZlPfc0mnVH4J42x6pO4cJNeSHw_sqSKbDfU6pWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpTcYcy33Bwvz_1lbPVr79u7WzcP8RAWoSWO1_u5tAF4-eekaEdxoV9YgJoD8tHmIUOg0iAsnid9LCrDUlK9P5O_A-vO-gVJIkcUbaJLD0-cFqmH_ovug6l3vBYb-wJ-hmzV_Yk7CpbpA3JvNoRaFxBORL8ECH4iU_GeaVR939BaR6WhMGY-dZnMpK9655TX9M5xEq9bEPaAIg5edkT17rqWuwjENNUCPbFL01Pof6GEUPuUm508QZSOjCbW1ciONif0aPgu1Cphmp1fpBYP8sDhyoP0MLkr7LdT6zvCrt96tEXaJPc6IVhVVmlKuwJpZM1NUOsu6KX9wQwf7WCEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/off5AbQFtJQodgvnXpgX8m91_seLN0AvGNeUhnnaLLb40PmEfhlie7nWGoKcypKor_N_QLamcvYrbtYzkvJz7XCgkxD-hcP8YUNp46zyzUPL8qZqBMQ9Oygb53uIZn588Y8FGu7WuVVY0CCUYzlom9IP5iOyKKg1-oUxcJ3Q6kqNwz1F9CTFJZI2i9QN1yoUCjFZi5EpQ1BRLLa-ohBs47U3HRR75H67Ute40dxamT28gm4Mwx9hKvTAQMVlJ02yLd_ALSROaXN55H8KBryd2dXqQPRiRJIXShySPlRBAyf4RzFWd2cEVad0BLs68aKPIltiTKbV7yBPHEsgHm95mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=h3xHUArJMJYuTJfBDlM9gX_4UMNd-jc84f8jeLI89I_3_q87HXmXmqnO_i3d_hb5H4AGqOcyNZr-QtxXvo5I-scfbI15l9k0_kWgKb9GShkyXmdlkGkd6YAAmJUxt1kFCRJPzUgu6NfAaUfqBzuoZCLufrrZgvn5txmm5q6xOVjUPSP7UKh6b4abaqdAMvbaHros1sOuM2P1vn-2-ApbO6waVqpz9LLax0qIOidv6BWbVCL9Qg_9nGLDI6TrDOfHUhAiXaQr1nTVM21bcKh_hSstR6oO9EpWR9OtZELTnU1r02Du2VVej_KBtI7_ND_VaaEvecI-kGr9TQlgUTlMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=h3xHUArJMJYuTJfBDlM9gX_4UMNd-jc84f8jeLI89I_3_q87HXmXmqnO_i3d_hb5H4AGqOcyNZr-QtxXvo5I-scfbI15l9k0_kWgKb9GShkyXmdlkGkd6YAAmJUxt1kFCRJPzUgu6NfAaUfqBzuoZCLufrrZgvn5txmm5q6xOVjUPSP7UKh6b4abaqdAMvbaHros1sOuM2P1vn-2-ApbO6waVqpz9LLax0qIOidv6BWbVCL9Qg_9nGLDI6TrDOfHUhAiXaQr1nTVM21bcKh_hSstR6oO9EpWR9OtZELTnU1r02Du2VVej_KBtI7_ND_VaaEvecI-kGr9TQlgUTlMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=RuXDF7Byoe3v73pWDPZYJ2VJ0WjnqsS6b1cJo7UlrdANqsObLjiRirsZkFSJvmIOMnGBAz1PsacRAHbCzhj2JutAyXam8f_Y7-uWRskHY_Yoz2uYCMBwQAX4wtoIuDPbD7KZlffE9o7KwSqN4uBHYM5W8h91DC5DRs5hec5jZ4j8fE2AR6Km_t6SE8ZiD69D1kRyk47tfQThfHEEyJ8DNKeSDqcKavE4-F6YdwHsA37g11tpAxCVTRK75N5TtzONs-cntYoAe1lqpzF4MIw6K9_7DECbQ7cKcmNkrQZoDOctUYO_kWhkw6gxH8qLKyULIt-vf4SonTsb9kL3G1nyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=RuXDF7Byoe3v73pWDPZYJ2VJ0WjnqsS6b1cJo7UlrdANqsObLjiRirsZkFSJvmIOMnGBAz1PsacRAHbCzhj2JutAyXam8f_Y7-uWRskHY_Yoz2uYCMBwQAX4wtoIuDPbD7KZlffE9o7KwSqN4uBHYM5W8h91DC5DRs5hec5jZ4j8fE2AR6Km_t6SE8ZiD69D1kRyk47tfQThfHEEyJ8DNKeSDqcKavE4-F6YdwHsA37g11tpAxCVTRK75N5TtzONs-cntYoAe1lqpzF4MIw6K9_7DECbQ7cKcmNkrQZoDOctUYO_kWhkw6gxH8qLKyULIt-vf4SonTsb9kL3G1nyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=sDG6SXkevWtwJfL2DYyp-TwpperivyZTGJ39Kc7cZ-zpuEzFEKnMjNT4middbo7oIx9oSYKche3awhQXU9batL0BExsLCwfybaA9liN9ismEPSMHx6bU6m76WC_0GPtks2_MnWV77DepflxjjjD9kUvz1tqAoamXswfPcvSiebLJdMWifu4yX7QeOyE3d7xValkTBworYWSkkA9RQEU8Iq-YhqLTPAv2yCcNz_mqHnk21jmsKnafxCweH7jIc_Nmm6oLrxhAqTB9Bq4dUMrpdq14n94riiaW_SwPugPTpk62oPeI9pnJmBsclk6ICUgk5nUU7XIHytBbwI1rcTS4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=sDG6SXkevWtwJfL2DYyp-TwpperivyZTGJ39Kc7cZ-zpuEzFEKnMjNT4middbo7oIx9oSYKche3awhQXU9batL0BExsLCwfybaA9liN9ismEPSMHx6bU6m76WC_0GPtks2_MnWV77DepflxjjjD9kUvz1tqAoamXswfPcvSiebLJdMWifu4yX7QeOyE3d7xValkTBworYWSkkA9RQEU8Iq-YhqLTPAv2yCcNz_mqHnk21jmsKnafxCweH7jIc_Nmm6oLrxhAqTB9Bq4dUMrpdq14n94riiaW_SwPugPTpk62oPeI9pnJmBsclk6ICUgk5nUU7XIHytBbwI1rcTS4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=l-owYyWEZOgeEy8U_umh6R3mIFY_cUQfaGmw2-gQUJx-U_GsrvbNUIEUHOLW98DidJ6dD5rJO7yDxDJa8oXbVtMr_yyjs_R_P5_QcrsDkWCbeE3jxe6ueCY_Ag0Qipx6FPrJFdtj8lNJO5p5p5EOyHBi2NlxTTdptv8oz-lY7ifyceexCkRvdUATXN-NKvWkPEqGFJITbWIVWm9u2r8cWC3wr0Qe-kCnD5z2tjBMZHaCnBsiNAXrElFbAomAgQTsTtTtFtrmVVY6uF_AUZNWTyjq_fSV3Yu-a0Ro-t1r10Pv9eRUZThnZMAEUiNvTUY2jyklRbnr3cjzZqja7bTAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=l-owYyWEZOgeEy8U_umh6R3mIFY_cUQfaGmw2-gQUJx-U_GsrvbNUIEUHOLW98DidJ6dD5rJO7yDxDJa8oXbVtMr_yyjs_R_P5_QcrsDkWCbeE3jxe6ueCY_Ag0Qipx6FPrJFdtj8lNJO5p5p5EOyHBi2NlxTTdptv8oz-lY7ifyceexCkRvdUATXN-NKvWkPEqGFJITbWIVWm9u2r8cWC3wr0Qe-kCnD5z2tjBMZHaCnBsiNAXrElFbAomAgQTsTtTtFtrmVVY6uF_AUZNWTyjq_fSV3Yu-a0Ro-t1r10Pv9eRUZThnZMAEUiNvTUY2jyklRbnr3cjzZqja7bTAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=YJ9ht_6Db_7JnTQSqvejolPGKklBF6qTSKHko9DH3BoH7KRXNSKSAijOV7pm5tn-a5ZdgZNFolWBk2gSU_yERoK_8q7Ec4OWWcaoWL-NWbHBMqu4Ko02DfyV1d81nsd3AET1aY5lkjx4jYyWnlyj7HWCUGjV5SeFKTiWOqqefXqhlwF3U7o2hg7W9g7TuRi4wJFCcbHWXvKNVj3hHfB5PtlJRHPXIi1VKM1I1EBTZyduHhkao1Cdu2ONukqWi0S1o-zuk9t3j_-6cDYjDysfYkb6xsaiy9K0CKyRjERFQU99vALmhrxwKRag_mR1Nl2bu7_zh1HAN2Djk_zjQoODrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=YJ9ht_6Db_7JnTQSqvejolPGKklBF6qTSKHko9DH3BoH7KRXNSKSAijOV7pm5tn-a5ZdgZNFolWBk2gSU_yERoK_8q7Ec4OWWcaoWL-NWbHBMqu4Ko02DfyV1d81nsd3AET1aY5lkjx4jYyWnlyj7HWCUGjV5SeFKTiWOqqefXqhlwF3U7o2hg7W9g7TuRi4wJFCcbHWXvKNVj3hHfB5PtlJRHPXIi1VKM1I1EBTZyduHhkao1Cdu2ONukqWi0S1o-zuk9t3j_-6cDYjDysfYkb6xsaiy9K0CKyRjERFQU99vALmhrxwKRag_mR1Nl2bu7_zh1HAN2Djk_zjQoODrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF6iShvHIiBD8ujRY18n2OM-IZxsM05S5kJUb9LG29I-YRjfd-d0Wktxga93iWuKvS72xIqVyTlrYudYjrQyH-HAi13yParWsYhA_vlowi_VRh-QBsMlQEFB-cQXmP-x1i02DRprrBZdi5HqDWsCLE2YDDMuLGCjEridFEkt4sCg8uk2bDcBa21Gvw9Rq3Yo4It5E6S4uYnVJLI2UTvRiKSHl_NIi3yZAHeqJCobmJ7VLz4l7yZzvLZu50jp_HmX4-F8JhEksGQaAXBVrbLfg0Duvah8lN4DpA2cS99LDB25VUPSZJbxoH8EVxbGV-0oxcvp2IWJPmrS5vBG5ZHFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETmIPwE_uV5OqqKSLrm0i11gRTe-pz2S71PJWawHcB_SrmdmBw5n5HZHrm1lAeJ421T3V3pcvqN0pAGc6JRmEeXNLTaYk9FZFZU2fz6LovWXD88SgmFAjFlQjoBlYBKNWZkwsGyO6cf3zCNcrbvQfWTrSrCYDlUsCSVF1wMDYkv11ZUAc_cPiI8U_ScYPjTk9XrRic6PQ9a6S-vJEbMw1e8WMtiN7M4OZuId5CA9xM35g2vA79ioG7CmNFRSa7_vLc1w22wuu83maA_S37q4tC5-IAfk_SQeYkjYQzAuRBdvy97EJ2gEkA4DOpRQJPWpZcN3aaePOWbj4GPHWDBxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGGR50obivP7ahOWPkrqANgMIYxjxPZWgvODlI8RfYTGSblapZqjL7avyEMB0e75s06zoTrCsrOOKh3yj4dxTDa4liFUQhmU2wNfVJedaBOSYdrLBNyOfBsNybTFqmEfymxDq1ONHUvVSpUgIznP4KLrqvpv_eDERNX6ukpsK-2C-nLreArLQmKD4exRgfAS1Fx4ZGh7VA3gema7inVfbZmbqD8t63zIjPKCzreDBzG6W0mfUBTA5MXjYc3jcXpnLLuZ1cS7cksmkFuQmv5XGf2GsSgtxGJruFTJeU80JDFIhiBgIKDXqs-XRh9d-gbBAMl1GWV37gWvCoioEgfZJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He4-3JKW6rkh_dLLJ1zZ7xyx_fBkcsgjsy_zQ2HhCGcf3s9ORWbh5q2aRaUZCdVUhv2U_hJcqQnED2m2OwpKqY3FQDSscfr5YwXt998c2WUUNivj8YvK7QrC8uzhcWcF6N39slyf3a3Ums5aAaylNTGUHV5updQufTLlWW04TRCHWxbU-HHjAfLcVlXcOkXNIl_0OiuioHwWJcQFtl8Max9NACmrY7-wTmbB0kzjpjBDMAA2Hs5q-SQMPZOQXKGfeBVfqmCRJBksowh5tBBId42vIooN4evU283A05n83wve4TokJSHqIEIBHVcwwWNJ-_IUP49EGVWJwt9FTOlxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZKQ4YFu-DNMbiWJglBsxblfYBEfHNBs-PsVguPrV3gcEE5sTrOSc2HBaOCbmVHbuaX2Nzfe2TjIv3ZxU8wep3rZ8iTNa75Z65IYwjOrRndQZUl99yny-TaL2CHk-VWQeoaWNgQwCvnGv4gZye7JTgRrVdZrOJJ7Sj2w_18e5XwlvSdAHcEpns-Q2a5MkrtLlZR9fgwR0awM7sFRhBCV8E29H5c5fQRn2xFyDm1TVhZCRZwle2gxiw5esQtCPRkPecOKe4wjELefC_PecFTesZn8CtEGqYubT6-rbKJ8falATreDvj0IbmkYgzM6GgzqkEkrBXpbB3CCz72wRrsa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI3lt0VjjmdzQ-xS_mUFheW68DRD7tUqbPj6qAfZ0vB1zU7KcTF_4ycV3DNcb8_evM4QjFKJ3OvyyhyNfjoOYBXJr2D2qEXTIuD6zftUr1tDuH_gvO33sscWNa9MEZ2N2Azh1fAmRVX-wbNPpPZDMo4-hcNp9qN3IOnDflSzbFCL4eM59xP_zJtKvMZEdkHk6J1KZ9Do9VYKnAOwt5bRkR1S4vOKZ_mHplTKuJHRB5mDhVeOhSV506DMSORvaRZECLd4EaWAA0-0Nyyw5rT5NYmRPZr37WWP-n02rK2liQjQnMTAMAH2zv_PzLzEwMlucratqotJULBtUWtvycyr4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtO218az0XjYPf-qVgUBjhhV_R-KNEwiEfEfl7T1tL0uJsWujThgl5HOJJtT_cRDitbILFffLNWRk1kyYyL_3kpEl0aJ8xvNnucxY4fC2HJE9mTbFnwirEBocE0eZA7wD-ZNILkDSnLbZgXPZW175bEjJS4tTzTwF01vC6oKn4BBXLwyN_wjK0-QAVpzul_mSnUzq4huP_xYzh925rgNMrAC5SjPRJxXzxSZ-D8Fl4lTyz1I6RyXJExMqhgljGpMpCSQ9mQuB33IbJrUzZsqNBP8tGy2ArNyeZmEtBKjPXDS6o1jnAUNut4bxKmRsf6EGZ4bgaRVbcAgqKohWBxTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlyQvQD-9rULrqCmqDWqWLFxdD4y1eEk7vm2d3l25SAmVtvsXbCMOXV68-NsQ9rqdPyMCtzUO2UZjfc9ZI5rYLL4ZoTv_yMgXhOpsMT7HuORqSbnevhcVI65VWj3hIqfsmqFUUw7zh0Vw8ZHQtqpzjvdOv9ppQi0QgeCgcN5_aBkk0cJ_5V3aGn_Az_mRvupiTxClLeHNKp8WDrMuxBdU9ooB1x11rm5QamYdjH0tbOHB-hCyDHVn2V_qlVuA8clyYsCBKh17-le4RRxYPqzebOXV-uSp28pBN6HzwGQUanxG9tNayqEKk3hQFSqjxm2JYnaiw5LbLfFui8g0WR9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvzLITI1a4fk2ceDw9iFPUbdDT7-6n9sbooe-IbXX46C12YyenqpbbZh0_XhEMoSY0-sgYILN8jHcPMZA1auX2c1WtnlGH2hPoC5jBtI6KpHaK10K_9wRcGsKozP6RkIvd3-TAAIvWyApjtF1_c-3WKG7-7yX0YQiqtoAxoeT05-4JpdIf59bLrVSMiNX7uLqGM3UNBDqcsgSjuVY0gWgAGjUHw7YPWRz0BaeNKyQzDBHJQRcqLzSXHvFsOWc6uraBbDwLXNI3LNRBsTGulMpCgAMtG_0V9M0RbIxysc85jJ5rjzDXfflWAvl16Bs6v_11PMKv8_cyNZw_YYFFe9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viXVHl4tQAyixNR0FNL0wHb4QJxi1XukVJs_GvkKgV3YDl5kwnJkn6wJ0abXarRqR0M-SeSobgJGrc21slSP3OStt0570IhnyO_JGQSj8O3WMH_QppCfFZXknHlqC1mB0PoP7nvk6KVf2MR2_An3zPABrGjAmaJJxgR1E27EggSABOpoZH0Nf93hP6iB-pidD5NqW8BkhsqtSEg8ZzNkA_Y9rGJVB61kq3oVbILewmO6Pg6b5ouuMHWNrjyTsmj8KF28792U5BQH9S2NQR1l33vKjSESUx5nxn-JRrLxDF-gE8sFrs3Qhv-uOMOgsuEoM6mgNl56fNi9Vi0UOq_kEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKXSw8YnkSBj5ajKGi88lGOkf4nbH0S7c-URPeZM7spqg0eOVRW9Rsz0xPAv8aCXBwK0MO1aYZZDPOPH3TbQ4pcElnIsCgpfMr4Q23UV68ecE8syQ8cMz6ULzUeKsZqmWdFb6Hb5N_0LrjALyxKf0q7Fz7bhAZN7FDxWXXfOif3zifHyzSmqw9DYtq27dqvufWY1U0yDA34sDz7l5EkOtig5HYHJcU4XHCrtODYiZc_MZEt4jO-D4GuSePfzZUtZCPhuof_-AaKX8nFsCiFOKsdoMCD44gs7ozlR6Pxnc1K9zOO1mVqrBBF7H6R0tzxrob3Z_05tZr4lMT64M-A0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHAcfLUOvnOyH_N-na1edTLc8DSxXAqyqUO6Ug4X2MPo-g8q2xBqi8bjoAZ2KwbkUdPbAMgsr_zeao-lj2mTpThszufbZhfYdddYkB5oBHbWdBuoSPnYqQZ9ErNKW0u0QQPR5OTiRx2fTO-m4ftGnLi-bNDiciHi1DZ4qWqDvdj_dC-NbnC9zSWYos12c48F7wMLyCcYb87Ns6NgaXTLvJa2B4E-bDIUzAIqWFlWKwBVZ8YbHwuoq-KBE8zF_Sd90t-OdzJERsnAYSixoXJN3uNzQ_mX5hY5U6-du_3imWgVkED8t5K0pSt4s5SFnsrIBsiKbGwobCsTJTLJo9OGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=jU_BpTwTodx6Stm3q07Op2XtuFUD4Vag1LotOAn2coEPnDUDjeRL0L7bVaXHwGFgdfP576QMqR8kUl6Ytz63lImiVJgC0qFbRh5rppdn6lbOlQgLEkvNCT7enN36lwpp0YWWnCm3lPpvE8BIsbb89FZcEI_-RoPVcImmkVnWxwJkwtAb5Jx2PpYHx4ma591gMMMUD_Ii55YTyqjKM3K1DVJ8LKNqxMJmpkrl8mCvADJaiVTw0_bMbCmgg7SAVUNloRVPd7288aP5PQJ_NNk2uB8jng06YBaegZ3nTEThVMhj-DJ6NRX-L4qgRHSNxt02gBdHsgxG8Qw8RT66f1iFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=jU_BpTwTodx6Stm3q07Op2XtuFUD4Vag1LotOAn2coEPnDUDjeRL0L7bVaXHwGFgdfP576QMqR8kUl6Ytz63lImiVJgC0qFbRh5rppdn6lbOlQgLEkvNCT7enN36lwpp0YWWnCm3lPpvE8BIsbb89FZcEI_-RoPVcImmkVnWxwJkwtAb5Jx2PpYHx4ma591gMMMUD_Ii55YTyqjKM3K1DVJ8LKNqxMJmpkrl8mCvADJaiVTw0_bMbCmgg7SAVUNloRVPd7288aP5PQJ_NNk2uB8jng06YBaegZ3nTEThVMhj-DJ6NRX-L4qgRHSNxt02gBdHsgxG8Qw8RT66f1iFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=o8Rbl_71SH77pTSwJhE6lgSK7cpqtGDaOHLC0H5L7avOV1BU5pb7-i8hhUVkcsHj-UWBOLRITEc7s4A30kVDlFFGU5J52_w7lSXovBlYDDGvjPowZkNGAtzdp58EAzIMyLE0fn4ldXOKEqdGplIgVG7iz6DYNpT2pl-V2cg-Y7Lfg3WOmRvLAPUWbeMwSgbnJvyllqwMs6pcIyX_me_haWqgdUBnhAPpzZ5-ZQddy5kYNbYvgupTPDBLu-MMXpl4WdYxTCzSh3gOyYBMPXEXbQbSFxQYs5cWPPTYESL9qD6d8OItW9AQNdfsortEVY9Wa6LGKKlIpjIaZdFHXmbRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=o8Rbl_71SH77pTSwJhE6lgSK7cpqtGDaOHLC0H5L7avOV1BU5pb7-i8hhUVkcsHj-UWBOLRITEc7s4A30kVDlFFGU5J52_w7lSXovBlYDDGvjPowZkNGAtzdp58EAzIMyLE0fn4ldXOKEqdGplIgVG7iz6DYNpT2pl-V2cg-Y7Lfg3WOmRvLAPUWbeMwSgbnJvyllqwMs6pcIyX_me_haWqgdUBnhAPpzZ5-ZQddy5kYNbYvgupTPDBLu-MMXpl4WdYxTCzSh3gOyYBMPXEXbQbSFxQYs5cWPPTYESL9qD6d8OItW9AQNdfsortEVY9Wa6LGKKlIpjIaZdFHXmbRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=Fef0I4-esDaCYGFVsn5yOaGAqo67H4cVehBjOul4Pgtomlv0SX0CdqAy1uUX5QcYRFhTp-PFvOCsQXrSbhCAagp_E27PTMJ43lyDa56M6bEUC0GmhA5lCW90T35QGReGMZJiNdu0f89gtYiJtE1Z4VY-P5Z_giK5hkgREk9f9NM--bfKK1BLi0wK0pyGswvlTVN8XQ6E9-SK3epDuoC_k2NNnJfv0WxHc9hzJ6IvTIj1F5KiYxEDD3CFjAVdapliwxvD7FsUy5t6kFvg7fD9VVgEeW5B4VxWR6-V5bXUrnCsBVZWwilL9ztJkDJ4MSxIN7LHz9bsUK7vcIwv-ZhMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=Fef0I4-esDaCYGFVsn5yOaGAqo67H4cVehBjOul4Pgtomlv0SX0CdqAy1uUX5QcYRFhTp-PFvOCsQXrSbhCAagp_E27PTMJ43lyDa56M6bEUC0GmhA5lCW90T35QGReGMZJiNdu0f89gtYiJtE1Z4VY-P5Z_giK5hkgREk9f9NM--bfKK1BLi0wK0pyGswvlTVN8XQ6E9-SK3epDuoC_k2NNnJfv0WxHc9hzJ6IvTIj1F5KiYxEDD3CFjAVdapliwxvD7FsUy5t6kFvg7fD9VVgEeW5B4VxWR6-V5bXUrnCsBVZWwilL9ztJkDJ4MSxIN7LHz9bsUK7vcIwv-ZhMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khbMbgfdl0Hq8184EkAipRlw5BGUKE0a76dbfhwEfhHcpS_CHEwtrrIgrH-LkKByb18c2rNVsn5JncrWtXsGebMP6WQnY4e76m4CeIMIuuY9w8I3e1TPTFu-TB9OLd4wGcL5dQzDcpum6qpkxjSQRGsNEU3q0LH3iC0He-q_sIrQsLyzeFTLi3nTnyVmLoG6eK528nhwT6NweHYQ-tzvfggvGgA0ZnjxLnlYGhqLGD6e4w_5XurvKe0mbv6ZWV5a_aOG0PfKImf0WrdsO78CQajqifAVlm4NSUG5J_C41lwG87_I6jWeOUlECPfgLvvum40bqaVBdgkTtIeL4CSlZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhPA4zxloa46FJCap62aGyi9xR82ZkdavlUDjCwY04j7dKYupeA6G4FZBR0oRVOwvDMo0vx85BnpeoS6DlIrXmEhJMBf76X0f3_8ivIivnDNelOAzSd98B9QQOQ9GwQw4j2HzChv2AvWR-2UacryBxb7hdeiCkrrW9V0EN4uKfVQPol0yCcGZecIKaXS5ElL0Xe2qXUoWLH98cn_aK8RsJ0ZaLKlZP15OIaAT3xrGkm0gGjx6ojGTdPitRM1S-d6oBvJ4kCaypLLN_qiZC1Ikzez6rp8RjC-Edhha1sVINDGBgvSv_jRN6300t8OWNHJV7mMeQf3DoQthvCvAcOF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyaBVUCXdZqzlmqUAkSTvMh1RNoV4qFfQmkD50EpXNwnqCp-Ot3QbbOptBe-MJdAZFZF8Aj7bh-_0cJ4wA9g9EyocPRDh7MaD4eEqHOJBgriSAY4tAa9fc2u1oA0RwNUrpGO-0emqNfeH7ReGEYkAhRAVxtnG2axxvbz_2N1qfbA4P06nt0GhODbkAdyt8vfSrmrIK525NCXXcQIbcolewNErRZK3res-iSXaoBh-O7sMPew1vUy_UVZw9--gBZYfhAzjGbxL2GMyYbygv8UA0F4oMaAmzBCpxS0TXbVZsTEGEp2I9WvXvC6fGXn6gYjiK32oW94N3B_9qULvm-nAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=FC-md6VZDwxV6t7C-N-sUHY2FM2XQW--hlMXHqUukFMLt5RFiY2wb0o_KO6OmECG-g82CVRR_rhzNMsTWa7O5B4prW4wDiRQsR60le9X3EnQQhX4ieLyEf5okHlwbwLsp2XKsZyw2l8KRLa8PuTo0xabdi2bAgIAkbJKaqHj5EQwUecR4LEwu08E7Un1MDSCy0ZFPpI6r0ikE4x2WLJnqNLL5xXSuPDXm1ivwy2bkO8d1TZQJDk75sMS91YNqVp4XFwf70qD0EsY2tsc8pXzK1fXWei60plvsaKcSQvF39SjDUxTsaBeMbE5cmzaOoTElKzONuYP7exn4hrRatBZlXSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=FC-md6VZDwxV6t7C-N-sUHY2FM2XQW--hlMXHqUukFMLt5RFiY2wb0o_KO6OmECG-g82CVRR_rhzNMsTWa7O5B4prW4wDiRQsR60le9X3EnQQhX4ieLyEf5okHlwbwLsp2XKsZyw2l8KRLa8PuTo0xabdi2bAgIAkbJKaqHj5EQwUecR4LEwu08E7Un1MDSCy0ZFPpI6r0ikE4x2WLJnqNLL5xXSuPDXm1ivwy2bkO8d1TZQJDk75sMS91YNqVp4XFwf70qD0EsY2tsc8pXzK1fXWei60plvsaKcSQvF39SjDUxTsaBeMbE5cmzaOoTElKzONuYP7exn4hrRatBZlXSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooDFA4QEwwvWa_tmJzF-i7oLYmwikRb57MNJ0dm8d2zSYNlmi1HhpX5upCcS8yMx-lUMo18M2Q3QJWzT1ONF-HSQuvbxSnl2Ez2tBMSkBy5VGB3QpuC7W4uNNDowtAcuiMQUyayeQ8dDRwJBmgMPPQfYNS2aLW4KvOof43eyPdV5MIEWctKapwxxoNI0S_39gtKP30U9maZqLocKQeSorDPD8IcOlKY0jhWQKpRWnDIDnnAfrN3oTkTZYhUIF59PTm7aQ42rpMp-Y5Lw7beraCkoU2CAUpad07Ra86d01ILYu9RdGTq13YM0_7qT7AZp38P_aIwq8vrzE4iOgbh74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWFL0vKg-J9viQ4iqOR7vXwzUY55uu8yPi4Z6B_2sGSwlY7WQjdJECVvVpaMqlEyA5ecxCxhmpbkTXmG8F70Xgkyfc-ILFM-FK0QMjcghyXhnE56GiRi9hTF4V3uPDr_fv1E08ENm4U-qlg6sEWOftqYhCUuRCiHjflcGQfOmz-g0yAqxv6oV5BubxA47Wi8qtFVQKz2dThDBZoXsyeOJhOJRtjb2Hube3CyzfyuMXhVk2gx5wLa7WODvFnUabAAeiUhsjpCB8oZSBNJQOVURYoHIC1lbgAxzw0eOtRA38Ds_iCXYXl1F7uDB1Z2R8HtVhWZxJVKt1XZD8PzL4VnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzpLR_Qu0Se7u-NyFJ2crscbaYECbJEprmVXqW689milwymt69FQcmZG7hrXC_oQ0r5mHMP1U-mvcOJ_ZAybzhlm6no-scOCc_vsLJrNXAnRY5tiEWwSL6MbLzT5_gWZwvGFBQUveRxryroWbJh5BBkoPyFbKU7XuHzzXM8kZs09lwbcMRdyo7hLm0BywllIOelOzKjLOyPJdbxUJzc7GCh6d2ZCsH0sFHEp98b3aFMGXBHo7pjkw6fBZClFAmnAiC2doQV8EtQ4sqbdddKpD5LVn1oSOOlOpREv2a0dvZsOTKdidS1jxrRxwlvo_qX_Tum_v-C2GcOEmBjVWmD1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbmP_7x-6LIsjn3pSQPM1JiD7jFDT1_LvZjMgble_PSd6ftXoWJbTCP49XpC3fW3txx1euKkb6vBfmKweze6iDoerywdOF14gtLgNXI4rYn6o_85ymQzmsS-uX9bFdnbHVarTdF90K73RglqW4qB6y-MtupW5c5AFOBcOC3ec-EAZnk3YgY_rK_E6h8t2YUAZYk18wEy8etNzJ9cvi30fybtyLVvYDEKFaX0GERVkyFDImbKn8FdLypqtazHwr77fJWwIu0DC2bgk9AfY3Y7_gW5LJpisGNOI9QTueN2rE8LkT-1895faoaXrIyKd5pWXTJANHJqo5Y6QOd1DURdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdrMN7IGLYiRwPHw83Md_ZgDzqlv7xo3IOm_ixO1RSaY1fjG3J0XOujNdgOJYWBjYZdMwaZhsb_T8F2txHniTCIQzwEHB-KRVjIUDq7H5Mm74J-oNSFdBmW75U1DCBk1V4miRreKX53Z7QSVTmgdWR2VY8wUExuDuq-RPCgw2MTyR1Q5UaO-tfaZgQZxsrT2JdAqPgMDGymJUoH2-KwjUk_V3P9SKUIbUyMPK9YrMzHvka4Hh01RZzcEFf4jSs0VTrNv0_L1uqfsFptSR-b7am7fAKygopCtixJPtpZErcz3y-RUO8mliTWiFe49b9ylkyw8ExZ1RIKI2m1qIBHg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-x4s8BAUzA4BlZI9DCmsq3h4UuarGdLbvvg7uR3nqKhHv6-bAxRdtdSjvASuqHahw_83z_k0wDJBk7LLHQXGwsb6bO3LSYwxNNqVEMmG10OdwFkUITiKCQ6wIdJZQGfOfyjuCwg2TjLIDqUNf9RxMk87uykFY_sLtKmXSOa1-RTxtDmfvkC2yE7vkVgIuRJtw6htdnTC6K4pf_9Mjk0kneMLodTprjeu1mdO2nO66phq1KcM0Oj7G6cy-yg0o9jjOQXyJb9yii3PBfkrRVuBM53MSuKByd-CdJpriMVFQUzRhJdqT71Or7BivMnW_3THoezbcGO0IRYWPBpKvXZ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDiX6QX6X9IgDyjkA6_2frSZQErTN8ZfP0M76fIFUR1xV6Uc-zqeOdB8aDxgykbaJ0S36sMNMNU3mQ2OwbYfXgDMxO1OAXjP__vO7T92LB6ehto1eD_Vpu2S1r4DDhW5-QwHel9X-bJ0lkH99yGF8AxmuyAaHmVBMWr8SaDTTpqz3t6SH5YuUBHWcwebqs7_GCQidcOvXLiCIsNuXfUpAupyoEpo4ggn4HPvwXfp3DvqaR2uU3sCd_DJ50BkAtXVVSL63D86A-9wF80CFxRWaz44B6wtdfRvLjzwqVwfCs2vYKjmRvcyC1xnUu1PHV83MM-_MlMfkl9_gEMG7GpoGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNetObB3dFJYcvCTmBwclwlrnAHWiJeC_LcG3DZHy04YuaeF4c_wBhqCS7vcbB-7PpG-Cdl1XfkIMQuRzCQ_XPvDbygw6H_WGEt_tLt-4u4UtywjfbOjKBwrqkYHjK1Ncy8pwXYphJO8wCHYu70gTjhNwvETNrifci5jq5Q2pSt44pTYzAjouDoDD4Zi2ZHZRzD7nRVaLw4oHuTfAonfabsWW8MHmzVSiS4AgzYecwy_O1Kn2X7TJwMLandBIupTIj5Wysqe0uaVfYJAXnIF4oNPxV99ajUWxYEqBD__mm4ZDKu2AUhcO4lbUKxh-frvrunRkXzTOYnGzvtkMkyXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_gwruxnkRZZijlOKgU0saIhZJsKAo0y-sSWq8bKF2o58bhKgY8tFl4WWpj5dovL5uT3HzZSg-OZK1-vRt2MW342-6Vy7wFArhKfEmGixPVOJk3_-svEwTTJxd2vsorXgHuTDwPosJDMsCpUcThIWYf1Ld9sSu4s3toJe4fzagrhnnsYy34RAcqeCjH_j2BU0aILD2kOiPk5fPWhK_D7N6IrvDPHJD87YdPV7sPqVMU5szetRoKlXkj329wWIhClW8bD_7Mz1VTgMJaClsTV9WLxcTPWN5ilaD9c6NgVhaDhCa3d8-2_yrnjPBL3XZUoKPtJtXc7bxX5XL-doYl4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8KQzvUUIxCpS72hjVHxAqIz2mtpiwgAh5cdCuzk2RFXoBjdjcJcD_H3Md5hT5BwHXiQOCV-1PQFj-fb5KxrYl-d-VC4PmDaIaHAwz7aVztgTXqU6ZawC3nnIKc3S4YwbylpSsy0b1Gy4g7eArwwGeiKuqenCscdkKbk5YgA3ONVp44xzOD-N6WaHs9y0pK-oZoGSF11zHBD3sEeq6O9EiDAlrCy3yj-jBGroa_8umQQiyN-H37kHbTMMVI5X8u8LwC7iuB-OwUWyELn0uv83nShDm9A60rL9mLGkQgChTin0SJq0qtNRP8v674ki8uLypvpr98LHCicYj4ptLEyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8sWYNUqRe_ny9v6X1BYCmRz5ovfP6iKxKtNAuDkBQaBeH9VUPM4srnq2e5Goeb8EZXuOsYZZwcLoKVzFjhQSpTJcJ-kezJpBQjVWoL7uDc7BUkpWKguh0PQLcme7MWzgBMuvkPI67zZlRFY5zN2K0ZUmItcM46RzqbVloCMxw0b5BDEbRxjL2JOg-M8GRHrqR0RCvcUdXENEP6EBMP5Zfe1Q41xF1S7QT44gQ4XsxTp1ohSe5WsvHABEpziWdyXik1vCOluyl4HkeK7LP58zMXgsnNIRZWNAixkomt4pXsFPW16YlMTZPK8Vo3zGPUVXI4Cmjmh5LGd5hLnyReH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqjfgCFnDkKP_YkLNpIoDvnXk4U3WEzvv1qv5qY3aoJGANStN_5kiYdELRou7jftpozMItSVG1D_rGMBRMCsANmyU9-DnTHKX0W4qk10-l-QTbLS4yNY_IuqJQQsS2hBF_8MVynsRII1KwDPbt_pG481TGx45mGSGSGYbejkJZVMsPogh712L1LwjjDamuWLNlLhO004J7toGB5TIRQKWDvm39NdSR_JK9GgfLFPM3R0ScoI62_VzzEPYSAajZN0-5shsH__Y_63LagDY-fQSPX244apCGLLERZk-j1JLF2I_X8olxXd1MTESxn1mBegdkIuR7pR2ZsqrmNYJb4rNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=HgUnKKJMY_v7Btj6frwX3i37EuGG3QeJXCwh87JuhlfI9JjLnknbxWXUDs6UbDf4SJO_gF9rerAS5k_kGrnrvPwdABZfDeYdG_TY486kUSIcY0BOYJ23CzlWobOvJsOJDJah_7WPnzQ0bduoFFM8UTBfY0uW_SQP_Kh6rkko3RefVvpdbmruEpi1kc37X2W_vqD7Uwocx9CqC5J2-Y5d3A1ALuwR1hESnqBa48xh9OpDjzYxVVoRm9rK8iPOLFw8lFT2Vm45_SLzHMfLLB-8LlD6vLew7Z_DwFDhncwMZGJRigo_iiPBLFhaWSWV5P1aLw6P3I0xIRHRyBlNBxLrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=HgUnKKJMY_v7Btj6frwX3i37EuGG3QeJXCwh87JuhlfI9JjLnknbxWXUDs6UbDf4SJO_gF9rerAS5k_kGrnrvPwdABZfDeYdG_TY486kUSIcY0BOYJ23CzlWobOvJsOJDJah_7WPnzQ0bduoFFM8UTBfY0uW_SQP_Kh6rkko3RefVvpdbmruEpi1kc37X2W_vqD7Uwocx9CqC5J2-Y5d3A1ALuwR1hESnqBa48xh9OpDjzYxVVoRm9rK8iPOLFw8lFT2Vm45_SLzHMfLLB-8LlD6vLew7Z_DwFDhncwMZGJRigo_iiPBLFhaWSWV5P1aLw6P3I0xIRHRyBlNBxLrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=EzfmaCCZCC_3bFl8isInvGsW_2SNvUL3YbedpBS10qs3skRdC5FGfLkF-anbgVZJH0plO2roJ54Vhl798wfK8n6Ix3_IvO49aj9jx-7TCNrBwHA3B5I6skp2XY1LqVYlsasCZgcVHDn4E3yza3CcCjUvxuRte0PkOAomuW9l1JEkfh87YUhPD3p4-91Upy8XZmUD9vqPiHxU9oLkyy6GUflAdCDDXcC8sIZbAGiyfjS0fTaW4TVOOeKDprSf-UmzflTUt90g5F9KOPLzL2ewr0nq258KCJR7j38SYDDTu1D6fN-WleFcCevHkh6khmkuv20f80ROqq0ymAiwlMtt3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=EzfmaCCZCC_3bFl8isInvGsW_2SNvUL3YbedpBS10qs3skRdC5FGfLkF-anbgVZJH0plO2roJ54Vhl798wfK8n6Ix3_IvO49aj9jx-7TCNrBwHA3B5I6skp2XY1LqVYlsasCZgcVHDn4E3yza3CcCjUvxuRte0PkOAomuW9l1JEkfh87YUhPD3p4-91Upy8XZmUD9vqPiHxU9oLkyy6GUflAdCDDXcC8sIZbAGiyfjS0fTaW4TVOOeKDprSf-UmzflTUt90g5F9KOPLzL2ewr0nq258KCJR7j38SYDDTu1D6fN-WleFcCevHkh6khmkuv20f80ROqq0ymAiwlMtt3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt2B8LVHb5kJl3AwbwSEAULnkwI7mQQqxbpNTa6NkK93PhLhb8pKV1jHw1I6U9-NgV-HsoZEfh7Nd6htAoRL8-E6UU6ktiwZB5gKxm3aXTjlrXqi1TV5bP5Z02WSwaKr_mYVVtEJuawfSG8fdhq68f9ZMo2Aw7Osd_vM_JDdmtBz8Jwl8mxl6J6Q4h5yIx1qd4x4OLVi9aJOdSQ0cUZbU3YV36rlC-QcbAFHqThoWbeOqZuQu57UMfw_-1SYJPVW4laN_OzHOIdczJZ6Yp5uU7mvzvY8ZAv8yMVmCVZC29P1DcL09xsrTzpROIrPx6QlEVY-IwJbk4itKbhR6gUGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgP84KOi5jx9N5ed2FxQRvjJkzV0Ay-g2bRaltFdBt5XsN4q4sdYYi9AuGKGPvqBSLeEwufhv6Y3q9_A-myhul8oV-ovwHdd6vD6uAZI7VHHDpLaZW0M1W0436OBH0XZBMc5DJxmJoip8Xzao1n_8K_1GaxKlbILFy2GD5QZaE2YOqR85pJogjdksOTW8sPcHrXvoHSwxTISW9w8NUMIGlaD-ZENNycEnErzCwHykP3_AEWzONc6MoZuoUVSS1ZjixDkpqUHj4gsNaPq6LFRfZmZiRxVtim-UfdsxJ2vpbH-cdgVt-L-FACF0-4VbPotulciXZuYFAI6vRI4_cNfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRkxY4gm6SeHXrp5zP4Qbb3OlRWCul6AsdEKNwJC8GHET0QnsI4qeusajWb-Kxkkfq-T0wRlGgchJkim9xgCgDMYLn--WpBt7AHA-c1pIdBbqCMvktWs3mf36qHAOAPRSN8Vg4n52usenizT2hNAjvYi5Vu6XU0BrcTPl5fhTBZ1zPYZK91FYzUu_Pnul3uO0QMPEdoSW4qsKOxSrjx-KtBorcyUyl0MjbXTTJ7hkEZt94v5PlCSyifsHNV7IKravO0HNAE5nuJKMEmux9DG4YCx03f0XXpazc5FQ1s6x9IKM2nou9gJCZ-VMRoj-RandVo8sHZQ4foSJhv2HxMNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjsObw_qUx0K7hPexYmpkTCiLL_vyVNHnbM1ae8Rj--pO8KNFw_TtQetVFdPyyhmbNjhZgpO3s9lxoViG7GW0aKQAv24AVxhuqwlNHxLIt1CSVpiTGfTn5brtGeCa2sq7uPW9qeKcLN8ZXSfLEE1OcRGmfAEkH8eQ43IowRbBeexcAw0CIYqCLdlX7K9ZBgSdBC2xuTvC5LS8yollQtfjo1KYgPjSObz9-PYxh9REzCXUOG1xjhsFpO3tYVwCi9KMtyV4I3yrVCZ3bTYIIKU8XBlKGt6Gg4TGZKZ3xZ_eASXsqT5ZMzCP-aSf7VKVUYw4R3d-xa5pxSIBT4RdlCW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W03YtzW2EVnOTzsbXopnwvW-DNDQ71VOeTRjFlJjxWPspVYju7fNZmNL2AO572AVNJEcrW-oQv8uUfS-sOudW6_SL-qiTmtX4tBkaMYHFbhAjsKAxFWkExKPXwg_xSGqlsVePqohML8plOS5qLBM0aVH2BZBU28rw2IqhYKEXZni18GWTum_3IetDBfhKB_a2pQSblH_X0_3VItswes0SDPOU9cNBjbWcLrVieBtI3bQqt9ozNWpcDeUxcR9UdXe4hFjjleAr4ojlqLjh8Stf0EJuC0qq6MWLN5BVNmNttF9cWP7Nrp7q90IG54bXAdRANawSkJczlT5luDEXN2reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6530yz9-JWix8U-HpWxxz0C9n9UJ6uSyH01t5YgA_TlYjstAbqjBlMirVV1m0S6PtCYei74tkbmDw9bRiVB0CMxRPJawXQP0yIuvb7ZOdC7IZqDUdTGcYQYwVkkkl8ylkD-OypZYrkDGARBa597I4ZCNqOAfPKk0oOYAYrPdSZWDTrEm-HsFYsptI5Yd9ap5WwOLCwtab7jIpClG0JNExfpXSomTLSuNL3C0V4z2qTia18VEQmYCrEeLN-QYf5SJnlC6x6n7QF8om3EwCjYrxX2OPyIZcr3LTQ4UzA-b3-XUgQONNTLXjbVYVgPFDRHIjpofvezF35CMRfZt93Vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0z1jnYEqitJOOmMvJgBqBy_RqphK_bgo2098AvEjZsHdZ2TUz-n8rHSiIDRWHMqlrPTYujE5rnBUIZKtkHNUaBXgE5vbjMtpQcxfkS66unDzIBzGj_hJliA4DucQrdQj13k6SFQ6k8_7APZ2PMw54NQr9SQkgs7Nsn-l1_-UReAbeolu6RDbflMF2m-A5gBkAQc88FIVAuHNVeGXEwEzTRrd1RS5kWmlIsvu9LLBGsdz68rzw7_LoaPhM7_dmdKdMIUWqKrRXrwxcc5CQvJgk4w2MPYLKGbmXn9XgWIwTwJPRiyD9GfOPrG73NSjLCMOzLrhgeB1B_jfjeTD5cA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK_8o92JNnKQmaVSvU2wHstl2OtLaVnTc_6vWc3kmyBXQ9aAiONUQkCkuO3y6H0n9QiLczdC75L9X8QiXwiX2L-Xy3u389fhfVS6W_y8Xt4yaa6n0oeGQoBTKC_vQ1lIqy8ouS1FGi8WTqgwZ_M5azv0B-mnfsXGfLCr6MyF76ev0qicY_eO8epKzpamn7SYu84xr5FENYsXGjKj4EPvpzIHiWJ93BxT21UxAotMNqVqDeHZdM7EBk5gm8j2ng7sfkar7kejd3s2RlwB902TIEj6R3-2lQ4pl6nsrBfM0rrlGz5NKBlso1jhMJa1KMmcIA4Jd5W4E07MIu4eiLDaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=K-hnkuiMMVMn3Y5k5XZECei0SgL8xZ3jm3k8QQCWBk8jaYiVZFyjdblW-OGJvQhrVuzIoTp522k_Kq00b9uISjSr_Y_HC6EDkrKYLoitX3t5ELBRPdAx-RVD_RBD97o_ckIGj6PG0gc9tYB40AbJ4oPX20zujxea6S34y7L_ojWMy-htof_5FMr6thN39mX0KT-BNwhI0hhFHKvnhn-JxUyBOVKBEwhY5uTPFHw-HE5R8X4e4_Z5V4VA1Lsmng4mwLY_1LuM5kXGKell5QnFoqzqZAWK39GZe1eQaFJLbyErqhYYnCO9gffi-Yn8clrBoDyATg1eZWSu9as6epQtmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=K-hnkuiMMVMn3Y5k5XZECei0SgL8xZ3jm3k8QQCWBk8jaYiVZFyjdblW-OGJvQhrVuzIoTp522k_Kq00b9uISjSr_Y_HC6EDkrKYLoitX3t5ELBRPdAx-RVD_RBD97o_ckIGj6PG0gc9tYB40AbJ4oPX20zujxea6S34y7L_ojWMy-htof_5FMr6thN39mX0KT-BNwhI0hhFHKvnhn-JxUyBOVKBEwhY5uTPFHw-HE5R8X4e4_Z5V4VA1Lsmng4mwLY_1LuM5kXGKell5QnFoqzqZAWK39GZe1eQaFJLbyErqhYYnCO9gffi-Yn8clrBoDyATg1eZWSu9as6epQtmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5FIhDCgPJXtfTdwBH5YEeb5a9nOryMgMnRoR_3-hdhwtTuPXiSWS7bKQeU-Oea0s_L2BPaW9AEdXq6y3EzOlq584NMldydmlETCIM1DKxhWMTImme2KeGCqdJMA8pBThRJQ4XddeyyTHFmJxl-BAXBNskN83kNFepirafcwRGzuQiVnNpuQMWwxV609_PQQLZqGjcmoa7yTBChTDJliJsXA4-tk9S6Ao2US4R_1kgt2rvzqDJh0-Ei9D6Mqft4X2sH8OqqAostLTjvFpoUgXZIQdqmFX8y0EQm-jzIPbddwVsCS47HwX5BDANgGbR-bZTeB1OcgxXSNoDvhzFbkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=cBSsSJltE7vTbe79UWSeETwn71Q8fLSFzf0uwLEFNnAfUIEc9g6hBk2HBWhJgEm0d68k5uRqxviEQwKnzG74o4FKJDwfji_Pvvaxs3t29SPTrzDAqYxJIjRw7SvLtF8dRPsOb_rA6zjPZtjy-6O6t_jKLzQpZZ1tOC5QSU-aIp0gv2BsqWL57p-Ac_mf-MXoig1VCLyelXPMceRGBK5NimYd2VV2JvBcZOjGH7zgtbo0Vk_isjGEPA9V6YGF7AbuDEo2PMK5p7YP6-O6-svE_ob0wlJFfRLZCazMIqaq_orMOGT6k5sysb0wd_81NhaRhzCZ9EBDB1PQCPlBPaHniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=cBSsSJltE7vTbe79UWSeETwn71Q8fLSFzf0uwLEFNnAfUIEc9g6hBk2HBWhJgEm0d68k5uRqxviEQwKnzG74o4FKJDwfji_Pvvaxs3t29SPTrzDAqYxJIjRw7SvLtF8dRPsOb_rA6zjPZtjy-6O6t_jKLzQpZZ1tOC5QSU-aIp0gv2BsqWL57p-Ac_mf-MXoig1VCLyelXPMceRGBK5NimYd2VV2JvBcZOjGH7zgtbo0Vk_isjGEPA9V6YGF7AbuDEo2PMK5p7YP6-O6-svE_ob0wlJFfRLZCazMIqaq_orMOGT6k5sysb0wd_81NhaRhzCZ9EBDB1PQCPlBPaHniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCl1AtDbYkLgdEbnH-OwwqgJRZEylgx0CFv2uuiZ86d-brIEK9zIIE5PW9Q5GORO92FFfs48rCiW5p-gk76Y9v-O8z_JJAI-M0y4gwY5cnmhqqiL6QgBGVGHyumRBr3Cu7XkH6cIIhpyhVlicE69ENLTon4ZKnmZcWK8b6fqBxreZthuFpKEj655D9DIIgCQri0x5jeuA_JEUK91Q1zpThTQ-Jr1jPm7OCuGkGwVKC7L1a1vq3RyACB4Bfg_LdQLeg2UWdB1SZekUWwhR4TsNws_lMESypt__wp57CYuNNYraUCyk7RvihdEk5A_LA5ajiI1VVTisKDpzn6GeVay3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6B8qQJVdTyF8j7XbjTbZlHQLrxCJEQf2EXzGAzZETiv4XR9-k1aZtJVTAjAmHO_3HeHo-WvLZl5ve27C4HoNaUWQiP2THdiwlPxLQNXCW4HVkiCmnE2zWBHYrA8bAHFHd213bIxWyJe_b1z_C-ZQeVVC5n2zASZUUX2jMOnwNMQhMdBfLZ8pmxeDF82MvKVY27l8EGMo3UbjC4lemnLmfyP1vj-TNiLry42RC0HuQxruELaLN8axjzw6VR0IP3TUuUJvCSLrn6xU2OvmfUWKXl3H8UjszIBVnZ-s53pRQxF2TNUQa69Kdds2lurjbZ1pYiXS_TKSmNAtq5xJcw5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=jko0iq_LNAfZ4PYtoj21xQ7v4gcS1gzCjS_jt_Q1zzFSjtbIBZm6nMn_lhhyerBT0TezpG8vieB3ZMp2yecgc54PMeNJ_NOpkZNgErLpIjWYit4zZbEdIZ_EWG95yxnpcgorvpz9LJIoA_Sksdk9xK-GVW39yuFRM28-m3Xjzig5KB9Bcd-XC5XP6xzXvow03SXz0MZSCyNSRM5vOyiWDewH6yYNvMRbM6nnnzAsRLSF4iFpfpn8TNvJFAn6BziSCgh4XGB-WpvSE8obbF9Jty6O11dDC7WaGMLhBqLP4kxXUxWApPbrZ9dsvmlKr7JeE9mKU76co4Ca6IEIObukhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=jko0iq_LNAfZ4PYtoj21xQ7v4gcS1gzCjS_jt_Q1zzFSjtbIBZm6nMn_lhhyerBT0TezpG8vieB3ZMp2yecgc54PMeNJ_NOpkZNgErLpIjWYit4zZbEdIZ_EWG95yxnpcgorvpz9LJIoA_Sksdk9xK-GVW39yuFRM28-m3Xjzig5KB9Bcd-XC5XP6xzXvow03SXz0MZSCyNSRM5vOyiWDewH6yYNvMRbM6nnnzAsRLSF4iFpfpn8TNvJFAn6BziSCgh4XGB-WpvSE8obbF9Jty6O11dDC7WaGMLhBqLP4kxXUxWApPbrZ9dsvmlKr7JeE9mKU76co4Ca6IEIObukhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOetC8DtAwgvu8ief8_MVa3E2oRdKm9L7NiauSnERb1Qfmi9dJlgZcY8uRNORDFofzy4s4V0IDC3E8DD21iwV89SP52ITOUJCydBDcPy3_WsbAC2-lsjS9tGH0hX64bwgVTy8J_4NNSTj6c2Wf6o2yeFlQ8Ur7c57wm5Nqd42zaWVc8NlgT9RPCh5uwAPl7yrp9JMbffVRM55q7Egh1WBdPccsNomT4JYvwNO7ndhylR4JGROmKogkL_zQS9W9ZQvYgUEoNyY34nPELd2CCLiLpYKeMIwXFoyhWJWp7Q9ok5XL293nIZwslWbb2A2sXfi_uFqWtJQRXsEopl1akkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF8_Z1ZsglapZGlMp3s5rt3K_tr2ZMg9qe7ouneHYbqdNmDBCE-a_XgUnQ8l3fqgjh972UHr6Z3fl9Y8u2fQAgPKMxntNA_qar6nKMnRVz77EYjnOHHOwYpkpdSl6nVjKUrSn-bFaUsrLC3M6JL-k81gyb87p3lyoJCmUba0jZbCGB5Wt2aLG97xbiIferLjBHc8e9uLbD7v40E-P2lo3lvJMsPS697zCq6mt_6YsJ4I3Az_-2IU6S4UJnh-Gjdp9WQG0H813w45VcjBq6ek4-7rwj8emfiossZdoSFIcvKqn3EkdQvTVnP_NhoDlW1kwRScJS6v4SW_aLBNR4hTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhdaH1x71AmIvBesQJjerEqUghIYxAy8BkLFoTdSIQBf1HUThYX9OrFIzWAuMrqdVM4akwrnvjKqO92SfTAdnBVnKGltk8qhTCxs19uirHKXjYxWh-x78rv4zRmIrVuFzcRacUb7ySk-lXr8ra_QEX2pO-_pF9cUH74buS-IJ3Q0wxwepPKRfkARCKxUjgQT0Vf8YRdZ5xsL2ABh0Yfo0tBmA5OZKHFnIs9NUNMy1hKRPhSSW5pPylDAk5FnkjApsrrszmVcaArlyPKM7lMz4wm7AV_Q-sNBY75-4kZA4-A3Yh8OKUF4pKk8d86-TdJw16Dy26yAlXjkxfXwywzskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBsT90t2l-UifiqxgWL_9HaFpmt5izWPCA8lrOen_sn1UKNBu9KZOjX15lH2RZ5k60Q4eeLkblNzE1ID0DYwTTrYgBIO9l-jLV_kkdMjr-n_EPpNN1LlZKtSazcYZECJfjQ6RQKrNSeEDWQlA8FRnKb4z0mZD8ffJkO2tygV0GQNDryjlInvKh_jOB72ndVJ46aMX1Ad9n2WWOWxpGnZZVFW25FSNU2gJ0-5XxUyWP4upgmwqAPP2_9fPxE4yJNV-M82gRBOtVszMkfSqWZBGufrWdpOsP4b6XLTtbVeLaDmgU9AXonk6s-PqP29A_651HJ-VizmRUfEnPMOPyw98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rbg1B2o3vdyy_ozKnOvtkvF2F_mrhsaMTHm1i0d-T6_g4A0uGDd_sgoBVDssQoKI6e65aTDh2qFKKhPNfxT1eoPzM4tkxfdENrk4PVXX5mJYfKsvmzNe6r8uXl2bzxvuveHnsEiuwYppKzq4UfG0pmSwDzRWVOw8KmbuRiFY5IK3C62NFtbHNO5RgM4Svwkgh6_adQlzq64YyG4a8FOFAjyGLGr83J9ETaKzT_XEEHW_ATpH8pZkM2jY3dZRBTioKJRjj82zEVfb4hJ2QGT65Ug0BD5mV73GI_4htNqEtMawdaxY8qR_iEFV11i8vMvw9PUaqU35gZ68KwDnbzW15w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjzJykcSIfYjiziDy07liZWmtgDIWaJNijeT6TBZ9VYbzbtg1I7031SIP7aRoowguvkFJbTi6yPK5sCCBUKEdO18EMm7qkBmBX9vgFvmXnk8NwYlwQSIssjM33X0X4mU2K9Cxfc46Q0PuwStW4uz9AFKEjvOSRapR62IGnotDugg1RxoB7wT0xjziPsMwM7R6VVJUeJ-syjFF8tSZznarzpzD36BSN_CfEFR2yo6AygXVTL9dKAPBR5gi3Dip7HO-ZbK-WzdLenCt_xrdevLyOc-M2HGBZgJ6eyeWNa4mDuEoztFmdHOnUOwHz240jX-LKdUC67EvPFLYVLzaipnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGvQKXC5IFVoT9ot6YZr6Ik1dYBJQP8J4b_XGlQiFzXzgP_1H1Rd7fUYeumGGyiquHGhJtU5i4A5y7_beonJFxnxqQB2TpgBqoYnh7mEnpiCp-XJQZDLnWQcwRElFXBaIdHcfAC4tp0gi39z151foROX_vFJsakQTjzs16Z5tOTQ1cmdSMAD2D1B11rgU7OWWFrDvP9jw95kwn4WuniVVbmUo6e2VBSpsdpA19HYLmK2cgZt4KR5H0vpooBUx8Q9KyeR_J89EZKiNNDek5rHz-qYb7K76mNxw1Kj5ajRQLc5uyIEgWbJ2jTBxwJCYcPEAWoNnXcCYK-U7Sr6-tDWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM1AdILKWClACPO8kYQKkXdakPcZjhFdjY9HJR1VEO-oRDaiU04TXrKmWjiujeMjrtqY3hXm0b53gyHUp6ZzRZSJJAONVfZEAI6RY0sN_yDIEnZoiFklgZE_wbrL20cAkcOKbMhMWf0fvCg9sL3qZNHd-yTB9pHwS_IoayCcmIfh3gFOeo1_l8XKenwNuyDuS9Sw9WRlYqXLc1DfwepS_fnae0TIH6C_C3BS07edETMJV-PsGIqSg8z62awBHkILlhviZmMy1jQcLBtlsUoYKrG8hMX5hA34VItUmt6NjCt6Mz5FasVlK7AypsQErNplNVUgOVtq72F8GN2gH2SNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m31-VHsPgVZgGajEdLDMNznS8yznX1UJW635kvz5SR-3h6wSWaD6b2Y7C9sVzqUzRF6SOdqZ_dIVFb7Y6F8PZfuUFeWw0sYN6K9h9LEHyZIVQm9rPatIyZA8dFYedBRIQRNfkjlumAcTXkREv8nb0yx-TXsrS1nnz7vabKN5zrd3sYd8S5uUwIVS2hYbRpiBD4EsDpXrSD9MtTsymLWUscWpIB4xyRj1EAC-EmTECbDtOOqcyMdwd2_G5NyMNuTYPc2gvVuPTK8kD-vFXID8naxBOZ0LskqkAdMA9OoK-9bHnZo2VrD9KsUGYp-wsDnnlUQfNqRa5Or-j8L0nOXj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0puQM1CPuUTOhHsNeHeLMz-H_fRzh4nsbMZRJUV4AKJ2wjiJ2pR1BZakbqWAERD8w34SN1K_lm1dxKTZoChP9uYLWNfbuhDcYR6VEkb-djBWrkCvqJ3kBXZlVbHLMElolkyzvBEXlj7S3OJAvCJbfWHk1tAX2QtaG0RmVU-bCckZ3jmSOBKdhIipdL5OOk72r23SYLPQ9jbbSoa2QNdmoeFZv4TdSnZHsN1XIdizuKxc48EB_ZVonZNUJJ1W5UiMrCENvFLn53UHxa_0O5j5a6TZFj0oJdmQrRDM5l8TUZ5eafPkT45RrIEEZgQtpbcMd4542ekkX4XhJ94gJamvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbwS4eCILTyFIPGNDFcQiKRoebJMJhw5NGCIbpyQKowVlWMvZ5asWG47dcv8eDdY4okpBrnr8i8Xsh1twHvuxVoqfstmJkO6ngiNE5ySZpgjs0RfoE1bFrMr-3l_pGJ147HaRxkyygXCUON0ALon2PhEaESYk6Jwj-gzD5S-uzf8ngS4Jyt4aAQAf0syhb9x0pXJw6FgPeDWldr5NooPDbXQqTIIm13uyuKqIoqylNQPNEeY2zMueZnGwLLq5T0J4OAcWP4qj6fGS60tkJyDIguPEzU_QWn3JZWjFcuC2IG9vCV7j8IlR4Gmaw48lyBWx5KGou5a63_yh4JvTYm_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL1REdRkoUxlI_kZerQFyrw1jy8gdqbp6GagY1gjCaTqoWjVtRUXn5EFJJ-ylzXRGsPwAzYu62EaLQN3b8JMMCd8_nMGUuKgf88-HaYvYmt-2zYYa2DRgeXLUrRn0rXTBe6GJvEop0uGbbMRCegj1Po2MgEG5N9mg9l2RPhha6txk8lrZmrPBxAXfrR-HoggdllTs7mQR4Nlf2jmpzy1T_0K_Wydam4wB4bkhC9QwMDmRA3G7Fl-ZhB_4bClGAlzNTZCq4RT1hQX88wAMhRECNjmKbDFb2lpQ78R5brzmTNv8e9QGZslg01uQywrQJEsTlMB3HtClKXy1QxRTW9kKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTd3jMJO7_EJnP2kAqyLDXfBgiWlpxRJPj7dPo6hrhWx35PIPmCY0FKciwDAgfv3kX1yT0_198jAcxQtscJYD9JQCrSBBpLj49QEgF2R-MQqJpYJvyP8yF8OnlvMA3OJOJCtKmUwh5SmjpBrCMm1UmA92Vhjtn22GlNRAZLxJdf161znf_ObeE89bUG3mxlzzd3WUAQ1Ec-6i7RvNA3G0exAg7NQX9sKJbx3_UWPTYukSpbPPy2r961dgBDhBXZ3DUyQtjBijlCFEVGRuqHKLdifZkGZteTC7lJxnMuhKzMzYudIiI54TMInOjveNyYHu7pCBC6AmWjjQgwqP5h_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNrdSNEksQzfHV5MH6drfRInKY11ljO7i7OJ1wQPZnGmI4-RvARv0Goqb1toVGedYum4BTO56uZtwczMe-VkcbdTvXxJJusLWRrD3zgVaIXajz0rI0QuKGwFYqmR4IrYYuoVz3UiPlvPdxoDHgFuE0xSLlHdjy1CPDvm1IQh_V0R9N4o7cGX6w7lGfWfKzp6ggTyB0ipYinMWh95HTLRDpdwwf-jquz85dqANMQzAdXHo3aqQFxoJ4yXjZ9mdVSkeqqqWpcBw0uDBj2RUM1NZ6HpwSB1AMPyZQH5qp-Jcjc_yKXAMMT2O-pnw0tdR5RhTgpnoxN-X8gWpjIrdEkQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJocXYPGSXjzONFMfu2cpy_9G4aohR_9MWUcUgU0gYGXje0V_Aydt5JjUOjZVsDw3f9l3s2aSIFcTvy6WXbOjPr2W-GIlKskmb_XbI_q0jyR7N_zwpJULBnCH0PFG2IIMSZdGVCWQBuJSuYAeVruYX_G-Umiup3dcAnlcHIVB55KvEPOPJZCP_T_BCFRKvA3AAvll-qt1YeDvswg6hnGlYoYr4JNl-c3zfePBuhHs0o6QGkaTak53ZKwhzjEXc30ub4r-3N9mScs-VtzJc0mmm0EoeDRkLbydJnKs_M6UODauxH9qMPNg_M9pq2wbd4nJSBcUnmhIH4ll8SrqY7qoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwK5WXVzwgd8gHetl1fmeJYPMbvywmxSF1Wr9kR_-awwEN3cofO0HJgpM7OjdrcatC_cFqyz8bn61xK9_kUVVQb6h7GE_4F5UBZSKrHoa1NyQJfc5IU7NDmFUG6cYe-IM6Icyb1ZsU7OQtdeRnE4giHQwXi16fZFVcaYW8MVJV3bSpOTPt4Bs_mT62whB-LPub834aODSt33H4QbysTGEfB0FE7iFe-Ix_FJceSzp35H3bsAAdDkChcXMXiCBVOVRAeMSMPsS04GbQ525d_9_rNPgTjZEIkc69h5-m5tmPWQPMQ0_pjQ4eCegKXe5uqoWlMU09K7EeTQibR_8czBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR6m7MauR0UmSrICtKsz6eq8AEZ2-3w0oQwI08c-A62CZvCHfMMO0nMWPE4PycKQxa28A4BBlrJp7nIapyidVhRtlQtX6diguYXwPmyznYfH6YMPRYRVS5gdkS-5En9C8P6SZIrllzxai7KKDVVNZPZnr-gKf_H33Se92hEVOAFOv4bKCqA-l_7JhjpOrRB4ltHu3WcuPMp8dFGBV1fUsjpb0CjB6sFvtB4wnYJZsTGNPFwV7h3y5GND01Z2recDn_lJCr-y6IGNf5RYHNPudxhJzEtZP1iPIli-9XlokMQKZOYi0oMDbZbRiGWwwiBv08RuD9C1S4D0eNhvv-9P_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKwWGdIMZdMYhty8HwWaM0WZ0Pc-Mj9wX4ghK9bj3W1QhvYaP2rKwG7mSeA_9mlrMKBzciYo_zu39bAbqcL06ha_N5Qk5AZguv0PkAmlfthp-p9IEKFCLfmXiDJXIcXrSkoWGLCxtzTgpxgdfTGoVYBoJUy7YnBbUOQXXLoiaaddOPaq5PAYUakMg7x1o1SDmNSXyt2hYfBYc7yBAMdeHR9g71j64v3zRupFlBkqS_MCnQGbju12PR9f2sxzVNDc5H1PHLZdUmiPB0UOwIwPHWIum3UG3wXxMrBkRT1SElEs0u_LXYIgagPRL6a6J7wHSUJ4kwbnWJfHBmfx10Iv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzKkszgq2EgkmAYRXtb_rXA3vbdNA4HlQ0AArtHdquv4F3er0K38mpDP4vGNuXghQ-6t9ZBXCuaCPgl4BOpjaNRzArE8jf6u2Cx6V6OR2vrcnjLaMwhIkuZw8KQSqBo4DgBPZ5v0TolFApuD7hLJT5DUTeN1QWLZCetSihOK4pmQrN4KFJqXkZqcce9Dsufrdd2Kq_QoxgeKqQcFc2lqhreZSRi7LFZpN9LxtkUTsJIS0-LqcJ2JWZpreYMiJTam4Uubhe0qZSLN7rtsVbsZxFTUdtcWtvXMnpKklfroSCKWkpuhm4DHntLU-9DAld-1Zv_pVS6ePQOadWcsUg2HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUi_80EAI6U8RK3CxnWhqRu174oJFNmoF5T9xpQY0UwEXlnkxj4ZPqjPB3oMEXyD1niHmr0KHwlZFEvV3HBYBhteIo41I87qh51QyTKna_qEjkJcAILeXDzRQj8TIR_0vlanQiMHPlnVrZR0VnOswb4J8Ehm7WW2omdfKpVgVANYM2D1J8CyJ0aCl_0DRo9qLw3jjsW7U5EfcLPozZliPHlyOrWWFdtOMgOo9md_s5TRHFtjxZyplVRytmmvWcDOhKU5KLsLp72uq4Vc6isZ-cAOCnq7JNVZAEdhy40vTf-_laaEK8PfMgAzdN9pYQUUaPon2ly79vJDeXNMJntZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCygH-2CHUevTIS5u2VhoehO3lHeQvxcYnYcFxxRYQU6_FWV_b6HMYkIG0aw-GTpjS03bM9xq8PrpIYOM9NN--j2_DW3PSOtNa-vg_yMqfbYX3Lz3Jzy52coXwchmvUgOyvl0MF_EPq9Cxwe7DgMmXqpYTCL1eNlpGwYF5D2Y3eYp2qrmqC14d7MTX8MRIyoHdqsZvR0dqHYRJFe7KItu5P9wL3Kw0haM6oC3-IsLQgo812Q_7Mua_us9ovpXTP_Q9F-3MO0YvCqayYTnMf1R2gUAvs9LtFq2D3ckZEK6nJpfQ-RukzKJC63yloBWxZziDC9_fbuaqOg4Xq1SsCf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=P30E0kGPgOfHu6s-EN4CI9RWSS3W7k52_mlEnbiFQUBfCg1i7Gt8hcoBhuKZLYrl1opBRA4A7gbQkIRBXAE-QKeys0tFwU_XdaCIrqlTQub0WiN_ZInmVJto7IU0lzBJ7zN5vq0nKdSEAfXGunuaGy7UBd7Adt0-2wZxBG5w7aJQUOEyfoDsbwVA4xmhaq9JQYajOOvGaWu1RZz6eNvcdUFAULpS2t9-skOk2dkXadFLhAjXh8dSrSYOzIhCTVAMdUTQTSPDadZKAHP5DbULccWEfzbwce6cWe2_wK4aUqr0SNtU-Z-9DvBUlSA7j8-sXOocuEGHZ_n8Wb1QJgxfEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=P30E0kGPgOfHu6s-EN4CI9RWSS3W7k52_mlEnbiFQUBfCg1i7Gt8hcoBhuKZLYrl1opBRA4A7gbQkIRBXAE-QKeys0tFwU_XdaCIrqlTQub0WiN_ZInmVJto7IU0lzBJ7zN5vq0nKdSEAfXGunuaGy7UBd7Adt0-2wZxBG5w7aJQUOEyfoDsbwVA4xmhaq9JQYajOOvGaWu1RZz6eNvcdUFAULpS2t9-skOk2dkXadFLhAjXh8dSrSYOzIhCTVAMdUTQTSPDadZKAHP5DbULccWEfzbwce6cWe2_wK4aUqr0SNtU-Z-9DvBUlSA7j8-sXOocuEGHZ_n8Wb1QJgxfEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsnDBLtWxffrpehkPawCp5mD3NeOYSwzGIAI4xuTh2oGlWL2_aYd15lr3Fx0eC4SBD_TCz3ykV_4B56zWT-0Glvmu4CMvLRmsrSdG9j_-MXhgm7PJ9KBxkYdljBB66TcT4UnbBW_nZY3ck4XBjk9ujl923e8cqXO1TLZdNpZ8nrk2PCGHEZCIXNX5dlJeTjs3OIe-ddsCOY9OsC147g3zL644oUK8wS8JGU48meT2yyDRa-f2-e5huT3A86fTZMfIrOU8o0Fvba_lh5zzgI1hVkn8TeZSxOY-ZCQtw6QjAo4_tOSy8ktUaM6w7T4WeYrWWxHUzgM2c9D5iZhKg1o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=qyIRqjv8PRUYi22FgcRrTLWTB7XAJQiu7s9CROsqQmPpi3_ZSdHKMzVYHWn9LY4MYRHmj7Ip0T3IpGQrVklyIAvDrpUivml-HS7OBKehlSv3d5usmlMvxehZtIWM3k2RKD487rPiDrG02umWBK5exzP-sXzP6DVzFO686JxtICoPuG9ZfBSjwiEZt5lqVhp_cgk76Cm8Fbt_QmUSprYDMiY18Tbu9rYsRGjg850EXXiymlh5tA3COk7jcSA8pjytrVvRdyXBXqRBCgnPbCvjGO2_WSFWG5WbF0CcPy0fXHwHHpMvuUY5Ujlpi1AYn4OWmD0-q8KkoLmUr4XbAnxdrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=qyIRqjv8PRUYi22FgcRrTLWTB7XAJQiu7s9CROsqQmPpi3_ZSdHKMzVYHWn9LY4MYRHmj7Ip0T3IpGQrVklyIAvDrpUivml-HS7OBKehlSv3d5usmlMvxehZtIWM3k2RKD487rPiDrG02umWBK5exzP-sXzP6DVzFO686JxtICoPuG9ZfBSjwiEZt5lqVhp_cgk76Cm8Fbt_QmUSprYDMiY18Tbu9rYsRGjg850EXXiymlh5tA3COk7jcSA8pjytrVvRdyXBXqRBCgnPbCvjGO2_WSFWG5WbF0CcPy0fXHwHHpMvuUY5Ujlpi1AYn4OWmD0-q8KkoLmUr4XbAnxdrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA8qUI6YwokDeCoqyjKXWR8Yyp4DaVTcx4SFr8S1lU5yATBvqgBVz6wMD8Ajz8jRdVXVrEvGy2HtHOKcvdpxfHnK4yqhKuqr5-ZcJABo4JhjaZN7en30Q0uZkGlcMzo53SJaNSEI5cp68ElyJWnaHWhmT8fjYhycQJTITahJLkGkJmsyM6cORfpsLbIt98qPOf-4lNIJb5qdVyBXFEpD9HQd5CIU1sI0pt30vZnNI5PElplvdKkkAPYTJ-SRyCfVUIy1GNRjsVFvhVKwQdN6wlGTgVnfB19NAQLSjyZVDtMmLbSX9ArXwmOf8zihqrpxI2keKDesf3vZxIxOLPzgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=AgKbHJBqXIf2gXdYGMWl3f2ug_MxNol1iqNXGnfDpbHtazIXltrxvy4zXgOgisCxmmawIsbUYW-F1BfoRvs1bw24zRNJejq_5_oSPt3JLt9UbK2yWoaYdJUQR1QGBWsBz74-oU96Ycay0_PNeWOaD7KhG3gCC4oWC-NvKmcfyz6d6SbN6iIYlQB2HGpt2tmLyETSOonB8k-UND-qBxZ42wUZEw-sfrIQIwBypXk4OgvkNw5cl8eqgV8hBjt_krhrjJfvb4jzF3Wg5LC9zUaRVigVqc7x5axYIT1B4Rzl1XbFkN9Cw7LA-ZhwJe6xsoHSpITVpNOCmai_KIXk7Opb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=AgKbHJBqXIf2gXdYGMWl3f2ug_MxNol1iqNXGnfDpbHtazIXltrxvy4zXgOgisCxmmawIsbUYW-F1BfoRvs1bw24zRNJejq_5_oSPt3JLt9UbK2yWoaYdJUQR1QGBWsBz74-oU96Ycay0_PNeWOaD7KhG3gCC4oWC-NvKmcfyz6d6SbN6iIYlQB2HGpt2tmLyETSOonB8k-UND-qBxZ42wUZEw-sfrIQIwBypXk4OgvkNw5cl8eqgV8hBjt_krhrjJfvb4jzF3Wg5LC9zUaRVigVqc7x5axYIT1B4Rzl1XbFkN9Cw7LA-ZhwJe6xsoHSpITVpNOCmai_KIXk7Opb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
