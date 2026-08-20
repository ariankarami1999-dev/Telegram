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
<img src="https://cdn4.telesco.pe/file/V-IDURumeBKRfzRWD2XFEYpkC81_byU5ueuSUek1tmZ6q8Omaffbwo876uIg47sJedshZnnTZ3BSkELKc7iNMKaS8y4DA0b1-pUi8GamC7iEH4lN-bpVwpBfkunEwqN3fP5MW0wbLeHWBIZfDF0IS-pY-wiSDyjRtqXRclY65FS_hQMryS7b31KNg-qhlW0xNH_eVorMb3i7dx0CsyeePrK5eYi2ki4YpK2-xA4aCNg49P3vXkC7ZbeAI6ecd9SWG9WXNEb1XjPCMdO7qz1zpFMvY9--xco0OblMJDBicrRM2bFxRb0vTynrROP_81O7uAaQmCS2xdECmmdjOQwBQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 994K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 18:32:12</div>
<hr>

<div class="tg-post" id="msg-142849">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCd6D5jvrGJr6aeqzanteqgHAtIftAwqMo-MQVH7qmBkD6VHvgyWF0YGnQmpKIPKb1iVPsp0p6kxcLgbq_3XzNCGSo2JC_lVxWYeZHEYjkKIslKgt2I8dyV3MNcjDkQ3wQnTk8Fug3e1RC5Ermgr0KWMy30D59VQ7WWbg_Dlv8BWqC0_NsnWHffOZUlag1LMhtt3TDrpeA3XBkHwkGYB2Xsx4VHB4z9y13YxDmJaXn8rhSGjQ3_cMnP-uJhiy46cO8dG1mUU5kQNLEMl2HTsZUUIiBwMaN9d7Q5f_qzaFD7dolrXWUeMiPK2lMq5KTBeR9YCVWlvh-5en2Ra8v00ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/142849" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142848">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwb1ePm_BD2zW7ZfqgMrZ8_pVDYK7LPFikC8nSoU8t3RuYfJCbLxLRMTCgSnETpND-CyL0dYRNHoUmIgw6zvV-ZgYVti1Dh4-SpD6QZnHfw0zWaJAA3FP_ooWCstC0REmOSL1eouEmvAbPdSo6GnW9eTIbpLS2LbR9JUK9FQpJ6V8ueVBbjU_oqq5FLbxjpbl3zxn6_E8r6iftyb9WJRxUM9mxjOLY_ifAU6ts2XgtIHRRbnlx-PTtIKmCbR5ozUNR4PnMXYsG9MV8lirqreiE0Ei6NXgQLear7igfUQpj3K7xnNkmro6L7sfApSNKWkaQW2hJwbG4o2rYa3CoTlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت امور خارجه درباره تحریم‌های اقتصادی جدید آمریکا علیه ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/142848" target="_blank">📅 18:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142847">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB0IMl6YI43laCi3PokJDudkxZMcxX65rg91Dwdoji7C0ye3ZGDkJuaj4yo6INNxbZ2BTEW9A0MAp6JftdYpK2saGOOZBfoJyjK2RPI5k7rxagKmnaIl8r52SsH80hIvZlXuI0Iwtt0oTEkRyhKNVVg2RqlTp_CBjR-g7zAy0UfI3y1UOBkHA4NE44uGMtyc10joE3DNxmkQduXFG76U1MOYE2NEHrMJf0hkD0Luw3_7qJnOY9paLvyEEf6Po4m2sdX106coLO6ocVPnAJwNghoe4ZHYwSopjUDkXdUiGJR4AUYiTlkOPX5_RQut85S_G7FFIDBx0Yke0STTsf1gfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخلیه کامل اسکله بندر المخا پس از حملات اخیر یمن
🔴
تصاویر ماهواره‌ای نشان می‌دهند که اسکله بندر المخا، که تحت کنترل نیروهای وفادار به عربستان سعودی در یمن قرار دارد، به طور کامل تخلیه شده است، این اتفاق در نتیجه حملات اخیر ارتش یمن در هفته گذشته رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/142847" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142846">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انهدام یک پهپاد در نزدیکی میدان گازی «نپتون دیپ» رومانی
🔴
جنگنده‌های F-16 رومانی در عملیاتی ضربتی، یک پهپاد انتحاری دریایی (USV) را در فاصله چند صد متری پروژه گازی «نپتون دیپ» در دریای سیاه منهدم کردند تا از بروز یک فاجعه در زیرساخت‌های انرژی جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/142846" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر امور خارجه لبنان، یوسف راجی، از ایران انتقاد کرد: مقامات ایرانی باید دخالت خود در امور لبنان را متوقف کنند، به ویژه پس از اظهاراتی که اخیراً رئیس مجلس ایران مطرح کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142845" target="_blank">📅 18:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142843">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCeoLrROsp68g6VWeLCrbbl_7Q8tiIk8-VmHEGEawXITUJjYPY5W5N94tjluear4f-SJK7q8i16UF7GebedUsGs0qWmtDCqo8ZWlrTtIM1dhS8nmuk9kY8eFC_4Fff6iP_OfDwnVhBgSDZfHeLKOGJuEU2wZahINfuqz-YUjSMKOzSG0iBk68Nic4Aeez1ovHpJYnSCm6pztQngY-jGJi5zpiz9Gr-UjrJIbfTmNwnTHxlkTTS5yCXA8yhSrRBZsvn-on3y79P_mfOKWlSYVpi91j1atimjGpl2RQCs5H9rFzTjDGKm2rQneYtFN2ei0hMjL6vTL2R8wCN4ihvSY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kg9Jg0eJJ-r3RYrtxoz49VVTX0krMn3XOX1WqmlsGgN3U3B-ugmQQ7tM2gkzILDKBTbvDn5lDb4oq2W_lK03i2O7k3Gjh2wPrOiwsy4T0xxls97-ZgMD_vaVhm4G718raA8efKrkvppvF_Qk2MyAktgd6loPG1LV2DfAisrkaaQrS-M2VT_o-0F_m4yf__xkDDuSHV9yN9naTkd0dKg4pMtDGQ_O7jYXaIl4d91fJNLcu2t57NUMka3ntt6xpkCsFvAgR9tzReuuJP7nWAP3bFhuPzDIh5hTR031q2VHzaGebEpsF2fNmvfW4CgTWD54tLsOEXUttv8G67vHUVv1LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 از روز گذشته، یک ناو هواپیمابر آمریکایی کلاس نیمیتز را در حال حرکت در دریای عمان نشان می‌دهد.
🔴
این ناو احتمالاً یکی از این دو است:
USS George H.W. Bush
USS Abraham Lincoln
🔴
همچنین دست‌کم یک ناوشکن موشک‌انداز هدایت‌شونده کلاس Arleigh Burke این ناو را همراهی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/142843" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142842">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیافه نقدعلی نماینده مجلس، زمانی که قالیباف می گوید؛ به نمایندگی از رهبر انقلاب به عراق آمده ام، سوژه رسانه ها شده است
🔴
نقدعلی چندروز قبل گفته بود قالیباف اصلا دیداری با رهبری نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142842" target="_blank">📅 17:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که دو حمله با استفاده از پهپاد علیه اهداف سعودی انجام داده‌اند، که در آن یک سایت حساس در فرودگاه ابها و یک تاسیسات متعلق به شرکت آرامکو در ابها مورد هدف قرار گرفت.
🔴
این گروه اعلام کرد که این حملات در پاسخ به نقض حریم هوایی یمن در منطقه صعده توسط یک پهپاد سعودی انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/142841" target="_blank">📅 17:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142840">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX_q8yQRQ65k5SesK93XJ4kpTUl6fkzAZFvo3thGlDig7zv5lff0aqZzIMZ0U4t-CCn9NxD_axV8AQIRhZsn1D6RPAd4cLThS31DklaW3XUkizWin6RUmJZWQd7Rn19AQ8xDgwvzarW4kFrsFevRp1B8HrBEdrFnPwqJgmych1x6vI9MPqleljr1EEkrup0Q-vVJ2tUNOiSaBTdWkF7v3qHymoyLENe0iZMesBCp9nWReiKfHS9_iw7mfS6fVR3F24SaxupaUW0hty9x1pdM_hut1YeXPt-cGs2yuO3uIm_TkI3rKTyo0hO7zWAUQRxHiBPJtB-uHR7IN0kOswR7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه اجتماعی Truth Social: جیمز براید، مدیر امور مجلس ما، در ماه سپتامبر از کاخ سفید استعفا خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142840" target="_blank">📅 17:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142839">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
به گفته دانش آموزان کنکوری، قطعی برق در دانشگاه شهید چمران اهواز موجب تاریکی و گرمای سالن شد که به سروصدا و به هم ریختگی نظم سالن جلسه انجامید.
🔴
دانشگاه شهید چمران اهواز میزبان هشت هزار داوطلب کنکوری سراسری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142839" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پلیس گزارش داد: کشف بیش از ۱۷ تن انواع موادمخدر و ۷۸۶ هزار لیتر سوخت قاچاق در ۴۸ ساعت گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142838" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش گرفتن هواپیمای مالزی در فرودگاه توکیو
‏
🔴
یک فروند هواپیمای شرکت «مالزی ایرلاینز» که عازم کوالالامپور بود، هنگام آماده‌شدن برای برخاستن از فرودگاه ناریتای توکیو دچار حادثه در موتور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142837" target="_blank">📅 17:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نایب‌رئیس مجلس: وقتی قیمت نفت بالا می‌رود یعنی ما برنده‌ شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142836" target="_blank">📅 17:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRKPHkcdEz8eoBWiY2U3pAmJMsh9-C2Vg73wFnziDrg35qy0LHYQLffwYFd2J8wyjO0gsOb8H3ofUq8pnSWO10qaxZ9xsBDfv-Jv8VZtkRsFOOCd4xUemF66qD1rNBICnhKTo81JX8evIIHUlj2jd_AJA6ArwY93TD-sIKpKl49mS7g-dbvpvk_nxEYJe33ZtSGhuSo2BWaltfnZ7o2-ShGa-Ul22d8qfA0NLcn6lPoDMheruE9LTG3HhRXy48ijG7LkZl-0ZJwEryeimuAEBCSU551ZVJBCZ4F2Kzg3QbsHhTYxU73G1a34vSomHeqH0bmB3dJibDNgBFj1Vi46-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی به ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142835" target="_blank">📅 17:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر امور خارجه قطر: ما خواهان بازگشت وضعیت تنگه هرمز به زمان قبل از جنگ آمریکا و اسرائیل علیه ایران هستیم.
‏
🔴
پیامدهای جنگ علیه ایران نه‌تنها برای منطقه خلیج فارس، بلکه برای سایر نقاط جهان فاجعه‌بار بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142834" target="_blank">📅 17:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
پوتین: روسیه قصد دارد حدود ۳۰ گیگاوات ظرفیت جدید تولید برق هسته‌ای، از جمله نیروگاه‌های هسته‌ای کوچک، راه‌اندازی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142833" target="_blank">📅 17:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142832">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRjhQIEccTGZbi3HVGYey3X0eQ3pkXSNoNc8xbQBLMjSRiMinXXM6FLp59F-kTdSAlay4fV5ex9PHzk629RQoSV9cKvxt4SlPbfRGZsWHhzWHz9pXUK-aTM27qpuFklNIoOhh-pC3Ip-8hvuaJRO1Nl0eZSzvbiTlKko97_EiUEeAvcyzedAfZXjD6hO2k8eFrJDKwx80uxR4ZS2BGeoxmWR-Qw58KxluCRbECDDTXJXf1gUpJ7mwku7RshniifIQdq7Ya69C3IC98kxFSDLtRvmuUYVvM5a4Af-uOGWFZl-by3uJzpnoMgupYEa3PhLC6lfnD3joTOLHHm79fheDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت اسپانیا اعلام کرد که موج گرما در طول سه ماه اخیر، سبب جان باختن ۴۵۰۰ نفر در این کشور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142832" target="_blank">📅 17:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پدیده‌ی «دوست‌پسر اجاره‌ای» به‌تازگی تو ایران خیلی فراگیر شده، مخصوصاً تو شمال تهران؛  قبلاً این موضوع تو ایران خیلی کم دیده می‌شد، ولی گویا الان خیلی بیشتر شده و دخترا هم انگار استقبال زیادی از این قضیه کردن. ماجرا از این قراره که بعضی دخترای سینگل می‌تونن…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/142831" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142830">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t13fTNE1f7T0vZhxsmzl7FSrOlP4TFoZJqjhbJfrmMQXaEejgWIE-stctNAxdLB3dxmwaEtvYUkJB7hAUiTFwCa4mwyS5XravCG6ifN1xD5vU0JpoptsXiLnos0YY_91Z5z8dl3OO0Q8cakMTC8uYXgBwc-V7sVaO7hturFH_lvIbq7c6sCOBFWvaTzFlZyv5rTbJ320u91tpB8C_yG0Q7-bAinCgZitJFHfiqFGpzX4F5JZe-eSnDnXFx8cDfmPZBq8ZRMYteEsr7OKD6X5B7Yue_6HpDHnVCnU1tQss_Yfo9ClKGqiM1LlxbGcGN3jEulxzALyL7mM0VAt7np4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پدیده‌ی «دوست‌پسر اجاره‌ای» به‌تازگی تو ایران خیلی فراگیر شده، مخصوصاً تو شمال تهران؛
قبلاً این موضوع تو ایران خیلی کم دیده می‌شد، ولی گویا الان خیلی بیشتر شده و دخترا هم انگار استقبال زیادی از این قضیه کردن.
ماجرا از این قراره که بعضی دخترای سینگل می‌تونن برای چند ساعت یه پسر رو به‌عنوان پارتنر و همراه اجاره کنن و باهاش برن مهمونی، دورهمی، کافه، رستوران یا خرید (ولی قرار نیست پسر هیچ خرجی کنه)؛ یعنی طرف برای مدت مشخص نقش دوست‌پسر یا همراهشون رو بازی می‌کنه.
طبق شنیده‌ها، هدف اینه که فرد تو جمع تنها نباشه یا با همراه جذاب‌تری ظاهر بشه (هرچی پسر جذاب‌تر یا خوش‌هیکل‌تر باشه، پول بیشتری در ازاش میدن).
طبق گزارش‌های منتشرشده، قبلاً رقم‌هایی مثل حدود یک میلیون تومان برای چهار ساعت مطرح شده و گزارش‌هایی از تهران، شیراز، کرج و اصفهان هم منتشر شده ولی الان گویا قیمت‌ها بیشتر شده و برای هر ساعت از حدود 2 میلیون تومان شروع میشه و بالاتر میره (بستگی به پسر داره که چقدر جذاب و خوش‌هیکل باشه...)
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142830" target="_blank">📅 16:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142829">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ39Ol2p0gS50d-0_kC9wEPlpBU5Tk_PbR2OuisgVD9aOpaIi3oZMBW_84R_09NLHOHCj42b5oBE0VH_SUEscDq3dJLCWfaoKsm5r6xiQ4iOWM31zd4j0W9a1VaG6SAsd72MuBUsMdrDOUh2krCKu4F9MWlBOaP0donjSSd-HPMg6xIZXHvwhoFSzgCy5cdWZHQLWDuECnor8ujot3DdBiaR0Dvr29SGi4nzMDaDJ5-ryDHakB7uMaJ3h8-dWy_LmfMHc7mEqGgYeAZUmghrpP5spmGd9kDQLSyhBP0QyEOnRgFEYuH2xdcUFp5JR-_mYG1hGBEGg2ANMKoYork-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
چین میلیون‌ها بشکه نفت خام عربستان خریداری کرد
‏
🔴
به گزارش بلومبرگ، چین میلیون‌ها بشکه نفت خام عربستان را که از طریق یک مناقصه کم‌سابقه و همچنین قراردادهای بلندمدت عرضه شده بود، خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142829" target="_blank">📅 16:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142828">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95183641d5.mp4?token=oT5_eytzZpXOQmUKwOjyOKrEUuVcM1Bl2YjrN0VSU3jKj7PvqzWl4dLum2_c2_6HqVpWphpq5pDR5X3Z0ccamJQ-IJa944AYYCep4l3C8-O9LBwVjHHz7rtaQIXcLfz4fhusRVo8MofYpw_aqrbi_UiixQjdPWZpY2Bu_CxTYdzWp8RAmJgHf7gtydnSTX4v3huaKdfZITXUeS7WLvfXD-lQHEpEoCn2Bvr4G9nkxszen9ooXt22_PznNLRuzvBgaEkxHYlGZmsLwKWp-63xkaqEDBr3kQRv1YiwjGGkbIfcrvg4K6frPrQJUvWR2cO9wpTbKB88NwBO0lvzyKAhXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95183641d5.mp4?token=oT5_eytzZpXOQmUKwOjyOKrEUuVcM1Bl2YjrN0VSU3jKj7PvqzWl4dLum2_c2_6HqVpWphpq5pDR5X3Z0ccamJQ-IJa944AYYCep4l3C8-O9LBwVjHHz7rtaQIXcLfz4fhusRVo8MofYpw_aqrbi_UiixQjdPWZpY2Bu_CxTYdzWp8RAmJgHf7gtydnSTX4v3huaKdfZITXUeS7WLvfXD-lQHEpEoCn2Bvr4G9nkxszen9ooXt22_PznNLRuzvBgaEkxHYlGZmsLwKWp-63xkaqEDBr3kQRv1YiwjGGkbIfcrvg4K6frPrQJUvWR2cO9wpTbKB88NwBO0lvzyKAhXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: روز اول اومدم دیدم نهاد ریاست جمهوری، استخر داره، گفتم خاموشش کنید
🔴
بعد دیدم به چمنا هم آب میدم گفتم خشکش کنید چمن چه بدرد میخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142828" target="_blank">📅 16:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142827" target="_blank">📅 16:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
یارانه 1.5 دلاری مرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142826" target="_blank">📅 16:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWHhM38iEpxidKBgEFfSAL3isjjEUROB21sEzPTkScB__vM5-g30Jw5JFob7LpZdOyA333S-JFLyL_v8MWYu0xUulhMJMxaIF_JvPKjDEB84yEueVs8pqPC1MEHvrerpfM9J_3eEHidMdlhNcb8l1TLYOGGa4Na8_OYOZZ6URiGdrgnhVN9hHpm9KG_EhYO0FhcHpmvC1d-VAAF40jxbFzHwrxfGixF8tU_vBM_6iB5IpP7fE1pwNz4GQHlLeAi-M6nTxnV5JCOIWq-L7rLbkEtoduICba90qNDDvO3k_rMiPwdLODu1UBB39jQPVspVBSzcZ4gBbA18h2AYHvDYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۲۹ مرداد روزی که جنگ ۸ ساله ساعت ۶:۳۰ صبح با یک آتش‌بس پایان یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142825" target="_blank">📅 16:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGeDNSf80-VOpiWNwX7GWfqKZgDV2UzORVw8hIsnqtIuGMbgBDaQ9iIPQ9mcNcHRPOFIIPt0Rw1vNE9hcg86-sJB1syGUjPEm8LfBd86RkVO02ffa0mBFbN-LckMxsG-kN4FZnBOhCBjyLFnEYpgtZIyLBeZ0TpyOTaPjDzuRxBX2jYMhyoZxB5MzXh-Z1jTZw5f6EQbmQFKX1PZMvJr1Kot4kpzb7n-p5_KHRHJHd2CA6bgTorerNwOinK90BNA27RWbjSKn6Ves8nou02Nqk5-MhPJMM-kOrc6bOLkUjMOakRTssgn5ieDo20-Bx0WZkIIRz72GdaQ1T9qtZEQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم حسینی از اتباع افغانستانی، یکی از بازداشت‌شدگان اعتراضات دی ماه پارسال تو پرونده‌ی میدون علیخانی اصفهان، صبح امروز اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142824" target="_blank">📅 15:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142823">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvoiB81RfRXM5FppuDhzQoSc_qv1EfjPqoUyF_TU6ZR8nUOaNlgeFPUZMuAxC2VKeVbcTlCLQsb5fVfg-L5fQ4Ux88rmp8PWb0eV83G39lDSrXZ61Fw9olBjkDVbcbphyOXkDGz3H0gpzFu1avpSbD9vj42cOZ_tgBhrAZkJd5u2ONAoNFeovzmEeEss7M2TlDIa0xpR5ZkX8Ti7oAjz5FFF4Klk27g-ggcl-jfFLqkgcKvVjY6E1Q_aYi868m1X3dXQu74DDvsX6HHHWTKw7Hct-61OWm7lhfD9rQ8hzenYdlGvBUMIM9jhMQPR10Jf80U1j1SroRBfpsW7kja7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عباس عراقچی :
تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی مردم آمریکا از بحران‌های مالی داخلی و مشکلات اقتصادی آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/142823" target="_blank">📅 15:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142822">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDH0qIzSYi72pcyepINu-xBN5x7vUGRyaNOKCDbYSDJ0_cYDLC2OfLfY2vTk6luH85O_vlNi7EtGx8H9sVf53xyYro9_h4z2ZWcjSUD9-KeO0_3oGNJ8jZGAZllYDCoa8HgPK4odkTLCrL1YnVQoU31pjwjeAN4B1ZkYwDXSV6BHe9Uu_INMAUyg1FK-BXksLBOjLCG9iErd0X29o6kWfTHrw90tvdcHR3WOfWXHGBgYu2zCEUmZEBthhSftdNA5lVPiJ2iTRB8obpp1BxacInSTIMO2meeezBZjchnkJ7OiX5c4mrTePylNfoHC6ApLV_wOpyIvVjlQDsdioTlPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، خلیج عربی نوشته شده!
و خودش هم بالای عکس نوشت خلیج عربی!
او همین دیروز با قالیباف دیدار داشت!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142822" target="_blank">📅 15:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142821">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f667bdd.mp4?token=qDJoIJVVe-IbPFli43ab6OOyjfpppB52n7bf751Q2fuCaDQmGlzSsleH2vnvfGJUvXFemDvZ7RN5DpGSdVBacziMfCYG_5ZTIKeMOxpV1jz38zmplVz62jKdxPOsjzJ7Q2C-FhgEVAx55FA2M7Glbo7VY9s9C5benUifsQ-o1WgyxRg6Ad-slSfUm36KQFPUhph4Axk4trqsinrnPERUY5wIjATwlT2L5Nf52JYgoYrZeIkbwwe3N_TH65K8tEdpKRalZkUtQAanlrXJdxtMXPZHeNhGSl4fJqz5Ymq1Mvhmbg_M-sQQMEqcMFdlGE44nmed3KwSK8W6f0PodTsm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f667bdd.mp4?token=qDJoIJVVe-IbPFli43ab6OOyjfpppB52n7bf751Q2fuCaDQmGlzSsleH2vnvfGJUvXFemDvZ7RN5DpGSdVBacziMfCYG_5ZTIKeMOxpV1jz38zmplVz62jKdxPOsjzJ7Q2C-FhgEVAx55FA2M7Glbo7VY9s9C5benUifsQ-o1WgyxRg6Ad-slSfUm36KQFPUhph4Axk4trqsinrnPERUY5wIjATwlT2L5Nf52JYgoYrZeIkbwwe3N_TH65K8tEdpKRalZkUtQAanlrXJdxtMXPZHeNhGSl4fJqz5Ymq1Mvhmbg_M-sQQMEqcMFdlGE44nmed3KwSK8W6f0PodTsm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رحمان قهرمان پور تحلیلگر نزدیک به عراقچی: آمریکا در حال آماده شدن برای جنگ فراگیر با ایران در آبان یا آذر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142821" target="_blank">📅 15:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏
👈
فرماندهی مرکزی ارتش آمریکا:
هم اکنون ناو هواپیمابر جورج واشنگتن وارد خاورمیانه شد و به سمت دریای عمان در حال حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142820" target="_blank">📅 15:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7407cb81.mp4?token=omnN9UcZvo9-HpZ4TMVaDjrQ492dtiduM1R7SVcwOMeco2q5OXKdVh7FHA5Vi-v4GWQSd86Hfl0UhuuMqiP3_swC5Fm7_pJ3ACsqBE70urh0CF71PotLfcUifUtH0LG24docj4vUuFjOWTeKw-_e0lMmBrPy0XYnuT0j3SJQWAQyoQjGqw0nISkGIbLdFd-lmQ8_3GcDr_X_prHxofADEYpFldn94yP-aFRW4JFm1d9Qoeb31nRcVkiX7A9X-TOH5Sx0YzkJnf2aCgK6hcaue0VoAdHc7_jy25yU0m-1uBVV9JMang5DEK3x47CKFMAg09Dv5nXA60jQ7VRIuoYg6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7407cb81.mp4?token=omnN9UcZvo9-HpZ4TMVaDjrQ492dtiduM1R7SVcwOMeco2q5OXKdVh7FHA5Vi-v4GWQSd86Hfl0UhuuMqiP3_swC5Fm7_pJ3ACsqBE70urh0CF71PotLfcUifUtH0LG24docj4vUuFjOWTeKw-_e0lMmBrPy0XYnuT0j3SJQWAQyoQjGqw0nISkGIbLdFd-lmQ8_3GcDr_X_prHxofADEYpFldn94yP-aFRW4JFm1d9Qoeb31nRcVkiX7A9X-TOH5Sx0YzkJnf2aCgK6hcaue0VoAdHc7_jy25yU0m-1uBVV9JMang5DEK3x47CKFMAg09Dv5nXA60jQ7VRIuoYg6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ماشین جدید رضا گلزار، تنها رولز رویس کولینان منصوری ایران :
قیمت این ماشین بالای ۵۰۰ هزار دلاره.!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142819" target="_blank">📅 15:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15778d6d8.mp4?token=JWEAIoUzsAaHgex9LC8NUEUB0v6QCDiplUMIo63KIAHnHSqnJJJWbSUK9NivcZddhzwXR30S6A8Iv8xmHqRpLHPPaDXHSwS20XRSsmHieJU1Mb7jjGdwcm0YRmbtlBpujnVreoQGA1GINFCjXluMOcULeCqpLXKw8hanknro__5k6MtkTRPYmPMvXVU7rwga2qmLEkf65MKy8nZNHfRSUJetClIQxHdiIP2nfk3QmNQe2fmaSTNhJ9W2OUv2NcYnmeWx1bkV_s-9L5UYzAQ1KTVuzP8Lvt5B1fQK-7xk2qK5ddaW0EJWjzgPbTArigEU15K_aEtcWN7alIdSIt1jxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15778d6d8.mp4?token=JWEAIoUzsAaHgex9LC8NUEUB0v6QCDiplUMIo63KIAHnHSqnJJJWbSUK9NivcZddhzwXR30S6A8Iv8xmHqRpLHPPaDXHSwS20XRSsmHieJU1Mb7jjGdwcm0YRmbtlBpujnVreoQGA1GINFCjXluMOcULeCqpLXKw8hanknro__5k6MtkTRPYmPMvXVU7rwga2qmLEkf65MKy8nZNHfRSUJetClIQxHdiIP2nfk3QmNQe2fmaSTNhJ9W2OUv2NcYnmeWx1bkV_s-9L5UYzAQ1KTVuzP8Lvt5B1fQK-7xk2qK5ddaW0EJWjzgPbTArigEU15K_aEtcWN7alIdSIt1jxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرودگاه بن گوریون پس از بسته شدن و توقف پروازها، به یک سالن رقص تبدیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/142818" target="_blank">📅 14:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwqjMf_PgiQ6OioAytXDvzdBNUZbBv1VOfVn1E3hnRQdOuve_w-zwIfVZEe5MdRBBs0X7aZ5042oS_k_yzPVzqZ-yPQ6S4U941PmQLAYW2E15-5q35jGKmkpq2oQfxGjhIvuakfmvEDmVqifeo-l-6-QCuw1m84xhL7HxNcP-X4M6oU1T9-od-7uFabASTcYxbZmyc4b4lM7jGmT806Xomdn078dOnR7IJWQX42U0Vjtnho7OLJU8TnhkuMKVrQNZgPOp8_-viK_Hp_36tlY8EPtfUrpSeGqh1mddCiATkrhw6aP8ULyhrPXeXuEbMl2V8eI-3eULwUfDeJQylEIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیشرفت نیروی دریایی چین
🔴
از 2016 تا 2026
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/142817" target="_blank">📅 14:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC0a5nvycfovvvlaehcWFWPkCi-LDHtDWXZpnN-BZtU8tkaMevd5IpQ_Zch6AT5H_C3FY26meDv-Qwtdbg2RH7imZUbjq9vxxXs-tB0fpNAXXEG8JnXD7VNMdVQRvyTlfuxBSGKmx3UIk9qPWPKVqk1SXLQBSX-hWOySANkXxQIGkkrLnR3YP_qAelQ3HpsEO_hLG0Bnj-Auce1YiLdPuxNtJiJ9QCyejjaWK6q-JmFk9E50aaaui86ccUiawHcdPh0qDfjhqJOELun8ywi_ZNm-shOmsg6v9bS3-jolH6ljrT2sz4hmxlHcc8rC1WdZYTdrDMiH5yW8HKAB4kMWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
باید حزب الله واشنگتن رو ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/142816" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzkWM_2L2z9EJUdvTxl66cqOSj2AkQKBvWvwOVWxxVSPuBrP79M3QUpjxktdkASqZwLNv9sV3nPUSUDKsxb2E9gbSWhELeKbL4DqBAUqFPVlQwdO4AUquJ6D-eo730VHKC7XcOl_hKkKqPpeB_JxoTHTucHd7paRa2lTdEUJtGgW7KKsUc8QpTwsEWLjz3Q9Y6Z0D19OpvgjKt43Vfk5DcZbhIFTXiSy6wDAsWm1xGvr25DXrG_AAap9FPDxXKedicy7uBFCoFVWCPAHB2IpdNuEJVstMqmCbu41eZYqqPq2zsKjWagYFqzyNH2o6kJ5g0y6KCWllomgZWSlwmS9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه مصر تأکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد، نمی‌توان اجازه داد مانع دریانوری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142815" target="_blank">📅 14:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323763dbb7.mp4?token=hSCnCcVmXICbCSjokr3pHvLETc2Hj-uL6KEvEhNqrkcBEhPJ68FMh96MCb9XIkU8i8rKCF8qmz9k8nmlZCAHNAKUcXLEJoiR3NvsKR5GF1WPuuzHcNgdK9AZ636xqa1mJPFj1tVXeJWg4GwVVVKFMi4ICoZvkGEsCQE3ze3w1hyNPLyJXdfwA0T5ryavQfCZ4PJ4PhutXrqXSKi9GFkRK7nZ6oaGJNMhbf2N6sVSihC0aDluZklVqkccy6gUit7kiW7o_vCML3aUrV0k3X61YGABz73elTdDxJZXmFe6iyJ0tukaD1x3ThFispti5BMHBN9SpJMnvJCtl_w13OqW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323763dbb7.mp4?token=hSCnCcVmXICbCSjokr3pHvLETc2Hj-uL6KEvEhNqrkcBEhPJ68FMh96MCb9XIkU8i8rKCF8qmz9k8nmlZCAHNAKUcXLEJoiR3NvsKR5GF1WPuuzHcNgdK9AZ636xqa1mJPFj1tVXeJWg4GwVVVKFMi4ICoZvkGEsCQE3ze3w1hyNPLyJXdfwA0T5ryavQfCZ4PJ4PhutXrqXSKi9GFkRK7nZ6oaGJNMhbf2N6sVSihC0aDluZklVqkccy6gUit7kiW7o_vCML3aUrV0k3X61YGABz73elTdDxJZXmFe6iyJ0tukaD1x3ThFispti5BMHBN9SpJMnvJCtl_w13OqW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توی استان زنجان دو تا دختر ۱۷ ساله، این شکلی با موتور رفتن تو تریلی و هم اکنون توی کما هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/142814" target="_blank">📅 14:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خارجه سوریه در مصاحبه با باراک راوید: ترکیه هیچ قصدی برای تاسیس پایگاه نظامی در سوریه ندارد و اسرائیل هیچ دلیل موجهی برای حمله به خاک سوریه ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142813" target="_blank">📅 14:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پروازهای مستقیم بندرعباس به رشت و گرگان پس از وقفۀ چندماهه مجدد از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142812" target="_blank">📅 14:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079a21a394.mp4?token=LfF0k8FS7lRjYHsTu4IgyLqku2uTC_javx1-KJKz5FsLS2L2Fg7IDgP5AnVUgAgsttYLgo3JI_y0KjOdr3G4r_BOE7FGVIXq8WaILTDWRP2q99EhJW8LDRr7I7t3ZQN-VoKQ3piScRnr0po3bl3wrrOcu9Orpn-lHStNiZk5wu6kOz--VIKwAWNDnWCuTriJo7yJcMdeKnuLAhzEulLgEQHvg424ITwrfu8fexUjw3nnCNP_VnvNgsPeuc5W4_YQqN2G7W8z2zS4KoVyXaQganyex9uIb3wrhLZbbkzIeyBFKoTePExTTSW9NSjchbWRNU6J4xK3iOwe8Jc-_g6eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079a21a394.mp4?token=LfF0k8FS7lRjYHsTu4IgyLqku2uTC_javx1-KJKz5FsLS2L2Fg7IDgP5AnVUgAgsttYLgo3JI_y0KjOdr3G4r_BOE7FGVIXq8WaILTDWRP2q99EhJW8LDRr7I7t3ZQN-VoKQ3piScRnr0po3bl3wrrOcu9Orpn-lHStNiZk5wu6kOz--VIKwAWNDnWCuTriJo7yJcMdeKnuLAhzEulLgEQHvg424ITwrfu8fexUjw3nnCNP_VnvNgsPeuc5W4_YQqN2G7W8z2zS4KoVyXaQganyex9uIb3wrhLZbbkzIeyBFKoTePExTTSW9NSjchbWRNU6J4xK3iOwe8Jc-_g6eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی:
آمریکا در فکر حمله اتمی به سایت‌های موشکی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142811" target="_blank">📅 14:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142810">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95291bdcf.mp4?token=W9S_tcjkqB9Ge1FvFJhdKkf0ZODfAlNoWL7iRK5MXjGyqXqJDrJV2lNQUV_QT5u-A5WwIlyqdQqiWJg2MbKO1gpMYIrdwT7VFCXozIVLHZpjxdGRBNspZD6Nq8aH1Zf5GcsguwVKM4Kf9u_6NihRsPsF_K5o-c7K_fihyGpryi57lCfGIqgXBOgoVNr8OMRd7dQytto-zLbzGSKuL42j9UewAIaqjudjFbgZYht2Txk5d0JfjOtBvpvhJjw840g18qPNavO8gCA9VmR5Xf6HtOAOfI90EiFoZDPxqzNg23ZUiHUM7w1hNkxY5qhdSCuEQ2LQBF8JUwtpXtFGIE9ofqftQtGbd4yrs0n_Csh4cTT7vWqusr4cmw9u0SRObOdaAQROC03bL44jGt4uYQu2fdgedKBPl12JxnhcZjZu6EdJI09SaxhkOlOppngZNVDKCZPo_vkvcxd2QhTMWPghOS6FoqpxOqMTd5LoVgPiexSFPQjEAlErF4UWWWy7CmOSgypPy6z-XpOUvP4gyggOx2E3UZFO4ht_4IOLEbCgH_wNtzeor45diT7yANIeLRW_tCSo6phz5QyxNujZpNz9OU68HaZmQ2c4jSOK8YFIaE2NkDkIiM3Fj9A8WSTSPz-pQpVdQgKeEQ-uOCGQLnwWv_NJokDFt0Lvon6h7BPNQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95291bdcf.mp4?token=W9S_tcjkqB9Ge1FvFJhdKkf0ZODfAlNoWL7iRK5MXjGyqXqJDrJV2lNQUV_QT5u-A5WwIlyqdQqiWJg2MbKO1gpMYIrdwT7VFCXozIVLHZpjxdGRBNspZD6Nq8aH1Zf5GcsguwVKM4Kf9u_6NihRsPsF_K5o-c7K_fihyGpryi57lCfGIqgXBOgoVNr8OMRd7dQytto-zLbzGSKuL42j9UewAIaqjudjFbgZYht2Txk5d0JfjOtBvpvhJjw840g18qPNavO8gCA9VmR5Xf6HtOAOfI90EiFoZDPxqzNg23ZUiHUM7w1hNkxY5qhdSCuEQ2LQBF8JUwtpXtFGIE9ofqftQtGbd4yrs0n_Csh4cTT7vWqusr4cmw9u0SRObOdaAQROC03bL44jGt4uYQu2fdgedKBPl12JxnhcZjZu6EdJI09SaxhkOlOppngZNVDKCZPo_vkvcxd2QhTMWPghOS6FoqpxOqMTd5LoVgPiexSFPQjEAlErF4UWWWy7CmOSgypPy6z-XpOUvP4gyggOx2E3UZFO4ht_4IOLEbCgH_wNtzeor45diT7yANIeLRW_tCSo6phz5QyxNujZpNz9OU68HaZmQ2c4jSOK8YFIaE2NkDkIiM3Fj9A8WSTSPz-pQpVdQgKeEQ-uOCGQLnwWv_NJokDFt0Lvon6h7BPNQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، ایتامار بن‌گور، درباره لبنان:من پسری دارم که اکنون با واحد شناسایی خود به لبنان می‌رود و می‌آید و به شما می‌گویم: او و دوستانش شایسته‌اند که ما بیروت را بمباران کنیم و آن‌ها را له کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142810" target="_blank">📅 14:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142809">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
العربیه: ۳ نفر از نیروهای سپاه پاسداران در حملات به مواضع حوثی های یمن کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142809" target="_blank">📅 14:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142808">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مقام آمریکایی: مذاکرات ایران و عمان شکست خورده
🔴
این مذاکرات به دلیل احتمال وضع عوارض برای عبور از تنگه هرمز و پیش بردن مسیری که جدا از مذاکرات تهران و واشنگتن بود، موجب نارضایتی ترامپ شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142808" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142807">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuJ-9SmcnkMyaltMZ30-TjtkFliaK6F-mZqlAjkleIeSN0bgkAn3ezD7Y5uhBYOWgYCRFOLrbCjAyl0ThOyPq0bhWRBrjPEIgMboqsGBvsd48GKGVCEK-1KvL4xAkcYibdaTUGVGxouYdvzzAKHDTTi1K68UecPxeromvS77cmrV43DpndqqFT1cqNFb2JuZ0MA3Duqw2jtGnBqx4zYGhX60ZNuFTGxuHq-uQ5_i7Zc_rtb5Ne3SUON3JqM-42oUxtJ1AiDoJtnWTH9zdjqSZg27PDxbwnH6YO9RtY6i69nR_zNRZ7PJY05BVXxyjqyclzP3kzWSN29K2HUGIUQUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش نرخ ۸۲ قلم داروی دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142807" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142806">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خارجه عمان: ما با هرگونه تشدید بیشتر تنش‌ها یا درگیری در منطقه مخالفیم.
🔴
باید ریشه‌ها و عوامل اساسیِ بی‌ثباتی در منطقه مورد بازنگری و بررسی قرار گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142806" target="_blank">📅 13:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a475b96a1.mp4?token=D8opmABSWrqFIQvsiADcnE8yPnelVXNlhS-r8eanfAW6_XwRRbO7Zh5f6BGlXsrF8KS2DGzw2CbpMZ0MqhwERfUyr96Y5HI5bqIAox75R5q_LwPzC6SR7rFRLHtrQVo4ZaHvdK1cW8MoFeNHi2_Dj4R3KZ1RsCOSpNLmxpnLPR0XMaLjzcPgI7XE-w_umGHhf9YT4L-c2HYI0lrgSLws0XSNTjEwLFpEmz1-aQp5QEN_Dpr2YSJdM1xvyGtGR0VSdimb4uo7jDG8pX-Icqrn-_D-k-5gFm_S673A_2Ur1jQC_ggSRPC3pGQbhdGxnDnAK4pGqqk9K41zZlHfrOsm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a475b96a1.mp4?token=D8opmABSWrqFIQvsiADcnE8yPnelVXNlhS-r8eanfAW6_XwRRbO7Zh5f6BGlXsrF8KS2DGzw2CbpMZ0MqhwERfUyr96Y5HI5bqIAox75R5q_LwPzC6SR7rFRLHtrQVo4ZaHvdK1cW8MoFeNHi2_Dj4R3KZ1RsCOSpNLmxpnLPR0XMaLjzcPgI7XE-w_umGHhf9YT4L-c2HYI0lrgSLws0XSNTjEwLFpEmz1-aQp5QEN_Dpr2YSJdM1xvyGtGR0VSdimb4uo7jDG8pX-Icqrn-_D-k-5gFm_S673A_2Ur1jQC_ggSRPC3pGQbhdGxnDnAK4pGqqk9K41zZlHfrOsm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142805" target="_blank">📅 13:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142804">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک حادثه در نزدیکی سواحل یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142804" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142803">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142803" target="_blank">📅 13:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142802">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142802" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142801">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5tf3eWQWYbyHOo-C1r9FWnZwTjDapHIWGBsoXZ8tux4f3iZVc6PVPg-f_F_-R3cTpAbj4vw8YD9Hj_tT2qz_UxapVagDr4FDZk4xhx7jpYBSfWeDB0idtHaQCuhRpr0gm_kqeWTUjg2egnTnAsVtrd8zm3pzGb9YZIJ0uikr4iYBna04QbbS6AUqy-DNrhgH_xPIHCa77yBMKhzmO65D6XehkyGgXziD5dH1TAuZoaNid3zzVjsnvAUDmjbyGmUcKijScfovjh1fXCi5kXIV_z0u6hssn_BcNJ8UHnPTjvMwXcETOnsWDRbIpQpHIQmyWgpjk59tWEomMpPYB55Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حادثه در نزدیکی سواحل یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142801" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csxkq7MzX2jPnWZZZX67v8OiazMwHRsQnjDXFJmlukRkIXqn5nzcRYdmY20amtSqPd3uu4Qku3nc7BG67MtGqIucfuczQRggQtlvuD_o0u3-ezSlAV_xYwfTlkGbflQMwn2ktx9WbioxfWQGxdxnunXvP8eCtWJUaAOl32z5rS93Rk8M_yJv1k8UH6YqO7uOBvEWDcd7_8qb5hbxprNmhPagyltZIGhcASdXy6wisQjq29fRmk0l1RnTjPV7yoESr2QcWrfjevFlfWQ9P_k_6Lcdc8qudpaqKD5AZ7T1G-AA6_3D7X5YzdJ2eUwhbGSkzlET3lir1g4gYfDUsp-L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۳.۸۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142800" target="_blank">📅 13:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS1omGigjYkGtP_Xsd9awUQPyVYsaftbjtnUfzzR51JOXDJZkkT0k17a_768wI50XMXwyvFx_A4UCKwBPGF8CVFC39OXRz-2Gpk8J-eWqn1khwtgs4BzOG9stT6LM34d3DZx8Jg_xFhbJfHcpvVilmKIOkkRZGScoc7jS2TigzpSbuhf6_DGc1zth2gEHAgC8OaUau2FSChYz-Z-z3I6QWGNkOrIXWc950r_fozY2o-JtAW_Dz2bS2oxyZU_SGTZh82xSbZevAaZkoerIvkAXnTDAh6DpD5yDj3WZa5U9eHj9dFcyTo6oUYjz5BdjaM0UTLDxGIxHZjK3Tq6YqQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروتمندترین مرد آسیا به حبس ابد محکوم شد
‏
🔴
بنیان‌گذار گروه «اورگرند» چین که زمانی ثروتمندترین مرد آسیا بود، روز پنجشنبه از سوی دادگاهی در چین به حبس ابد محکوم شد؛ پنج سال پس از آنکه فروپاشی این شرکت، اقتصاد و بازارهای مالی چین را تحت تاثیر قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142799" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سازمان بهینه‌سازی: مسئله بنزین بحرانی شده و نیازمند یک راه‌حل فوری است
🔴
دست‌کم به حدود ۱۵ میلیون لیتر واردات روزانه بنزین نیاز داریم، اما تأمین مالی و دسترسی ارزی در مسیرهای جنوبی، محدودیت‌ ایجاد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142798" target="_blank">📅 13:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdTmS3F7DlIQCb5wNDiq2QvX1aHGS4Vp11Uh3yE3JyGMtJauxyb1eRNWvKMQdajlQZXNPdxUDOpanMVsdm5cg-2zBc0gVRKC5ZFA8MBUen-WJXPHBfmMQqKh7wdZjVDzvLri7zQy55BKAvUVGbgD55L9E96j7R7ApgZB4JATzrsRonv0dhX-9N8WXjEr4wtyclDq1XnlcUIY8dIr0p9X-kQsJHY3vuPlrBh5fZMQ1X7yeeT6n17MlIdstkT9BzVETQxKC6f9R-MGDa4HmV_ZjsQ0QH1a3o7ZL1JtWLGZvg8DC_WJ8MRuHhPz-AIkPYRgGf5AhrhpsUqyoepY1hm4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش لورا روزن، خبرنگار ارشد المانیتور به وعده اعمال تحریم های شدیدتر علیه ایران توسط ترامپ
🔴
ما کاری انجام می‌دهیم تا مجبور نشویم دوباره به تشدید نظامی روی بیاوریم (عمدتاً به این خاطر که موشک‌های رهگیرمان تمام شده، و شاید هم تشدید نظامی جواب نمی دهد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142797" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سازمان سنجش: میزان تاثیر معدل در کنکور امسال، ۶۰ درصد است
🔴
۴۳ درصد به پایه دوازدهم و ۱۷ درصد به یازدهم اختصاص دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142796" target="_blank">📅 12:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قیمت هر بشکه نفت خام برنت از ۹۳ دلار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142795" target="_blank">📅 12:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
منابع خارجی مدعی شده اند که ترامپ به مذاکره‌کنندگان گفته که چشم‌انداز توافق با ایران ضعیف است و ممکن است در صورت شکست فشار اقتصادی، حملات گسترده‌ای علیه ایران دستور دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142794" target="_blank">📅 12:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKHlRWcaljk6_nxsH6c5iwnzihmRgWeN1Pf2XLPh8kElUVBH139aZ1v9cx2c-TyjGVkzc4AEIh-NNAssoARyQE9crsaz7u7cBk1MerZhhODwaJHYcXvpf3XCFaIR3ar8ASqxz5FeEBdrN-NmbFQ96UJKV4FxGdAlJ52aEQrWxBuQmPGLlSs5nwsk0RkPZ3k5qNlxp85pXS1SRCaPUWaNtOuyatT8698dHw29kEwpFAo1KtVTKsNNgt8igDmza7cwT54HUqtVQrj0jx8c0tnIrja3zUc-1LtBrEgEj5y-zirVjpBAo4Bcw2Lm5_OqEJ76RlWCIcY_9L4S2Tuhj4YKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین پس از ۸۰ روز به ۷۱,۵۰۰ دلار رسید
🔴
بیت‌کوین برای نخستین‌بار در ۸۰ روز گذشته از مرز ۷۱,۵۰۰ دلار عبور کرد. قیمت این رمزارز طی ۲۴ ساعت اخیر ۱۱.۵ درصد رشد داشته است.
🔴
ارزش بازار بیت‌کوین نیز با جهش اخیر ۱۴۷ میلیارد دلار افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142793" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کره شمالی 10 موشک بالستیک را به سمت دریای ژاپن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142792" target="_blank">📅 12:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صدا سیما : اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!
🔴
با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142791" target="_blank">📅 12:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=XZp5bbO26L78F1A7aHN8n3FTZT5NeoFTSAgxf7z6yWStA7AoNpQwenqj4tn3xOF1sZJuSqMjjjeOgBtZAOZzZEKWnC5eY-U-DLXxJaLssEks3AqiKYfpC8aZYL3PKqkiQAVuQG-mXKHWJACW7czcxlDAMHpD4Wspa8K8iuc-xTGxJYyEKBaSgwj4ZgIDGDx90WwhuEbOq4qzbj--q4gsC5n0bXa9uzEzbIzhdSn4S5339eHUptr536qgv95F_Vx-4O8biXRQFRmSDDWA_2E4AOcjcikd4Hy8PFvjQvY0boewJP_UEhTWBQdxbzkUYyG2y1z7Yd2Yx81w3qoeFBcngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25ab02a82.mp4?token=XZp5bbO26L78F1A7aHN8n3FTZT5NeoFTSAgxf7z6yWStA7AoNpQwenqj4tn3xOF1sZJuSqMjjjeOgBtZAOZzZEKWnC5eY-U-DLXxJaLssEks3AqiKYfpC8aZYL3PKqkiQAVuQG-mXKHWJACW7czcxlDAMHpD4Wspa8K8iuc-xTGxJYyEKBaSgwj4ZgIDGDx90WwhuEbOq4qzbj--q4gsC5n0bXa9uzEzbIzhdSn4S5339eHUptr536qgv95F_Vx-4O8biXRQFRmSDDWA_2E4AOcjcikd4Hy8PFvjQvY0boewJP_UEhTWBQdxbzkUYyG2y1z7Yd2Yx81w3qoeFBcngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آقای شهید یک پله از امام علی پایین‌تر بود و معجزه هم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142790" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⁉️
بیت کوین تا کجا بالا میره
⁉️
🔴
بخرم یا نخرم؟
این پسره پیش بینی‌هاش ترکونده
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142789" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raci1KbBF4Bal2xqisjUwDaSSsTJwjIzCP7uNVW21ACVch6_65jEeuPr7B6qOqmYSR6zqP8Y7Mcg_7ekQMpPT5TJDxrhnV5bvEzBvgFdtlEv-GgodtcFMLNqQR2UtyueOYf-DPpsVq4RdVY4CdtYm9IH9sDP1qc_E_aAHXBsBExLVPH8LjOua_9RTjXFXCiBmDFVegFUp66JAemXC-DgJ4Ng59r6E_zZaVdMDQY-EM5oXn39dwevExxCG5iKdwuJK4Z_3fTI7oxL9OxFzOAZzGAgXWnvPjMNmeoFE7OjWsw_MnvqUcKJDv3lDMkf42cm_-QYBlyLyZ-JABCWGPiYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر متفاوت ایسنا از  آزمون سراسری در دانشگاه امام صادق
🔴
این دانشگاه محل تولید تندروهای ۶سیلندر و بیسواد و عربده کش هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142788" target="_blank">📅 12:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37020c0eb4.mp4?token=G2jIsEWClqgCrmjjqXR6CI-AaCcCrkwoKQEannlmv2wEgGSytxkf3XJqOdwikJzCkJwMyfWqDKu5orHQeBY6ahi1NgOnJuSjvFjamxKv7xNjejLr12BNQYGUFD2tJkMB98ZARV-rE28QtBjmkez7eD7v1g3HD0Kuy76nZwuBrncTQPF-y7BABZq8cudFIW6kc4le5uuMweElPMLT-Yvo4gREAcQxX0LT3MW41nBYjPaAKCERfmH3fr9IGfQPggalDjPl8H0gg5FSwIdNwFcFzIxcVugcnAdNvkJpcYs4JX1OzufOUvtD1qevESVQHJC3XodMOajLdD7tkyahhva61w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37020c0eb4.mp4?token=G2jIsEWClqgCrmjjqXR6CI-AaCcCrkwoKQEannlmv2wEgGSytxkf3XJqOdwikJzCkJwMyfWqDKu5orHQeBY6ahi1NgOnJuSjvFjamxKv7xNjejLr12BNQYGUFD2tJkMB98ZARV-rE28QtBjmkez7eD7v1g3HD0Kuy76nZwuBrncTQPF-y7BABZq8cudFIW6kc4le5uuMweElPMLT-Yvo4gREAcQxX0LT3MW41nBYjPaAKCERfmH3fr9IGfQPggalDjPl8H0gg5FSwIdNwFcFzIxcVugcnAdNvkJpcYs4JX1OzufOUvtD1qevESVQHJC3XodMOajLdD7tkyahhva61w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید خضاب مجری صدا سیما: تفاله های پهلوی دست روی شما گذاشتن اقای خاتمی !
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142787" target="_blank">📅 12:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی در مجلس : بهترین واکنش به تشدید جنگ اقتصادی ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/142786" target="_blank">📅 11:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f0c39a2d.mp4?token=bSWRItbQNEeOAKuLzsHIukUX8BscOPWHT37_P9C7V_eupQ6AEGyAgMZ4t_hdZ9ZWFFcOoFpy2k-g7asTAdBZpmoIro6QVHN6fyYXgS7hn-HSEKT3DKP1-DBoNUh9uG0scojOfLXKNOGBMrtp_fV7GHCo_ojn3I1PFguYmU69h0J075kQ4zP_gFVCzE-5TIYCJBJ9ZFTcObng1trc-wmS2lsVftVjw5aOy9dKseJRBV-CfhzDGg4AcutSJ3mcO1RUCVPk28VktF0A2PrJ2bJkjj9S4kizKSJQ97Scq97BjRC9-Lw0wV4XlOhwI0_5DgcpPl-Q1Q2JYmxJu8mLgkddpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f0c39a2d.mp4?token=bSWRItbQNEeOAKuLzsHIukUX8BscOPWHT37_P9C7V_eupQ6AEGyAgMZ4t_hdZ9ZWFFcOoFpy2k-g7asTAdBZpmoIro6QVHN6fyYXgS7hn-HSEKT3DKP1-DBoNUh9uG0scojOfLXKNOGBMrtp_fV7GHCo_ojn3I1PFguYmU69h0J075kQ4zP_gFVCzE-5TIYCJBJ9ZFTcObng1trc-wmS2lsVftVjw5aOy9dKseJRBV-CfhzDGg4AcutSJ3mcO1RUCVPk28VktF0A2PrJ2bJkjj9S4kizKSJQ97Scq97BjRC9-Lw0wV4XlOhwI0_5DgcpPl-Q1Q2JYmxJu8mLgkddpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات مسلسل اسرائیل به سمت شهر تلوسه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142785" target="_blank">📅 11:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSGsk7StFB8_td5LwnsspJxubgLw_grlG25weQUxdaqB__Ce_WIu-cylDX0JngTwa-RZNqXltHNPbUxy2ed3xVyz0x_kYjXXkJr39ag1xz5riFtFH79BNZOSEM4BTbJ12y7WOR9g0Sl5QCb6Ke2k0JR5DEgyX6FQkipyhWhQ_kxy587ZjmH2CJOplKvrcWGBkF8K9cWIHW4nXk_t1XZemhIlgWV-_NKcYfWu19IiISP1k7CrwEhXrQSD1evc51zb01IKuqS1d4cFG7O8Sfz5ZM1YZ3ACHj5HtE9Wu9MpBJl0eqGZDJnTh6zUIwwAtF3GfpVJZj-NInmUtsX20yeJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین بروزرسانی قیمت طلاوسکه
هرگرم طلا ۱۸عیار، ۲۰میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142784" target="_blank">📅 11:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه:  ترامپ دستور داده است مذاکرات با ایران برای چند هفته متوقف شود و احتمال تمدید این توقف نیز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142783" target="_blank">📅 11:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJiYuibqItqgf95f09AB0rNshUUqN4E_s2W36fZOZyBYfwmCri-FBPBQXUQdoroQOUBeYstFQxsxti1Wk9HdwJmi-Kc12mUza9EaNoXPW8FBb8EIXYOqnNV7AfqL7nclPJxeKIkpJZ3DUoub7pHt_uN9QvrHyGJRUtGLkgbaCz7rClOxlKKt9yXBSoSZg6i5b0SztPEiL_xNET-H3YcV4M0Mc16MPc4KFnKYHhwBcrLDDodLwtY_3lcG98ZCgkv3x-xohFqkVdLhs-sSC27w9-5Du904M0ILYNWX6ZLaFs78M7ieZgtpwvBB1pDuM1wVH_PiBVlC-ICeQFYtRpi2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر نفت چین از اوایل ماه می ۵۴ میلیون بشکه کاهش پیدا کرده و به ۱.۲ میلیارد بشکه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142782" target="_blank">📅 11:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_LTXuD36seQlxwVDTBNg8VuIMvd3qvwJzXVqdn1_G2AIEWLNkhK5cgNe2QuKk-8WeZD6DY60Me5ivQaZzaJKmBDEfNPK14ApWs0SYQxq_aeXbBZIdVyQA010rCa9pGXP0-j03riTmgLyut1rN4wEpcdvHpqqDVvBZgCSr7lOeA6ZOOle0eY9G6h998ysWe5lj7TdW1wTYjGprMTWSxOF-ZW7BucjoTomjxNPCv4iKtC1NrhAIMzB804oe_Mw-jYuXl3MaDgdzjVshLscC07L-oXSXcv7TAstfS5gN8u6sv5yupXUq3IV2HrnVjrvkefhC67Xwo_nvhwwYsdkYR4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد اقتصادی عربستان در فصل دوم سال جاری منفی ۴.۸ درصد بوده که ضعیف‌ترین رشد از دوره کروناست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142781" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142780">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAWYtjYCadoIU4fYRONtKr7sIXM26uGK8C7Xej3ummALMvwiRiZUBR8-dd4e6ffJx54TYcpLJZkwNkAWLNlHZgxq3L6QPtAyGqqfu0nWv0M1ECJo9kYo-EFTa1q4veofQpPSUH7lMJBXE90xaM0AMGqRPl6sVJRlBiwmuy2L2tnQOn8LczpuQ2HuktsXTc-G1UBUX2tGv3ihNPrjPz0TpdABY1ixin3xwwlVeyn5OXBfHDiZ5R9lDRURojZgnFawnFuDDenm7QcvWar5e6rMm1EEs2gfl4bDENFthVzOKrUetKdweyJMOdIjgjIye-OrkFR_q1e1pK64vpEFgfvGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی، معاون وزیرخارجه: آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/142780" target="_blank">📅 11:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142779">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8LOTGsW3L4oCMeCcCaBZVZhc0PzwYPfGxag_Ie4hhO7HJgE9jH28TWQM-VRrmMv517Pbc6EQAIhRDHlTyOIaIID7gOXu-mJ6pCaGoSrsANAJTPUC6k4BNSVpi_xPHtoMnrJ8By0iKfYt5cZ_P1XQjt5p5ZokMh0A_U7-JEvExm0zSG1P01rv75a094-jrn4HNlTcyacp8JMCjx9Brmak7jSuSrr7dW2-ADFiqGtOwlSQxdUwdNWNsjejl7akiwccCRwXLoCIaJ_QVIDhkAUG1_Jjmcs42qq4JM2a-isP-ilqgRwSvJqfKJrkA1S08eUi8i2mdUOsIz8oQBb350VqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به حدود ۹۳ دلار برای هر بشکه نزدیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142779" target="_blank">📅 11:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142778">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl0OTV1FzOpchQ6sVI7VhVrrN0uBGHNhDet2f8C-r_zRjnjZax8m6m2ziEc_BGLaVhx3SAwgv6wRJF_eC6E6B8l35vpwSw1oIdgjiHdFQj-KY4yCPLn4vUdOwJhQ-rBiUao7OobPVUasJA8NV38ZxwR8u6ZvAjD7wW8z6lQKJx1q6_UNfrX2m-6cJF5h3QMjIiHJcYkpV2-RPsfXXF9E1qx8u_eYEUlx-XSMmznj4TWxq88VmuHccVoEi-oMFO8imE2duOZsRZeq46E4sb7FECWQDCNIqNsA1Lz4i5W7dz_UlnA4odH_rtQqo2ezeMQCAr1Q15u8IqWJxIop7aUQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماری جوانا به محبوب‌ترین عادت روزانه آمریکایی‌ها تبدیل شده است
🔴
مصرف مشروبات الکلی نیز کاهش چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142778" target="_blank">📅 11:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142777">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به کار می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/142777" target="_blank">📅 11:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142776">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXZMjv7fzYF7DuxCzUDKugHxI8YovZ0UnwuLaQ9DdItxe3x3-hxhOqwu3kHhQsn0Abdhe_uy3tsgSjdoCYdIn5fIeUQvn51PKdjmLS6T-njOmwhEoNachCedmiA-HAkHQuVKOpgjbd3Y093bzd_GAeyBt7gxusC0nie0DPonzhZkPpRYK2fbXz3OJ4tjMvOlW9wbhU_u_R3tRCoqAfmARR_GFL7xtPtFxBmGRbySdmPZzVosmddB7pW74CFOG-D-u_IUofnp9JeX2yoDqW0Zyr0IFGPDrL_H4-vWoTppHrm2ey-6qhw234Z7Gmx6WTIjQGphbwcvD0bH301qACj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کره جنوبی تخمین می‌زند که کره شمالی بین ۸۰ تا ۱۲۰ سر جنگی هسته‌ای دارد، که بسیار بالاتر از عدد ۵۷ اعلام‌شده توسط ترامپ است.
🔴
سئول می‌گوید این تخمین از پژوهش‌های خصوصی به دست آمده و به‌طور رسمی توسط ارتش آن کشور تأیید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142776" target="_blank">📅 11:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142775">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUyzDCDBEtq9sigg_ojQqTrPy7bMhOv20z2SM2ZztZfu31zD_ViisqVCusx1KwZIbSKZ1AisJmuy0Sz9YUMDguVk0eIGeXZWIDAs51BGcNpyOfxcnapwCittTF7SogE87xtC_ehbfl8jbO0L6LbiUW9DMzhsB-BUjvOaoZs0nZK9gNQjy8UyPXJkZBpe0cuhnCJLYUvh8MQdye47-IO7ArJ6uC1kyv76tkBxN5ywEsCzw6vOX48YnR-Bsp_SGy6tg6RbhUppq_p65Smg9eUOIlCtI46W5j9kV0iHFdkreKGiQlxk0JtwpyNcC7HuiF6fYIk4G2rKh-x0-447JMmASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه یک تانکر گاز متعلق به امارات را از عبور از تنگه هرمز منع کرد و مجبور به بازگشت به مبدأ خود نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142775" target="_blank">📅 11:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر علوم: آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142774" target="_blank">📅 11:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb38b789a.mp4?token=LCUOtBx8Ed8rHBa9n0RTndReLZQDbB4EuaVtgHBiC5akJVjhFEookdzyKEAgSvLoDWhB2BLmHfkEK7T_yxutROL-3A78qGU6a-dq_NjjXEAtK2OtVtdsxoOQ9pnFztuVDh1sSulrI55MHUXnW7RuV7aLj9ueq8DDmjfgysRFjvtRblf957KFNaeWG-GHYBB0tQXrlmKrUjrfqxCaZCl55rzRhRT1axxt0tDbGD1GnOy8HyfTJGvtHrb6USRDZI_XFSeSEw4cwKwXPKG2nzFEqLsgyiIn-DfkYRHlz4vf7nbH45CjVTi9K57Jlmnkx9SPfLi1WeKX5_HqZi44zcZHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb38b789a.mp4?token=LCUOtBx8Ed8rHBa9n0RTndReLZQDbB4EuaVtgHBiC5akJVjhFEookdzyKEAgSvLoDWhB2BLmHfkEK7T_yxutROL-3A78qGU6a-dq_NjjXEAtK2OtVtdsxoOQ9pnFztuVDh1sSulrI55MHUXnW7RuV7aLj9ueq8DDmjfgysRFjvtRblf957KFNaeWG-GHYBB0tQXrlmKrUjrfqxCaZCl55rzRhRT1axxt0tDbGD1GnOy8HyfTJGvtHrb6USRDZI_XFSeSEw4cwKwXPKG2nzFEqLsgyiIn-DfkYRHlz4vf7nbH45CjVTi9K57Jlmnkx9SPfLi1WeKX5_HqZi44zcZHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانش زمین عظیمی در معدن طلای زامبوی در مرز کامرون و جمهوری آفریقای مرکزی منجر به کشته شدن ۱۰۷ نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142772" target="_blank">📅 10:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4BHHgFfWnCM-ncDTA4wWR6nUx57uKF7v0YoMbreTPlZT7H5i3A3jwPkchWxoRNvLQvAIjG0GYIf0SXVw9qg1sLiDG3F57j_4NLKbkXG-mTryoAHIfhsTTtm5rwYxd2qruBX_7ouDugeHI8tKfyZt-8IRVADuloWa_lUb0uHyJMYNzTwW_I3tFvgM2aKCa1mLo6ueKWiVvhumepQoH1Ny6UnmvZUq0JXhvITfMRUZ5S5SRlFELcGgVLsyCPMRiGkxXBQwieh_fgI9vSFJYno5lmHzZ0Zi6_-2MqMZItcgb7I9H6_RK8goa_EzX9yemtKl9rMmLJfjve8sIL7lKgzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره گزارش داده تهدید ترامپ به اجرای یک «عملیات اقتصادی خردکننده» علیه ایران، ممکن است روابط آمریکا با برخی شرکای مهم تهران، به‌ویژه چین، عراق و ترکیه را با تنش تازه‌ای روبه‌رو کند.
🔴
نادر حبیبی، استاد دانشگاه برندایس، گفته چین مهم‌ترین هدف احتمالی تحریم‌های ثانویه خواهد بود و پس از آن عراق و ترکیه قرار می‌گیرند.
🔴
به گفته او، اجرای کامل این فشارها آسان نیست؛ چین با تبعیت از تحریم‌های آمریکا مخالفت کرده و محدودکردن تجارت زمینی ایران با عراق و ترکیه نیز با موانع جدی روبه‌روست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142771" target="_blank">📅 10:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عارف، معاون پزشکیان: گران شدن بنزین تا محدوده ۸۰هزار تومن قطعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142770" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142768">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhmS-32MQu-jhNTtudUcpqK-mM9xJUOMdsyb8z-3mnsmafqrKjh1d9rlyHn30PDsF_DsyRVdiuvKnTJYvCX8E1pFIlZCQH-zrkch9txc9sPFh5YSpgKWcqitVtqJVzaewW_8yiaYSnDj64oG9EnB5qpnHi6NwYUNRAtA3KSauyxhgGUHpOdfg5nzIm-_HWn80dohkZemf4_Jq_2hZxmEEZLWCYhNuSPtl5WY8ieVdfKd49VpF7Wt4e1A1dUvsIa2A2LpLSao9vix5o5MoAW_a0yUxreSnPAhmh4Jt3PIa9GOEgOdsugB_4fdCKpwiqKZm-83wvvvyaposnhrpcrH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBdgC2rcy_6ePgk_EXEx0rPhmOpIHYY8dawktZzIU9PFya3fW33Cupvur3I1nTfCXKefg47JCFLuvUktpkU8gJiAXPdjMUV8cshuzTIXcAfeAW7OAiLy18FvIX0b1aeeT71qkIfDw2YpLCgzSdDGV6lNXtorLC4gl5kIFj0KIwz4lfwkrYFVJJfzGNmcaNZ3AM66B8hIhOLIHkiPxW3BHrjPp-JhMB91ILWJOa6clEBDDeGDTgXM0bM_4ps3GaZ1y2ZAbVG1gywfpnh64ovotKqsHipjtz_4ZBjzK-az5KuRmp3rD2cZLY0fP5bF_I1odCufFqiY8OfSXbYLNlbQxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر نفتی هندی تلاش کرد از تنگه هرمز عبور کند، اما به دستور سپاه ، مجبور به بازگشت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142768" target="_blank">📅 10:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142767">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قالیباف در دومین روز سفر هیأت پارلمانی ایران به عراق با قاسم حسن العبودی، مشاور امنیت ملی عراق، دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142767" target="_blank">📅 10:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142766">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn67MNh-IiU3OlGz0w-4ehcDsBw0ZZZ66JNKE462aK3NIsL9zUNABAF5xLdvLbWtl0Rc7Q3aawv3ycN6XNGhKx9Qh-QiAjU1vc8mUReWqCnp3BD_ciUAep7NMYabgRnF8Gn2aQfWlNokPhnejhko9DGQ78NSExoeP1TpGpa3oXKwlQDHXrcmlIZMnX1bwf_0AwjMC1WNO9kdQyoKYofTPbZkwPqeBrXoZW--yi57Yt9dxWHIVovT1VCXY_meAIb_IepDoknS2FVjg4i1y4Df5GqihmAtKiax8S__yMeB35nj_ZeJVx9v48jwdZ1ussLpYLoBfNSNikJTfYJHzS1BXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل به نقل از یک مقام امنیتی: اسرائیل از آمریکا چراغ سبز برای اجرای عملیات‌های ترور در غزه را دریافت کرده است. همچنین تأکید شد که ارتش از «خط زرد» عقب‌نشینی نخواهد کرد و تا زمانی که حماس خلع سلاح نشود، روند بازسازی نوار غزه آغاز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142766" target="_blank">📅 10:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142765">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDlVTCnhHH2kPh4UduWYv_m9jmNIawj4EyOt6s8d0zftbwmRPEhMBGyNPhIbmBrspzTCv86LEM-vHwZSfwEpLFiCCbf10Z60V-TJz8S3w5Mosfq-tQaskmFN7OZXC_npeCaWvUgoQtSbbEdOpm-XeER9EJhr1U0SWiuvXlgJXLuUYwGvp9MURubHxUPA9XkdTrG4z9SAN1qrgG9mpyqSTtz1LutdnPjxeZ3ffWBUMJhTh5YKkdbFdcMy4yFrqAps6xdzwVnJB0PJmR8-2bef-37YZQEPBAkhF05h0D5wucZoMWqXwqEI1ul2QAkeP6X0gciVDrwJLBFPGSAVc7n9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین یک جزیره دست ساز برای بزرگترین پایگاه نظامی خود ایجاد کرده است
🔴
چین ساخت یک جزیره عظیم دست ساز در آنتلوپ ریف را تکمیل کرده است که به عنوان پایه ای برای بزرگترین پایگاه نظامی پکن در دریای چین جنوبی عمل می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142765" target="_blank">📅 09:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142764">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry4J1hz-iNGGL_b0sthVQeGCvRNUPVIq84tQWf6mQRAlC4VP3sOFi9k0cWnX9y8n5BrErtx5LHwP-tq1ZajHKdR0dSdhksF__n5oZyQ4DI3CjSg8CICzv3ROtIrHfGdvWpUK7VbcUC9sKramJZQSyZQ_XWAnbvqEo-xWg7V2vKb4WoGIICaUtgq9J7eR8joyyENQ5QeWMeKxW0LaLW6Gjkq9uvklQA0DJEC35jks7ktJiGVr3kmuSGhyWy54lvroVPQ9lxDzB1HQeOwg_4GFmWYXHS0oBvowYhNsx2aPWNK8iMxzeFYEA9-DfMdVz-F8Ny7ys48IgEn2_347PmhR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل به حومه حولا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142764" target="_blank">📅 09:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP32lYjcHiOJvXEKJwx-HILbyWFVODXidhSXO81POt2Q9o3CRqVKMh_ztcs54tTvGsaa-S2otfeC__sFnN_QOJ5-GJT-HavI24Cion0HxYz4Gqa2nRhm18lF353NYfhGAcnxUIGL05Tv0aYYWy_UYHL0ccW4o1iVgKUJaEnUzf46qu2MAFBX50OsGjRdumBfbOcQZHeDKbfPY-OqxAkXmCAovwelWzzmEHeAgBdBMX7IGUfkVM5wqvRMsUPhzmDrxfzJXWbDBwv14MS0muOs6n5W0FiRA0EcTEHIzMGaviVF01BxpatiMiTqKKJNTwDVnkerg10bgS29g1g-X1KAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=uUVeuubkL7HUgUfrFEU3pGruKWT8HSxRaKSkUwnYRbBc3NHuv-AZ8szNC9PofUSWMprfBMjCkXb48w1JIld_ucZJCUyKrPK4FcnLBBnHbuBMB2x09cVX-3Xnb03OLQFkMln4eoPVxHXkh6P1syQwZQQ4UnGCa--tGiddpTEkXH4y1s71B7-D-NV5g-8k7fMdcNVSXJYBMU3CfjVYO3FUu2IEvjUTX1ssA-WpLM06q9O5hUcNLbZ3W1-b8Q6qk9Zu3yatwZOIPwzEOIkSufXj4-L-to9KUk-bsYcrnEO1ubS1TlbXeTBt7GS2CDmNnkFhuOcYawXYd64Mh9C6PSZCPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=uUVeuubkL7HUgUfrFEU3pGruKWT8HSxRaKSkUwnYRbBc3NHuv-AZ8szNC9PofUSWMprfBMjCkXb48w1JIld_ucZJCUyKrPK4FcnLBBnHbuBMB2x09cVX-3Xnb03OLQFkMln4eoPVxHXkh6P1syQwZQQ4UnGCa--tGiddpTEkXH4y1s71B7-D-NV5g-8k7fMdcNVSXJYBMU3CfjVYO3FUu2IEvjUTX1ssA-WpLM06q9O5hUcNLbZ3W1-b8Q6qk9Zu3yatwZOIPwzEOIkSufXj4-L-to9KUk-bsYcrnEO1ubS1TlbXeTBt7GS2CDmNnkFhuOcYawXYd64Mh9C6PSZCPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی شبانه روسیه به کیف منجر به کشته شدن ۶ نفر و زخمی شدن ۳۳ نفر دیگر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142760" target="_blank">📅 09:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O__LYXWgvRqGy0SSNcHa3dDdpkxN-A-kLWAkwm3L7P4AH8pexUaXFnNPXfXLlQyV8QAMXYvtcf5-sLCe7YU4LD-4WOnuDb8g9e2ZPAgfZ0lSY1a3eGgsT1gV4x_ri9a6D32-2f9Y5cc8VxEyTTTNIMJvT-uk-4m5EpMa2TMD1BJlzxCdHpYsXK3TdBm36uGH0eG7G_v_C3chZEFbZHNmC9xd4K0BMjaH4127TsPiKIcFoY2xJyUxR2Q35eb5BshS3ryUj4SZgqXxApZty8rqlUqUSMwZ4xEFtW6N0vCjqLISMYQ9ltv9w5eySxfvc1ODFputARJukPk1Dv49H0eQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی آمریکا از بحران‌های مالی داخلی است: یعنی بدهی‌های بی‌سابقه و افزایش سرسام‌آور بهره‌های بانکی در آمریکا.
🔴
اصرار بر ادامه سیاست‌های شکست‌خورده، تنها شکست‌های بیشتری به بار خواهد آورد و دشمنی ایرانیان را در پی خواهد داشت. تروریسم اقتصادی آمریکا، اقتصاد جهانی و حاکمیت ملی کشورها در سراسر جهان را تهدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142759" target="_blank">📅 09:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPajVaDjPnIlMPQ72GvVfxMwc4pvorzTIaTCVUdqPPnI4fQG2oGZ8sTL99A9Vns92jfPXLn8op9qkkue4nUklYUJqw3_dzqlIXOYw9PDXDOqDAQLIG_d9ZzKewZKWC3rvhiz-jvWc1lpEb-YRQZGjZKkhXONP2OT3hI0l44svOYnyIjE7f84RxasY4L3ZfJ4OA3tLbkyDJ0s13p9tJjkXKdxvtiuy6ETfIoDqMknuZibfkyoKUUknofUtEupJWpgutrXS6zRaI8B6f7dFu9h8qyHSBOhruKx0xazWxjs2DX-zFmwxkudi4tyllXzosFMwQlvjlnVKt_MQA9O1cGnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: اردوغان ترکیه را به ماجراجویی‌های غیرضروری در سوریه می‌کشاند.
🔴
اردوغان نباید عزم اسرائیل برای دفاع از خود را بیازماید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142758" target="_blank">📅 09:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پروازهای «العراقیه» به ایران از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142757" target="_blank">📅 09:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رئیس سازمان سنجش آموزش کشور:
پیرترین داوطلب این آزمون ۸۵ ساله و از استان کرمانشاه است و جوان‌ترین داوطلبان، یک دختر و یک پسر متولد سال ۱۳۹۳ و ۱۲ ساله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142756" target="_blank">📅 09:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142755">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
به آسیب‌دیدگان جنگ سهمیه‌ کنکور اختصاص می‌یابد!!
🔴
وزیر علوم: برای افرادی که در جریان جنگ منازلشان تخریب شده یا آواره شده‌اند، تمهیداتی برای اختصاص سهمیه در آزمون سراسری پیش‌بینی شده است که پس از تصویب، امکان اعمال آن برای مشمولان فراهم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142755" target="_blank">📅 09:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142754">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پنتاگون: تعداد نظامیان آمریکایی زخمی شده از آغاز جنگ با ایران، به ۷۵۷ نفر رسید و ۵۰ تن به رقم قبلی اضافه شد
🔴
۱۸ نظامی آمریکایی هم از زمان شروع درگیری‌ها، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142754" target="_blank">📅 09:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142753">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqbgPEfCzTqago-pojQ5OiA9OPAUsmpmSP7SjetK-DlMj-lHQ08IwHlTqqSLq_m1-NQY6oMLJcBGErdQyfMyl4sZZFE7ODbe0kwP8MFkE43kBf9I_zIECMBRmn43bGk7ufJBZhk3vOzXEwhXsnplXEMfVdvnoitjS-1cnIk7km9jAV9cDGR9MANuqZCgjOEvRIlFas1WXHmU3J2fmMACLPN8xc5Z9lWVRf9LLPqr9QgOcOeT_DtK98MGDbiN05eggujhIBLuzl9-CGyXc-lEKONGVLWCi9IvG8pfB7uwb2ed6XEsVf0RqVu5fBvjo-YiAmK20fw44NMqw808FIyZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابولا در کنگو از کنترل خارج شده است
🔴
سازمان جهانی بهداشت: بر اساس آخرین گزارشی که دفتر منطقه ای WHO برای آفریقا منتشر کرد، تا ۱۶ آگوست (۲۵ مرداد)، جمهوری دموکراتیک کنگو ۵۰۲۱ مورد تایید شده در ۵۵ منطقه بهداشتی در شش استان را گزارش کرده است که میزان مرگ و میر آنها ۴۷.۴ درصد است.
🔴
تدروس آدهانوم گبریسوس، مدیر کل سازمان جهانی بهداشت، گفت: «شیوع این بیماری خارج از کنترل است» و نسبت به خطر بالای شیوع بیشتر در داخل کشور و در سطح جهان هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142753" target="_blank">📅 08:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142752">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قیمت نفت روز چهارشنبه افزایش یافت و در بالاترین سطح خود طی حدود چهار هفته گذشته بسته شد؛ این افزایش در شرایطی رخ داد که نگرانی سرمایه‌گذاران درباره احتمال تشدید تنش‌ها در خاورمیانه بیشتر شده است.
🔴
قراردادهای آتی نفت برنت ۶۰ سنت، معادل ۰.۷ درصد، افزایش یافت و در قیمت ۹۱.۶۲ دلار در هر بشکه تسویه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142752" target="_blank">📅 08:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142751">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آزمون سراسری سال ۱۴۰۵ از صبح امروز پنجشنبه ۲۹ مردادماه با رقابت داوطلبان گروه آزمایشی علوم تجربی آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142751" target="_blank">📅 08:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142750">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj7_PHlUXjgA6-Lya7oZNCSbCq3qDheis6EjzPtJfPxsWKUeHKd7CklUbG3iMyT7HLLythPFcx4JYcPOO02wMtmUK9kjmO9slRa8ldhXBQoFKWIKGjV8X2NqJJY-5dh4eVeyLG5ciBIOF1MoB0bTp-IsLfIdRQFozLhjVwHEvObOFTddy00_DHXFHgJW-a7cz5o4eTSjipxlhUm4LAjIjygGwoHG0Apzr0mTTCoCfdowsar_ZVpYbtELP-71XDfQqt06VgfLAdSBMvJHKgTBCYyUkWGQ-t8WGqqRvo5TK3ruySksxJ2T059ScTa0p3X3xLegcWpzx15vpIHNHzIn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
واکنش تانکر ترکرز به ادعای انتقال روزانه ۱۰ میلیون بشکه نفت از راه مخفی تنگه هرمز: شاید منظور مقامات آمریکایی انتقال ده میلیون بشکه در هر کاروان باشد، نه ده میلیون بشکه در روز. برآورد و اجماع فعالان صنعت بسیار پایین‌تر از این رقم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142750" target="_blank">📅 08:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142749">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4669764466.mp4?token=BOwxcJMz9OqAiWJT85vAIdFFqxRcV3d6VFAaszyXQUdmTHmI4ijm-zQ1ydHC0t6JHgy1AA4F1Lc25e3TvyNdmMDONxeE7N3yER1GGIjxsZVFoHBartEvS6OXB8Lm7kTBYcWtdHPhbGRttp_1Raea369vn9FYHldFNUG5WLBiXrV1HBt9yhiAbmSKKP6NsTgLrap1d1zuct0NlEjKhFXdQFhKwj5VWOrr9hPFhBjdas-Cx-l1q-XTGhvQ_A22nG4wN3kJlmEcVKLpYhsx-bF5SGTMtBnzNRI_uTNRrTX6iG-4asMkrzRpDgcVEIWYnoUh9oG3A0w4rSMNPh8sTPHHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4669764466.mp4?token=BOwxcJMz9OqAiWJT85vAIdFFqxRcV3d6VFAaszyXQUdmTHmI4ijm-zQ1ydHC0t6JHgy1AA4F1Lc25e3TvyNdmMDONxeE7N3yER1GGIjxsZVFoHBartEvS6OXB8Lm7kTBYcWtdHPhbGRttp_1Raea369vn9FYHldFNUG5WLBiXrV1HBt9yhiAbmSKKP6NsTgLrap1d1zuct0NlEjKhFXdQFhKwj5VWOrr9hPFhBjdas-Cx-l1q-XTGhvQ_A22nG4wN3kJlmEcVKLpYhsx-bF5SGTMtBnzNRI_uTNRrTX6iG-4asMkrzRpDgcVEIWYnoUh9oG3A0w4rSMNPh8sTPHHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: جوابتون به صحبتای ترامپ درباره تنگه هرمز چیه؟
🔴
حداد عادل:باید بگیم تنگه، تنگه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/142749" target="_blank">📅 08:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142748">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رویترز: زمین‌لرزه‌ای به بزرگی ۵.۸ ریشتر بار دیگر منطقه فلورس در شرق اندونزی را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142748" target="_blank">📅 08:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142747">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=dS-_QA4ZR7bQeDw71cPS7ATyDPiRyyl0cMD0zrVz9-1xH0a2QENf35KQEg834RrbqqXcmX12OheBal2rRcP6bE_PfdrDhhsA9AjfZ90h0c_Bo45dB2a0O0-WePzK_IruPnyxLcisyPjYbofF50SCfUplLLLVkQBFI_DJJtt5DhVPsSCEdSLc5iI_lh2mZx2JMxJsPpTRAouKN7QhHEGZLxtpiPsm1Gma5Lr1KcUkQnX0uihnB5WHy0TlUWzGtCUMaeuGfVYGPpGefiqRZYN4fPrIgt_h8jv1ZaPA-_Q6EfoFL8mAFDr07cPm9_Zt3h3OtMfH2awe1-_BmCzS6aPRLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=dS-_QA4ZR7bQeDw71cPS7ATyDPiRyyl0cMD0zrVz9-1xH0a2QENf35KQEg834RrbqqXcmX12OheBal2rRcP6bE_PfdrDhhsA9AjfZ90h0c_Bo45dB2a0O0-WePzK_IruPnyxLcisyPjYbofF50SCfUplLLLVkQBFI_DJJtt5DhVPsSCEdSLc5iI_lh2mZx2JMxJsPpTRAouKN7QhHEGZLxtpiPsm1Gma5Lr1KcUkQnX0uihnB5WHy0TlUWzGtCUMaeuGfVYGPpGefiqRZYN4fPrIgt_h8jv1ZaPA-_Q6EfoFL8mAFDr07cPm9_Zt3h3OtMfH2awe1-_BmCzS6aPRLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک چینی بعد از پرتاب دوباره روی زمین نشست
🔴
چین با موفقیت مرحلۀ اول موشک قابل‌استفاده مجدد «ژوچو-۳» را پس از پرتاب روی زمین فرود آورد؛ دستاوردی که می‌تواند رقابت این کشور با فناوری موشک‌های قابل‌بازیابی و کاهش هزینه‌های پرتاب‌های فضایی را وارد مرحله تازه‌ای کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/142747" target="_blank">📅 08:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142746">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ybU1-dTAtVYFpm0LD5dehYO7r5-04s8NHLdNo5PXYd3B6KxvZ21t5Fd1C9_aHTU4G1_wQfGjPQBneGdj0KHudYjhU15y6EhNbdiZHBMrbtx5U_T4sV5v0J6GvT3UDdyDw20QuLtbIyQ6Z9TfFcFBuhMFgI0UT_H3V99e487vsP8_oKCySwZKPUeMQ1GwrjUHUEeQH5AwqL6KY_5Q8UuoZLgJv1upuRNTeKZRZ9D13FKJ-L9AvM-LZC-c57r-8zH2azBfgZcZBePrsS29bhxHet5kVAYwfdAkW7iESwB8ZYNY4aoAGSxbJsa5XEo1AmCsrRhwe3yD0K7w5e2fcoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ:
‏هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند. بنابراین، امروز اعلام می‌کنم که کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد! این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
‏
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
‏امروز همچنین اعلام می‌کنم که هر کشوری که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی عظیمی روبه‌رو خواهد شد.
‏قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید همین حالا متوقف شوند. خودتان می‌دانید چه کسانی هستید.
‏این یک روز دیِ اقتصادی (ECONOMIC D-DAY) خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
‏این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
‏ایران هرگز سلاح هسته‌ای نخواهد داشت.
‏از توجه شما به این موضوع سپاسگزارم.
‏رئیس‌جمهور دونالد جی. ترامپ
‏realDonaldTrump
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/142746" target="_blank">📅 06:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142745">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
برای فردا انفجار شدید قیمت بیتکوین و اتریوم
اصلا نمیخوام جو بدم یا ته دل کسی رو خالی کنم
ولی این چنلوحتما داشته باشید بدونید واقعا چ‌خبره :
◀️
@agha_trade
قیمت طلا رو هم صعودی پیشینی کردن
😳
☝️</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/142745" target="_blank">📅 01:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142744">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32c922962.mp4?token=XLOU2-VCnGxkjvC0Sm-YdBGg9Ew7h5qj203MOZclo_rwIONZ2Nq2gdjV_pHebYUq0WomWcuS0F56qVaY3LzHcW6krFyQebaBLMaseNaUauumw53tLY04Gs2JaoYlnkwDx0C2pwPbf7g-4tF8mavhH5iltc19YXAR0fIAkw9CR4NjLdu6S3a1k93KqmRo0bTR7OmK9CekJsxrZM3ONx_mvmwSV6FCjKtMpnPdYPsw--uwv4IcH78JqHBraKCRFP-h2wBaYl13BLcVbAdE8P5lK6fVS-7uWyORuB9iRLKpfMw_dBKl4THr3pRh61MMzaI0iPNOfDlXhmkkp5Of-gbV-CLYsJJ0c1-rY6CfPt89Ou8vOxrte1cdyHPs66tUqWqBXNdhtAewGYl_PM8fesYz8B9LwYkZQ1_dkm2k4fnfJc6ppiO3GcHhBB-frFW8d4l4Q_-MyAC8WM74E5o-NWK15mnN6D_ov2sumQw06wwh_qY92gYy3UzLRwLqWnCL13_7GWJMLGvR7FiuGqFGOSNZQbGIm7QipZHuYyuTjB0J_HTwpBwxyMYs_SZRF7GslDOTd1dDIOz1kl1WOIZkkkJ5yQjpbaZLqt9JY8zZOhvm1fYsHwTUj9gIUNlVCLys6nzf9m2-MWqyD-bvnqtpNbfP-dBwpbSHJj964wIWEovs8qo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32c922962.mp4?token=XLOU2-VCnGxkjvC0Sm-YdBGg9Ew7h5qj203MOZclo_rwIONZ2Nq2gdjV_pHebYUq0WomWcuS0F56qVaY3LzHcW6krFyQebaBLMaseNaUauumw53tLY04Gs2JaoYlnkwDx0C2pwPbf7g-4tF8mavhH5iltc19YXAR0fIAkw9CR4NjLdu6S3a1k93KqmRo0bTR7OmK9CekJsxrZM3ONx_mvmwSV6FCjKtMpnPdYPsw--uwv4IcH78JqHBraKCRFP-h2wBaYl13BLcVbAdE8P5lK6fVS-7uWyORuB9iRLKpfMw_dBKl4THr3pRh61MMzaI0iPNOfDlXhmkkp5Of-gbV-CLYsJJ0c1-rY6CfPt89Ou8vOxrte1cdyHPs66tUqWqBXNdhtAewGYl_PM8fesYz8B9LwYkZQ1_dkm2k4fnfJc6ppiO3GcHhBB-frFW8d4l4Q_-MyAC8WM74E5o-NWK15mnN6D_ov2sumQw06wwh_qY92gYy3UzLRwLqWnCL13_7GWJMLGvR7FiuGqFGOSNZQbGIm7QipZHuYyuTjB0J_HTwpBwxyMYs_SZRF7GslDOTd1dDIOz1kl1WOIZkkkJ5yQjpbaZLqt9JY8zZOhvm1fYsHwTUj9gIUNlVCLys6nzf9m2-MWqyD-bvnqtpNbfP-dBwpbSHJj964wIWEovs8qo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکی، درباره ایران:
ایرانی‌ها دو بار به‌شدت تنبیه شده‌اند. باید فکر می‌کردند که پس از این، ممکن است شروع به یادگیری کنند که رئیس‌جمهور ترامپ جدی است وقتی به اقدام نظامی فکر می‌کند و آن را تنها گزینه می‌داند.
او به آن‌ها ابراز داشته است که اگر حاضر به رها کردن جاه‌طلبی‌های خود در زمینه سلاح‌های هسته‌ای و غنی‌سازی اورانیوم نباشند و اگر حاضر به باز کردن تنگه هرمز نباشند، آنگاه درگیری نظامی بزرگ روی میز است.
آیا او این کار را خواهد کرد؟ من نمی‌توانم به این پاسخ دهم زیرا او تنها فردی است که انتخاب شده و تنها فردی است که مجاز به اتخاذ تصمیم و سپس اجرای آن است.
اما من به شهود او اعتماد دارم. او در این مسئله شهود خوبی داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/142744" target="_blank">📅 01:47 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
