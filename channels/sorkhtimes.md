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
<img src="https://cdn4.telesco.pe/file/gO1DGM0xjkVNCgfyuXaA5oR_iy_nyCfP0q1AiuoR530jo7GTejCLCUWafjB0yjheb19ZogcFrJma6Mw4xTdxIRSZrnlZ5ZiOIodnKYgRotj1xzExZYvOaYPK0QAGz-zAz9Xr-LmcXKafrQ0v64k0CVcMZA-fA-Nu6ptRr6eUJ0rZa_5IRHkBa2xFhPqc5x5U8VQQ_naPlZXiC0AXRhkRcOEttZ_ixKlMTnwemUAjBsKUqsNaHfEvcuPSBaLFGYYVUYD66j28vQxiL1xJuyMqgx-uOOEIaqBkRtWNsVfMOOvb3AyV63LkZ8VTIw7WJYDzn3IvVdCoJ-0Eexb0WdMIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 01:28:00</div>
<hr>

<div class="tg-post" id="msg-134893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💬
چه همزمان فیض بخش و خداداد عزیزی اعلام کردن اسکوچیچ کنسله
🤝
😵‍💫
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/SorkhTimes/134893" target="_blank">📅 01:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=YnvJGexeS3l-NV2OGdYT_DwvKEzBf439cn7Mwc_v-1syUiO5Yc4b9u3sNdtst-ZeoLSqXNyUGZfHWGfitameKOiTUbcBGZ9g6HHbK5Clc5s7IJRfua1EGTn3sd3oLTqx7Ni94df3-hkp0UqXHpzIfn9NFVnAhxDrNBz2BQMm6ciJ1wFCeVMEg0oV7SNjO7NGVMnN0OwWSj9BYRFdrIkQ-M2DTnmLLWRaU8OmLuAsYBPqSOlsX0FhnRFfAEozCwmWxVtaPwNx9xQ9wDITyKw71TFgjpdKvswMxpuCblF6ZJhvgL0Bs03_vIgOjH7ozHsXv-GUmKDEGE5dzrrCjna8uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=YnvJGexeS3l-NV2OGdYT_DwvKEzBf439cn7Mwc_v-1syUiO5Yc4b9u3sNdtst-ZeoLSqXNyUGZfHWGfitameKOiTUbcBGZ9g6HHbK5Clc5s7IJRfua1EGTn3sd3oLTqx7Ni94df3-hkp0UqXHpzIfn9NFVnAhxDrNBz2BQMm6ciJ1wFCeVMEg0oV7SNjO7NGVMnN0OwWSj9BYRFdrIkQ-M2DTnmLLWRaU8OmLuAsYBPqSOlsX0FhnRFfAEozCwmWxVtaPwNx9xQ9wDITyKw71TFgjpdKvswMxpuCblF6ZJhvgL0Bs03_vIgOjH7ozHsXv-GUmKDEGE5dzrrCjna8uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود
، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/SorkhTimes/134892" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=REgBAsnI_fEo2C0H-eanY7sCWJXoqv3seT5Pnz-_zcuPoGlVt1FiDLUewabs0H0jF-TY85u9RgQm-Reg1M95QQ06KLqVWvk5o1KFxjlQs-8uz_LLyRuo6kj2VxiZYWUhChRcnbTcpB6POFVWsPKbPrqv91ps45Fqjip525a7hhSw94Xxo_l3m9bJRbYbUnsGG6L1Oj5Dnc5FZMj7BficwrlLglTMzhc_7S0yPc9_oFgn72ghnPZjrocUOd5upa_ffxx3AWKyAD_6c2bJ-DTRkJXmCNPOUw-__7zLSyiz66TB5ilCk7UverKXkCEDHEFG4hZkhmvP7AjfuFQRsTxhmaqMn1BpHP9quMMCWVQCxgkBWBbsljWCepgltULBuTHLBih4pekyn-xAPRpHiCnup1vS0x28RMIlqFNvkGMuhePuQkN-f-OHhGYRO0M93f6DQ2Dc9C9trCr9aezuUjoI557NlBVCUrdYl4ZfrfNj9cDytvfDtR_WyzUUSb5rAO_iLTPVz2shcHbcQ2coZfgQ-FAWZ7lbJ1Z2drPzfEp_iwhNvGjoaZvFI237F_ZxhvC3boyifVSrpMchYEs0MjeHbsXos7dL7EKrRBK-4vG1tPHwnAR7Ul_C8vIPrnRTz-58PHTW6NWTqobcUw45-DhJt62Sg9i3w4IIId0y36EZrL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=REgBAsnI_fEo2C0H-eanY7sCWJXoqv3seT5Pnz-_zcuPoGlVt1FiDLUewabs0H0jF-TY85u9RgQm-Reg1M95QQ06KLqVWvk5o1KFxjlQs-8uz_LLyRuo6kj2VxiZYWUhChRcnbTcpB6POFVWsPKbPrqv91ps45Fqjip525a7hhSw94Xxo_l3m9bJRbYbUnsGG6L1Oj5Dnc5FZMj7BficwrlLglTMzhc_7S0yPc9_oFgn72ghnPZjrocUOd5upa_ffxx3AWKyAD_6c2bJ-DTRkJXmCNPOUw-__7zLSyiz66TB5ilCk7UverKXkCEDHEFG4hZkhmvP7AjfuFQRsTxhmaqMn1BpHP9quMMCWVQCxgkBWBbsljWCepgltULBuTHLBih4pekyn-xAPRpHiCnup1vS0x28RMIlqFNvkGMuhePuQkN-f-OHhGYRO0M93f6DQ2Dc9C9trCr9aezuUjoI557NlBVCUrdYl4ZfrfNj9cDytvfDtR_WyzUUSb5rAO_iLTPVz2shcHbcQ2coZfgQ-FAWZ7lbJ1Z2drPzfEp_iwhNvGjoaZvFI237F_ZxhvC3boyifVSrpMchYEs0MjeHbsXos7dL7EKrRBK-4vG1tPHwnAR7Ul_C8vIPrnRTz-58PHTW6NWTqobcUw45-DhJt62Sg9i3w4IIId0y36EZrL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی : پرونده حضور اسکوچیچ در پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/SorkhTimes/134891" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/SorkhTimes/134890" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
آقای حدادی .بانک شهر پاسخ گو باشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/SorkhTimes/134889" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eod6zoLYDJN4Hy51z7ExdeEqixLdedMKohtuX5A1NpISQJakwxQaTw46sgz2BWNYWJP0cw-DnGExqwXE8AnLWbWm1ERuo7FxQmUu_3cUoedQ8A5KdHSJ5-3--t5k0zxGpcFJBwHVk10x62My-8WntO15w97U4xxmmbEHZkVxn44i5Z4a-BaB2VB0P1BhLj_NshUElacrH6nTYKLViTvIoM8SKLFMR-gyBxe4zFTfsrxmPXCap4MDPYZpA8Cmc-D9IlSSEOEzEAhEc95A8GIY431-0dL1n2yh6W5Aoztjqvy8IiVoCrLLJRlG905ueY_ZguCg3hLXAMHdti6TmJOq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/SorkhTimes/134887" target="_blank">📅 01:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
گویا همه مسیر ها داره مسدود میشه.یکی از نزدیکان و افراد ایرانی نزدیک به اسکوچیچ، بهم گفت؛ بعیده این انتقال صورت بگیره.
🔴
البته باید منتظر واکنش رسمی باشگاه موند . چون اعلام کردند ظرف چند روز آینده ، همه چیز مشخص میشه//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/SorkhTimes/134885" target="_blank">📅 01:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
امیررضا رفیعی طی روزای اخیر به مدیریت باشگاه گفته میخوام جدا بشم و به زودی این اتفاق رخ میده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/134884" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLwXnms0a1iDlqBjW20kre0XCCf6NY_guDGoDPcBXy6RRqV1G0I6HBdSWmNH7jCIvjwzqgvVgAhK4IY0uowQ434VBHmib9HEcFkGFlRYxePmpvDR-CRGrVarLC2wDYW0mB0vfwU18iFbUoGivEIn4RnSh52YMTf-7VHzJzMLKJk7OwfuTZxT4NZCb_gspGopwPE3loTkJ5el-3OY-6On8qEQ9TqsQtfm1KY9FHkWohvEbgfAIUgMvLFa3wFgslKxGPJUlw96v2Ad7c28BiYK9bXRotYbYtGMtECmXFG7mC3hrXipuWl6NpRn-6GU0oCJUUsk6sdl-RNX-wOcog6D_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تیمای آسیایی تو جام جهانی
:
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/134883" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/134882" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/134880" target="_blank">📅 00:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
بازم تاکید میکنم اسکوچیچ مربی پرسپولیس در لیگ ۲۶ خواهد بود
🎙
طاهرخانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/134879" target="_blank">📅 00:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی
⚽️
🤩
رسمی؛اوسمار ویرا از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/134878" target="_blank">📅 00:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWpI1DdBhTwl1cbLbrFgxF-AalxWct3HR4i0_9ARk-3rEYSdT9pTAMwjXsBlzJb5PsRB0ZFFpWXAAm5DX4ewL8Fxwv013-CDpE1gRmE3LokiMdGcqsgxMAI5k2kE6Twpi91HvJ74G59iYqEuG__1zmYeeRSGV-fxnlNgO3uiz7IClqmmrkOkOdrdts-A3MZvW84hjBM-_Rmh48f3HL2-6BqoO6DEwE-PUGpt_6joRnXOBOuRAYkalBI5F9VXnku_t7-lDBOtbqQ1E7q5kWlQx3c2VWlZr9ycdWKlHpjD25hwJKby4hqPOfWj6WXI2IeGVEZwgVEEumU8-HCvrBmPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اخرین نماینده اسیا هم حذف شد.
🇪🇬
مصر 1 (4)
🇦🇺
استرالیا 1 (2)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/134877" target="_blank">📅 00:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
ادعای رسول خطیبی:
🔴
زنوزی مالک باشگاه تراکتور بچه بازه و همجنسگراست!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/134876" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
پرسپولیس حاضره تا ۲ برابر سقف قراردادش به احمد نوراللهی پیشنهاد بده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/134875" target="_blank">📅 23:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=mOiCRNutIMpL6tk1tcaGhHYbDODWE4aNf6YuuNdni9pBrwLQB7fXeXJH7QF9olfPP9V5869YeaOQvSu5bI27ZPVaPZVnAS4xAPzQ7bXR2KHuWfuFqLGp7GJfCD0jm6PFHflVxIrKOmlI6xnAuI-Dh2jzlVVWLj2ZXLxgggbQvIU5uWP-tLaDrhoB75eKx3idVZnl-DOcaIJ4PjDamF9blpmDMFqgA3yRIYfrqvwbNIVS_AK-7e8_9hFRy2FCwf9zrqZCYkD4-Hox4LQRinkx_BBzI5468gaxM0VztZ0tknKJAgwdTZn_dJw4EzT6dORVxBduh4uOb06iXpVIskNwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=mOiCRNutIMpL6tk1tcaGhHYbDODWE4aNf6YuuNdni9pBrwLQB7fXeXJH7QF9olfPP9V5869YeaOQvSu5bI27ZPVaPZVnAS4xAPzQ7bXR2KHuWfuFqLGp7GJfCD0jm6PFHflVxIrKOmlI6xnAuI-Dh2jzlVVWLj2ZXLxgggbQvIU5uWP-tLaDrhoB75eKx3idVZnl-DOcaIJ4PjDamF9blpmDMFqgA3yRIYfrqvwbNIVS_AK-7e8_9hFRy2FCwf9zrqZCYkD4-Hox4LQRinkx_BBzI5468gaxM0VztZ0tknKJAgwdTZn_dJw4EzT6dORVxBduh4uOb06iXpVIskNwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
😐
میثاقی امشب به سیم آخر زد و شماره موبایل اصلی خودش رو به صورت کامل روی آنتن زنده اعلام کرد تا مردم بهش پیامک بزنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/134874" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
اسکوچیچ برای خودش ۱۸۵۰ میخواهد به اضافه ۲۰٪ آپشن. همچنین برای دستیاراش ۴۰۰ تا میخواهد و گفته مالیات خودم و دستیارانم را باید باشگاه پرداخت کند
🚩
مجموع این ارقام ۳ میلیون دلار میشود.
✅
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/134873" target="_blank">📅 22:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
پرسپولیس و اسکوچیچ به توافق رسیده اند و تنها بر سر مبلغ قرارداد اختلاف دارند.
🗣
🗣
سایر موانع و مشکلات جذب این مربی کروات، حل شده است. باشگاه از اسکوچیچ تخفیف می خواهد و او تخفیف هم داده است، اما باشگاه باز هم می گوید باید از قرارداد کاسته شود.
🔻
🔻
مسئولان…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134872" target="_blank">📅 22:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134871" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#تکمیلی
🔴
💥
یحیی گل محمدی به محسن خلیلی گفته من تا شنبه میتونم صبر کنم از یکشنبه اگر منو بخایید باید ۳۰۰ هزار دلار به دهوک عراق پول بدید رضایت نامه منو بگیرید.
🫦
قابل توجه اون کصخول هایی که میگن نه یحیی نمیاد تیم داره با اسم امپرور بازی نکنید  #نه_به_مربی_ایرانی…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134870" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرسپولیس 48 ساعت برای اسکوچیچ صبر میکنه، اگه پیش نویس قرارداد رو امضا کرد که هیچی کار تمومه، اگه امضا نکرد میرن سراغ گزینه بعدی / آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134869" target="_blank">📅 21:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
پرسپولیس و اسکوچیچ به توافق رسیده اند و تنها بر سر مبلغ قرارداد اختلاف دارند.
🗣
🗣
سایر موانع و مشکلات جذب این مربی کروات، حل شده است. باشگاه از اسکوچیچ تخفیف می خواهد و او تخفیف هم داده است، اما باشگاه باز هم می گوید باید از قرارداد کاسته شود.
🔻
🔻
مسئولان…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134868" target="_blank">📅 21:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان بهترین کانال آنالیز ایران رو از دست ندید
هر روز فقط یک گزینه مطمئن می‌ذاریم، بدون ریسک‌های الکی.
بازی امروز: کانادا – مراکش</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134867" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚽️
جام جهانی ۲۰۲۶؛ وقتی تحلیل درست، سود می‌سازد!
این‌بار نوبت جدال
کانادا
🇨🇦
– مراکش
🇲🇦
است؛ مسابقه‌ای که آمارش یک نکته مهم را نشان می‌دهد:
«مجموع گل بیشتر از ۱.۵» یک انتخاب کاملاً منطقی و ارزشمند است.
دلایل:
✅
کانادا مقابل تیم‌های سرعتی بازی بازتری ارائه می‌دهد.
✅
مراکش استاد ضدحملات سازمان‌یافته و استفاده از فضاهای پشت دفاع است.
✅
اگر یک گل زودهنگام ثبت شود، ریتم مسابقه کامل عوض می‌شود و راه برای گل دوم باز می‌شود.
ما فقط احساسات را تحلیل نمی‌کنیم؛
داده و روندها
حرف اول را می‌زنند.
❤️
برای دسترسی به دقیق‌ترین پیش‌بینی‌های جام جهانی، همین حالا عضو شوید:
👇
👇
👇
https://t.me/+iIi9FxzzcYBjNDg8
https://t.me/+iIi9FxzzcYBjNDg8</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134866" target="_blank">📅 21:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134865" target="_blank">📅 20:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134864" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134863">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134863" target="_blank">📅 20:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134858" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134857">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134857" target="_blank">📅 18:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇹🇳
یک اتفاق عجیب برای تونسی‌ها در جام جهانی؛
❌
دوپینگ ۸ بازیکن مثبت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134856" target="_blank">📅 18:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134855">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
جدول نهایی گروه F جام جهانی ۲۰۲۶
🇳🇱
صعود هلند به عنوان تیم اول
🇯🇵
صعود ژاپن به عنوان تیم دوم
🇸🇪
صعود سوئد به عنوان تیم سوم
🇹🇳
حذف تونس به عنوان تیم چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134855" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134854">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
🎙
رسول خطیبی: محمدرضا زنوزی، پس از باخت ۴-۲ تراکتور مقابل استقلال در تبریز، جشن گرفته بود!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134854" target="_blank">📅 18:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134853">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134853" target="_blank">📅 18:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134852">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
❗️
فوری؛ شنیده ها: ابواالفضل جلالی خودش رو به پرسپولیس لینک کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134852" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134851">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/134851" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134850">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس: هیچکس از مدیران باشگاه به هیچ عنوان با خداداد عزیزی حتی یک تماس هم نگرفته و خداداد حتی گزینه هم نبوده و فقط از طریق لابی و رسانه ها خودش رو گزینه پرسپولیس کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134850" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from"mehran"</strong></div>
<div class="tg-text">اگه برگردیم به دوران یحیی بدبخت میشیم
بزور امثال پاکدل و دهقان و ابراهیمی و نعمتی و صادقی و فرجی و عیسی و خیلیای دیگه رو بیرون کردیم
تازه هنوز ی سریاش تو تیم هستن مث سرلک کنه</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134849" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134848">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">یحیی بیاد که دوباره باندبازها توی تیم بموننن و دلالی باهمدیگه</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134848" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134847">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134847" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134846">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134846" target="_blank">📅 17:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134845">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد علی الخصوص که اون شخص یحیی گل محمدی باشه همین آقای خلیلی هست!
#نه_به_مربی_ایرانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134845" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134844">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسکوچیچ امضا کرده و الان رسما سرمربی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134844" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134843">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
میثاقی: قرارداد پرسپولیس برای اسکوچیچ ارسال شده، روی مبلغ قرارداد یه چند صدهزار دلاری اختلاف دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134843" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134842">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
خبرگزاری تسنیم:
🔹
تنها مانع عقد قرارداد اسکوچیچ با پرسپولیس اختلاف مالیه که همچنان پابرجاست
🔹
مدیریت پرسپولیس خواستار تخفیف چند صدهزار دلاری شده
🔹
اگه توافق با او صورت نگیره احتمالا گزینه ایرانی مدنظر باشگاه خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134842" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134841">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134841" target="_blank">📅 16:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134840">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134840" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134839">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134839" target="_blank">📅 15:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134838">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
بازگشا سخنگوی پرسپولیس در مورد روند مذاکرات با اسکوچیچ :
❌
❌
تصمیم‌گیری، مذاکره، تفاهم، عقد قرارداد و امضای توافق با یک سرمربی در شأن باشگاه، نیازمند جلسات متعدد، بررسی‌های دقیق و رفت‌وبرگشت‌های فراوان است. اطلاع‌رسانی لحظه‌به‌لحظه درباره روند مذاکرات و چالش‌های…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134838" target="_blank">📅 15:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134837">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
بازگشا: به یه ضد پرسپولیسی داخل باشگاه اجازه موندن ندادیم. هوادار مالک باشگاهه، از هوادار سواستفاده نکنید که بمونید و کنار تیم دلالی کنید. آخرین اخطاره باج نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134837" target="_blank">📅 14:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134836">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134836" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134835">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134835" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134834">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
❗️
درحالیکه استقلال ، سپاهان و تراکتور تمرینات شون برای فصل جدید شروع کردن اما خبری از شروع تمرینات پرسپولیس نه تنها نیست بلکه حتی تکلیف نیمکت هم مشخص نیست!
🔴
🔴
حدادی داره کاری میکنه تا دلمون برای درویش تنگ بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134834" target="_blank">📅 12:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134833">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
🔴
فووووری؛ رضا شکاری از پرسپولیس جدا شد و به زودی‌ لژیونر میشه. تیم جدید شکاری در قاره آسیا خواهد بود/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134833" target="_blank">📅 12:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134832" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134831">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
خداداد عزیزی: ایرادات و مشکلاتی در پرسپولیس هست که این تیم را دچار بحران و حاشیه کرده است و تا حالا این مدل کار کردن رو ندیده بودم. در صورتی که در تراکتور همه چیز با یک زنگ به زنوزی حل میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134831" target="_blank">📅 12:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی:علیرضا دبیر اصرار می‌کرد برم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134830" target="_blank">📅 12:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🔴
دلیل ناراحتی اسکوچیچ از پرسپولیس اینه که قرار بوده باشگاه بهش پیش‌پرداخت بده که تا الان این اتفاق نیوفتاده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/134829" target="_blank">📅 12:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134828">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134828" target="_blank">📅 12:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134827">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووووووووری
🔻
احمد نوراللهی در آستانه بازگشت به پرسپولیس/خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134827" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134826">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
#فوری
🗣
حضور کسری طاهری در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134826" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134825" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
خداداد عزیزی :
🔴
🔴
اسکوچیچ سه هفته منتظر قرارداد با پرسپولیس بود خیلی هم راغب بود بیاد اما هر سری از طرف باشگاه بهش جواب درست نمیدادن
🔴
🔴
ما حتی برنامه ریزی نقل و انتقالات خوب کرده بودیم با چند بازیکن شاخص هم در حال توافق بودیم که همه چی بهم ریخت، داشتیم…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134824" target="_blank">📅 11:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134823" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsNhXBbCzsqaPtBUO_oVyfgs_JsbrY0o2uyJllD0guDWeuj6suW04DoOJRSuL5s1DkFiM3aNty7RyVaCUCH_Tim33-fnmMQ_MaocFSRSQHlBKVaUiXslflkvIW9BvN8W4lLFTJQCwY76nZYMKBhPrBBsjwAE2b5VKrqTm-zyQ3plDGS_zYxmGvlqyxHppk5-W13kvM6LV0JppNQk9yK0d-gnvymKH1gZWGNcnkLTlp8k4MPS5bIVVYWNg5YeiH6YjUUNN-ve3k7dGdGs1UpXbdYQlbMR4ON5wKKN-xJmMhJio2Gvga2ffygzVXieSzkTNKIuSrCwljdaOFeFLhF_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
پرتغال موفق شد کرواسی رو شکست بده و در مرحله یک هشتم به مصاف اسپانیا میره.اونم فقط 72 ساعت دیگه ..تیما دیشب بازی کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134822" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134821" target="_blank">📅 10:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134820">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
رونالدو فقط انقدر تنها 25 گل با 1000 گله شدن خودش فاصله داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134820" target="_blank">📅 10:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134819">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لحظه‌به‌لحظه با نبض واقعی مسابقه</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134819" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134818">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مزیت عضویت در کانال ما
با عضویت در این کانال:
فوتبال را حرفه‌ای‌تر دنبال می‌کنید
از تحلیل‌های سطحی فاصله می‌گیرید
درک بهتری از تاکتیک و جریان مسابقه پیدا می‌کنید
همیشه یک قدم جلوتر از بقیه خواهید بود
اینجا فقط خبر نمی‌دهیم؛
اینجا فوتبال را کالبدشکافی می‌کنیم.
https://t.me/+hhwRu0jTAzswN2Nk
https://t.me/+hhwRu0jTAzswN2Nk</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134818" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134817">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp8BnZsWWIbDsQV4r7X6KTZvcvxcB4jo0uEhSoMHPo5yV7fedbQuQ7hG5FufROizurfb8VQV_dZyaqumMOAk2cep_0dJfa39VYI8YkYozEod2CWYVD3i4XlnYnNK5H9Qq0Xze-nFzdbATHdcwOlQK5Pw_P0zyFwV0kD5R1O1qWHR8wv-S-mNQF4mrn0kDvnS1yRUT0u8hzRTkM-bsWKSsHkSBJuvVkGlnLzzBIxAtF1EmPolLLLYZ_lrR_IshlbnjLnud8vZE9dEBuABCwhtpZHCuDmI29FF0KQlxP0d6ddkcgdNVt6Vn-7q7K1yKrGGboh0WeHpm83ojuuvxT1Gig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
استوری خیلی سنگین رسول خطیبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/134817" target="_blank">📅 00:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134816">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1aQ0iWVzn5jra2g2O8yqMBoPPhQc1ZASVB8YMKvbwixKiOaKwQuvSj8kAa9tI8UFaCNqJT9inxhoR7axeIQXsXn4Nn9vlf1x5nl4wspg0ZpP_rI2LeqkdcqqkyRqL00K3z6PgDka6O57szG9FX2IvVoQuESJ4bmaqRVmBVOUqDQfYO9MEGm264uqU5Vhy4dWvSVJIcyE9Qp39H9uhcxBE7OdVZgej1YJmeTxXRpjosslSRvYr6pB6E4lsTko_wZMYRQcQvUwA0hIAVomE23J_VAZnnqqYu-oedn_o0WEqSDYgUaOUSEBDNJlFHTcnOmCeecGV19qTctg6PmjpHG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ادعای رسانه مصری؛ ژاوی گزینه هدایت تیم ملی ایران!
🔴
رسانه‌‌ Smashi Sports مصر، در گزارشی مدعی شد که "ژاوی هرناندز" سرمـربی سابق بارسلونا، در فهرست گزینه‌ های فدراسیون‌فوتبال ایران برای سرمربیگری تیم‌ملی قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/134816" target="_blank">📅 23:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134815">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
#جام_جهانی
🏆
کنداکتور آنلاین جام جهانی امشب و بامداد فردا مرحله یک شانزدهم نهایی:
🇪🇸
اسپانیا
🆚
اتریش
🇦🇹
⏱
ساعت ۲۲:۳۰
🇵🇹
پرتغال
🆚
کرواسی
🇭🇷
⏱
ساعت ۲:۳۰
🇨🇭
سوئیس
🆚
الجزایر
🇩🇿
⏱
ساعت ۶:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/134815" target="_blank">📅 23:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134814">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
زنوزی: هدف خداداد از صحبت با پرسپولیس فقط خوشحال کردنشون بوده وگرنه میدونستم نمیره پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134814" target="_blank">📅 22:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134813">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
واکنش زنوزی به انتقال اسکوچیچ به پرسپولیس: اسکوچیچ مربی بزرگیه و تونست تراکتور رو قهرمان کنه اما او بدون ابزار قهرمانی نمیتونه در یک تیم معمولی دوباره قهرمان بشه!!!!!!
🔴
🔴
پ.ن آقای حدادی آقایون بانک شهر بهتون بربخورههههه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134813" target="_blank">📅 22:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134812">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/134812" target="_blank">📅 22:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134811">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134811" target="_blank">📅 22:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134810" target="_blank">📅 22:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134809" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
صفحه رسمی باشگاه دهوک عراق عکس ها و ویدیویی هایی از معارفه یحیی گل محمدی و دستیارش محمد عسگری را در پست و استوری به اشتراک گذاشته که نشان می دهد مراسم معارفه ویژه ای جذب پرافتخارترین مربی ایران در جام های سراسری برگزار شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134808" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">💥
❌
با مالیاتش میشه ۲.۵ میلیون دلار معادل ۵۰۰ میلیارد تومن/نیم همت
🫦
بدون احتساب اپشن ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134806" target="_blank">📅 21:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
🔴
افشاگری تازه؛ ایجنت اسکوچیچ و درخواست جنجالی ۱.۸ میلیون دلاری
🔴
شنیده‌ها حاکی از آن است که ایجنت دراگان اسکوچیچ به دنبال عقد قراردادی ۱.۸ میلیون دلاری برای این سرمربی است؛ رقمی که فاصله قابل‌توجهی با قراردادهای قبلی او در تراکتور دارد.
❗️
اسکوچیچ در فصل…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134805" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134804" target="_blank">📅 21:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
جدیدترین آپدیت اندروید 1XBET
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
حتما
بدون فیلترشکن
از اپلیکیشن استفاده کنید
🎁
هنگام ثبت نام کد هدیه 130 دلاری vipfarsi را وارد کنید.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134803" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxnzr4YYEBDv5ducyXym0OzaRbNJaScjP94hFzSZzQo3WmaJqDR9P0yTgoC7VZ9D7V4Mnc8F5DOgWM_nT_5zYwTRsfpxyn3R3t8rFNS5YSU4VMGEQPYLAr9LDecHtzUwLFSCeadkicuPD9LI4Ig73ejshzX6d0j8rK_d0AUCn72Biv3T2dPIXcS2BibKJtxfEeh5tG8a7BUyActVYadp9WKrztNiAv2SUOROGbilcvQPXPr5yBQcRztxJGZsXSzlkumuyIpuDdyFcmvRSCHB6XzLaMQPlov3JinULpQZpsjLBZEhWBT8mRwNKodhfplDP5pMDiDbIN1oK5rjE5nhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
وان‌ ایکس بت برترین و خفن ترین سایت پیش بینی بین المللی که به کاربران ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
vipfarsi
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر بازپرداخت هدیه میدهد
🔔
آموزش ثبت نام، واریز و برداشت
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🔑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/134802" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134801" target="_blank">📅 21:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
بانک شهر حضور اسکوچیچ در پرسپولیس رو مصوب کرده و امشب یا فردا باید قرارداد برای امضا به این مربی ارسال بشه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134800" target="_blank">📅 21:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
فوتبالی : پاسخ مبهم دروژدک به دوراهی تراکتور - پرسپولیس
✅
مذاکره پرسپولیس با دراگان اسکوچیچ شایعات حضور احتمالی دروژدک در جمع قرمزهای تهران را ایجاد کرده و گفته می‌شود اسکوچیچ در صورت حضور در پرسپولیس، هموطن خود را هم به این تیم خواهد برد.
❗️
و در همین راستا…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134799" target="_blank">📅 21:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
عصبانیت اسکوچیچ از باشگاه
🔴
🔴
پس از مذاکره اولیه و سپس حضوری در استانبول، اسکوچیچ در انتظار ارسال قرارداد بود که این موضوع از سوی باشگاه چند بار به تاخیر افتاد و باعث دلخوری اسکوچیچ شد. هنوز هم به شکلی عجیب و سوال برانگیز در ۲۴ ساعت گذشته این اتفاق رخ نداده…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134798" target="_blank">📅 21:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔽
در جلسه هیات مدیره صحبت از پنج گزینه ایرانی و یک گزینه خارجی به عنوان الترناتیو اسکوچیج شده تا اگر جذب او به هر دلیل میسر نشد چه کنند
🖥
ممکن است درباره گزینه های خارجی دیگری هم در جلسات صحبت شده باشد.ما از اینکه نام،عملکرد،رزومه،زشت و زیبا و شرایط ۵ سر مربی…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134797" target="_blank">📅 21:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W25nY1GpxJlgtCcgyZltsL4MQIzmDbJ-Pf7T8z33lE_xiaE_1EeUnMnG7OUfSqXwa3G4CmPhn7DFDtreUv6BIuSuiRH8sHK691biMfo7VGL2E2vlWLu4EDj-hh01LkqrCLasP0SAg_BWzl5ymBg9ejZlNuN7HpmC-fPsugrQm_ZCXCVPXd6GvB1b1iARyoREikvNVxkVrwkcWtpoN3_bDI2c0JXlXx3ygzzs7t2KptH5GyULIOer6lUAWR_NStYUnh53uPu5ho1FNlbwIk0bnye9BhQm4lUurRFfZ_HJv19bHSb7nsw8GbGMkf08P2EJCU09yRuo99aIbIoT5oNWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134796" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYtaOu4gIrX2EISWWb4yVlKA6MwiS53mJOnYmwBZlBYXnXUJIFD9W4slBbqH5KkTB3h7ah2gXCQrlF9KNMkWwyVydAcWJ8R3TACHjQmPiw0sDG-oTXi1FlxNvtLp-gBGxC4KLNp9l8NrdvwfP_dmfdms9pKU4zCLgRtG-5SlNIVv1gq5VLdB0dhnSVn-VZ1X0WySGg0DlW3ILPL70ybZ-ByVgwW_ujYwKBtAjdPDBWCa7hyINg6Th_9pZ7NK0FQxWzOBfv7qd6d4sff7vEyiWwMEalur_PgtPAb1qvyit2kC9COnBBasXbysx6C--wujVlLEvODEslEC3Icicwd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف آیمن بازیکنی که در دو فصل اخیر بسیار به پرسپولیس لینک شده بود؛ بالاخره بازیکن آزاد شد
❗️
موافق جذب این بازیکن مالزیایی هستید یا خیر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134795" target="_blank">📅 21:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134794" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134793" target="_blank">📅 19:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134792" target="_blank">📅 19:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
منتفی پشت منتفی..کنسل پشت کنسل  ..نمی‌دونم باشگاه داره چی کار می‌کنه .نه بازیکن گرفتیم .نه سرمربی داریم ....بیاین جواب ملیون ها هوادار و بدین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134791" target="_blank">📅 19:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134790" target="_blank">📅 19:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
خداداد عزیزی:
🔴
تا جایی که من میدانم اسکوچیچ به پرسپولیس نخواهد رفت و حضورش در این تیم منتفی است!
✅
وقتی سخنگوی باشگاه، ناکاربلد باشه و دانش کافی برای جلوگیری از حواشی رو نداشته باشه، باید هم خداداد عزیزی در نقش سخنگو بیاد درمورد مسایل تیم ما صحبت کنه.…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134789" target="_blank">📅 19:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
خداداد عزیزی: حضورم در پرسپولیس منتفی شد و در تراکتور می‌مانم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134788" target="_blank">📅 19:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
سعید اخباری کاری رو کرد که طی ۵ ۶ فصل اخیر لیگ برتر هیچ مربی انجام نداده بود
🔴
آسیایی کردن یک تیم غیر از تیم های پرسپولیس،  استقلال ، تراکتور ، سپاهان و فولاد
🔴
آخرین بار یحیی گل محمدی پدیده رو آسیایی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/134787" target="_blank">📅 17:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134786" target="_blank">📅 17:33 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
