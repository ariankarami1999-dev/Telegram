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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 22:01:32</div>
<hr>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگه خدایی نکرده زبونم لال یک درصد اتفاقی افتاد خواستم از همین الان تاکید و یادآوری کنم که این جزایر ما خواهند بود که سربازان آمریکایی رو محکم درون خودشون جا می‌دن و به عبارتی به اسارت می‌گیرن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/funhiphop/80590" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCOI-6mh5NjwFoAy0c6dGx8TU8ZkKvnmwwLKzLValIilSmLgHDBdyukcJMEf7R5RuQ3nrmL-hzgr24yYAfl1pKK0SVF7OzlvnfR7Lfa8PorebW-WlqVJNysc1F4kyd2I0Zrne6B1DCg-ceQwA8uG-J1fvPgS23ZV14MLdYsNHE4oRllz0nM--DZBlfCKsG-0M1O6jwqqmySK7Y6q0XyhnzUqxrXtyIE51sPNGy8V6I5FkvlRlFaIYQ9NzDZCipIX3cBLSub1vRjCdorGDn-wZRMZGoWYCZcyKCsRsfTk9GFfygn7h-rfPHoHs_VfB2ga07LNM7CIXJutup5c_0gynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین هم رفته بوده اسپانیا ساشا سبحانی رو ببینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/80589" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVy12dwy5xUangYBqZ4y4ZDTlSNxCJAamcm5kGqGKxkHCeMgppLtjSNZFBHaP0g9UWFpcfJw2Xt3S6iHeqGeGU77xjGRKJPB950QO0rGB2BQ9eGaSf1zi4uAjxkzWvIKmeAwCPQDDYpYPJIm-9eUQTqCW9NeHSaFRfg1bjHhxI2yQRrSmgbNInZmEmlwRLbXy8rb-JFqV1L934ftgWuqNY8YiRM1BAPrS38FCtfrAcI8dhZKmVwo944HkkRbOqNVC0swCm1QA7QJs6ODwb8XjMiz2Yu_gPQWb701IgkBlhqqbi5KdbUBjzBHnStrvdcfDfxD-gBlbrTc-j63eLEjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار برنده توپ طلا ۲۰۲۶ رو یه مرور کنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/80588" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHappy Smile VPN</strong></div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/funhiphop/80587" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از دستاوردهای آخوند اینه که بندرعباس و جزایرش از جایی که همه آرزوشون بود توش زندگی کنن تبدیل شده به جایی که همه ازش فرار میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/80586" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXjdlwnONUWFRcRkJBd3YtvGY-C3j3Juj9IX5tkJDK7Gvhuyte_UqcCeJZ7pnYEKT4Sp3ki0wl36zq-f_3Z1rFcBW6lAInx7WRfEc0MgnUVaNNKPku7K9q4fRKJf9y0RT4TwFrpXkldhJC2PW_VUcB7sgclrxEjij7Xg99mfbgbD3uS6gHVkQN_ptXvURaag2opBpRoWZYSa3-gv9KBC7tj74HuixEcIsZhD3qQZ6t2JpypOYDDncBnYoY7_PlrY2sNFUv_pFztDCawJPLpTN7sdAnkHSaYs33i-wJwk5SXa27Ivgo9SS2wcbHoZHIP7LVK3N7_cZBllwEwAhz6KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/80585" target="_blank">📅 20:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI3RfsWHgLymxSgdgqCn4J6z1a-PnBI1llwa-Ej7sS2hg8SvSMB5G6swVtvuNxCMFgm3ZzWf0rU6CglYT_xHr0dxo3G1EGadfA0LFuDFI1OGuyNeXX_qMUgpKewW_sNqDK36Si-E-fUxMGf_EQnzChrQC_0vzsI6KOWtaSwqEMx-KILR57vOoNwInyrcidDsKiDpD3RfcUbeG0faMqSlTE9jCHsY0cknThhcQH9wr39XkTziDg_NH1HHYskchJpWW0tqd-1gYjQt2pg-lwNPUUwzU9AwA95GPA7Gv45L82ttF3nenGu9QVfll-jPrIEyGF0LQZxtrGfGVZ89FxkLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/80584" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رویترز: پاکستان به جمهوری اسلامی هشدار داده که اگر به عربستان سعودی حمله کنه، اون رو حمله به خودش تلقی میکنه و وارد جنگ میشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/80583" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علیرضا جی‌جی چرا دست از سر رپفارسی برنمیداره، بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/80582" target="_blank">📅 19:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW_9riKSnKUvK13WvtyFAihjTQwqnj1uwTzvxgbKUk3_uV7R7MqWHz92V08uo8BHDRrJowJ3-6LdTmsE854pCVus14-9yQvBKfS5z4FsiIy9DispWyGtHm73eLbZrBPRbno5QlSsJGPzJhv7wp5f2t1698vEKwuiaJi4bUoOmySmbR2nya6LocaHQZA2ZXFQSGAPJLN8mDDJoVdcWlpfCo4DpWo_pT9WkB5vCuJNLK1XxCPqgJFp5perSQ0E4rR8vXmTA8JU4Xa_nphjrRtiOWCP12KL1o69KaRum2XHzjjW0VzugMx_CcpH8x0F0nxpqKdW9rr0SFGiur5FsL7siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=GmxfHqEEhMcUZsv6qGl4DRZO-6X9Br17TsVYHpPugHf_PS3Zo_W6yXaEoh07aiAA4yeE4FHlBLKb-jx1mDvCow8RnGu-8eiMprM9h3zGOZ0HHoKYfCO8iif0kECQUzVYRByE2UvJn4UeCv_RiFsk1wTY6bj_JH2zmh5mBTlZGFPDI4zAAQE2gRvXjan3BAmzMJYZa7nZQ3ZuSd6pdqDj9qiS0peJ4QnLWHr1wrkliYBr-4_Jh-1K2cKhxp8tgAOtd1gdyofMzWsyAhtDPObebPd5_u0bylTqSmpsebfKoh6UnDgVnm4fEtW69iEaAvH_bulBFNIVMYTIFzsAhdOcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=GmxfHqEEhMcUZsv6qGl4DRZO-6X9Br17TsVYHpPugHf_PS3Zo_W6yXaEoh07aiAA4yeE4FHlBLKb-jx1mDvCow8RnGu-8eiMprM9h3zGOZ0HHoKYfCO8iif0kECQUzVYRByE2UvJn4UeCv_RiFsk1wTY6bj_JH2zmh5mBTlZGFPDI4zAAQE2gRvXjan3BAmzMJYZa7nZQ3ZuSd6pdqDj9qiS0peJ4QnLWHr1wrkliYBr-4_Jh-1K2cKhxp8tgAOtd1gdyofMzWsyAhtDPObebPd5_u0bylTqSmpsebfKoh6UnDgVnm4fEtW69iEaAvH_bulBFNIVMYTIFzsAhdOcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تبریز یه نفر بخاطر اینکه کل پولشو رو برد انگلیس شرط بندی کرده بود و باخت، خودشو از طبقه ششم انداخت پایین و خودکشی کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80580" target="_blank">📅 18:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_VuomEpJXl_PzaJjNwzY0eMv3pG1UZHynylcdLfoKN7VUgvahRso1lCGLUiIHKcvPQ0AffgTiGGkGFokcYuseMnZp-3hUG_AWUt7CmD-h21BPCoVm8Iz-BAsakntD4ifAw54zNLFqJZjO0BAQnWNkN334ibq7fzHQPuQW0oq6WHQmK44fbyryaIEIdWgDbVW3hvhI3mdhzbHYzYUsP4XkAcnQXSY29IzVFbzBZlKeMKyKf09XZbi95LgB5aYKhBRAannYLYAH-e-2uGXrZAnPc3sjieB1_ch1nymwdVH-Y4mo_7njNZeml21VqKVLPibo3XeOujNvh-4IyoIlq4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80579" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80578" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توافق اونقدر خوب پیش رفته که بزودی هزاران شهروند آمریکایی مهاجرت میکنن به ایران، فقط لباس نظامی تنشونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80577" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">لاپورتا چی گفته باشه خوبه؟ گفته اگه داور خود فروخته نباشه اسپانیا قهرمان میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80574" target="_blank">📅 17:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ولی بارسا جدی بین اینهمه کون بچه به دوتا بازیکن با تجربه مثل رودری و لاپورت نیاز داره</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80573" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نقش من تو قهرمانی یورو و فینال جام جهانی اسپانیا با پدری تقریبا یه اندازه بوده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80572" target="_blank">📅 16:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaj7wmsj01gaxLlh7bluhU1Q0wp6WwnkteNXYAN_UjD2umxBydEFFmEl1Yl3YuzNfDtDJVMcZHWjguaE14IDXgLXk6QZHltn3T9_CQWfoPKKwSXZRrEIk228tFK4Ic2ZxQVjrNRHeTsimirAvxaw046wfrGmFKE-_i-6aswOSsP-txoqFd4X1oQBvgz5mWLtorcbGK--xAuysXBFicDltxwTA8zkXxte-SOmteoe_-mCGVLo3FBXtuZ6hQAvOTEarTKiCyWMz9x_7FHXHhrzHT8SHB3Wu5qHyGubKIdnhIRnyaY3yAvuwD8UaZ6VlXpam5kPaT0K4CG98uILybSm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای مسی با بازیکنا کنونی بارسا یجور عجیبه انگار واقعا خودش پدرشونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80571" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">باز خدارشکر این اتفاقات جنوب پیش اومد، وگرنه این وسط بازا لال میمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80570" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کل زندگیتونو ببندید رو حمله زمینی آمریکا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80569" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قیمت دلار هم شده 190، صدشو بزار تو جیبت ی نود بده بهمون تا آخر ماه پست میدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80567" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80566" target="_blank">📅 13:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پخش جومونگ شروع شده؟
اگه شروع شده لطفا ساعتش رو بگید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80565" target="_blank">📅 13:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRm5ZsFV2T_B4MWcQcVftsrm3EHLDxDZu9iR02sUZ1tgXWmezuPDGh1tR6OOsqjBAHxyPMmx-nT48nib6tKZaL_O-8xoydkNBIIeZt713BcviaZ-87_t7om5FYT-j8QJKkaDFoRMUzjosWC3v1uHRCVUcU_ZYfkvBGoIhLX1UD3LFAxpriiF34PYV2omTkkUAlMGvbHWndcN5jmzc-N9wiQk3OYts4nofedp1c3A65g8Fa1gCKxgjP0UJvyrnTxJ3ocGdEfUM5KMAg-Ht5N01BPsvrQLMY8F6qJErXfN-uM5BaFiz145nWkDKrDN_N15Ua2JVr5Wl0VJDsrV3r2J7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80564" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl-L1kIkGnyo68HggisJYgsTerAYcTnkTUBYF2PRny487iMfYc1QZBfS6sNKIa_0RRKPaVIzLhhebKaUcr7CCWU_yxImMfTzsSMGzLkFHfvRqs0pt5Gy1c3bETV8PBoKsnHuv8Nfveu8kOu-Z5_T79LkMQe3DWQBFk1Mohn1ZZFnZw2WPHOacJ8uYxrtpEqUS0dBMPSKp_7XX7h_0mKpZnaUHeN79fukyZsZ4ak9rSVOn3dD7HR5xQdmLRhaaFdKa3Ut-x4KmcETUycM4egiZMd6d4slzqcMNNC0pDotEPVqvbchUv4Ssv5_hLTsAzFQHUMInjEUXeZf99fF07RkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها راه شکست آرژانتین در فینال جام‌جهانی :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80563" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80562">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80562" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الان این کصخل با همین توضیحات میزنه انتخابات میان دوره ای رو لغو میکنه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80561" target="_blank">📅 04:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اون وسط گفت ایرانم تلاش میکنه انتخابات آمریکا رو دستکاری کنه که همین که اسم ایرانو شنیدم پاره شدم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80560" target="_blank">📅 04:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یسری مدارکم منتشر کرد که انتخابات ۲۰۲۰ و انتخابات ونزوئلا دستکاری شده به وسیله چین و تکنولوژی هاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80559" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80558" target="_blank">📅 04:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO2wEec55I8UuKX7nO5iJYnbrwm1D-G2MvRmihbbaQMAFbDR-yPsoYEB3sbZVD6Wx0q3FGBfcS2mRtCBThExZqAMQuxYretCrJxmgKuQ66M_b3gQOmY-Zizzchz__uBR02WPpzonWhrDad8YZqyY3BaiLOOzvrTqj_47jQmWzUlcEWxwzfG6UVmQBAINvWwnoI0KVsP1VPPCPX2YNA4OxdU6DoAJ2FetosikvSsncEi5Qlarhi7k6gzxPswR7ViG_6ON7LzcWroLqDpWBamfh6eUwAgsQ2oILrk6wckySIwWfxu3kEEO1bk7Mooj3Vtec8FEzmzjxJDOZxw3g0RfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUWCrjs3BqwvEsNEYmlnwG7lXybbzyBp-WGUwnpac1pt8a9MQHuc5mmzB4L4uuJ6C0rikl89ed0qSBw651Oi0s_yslrqe8BZxAxNcSNwKjg62zqmbmE5Snyx685cYlTcxTNUl1L_gvJGy4i1hZBDpRRWEP2zyeqhZLU8s15sf7So_qtPAi2MXX9oeukw5GYBlbeM3caqutlM8_Y8Nw0sUAAofaL93J5VKCe2Id5v-uSnjdyAjPL41WlwktXcnqpvt-eAs421uS8KUCnUqwlaUrT7-XiqIJg7dlfMZ4bu6yy4LMnFJNjWdsroencK75iNJN7BMHh-EFhjYbZm8uJMHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متاسفانه فینال و رده‌بندی رسید به این دوتا کون بچه، فغانی هم کلا به دنیای داوری گودبای داد قراره کارشناسیو ادامه بده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80556" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80555" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تنگه رو وا نکرده پس فرستاد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80554" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی رفت مذاکره</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80553" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80552" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا: ایران کنترل تنگه هرمز رو در اختیار نداره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80551" target="_blank">📅 02:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186980592e.mp4?token=ZclmL94cqFelGObvYht6gQrSiTocpYlY780vKnYw1s_GxTxNRjs20EhoKwiKgbgo-gYQAGH9Lj2_PTQxDgVuA_Kxr6ShbFJO0IzLuvSVkA_pZlTBHqsaUT0JHUYNg8djuKLLKHBtcYWDvzK7vDoQArYIks40vVbNczzL2_2RPM1JpSyph2lA1Qxl3PFFltvwWjgQgw3Nrua93MwSfuvmebuba3bNbKDg-3V8-CXSASwXWdHQsdyZ9EdE8ebaupWlGWIa6U6vojPhdfKT96e2hlfO47C0LDi_wOcvGF7dNE61ckoVJfsivIh1Re1A4v_YLxLaFXakAV3wiSNMBLAH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186980592e.mp4?token=ZclmL94cqFelGObvYht6gQrSiTocpYlY780vKnYw1s_GxTxNRjs20EhoKwiKgbgo-gYQAGH9Lj2_PTQxDgVuA_Kxr6ShbFJO0IzLuvSVkA_pZlTBHqsaUT0JHUYNg8djuKLLKHBtcYWDvzK7vDoQArYIks40vVbNczzL2_2RPM1JpSyph2lA1Qxl3PFFltvwWjgQgw3Nrua93MwSfuvmebuba3bNbKDg-3V8-CXSASwXWdHQsdyZ9EdE8ebaupWlGWIa6U6vojPhdfKT96e2hlfO47C0LDi_wOcvGF7dNE61ckoVJfsivIh1Re1A4v_YLxLaFXakAV3wiSNMBLAH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات سپاه به کویت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80550" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگه نتتون ضعیف شده وی پی ان عوض کنید توهمیا، فعلا خبری از قطعی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80549" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80548" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80547" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به لرستان هم حمله شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80546" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80544" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80543" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80542">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سازمان ملل بخاطر اتفاقات عادی خاورمیانه ناراحت شد و گفت تا اطلاع ثانوی قهرم بای.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80542" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80541">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">راستی تا وصلیم بگم کیرم تو نت بلاکس، از این اسم دیگه متنفرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80541" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80540">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حقیقتا میترسوم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80540" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80539">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آمریکا یکی از نفتکش های ایرانو با هلی برن توقیف کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80539" target="_blank">📅 01:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80538">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80538" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80537" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80536">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سجاد پسر تا نتارو قطع نکردن پول ویناکو بزن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80536" target="_blank">📅 00:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خطرناک تر از ناو آن جنگیست که اینترنت ها را قطع نمیکنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80535" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80534">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بابک زنجانی میخواد بمب اتمایی که از پاکستان خریده رو کنه.
بابک زنجانی: تا غافلگیری دشمنان چیزی مونده، صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80534" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80533" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80532" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرار بود زمستان سخت اروپا شروع بشه ولی تابستان کیری خاورمیانه شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80531" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یادش بخیر ی زمان چند نفر بودن میخواستن با ی سطل آب آمریکا و اسرائیلو نابود کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80529" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خط راه آهن بندر عباس مورد اصابت سنگین قرار گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80528" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه پل تو بندر عباس زدن که یکی از مسیرهای مهم ترانزیتی و لجستیکی جنوب کشور بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80527" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این عاقبت 47 سال مرگ بر آمریکا گفتن و ایدئولوژی خودتونه، بیخود گردن ما نندازید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80526" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آمریکا هیچ غلطی نمیتونه بکنه ولی همه غلطارم اون داره میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80525" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب سی میلیون جانفدا، الان وقتشه، برید جنوب از کشور دفاع کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80524" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80523" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فرودگاه ایرانشهر بلوچستان هم زدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80522" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جنوب رو بازم دارن میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80521" target="_blank">📅 23:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از اونجایی که دیشب تهرانو زدن، الان تو جنگیم یا آتش بسه همچنان؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80520" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbKY2NR-n8yrbcCqAb8tc6qWVfqsdju8-UFFHWxmXdj6fXy8SuZsgl_PkMR__6LB-BUZUPvAtIxypnI4cRytNIHhTmXkwmEc0zLvY5017VVW_CPwfIwSv5EZjIAc-OmjL7_63dLumaYGAHRDPYtz1YhFs3SmkzPlYnkqVf09kYqP_cBar7slgO1yIWmDrr3eJkg_6NWG69qw63Pw77sDdb8UfVm9-UL3v1PtI7YxM1Evd4KMxM4oxT2tA8P4c81fHBS2Pcz-mbVomIgVMiHrheCPgel6pE3NeGBcrHL0mJi5TbiK_gNYoIU7MemFYrfk4OYar9J7embOJSE1Q-NW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80519" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اهواز
@FunHipHop
| Rea</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80518" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با اعلام سنتکام دور جدید حملات علیه ایران شروع شد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80517" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWLiXgRKTO3xTMcgFqU6PFu81DJvzMWprvHEA3nbXTMu00AkJ5jBN6nOh-y15eexV_-YwQ6_5SwJfrXkWO7r5KbMpGzsOJX7g1KkOhKDXuq0H2Fb0H4isjk_MnmxBGFhazOKTsVEYJ6bNnGFJsElg7o9s2aCqfIsLOaXPrZk-pJgCBRHXHj_d-5M1deghItBqCubW-dwDBiAT8x79jze5QbgYrWgxSLg6uQJZJf5NzYt0BbRTTDYvlFnXHYDAIMDt3n6QYuQM_UWym_NygFyX3ul3adMZYCL15waeyESZqBQzd7wh1XZn0DZMaiAlgQUII0lK5g9n-UCesOiWG0E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام کارام هیته منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80516" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همان همیشگی (انفجار در بندرعباس)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80514" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=JTp1KoD5udlVyU48oHOul8za1B72Dnk78kG5Akho86TuPCs4x3lQcOSj7qzA2r3OINLziMFqDRaDQYOl4kb8ZiVwaMU5sC-VVisTWhA33JA9DXg8d20TvIVRfHP7UhAf6Y5iq1Qan-2uyYRjTGusse7hYcHLKvBYO_ZVfxk1wo9o4JlfG8QBMqDN81qXCuAYTAL7WGgD7DhE_gUmgSMN-6trusEh-iFnaHi1ZFmUR5LSoALqZx0FqULFB2jhmXvayrMJs_y-PzVQyEbqs6188bWdzGvUEH-3ewtwftKLEr6MQTAmuLGljJI8ceLOKq3VSgseUCpeWfFyARubjUP0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=JTp1KoD5udlVyU48oHOul8za1B72Dnk78kG5Akho86TuPCs4x3lQcOSj7qzA2r3OINLziMFqDRaDQYOl4kb8ZiVwaMU5sC-VVisTWhA33JA9DXg8d20TvIVRfHP7UhAf6Y5iq1Qan-2uyYRjTGusse7hYcHLKvBYO_ZVfxk1wo9o4JlfG8QBMqDN81qXCuAYTAL7WGgD7DhE_gUmgSMN-6trusEh-iFnaHi1ZFmUR5LSoALqZx0FqULFB2jhmXvayrMJs_y-PzVQyEbqs6188bWdzGvUEH-3ewtwftKLEr6MQTAmuLGljJI8ceLOKq3VSgseUCpeWfFyARubjUP0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80513" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Q2banGvBajs2IcMIH3RK_nDTDZtwD20l8bAhYFTxydFnRNqNVMvIcn33lrKDTgkG9WTjSy0QPh2pU6y-Nq-rDJqrtlEz25yDBTwv3YzWsWjBa75oODuDbtpvd_FkRoLBJYgrwvpDBs04aEzHHcsduIfZGP4diuCV6XWVfDI3_m1VQ4fPn3IUUli5WNIo0uocONxVaSKJwR7-WmPpoDTxxDi-9c7qD70b95M2njfAa_CC11aFmRUGCF-QUqs0UdsWDvsaFgJeqmbWGlAy8wxZJczm-wn0rXwoos68NeLeqATMLtH6rEe4oApZBazV3sHqYIgO2Tv9_iTEen-FyF9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80512" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طرح استیضاح وزیر آموزش و پرورش رو یه نماینده ثبت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80511" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3q13pyWVHW3Jr4Rw7jM9ygO_ejUFQPCtbMrU8IYp80wc9txbU-Z6lPW5cf6WsvrlFRhZugyPAU0pWpNHkOQPISIAu5DJn9-r1SHq_MuelqvUCSLFMaOdvib1v4BmBmpDXuqp_2orDXZ1X79u_Mm8XyKkOoELHftV1E3pmoi77zkK5aGbWToq1cDVlk9tACU7rUSHGEEZCAtFE-KXWYpb4jJmlV_SI6wvB7ed4paFyyM5CAYSNWMy5zdbKI37h8KYJbaBQL-CZZRpGgPJNMZud1Kno9vjiLFB0LQi7IuvfFPe-RA55Ue002Vy7gBsrc5OP-MOrbF6k2-UMbegxAfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل برد آرژانتین:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80510" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=BammMde_bEsl2UPX2Enm3UlBYElxQUyVBJI_kHPPgoLI08l4bEsNaRl7DTLXOB2xpYn2_mbJ2HtSmQ576CxxK3jaHaAe2EwdYKclQSkF_0UUTeJRNJ9ZNUo9jzLi4GLxXyeoIPjHL1bxIicAXLSsOepW3XuzMOfgeKQfxMwbo4F82ZtTQ7uOAbUwHfFgEsvMYg1DAdyWDLGrtAUUxMk4SgHg4PIRCAOrO-aT8DAMuc83cXJ22RKyhX5OUofirwOYa26As-mR1gP5r9dyYdMmDV_x-X65M_CO5QWLbLXrBD4ofUsoDDuNIBKM27su_JswYh9zG80uWkp0XuENQ3LQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=BammMde_bEsl2UPX2Enm3UlBYElxQUyVBJI_kHPPgoLI08l4bEsNaRl7DTLXOB2xpYn2_mbJ2HtSmQ576CxxK3jaHaAe2EwdYKclQSkF_0UUTeJRNJ9ZNUo9jzLi4GLxXyeoIPjHL1bxIicAXLSsOepW3XuzMOfgeKQfxMwbo4F82ZtTQ7uOAbUwHfFgEsvMYg1DAdyWDLGrtAUUxMk4SgHg4PIRCAOrO-aT8DAMuc83cXJ22RKyhX5OUofirwOYa26As-mR1gP5r9dyYdMmDV_x-X65M_CO5QWLbLXrBD4ofUsoDDuNIBKM27su_JswYh9zG80uWkp0XuENQ3LQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستار هدایت خواه نماینده مجلس، که توی تجمات شبانه کلاه خودشو در آورد گ گفت هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80509" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام همون همیشگی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80508" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ویلسون دیشب عرق لندنی خورده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80507" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=N7A-2BItRZIf1gIZqw81DtqzEDgF2goEVhPYRT0M3dbwfxJTrkJU6usw24A4TWtqfI0JIwEOsxIzA7WxlDfkO6nH6eQo-FN2c9AjWp-VidKCdrbrg_zwGvA1_2jDKGAhf_byEy0uDBFs8bHOhhMzCf1Gw9aazf2WlNNlQ7q5HCuGpRP-ncXO8QIEqzmDO-mpqimHgvIhGGkjBrZs1FFHQ_9AlAKea_FXNaujvn7nC_HNbWoUKCcyVpXkAXzOSCs2tKO4gKZzb3LCjjNKsA9yLKIBc5nx_h6cwuYOi8Ntk0wE8KWYzR9S_ZlBbgOSZeql1Qv99Iq7SvBcSlTl5VXRJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f805fa8aa.mp4?token=N7A-2BItRZIf1gIZqw81DtqzEDgF2goEVhPYRT0M3dbwfxJTrkJU6usw24A4TWtqfI0JIwEOsxIzA7WxlDfkO6nH6eQo-FN2c9AjWp-VidKCdrbrg_zwGvA1_2jDKGAhf_byEy0uDBFs8bHOhhMzCf1Gw9aazf2WlNNlQ7q5HCuGpRP-ncXO8QIEqzmDO-mpqimHgvIhGGkjBrZs1FFHQ_9AlAKea_FXNaujvn7nC_HNbWoUKCcyVpXkAXzOSCs2tKO4gKZzb3LCjjNKsA9yLKIBc5nx_h6cwuYOi8Ntk0wE8KWYzR9S_ZlBbgOSZeql1Qv99Iq7SvBcSlTl5VXRJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80506" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80505" target="_blank">📅 15:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ی زمانی غزه و لبنان و سوریه رو سر اینکه بی در و پیکرن و هر شب بهشون حمله میشد مسخره میکردیم و در مقابل کلی منت میذاشتن که عوضش امنیت داریم، اینم از امنیتتون.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80504" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نت شمام ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80503" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عجب امتحان بخوانیم و بنویسیم سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80502" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لطفا فحش های جدید بکار ببرید
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80501" target="_blank">📅 12:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW9JmCYTnVmgOSVlZTvwAsdW7o8Di-PsDuuxDmNJ05ze10yshZ_kpN5s4ySjj5jTpf4ID6ff9issy1itaS1LopEP1VmQ91zj-Z1E2CKoT29aIOlZj6uYTrtDGWQG6xyrMxJPAh8k5XEV6h4PPBiD6vB0o671AftWnZb0Q9NMpqdZJMdrxFV6iuxWKk1s7PrpIM_K5t49Bl_63ufAs5PX13XopdxhXKHmkqK1bheMTkhwmTUpsE5qKVMdJ_qLIlwrpoJ6FC8VGt10aFDLJJN9bV-VixBcB6SNjVQbUl0d_aQ5ik97D0979cgPzDr2xMt6aAzzBNlLW6O-W0VOT-cXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم پول ویناکو ندی بدبختت میکنه خوددانی  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80500" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkZWHJKkJ8tJzPt7fSBrKHVOAeKwSTF3pU03iYlY5cMMeQntIOac-kT81PC9dif2ubhqO0SKP3UnxkLdsh_k_zVgQBvCUj8voMApwCfl4Wa0jVjbgyYCeeicWp6Jmb-4TQrQoGqGt-m89BKjllD8fkKbH9xWse-ewKJ1plWYICEo8a6dvD4lKFfeNATtGA-U1mD6WVikLkhCdBiFCnSQlS_gpVl1wkqgv8QW3YbQd0E3RDGLG0ti9TTrkgjmx-DY6r7CjJiR7t-ADA7Nrz10rUoytBtPJq20D8bCRZz5DhdHJ-8hEMX0FWLHsTLqzC-QmyHyXvRKo9zLEsi1oAqf2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80499" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=Uft4WCEh91oSFGxq2Ntrv09WaCJ3Gr1AyJWmcc9s5aAlTog5KdDh_wbq0y8xVTI7e45TDchF1WTvEsVjhmBPpvRcsi6VF9O1WlY1awukRHVCI3x2XL0oQtkfjFK-0NFGr3uEfgfajZKKe9Vd4aadV7szJJxxenQG__p2GMqIlpeDNBzYADt3WrWnb8jpqOLvxH6ihftQZlCEsBWxAsMhcdKxKGq2e2Jzp56qxIEhKooos0fTWjDMV0w_YEdL95UzGODyb7ckZkVAplbajDXvO8sIeZv2rLRC8pwZHak-Urx7pOXA4RjhlBjYOTkpyYI2rdwrFuKkSH5bLMECPMnsjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=Uft4WCEh91oSFGxq2Ntrv09WaCJ3Gr1AyJWmcc9s5aAlTog5KdDh_wbq0y8xVTI7e45TDchF1WTvEsVjhmBPpvRcsi6VF9O1WlY1awukRHVCI3x2XL0oQtkfjFK-0NFGr3uEfgfajZKKe9Vd4aadV7szJJxxenQG__p2GMqIlpeDNBzYADt3WrWnb8jpqOLvxH6ihftQZlCEsBWxAsMhcdKxKGq2e2Jzp56qxIEhKooos0fTWjDMV0w_YEdL95UzGODyb7ckZkVAplbajDXvO8sIeZv2rLRC8pwZHak-Urx7pOXA4RjhlBjYOTkpyYI2rdwrFuKkSH5bLMECPMnsjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتکشم زدن تازه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80496" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvavNFRIEOjS1SHpLoQwKQSJEUZ0KeOErVABmyNtrPCsN3CIRQOsFH6Cgj3qbT9jZcN4NLVTs0lmqS7FJoQPOGKsyM9NtUpkSUj0tAv7oLPjzwEtjduEvbvTxkUIbHlu0TzjzIcS99oqrtFS3SLfpEAvuWOh70yHail0ONnZkjXBckijdXYbVx0MQcSZ1N5Q6yKPDpI7Y4Agx5z-FWpnEVH5_G9Qa5We4wsMo4egA8YorMxrPIiT27gu7Z1_EQYVYTen5ik4QFBbWNJ7J8SUwn_Dmb31oP9nRXv-Cke0TyJjyi4rGTRhp678X0x9M6_-eTyOuaekj3qSkYuvMMk7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بخدا بلینگام بدبخت داشت خطایی که انزو روش انجام داده رو تعریف میکرد، گاییدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80495" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فکر کن خاورمیانه چقدر پیشرفت کرده که دیگه تا خودت صدای انفجار رو نشنوی حال نمیده و هنوز جنگ حساب نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80494" target="_blank">📅 04:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqnDGaxw4mgUBYmpe7C0R1dAYHrbLqhMCnMA4G0WholBvG1WiiZWwpv3H-KioyA6edG3V6DAX8KUpoeYO2lXcFrGLVVEKHPbdQxy2y2PcEv6DAFvXcHADRxkhG3D--FHOrm_yk9fP6PFKwZeelLVmIIlS_KfmbMpfBL_kMlMEL0uxsqHnhEqu8EbuN9EwiE3JIzgwobXfI1Js0H1TC1kX7w0bW2UsgVS6W8zCYF1OLohnJgpMIqxuzAerAyJtyeUjGEGuOIMR9nT93ER-wk6LXGcj2CLqzAuUrZrqnHtTDLucvZ4PIASsued7dXmpe39jZ9H1GWVgDrZ5_Aw01NlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPSepVwYTE1XPeoLt10U8zSEUtCZ7dijiJf8OpgQTKs-dbgprZAQB52U1tb5976GEJj6-B1RXufkKt0bXmEiJ-Bh9fkoXA6vh_lz1ivOuLLl35P2anDKry90La63YwKZ5mWmVgedosUVYLhCV1LYyONaF3eXgSifZk3xKVXJNEx7Yg6KWyoY20KwQiI-X_UO91GCx6PL2I4HODqtRN9LdRYyAjreMeswK8UQOJvnfK5Wht50_Ra5n-w9Wofvg4-MWXtLu0d-k03agfPWildlu8WP8utpZacjYaQF7Gk31G_RN2OAp2UuSM3cM6-Tu1QypnlCqC6pUbwjC9MDDHuUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
