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
<img src="https://cdn4.telesco.pe/file/ZUsz_fEF3Tt2LFt_LgOT9qr953nSkdOW5C5aytZwkl8HnqGj9QIbC8goSd_UIm7nqvjpgjqwj8ZwoywpH9h7OCDSe9-EatIAU72Qa722XJcm-p-6tvQPB_lbFKh5sxcRWVPoogtFj8kehQ58eKkBO1FJTIKFBdB3mm2R3aUD4SeHFWSO_cIBOMBgn8lnnMP5dYYgSZr4_dIgH-5D9sjT7RBLO-sClFLH8JNNZQem5tSCvCRzlwq4gtB18QbN2gimMv07UKFWEMXUJCPBy_6Wo02vSBxX5JYUB6c9qQPxULzVfe-yjW64KAsRHedz5xlT_Uw4uk5oXJSMkOPiWs_EyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 193K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_VuomEpJXl_PzaJjNwzY0eMv3pG1UZHynylcdLfoKN7VUgvahRso1lCGLUiIHKcvPQ0AffgTiGGkGFokcYuseMnZp-3hUG_AWUt7CmD-h21BPCoVm8Iz-BAsakntD4ifAw54zNLFqJZjO0BAQnWNkN334ibq7fzHQPuQW0oq6WHQmK44fbyryaIEIdWgDbVW3hvhI3mdhzbHYzYUsP4XkAcnQXSY29IzVFbzBZlKeMKyKf09XZbi95LgB5aYKhBRAannYLYAH-e-2uGXrZAnPc3sjieB1_ch1nymwdVH-Y4mo_7njNZeml21VqKVLPibo3XeOujNvh-4IyoIlq4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/funhiphop/80579" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMA04YrQwDmqMOFPPPZ-RyeRKumOXNlhZfUJDo9oTNLbVqTp3ALLdMFATYbfRMEzRWLUm-cyEU7P8K-Ia7IEyAMDndJxKJ7hAKloBsgv2uHOVfaOhPd9cAGwEJWO5yQ0ostG2iOO05Fl8NLDSm68mSqDx9E5XLmd6TI6q5N5YVULUkMrNYPsJAu89cabnCwfVokR740EhT6wzKKViAT0zxrXLyP9vSgkDlS8Ak97sgFdNgG_8hEZPQHzN3-ysKqCMs-0AR3xTygcax8zKCQZUwdl2G2_iHNmcbKRtpk5rUcHBDlEbSn1ARsaoj_PC7v1FdrYrA8omHpMOUegMkVq4n7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMA04YrQwDmqMOFPPPZ-RyeRKumOXNlhZfUJDo9oTNLbVqTp3ALLdMFATYbfRMEzRWLUm-cyEU7P8K-Ia7IEyAMDndJxKJ7hAKloBsgv2uHOVfaOhPd9cAGwEJWO5yQ0ostG2iOO05Fl8NLDSm68mSqDx9E5XLmd6TI6q5N5YVULUkMrNYPsJAu89cabnCwfVokR740EhT6wzKKViAT0zxrXLyP9vSgkDlS8Ak97sgFdNgG_8hEZPQHzN3-ysKqCMs-0AR3xTygcax8zKCQZUwdl2G2_iHNmcbKRtpk5rUcHBDlEbSn1ARsaoj_PC7v1FdrYrA8omHpMOUegMkVq4n7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
r27
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/funhiphop/80578" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توافق اونقدر خوب پیش رفته که بزودی هزاران شهروند آمریکایی مهاجرت میکنن به ایران، فقط لباس نظامی تنشونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/funhiphop/80577" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لاپورتا چی گفته باشه خوبه؟ گفته اگه داور خود فروخته نباشه اسپانیا قهرمان میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/80574" target="_blank">📅 17:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ولی بارسا جدی بین اینهمه کون بچه به دوتا بازیکن با تجربه مثل رودری و لاپورت نیاز داره</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/80573" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نقش من تو قهرمانی یورو و فینال جام جهانی اسپانیا با پدری تقریبا یه اندازه بوده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/80572" target="_blank">📅 16:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaj7wmsj01gaxLlh7bluhU1Q0wp6WwnkteNXYAN_UjD2umxBydEFFmEl1Yl3YuzNfDtDJVMcZHWjguaE14IDXgLXk6QZHltn3T9_CQWfoPKKwSXZRrEIk228tFK4Ic2ZxQVjrNRHeTsimirAvxaw046wfrGmFKE-_i-6aswOSsP-txoqFd4X1oQBvgz5mWLtorcbGK--xAuysXBFicDltxwTA8zkXxte-SOmteoe_-mCGVLo3FBXtuZ6hQAvOTEarTKiCyWMz9x_7FHXHhrzHT8SHB3Wu5qHyGubKIdnhIRnyaY3yAvuwD8UaZ6VlXpam5kPaT0K4CG98uILybSm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای مسی با بازیکنا کنونی بارسا یجور عجیبه انگار واقعا خودش پدرشونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/80571" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">باز خدارشکر این اتفاقات جنوب پیش اومد، وگرنه این وسط بازا لال میمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80570" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کل زندگیتونو ببندید رو حمله زمینی آمریکا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80569" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قیمت دلار هم شده 190، صدشو بزار تو جیبت ی نود بده بهمون تا آخر ماه پست میدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80567" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80566" target="_blank">📅 13:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پخش جومونگ شروع شده؟
اگه شروع شده لطفا ساعتش رو بگید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80565" target="_blank">📅 13:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRm5ZsFV2T_B4MWcQcVftsrm3EHLDxDZu9iR02sUZ1tgXWmezuPDGh1tR6OOsqjBAHxyPMmx-nT48nib6tKZaL_O-8xoydkNBIIeZt713BcviaZ-87_t7om5FYT-j8QJKkaDFoRMUzjosWC3v1uHRCVUcU_ZYfkvBGoIhLX1UD3LFAxpriiF34PYV2omTkkUAlMGvbHWndcN5jmzc-N9wiQk3OYts4nofedp1c3A65g8Fa1gCKxgjP0UJvyrnTxJ3ocGdEfUM5KMAg-Ht5N01BPsvrQLMY8F6qJErXfN-uM5BaFiz145nWkDKrDN_N15Ua2JVr5Wl0VJDsrV3r2J7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80564" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl-L1kIkGnyo68HggisJYgsTerAYcTnkTUBYF2PRny487iMfYc1QZBfS6sNKIa_0RRKPaVIzLhhebKaUcr7CCWU_yxImMfTzsSMGzLkFHfvRqs0pt5Gy1c3bETV8PBoKsnHuv8Nfveu8kOu-Z5_T79LkMQe3DWQBFk1Mohn1ZZFnZw2WPHOacJ8uYxrtpEqUS0dBMPSKp_7XX7h_0mKpZnaUHeN79fukyZsZ4ak9rSVOn3dD7HR5xQdmLRhaaFdKa3Ut-x4KmcETUycM4egiZMd6d4slzqcMNNC0pDotEPVqvbchUv4Ssv5_hLTsAzFQHUMInjEUXeZf99fF07RkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها راه شکست آرژانتین در فینال جام‌جهانی :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80563" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMBtIHauzgX_rgda-3YrHuOFhBVi3Vyjxuggnu-SJw1Fld0vA0X3xhkmG4YosZUH1JUOZXce_Oyv8MbD9A6m2CJuG4qpfdHDO2dOhqT_exSvQZBklNs-ZlzCTVxkctyXc7mQtoODcRUNJviVf1jskkJCeJx6K7JFS1A1yavYUqYGWwGNL9Zkmgni-qweTCv1LaYjE2ci9BD_fv5sPt27BPR0iX_lfd2fdbFicSyAesT1I0Mkr4hNW_H44ELLbitjs1-6KmjulWgsVD0slR6qDKPr3i1wzc5igBwa1e4892Hn5us5jnJIjOn4sFTHNHKPVea_7Xa4oTkm7_GkJ9mK62oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMBtIHauzgX_rgda-3YrHuOFhBVi3Vyjxuggnu-SJw1Fld0vA0X3xhkmG4YosZUH1JUOZXce_Oyv8MbD9A6m2CJuG4qpfdHDO2dOhqT_exSvQZBklNs-ZlzCTVxkctyXc7mQtoODcRUNJviVf1jskkJCeJx6K7JFS1A1yavYUqYGWwGNL9Zkmgni-qweTCv1LaYjE2ci9BD_fv5sPt27BPR0iX_lfd2fdbFicSyAesT1I0Mkr4hNW_H44ELLbitjs1-6KmjulWgsVD0slR6qDKPr3i1wzc5igBwa1e4892Hn5us5jnJIjOn4sFTHNHKPVea_7Xa4oTkm7_GkJ9mK62oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
r26
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80562" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الان این کصخل با همین توضیحات میزنه انتخابات میان دوره ای رو لغو میکنه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80561" target="_blank">📅 04:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اون وسط گفت ایرانم تلاش میکنه انتخابات آمریکا رو دستکاری کنه که همین که اسم ایرانو شنیدم پاره شدم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80560" target="_blank">📅 04:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یسری مدارکم منتشر کرد که انتخابات ۲۰۲۰ و انتخابات ونزوئلا دستکاری شده به وسیله چین و تکنولوژی هاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80559" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80558" target="_blank">📅 04:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO2wEec55I8UuKX7nO5iJYnbrwm1D-G2MvRmihbbaQMAFbDR-yPsoYEB3sbZVD6Wx0q3FGBfcS2mRtCBThExZqAMQuxYretCrJxmgKuQ66M_b3gQOmY-Zizzchz__uBR02WPpzonWhrDad8YZqyY3BaiLOOzvrTqj_47jQmWzUlcEWxwzfG6UVmQBAINvWwnoI0KVsP1VPPCPX2YNA4OxdU6DoAJ2FetosikvSsncEi5Qlarhi7k6gzxPswR7ViG_6ON7LzcWroLqDpWBamfh6eUwAgsQ2oILrk6wckySIwWfxu3kEEO1bk7Mooj3Vtec8FEzmzjxJDOZxw3g0RfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUWCrjs3BqwvEsNEYmlnwG7lXybbzyBp-WGUwnpac1pt8a9MQHuc5mmzB4L4uuJ6C0rikl89ed0qSBw651Oi0s_yslrqe8BZxAxNcSNwKjg62zqmbmE5Snyx685cYlTcxTNUl1L_gvJGy4i1hZBDpRRWEP2zyeqhZLU8s15sf7So_qtPAi2MXX9oeukw5GYBlbeM3caqutlM8_Y8Nw0sUAAofaL93J5VKCe2Id5v-uSnjdyAjPL41WlwktXcnqpvt-eAs421uS8KUCnUqwlaUrT7-XiqIJg7dlfMZ4bu6yy4LMnFJNjWdsroencK75iNJN7BMHh-EFhjYbZm8uJMHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متاسفانه فینال و رده‌بندی رسید به این دوتا کون بچه، فغانی هم کلا به دنیای داوری گودبای داد قراره کارشناسیو ادامه بده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80556" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80555" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تنگه رو وا نکرده پس فرستاد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80554" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی رفت مذاکره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80553" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80552" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا: ایران کنترل تنگه هرمز رو در اختیار نداره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80551" target="_blank">📅 02:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186980592e.mp4?token=X8YVgXPOyYMwr2iIvBtUUrNwIP5F3cXK7skopJFxmyIaMe7Z3nP-1SKJAvrAxLMpfq6xLoym-Pb0tLTbbjrYOVKcOssO_10UPbDmjwNxRTXAYVer6SrsbcHcx2jUt_5CNsvLM3FRzCOSa8LiwZXTA35qzC5VaDCuW4tgS3j0GP7kx406IjuI2NveSZwsGbC2AYsMfFxvz-ZohD-SCOacBVaJlQCJw1OH9p3xqyhKXQzka3Xo8oSp381IQSYOFD2pVbTxN_f7ECl1scaZlfs5AaL_qiWZ2Z65xT5D48Ov6mgvVC0NS6M4jve_ndC8NND9xVc36hni7Gisrkk5VxmtAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186980592e.mp4?token=X8YVgXPOyYMwr2iIvBtUUrNwIP5F3cXK7skopJFxmyIaMe7Z3nP-1SKJAvrAxLMpfq6xLoym-Pb0tLTbbjrYOVKcOssO_10UPbDmjwNxRTXAYVer6SrsbcHcx2jUt_5CNsvLM3FRzCOSa8LiwZXTA35qzC5VaDCuW4tgS3j0GP7kx406IjuI2NveSZwsGbC2AYsMfFxvz-ZohD-SCOacBVaJlQCJw1OH9p3xqyhKXQzka3Xo8oSp381IQSYOFD2pVbTxN_f7ECl1scaZlfs5AaL_qiWZ2Z65xT5D48Ov6mgvVC0NS6M4jve_ndC8NND9xVc36hni7Gisrkk5VxmtAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات سپاه به کویت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80550" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگه نتتون ضعیف شده وی پی ان عوض کنید توهمیا، فعلا خبری از قطعی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80549" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80548" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80547" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به لرستان هم حمله شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80546" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80544" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80543" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سازمان ملل بخاطر اتفاقات عادی خاورمیانه ناراحت شد و گفت تا اطلاع ثانوی قهرم بای.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80542" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">راستی تا وصلیم بگم کیرم تو نت بلاکس، از این اسم دیگه متنفرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80541" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حقیقتا میترسوم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80540" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آمریکا یکی از نفتکش های ایرانو با هلی برن توقیف کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80539" target="_blank">📅 01:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80538" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80537" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سجاد پسر تا نتارو قطع نکردن پول ویناکو بزن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80536" target="_blank">📅 00:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خطرناک تر از ناو آن جنگیست که اینترنت ها را قطع نمیکنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80535" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بابک زنجانی میخواد بمب اتمایی که از پاکستان خریده رو کنه.
بابک زنجانی: تا غافلگیری دشمنان چیزی مونده، صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80534" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80533" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80532" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرار بود زمستان سخت اروپا شروع بشه ولی تابستان کیری خاورمیانه شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80531" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یادش بخیر ی زمان چند نفر بودن میخواستن با ی سطل آب آمریکا و اسرائیلو نابود کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80529" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خط راه آهن بندر عباس مورد اصابت سنگین قرار گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80528" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه پل تو بندر عباس زدن که یکی از مسیرهای مهم ترانزیتی و لجستیکی جنوب کشور بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80527" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این عاقبت 47 سال مرگ بر آمریکا گفتن و ایدئولوژی خودتونه، بیخود گردن ما نندازید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80526" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکا هیچ غلطی نمیتونه بکنه ولی همه غلطارم اون داره میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80525" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب سی میلیون جانفدا، الان وقتشه، برید جنوب از کشور دفاع کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80524" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80523" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فرودگاه ایرانشهر بلوچستان هم زدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80522" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جنوب رو بازم دارن میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80521" target="_blank">📅 23:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از اونجایی که دیشب تهرانو زدن، الان تو جنگیم یا آتش بسه همچنان؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80520" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDLX8lqqfWjbiif2lMsulA8K6bcdL1XTuI8u1DQMdGgi0Q7B_sVVrFG2CtSwuLz0DBH-1hA54cK0ZhBDfPOudTO14X5tJhmN1I580m0W7bM3p1S-6U5Z4Tm6mUmakJLynXTUKPWoZwITx8nknHT3qI_dyo09IqIU-t9hK4EPmrsV_2hwRAa0nSqW6IW7oWIeFCE0T4qAg2oT6y1LH4tKAfTCQjacHZDP5B4Hw-iL_fpfJz_xeduiM7jcyjO-H-uBeWTVQvel0M8PM34STmfcmMfby3RMIDNg_U-3k6KiM-MhL-s7uHjIf3_q4Zmz69UTGzDjOo2wwYspzmkYRBwEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80519" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اهواز
@FunHipHop
| Rea</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80518" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با اعلام سنتکام دور جدید حملات علیه ایران شروع شد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80517" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG2PkKJv5jqNv3Ha2YEd7L6hlQr0QcXJ1obE5ea30QKYqM6-WXS25akni1ebB3QvjYifKaCxl2tdWgWUDPlXFbBUuOZXnRyui3hKXz8hlSnGPIdJaO9sf-YSotLEaqE9R7PU_7SLc8-m18Q6tNhtWva0tfLHFEawDWRHww9xjWsOPtyDjsb_2z1Xepjzw87gEjVSlDW_4AiGNG64K6mTvuUT6GC3AShaHvHbZTsK9adytWnqRqYTBJ17gO07T6gow6CbLncrofSuBy2obUegCC3PoBG-KfwjKoXa0e8TqiLMlndyQBcW3fvGIW--uI2R6iLBbE0n4JrLBA_pSGhzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام کارام هیته منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80516" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همان همیشگی (انفجار در بندرعباس)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80514" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=pZMnM7uF8jmV-HtJ-llgDkF3eIp9GlPFSkmEce238G_Sd6HREUYx6b4dE_T9GHZP5b8EQE6t1YCT3DgdafINUNRMITHlS6FTK-jhMj-LVkrVe8tt8Awwwq-gRXNhDW92l_Q0YF7rRIEsgFu_MeFQR2sW2JIcn7Ywa8aCOlkm6lp5LbLrM1g5C7x5sdxfXSpSAY5VyYjq0alv6ARN1dOAto9-e3Ai-S3e-Y2-R3mNtykMGeODKRKmscnPn9M1oDay9iF-1ymUAw2HYAGQr9-kfwRvTTXhiNhG-KdwXCZaSOkic7QiCJGxGXgfCgM2kXhG5eum-wowgMyRaPl9wX9XHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=pZMnM7uF8jmV-HtJ-llgDkF3eIp9GlPFSkmEce238G_Sd6HREUYx6b4dE_T9GHZP5b8EQE6t1YCT3DgdafINUNRMITHlS6FTK-jhMj-LVkrVe8tt8Awwwq-gRXNhDW92l_Q0YF7rRIEsgFu_MeFQR2sW2JIcn7Ywa8aCOlkm6lp5LbLrM1g5C7x5sdxfXSpSAY5VyYjq0alv6ARN1dOAto9-e3Ai-S3e-Y2-R3mNtykMGeODKRKmscnPn9M1oDay9iF-1ymUAw2HYAGQr9-kfwRvTTXhiNhG-KdwXCZaSOkic7QiCJGxGXgfCgM2kXhG5eum-wowgMyRaPl9wX9XHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80513" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfNO0AmJyhAi9kIYdhcxxBc1Q88zFFCF_kzgU1Tq832UuBOq_BFpveRR-J6EIH-Ki91niYxS2g3Yc_FulG0gIdyIX8A7-Sgb17qnGyskXt8Au47xhwjNe_arr-EcJ-2CorHTzDs1lWdkkoDsh_-dp_bI3U1SgdLw3Ccr6DciamN6icrkMs_wCB31yALHEHP96aMcZOSLulB6CHkzkiBLPO9PNJLIR-TOSsoWtkKrzJeQHijOrNt4gpvUIULd0fB0I9-mwYJYnE6_rLKXiNG37VE4Pb6F_4eRqKFUT5_p5nTa3fHtQWAS-QbgARaXgUXVmICwHBBOymIILxAq-NM7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g25
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80512" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طرح استیضاح وزیر آموزش و پرورش رو یه نماینده ثبت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80511" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiqxfOHQ4eO2iKz8vl0iuqvjxZ67UzEiwRLtnZ7pBSnKBhoEr_QhBSllFBF3Yf57qKA2hEaKjw1lXaybe2fjnSZ32AO6v48W39tx0OTbup9pokBNcioUVq2JktogTH1xVRQXznvJDEvW-PKxLrKh5MmqaheEF-HeuJM5VvcF1Xq_SPlMrYwcHdziqxNz5tNAo60JfI5EPd69CdmA2FVCKn-zMoWNd35Cl2J8w7AnEVdntiYNvIyt2FqPdwVOtyXGVdIBBk_CjNZdfZnGtSE4vNjY1NW31lCmE9Dj6oQpxZfV7OrHVdtBHUvf4GXFTMrGX1KTjf6MJjY0b2tbrIQ08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل برد آرژانتین:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80510" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=D5wHDGpAzksNuxrVogSmQR3hSraOFOkPOU_trp5P6DCBUUbFU-0UASyZOfZyCts7NnUWpxAxnpQJBJpSPM9_Brvy1GNnGsfWqsKJ4LFoCvGgDHNAC-1XP8hqDwSO6bCkJGiOwEHbH1TIgN66dHUhcjPLTh8IRJxVg8GHIX-DdXteNXqVYDqxWDOGJWEZmcd8BBePsKi-PLkvX0LGIlNu1ebDL_O9W7UtbAO3rtP0gNkgvVOP_FnH0dcMQANV40zz1H9ayP7hLHO-RtWXCO8hJg2Yi9N1G7ZoRQyZRotpjTyypDCQgF9cL2pLeKcK2aPeB7lAbWcVY4KIzSOFDnho5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=D5wHDGpAzksNuxrVogSmQR3hSraOFOkPOU_trp5P6DCBUUbFU-0UASyZOfZyCts7NnUWpxAxnpQJBJpSPM9_Brvy1GNnGsfWqsKJ4LFoCvGgDHNAC-1XP8hqDwSO6bCkJGiOwEHbH1TIgN66dHUhcjPLTh8IRJxVg8GHIX-DdXteNXqVYDqxWDOGJWEZmcd8BBePsKi-PLkvX0LGIlNu1ebDL_O9W7UtbAO3rtP0gNkgvVOP_FnH0dcMQANV40zz1H9ayP7hLHO-RtWXCO8hJg2Yi9N1G7ZoRQyZRotpjTyypDCQgF9cL2pLeKcK2aPeB7lAbWcVY4KIzSOFDnho5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستار هدایت خواه نماینده مجلس، که توی تجمات شبانه کلاه خودشو در آورد گ گفت هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80509" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام همون همیشگی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80508" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ویلسون دیشب عرق لندنی خورده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80507" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=fzQ7oRPRMRfzMCVyEwN6_F1SE_2MCJh76D9xJeTY_SJDX3faG-K7iyNUadzG1POjrsGZgWx_Dc64ecRFGDNh7rze2ogt5pGp3QX38xTYMjXpsSP08jk92H16CE0J0VXIKgOGiV1PapOl7VSH7eyNSuN05oA5GT8-qtr52vSexvYCqmGnmGtqIE7vKWMf5HwYSgAmA7qpuL8FUnO_NampsgRehClxyIs3OKg0JLNINXUl1kdLfKHVll4bBpoEOwHjEFc0uKfZbRuBhTQfK6UnrerPX0W8BUKoLVB4kpO2OMt-R3kGMvod_rSMxTr6KkzWtWDjvIClWWeL_IpEQm7lYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=fzQ7oRPRMRfzMCVyEwN6_F1SE_2MCJh76D9xJeTY_SJDX3faG-K7iyNUadzG1POjrsGZgWx_Dc64ecRFGDNh7rze2ogt5pGp3QX38xTYMjXpsSP08jk92H16CE0J0VXIKgOGiV1PapOl7VSH7eyNSuN05oA5GT8-qtr52vSexvYCqmGnmGtqIE7vKWMf5HwYSgAmA7qpuL8FUnO_NampsgRehClxyIs3OKg0JLNINXUl1kdLfKHVll4bBpoEOwHjEFc0uKfZbRuBhTQfK6UnrerPX0W8BUKoLVB4kpO2OMt-R3kGMvod_rSMxTr6KkzWtWDjvIClWWeL_IpEQm7lYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80506" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80505" target="_blank">📅 15:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ی زمانی غزه و لبنان و سوریه رو سر اینکه بی در و پیکرن و هر شب بهشون حمله میشد مسخره میکردیم و در مقابل کلی منت میذاشتن که عوضش امنیت داریم، اینم از امنیتتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80504" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نت شمام ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80503" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عجب امتحان بخوانیم و بنویسیم سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80502" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لطفا فحش های جدید بکار ببرید
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80501" target="_blank">📅 12:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW9JmCYTnVmgOSVlZTvwAsdW7o8Di-PsDuuxDmNJ05ze10yshZ_kpN5s4ySjj5jTpf4ID6ff9issy1itaS1LopEP1VmQ91zj-Z1E2CKoT29aIOlZj6uYTrtDGWQG6xyrMxJPAh8k5XEV6h4PPBiD6vB0o671AftWnZb0Q9NMpqdZJMdrxFV6iuxWKk1s7PrpIM_K5t49Bl_63ufAs5PX13XopdxhXKHmkqK1bheMTkhwmTUpsE5qKVMdJ_qLIlwrpoJ6FC8VGt10aFDLJJN9bV-VixBcB6SNjVQbUl0d_aQ5ik97D0979cgPzDr2xMt6aAzzBNlLW6O-W0VOT-cXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم پول ویناکو ندی بدبختت میکنه خوددانی  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80500" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwadDHewxhBh040mOK7Wb0v7tX0UKISpU5bG47oz5jX69Sw4qEj3qB6X6bQWpw0hX1l22FLTEST8NOiSZT1ilLp5TkSWMkgiWszPx8BHLaTqV4-eBkELD1ZDr30qe719eLva3dl10OAq_mob0bqlyxGVgT-w9fqujl-QPJuPj6Z4zi-_MG9mFhHMDNgOSMU3ORRo-r2VaKuxUa0SdVS_7Vg9InNwQHzHpKX-wQJoNB1cep4dBrlj5K8hqyqcJ2fRzBITva0_suAFbpz9opjJEwgaTMVRRwuiEN4MZkL-MpTVwaZisl4m7wVVp09qDjWAx9G6b62z73zHti9YgKD7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80499" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=XhfBfdzQ3eeNzpKXPzdijCt42A_g0nGA1Ctj47AfUmM61CH7OVVVjVtD_8HqXGWfODQSJ4Ff2_n-iy9U3qduYAmnlREnA4NEfSOI_GC-vH2q6QATyMv1VZoVNQGh7KR270GCMCk_e-WmgOYSa8GPNRNUVDcfVJixmCjXw-oaVrf9Dr0pcC6ad4UC6JPcXmVnmnG3lQ6CKyy7x14YdH5oBoRAAF8fcqd_ufBptbQBov2iRJB3302JcB5BchAsXAjeS6jhYwAYAYif7WWDOb9CU6gkH3V5Q18BDzR-TPenstkqBtUtU9Cr84KfNbwDJa2L2YV4_i7htgp2FJRx7dHWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=XhfBfdzQ3eeNzpKXPzdijCt42A_g0nGA1Ctj47AfUmM61CH7OVVVjVtD_8HqXGWfODQSJ4Ff2_n-iy9U3qduYAmnlREnA4NEfSOI_GC-vH2q6QATyMv1VZoVNQGh7KR270GCMCk_e-WmgOYSa8GPNRNUVDcfVJixmCjXw-oaVrf9Dr0pcC6ad4UC6JPcXmVnmnG3lQ6CKyy7x14YdH5oBoRAAF8fcqd_ufBptbQBov2iRJB3302JcB5BchAsXAjeS6jhYwAYAYif7WWDOb9CU6gkH3V5Q18BDzR-TPenstkqBtUtU9Cr84KfNbwDJa2L2YV4_i7htgp2FJRx7dHWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتکشم زدن تازه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80496" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxxviwjU2nTeGvIFAzd0mjgQPbhP7-314Qnxeq4WA_U42n6ozkVKhGHKe4gjn31ZTmOaif1EdlXBC6_yLThLj-Q4bXL4zdxAccS_8rECg6nt2DDAzHVzNT9GObksnDFRtZ5LXKnmLCnhNfLqvL01QoD6sZj8HLF4o-Zb13yczSOYK6Sz6aZgFSIEmcLKIAMIwocAFGTkvgPkvovaUPbY7SAX39NLKAfnpbSeyzXMXfVcmWACGRz72MNd0ZEX0Z_SlGDCqaYdFvY6SfqrjWlmkJrxLwcm4-710WyEUtGOZqBxriAJyqaSVN8jS3vaAJ2lsqSZCGLjqwxldfd4MPSfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بخدا بلینگام بدبخت داشت خطایی که انزو روش انجام داده رو تعریف میکرد، گاییدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80495" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فکر کن خاورمیانه چقدر پیشرفت کرده که دیگه تا خودت صدای انفجار رو نشنوی حال نمیده و هنوز جنگ حساب نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80494" target="_blank">📅 04:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/80486" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شاهی علی الحساب یه‌مدت شماره ناشناس جواب نده
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTWrQRwVrAAUsJBrrwFOz4dMXtcPS7Q2g_Euz17ycDsMusjBQW4FIeXuInIqs7W1P_Kd3QEAbnoQmSDagovL_-poW5Wi_xKCfi_AaPJ6MSwwtgTP9Fv05td3rJxGBBJlr4Vz7ZtNVE8UYG8MppI5WD2g5wQGzDyIuOjomyoYN_ZVU2vqRMgJAjKykcdVQxKra6A1X8LgI3CJNPXmbHTtj3MGlHlmSJ9a1chs4n9lNqXnwsUhDJGXZIKQw_iD47uYUtU2leYpnaUJsvpOwBQPURsYBSeOL8KZjupQgOyKlokQNT_6Lj2XBkCkmYDV-KcxEAqjzDz6_a_FDO3eYWohXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmF1cgOEelNq47KMV24Nmof-xA6qIQM37iTYATBbGMMPCtAnNMFqmUuRd-wVLC_s_V-awHIjFcD2MJ65oBvV9VkQhhpujFAkS7_7OwjI4_W6BIhG1_l9dvwcOmnVLAAqi6c6p4T38Bsog4vYCJ-g8aLdHIXem0VaLukEMqLO_hjRcFAV5vsBRyIxXJT_j3VVkblKE6zhjPi2zQIWuwu6UcdsWWxxcI2t3PIRoiSF7S0br89lV8CVZkgjOXHQ0nSgBtOjOUk6xh-5UMXVFYZRO8Z-4m8s13XWki70YR0A6cx-8QkYzU6F7-VJ5fqewEEZwZZ8IX91xZB7nQLo4A0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtW06ic6xSjrjmN20CfHwT2o7XeIDjoc3CnVTeLL2tbibNBFJt7UQ_gjjVwYIFZ_wn-VEckwjJjY6cBkcjO0s7w76Ro7rufZmWhK0ISYrKin266cqbfinVhwx0nwV52bOWbdPTt-01qPEx6_nE2y0EZhX1JSRDmPnN-2Hqa5b1H6rIr_MxUwaR0kHcN_U0uYXEYIn2-XzF9gWdvbfVto6kW7nABYHKPW3Oc8gNNjekxq5QSBoe10a355Dx5Un1CysCEIxHLGg2bF57M0gDAjLw74FhYpSbAdhcUbDfx_QczSYMYRPQIxiuwUeuA8sJFyckUrX3I-3-hL2Y6jUuqtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbWQsAJch0dfJFHfa7A9PI5ul3AD68RxSPy6-aORw1A2G08Y8iujCb9XiXXzw_VaESVa_a4s8aAIfRpGV4MncVd-bGtBx9gjZaEEyiv_NhgOA_zpiGP6NLzdzpp5m6fyRVc0ZNtEX_Udr2ECcUJoWQTu5bydYjWVx4DIZcIo65r8qjYTo8v5PjTvDlWCwaWVea-47qttFAgbuxFhPYS9bBAsUGlQ0opqMuW2uWA9xK1qsoRrbF2uYCNeLakAIoi_60_LJXw5czg0IvYST-6CD30nI-0n4OU5DnKS7QFlJDnZGLMQFg1fWHAb1kabI_MWj0PPcX2ncaxDxChrTgZQ0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یا عباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80476" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNZ-3ub2TWGHuH4b2Ir_dRsTKVJG0LrGKNiqtcxfNOI2u1ukNRDcP0UD3eVTrnTjmuqfqzXSRtOfMj6cOy53GRtCgfZ-ONuWEKvCVvozLCXT90MCdLvgOPPCq1Gg4k5zUV4PzMgaumqN9qWKSztPAG8F6RmFXh659pCdRnKg-VsYaGmifwIkRZG7ax-86w96YI3Qd1U9KWNsx7cT8I1h6V8A8NPmVcOkyeFRoDmBfW09HBEPPS1sJvONrTPu823Q6wZFasQ2rl-9phNAxJVBiQ7Ayy_EWX6N-hAXDMNwrpUFuETni7MAlE56dScDP2pckvqIssCM0pb8sgxcrd_6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزا جان ببخشید
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80474" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رونالدو فنای عزیز صحبت کوتاهی دارم،
جدای از اینکه جام رو یا یامال میبره بالای سرش یا مسی
باید خدمتتون عرض کنم که مسی اقای گل و پاس گل جام جهانی میشه و توپ طلای بعدی رو بهش میدن.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80473" target="_blank">📅 00:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ساکت شید شبهه علی دایی نواخته
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80472" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromvahid</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrevWUZMuIE98zHOtQJQZZh-H_1LuLcVSj2rQcxW8cAIncakAAhLq71RRXzVr1I2gvVCzGSVkTp9UDTOAh5WHGYGKG9uf0iHULZhU7cDYsqG87X4WMIY7hHhSUFWDL1uLam4nHdgvD0CteVNAKEj5MfiVwEsjtI0bqrfU_S4VnG85OgatEZHpi4qqKNDpZQUEjEx9EEbOVvaGW574zszuVzpz7xF1cVI9KRXpux37VYMlOLnzltL0LklNO46fLMtimaOPt1j9389y7eJmZ8awkhv6Zhik5NTnM-sHBO4s2rem6MxFY_SbtmXL15PZnT_97KSV4Iy_rMaw75sFJza9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم ی سری جذاب و خوش چهره ، جلوی این گوژپشت اوتیستیک کم اوردن
😔</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80471" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا ۲۰۱۸ رونالدو رقیب اصلی مسی بود
از ۲۰۱۸ تا ۲۰۲۵ امباپه
از ۲۰۲۶ به اینور هم یامال
تو دیگه کی هستی پروردگار فوتبال
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80470" target="_blank">📅 00:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان بخدا کلیدی ترین بازیکن اسپانیا رودریه، چرا انقدر عکس یامالی که تعداد خطاهایی که برای اسپانیا تو جام جهانی گرفته از گل و پاس گلاش بیشتره رو میزارید رو پوسترا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80459" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80458">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صداسیما: شدت انفجار ها در اهواز بالاست، در خانه ها بمانید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80458" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80457">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سجاد شاهی ویناک گفت پولو ازت بگیریم بدیم بهش واقعیت</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80457" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انگلیس عزیز تو امشب به صورت استثنا فوتبالو از دست آرژانتین نجات بده ما فینال از اسپانیا درخواست میکنیم مجددا فوتبالو از دست شما نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80456" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
