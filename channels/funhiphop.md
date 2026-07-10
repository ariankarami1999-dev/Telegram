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
<img src="https://cdn4.telesco.pe/file/sld_673kh4cqwRQ_Uzy2UAs81Pb5pRvql94KTohnG722AylwY5UnsKifTmoMmd-L8VdBEWrtI9ONXOByhjciG3EsXC9Muv2DXHA_kNJWbDpcbRa41k7B-PNWRfZHYWpbE_f-Yq5Wqq1vfnJ94ZU695b6OF-OZ9q1tYDzdQckzq5l-hOAXh_pc6i0E8IIa7QUZ7L1-zIY68houllLR9VXRZX_VTAFNeal70Nj4fMbjO40QDHuWdbl8aqO0XhHHZPh_bcjqvcGj5NRRXbwqNilHA7quNHLBh45JhnPsz2FHPW8nQsHVK_NbKR11do3IPZnT4-o1SmtneFOClhlWThQZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/funhiphop/79927" target="_blank">📅 20:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGYYnRHrRQO44wPPduUMGkogWIMpHGdTwwcWzceY5-x7aJsyrYVnt5-lFnGmlyyYU5HagZmsNAI4Si9n0waN2tA3MDaFALLvwG5gpsJZdvXie4PAsjQ39R0t4ik9QcB7_pB5CNULfgnqreSSEwSX16wb_mIoDnFTUV0OyoDrO4YnH0k-03fEDz_L49-ukgx_T-MzV4l-9yZCH-9jh8UCjSDLDYROcd0w2KG6PaBxJnzqWNWy8lGS-RUl1PZ6TuDi8w_lZ5jlRu35Qkg7A-N3wForPolqs7jg1FCByfXkDUjjbJxCpY4nZmTV58jlWMVWS0IVBWXXUuVSscXkk_YsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم شاهین فلاکتو یادتونه یا نه ولی گفتم بزارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/funhiphop/79926" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsWVfOz-mRwC1kVl21p2hjLwft2xic6xe4UzF_TRlwSPvgBP3lu47jOU43ipDo3jwrZz_dey1iVADawwNp6Zgi1a_WeqqS-St7UwrMLXDZ6bnrg91bAto8vp90slJawt-5uPVpUKnPCiPXHO0MXjGjfpCh1KpEySntUiqgu6_aPXJwkGszEcNeRr8-kriBm8oOl-2b0JNJd0DMcbyY4It3J9izzreV5w1SaYiQPsQgIHlv9TnzYEgQsbnQxfWt4bBoiNfiNZEPWK8oNTe41efFwhQCV109uOlgDcjPIqb5gN9HQxIrTpWXXVr1gi0AWa1MmZ6nXRHreL5VddlEWFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا عجب دزدی ای کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/79924" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برای یبارم شده چیپس لیمویی(ترجیحا مزمز) رو امتحان کنید دوستان، مزه بهشت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/79922" target="_blank">📅 19:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/79921" target="_blank">📅 19:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این کصکشو تروخدا
جمله پایانی ترامپ در مصاحبه با نیویورک پست درمورد ترور شدنش توسط سپاه:
به هر حال واقعیت را نمی‌توان تغییر داد؛ امیدوارم دلتان برایم تنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/79920" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/79919" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGavNKFElSSC4p5CKFbhRJ_JzVtEEbjjn22HD53bNAIY17tLEojAsfbtfyLBfUvMgIINfaltLEKPE28Q-xcoDAE6uRxnNSlKuMT3T0NSCDrXHC0UlhQko4PATWNrRf6FdstqpW8MAwEB_RQ836lf-phC5vcPdClMMUWpMuP4Ww7FUkofg5Toye9FHPfsq7e5AkEDwPvB3gwkHx5gobxr2zc-mETa-qTYrg21Mhxp_MrZvTHtP2R9ESSFhuGNRb_FojbvJu524CUn-xyGmh2Imk_G0FCc5LatwdK5158E-eaFGDob9YJQHNqi0PeNundjSrUXEzrw6AA-_y8Vz_ysjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک چرا دندوناش انقد بزرگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/79918" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf2d4hIhBbCP_NKNuIrBL8d6kYsVP2qzgJ3t7RWQfTlEydeEmoO2IKhK0Md7dZk_uuYaW6aCWGBmC06BQRlr9eI0mC3V-2lO-nXLkoqFP7ktelyaq74K5Nqhz4mfixLXvA1jtlZI-tlFvfrrMsusWDXbgirk4CeiqppNlF04stFyoBlhmv16UikaBiV77PfeOw0Vi3Z_hg50NTeCNW6K6IRXWWLOvWFZYd1-rTRPvns1kGGEOd_oBntWjR4fVb1ZTztHRpPo6ygwvPD_yapLvBs1jFd3RokGkHus9DPW6MqplI7_I-vsGcrLSCrYxENb8oPmDUvxzEbzjgRtcK8YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/79917" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/79916" target="_blank">📅 18:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryEQk6ZStOD-sYT9bJvragiVKNp2oSYTHjp5fzYZq8KiCVzuIzrZluTUPo8XAE6FZrqefcd_3xstmaWOUD2BjC7LXYFNJTkIR8-ltYsFYiimKfuTw1P9I9m3mSTXVLe-7ehzU8V9y-Ghxh8VCb0xZdPjsorOZv5nYlGk7XhjQgK2DCpeP1aKdcmNNXvcGjvPG3MNlBWM1J6JryvgXhE3_d9H_J0HqFsKMKt7SPBaoXSKMUBLgP8YZXxVwUHc4dgNLnmh8I-yCe4AnXi6lsvmR-ejL5usdF53JIxJvqVrw_1mtASlSymv3QVMY-8LZkfsptEwr7Ncumfw0df2pbBNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PccYM0lo3cLj7SVnVtAIYeuP38IPjUevmyLq2ngT3BmRZdcjWumVjnawDQ7MU0PaNxFth5HyEdpWJyYgNwRCbLAYJc1j1d_3WGIOaiqTAkD-MmGtOnhPJERj_-PzW5negoly0NaEcTiidVD7WPgkz3zTFKlUC7Bfa1K8f17A9FqwMbLL8oXYxuNbRcx_utE6tW3nlV7eotrcZzdMHeCTSqGmvif4y0h-x2j6i9eqL0ICfTgXNEPgcRG2TAg4Wqd0p4KNznDrY8fSSn-E7O7rYVVnzU7jVMGLs01gVlERh5_0om-Av6fA4vZDhWPkfLZqhZS1TOuCSgS8D5DpvSHPWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ درمورد احتمال ترور شدنش به نیویورک پست:
من دستوراتی به ارتش داده‌ام – اگر اتفاقی برای من بیفتد، به سادگی آن‌ها را با شدت و شدتی بمباران خواهد کرد که قبلاً هرگز ندیده‌اند.
من مدت‌هاست در رتبه اول لیست ترورشان قرار دارم و این بخشی از زندگی من است و چیز جدیدی نیست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/79914" target="_blank">📅 18:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/79913" target="_blank">📅 18:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/79912" target="_blank">📅 18:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpFxLEJtGL0K-uO5LkE5QEzmW1uytqFslABCq0yjA17KNnOr7ODPGkkMw7Sutx2FReQHUBLiZjFfeMODJlpfFuV4fDAbSZy6l8jb7zPBNSwKrQcUEP6IiQVBPbdz5in3IkwRafW05QFb2WPWSLtyaRFwLEimSkpy_TQHF3cq28vU60wXecwZ4fYGVm-k5uoJAN8EkTcb5f74hpVMbrtifaZLm4ydp9eFBNdN-M2xI5Ntx6MFrWxwW2EZT-0zq1kvGo6n8TQWsYwIbPa_g_q9y2d7un9brzyt9aUsIXgSae9W5UxBOzBGx080LrQ4I-pqizgoKpYYK7cZJ-EK71nsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/79911" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVlTUlhIPUkrkcK-n1ZPdYonpwIFShGRzrpPnM5i0sz_Fs0E5P8Z4irgPvmkQrD75lgT-8QcIwJCPjCmE45IJnCkiiEGjhr0kA6Y0mQ5vql-RAXY_Qc8k7ow1AqJGM9ljMCovFFdlh6ocHqloQB_-C6IvzafecQn9OXG071IDrvSkR6WZXkNI7HvYRcsFHUGSxDi_phr3ct2ZZlLicxDZn7tMcvHdwsgwsN641mQTiDSyS909DB_SumsoxmJ1EBKGqZIau8u-U94D3L1e1MkHwJA_hKKTOr-WzKkLu75tgVh0SquTwjNVlSgztSfbnF72yGnqkbZFVtIquane5mQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه با همین ترکیب هافبک و خط حمله اش پارسال به اسپانیا باخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/79910" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0rJGZSaTcZPXO4fvXPsX4LpYl6GTt_fn2hyXHdnVA19ku2zv8-Zq_VO-g54fU1gde269nLIMS28AHLbkto078gtb4Srpv3ZFkbLMvb7eR1kvp5xAqA5YNrMKhOwhuqfVNp7sewYPICXLC52jGL4XcwmG9U1uLvrtM1M9PsCf80bGad3FVQugGLcopMcSDZ3P4yar2w-m5fTtnEx4IYwPd4xOYAFvGt9G49cqtMHX8wWKQyGk2IifKPT0qHzfDHYHFjayZ15Tk4mHEvZlsoSW7O9BWB-wE313Hk5mb9thxQQDAylRv_sKC6TDsBpGTQBLzMC3ox_OKxnO66ZcwXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX3mtONa6Bgbd5NHTq6Coxa1-EvMU95qSoPh5OycipYD4JO9z94oLdNUOidvBs8NHa5ORssUvVfWxs_Z5PrQnF1R9cSGJtKATpUui8gLqqr0tOXViUBDms_gA_Yo6dnPaGrS-c0lsH3AGPkjJb9rvAmzujN0eax5jAHqKBpQEFHhVj6ilheqw1IdUkYGxhIaZnNBgPVWi0bVCubfqNoUnsvLrmV2ownvWXlOlj3J_Hh_TsgFnqLhR2MxHezESm45jcOLP0f1lgj-O9T8veM8Sjc3bCe7dUxhDGX3pR4Hr_lOq9YCLIvxz0D6oON1SFrRqY22jDmJ1Rgv55FQkaa2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داره بامزه میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/79908" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پلی بوی کارتیمون کم بود فقط تو رپفارس</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/79907" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو کجای دلم بزارم</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/79906" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTijay</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/79905" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvsGZsKkff2RqQ3QFy1Ge20pigfWh3xkS36V2GkCYK9azhhqr3EHDOSrTuE1-c4JJSpbR1STs6Hr9qAcbJAPbTIF8dFj6dwEH-3zGSVKVtYt6TsiqzYBt3IIoyLaw6MmsfW0McjCAMaJDQxJxJwZ45wbGC3t_eAL1MMFfL8TzDXbNtw364UZ7tOg0jZwdzEtKocRatZ1lnVrsxGZbNOhHAhjwMuT-T7jNQ8zk59HYzt1N1dmRoIn1Lx7LQYvEMb02EzCItqZjsfQSV2C8Dsc7MGu8F5gxCsb-LPqXrByflu6RySziApNd6OrufTqjNBsKTjnLMkX9hO9Q7J4v8K2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار به هیچی ندارم ولی ناموسا چه تحولاتی تو مغز انسان رخ میده که عکس امام حسین رو میگیره دستش باهاش عکس میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/79904" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxlqPGOpwddQVgBj5IS0HdVXNYPX1ObKs5WhIv9skF57WmZicqGWuNfkAaR3PQF8WdbmVokFHeorZcuI6UEtGZBoqWHRKP7A5Lv5vw3_iVixnxAdu-S0AkzkIpShy1u_21_T7S2M6d-_z5Ztyp5vVQtBA_wxTGJaTEIhP1wnW_JXHd1koU-zC435XuaWYYtEnoTM0vc4zQK2fqa2aJokMZ-JDH28umIXETm8mwLbosbjcc-RLX1LACs4366OgvCfd4izEJn9HIEmz6ezZdSFT2QkPPtgwzVRMDNpkEGHxmt985QEN7iiFthn6mZAjGgDO5cx_gijQ_yGZcuLz8oXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکی هم اینارو پخش کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/79902" target="_blank">📅 17:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBZpwAsINOJ_DvVD1wh_1YMYxFoFarGCy4E6R9V-DJPGLrGYVDnLHW1F6yi7gREEH7YN9jbeakxNv1zGanyquqbjVmwVdCzjuTmywXZQlVnHBT7kh_y-vMgbHiJJhymUvs78gVFkZnacVwvFeo-1sl4mhsG2oFO_AuSUzbo3x4tGJpbWfMrczhjYbfH9BMEw-HJcOsTWmAUfhf-8GszWnfYFJDpEEyz1yCIcOs2eWi4o8Gd4ZKzYwt2Y2ngxSWrtZWQZaXUN8YQaDKVnNSZxShPqeRxffr-A_i3OrSlnDSfEBFPkxEw1bEKuJhgpH3kJOTuPUhTtZ88oVymbzwirgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی که ویناک از دکی پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/79901" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkIA0EVJWPANxYp10Ks_Hr7tZ8xvcZEQ5wn5-IV2XNFDyxqMeL_UJbkAAToYwqSNA-1XmsOwEyHE-G7XWIrvKy7eEQWd0PDj_SkzGnli-F1iFNn_3eMSvFKcsIpDhIkGFNadH4R84zMlMi0WcxAgd5LDcGp6TJg0ejNRiI49O_poY8UAUpDZV9XOdy_G2S-T1bZPCJQLUyxfBJz55keY2gsYbOlJ6GA3JusaTv4i8fDnzfQaeSlyx9kzBfBOiCRC8AFOd7E_IyWDhkDU0Kb15fJx1onznjUZeu9ocrOUmNSbp85vbgN19Oc6zPQbrQQPTXrjA1cinV1tfCKlDfPMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاد
👌
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/79900" target="_blank">📅 17:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کباب کوبیده با گوشت گوسفندی نود درصد تخفیف به همراه ارسال رایگان برای گیاهخواران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79899" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79898" target="_blank">📅 15:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwxSe78k6GHZnFjp1clwYd1tt0Nzgt_tqjlVGAgOA4DIYkdANqb8azmzwzXapKoSvhBUJkMFC7PPK1w_2aRsXi-bCYO_uF5cklCQl6xsdIWmyGMEF877LArLCFchTjgkam7WfTN6_RX_Qs63dvRMkg8oQqN4kXzPiH_tDEdAunQGffYQu840_Y7zRP6sijTe5crVts06cFI6IoQiNLEaNXFA6QNVWoKL0s-pF6i1RWZ6zrsh9XVL59gY1TfC-RvdnohKjCFBaAayBZKwa-BPhVjiD6bdA72JSy1mu04mAfmLbj_-VHukhGttMYNAovFKA8NhH4Tuw39yEuPdtaghMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79897" target="_blank">📅 15:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79896" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my-rJhG8zYTu2hJ8IBa404gwZRHlm5kgA2vH9mmmrxKtO_4s63ZMZONAJXtB7uiirIubBwaTdYSLdvjYdJ1mhCfuc0o1gkrSSE5umWXT6jqqwN_noixwbmt5CW_OAZwNIOFD80aYk79JE5_Y2CdNvy7-7WCS4ZpSqEiOKa5uwp-GaDae9TFoVJNLinfbeL7FeiBFgNNKAqrIdOn1hr485zA_MnZRj6nLOUXr_DXOiIHU1Wc8Cwkz-juNbxh_W6FVhI2URWISTH96YlgrVDkveGQsuha1g6gd0vPUVfBsZcd0Hvjoc3lh850Ue2x2DhZv5S-J0R_xPpcf2Wo3HhtBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده
کلا دوساعت وقتش مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79895" target="_blank">📅 14:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79894" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رنگ شورتشم بگید دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79893" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79892" target="_blank">📅 14:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ولی خداروشکر لا این همه بگایی و دغدغه، نهایی و کنکور ندارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79891" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیاید بگید ببینم وضع زندگی و حال روحیتون چطوریه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79890" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واقعا بیف شاهکاریه، هم دکی صدفو دیس میکنه هم ویناک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79889" target="_blank">📅 12:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWMbzC7RS4i1bhmDnhO35Aw5CetNszunZyimoyx4SvHprLTQQ5Tuxw8imJRKtzwPBy0yMbTe-J-LNI9o9DLlnc9cr8IoB0MwdytWwFb9XY0eKNxJQ4FHaFpeTfFZTncP0KHzlgEGvmxCsoAp210aHZ0goDE0ZH7DATQ8NuTcNPbQ_TPlS-CdhZTvwbALMWrHPzxsxsSosqcGCBsb6AZ_2B4S2cXph2I9Rop55rE1ho8E22NjSwPdtxyE1aT0to86N5oSbwC1iz11EngrUuuqMHKZaZ94ty3aH15p8dnALpoDmC9uC_IgTR10qpC6izNCPmndeAfDdlv4Gq-BdADRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=OLYk7qpx0k3YtnG6iHCNI_hWbcbmsr6nKp__FbsG1pR3rXy44UHfa4495UO69OjAGD32WiHgg4o2cTP-dU8PoQeS0KhGMv3mwp99JBw13dy_7s2qCi82lCE-WS4K8rSessTRM2_oZzyO3O0jbeGBIqpYYw51JjgdwLNyxjmHe785yc4qhnVCwI658les8XP6ixQGmifFfgTtELqOKcpnugw-wXO-HEo6Ag-kYk5K2BOpZ_vS8RsAU_4mExIF7y_fmd90wJxDqh-GYTdJUH3NtNr_HKNoJNnaV797k1EAQaBzTTZZDBDsLlHBkVDzabhmYVtMMqWcLotF2k-Y2Yd2MTyZxJ5iFj-FaVMX9uQgAAoSvHaR9wdBr3wVvRXGhCbhvbAA24dd9hX64XtFWGk3620J1Yxc0Cb2Rc2P71-O6qXU11_wG58ffxTRHu2kLo2dJw8mdiKZPflq9Jfk8dSTOpA13baxzP5MnGv9MrjwsKSxBWBaRvv1-FHB12dZv6KjgVbaFZN9E-jCOM_ZEinoi7GwBaHb6ssNxRwYS2jcXNjNTYe0_58KcZ4kRh5WJ5r9FvkDyWZBi7kC5WquFjJ6VGVI6hNLknWCjpsEcMFn9vvwSyKxuwQVRio6R7h6TbJuTW3Q2G8JdwTkorhmKBHVHauApCRGACct3RqH7axpXxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=OLYk7qpx0k3YtnG6iHCNI_hWbcbmsr6nKp__FbsG1pR3rXy44UHfa4495UO69OjAGD32WiHgg4o2cTP-dU8PoQeS0KhGMv3mwp99JBw13dy_7s2qCi82lCE-WS4K8rSessTRM2_oZzyO3O0jbeGBIqpYYw51JjgdwLNyxjmHe785yc4qhnVCwI658les8XP6ixQGmifFfgTtELqOKcpnugw-wXO-HEo6Ag-kYk5K2BOpZ_vS8RsAU_4mExIF7y_fmd90wJxDqh-GYTdJUH3NtNr_HKNoJNnaV797k1EAQaBzTTZZDBDsLlHBkVDzabhmYVtMMqWcLotF2k-Y2Yd2MTyZxJ5iFj-FaVMX9uQgAAoSvHaR9wdBr3wVvRXGhCbhvbAA24dd9hX64XtFWGk3620J1Yxc0Cb2Rc2P71-O6qXU11_wG58ffxTRHu2kLo2dJw8mdiKZPflq9Jfk8dSTOpA13baxzP5MnGv9MrjwsKSxBWBaRvv1-FHB12dZv6KjgVbaFZN9E-jCOM_ZEinoi7GwBaHb6ssNxRwYS2jcXNjNTYe0_58KcZ4kRh5WJ5r9FvkDyWZBi7kC5WquFjJ6VGVI6hNLknWCjpsEcMFn9vvwSyKxuwQVRio6R7h6TbJuTW3Q2G8JdwTkorhmKBHVHauApCRGACct3RqH7axpXxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من یه سری سوال دارم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79887" target="_blank">📅 12:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79886" target="_blank">📅 12:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79885" target="_blank">📅 12:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یزید این چه کاریه آخه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79884" target="_blank">📅 11:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=X8gR4yOei1xsPOtVhTIIPxmfXWieTKocjYCCqdKRbG52TfHCGHUArfr-8xWCkObIMkwxdnErreplIbJftegbeMrADPcHKPJZnVicMJvrFdHZJWf-9-th4s5MF3DrgKLoIsUNXeWJQ0fxFJwKf0kfMl6uE8-lHOCUlLMjrzRWz0NArrGspF3iiRVEAVhaL3fBeXPiBGnvey_IOI5uF9E4UmPlulbD3Sx1MvS9gSktyeashY8yAytVdPseaYqwL6PKLGLwUOxna1hbjgA2M9jgEcwIUZ8lVp2KwoqKpdR5aqZAGF2-FjTFTWjZEDJjtj2HO1w_Rb4x4nTfbIpbeweBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=X8gR4yOei1xsPOtVhTIIPxmfXWieTKocjYCCqdKRbG52TfHCGHUArfr-8xWCkObIMkwxdnErreplIbJftegbeMrADPcHKPJZnVicMJvrFdHZJWf-9-th4s5MF3DrgKLoIsUNXeWJQ0fxFJwKf0kfMl6uE8-lHOCUlLMjrzRWz0NArrGspF3iiRVEAVhaL3fBeXPiBGnvey_IOI5uF9E4UmPlulbD3Sx1MvS9gSktyeashY8yAytVdPseaYqwL6PKLGLwUOxna1hbjgA2M9jgEcwIUZ8lVp2KwoqKpdR5aqZAGF2-FjTFTWjZEDJjtj2HO1w_Rb4x4nTfbIpbeweBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یزید این چه کاریه آخه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79883" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه و ماه‌گرد قیام 18 دی ماه هست روح تمام جاویدنامان هر دو اتفاق شاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79882" target="_blank">📅 11:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گنده گوز اعظم بعد پنج سال برگشته که مکس کونش بزاره.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79881" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNNHANAnHiL8uEqURqKW-9WcVcODVX7F_jlA2-YQU-qYA1mGPzSouh-epjjKNZq_SEWuwK51EUTD810nxtaLudZTsN_yiJMEipvYlKY-DlCkDyDP28wqAWQhxW8i6I0DvnoPgg_h91u_4G0DKetqofhFDwQX86Oil1KAy4ohWXY8vJtI8AWWx-hgutu6liHV4aF3G5AS5nbEtXKEg8w6B7FFVkjziy5KD79JvA-rgAvPQA1Yz73nZhgtVf_Trf4NLK78xciDudkfmxdpkyhYcxBPbM9Z-h-QfZZOmdDpEtswWm87tBGOwCp7rNLf7fH0rF13CzjSPUougSO3o8NjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79880" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=XwPaN_hHvab4pi5NyIo0hxibmVlaecPKrz-SjgBT_K97j6brOV4BMv469t45ukkxyqaZoidFdD0VDchls_UvJUV4xctKQ1yDiGMBoS6dWOqwZbLI3HpkJg3QJt-7jaVGAgfUIIa7ZT-_nkg95lP9s_Hxba1RyLjuDdeQWo2ZSyumOb1IB4CW6hoU3-GbStYr2A7WOVg2vIdY9vXmTyFPUWKXZM0hwwOICL9MnfrDgqacP7TddkJsCXQbSjaCBr9ILgzSEeiZqLL-ozmbgn6tLisyIRSlynR1vqIdQ8jY9Ag_TcGQOHCfZUQbh9pfv-aGzgm6GVy7FkzQcqtnVMFQYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=XwPaN_hHvab4pi5NyIo0hxibmVlaecPKrz-SjgBT_K97j6brOV4BMv469t45ukkxyqaZoidFdD0VDchls_UvJUV4xctKQ1yDiGMBoS6dWOqwZbLI3HpkJg3QJt-7jaVGAgfUIIa7ZT-_nkg95lP9s_Hxba1RyLjuDdeQWo2ZSyumOb1IB4CW6hoU3-GbStYr2A7WOVg2vIdY9vXmTyFPUWKXZM0hwwOICL9MnfrDgqacP7TddkJsCXQbSjaCBr9ILgzSEeiZqLL-ozmbgn6tLisyIRSlynR1vqIdQ8jY9Ag_TcGQOHCfZUQbh9pfv-aGzgm6GVy7FkzQcqtnVMFQYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 5
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79879" target="_blank">📅 08:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بعد مرد مومن به صدف چیکار داشتی اینو خود هیپهاپولوژیست تو دو تا ترک دیسش کرده بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79878" target="_blank">📅 03:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اما اگه بخوام خلاصه دیس ترک رو براتون بنویسم: زنت جنده اس، بدهی داری، فائزه جنده اس، پولمو بده، زنت برام میپیچه، بدهی داری، حصین زنتو گایید، به علی ضیام بدهی داری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79877" target="_blank">📅 03:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79876" target="_blank">📅 03:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79875" target="_blank">📅 03:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxNrpAce7jp1xKRwU79eSmXmHMCSqP6Oyky8p6E9GS90NQXuK3UNi6hsy80ZCAXnVNYRU54xn_8TR6x7sqcD5ay8iRHEg2pV2L4joV_Cqji6C6CuXfoKBtPPgqd0DWPU63jK-FvUifB6S0uLRqUzdtgTtH-D8OV52FfefzPiU5X5S-6frKwPG-s4MfE7wDuUF186oBiH1wOhPa1cPqUJqOd-N-xZyzl19Jvn6QeZ-wD6jP7ugILIHpBGwx0GZtd4ugT3E5aK1gk3GP3-F7LcI51vtbYVPvX3nYfa0cm2NZiraZrxo34XpFX9HXTIMZVk8isKOkTo5LbjpBAjeFTbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.
YouTube
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79874" target="_blank">📅 03:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دیس بک ویناک امشب میاد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79873" target="_blank">📅 02:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فارس اعلام کرد که خامنه ای بعد ۱۳۱ روز و یک تور ایران گردی بالاخره دفن شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79872" target="_blank">📅 01:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">البته دمبله زد یجا که یه ذره غم و ناراحتی وجود داشت ولی خب تقریبا از یه سوراخ زدن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79871" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79870" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79869" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امباپه میزنه
سوپر گل هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79868" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79867" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79866" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79865" target="_blank">📅 00:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مراکش عملا زورش نمیرسه طبیعی هم هست ولی فوتباله و هزار و یک اتفاق غیر منتظره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79864" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یاسین بونو
🔥
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79863" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تعداد حضورم تو جنگا داره از امام علی هم بیشتر میشه کیرم تو خاورمیانه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79862" target="_blank">📅 23:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79861" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ریدم حاجی فیروز کریمی تو شبکه جم چیکار داره میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79860" target="_blank">📅 23:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دکی سه دقیقه دیس دادی به ویناک یه کلوم توش نگفتی نمیخوام پولتو بدم کشیدمش بالا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79859" target="_blank">📅 23:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">راستی امشب ایرانو آمریکا نزده، کویت زده</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79857" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79853" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79852" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حالا کی قراره ویناکو بگیره
هیشکی بک نمیداد بهش هفته ای یه دیس میداد الان که هیچی دیگه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79851" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیس بک دکی به دلو از این دیس بکش بهتر بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79850" target="_blank">📅 22:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دکی به لیتو: خانومت خوشگله بزی لی تبریک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79849" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79848" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینو نمیداد سنگین تر بود</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79847" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79846" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRYP_LTS_0Z7ZK04PDPMCzo_pov-sqSco6LIC6z9_5BSVpcejQbSCXk_KI38jg0ZRb01gtxMCpKfinSrKn6CFRgBWVvBQ2_zFR59q0x8aJyGdR2C47cKN5Seo0o0gyBo2EuUVPCrJF2YAN5-KQez2DY55LethK0tEuNq0oIRoBt9jR7EvqC0tA4WQlk7YgfE8010f25V68GfsAor4V2o5LqFdYy3XvEPDxcnnRbPeVZE33EtCJpPaEvOwXAdVEUYuRiGBC6uLXLxplC7-7x5rnJvnlvc4Evk8tA7hoaWgC1yoWJRdUSP4mwdi7nZlSJulItZR4iApIZfemQsF5ZkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79845" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79843" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79842" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA M i R</strong></div>
<div class="tg-text">پشمام اون داداش کوچیکه هم که میدوئه کاگانه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79841" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79840" target="_blank">📅 21:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79839" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79838" target="_blank">📅 21:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7EhpMXcVYiMhhZLVIxQisn8EKNkRPyTP6ZK9Y22jyPyFH2XWi-B1D7Sjfxale9Rz0_Xdvr1AhgAsmwB8wM99D8r417HmonpXWdX2l6jddKw1QrMzJUKYBUSFYbnSK_h1SYtQoSUQV4TlPOper6FhsmiW250PCQnWjfEqVbkqLjuGJgEh0AXW4R8Vveqz-Pii2GPRqLFLagq1NWOmUUu-x3D1MPedbC1-sSWYUZTPgOpa2tqGpKpb4IARqC-oW5GNJLoldfyRpw050kSS_DIfTtONb7iK4hRovACGWwiN9tLBgeikaPuMYCaXss1pldadqDUVRtArS89SQqnRuYwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات وعده صادق 284؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79837" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه
و ماه‌گرد قیام 18 دی ماه هست
روح تمام جاویدنامان هر دو اتفاق شاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79836" target="_blank">📅 20:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43dd96db2.mp4?token=iTEvBUe8Q7prcI0cn6OS1vG8pz20pEb6hhrw3Fobk0KG8I1O6vAi8GfK0GHvJ22W0FVIZAc2-fsXfbZoYpAWoDg1G8RnnWa2KMKhmRnCpXe4QinnQS4NgK5XdpuwVziRCzvwZ-YE5ixtNup47otPscdPJxWuuBDedkzQFxWGokv1Jor2j_96N56nRV-6vMlEVneOOidiJdWJh-O1T0a3uY4NiLki3tjZ9lVWRg--DL_pxOlqs2DcVHLyGKGVIeG_BP6m15M74PQbgpdbzpYzEyLFCJdf1dTiVaE9hFkACwQbNT4gt0wA8A7W-NgsnK6bykoA8lJGhq-gp-fTrnA--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43dd96db2.mp4?token=iTEvBUe8Q7prcI0cn6OS1vG8pz20pEb6hhrw3Fobk0KG8I1O6vAi8GfK0GHvJ22W0FVIZAc2-fsXfbZoYpAWoDg1G8RnnWa2KMKhmRnCpXe4QinnQS4NgK5XdpuwVziRCzvwZ-YE5ixtNup47otPscdPJxWuuBDedkzQFxWGokv1Jor2j_96N56nRV-6vMlEVneOOidiJdWJh-O1T0a3uY4NiLki3tjZ9lVWRg--DL_pxOlqs2DcVHLyGKGVIeG_BP6m15M74PQbgpdbzpYzEyLFCJdf1dTiVaE9hFkACwQbNT4gt0wA8A7W-NgsnK6bykoA8lJGhq-gp-fTrnA--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانیا با ai هم طنز تولید میکنن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79835" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jur9NV3S-x5wXUQCmdEimbSbG3viSTbpBrL1zVNQaLZ7yDlZNm37U0T74KvktGI9_wkRJAY9PMIpGIw217Hrtve502r4bv4UgUdp0KlhfKMXlbCOtnC-fVA66dRkF5h0c8amE86Tt1wXbmAMPw4-lBeME4ai-oCOj6AqTiBAIzmxECNvv8nA6ayYjNgGTvxYDyKA1CFd_NHp9muiZjYkj_wjCY_NDpVsSr2UJuPVHocY3ggQJk9PvBNAjteisXzqZJ_6yHOKuUc3WM4TgojTGxAwYp5AdMYhI0zGZaGpUi0aH3Efk61JocjtWowVT-BYjfDW15I4RBVJp2ss962j9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79833" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY703GLHVti5mBHYR9Jhp9-TYlCKuiOzSMgV98zwjZRFVXHt5odsoJq3aEEnhvICFaTj3Wq4z5jvbAtbVQGPDkWhfXmKYiBaV_TguWF0HdcSj-RIJ69o1E-Qwr_wx7DHipda5sCPrJEl7vHsyP5j_yKXdYKiNxcsv4wJthJRm98RHPXq39gNCG5UzDi8C5WkzZ_Q7DRTmFBnmpZYTP4EoT9o8amnHe84zmwwdfgMNwYS8q7TmSOys7VaJ7wCgMHJmjer3RSj59g1pxnVLuWLGNNO6rKaQbKKAlLE0l68jVQbbomRp0JTMpVx3yZQZlhYksx7O4mCrsmktkYJtlf7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79832" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esl34l2aL82fbiHbV4PzdjPq_aKweKGscQPiHAcWc5qtcSmtoE9yrfa8CKr1DR0zvhHUX1ZHI7MJpWEbSVZ8A_oxqMJxV-JFv8mCWi9Pv_T-ShnAS30JbVKqp-0B_yrUGZHsXmFh8zm8CFmFZoFUnD6_RBjoxMStSsBtKa8TzetthS3Hj749d8paMPcU6UeksSt2BW4gdwjr7Xe7mE3fHXiG4lw3zD0rA0UL6tvfxedOsNBusdxMMuaeu7JnRn5zkFL755Z5KQ2Ow9QXBsW9GX50MXi2f0K8sKeE6ZqQR7zjEidiBwsGzKHskKE8Z6O1pkiYR4Itmg0rWbSGS04OqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس کامل استوری چادی هوپان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79831" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sua4DwztJwRVgn8Iu5jzgmayji6K6FJDxS1nexJa3_Ml7gc5M_qdVuys-ceV5HBS5vCcFr-xglr3npb8aYhOvcqZQHXU-x_ul_SeFzC7MJoU6Y8iYeY3y5xKFrz40_hZKO358tFja5Nzx2G4cEQAh6Z6XUWHcvSsL_bt73xxX_RU91cAHkGQzpI_TUVCX0u3fn7YqJ3w2ZKk3musFWlXLc1k42tYdpvV_FgPOuHYtsW3_iVL6nKG3BGeCrEZ-DHeoeo3azTBDH44wkQypyY_t9r5KaJrw2lEUGoMjB4URhLf09K7U2SvZ2vHJLugELp1cssUibQep0ub1YcurfCUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79830" target="_blank">📅 18:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utpYDiXDhuk5xTwMwL6b6NvYzAN76VxFrrvAOJZpU3yi9Payqae4eOc1Mryh4GWUyE6Y9cCVkyqaji5p0oT1JjvYe3hAGj7kWOMTM6UmI3pir6kzh7O0FzZKSOGfQJcYYoKtIcQVJMAwyg5VAGFmeBYHrFvCIDUnAat0_7UfA31M1Gxo8zFWbKf2Or-gci8GDWDhl7calUm-aBR-f-oqYidtuy60dQcuPIA1zYvpp6qfpjg6ztQCmh7Ig5ZRgByKLloHIdxXyodjUsTMv3rTPIcITNu7LnNI3ti1xJJNQcS2QTeqWdokdPeCrKRHQDexY_oVpo1hIUhlZ7lSWM97qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
هکتور فورت رفته تو رابطه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79829" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzeLHxquObmPcoJzQFyLCNkDgLgLR9KyTDqfsaDENK1ab2e2Ze5PRjZTZSyu1E01upnzIuImunyu7eW2hTdt__sHko4-fxihUu6xIPH_VEAjrnKYi1vx9CK5LKwrZRWd767Lqq4YMdzV2aujAz-Fs-fhOcKPNjxV7_gDtVXCTjeTcFvay9shhcbDyzDi9EPzxRLELpdOIDiwr7S8Ss562qlvQLrjNKgTueILzaWyZsJ1Be4qHiQVV6FiYC6ssqBaDqaEzxFMgJWjoVBZCZux_C9HyeQPvw82ewH-dINf7AW37nIok9IXFIV8Jd7Cb-S4zE-HT2r_6mjIu3EkFWYmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqUbn7nPIXHkhnyVfW7-4cd09Eqf7O21_4EjPUSKd5rv0e6kjgT4J0mfI7XWCr7nGTnlXWJuJEY6l-HwvdV-_wrpIQTyHCA17dJKjF4hJPUJbjM2nK9beKg-VJeRBaM2ZRu9UxxfAldZ_fmU9yZcMRHBEIeMUhzPEkMXvI_R-0JwnNA1NTq60traoKq45ChgveY0VhxGDQA7iL9agg6uNmsTtakLwy9lfzj48eGH2l2kQTtuRz7PO_hsN_8SvQchRhychiFvVDZpTNeYOBUaZ120Rjb_19FZ-nhqjojPjqG6ib0yOTGnT5ugWgZiUQ8ZJbiAYVc6aubFa3aIsedbnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط لجندا ربط این دوتا تصویر به هم رو میدونن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79827" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK5KjMez7nKlcAlwv15R4eW4Z9RhUZhX-KnjYpGt6h6jOblv3cTqzgW3tu7XtUVHWcWFj3Iq0QSB_v647qivoHNemwmXA6jhxyW1DlbgkgUfRbsLEg-pVV5kU-Y_w1LYzwlRHvPd6ghpTBPcB33gg7XI-ORrVp7lkBfkuO4seb15tRURNBCBu42IyLfK2x_B0XlInk2gOpFirg8JtYsqwNNkIrcYXvDv86zYqB8iyV-wGBywdkNU0jQMMzFPjMy91apVv-cb96py4pYhNNCvGfx8X0I491Gr-YCPZePgTbDzeBwPRbm80ziHZdQL0Ios1uZYDnJCD3FS4V7sJHkxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
دو هدیه ویژه جام جهانی ۲۰۲۶ (مرحله یک‌چهارم نهایی)
🏆
⚽️
روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را تا سقف ۵۰ میلیون ریال به عنوان اعتبار پیش‌بینی رایگان ورزشی و در صورت موفق شدن پیش‌بینی ۳۰ چرخش رایگان ماشین اسلات به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/FWC4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r18
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79826" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.   Spotify  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79825" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca2C5RnOuZg-54d_u9XELsQEaItmnEK83uYBuxYBzhCQk7462EahgoIPfrlBgkx-IBzqvpKytMKNuPI5Sz089vpufzFSWjilfiQe957Bry2Q9McQ2fQxk36WF6gOEhBMrHpSgTlSCZx-6xlxUcZ_izqHRHjoo8-qJ3FxllpCJPNqJQAwiHmZbYh7uO_iHFvo6FOmb8kwvp7olZfxMtGElNeAJyPrv8BgRtDbenhSXO0-Ez7hvefpbJLfFuLpLAEyekSwm9eYfeuDcVLqnjXF8A5KY5FwHXUhqwdgG66mcgxXopJ9bEabABZoD1a-dmvfFNGPrtpKzUrdI_2z_EJp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.
Spotify
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79824" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=KCrlCmiHQjLq1PtA4fSXKcyeBzMSYWoSYbBTZqP26-eThuMAdlvjLl5Pq8KiCx2FfqIDxXQdsU_W5z1C3l6n2IhGciMiOQFDgTILzWf6Eq10oAFlubrVc6Ktr-apkY5pTtTv1butlRe8nLqTcbUw0xCZisGwnGg6QvsXnALltuN8uO8AnvDB95pAvvwnZJjHBByI0YTKU1tuy_urs31S6Q6jvIFDwymMTbnILShLp4O3JmxN5QonuxsYVQI0fj3-o2zJ88CwkHiE_UsffOSzb4SKmWf2jTNEzoaKbKJOR7whvmtoUUrTaBKkkatAm4R3JdGGKM1lc3Kdlush8Rt8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=KCrlCmiHQjLq1PtA4fSXKcyeBzMSYWoSYbBTZqP26-eThuMAdlvjLl5Pq8KiCx2FfqIDxXQdsU_W5z1C3l6n2IhGciMiOQFDgTILzWf6Eq10oAFlubrVc6Ktr-apkY5pTtTv1butlRe8nLqTcbUw0xCZisGwnGg6QvsXnALltuN8uO8AnvDB95pAvvwnZJjHBByI0YTKU1tuy_urs31S6Q6jvIFDwymMTbnILShLp4O3JmxN5QonuxsYVQI0fj3-o2zJ88CwkHiE_UsffOSzb4SKmWf2jTNEzoaKbKJOR7whvmtoUUrTaBKkkatAm4R3JdGGKM1lc3Kdlush8Rt8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواپیمای حامل تابوت توسط جنگنده Mig29-ub اسکورت شد، نکته اینجاست که این نسخه آموزشی و فاقد راداره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79823" target="_blank">📅 16:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اموزش پرورش همچنان میگه امتحانا سر تایمشه در حالی که یه سری از حوضه های امتحانی کنار مراکز نظامی قرار گرفتن و احتمالا درگیری تا چند روز یعنی اولای امتحانات طول بکشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79822" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2tfnWHu5O-KJtRdjMeuDlMGnTMmfMcoo8O225O1dftQM2cpiozF8W3tdPBuUMrnoD793oswy1G4leLyM_kQn-c3ArHiglPb98eAOLPY6JG0BWfyRaTgWjeYZ6u01WPkex6o-a25TGwW0QANOzevuAYcaE4XSecu-NII50jwIDo_nqLJWjUspMnbtwxqOag-Lu2XVuS2Z-mgB58q0j3g06oD_APoV7W5KZE3Oh_NLDAvajzjm_8keLHp9UFzWSRVdIZHf2pWLY_7vFEhjyjwp2evcJDmUj-kOYGnr2hf7On5B8oNFUj4O0i4WH36t2E_LnDrc60MzhLVWtxnN9Qk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این 3 تا هم تو حملات دیشب امریکا به خوزستان کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79821" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCiU7V9BrfkT4nGsRtdS0A3JtOsJ5SZUdY_5H31u60vqLLFDTz4LnyLE5mSRtBRahOc6QvxnJlo-xVpZ6DtKezudrXTkV3izyyZtZK97DiwW7TgUQDf-8LsgcvPkelsgKg7K2rPhnyxeN-C9wpspfP4kPUcRf4tNBEmnSvQJ5GrVfr1y6zcsO7GRabWBqQ7AOdMzwU6800v9mZfbgqfhCeAqRqDbIzxOtkxH2C-QjvcahDD2LEd9a3mXVMmzwpaJ1LwzYSZQhyas_5JGvCbjc3k9hYArbNJvI-e8FQasEOfqJMlJ_DxmmqHYRMCi-oBkzQGtU4JGBpkEcHdf0pMGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان دکی با موزیک ویدیو ویناک جق میزنه یعنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79820" target="_blank">📅 16:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79819" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">درحال حاضر دکی کیر ویناکم نیست</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79818" target="_blank">📅 15:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79817" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmZ-xts0mkE125ksndDCQSs2UK6WV_5XhDKIwSRGrzNk8hQMVKiu18UQ27xbHT9xYuXHugy1CkUGtwFh9JgkukOdTVTylcn8ZFA_bvk_lXiDdJRiUT_50J5PN2F7biPEyID_GC5G_8-od4pDytQshde03YOUmzuxSKJfZVyEm8dk4wO5pd63UWqgdOzxVcb8D4ZgyzKP78EZmSHyAJSjsdZRG49G2j6-Vm_Nfobsf6PpkkITRPwCKkdnzZamnI0OwR6NHnHGTpDsHAGilsEx1MqRqesuutad3ZzerZuPbglR8DshChdLXEY_I9k-Yo49v9CjFtJ_yzOssXOI7pqPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79816" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tkf5xHdqOuCSF1RFPoP-2yCp10nWvlKR1KgwKpCh67gE13XuonkzolrFNbthN-ICyDMpIs7lKdeuf5rTTU7IxE14jE03JZ5HRurEjByQFio2VoNYCpUPK0dhCMHE25jJrEWRs3JReWuG41YtXncu_d_CT91_CuGlzrM_L2gb0sQ14a9We6U6Jesr9mpA82BtTlNFE4nybNaQXTkhr2qu3J1xtA1rfVwtSI159gxtE5JtitCjTdzP0sklryU3ieeO7Wmh_GGOL76w5WjkepKXllPQUPrEG9Q-J8XSIEOqKZrvRG8ErcTVOXkWs1tSAeYGU--HH4ApQxrU1NNLcpuP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک ویناک اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79815" target="_blank">📅 15:50 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
