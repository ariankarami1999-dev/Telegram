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
<img src="https://cdn4.telesco.pe/file/WljXVLLMPG9YQQHeppFboPQFOOb4y0k4yYOhaFuwLaFY-EFpYq3xi3e9bqjMUg95Qk035SPcknobCFuC-4MlX1LXLukctDiWLoA-VTDToIbAiTAuusL5RI2nKs4-ExhFYHuDPZ36YMSF1vfNP_f5tTLEEfG9fxV8RpcgfZXsDqkRTqdxFC1vQxw4z_zobSWwbhyTC5DLWVbFuyQemeUI1O1atLxsNSKsQG1XVLjA3R8W8IcRxEjFAPtbO_WoThi8KUKtiKMFY_EMV_V7X_BtfUCsNN4SaQ-DxID2jMicJW0yLS43p_bTZkBqQOQCjgNesjY72XCubt4dc2n8r7GkWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 23:50:17</div>
<hr>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpuafsh7P3IP6UQXM8dLQT6FNMKzZNPQreJoxVUyVL-BVailUAIWepimpbxDV_63dW8yLkp9qogxGIhUeGq7U1zGuqv9aBl5_9xybs_Q9_Rs7KQs3ii6fM1jwKHkt_T7-ysLXQOqEtm67E5TRoHjDhKv_7GoT4XKEJVH7e15746srfYLeDI2aUc923F0rolYgalh04jdbZGU82d9EattCqr3u9rR8fiX-rHRCMSP8X35MamMf4MxDUHlEORE-yjBvO_ogWAw6EeBFvNiMdRJD9KXI-LGtAs1Gc7l9cnzQCrjdmRl83vDbxPZWlGGsCh9ETLjObbU1JaAQlznuQrxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔹
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔹
خروجی عکس با کیفیت بالا
‏
🔹
بدون نیاز به کارت بانکی و پرداخت
‏
🔹
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kev4zIZnP932u1pUzHaao6mocANrneVm9esqMo7TOPJ_0nIDSF_iRrSSlaFed1WriYYfgfRLKzNzTumNFCY1K0Q2t6DLIrrzLThFMNLvxe13KRuED1-WUhKL7_cBbo21hk-K3tumyBp_tgNyQXz7Y6EdZm5i2jD6iaTdeBru8KuqHJJ1XsKvDuXmwWi8m-qE-b79IQeMfrZRracoXW_XlRPqEUgDtHd3b3XnzcEb-jgeNAdT2-PDZm3uu89HPsKJ1V5IWs7-iMyxVb8Zir4S7VXP3OoQQsKrqtKLVlVfmGzMyZSeX_ddIybK8iDKFL0pFY5-xwo05xaVbyMWbj3HMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
200 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 5 | Sonnet 5 | Deepseek 4 flash 0731 | Grok 4.5 | GLM 5.2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://seekai.cc/v1
قابل استفاده در
Vega Agent
☑️
از این
بخش
هر روز 20 دلار بگیرید
☑️
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
200 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VklyWePl4vdlreemgCQZ8c4JhFFfYJNNWHX_rM4uobq0poOoO3TK90uWUk2eF83gRE-kofHGPNGGYc-XOjsyP6lavMNipOBfLT2gKYKFBVeHofIuYvvAXa8onIQ36Ej4ex6HaekyJaVJZjcpMLQwijAJF5kqTDheGjCrXhZnz4IXxsSl8AmvNLIfSaipB4vm46ZPWndo2bwYcR2xOjOEwZN2VfqGKqWZRK6D6GlxRyPjBtRLtFqsQA1t8RlRf5FmDcXGp0yQUL5nav3LdF-4X8XhhoSSmOKuDSTg2etcy8jC_1tNhoNNLtcXrRoD6P3vWUuHse43rVRb1I--SKkgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGHgq2vwJnsrYClefxfM4xa8OlHKtCd926nXuhpaZ11mEdf3zahWl7NTKtGOzqUIoBqZfaIkceWj9_B56puBEc46e7BfvKeEz9EBPWTrVhHHvpfmB2N1-V0cwhR-DOpz98srWYflthexRUnOf1aAXFKOE2fVpFdTJyAHWdwBS5mPomknK3UuP98ia_I9wjssDGcRBmuxMmHyIZc8ryTH2AjzBtLp14jxS0vsxzugSuFJ5u12xdTna7g684kVQhicZNLlRCWTUBcp2p43mV2i5C3m55F9E0W7T1luRdyq71xRXRamAP2GR__m6fVid26SE8y4jy688yx21siMvFN0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به مدل قدرتمند ‌Qwen 3.8 max
🚀
‏اگر برای پروژه‌هایتان به یک ‌API⁩ پرسرعت و رایگان نیاز دارید، همین حالا دست‌به‌کار شوید:
‏
1⃣
در این
سایت
با جیمیل ثبت‌نام کنید
2⃣
‏ از این
بخش
با اکانت تلگرام وریفای کنید
3⃣
‏ دریافت ‌API Key⁩s
📍
‌Base URL⁩:
https://api.aigate.shop/v1
‏
⚠️
توجه:
این دسترسی فقط تا ساعت ۲۱:۳۰ امروز فعال است.
⏳
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oenykGLBFQBejjryt6r28XfF8qrBWBBL5vMXE5E4GqmFbpfuq1itio8mUOvtZ9Tz98H4BKVs0-ebxDYKMUoebAYtdHVlGAVA3-TPZPnV3kcgjeL2ZBLC25rS4IU2_03fwvDm1RujJYLtghEfY7q2xnxu51OWeHc36OIWIwAW2lqicgWrFCoFgCAObAh_c4fV7IC7j_D_01LFmih-bbXblcgPZgVkgACGlwpV-AHTPILz_-80ymRz8YSRnJaUXD6exS1iLcu1eMvkY2DktaTCDWscuVmBCIHFSdaV0Goisr3rxeLMSsOkHMFvcsVCymzVmZztVbAbbRge9dsoaR-TtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
30 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Fable 5 | GPT 5.6 sol | Opus 4.8 | Sonnet 5 | Gemini 3.1 pro | Grok 4 | Nano banana 2
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب ( قدمت حداقل 14 روز ) داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://routllm.pro/v1
قابل استفاده در
Vega Agent
☑️
🎁
با هر رفرال شما
5 دلار
و شخص دریافت کننده
30 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=JW4GLS0TGuX7dFt4En91zovt_l__0JfOdPZar7V1KjJro_RjHgOb7jp9fmyby2JOOf_yLzJBaFh3aD2kAwYq9uzkNVGqBOa8fQDQhu9REwutY6MhDPhv-mwKHG2-OP72pDfYKBb0Gu2BUbyKLZxX_xRjn24gZ33EQhov4RHWjmFeO8siATL_lvbWaay0MCVzc2iUdx_cvt9tetDbXubeZzcc1d4k0KBe8is_LgAe-reXgyfyfWgWhV9dLVmqEkQr5ctGNVb7S8b4K0wCuxcjXdDjRBaoAChPTfWhDZ4JfNCIoRcoLG0pGl2Q0GuPKP1qkGUMpCBGhVf9MKS_af_C1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=JW4GLS0TGuX7dFt4En91zovt_l__0JfOdPZar7V1KjJro_RjHgOb7jp9fmyby2JOOf_yLzJBaFh3aD2kAwYq9uzkNVGqBOa8fQDQhu9REwutY6MhDPhv-mwKHG2-OP72pDfYKBb0Gu2BUbyKLZxX_xRjn24gZ33EQhov4RHWjmFeO8siATL_lvbWaay0MCVzc2iUdx_cvt9tetDbXubeZzcc1d4k0KBe8is_LgAe-reXgyfyfWgWhV9dLVmqEkQr5ctGNVb7S8b4K0wCuxcjXdDjRBaoAChPTfWhDZ4JfNCIoRcoLG0pGl2Q0GuPKP1qkGUMpCBGhVf9MKS_af_C1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
تبدیل هوشمند وب‌سایت به پرامپتِ حرفه‌ای!
🚀
‏دیگه لازم نیست با کپی کردنِ تبلیغات و بخش‌های اضافیِ سایت، وقتِ هوش مصنوعی رو بگیری. این افزونه، محتوای هر صفحه رو به یک متنِ تمیز و استانداردِ ‌Markdown⁩ تبدیل می‌کنه تا دقیق‌ترین پاسخ‌ها رو از ‌ChatGPT⁩، ‌Claude⁩ و ‌Gemini⁩ بگیری.
⚡️
‏
🔹
حذفِ آنیِ تبلیغات و المان‌های غیرضروری
‏
🔹
تبدیلِ ساختاریافته به فرمتِ ‌Markdown⁩
‏
🔹
سازگاریِ کامل با تمامیِ مدل‌های هوش مصنوعی
‏
🔹
افزایشِ چشمگیرِ دقت و کیفیتِ تحلیلِ داده‌ها
🔗
GitHub
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-83-arm64-v8a.apk</div>
  <div class="tg-doc-extra">42.2 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📦
پروفایل پشتیبان NekoBox+
با توجه به
شرایط فعلی
،
اختلالات پیش‌آمده و قطعی بسیاری از کانفیگ‌ها و VPNها،
با این روش می‌توانید به
مجموعه‌ای
از
کانفیگ‌ها
با
پروتکل‌های
مختلف دسترسی داشته باشید و در صورت
قطعی
، گزینه‌های دیگری برای
اتصال
در اختیار داشته باشید
☑️
🔹
روش استفاده:
1️⃣
ابتدا برنامه
NekoBox+
را نصب کنید
2️⃣
فایل
JSON
را دانلود کرده و
Save
کنید
3️⃣
وارد
NekoBox+
شوید و از منوی
☰
به مسیر
Tools → Backup → Import File
بروید
4️⃣
فایل
JSON
را انتخاب کنید
✅
تمام
.
تنظیمات
و
پروفایل‌ها
به‌صورت
خودکار
به برنامه اضافه می‌شوند و می‌توانید از
کانفیگ‌های
موجود استفاده کنید
📌
این پروفایل شامل ۱۴۰ اشتراک و گروه با کانفیگ‌های متنوع است
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=IaIaOT7NjKv9LbMIkUaOYQZnrYObzJECLhF70pqjJL39smQB0ndTT56Q2uy6VeXA69S9X7CJaFylq6DrgWrXGJtGMSoXIf8stLA6HBzI26NpgJvvFewJ_x-Z2f4HkHoIltah-k8UObycbj7fRKxBrwJ69_mC6dSCh9dGx8rTXGBDNTdoeVhYmHCduL-aB9U3VYJhzW0qCFdWepHR47hyED2iXxRjxc701kiOL-UOj90iMwF5vgzK7t5FC3WNCyCnGnwJQAXXE_Ktm7RTo3TFuyzu8VYuu9FSts0p4xXKpkXiqJGuweCVx_bJQa6iybSZK7zHQX2aK66Oor0uMAfEWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=IaIaOT7NjKv9LbMIkUaOYQZnrYObzJECLhF70pqjJL39smQB0ndTT56Q2uy6VeXA69S9X7CJaFylq6DrgWrXGJtGMSoXIf8stLA6HBzI26NpgJvvFewJ_x-Z2f4HkHoIltah-k8UObycbj7fRKxBrwJ69_mC6dSCh9dGx8rTXGBDNTdoeVhYmHCduL-aB9U3VYJhzW0qCFdWepHR47hyED2iXxRjxc701kiOL-UOj90iMwF5vgzK7t5FC3WNCyCnGnwJQAXXE_Ktm7RTo3TFuyzu8VYuu9FSts0p4xXKpkXiqJGuweCVx_bJQa6iybSZK7zHQX2aK66Oor0uMAfEWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
کپی‌برداری از پروژه‌های گیت‌هاب با قدرت هوش مصنوعی!
🚀
‏تا حالا شده بخوای یه پروژه خفن رو از گیت‌هاب درک کنی یا مشابهش رو بسازی، ولی غرق در پیچیدگی کدها بشی؟ این ابزار جدید، کل ساختار مخزن رو به یک «پروپوزالِ اجرایی» تبدیل می‌کنه تا بتونی با کمک هوش مصنوعی، اون رو بازسازی یا تحلیل کنی.
🤖
💡
‏
🔹
آنالیز هوشمند:
بررسی دقیق ساختار و معماری کلی پروژه.
‏
🔹
مهندسی معکوس:
استخراج منطق اصلی و اجزای حیاتی کد.
‏
🔹
تولید پرامپت دقیق:
ساخت دستورالعمل‌های گام‌به‌گام برای بازتولید عملکرد پروژه.
‏
🔹
شتاب‌دهنده توسعه:
ایده‌آل برای یادگیری سریع، پروتوتایپینگ و درک پروژه‌های سنگین.
🔗
https://www.gitreverse.com
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ربات تکه‌تکه کردن و آپلود فایل‌های حجیم در تلگرام (بدون دیتابیس!)
🤖
📦
یه سورس
ربات تلگرامی
فوق‌العاده جالب و خلاقانه براتون آوردم که روی بستر کلادفلر ورکرز (Cloudflare Workers) اجرا می‌شه و وظیفه‌اش اینه که فایل‌های حجیم رو از طریق لینک مستقیم بگیره، به پارت‌های کوچیک‌تر تقسیم کنه و بفرسته تو چت تلگرام!
✨
ویژگی شاهکار این سورس:
این ربات کاملاً Stateless (بدون حالت) طراحی شده؛ یعنی برای کار کردن به
هیچ دیتابیس، KV یا فضای ذخیره‌سازی ابری
نیاز نداره!
🤯
شاید بپرسید پس چطوری می‌فهمه تا کجای فایل رو آپلود کرده؟ ربات خیلی هوشمندانه تمام اطلاعات (مثل آفست بایت‌های آپلودشده) رو توی خود متن پیام‌ها و دکمه‌های شیشه‌ای تلگرام (مقدار
callback_data
) ذخیره می‌کنه و از خود تلگرام به عنوان دیتابیسش استفاده می‌کنه!
🔹
قابلیت‌های اصلی:
*   تقسیم خودکار فایل‌ها به پارت‌های ۴۸ مگابایتی (برای رد کردن محدودیت ۵۰ مگابایتی آپلود ربات‌های تلگرام).
*   امکان ادامه فرآیند آپلود در صورت خطا یا قطعی (کافیه دوباره روی دکمه همون پارت کلیک کنید تا فقط همون تیکه دوباره دانلود و آپلود بشه).
*   بدون نیاز به سرور یا هاست (قابل اجرای کاملاً رایگان روی کلادفلر ورکرز).
*   اعتبارسنجی خودکار لینک و حجم فایل در هر بار کلیک کاربر.
سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOPc-YuZtAa6pX7dYdIeS1QQJsIMeGF4BSCXpiBtOI3cryHue_G22Tze7MoXcQ8yTtWlxf6WzLIWCfV7jEU_N76eHOHGU3VCPbskg8Zz4ysYM3kKS1Mz07vt00hmDfAup6pxtePlmHYSX-nh-mHz2cHYe2CygMsYm5n0Ia295OkZTUhIZI-vNbQL_Bwd9ygJhUPq3G92oPJGYo6ww2iO8uQTVy18qzWn_8gCCvzDKHi0CVwXnT8VrO24eJqsryA9_lCbMaIvyPLs1zdjJF78k4pR4qySjjQxwhkF4TXKwB_DL_t7nfFhmsk9ZR9YbCVr7YgdoSvCF4Upu8WsZ7PbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2L9eCfSJrdqxHm0miUZdkJn6HvcmkAp3nTc3DKl3DNgLlrC5jGO5MPpzB2rzo60ISWKk8z775xH-uAXVR3O4GvqT-jVjFjMW5AfvIVT7Etb2XKA7eqUwpzak1YdlML_s_BwhRgg_AqGdYpDzuR01UA5L8Hi4qXrj7Ac3e_8z0FJRjcJ0OFk8dbw-9mA1lGRmZRtsOVkZXsAwJrLZCFK9BF729ibNPQqDrMEsYaDvC1cyId-bxrA-kwhNQWIR4pfVIf4mP6tYIuc01bpBnlelRYiljT7b6FCl82pipE5BgqhateGi7B5FOUJvr2u9LEzro9BzzPxcUXqwniHe7jwqp_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=rHLgGLlySC4yLitt1NlvnNOWtYGisFAVI1EpJLpZDLeHoQuU_ZshTWqL0IxdbR8H47iASt9oPJ66HgvGxHUN4Fwl-XTNZlATzTVl4CwytuLAq0ukofYWcNKlJ_nFEp3q9NBXPYpxGgSQ7BosWXWSoFmfbL8hQ16XGUewUaAhamuWpa_RYWSzWQBXtMlpdJ55FyBChx62dkwt_Og-8Wc5nTX45JRy15X4Chj_qm2ykSJaoqdHxc0aHUIrQytTH-18XJ2IzbwLmey5a9P6cZ65Al-u-fJejFTcNMfaRtN6ag64hr2Rk-tcbxrdWlowfMXhuOGKLhnYKH5y8zuW_iyG2L9eCfSJrdqxHm0miUZdkJn6HvcmkAp3nTc3DKl3DNgLlrC5jGO5MPpzB2rzo60ISWKk8z775xH-uAXVR3O4GvqT-jVjFjMW5AfvIVT7Etb2XKA7eqUwpzak1YdlML_s_BwhRgg_AqGdYpDzuR01UA5L8Hi4qXrj7Ac3e_8z0FJRjcJ0OFk8dbw-9mA1lGRmZRtsOVkZXsAwJrLZCFK9BF729ibNPQqDrMEsYaDvC1cyId-bxrA-kwhNQWIR4pfVIf4mP6tYIuc01bpBnlelRYiljT7b6FCl82pipE5BgqhateGi7B5FOUJvr2u9LEzro9BzzPxcUXqwniHe7jwqp_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window $🪟.npvt</div>
  <div class="tg-doc-extra">3.6 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7367" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرعتش از اون یکی کمتره اما بستگی به موقعیت مکانیتون داره از بخش configs پینگ نگیرید.
🇰🇿
-
🇫🇷
-
🇩🇪
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">window🪟.npvt</div>
  <div class="tg-doc-extra">4 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر vpn ای که داشتید یکم ضعیف شده و الان به زور وصل شدید
این سرور موقتی میتونید استفاده بکنید تا استیبل شدن سرورای خودتون
pass :
@ArchiveTell
⚡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HscLYXnSnFN_7bdtYxy3wcuiV9idvPg1EH8003Q5ejLlWEgQgTdabwfWmcsMme5fg7P6UzNzKrsAuY5A93SGRJKlvvh9erH_-EiX6opY-3t6W2LmbEmW-_XdXWXZiOVg2Ohny5e6DqcrmcN6BymhHEDeKxDaaBBEyUPsLXqHN1fXa1Tlgtm5XxPSi0qcsrFS95gGfHb4l0fhjCIQ3z2Q_9g7_dR2b4KGyizcJwn_KAZHeAzUr3ZcYG-f1za2Wdw7FI8jX_QGCXMFEvMMbd4MfhelUM7ER8GLwir3S5nDQrrIhXAJt1xsW3jw9PjZPu_wRtn1mWA1I3ebZddq1O4Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
فرار از زندان برای ‌Gemini 3.5 Flash Lite⁩
🔓
‏
⚠️
نکته:
حتماً با جیمیل فیک تست کنید، خطر مسدود شدن اکانت وجود داره.
‏
برای دریافت پرامپت کلیک کنید
✅
🔗
لینک گفتگو جیلبریک شده
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rk5gTVBAvWabWah__F7WMsAMm3kBx9FaZ3cHwNsh6xEWp8Q5JRZpCMAcKOFB0qY8TvxBi71XHS1CuzRYFfpE0WE3RV3gsw9SPmEMdfoYARhB4ivms0PG7qyBuogvDmBAh083PHoplfN7gyhZSryPSZkfrD_31daJAXrgnh4GAEJvPgviplOmfLGvdQxNOZBdtrktXKD0hVbnAvuSgMKFtogdtOIw8d5ZL6z0mLCrp9F2lRq-bADJ93BEmk5cwSYQjQGcz_0ADVvppH2ZjgxS2uTL1SwKZoFnkXHpD_4X4JJIGJCW1c5lgIXKwvkqImbHCY5aLC_AY-ZzERPoRrgqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتیوبِ بدون تبلیغ و ردیابی با Invidious
📺
🚀
اگه دنبال یه جایگزین خفن و سبک برای یوتیوب هستید که نه تبلیغات رو اعصاب داشته باشه و نه گوگل بتونه رفتارتون رو ردیابی کنه،
Invidious
خوراکتونه!
🔹
پخش ویدیو تو پس‌زمینه (حالت فقط صدا)، امکان سابسکرایب کانال‌ها بدون نیاز به اکانت جیمیل، و محیط فوق‌العاده سبک.
✅
اصلاً نیازی به نصب اپلیکیشن نداره! فقط کافیه برید تو سایت
invidious.io
و یکی از سرورهای عمومی رو انتخاب کنید تا مستقیم به دیتابیس یوتیوب وصل بشید.
📌
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukPWszrUy7tjTcTLF6MuzcK_QL4K6Z61rgGj5q7xbds8fVBgjW4zS0m3TVIDEEBswd8UIgCDG8oTjXKtIxb-H9eNxHkeJc65FKtDYSQ0k_8oNnRtmRqLXA0i_cTDtfmo2nevp_ft7KNz1InELGsBlc11HVZnVvcOdnReTRsDDgrwPxAq_GTlDcxu5ZIj1ncMkeGxB6T8dGcsquGWnLoSXFvsVaI1XhQkyb63s3NCezEU76cEYpvTtNJtayXBkS2hi1JCqoHOpTCmtrUbwpocaTAYyuwxDoLLO7qeYpYtzFifWff3jwiWfTLOCDbLdYRqEGLrO8zZapFyanaLbXS9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها: •
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه •
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان •
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب •
📝
فقط پرامپت بنویسید…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-d1ZoAlJXAiJfF_jvsDLUKNkp2Nm8HobjNR6LSwwxB7MjjxAr6zxlDhlTm1aVSMdphaYk_Xq_H-Qs-uIKxTzpkn7zimgL_OxZduCx2zD2Jg_NVP-tfAB1W9kV6v-JvadBw1wfuf3bDsWSObH3ynokM7t6tM9w_pqTK3Z2fUCrNQRitlgEaCVz1ddpOcuKQP-XkjDxjUYK1tfBCkBRXjG3VyP_73TPXW4gE6fPF3lNtjR2j3nqnmdEcp9f6n23YceIHk2SRNg6slB_X_HqwnduejaXOWfEUKGmynF5rBdXahJWWLSxyJoLLjUpIMpgE0t4NAbncFyuC7Qc0vHhvKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrewfb68ST9ZZAU05EYMB-XOBMUZRI-pL_lHo2DdW5w9Y3JVVrFOUTLM3VX9eUO8P95Rl_SvNu22i-j1SE1h7249MTINa8Tim4ynKvRena4Pr8CBhLLsZAIUA07VAH21-WvgTeOCgOG3XhHjT_PVG2swNAT8cueI4wJlmN6f4Y0P1WYzKumhQcMEWY5ln1clO88dty-X3wtmJ5sKOvYnQOM6vR9V1ZaoxfvrZcIQlSCM3TUjIabKeFzMP7tAHBUwXdfq3fPWHIts-jU6e9cheKtoQzmlblkEEhpzG9Q2By-zBpNkgXcwM46G_CwGKxq2naiy2-n44gx1IQKCBS6j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
فرصت طلایی: ساخت ویدیو با هوش مصنوعی گوگل
🔥
‏گوگل تا تاریخ ۱۴ مرداد ۱۴۰۵، امکان ساخت ۱۰ ویدیو با کیفیت بالا رو برای همه فراهم کرده
🎥
‏
✨
ویژگی‌های کلیدی:
‏
🔹
تولید هوشمند:
تبدیل متن به ویدیو در چند ثانیه.
‏
🔹
ویرایش منعطف:
امکان تغییر و اصلاح ویدیوهای ساخته‌شده.
‏
🔹
قابلیت ‌Remix⁩:
بازسازی و تغییر سبک ویدیوهای موجود.
‏
🔹
رابط کاربری ساده:
دسترسی راحت از طریق منوی ‌Tools⁩ در ‌Gemini⁩.
‏
⏳
زمان محدود:
فقط تا ۴ آگوست ۲۰۲۶ (۱۴ مرداد) فرصت دارید از این قابلیت استفاده کنید.
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igncc0wx7irBrXurQuN6Q1hjNyPRuZDKCfDvLoxibsxKB03URzXErj4P0BETTWiDVKhzkIlUakoFjPCxdHV3Lnnf25iMM7Cek2aN6vIYyvB8ieyrAdkXqec0a_VH8FjnLNhWBhWA0O8izI7OSlTJ8jZasYQIKOAeuNk5Yn4IkiI65-EihsX2m6TarIg9n2FjmQgnZFKul7XQB_KtaiWoJkodYxKvskT3q9PLqqCaWEOfJsL55Gm-0kCxRtRbMnAJXlJ4iN1a3YkIwoO_OP1JK9myKmQGVd3oaE41gJDPRKSIuC6ebdOMChQAQDvD_smAos02LukbimXYn6Fpogz58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API مدل Deepseek 4 flash 0731 به صورت رایگان
🚀
وارد این
سایت
بشید و یک حساب بسازید سپس به این
بخش
بروید و یک کلید بسازید
✨
محدودیت:
هر ۵ ساعت ۵۰۰ ریکوئست
‼️
قابل استفاده در
Vega Agent
☑️
Base url:
https://api.p0.systems/api/agents/v1
Model:
deepseek-v4-flash-073
1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkJIk2uK-gGxIdlY-S49NksV_CPFPcVdkoSX6TXryE20ODpCDtR7QeZp4NjiggUah7geIC9BlCUzRp6p71ApJFfC2JADN1-PArM3Dt4-G263o8DFFZJGLmGCIvuBtNjn1zjSxkNCkvGyp9wCSPLXe4hLDgqBMnyRTGAKIIRwIjRD36Vh-GIKvzL5ezWFtqEg3F8HifsPs6syolW5gmGDOPvJtjh_nLHKw8NU7rccsypnSf7_09uWlkMZzgNISx7_vpcr39-Gwl7PTsJMkQ_Lm2fHzv0ADliJQP60rh1-eKXqqpuH8AZIo7WYW8mBNgmwcw4JRiAEn81A0q_ZLaLQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر خودکار و مداوم IP در لینوکس با IP Changer
🔄
🛡️
اگه برای کارهایی مثل تست نفوذ، دور زدن محدودیت‌ها یا وب‌اسکریپینگ (Web Scraping) نیاز دارید که آی‌پی شما به‌صورت خودکار و مداوم عوض بشه، پروژه متن‌باز
ip-changer
ابزار فوق‌العاده کاربردی و ساده‌ای برای لینوکسه.
✨
ویژگی‌های این ابزار:
🔹
تغییر خودکار آی‌پی:
تو بازه‌های زمانی که خودتون براش مشخص می‌کنید، IP سیستم رو از طریق شبکه امن Tor تغییر می‌ده (Rotate می‌کنه).
🔹
سازگاری بالا:
روی اکثر توزیع‌های معروف لینوکس (مثل کالی لینوکس، اوبونتو، آرچ، دبیان، فدورا و پاروت) به‌خوبی کار می‌کنه.
🔹
دو حالت اجرا:
می‌تونید بدون نصب و فقط با اجرای اسکریپت ازش استفاده کنید، یا اینکه با نصبش (توسط فایل setup) اون رو تبدیل به یه سرویس پس‌زمینه کنید تا همیشه فعال باشه.
⚠️
نکات مهم:
* برای اجرای این اسکریپت باید پکیج‌های
tor
،
curl
،
xxd
و
fq
روی سیستم نصب باشن.
* از اونجایی که ترافیک از شبکه Tor عبور می‌کنه، ممکنه سرعت اینترنت کمی افت کنه و بعضی سایت‌ها آی‌پی‌های خروجی تور رو مسدود کرده باشن.
📌
لینک مخزن گیت‌هاب و آموزش نصب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nogGq1InpRmECa1kCxI5xNNBoMeUh9MqTNUFXZwb2ICd0qwPVfAuitIQ9pFMQ1nIVnmOjJ13S-Nn4JLP6onLsV_NAtvG5rSlJkd_xJ_YTGUm19tSxH7U9L3D6yivdufRnQU0FUIf9580BEWcupbIDiBP6I3OlhlQjKAC6nN-AnFX_6NIgU85MSHZAG8LvRrSleSepcnXs5r0hkFVUe25vv0gOjK1FDSgQYoEC6bpAvs80iPvSfOZQSzxsJOINGhVmqT5uxbn19S4PKS3FHoQ9U7yxuUjUWR6vN3bkLUm9lZjCneHqSiVCoZx64tGAslZBdaLQ-09LquzaL5sU5lcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Deepseek 4 flash تا 12 آگوست رایگان شد
🚀
میتوانید کلید مدل رو از این
سایت
دریافت کنید تا
12
آگوست بدونه هیچ محدودیتی قابل استفاده هست
⚡️
قابل استفاده در
Vega Agent
☑️
Base url:
https://model.inferx.net/endpoints/v1
Model :
deepseek-v4-flash
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh8vttQm5fR0WC74cARKvrNWSeKaO9q1haBu7w7xHHK4lQFwMbUBxd-DUvFlEgmjx0QAEQTHrOHoNxUvtjqjNUJex6b165kLgaHidadNQs1ycn9YEZUS2g32ZFYLs5WUoOyLSg4KyVF1yZg7L8mOUXgmWF7RL7R6L43bVNhpnImhlgocrAu4Kux32-nZ8ML49kOAyH5IEZ-n5o4RT49W8YG7E3MD-DxL8XPS2CwH-mApe213B71v5KJrLlQL90IjPc2QlI-8DQOtqArJ5tgFgvtJ1wlODHjHkk3ctEbAWTghZyQoGvGsqPDrJqi8GODibci1bdptc5eFG33f63OfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان
Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید و سپس لینک ربات تلگرامی ایی که میده رو استارت بزنید برای وریفای
✅
5
دلار اعتبار برای مدل های پولی
☑️
قابل استفاده در
Vega Agent
☑️
روزانه
5
میلیون توکن رایگان
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ArchiveTel
pinned «
بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا Vega Agent رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7350" target="_blank">📅 14:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7349">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj97buUB23-8OB-M6KCPalyUG9Inr9umH0GZfIZyXL-f_317sXf9DavXBsurqKepBSZzjxbr3HyeuTNdpq7t4QJB1kovbs4ImFcF5NJO609tL_WQhu7nm2PUT7ZDzkgF15vcyNv3j42Ba9hQWPX4Y2bol47Tezhe4z1dMxp-4i5H2bePDxi60z5muOW46GL_bOc4wjdMPrGOMQjFEK5Llp-5LPosetrw5NJegqZYDJKd0Fsrl7_FVW1m7hjQ_VD0VkI22xufwo2RAvJ97rjDXpx6RIqV9IXpNPp_zzY2vsfCZCWgaQGxzhyWm06VMi602k3Ao_iicHoWG_eE_7BnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnAGPsWU3v7rAHLm9GMvDrnugMAlwLiuCy6EDdP7e83m0BozGaFwm9O_Nf87_WKV7IJLjhJFUr0XpE9x4by9zUgL1iOCGkzHQiY3uA14dAQVy9fCQixNILozmA2MxOJsY0qurm89QX1ckotqO1mshZfCXv37UF2NSF1xHKU9SRzlDmHi_0_FVcMjyp-DD1gskdxyWyviDOO6nuqTv8Dhh1Boo7KkZudJEQbysq-qW7s2aSI_-mnGOICyXd0bmt2Sf8vTp4s2HTTBICLfGHtO27kgw9O5Pzw6u2rh3PqVMFA8_lS7fkB8M-0GzKNhY_hL89Sau8Ny6SVJSUTMK5ZPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این
لینک
وارد شید
✅
قابل استفاده در
Vega Agent
☑️
روزانه بین
5
تا
50
دلار اعتبار هدیه
☑️
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
50 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPGK93LrNcSM2nPGIs9zP1qr8rqCMxCJK0eZunsLhDdtSEce8M_2vBm7YKIeN_BmK3Ooqt1MGdyvNXoCQcyv1BtiFWK5PFtycu45TMHA8bvQDBTMDfwIOe18w6fmckR9c9n2zHq87EbSL4u3i7vCS5ywetIsPvOHFVqeuvfuKVJYfC8954vSCxhuuTsgr38pt16BxfKJhw2CiPUsNp9eIolVmXCeupbvrdZ5Uo2IhRNo3-am1CYLVoMju7kTDbtwiEga-F_IWjNU_AV916Yn50-2GBN-ZH9K8UX-Wc9nqcgU9vDmsm5anTYGry5u4X12ZN8M8XpBn8HbVDyeCMS12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Au9d6_dstHzMAXrZsslXXtw_cqrDgEAiKQn_NZr_njllKqnaxcNHip1CIZCksGjFiup_8MP2xC2VRc4aMiadLcCBktVdac4zJBqzeUaOGV1tsXLdpaSY0aJOP4wwE06GqvCy8uPIROLV4awKyqoAY0TBq4s6BfKnEyPGYGyUFS-zKkICg1KqshqViDY644v-DwBuGpCVF_Q2LYU4O74vaj0WHAqWFsMOaK3wWbe9itlvHcHXFQJyfiZYYW5vLeGU3FTgZITUehrucPIyKWQF_Tc5Ciq5I3ZZm-K7IQSrDt5VoYV7tRD0KqaPYay8GuTGQkurokjvvkvY7e6Jp0IaDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2O7eQJdga1eVl0MqCc-wbP6_wQiWH2EAh2JPHrzlT4kq6NrBtTcbSz8VzzY0LG0uXmVpB70y62PnIVT5UQ2Mh4_GBtzojQFnkuZk5SzMs-FKOq8bO6NJNoLa0sxZqrtxQ8AdTDuSjDdcl86oECyf6C5jdXCkbVLZo-R0uQ6Sk_GHpPM0o6f3jroQ40n3k3_b8kRsQ2v8P6rOaF2OQIXLVRpeKkGUV0enx6cicxLhHDYF83AASbpPprpYMfXgWOT4NTBEhgOsuWWGMLeOMMPE_XV_6zlM3H77p0F6Clc7zn9XTpx9SehiR_hHxq_EwjxoEuOqXK6Fx7AuZ-cuMxIQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4xxRzToWwquqiPL3Bj5LYFOELTiN7hWvki9MzxJgwA8Z2TG4VagF9VhLwtlaMomzYCDKBVZlxdW_9QcdtYqfT6DnWUcPXdUTk95uB8oDCbbf5a9GaJkXNrQeD8yty4TCSTBF9uO22xxVcaPnrdk9tHMNvaifckaTXQvn18ni1l9cKdU4QBpBa08x3xRAROZ9Ga86XUB5KFAvVT2_pwF8fq8L9AuEbEy-nkkVLYT_Asm5HdZi6BIqLSrRUmmVDu9ERlTg-9MpxR_2WldnKLlbnS8orZC_SnzWktjwYo0VYPpDkEttvc5wLv1yXAXFPqOruzEk_6vjAUFHQ7HZGtoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyLHRZRq3P_IsLKlWK2Fd8tXDYYCCfI01WEpm_yXydyDkFe4q5nlLFH5Tn5EvxAGjzsr1cyUPcWQPmKq3oSgfPAp0hd9VrRnRUWiy6r2sWcvwZBiOKxkL6x8zG53xpwHJ-aLzOfYep-tsUIt-tKP4Wg8-neopz-PHgoaTe-vNkUpmDg0KGASqGKXhdRAykZM0BPg5RtpRUsABXGqwT6BV2J2XgOjSgu8JGoQkn9if7g80V1BIqRDfh-o8ajshHO35m7MsVPriZ8kXC9USvlPpBmjnF20xkqxocEPNMzn4iXiX67P0Y1zbo_xdd08T1TYN4GcZYK7CAflzh32O-axlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ch6obs5Y7wgAvYuhK5fUy_lXosliI9DW197HT3uN5VYnJaD6HK_63P6ls-RFQpMJ8OiLBRazunlnF99gSOMzoHMv5dbuTYKILUdD3D9lGdnqPhmplRQvSg1TKQsrxB7RO87DXqqJtnmuK3ifFf49y3sxDUqYg49MiqhRHMFFA_fDolHEfvOqpu8t7tGfnkL1muwThSnGGDRN2fs2BItjFpU4HZ3AWmPjqucOmlN5X-BwZKG7uExlq8ad1QTrrtUqZUANlfptTTaAZpODHXFMaq_p5gh5m-cPp6SnL1j5EbhfiUIWHR6sL08S1AcPJtlSOfoaJuDjc51qJm0_y5gQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOX5WPh3FzeyqdU02xsose3cppuSW06PQDJ-11MVxPo3W1lhwpjSU8R5fiB7AXUVmwzqnusty6eP1zTssMk8i5PMUaaS13lWMrZeW9IjBH4qlwbmr8jm0rNwkAI9JPGzj0_yhOpaCMvwJoRJSgIutE4A_Upvoqpws3TQUppzOLbdrZnc8oPm9pFCjkSa6vOqbB2wVoYcNAvBo89XlW-p2gOul2WrTw5xSH5LNHn1QKZA4keIz0OssKT_-abJ6g4socpZuK3dSnRpgIubRcZH1D3_6oq-l6Yk3R81p95GXY19Y18B2MWdzUCDhPQyaSaGf08M9oGbjdod1Fd1yZU8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gq1-bkYPDO5FmjAzZi9dZJhDaR9cAQGRnvJd7PHDGQGk4slGVFHi3pS6kaIdPJqFlfkPDGsa5RNOxydKO1zr0E7Mpc09HE4cMytpKxXzNXCM-7LAEnSm2KFRh0fv35xBCuda7YN6UD5vZ7QLgSeGj-Ozl_56bNnSQ0BTo7NJuuq8LAAtj2YB6CtbfyB5V0IivmwH4yOjmp7Ay5GcbK4_XyMAbmrE0ifQUFIn4qHP4ptcQ9E3XW_cmQi8QQ3XnjLWxYYZ_ms2WVcrHEG-H-VoHNd7poHSNghDrL16WUvIkWY3hh-jktlR_OjdBn6byOSnM4nNFYNSdBPC-RDu_IETfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">بالاخره ایجنت هوش مصنوعی خودمون رو برای اندروید ساختیم!
🤖
📱
بچه‌ها، یه مدت بود داشتیم روی یه ابزار خفن کار می‌کردیم و حالا
Vega Agent
رو به‌صورت اوپن‌سورس منتشر کردیم! این برنامه یه دستیار هوشمند و همه‌کاره است که با معماری Local-first طراحیش کردیم (یعنی هیچ سرور واسطی این وسط نیست) و مستقیماً با کلید API شخصی خودتون (BYOK) کار می‌کنه.
✨
چه کارهایی براتون انجام می‌ده؟
🔹
پشتیبانی از همه مدل‌های معروف:
از OpenAI، Claude و Gemini گرفته تا OpenRouter و حتی سرویس‌های لوکال مثل Ollama.
🔹
مدیریت مستقیم فایل‌ها:
بهش دسترسی بدید تا فایل متنی بسازه، کدها رو ویرایش کنه، PDFها رو بخونه یا فایل‌های زیپ رو استخراج کنه.
🔹
۳ حالت اجرای هوشمند:
برای اینکه کنترل کامل روی تغییرات داشته باشید، می‌تونید روی حالت‌های خودکار (Automatic)، برنامه‌ریزی (Planning) یا تأیید مرحله‌ای (Accepting) تنظیمش کنید.
🔹
مرور و جستجو در وب:
خودش تو اینترنت سرچ می‌کنه و محتوای سایت‌ها رو برای تحقیق و استخراج اطلاعات می‌خونه.
🔹
امنیت بالا:
کلیدهای API رو با الگوریتم AES-256-GCM رمزنگاری کردیم و کاملاً امن روی خود گوشی ذخیره می‌شن.
📥
فایل نصب (APK) و سورس‌کدش رو تو گیت‌هاب قرار دادم. نصب کنید، تستش کنید و اگه خوشتون اومد حتماً با دادن ستاره (
⭐
) به مخزن ازمون حمایت کنید!
📌
لینک دانلود آخرین نسخه از گیت‌هاب
@VegaEnter
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhZ6joP6o3bx-Q4W3jisLW7jawWiPH9ctBV2wI2oepdDq4AAvbyKGGIyKwy1Cj61DN468mhUnMv8AGc9WsnsATRFqWbjSIjWsoxDchQffy8BtEObIdeUO1-KbpUUW9MDXziY5QkZyAWnpsKFmU2VLO8llYnXapVKJSWLqr1IQU8GN89TR4wLWr3lomiDIMCVeNPPUQVGOu4n6yZTWnJ9vEFx_4iuproZ0KH8dtQjPoWO38ySUWNiXVGhfoc6qUJYkQSluQAF6zg1jMXVHGgz7yyxqDb8jI3-g_GK9Ili8Gd42PNTLRFD1NKysGcEUvxMdx3mLs7HuKOIJZ7aeJBoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت ویدیوهای حرفه‌ای با هوش مصنوعی، اونم رایگان!
🎬
✨
بچه‌ها با وب‌سایت
Dola
می‌تونید روزانه ۴ تا ۶ ویدیو باکیفیت رو با مدل قدرتمند
Seedance 2
تولید کنید. علاوه بر ویدیو، این سایت ابزارهای چت و ساخت عکس هم در اختیارتون می‌ذاره.
🎨
✨
ویژگی‌های کاربردی:
🔹
تولید ویدیوهای حداکثر ۱۰ ثانیه‌ای.
🔹
امکان دریافت خروجی در ابعاد و سایزهای مختلف.
🔹
کیفیت تصویر بسیار بالا به کمک مدل Seedance 2.
🔹
دارای ابزار ساخت عکس‌های خلاقانه و چت‌بات هوشمند.
🔹
سهمیه رایگان تولید ۴ الی ۶ ویدیو در هر روز.
⚠️
نکته مهم:
برای باز کردن و استفاده از این سایت، حتماً باید از VPN با
لوکیشن اروپا
استفاده کنید.
🔗
ورود به سایت Dola
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfF9maHdC5yKZxF9-TJ2OiKMjULlrUmToM7aKs6gMxUefwd5CZWgx3rCpzCHRMdaSvzg6V65KjH68kTqMF4tlCt41TUk2u6aPtJrha3DIH3WwNAlTVxj_ssbT45vaRGIqo9urtkGZe9iaYC3PA5zuW0hgrMitFm0BQLdlso7fxLEihxrztbY2vmKnX-nUrOeJsVjhcaADdljZAsYqMR3Gtq-2xK93XyByzaAsFNqYOqnIXzYsgP4ZByYGaJDQqQGJZ9wZGqoPqia_F0hiLePW0PGvyuPDECa6-Oi1i1YCApvyvqjqQ56ZxXjcLgWSWBYS31t97ql2zSmhhYkMMfNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Türkiye'deki İnternet Kesintisini Aşmak İçin Güncel Yöntemler
🇹🇷
🛡
Herkese merhaba, Türkiye'de yaşanan son ağ kısıtlamaları ve internet kesintilerini atlatmak için şu an çalışan en etkili yöntemler şunlar:
🔹
IP Spoofing (IP Yanıltma):
Şu anda IP Spoofing yöntemleri filtreleri aşmada sorunsuz çalışıyor. Xray/v2ray yapılandırmalarınızda paket parçalama veya IP yanıltma tekniklerini kullanabilirsiniz.
🔹
DNS Yöntemleri:
Bazı ağlarda özel DNS ayarları veya DNS Tünelleme (DNS Tunneling) yöntemlerinin de erişim sağlamada işe yaradığı görülüyor, mutlaka test edin.
Lütfen bu bilgiyi internete erişimi olmayan veya sorun yaşayan arkadaşlarınızla paylaşın!
✌️
#İnternetKesintisi
#Türkiye
#ErişimEngeli
#VPN
#Turkey
#InternetShutdown
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5QhX8CkiHAgMQ1KCSO4jT19qtLnQd5KuObfPaSsaJ4dA36y1HSYsSesJvCkvgQrH4QTbMk_-6mLufQ1to5ix7gUznqmuhfxT9mHtCs7Bc8JyE8gFgbv3f9HI8xgDK-N03U0JPeH0NrcfMysaS13SMD__4YCKNhxGdv2tXoti54s8yU1oV90_zkaCADN22woGQ4oT-zIFeVGWY6-4yL5hjp5TRfk12caWcxtHaWJ1zcxUQDY2QMw5CzvJaNJ6gLSch0AkaNTzHr18rWoU1dnHLwjrwbs4EtPlktz_hLtk2OkRCoJMespgYDfk2Myn4KuPfiBy3lZEUZJJG_pidpzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به هوش مصنوعی‌های فوق‌سریع و قدرتمند در یک پلتفرم!
🚀
‏با این سرویس، تمام مدل‌های برتر دنیا رو یکجا در اختیار داشته باش. همین الان شروع کن و از قابلیت‌های هوشمندش لذت ببر.
⚡️
‏
✨
ویژگی‌های کلیدی:
‏
🔹
دسترسی به مدل‌های پیشرفته (‌Opus⁩, ‌GPT⁩, ‌Gemini⁩, ‌Sonnet)⁩
‏
🔹
مجهز به سیستم ‌Agent⁩ برای انجام کارهای پیچیده
‏
🔹
۲۵ درخواست رایگان برای شروع
‏
🔹
۱۵۰۰ کریدیت اختصاصی برای استفاده از سایر امکانات
🔗
https://app.clickup.com/login
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F08AL13IEsc4slnnVeyuh8cLN60GfP4x90jyqvk5GdtQcLrkrFAK9Mbnzi6FrzWJMJ2b2rdYX2aaCPT0Xrc2JQt8nW2p6PmRGej4kcyjG9OVy-HWcBFzfg7Q1b-Fg0rDU--kwUweY17zDiSNCvcXbEzw8lK52GkxZ05vLstv2afw9giYnRo3aKuxhFJ1bZvxnQG6B9DhE-NU65H9sgknPPysn3T1cC7QEzXwyi7eaTDy96wWC_UFIrCV1UwW7imuQH9KrJFBcBPPKdTyvSYwIwvAMV23jD01cSxdp3XPsL8wmfhbCy-70nHMIxlWGGs8FZRWGHFpn0yUNQzXoHTrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/preqa88fCG58py4nydr9ddTiKfUEH5XbT8cfM99lcYLMqzPWMxeJgId5c7GgK1DeFnaWHDYJHmWUhDCErjSTN1k2MkwunrB7bZAG7n2Wzr_fOngaEsWnIivmfZ7XTsYcQjAQwuVXmdAUZR814myvzkHI89nrZHdajasuPv15UxibWnzEcLrGvpzv6ZD1FRX5ywWhHhfr1hblW4jJGfttGsUiG2fk5PUmWWydBLlI1gsmdRlzdaAkxC7vFfRg5DDybq4Tp3nJDd_5SwLne2l5-C1-4Hqgt-V-ffZe8IAERmmWuB-NbMJ4EYnuCPMuxLwbV8OpldpPKTBBzUcT9aDVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuEXW5c7EC3Nfu6ognnZEyszmS4RzMgYZMr057Ko4cf8FZmjpZGHPIvgD0MuL4GoWgCNnmLwxxyJQbxR_Qm7BJFF8gAbfmdRw9SsaiI3w9ShFzS_8Vt_ISusqXqtxbxq5lIozrqQPUjVyiJr_Me9Tk-tT2XlgNYv53__9iBAqlN-I44BKl74yqTRhwwIbGaUnfHxl7MZhIW9ZSlkA7hm-EnHFtZxMVypTego5qBPir0w0dhutZwHnl13G1UdqOjYt1spo_zUPVnsl2vO5k8rm4Ga6dQSuRHyPGuUbfV2T4gqN0p6vg-K9qLELJ6BSaEh676BxljsBVdsOETE0O5_BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG:
github.com/patterniha/v2rayNG/releases
۲. ویرایش کانفیگ (
✏️
)
۳. فیلد
Address
: یک عدد آیپی تمیز کلودفلر
۴. کادر
finalMask
:
{"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"],"delays":["0"],"maxSplit":"0"}},{"type":"fragment","settings":{"packets":"1-1","lengths":["109","1"],"delays":["1"],"maxSplit":"355"}}]}
۵. فیلد
Fingerprint
:
unsafe
۶. کادر
cipherSuites
:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
۷. ذخیره کنید
✔️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PattNG_2.2.6-P2-fdroid_universal.@ArchiveTell.apk</div>
  <div class="tg-doc-extra">68.9 MB</div>
</div>
<a href="https://t.me/ArchiveTell/7323" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه یونیورسال PattNG (نسخه v2.2.6-P2)
🚀
📱
بچه‌ها فایل APK این نسخه (Universal F-Droid) روی تمام گوشی‌ها و معماری‌ها به‌راحتی نصب می‌شه.
🔹
پست مرتبط در تلگرام:
🔗
مشاهده فایل و جزئیات بیشتر در تلگرام
💡
*دم توسعه‌دهنده‌اش گرم، واقعاً خیلی زحمت کشیده! اگه دستتون بازه، با زدن استار (Star) توی تلگرام یا گیت‌هاب ازش حمایت کنید کارهای خفن‌تر تحویلمون بده
😁
⭐
*
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e89byoXfs9K2utqEZ0IF3c0JZZ5t92Fp0VoqHi2DkM6b1SmPpFQAHVHpZknI1qGo6QeDgErkQ_Bi4RPkmbU7HRzcsCF37NjA34Fh1L4PB9XsoLLauFVKk2s0z41fAEykbr4qQD6T-B7nYRI2xvVyX5p_Nd3APBo0NxGyQFzSHCSa6mtVzjhS1tuKkxiE83QIiUYZtHS1k7eAxqw1EMGNz48olyJLAuqoKMyQAwcc3on4ddmXePM6-Xq07xeUOIulHnljoQt6hAdCURjvXGp13rNBurx010sYyYI8xdvykE8mil3LMs82-jrgY0PphdmLUkPGUuXNkG5hykJgdw4dYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش شدید قیمت API مدل‌های GPT-5.6 شرکت OpenAI
💸
📉
شرکت OpenAI هزینه‌ی استفاده از API مدل‌های سری GPT-5.6 رو به شکل چشم‌گیری کاهش داده؛ اونم به لطف بهینه‌سازی کدهای سرور توسط خود هوش مصنوعی (مدل Sol)!
🤯
✨
خلاصه تغییرات قیمت‌ها:
🔹
مدل Luna (اقتصادی):
۸۰٪ کاهش قیمت! (ورودی: ۰.۲۰ دلار / خروجی: ۱.۲۰ دلار به ازای هر میلیون توکن).
🔹
مدل Terra (متعادل):
۲۰٪ کاهش قیمت! (ورودی: ۲ دلار / خروجی: ۱۲ دلار به ازای هر میلیون توکن).
🔹
مدل Sol (پرچمدار):
قیمت ثابت موند، اما حالت جدید
Fast Mode
بهش اضافه شد (۲.۵ برابر سرعت بیشتر اما با دو برابر هزینه).
🔹
راز این ارزانی:
مدل هوشمند Sol، خودش کدهای هسته‌ی سیستم رو بازنویسی و بهینه کرده که نتیجه‌اش کاهش ۲۰ درصدی هزینه‌های سرور و افزایش ۱۵ درصدی سرعت تولید توکن بوده!
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu3N3NpdGMlkiXTsRviHMF7PtRZ0n05r_23JZ9QnweC4KwxjN5KpAM67LOTzqtXp3zfAbtXAJPp6ZnJc1cL_opgZQ8hsJ4scVRStp2G20wf7kqSAz_5A5zIiu0Ea3fmxEylxCYEX5CRhAgcUnR0tze4n8zu4VfIL8dI9MBdFU4DLD5VYbuEr7Ed-qCsuUN_1GaZmveNbBO1IQi92U9tQX5niI7tv287kOg351N6jOn3KAot0LU6pTS9V8lOXwUiAuNr3qVmhLUQo7JAEKxK3XkKiYRTF8koqLgkVBOBQe3YMMGlyv9nWiuDM_Wy7AN71F5PziO0UVa10cPZSEAG1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت ۱ ساله Pro سایت
Beautiful.ai
(رایگان)
🚀
🎨
بچه‌ها این سایت یه ابزار عالی بر پایه هوش مصنوعی برای ساخت اسلاید و ارائه‌های حرفه‌ایه؛ فقط کافیه موضوع رو بهش بدید تا خودش کارها رو انجام بده!
✨
نحوه دریافت اشتراک آموزشی (EDU):
🔹
مرحله اول:
با فیلترشکن وارد
صفحه
بشید و روی
Claim EDU Offer
کلیک کنید.
🔹
ایمیل دانشجویی:
ثبت‌نام رو با یک ایمیل
.edu
انجام بدید (می‌تونید از سایت‌های ایمیل موقت مثل
tempmail.id.vn
کمک بگیرید).
🔹
اطلاعات دانشگاه:
برای اسم و لینک سایت دانشگاه، از یه هوش مصنوعی بخواید اطلاعات فیک و رندوم بهتون بده (سایت گیر نمی‌ده و قبول می‌کنه).
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CORe69PKBYWvF7Fr1wmJz9deORpv5LFN7nXwo9kgTb8j_YsAKRqB3UbeOVudaqZj-zqm_pj-FB3cOPQRg4jIjNxVTYtNe5F0JknbKkETIewKcBGmcR7-pvshT_zguKhQ45m52HOZb_Lhja9qKgafOMfhrXp2AqUT1idOhvddXngqi9HxrLetGEiZ-jnmWgH7P2xX9CFOb9T7Slq13HqHmnq8008iwnGfXoLXRoUVc9jZhBUd5aswAXX6xC8ImZrwtVDSaRVYmLW91cN6njmZcV9jzYyoZQz9uulPAY8M5bTAkY_68Konyv6C-bS-fadWBDepN1GrnUF8a8K_s-2-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی ابزار PDFx؛ ادغام و تفکیک هوشمند فایل‌های PDF
📄
✨
پروژه متن‌باز PDFx یه راهکار خلاقانه برای مدیریت اسناده: ترکیب چندین فایل در یک فایل، اما با حفظ قابلیت جداسازی!
✨
خلاصه ویژگی‌ها:
🔹
ادغام و تفکیک:
چند PDF و عکس رو یکپارچه می‌کنه. این فایل تو برنامه‌های عادی پشت‌سرهم نمایش داده می‌شه، اما تو برنامه PDFx دوباره به اسناد مجزا تفکیک می‌شه!
🔹
کاربری آسان:
مدیریت فایل‌ها فقط با کشیدن و رها کردن (Drag & Drop).
🔹
دسترسی:
دارای نسخه وب و دسکتاپ (ویندوز، مک، لینوکس).
🔹
دستیار هوش مصنوعی:
پشتیبانی از مدل‌های OpenAI، Anthropic و گوگل (با API Key کاربر).
📌
[
لینک مخزن پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiGfQGh3yU-jRyexQl5UvsagUVv4k544R4pjdNYIRGDdMWecod3jJ14IA4zYF7kKcTcOa4QKCCVLNE8phY-HrxA8j2PrnYQbur5Y3FrbG3Xk4IuIKncnzhxhNP0VxQGf48hOzkNeBGFlI-Uvc135G0znY6lnq9NCTAQCXu_XHYygqlck7_3ZNlHPV5W3QhtyKW143sA-QKhUAgxBo-KfEcdHAA_9-rEq_Fya6P2yeVwMvI853ZdlsvWS9BccVaZ5Bk3pTaQHJF7WgZdNbierdlpKaQkZHgEXC4HAUJZ03MuQfzhISBZoXGcOjwk60cpM4zylmQ9LdhzRGkcMSw6--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید پنل 3x-ui (نسخه v3.6.0) منتشر شد!
🚀
🔥
نسخه جدید با تمرکز روی امنیت، پایداری و رابط کاربری بهتر منتشر شد.
✨
خلاصه‌ی مهم‌ترین تغییرات:
🔹
ارتقای هسته (xray-core v26.7.28):
(نکته مهم)
ساختار
finalmask
تغییر کرده؛ اگر قبلاً از این قابلیت استفاده می‌کردید باید پروفایل‌ها رو از نو بسازید.
🔹
امنیت بالاتر:
بسته شدن دسترسی آزاد به فایل
openapi.json
، امن‌تر شدن توکنِ نودها و مسدود شدن دیفالتِ آی‌پی‌های لوکال.
🔹
لینک‌های سابسکریپشن:
تشخیص خودکار نوع کلاینت (User-Agent) و قابلیت جذاب چک کردن وضعیت آنلاینِ کاربر مستقیم از لینک ساب (با اضافه کردن
format=info?
).
🔹
داشبورد مدرن‌تر:
بازطراحی کامل صفحه اول پنل با گراف‌های تمیزتر برای مشاهده زنده مصرف سرور و کانکشن‌ها.
🔹
پایداری دیتابیس:
اضافه شدن قابلیت بکاپ‌گیری زنده از دیتابیس (بدون نیاز به خاموش کردن پنل) و رفع باگ‌های ترافیک.
📌
نصب و آپدیت با همون کامند همیشگیه، اما
حتماً قبلش از دیتابیس بکاپ بگیرید!
#3x_ui
#ثنایی
#پنل
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkRlW_bVZLMZmWhY88OsJmIEPm3OrYIUONJrkfgkuuDDcNK5llyye3LRbtLQNjOj4EobG0dCkB8ScBgrdD2aWFNeB1gLfY36pBBJ7X-WfKkWShfn3V-0y1Zzuz-TDJkdi0b2odwY8zpBgY6wQ3gN_a8q8jAMAsJAA0v5LIPrdbxjF25jZLExJ2KPPKzI2mQdppQaKDksHPWLf-3arjZBIfIkUfIF2ORywHqM2g4dWEj5vmPPQpDNz22QUs3TXpFo0BBbUu99gQpykt7lTN1FEQpJyLml5RC5RgzfkhJxtgJ9imotttvY3-dsFNQBKTEPixrGQmtXGGNW07OzVCXChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک ۱ ساله ChatGPT Pro رایگان برای دانشگاهیان
🎓
🎁
بچه‌ها می‌دونم این طرح به خاطر تحریم‌ها و نیاز به کردیت‌کارت و مقطع‌تحصیلی بالا به درد خیلیامون نمی‌خوره، اما اگه دوست یا استادی خارج از کشور دارید حتماً براش بفرستید تا استفاده کنه!
🔹
مخاطب:
اساتید هیئت علمی و محققان پسادکترا (Postdoc).
🔹
شرط اصلی:
داشتن حداقل یک مقاله در ۳ سال اخیر (در سایت‌هایی مثل arXiv).
🔹
تایید هویت:
نیاز به ایمیل آکادمیک (بدون VPN) + کردیت‌کارت (بدون کسر هزینه).
🔹
مزایا:
یک سال اکانت Pro با حفظ حریم خصوصی + ۴ دعوت‌نامه رایگان برای همکاران همون دانشگاه.
📌
لینک ثبت‌نام در سایت OpenAI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StG3VZsKsFD4FJMt3u0Fyie4BtngkC9ZxT0Du0cfI0RuOW97Zf8dvUDpfc2kKoQQmNG7Zuhd-_Mf6FPjg13lyEAFCAcQggkKZMlqA6sJxy2LQK8FtIQB-iQR9csWxigLi9zGTYCRpDBunMl9GZUr0abUJb62m2oCOxAD4RXl3lPToULtBYHm_VZuBOYZKd4KSgvYIscWtSrOihe_U1xwH0s4BKy_Opo9ia8DVClio5KvbLFK2OvqxJrKcBl3_Td646yoa7kzV8fWTbkCqkc3-53_EDC0qNQA_AHMWPa3_w2y6Enkp1k6Dt0myqsdFA4FAStZTU4TyBkhxd1TMxGIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از Grok Voice Think Fast 2.0؛ شاهکار صوتی جدید ایلان ماسک
🎙
🚀
شرکت هوش مصنوعی ایلان ماسک (SpaceXAI) به تازگی از جدیدترین و هوشمندترین مدل صوتی خودش پرده‌برداری کرد. این مدل مستقیماً برای پردازش سریع «صوت به صوت» (Speech-to-Speech) طراحی شده است!
✨
نکات کلیدی:
🔹
قدرتمندترین نسخه: به گفته سازندگان، این هوشمندترین و قوی‌ترین مدل صوتی است که تا حالا توسط این شرکت توسعه داده شده.
🔹
پردازش مستقیم (Speech-to-Speech): ارتباط صوتی کاملاً بی‌درنگ، که باعث درک بهتر لحن انسان و کاهش شدید تأخیر در پاسخگویی می‌شه.
🔹
رقیب تازه‌نفس: کاربران به شدت منتظر مقایسه‌ی عملکرد و سرعت این مدل با نسخه جدید gpt-live از شرکت OpenAI هستند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تغییر ظاهر لینک سابسکریپشن 3x-ui (پنل ثنایی)
🎨
✨
پروژه
MiTemplateSub-XUI
یه کالکشن عالی از قالب‌های مدرن برای صفحه اشتراک کاربرهاست:
🔹
تنوع بالا:
بیش از ۳۰ تم مختلف (سایبرپانک، مینیمال، شیشه‌ای و...).
🔹
پشتیبانی از فارسی:
کاملاً راست‌چین (RTL) همراه با دارک/لایت مود.
🔹
جذاب و پویا:
نمایش انیمیشنی مصرف ترافیک و چیپ‌های پروتکل.
🔹
مدیریت راحت:
تغییر و نصب سریع تم‌ها فقط با یک دستور (از طریق اسکریپت اختصاصی).
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvVerV9Jb7z47z9waF4p4h14fkxb5PtTyavFwevMdNNFM96T0Nzcy35mHCiLbS59dAay3YWiHa1rZVuKDiW0z88rzXIk4S8IOIIodvdZcGLVFLetWfFstKkNXrMKNMRccGCJk4_No-5fzZMvBYipMSeanbsbf33LKpH3NeBMqCeLUNg3p3UZtLN2bjdE4atpas6ypopoq27KDr_nVgi3YRzGVXsmdUw0jHtlP1V0GgsXT2rg6_Pp-WxpKe57Fga9GeO9IiSISstPo-d7ksL4_t6RM7ZU7h7LL34WZR0cj1b0UAYc5Dgn7TZUvjFu_PIfbP8Xn4J2di0Lv329vT7HEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ابزار ‌Onlook⁩: انقلابی در طراحی و کدنویسی!
🤯
‏اگر طراح یا توسعه‌دهنده هستید، ‌Onlook⁩ دقیقاً همان چیزی است که به آن نیاز دارید. این ابزار مثل یک دستیار هوشمند، فاصله بین «طرح» و «کد» را از بین می‌برد.
🛠️
‌‏
✨
قابلیت‌های مهم:
‏
🔹
ساخت خودکار:
تولید پروتوتایپ‌های حرفه‌ای همراه با کد تمیز.
‏
🔹
تعامل دوطرفه:
امکان اکسپورت به ادیتورهای کد یا محیط ‌Figma⁩.
‏
🔹
سرعت بالا:
صرفه‌جویی چشمگیر در زمانِ طراحی و فرآیندِ درکِ کد.
‏
🔹
رایگان:
دسترسی به تمام قابلیت‌ها بدون هزینه.
📌
[
لینک پروژه در گیت‌هاب
]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu3-xbVTgPLpezgcggngBft6qc9Bqrl-pQtLT0Nb2gGLZKXK10_WjM1UkMUQRSK2KTDKOfVLmTd8DdJuXhNQDFUpq14Yjl4Nv5U31VNn99EmsielUBad6wMNj4Iw9aXTnVbDCl6wlSrJ9i7bg06C6zixt87elmD19cfjAms0xkrcEAoJg7u0imuv6TLdFERD_eifK3MKSvd1gx3n-TIIp5YxU766ErO7EGWjgx8na2ziiWGJgE4kqiD-WM23iaSqxKoLXMSYV5nypEdCwcf9vPyGONLQRcqWRTnjcwKIqNM-UJx5CsQciRMaridLZ8ga_iIadwhO7Qz5wnENLZplOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
گنجینه‌ای از هوش مصنوعی در دستان شما!
🚀
‏اگر به دنبال پروژه‌های آماده و کاربردی هوش مصنوعی هستید، این لیستِ طلایی شامل بیش از ۵۰۰ پروژه متن‌باز در گیت‌هاب، دقیقاً همان چیزی است که نیاز دارید. از چت‌بات‌های تخصصی تا ابزارهای پیشرفته‌ی ترید خودکار؛ همه چیز در دسترس شماست.
✨
‏ویژگی‌های این مجموعه:
‏
🔹
دسترسی کامل به سورس‌کد تمامی پروژه‌ها
‏
🔹
تنوع بی‌نظیر در حوزه‌های مختلف (از بیزنس تا مالی)
‏
🔹
مناسب برای یادگیری، توسعه و شخصی‌سازی
‏
🔹
پروژه‌های تست‌شده و آماده‌ی اجرا
🔗
‏
همین حالا از این مخزنِ ارزشمند استفاده کنید و سطح پروژه‌های خود را ارتقا دهید
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXRnM0H44LyhNOYuokXXlSaU9-i9wCFKvG5ELKLSPldotxq1JVC4hc5J0crW5tOgh29siILRiqo-Q4fYo_b1Fofk2fGNYUgmldF_xPmzDUMS-jQ6d85WkrcWyP0AV99kqyL-vrLlYjKUdlOtaBDeIZe3e6DxCLI-JT62jX9KRumLtTtGRZWOAJtvL0ae2Xu3R4RWr47_TnLnwtQMSjyDkYYWOk9z-gIizUPo5EIAIa4yxTwnmOxF8jJ5OikbZxWx7V_6J9jZ9tCMGo4xZ14ra9gU42B1Fj-5BmtQtLRqDnBF6fkMJr5BXZbQKYLO_xmCrT2WstV-YfYTJgv-ae5gtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDZN-vnCRbuL9_eFjyyfZbggztkFiPSRIXHSMgWUMxELpP0UxsRXoUJFAhVbCXv2CLZSGL9Nu4j4BNHVi-R3GzM1KAvZ6mpN6l3O3YDua5QVfMauitURAm3o1SoK9YXA7iQV10YgKhuqb6ZLpPzSmwx179sGakPEpOjZeXQhcpUgbyKVcfi5pla4F_Nsx5E43DV3x4anz9Rz2l3YxP1duJPJtak0wcVBbtWrbwPYN46a6aAgNcZgP8-ITkIowJYiwZ0_-rx2iOgWJ8BZTaNtUpudG7ZJz0AvSbkVJDcFEosa_vDGIao6Tx6QhPwVQVLeKl1oXphPqWhZMONDq55WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2CFpUMa-foHRA4E2R_40z3farMq_TtzWfNaWnsctxN942qz3Jw_HMrAfIoW5Ldj6BNtkdt29041hW0WkVSVSIshMJUFks7PmdDLH9Q8kzuzH_P32dQbmhTq__a3uCKVJMpJUHRspYvzjQVJ_RkM1HwHF9-4q8VXYUmq4cJV_wNQPOaJtSUZ48imhHXcO1vLunbixUs8-6BgryLXnubIZlDiMC8VTdJ2REY9MAMK1t340oXeprsMl2y4n9UOsCz2i6YgIiSRiwugn3DZLvrfR_OsBoGqRuNoQ_Unb3vesTuty3UbbJZ0s0Ok_GieiguWGDEzCIsPWD0TBlx-Eo3KRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌APK Converter⁩؛ پلی میانِ وب و اندروید!
📱
🌐
‏این ابزارِ آنلاین، پروژه‌های وب، فایل‌های ‌HTML⁩ یا بسته‌های ‌ZIP⁩ شما را مستقیماً به فایل‌های نصبی ‌APK⁩ یا ‌AAB⁩ تبدیل می‌کند.
🛠️
‏
✅
ویژگی‌های کلیدی:
‏
⚙️
تنظیماتِ اختصاصیِ اپلیکیشن و آیکون
‏
🔑
مدیریتِ حرفه‌ایِ امضای دیجیتال (‌Signing)⁩
‏
📋
نظارت بر لاگ‌های ساخت و مدیریتِ تسک‌ها
🔗
https://gentsergame.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMl0qzBaYU0J0ZGxdifWijAXxtyGXPzR3KMAIjx5J-dxmjS3hijHsKyao5nHKve4lXFrSn1mdpaqEBketgRmTtEzhZQFEwLFeA-QbEXwi0bnEeQ-5H37Xa_kMcMSv4AwVYgkAZ3RehYtQfbnzsdXfD4lOK-GWF3-NTnuXYU5hsVL5gkzjN6DeYnsbun6JbDM0aZIVOJJVqoK1Up9Om6rULrBmaE3zEKvs6ctTN2lqQOSAMKzisbsHPBiY8Fc1dX7q-6xax4pRH2nG9Z6toAVQ9x3rMM5TONk8KpcViLDZYFjijD007cbOobLLF67TamSwI3yqpvlEFAQq4zFqKFZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
انقلاب در کدنویسی با ‌JCode⁩: سریع‌تر، هوشمندتر و قدرتمندتر از همیشه!
💻
‏اگر فکر می‌کردید ‌Claude Code⁩ سریع است، ‌JCode⁩ با سرعتی ۲۴۵ برابر بیشتر، استانداردهای جدیدی را تعریف کرده است. این ابزار نه فقط یک دستیار، بلکه یک «تیمِ کامل» در سیستم شماست!
🐝
✨
‏ویژگی‌های کلیدی ‌JCode⁩:
‏
🔹
سرعتِ خیره‌کننده: ۲۴۵ برابر سریع‌تر از رقبا با بهینه‌سازی فوق‌العاده.
‏
🔹
مصرفِ ناچیز: هر سشن تنها ۲۸ مگابایت از رم شما را اشغال می‌کند.
‏
🔹
معماریِ کندویی: ایجنت‌ها با هم همکاری می‌کنند، وظایف را تقسیم کرده و کد یکدیگر را بازبینی می‌کنند.
‏
🔹
حافظهٔ هوشمند: با حافظه سراسری، هیچ خط کدی در سشن‌های مختلف فراموش نمی‌شود.
‏
🔹
سازگاریِ کامل: پشتیبانی از تمامی ‌API⁩های بزرگ (‌OpenAI⁩, ‌Claude⁩, ‌Gemini⁩, ‌GitHub⁩ و...) و مدل‌های محلی (‌Ollama)⁩.
‏
🔹
خود-اصلاح‌گر: قابلیتِ عیب‌یابی، بازنویسی و رساندنِ کد به کمال.
‏
🔹
تجسمِ پروژه: تولیدِ نمودارهای درختی برای درکِ عمیقِ ساختارِ پروژه.
‏
🔹
مهاجرتِ آسان: امکانِ وارد کردنِ سشن‌ها از ‌Cursor⁩، ‌Claude Code⁩ و غیره.
‏
🔗
دسترسی به ابزار
‏
📂
مشاهده سورس‌کد
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK2WJz7OY6DbhczJ7QhugAUafMNYAMuQdvAHgF6XL1Sv2obTo60rJ0r6PlJ-YArrjnI3-ceO9LEZLojlqDChvFV1ZgaOhlaEQZcs-cIS3rMy2xWkWKh-hBGY1KnInjV0wrdskINYg1hR_einJhb1WE3XTbRAPwNHIHGctZDv69Xf3dkPbyID1nRMeOhsJPjNc4mPBe_lqQ8Qy2zLirPs2c5Yzy5TGFxzI76esNHW2LuZVX3yWdjrKYcaujdaQubOF-6IUFcWRkKpwt2IOvlT4HJkGqy6MnPazuM3lhY3rxDTgZnIOGd8I3fIidNYe2mf2cu-Ipf9_tWd3sfDrisnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
70 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
Opus 5 | Opus 4.8 | Sonnet 5
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTwjMDEkhfP832MIgTncwElKb_NXqNJ9hoivAwLVOzbrcK82_qcLaIsOz2sP1u5DyDQXDEwUpCaNLS5-T0qPWbzoq7LGHNYFiTjNZgd-Yk1yW6uPhwxYhC6QBLtNuVq-_9GIcJROcN_p0rtgtqYU2x8ald86yPLLeeVSZQu5qL7dwyYwKnrYaXu8bDHbPtj6ayWwTRRQtpIol3yiheEzkAV-leoK_yoqZLo3bjRfCutL1nRWcfqOb1iJuXBoJGfHA_4tMIReCndH00K8TQ_OMOtSBNi32BT3IUDpNkm3904muX2nmCAfhYGgfhufikgnzNozFE2jW9gJhh4gD-npUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام جدید و عجیب علیه پاول دورف؛ حبس ابد به خاطر ربات دوست‌یابی!
⚖️
🚨
یه خبر عجیب تو رسانه‌ها و کانال‌های روسی داره دست‌به‌دست می‌شه! ادعا شده کمیته تحقیقات روسیه (СК) پاول دورف رو به خاطر عدم حذف ربات معروف «Daivinik / Leo» (یک ربات دوست‌یابی تلگرامی با بیش از ۱۳ میلیون کاربر) متهم کرده و شایعه شده ممکنه سر همین ماجرا با مجازات سنگین یا حتی حبس ابد روبه‌رو بشه!
🤯
✨
ماجرا از چه قراره؟
طبق ادعای بازپرس‌های روس، سرویس‌های اطلاعاتی اوکراین با ساختن اکانت‌ها و پروفایل‌های فیکِ دخترانه تو این ربات، در حال فریب دادن و جذب نوجوانان و جوانان برای انجام فعالیت‌های تروریستی و خرابکارانه هستن.
اتهام اصلی دورف اینه که چرا با وجود این مسائل و هشدارها، این ربات رو از روی سرورهای تلگرام مسدود و حذف نکرده است.
با این وضعیت و اتهامات امنیتی به این سنگینی، به نظر می‌رسه فشارها روی تلگرام دوباره بالا گرفته و فعلاً نباید منتظر کوتاه اومدن دولت‌ها در برابر پاول دورف باشیم.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dockerfile</div>
  <div class="tg-doc-extra">35 B</div>
</div>
<a href="https://t.me/ArchiveTell/7299" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!)  با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز: فایل Dockerfile ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱:…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📌
آموزش ساخت پنل ثنایی بدون خرید سرور (کاملا رایگان!
)
با این آموزش می‌تونید بدون نیاز به خرید سرور (VPS) و دامنه‌ی شخصی، فیلترشکن فوق‌العاده سریع و اختصاصی خودتون رو بالا بیارید.
📂
پیشنیاز:
فایل
Dockerfile
ضمیمه‌شده به همین پست رو دانلود کنید.
🔹
مرحله ۱: آپلود فایل تو گیت‌هاب
۱. وارد سایت
GitHub
بشید و یک مخزن (Repository) جدید بسازید.
۲. اسم مخزن رو
railway-3xui
بذارید و تیک
Add a README file
رو حتماً بزنید و دکمه
Create repository
رو بزنید.
۳. تو صفحه مخزن، دکمه
Add file
➔
Upload files
رو بزنید.
۴. فایل
Dockerfile
(همین فایلی که پست کردم) رو بکشید و آپلود کنید و در نهایت دکمه
Commit changes
رو بزنید.
🔹
مرحله ۲: نصب روی Railway
۱. وارد
Railway.app
بشید (با اکانت گیت‌هاب لاگین کنید).
۲. روی
New Project
➔
Deploy from GitHub repo
کلیک کنید و مخزن
railway-3xui
رو انتخاب کنید.
🔹
مرحله ۳: حفظ اطلاعات پنل (Volume)
(اگه این مرحله رو نرید، با ری‌استارت سرور، اطلاعات اکانت‌ها پاک میشه)
۱. تو صفحه اصلی پروژه تو ریلوی، دکمه‌های
Ctrl + K
(تو گوشی روی آیکون همبرگر) رو بزنید.
۲. عبارت
Create Volume
رو سرچ و انتخاب کنید و به سرویس متصلش کنید.
۳. در کادر
Mount Path
دقیقاً این عبارت رو وارد کنید:
/etc/x-ui/
🔹
مرحله ۴: تنظیم پورت و شبکه
الف) آدرس ورود به پنل:
۱. روی سرویستون کلیک کنید ➔ برید تب
Variables
➔ دکمه
New Variable
رو بزنید.
۲. کادر بالا
PORT
و کادر پایین
2053
رو بنویسید و Add کنید.
۳. برید تب
Settings
➔ بخش
Public Networking
➔ روی
Generate Domain
بزنید. (این آدرس پنل شماست).
ب) مسیر ترافیک فیلترشکن:
۱. تو همون تب
Settings
بیاید پایین‌تر به بخش
TCP Proxies
.
۲. روی
Add TCP Proxy
بزنید و پورت
8080
رو بدید.
۳. یک آدرس TCP (مثل archivetell
.proxy.rlwy.net
) و یک پورت ۵ رقمی (مثل
14841
) بهتون میده؛
یادداشتشون کنید.
🔹
مرحله ۵: ساخت کانفیگ تو پنل 3x-ui
۱. لینک آدرس پنل (مرحله ۴ الف) رو تو مرورگر باز کنید.
۲. با نام‌کاربری
admin
و رمز
admin
وارد بشید.
(بعداً از Panel Settings رمزش رو عوض کنید)
.
۳. برید بخش
Inbounds
➔ دکمه
Add Inbound
رو بزنید و این مقادیر رو ست کنید:
@ArchiveTell
Protocol:
vless
|
Port:
8080
Network:
xhttp
|
Path:
/assets
|
xPaddingBytes:
5-70
Security:
reality
|
Target :
www.samsung.com:443
|
SNI:
www.samsung.com
دکمه
Get New Keys
رو بزنید تا کلیدها ساخته بشن و در نهایت
Add
کنید.
🔹
مرحله ۶: اصلاح و آماده‌سازی لینک نهایی
۱. تو پنل روی
QR Code
کانفیگ کلیک کرده و لینک
vless://
رو کپی کنید.
۲. لینک رو تو نوت‌پد گوشی یا سیستم کپی کنید و این دو قسمت رو جایگزین کنید:
آدرس بعد از
@
➔ آدرس TCP ریلوی (مثلاًarchivetell
.proxy.rlwy.net
)
پورت
:8080
➔ پورت ۵ رقمی ریلوی (مثلاً
:14841
)
تمومه! لینک اصلاح‌شده رو تو نرم‌افزارهای V2Ray بزارین و متصل بشید.
🚀
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvnH67rS2ZERcHElOurAxQAb-s7C7Sm_UTT3_Tq6oK5x1rWB-CQfg_ZYv-i0CK6zmFDwFkK8ouMgYZqa2xAH-TR72dy_qKnp0VDCy97m_RNe9pgk9Y74y9U7h4u0hOT3LwELtI9qUPrKyVpWhv3oQ18WbB9c6wMlfZkNGmOCQ9Nkz6NBTigBB2y3mpJ9aVwGy6Cx4MDIt2qEfEPM1dAEzKQRpPZaLQP38_qq9vt-0TNvW8N67n8-AB1qDbjk5Mv7klFryg3Uenn7vWadxItOhoWugwA0ua2yKBKH7ZzC_CFFyxIGhxhnLkUt27sqzwehaDnQiqXK0jUtfFmLILgJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
تبدیل گوشی Android به وب‌کم با VCamdroid
‏
‏با
VCamdroid
می‌توانید دوربین گوشی Android را از طریق USB یا Wi-Fi به وب‌کم مجازی Windows تبدیل کنید؛ مناسب تماس تصویری، استریم و استفاده‌ی دوباره از گوشی‌های قدیمی.
🚀
‏
‏
✨
قابلیت‌های مهم:
‌‏
🔹
اتصال خودکار از طریق USB و ADB
‏
🔹
اتصال بی‌سیم با Wi-Fi و اسکن QR Code
‏
🔹
سازگار با Zoom، OBS، Discord و Teams
‏
🔹
اتصال هم‌زمان چند گوشی و جابه‌جایی سریع بین دوربین‌ها
‏
🔹
کنترل دوربین جلو و عقب، وضوح تصویر، فلش و تنظیمات رنگ
‏
🔹
پشتیبانی از Windows 10/11 و Android 7.0 به بالا
‏
‏
⚠️
نکته‌ی مهم:
‏
‏برای اتصال USB باید
USB Debugging
فعال باشد. عملکرد برنامه نیز ممکن است بسته به مدل گوشی، کابل و سخت‌افزار دستگاه متفاوت باشد.
‏
‏
📌
دانلود و مشاهده در گیت‌هاب رسمی پروژه
‏
‎
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7296" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te5hxFQS2Wr4YlFXjapGS0cRIphCvZghWAOkNMbZzgrnq_4aeB6CXJSzkn_-oNbM68WvIvGoEUTwwMkFvCRCwp9rnzU5fTQ_6PHRnppktq9yvihFhUvyVf73-OGYn-auMi0N8gy9SLjj2Jcd86BRNcBAbxnZPaWhLtSOoC05Dao1noTFJNLse1FdD_odwfEVloCOU9WfMhRdYh4oGE9j8_vKkRoezDyQjMVUaJhyalSh-xLaGWq76S7cGiER1jxjicaPr92G0PwVuhhuWZ70iHqfKd4XbG6cL9Od7WWwHzUuwyhJ0EHIbmriWAkLEz4BiQJZNDN7NNI9hN5DNpbUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
Shotcut؛ ویرایشگر رایگان و متن‌باز ویدئو برای کامپیوتر
‏
‏
Shotcut
یک نرم‌افزار حرفه‌ای و کاملاً رایگان برای تدوین ویدئو است که روی Windows، macOS و Linux اجرا می‌شود و از طیف گسترده‌ای از فرمت‌ها پشتیبانی می‌کند. نسخه‌ی جدید
26.6
نیز با تمرکز بر قابلیت‌های HDR منتشر شده است.
🚀
‏
‏
✨
قابلیت‌های مهم:
‏
‏
🔹
پشتیبانی از ویدئوهای 4K و 8K، HDR10 و HLG
‏
🔹
ویرایش مستقیم فایل‌ها بدون نیاز به Import یا تبدیل اولیه
‏
🔹
تایم‌لاین چندلایه با پشتیبانی از رزولوشن و نرخ فریم متفاوت
‏
🔹
ضبط صفحه‌نمایش، وب‌کم، میکروفون و استریم‌های شبکه
‏
🔹
ابزارهای اصلاح رنگ، Chroma Key، Motion Tracking و Stabilization
‏
🔹
پشتیبانی از زیرنویس، تبدیل گفتار به متن و Text-to-Speech
‏
🔹
قابلیت Proxy Editing برای تدوین روان‌تر روی سیستم‌های ضعیف
‏
🔹
نسخه‌ی Portable و بدون نیاز به نصب
‏
‏
⚡️
نکته‌ی مهم:
‏
‏Shotcut بدون تبلیغات، اشتراک ماهانه یا محدودیت خروجی ارائه می‌شود و به لطف FFmpeg از صدها فرمت صوتی و تصویری پشتیبانی می‌کند.
‏
‏
📌
دانلود از وب‌سایت رسمی Shotcut
‏
‎
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag-_W2LIWjxkowU8Nq9kvftPcP4nRO4gFs78tqOsq4BchfyGAouCjtE5usAq5NZETUjFSQoeEqBhnRuOXl5tolVugUakaOFg49n323phuBSpuUTcVwYCRfZSZxbNjfvDUR7Qv0DOqmq6gOkLLoBYnq0jo7a1sMsi1QE78nnE_84rApp8UKJW1h9QosIFNQM3p1A6cm0lq1UqlndvoX-S0YFc4s6SEY4uSbhzuaU3mgXt5WdbnzGPNLmuxLc_I2HCB6AkhubVDdijgQ_91-46FS-kHqon9qR5S3BB9coIScPcO5o1y-DgVN6RdRrcqc1Fri8ljCrL24TI7zfdLYrbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏‌CocoLoop⁩؛ هابِ هوشمند و امن برای کشف و نصب اسکیل های ‌AI⁩.
🚀
‏
✨
ویژگی‌های کلیدی:
‏
🔍
جستجوی سریع و دقیقِ مهارت‌های ‌Agent⁩
‏
🛡️
بررسی امنیتِ ابزارها قبل از استفاده
‏
👥
جامعه‌ی فعالِ توسعه‌دهندگان و کاربران
‏
🔥
دسترسی به ترندترین و کاربردی‌ترین قابلیت‌ها
🔗
http://hub.cocoloop.cn
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=hPJ_aeGCw2Tovw1McKJxRH5_t6CnothEF5CWmuGwrCZrT33ephliBgvLNe9nObKA9vcWPXvkqFX1m2XTmpHz1njOj_9ZhUzNxqmQnLu__AluHlCvzirlrgwA5M-zdP50meq41w_hAcq0qmHqjXt_49pkH_OfgboteGvbhC86HS1aquBnoHLBZOgJ7xWnrvBzp4HDWjegFrDY_xaQiLkS8Gj-YrlAFyRsnUzdaGrVBe86pSx2-jp6oWSIg_xLJ1k53XZLyJShGiNj0nNQkXsDB1TcIiXsVTVs9jgNLS9WeX5o4Fo0CZvPd2pWr2-o7WhZ_HMcXGk2lGZ2YYVC78ytdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=hPJ_aeGCw2Tovw1McKJxRH5_t6CnothEF5CWmuGwrCZrT33ephliBgvLNe9nObKA9vcWPXvkqFX1m2XTmpHz1njOj_9ZhUzNxqmQnLu__AluHlCvzirlrgwA5M-zdP50meq41w_hAcq0qmHqjXt_49pkH_OfgboteGvbhC86HS1aquBnoHLBZOgJ7xWnrvBzp4HDWjegFrDY_xaQiLkS8Gj-YrlAFyRsnUzdaGrVBe86pSx2-jp6oWSIg_xLJ1k53XZLyJShGiNj0nNQkXsDB1TcIiXsVTVs9jgNLS9WeX5o4Fo0CZvPd2pWr2-o7WhZ_HMcXGk2lGZ2YYVC78ytdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ابزار ‌PromptCard⁩؛ کلیدِ رمزگشایی از دنیای تصاویر!
🔑
🎨
‏با این افزونه‌ی کروم، هر عکسی که می‌بینید تبدیل به یک پرامپت مهندسی‌شده می‌شه تا بتونید دقیقاً همون سبک رو در هر هوش مصنوعی بازسازی کنید.
⚡️
‏
🛠
قابلیت‌ها:
‏
🖼
آنالیز هوشمندِ تصاویر
‏
📝
استخراجِ دقیقِ دستوراتِ متنی
🔗
دانلود افزونه
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7293" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7291">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آپدیت 1.0.4 کلاینت UAC-SNI-Spoofer</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7291" target="_blank">📅 18:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7290">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIAJHwYE4AuHJyC4zy7fv7pAf9vytSHIgUNRFF3ZTFMPL85R_PhhDoMUjQ9QER75WRSZ605TGKcMqWKtx4aLA72cdL0CnGdMJUVc8ScVixaTwxPyq0uJR0eLe2TMSMBn5kCkpHwIPFuOqek9t2vWuQsEUA5Ngnr40GO6QRbhO1a2jh_VmJb-Xsk1jVm2Hh-nGm_FlHqmWI7RKzTMVvyd59ZzunvTUKMjMGJGBewDvXSaPIaQKHDD3BzHnkbQpxuixGkvAWmaB4fT7EPtQHq7V6MuZ7M5UQ176kWfHxlAnWAQIvwInXWQeXzy7nH3XZ4TgeV-NtEtOQtbuUsQfHyKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  ایجنت روتر (سرویس API چینی) امروز علاوه بر Opus 4.8، مدل‌های GPT 5.6 Sol و Kimi K3 رو هم اضافه کرد
🔥
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7290" target="_blank">📅 17:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7289">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-1VmI5M3v0vfs0clFk5SXM6MCHvaXqNWviYnpFRq5MwP5LJyE4eylM97EcIBDqi5zAnwdr7gxrXm82s6Tng9WJ91-_xF2PMXyqQ1JwIxzaWl1MfZnHHB3YvI4cmako3fdD-RoLPAkKI8nkhcFd8YpHTxhZyi6JvyHwW_20FfMlWiIf1rGIPAqUA7K6PJ4_f0OjuZAPNhvlzBcSjoR12_W21nAZVaM-UJbeCS90_4lW0Ns1mfiTwh622TBfHdo_yOkv_6D508aMWgfcPjlSMM0pzI3p0o6KI4tIENVxElB_CKLERrgd7EfJBCdL2JEyFC16J-K2kSnRE8rnsJtmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💸
جایگزین‌های رایگان و بدون اشتراک برای ابزارهای محبوب
‏
‏سایت
NoSubscription
مجموعه‌ای از نرم‌افزارهای رایگان، متن‌باز و قابل‌خرید با پرداخت یک‌باره را گردآوری کرده تا برای سرویس‌های اشتراکی، جایگزین مناسب پیدا کنید.
🛠
‏
‏
✨
چه چیزهایی پیدا می‌کنید؟
‏
‏
🔹
جایگزین ابزارهایی مثل Photoshop، Microsoft 365، Chrome، Premiere Pro و Zapier
‏
🔹
دسته‌بندی‌های هوش مصنوعی، طراحی، برنامه‌نویسی، بهره‌وری، صدا و ویدئو
‏
🔹
فیلتر براساس سیستم‌عامل، قیمت و مجوز متن‌باز
‏
🔹
ابزارهایی مثل
ONLYOFFICE، DaVinci Resolve، Brave، LocalSend و n8n
‏
🔹
جست‌وجوی سریع و بدون نیاز به ساخت حساب کاربری
‏
‏
⚠️
نکته‌ی مهم:
‏
‏همه‌ی ابزارهای این مجموعه کاملاً رایگان نیستند؛ برخی رایگان یا متن‌بازند و بعضی با پرداخت یک‌باره یا مدل Freemium ارائه می‌شوند.
‏
‏
📌
مشاهده‌ی کتابخانه NoSubscription
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7289" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7288">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید ‏نسخه‌ی جدید Aether 1.2.2 با استفاده از شبکه‌ی Cloudflare WARP و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.  ‏
✨
قابلیت‌های مهم: ‏
🔹
تحلیل وضعیت شبکه…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7288" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7287">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FToI9E288WF7k1uUqJ4hWZMQjsOWC5lDpBqxtkvEqG4tZyNwLdexVry9Yxj6ZBAltXnbm6QG4SMu7qhPtzHxMl-edSkz1Ap253CuW465-4TCnXTXfH4DD19ojSZ8L8ycUuyqycVGxDhFljQsbNtVwLhYOgJHTWPvTWaJPLgi7LoV5rBMkMAS4V6_l3zMh9FNPLPH2FyqKSCaOxTx_kRU1Q9CSNVWOQjZ6TUav3rKgd1kc9CCR5qQAoHMLUgWJXkuF0qUfpFZCgLbzLoQ_9UE9LndhWqBI1viOyQ-F2atYUCSFpijTmYRMu9lpIAAPtQEJic-5Z1lG2qgjvsnBDS0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید
‏نسخه‌ی جدید
Aether 1.2.2
با استفاده از شبکه‌ی
Cloudflare WARP
و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.
‏
✨
قابلیت‌های مهم:
‏
🔹
تحلیل وضعیت شبکه و انتخاب خودکار بهترین روش اتصال با
Smart Mode
‏
🔹
مبهم‌سازی ضد DPI با
Noize
، TLS Fragmentation و ECH
‏
🔹
انتخاب خودکار سریع‌ترین نقطه‌ی اتصال WARP
‏
🔹
اشتراک‌گذاری اتصال با لپ‌تاپ و گوشی از طریق
SOCKS5 / HTTP
‏
🔹
پشتیبانی از
Split Tunneling
و حالت Proxy
‏
🔹
کاهش مصرف CPU و رفع مشکلات اتصال، قطع و تغییر پروتکل
‏
🔹
حذف آپدیت درون‌برنامه‌ای؛ دریافت نسخه‌ها فقط از گیت‌هاب رسمی
‏
🔹
بررسی امنیتی کد و رفع آسیب‌پذیری‌های مهم
‏
⚡️
نسخه‌ی
1.2.2
بدون حذف نسخه‌ی
1.2.1
نصب می‌شود و تنظیمات قبلی حفظ خواهند شد.
‏
📌
دانلود و مخزن رسمی پروژه
‏
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7287" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7286">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟠
❌
اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت فورا تموم میشه و مجبور میشید زود به زود اینترنت بخرید...
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7286" target="_blank">📅 15:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ظاهرا رو بیشتر اپراتورها فرگمنت رو کلا بستن، البته باز بررسی کاملتری انجام خواهم داد.
در حال حاضر برای دسترسی به اینستاگرام و یوتویوب به طور مستقیم و با حداکثر سرعت میتونید از MitM-DomainFronting استفاده کنید (فقط نسخه وب).
* اگر از قبل از طریق فایل certificate_generator.bat سرتیفیکیت گرفتید، سرتیفیکیت شما بعد از ۳ ماه منقضی میشه و احتمالا الان نیاز دارید که سرتیفیکیت جدید ایجاد و اضافه کنید (در نسخه جدید جنریتور این مورد اصلاح شده و دیگه سرتیفیکیت منقضی نمیشه)
https://github.com/patterniha/MITM-DomainFronting</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7285" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYznvPRmUJ35UnLBCW-c3Tqcen_jaeGTJeouYZso5psC5x9VO4uayJhIRFih14JV66PvFHYe4crFYeHu2ryditlHY2Jg410ejVPQpZFtWLwbQOtU16peSHU1dB-guifMwwmHxC7c6y_EUSb12yEOhlaht71niNK5KgFZu35oG85TpfT31ze34KCW98Fen2CFb_vOJB9cgucKDwd6iNrHfB4iiD4GkUvelc1UA-39VgskYYSMXa9PU4iy4F-8Y021FXTvlHL8k53Zv7EoUFILV2ZlvucTQU8GWJ_fQiid_qx6CEeaGBiFkNT5CV0QUBSUgFOOOx1idCek53medSuBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لو رفتن اطلاعات جدید از Anthropic؛ مدل Fable 5.1 در راه است!
💣
🔮
طبق جدیدترین شایعات و لیک‌های منتشرشده، شرکت Anthropic توسعه مدل جدید
Fable 5.1
رو به‌طور کامل تو محیط داخلی خودش تموم کرده و احتمالاً تا ماه آگوست (همین ماه آینده) معرفیش می‌کنه!
🔥
✨
نکات کلیدی این شایعه:
🔹
زمان عرضه:
احتمالاً بلافاصله بعد از رونمایی احتمالی GPT-6 منتشر می‌شه تا رقابت سنگین‌تر بشه.
🔹
قیمت‌گذاری:
ادعا شده قیمتش هم‌سطح Fable 5 باقی می‌مونه و افزایشی نداره (هرچند همچنان قیمت اکانت‌ها و API برای تست‌های کوتاه و چندتا ریکوئست ساده، سنگین و گرونه!).
🔹
وضعیت رسمی:
انتروپیک هنوز هیچ اطلاعیه رسمی منتشر نکرده، اما منابع آگاه می‌گن مدل کاملاً آماده‌ی انتشاره.
باید دید تو این مسابقه‌ی نفس‌گیر مدل‌های جدید، نسخه ۵.۱ قراره چه ارتقایی تو قدرت کدنویسی و استدلال داشته باشه.
#هوش_مصنوعی
#Claude
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7284" target="_blank">📅 15:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPixGKKiBp5kGACjo7-cPAbY4df0Bo5_4p6oXrs8nuONOvENggg9YtNzlL1retHZm4MBix46PH3dKgSR8n432ARTuZdJGt820RAF9cwQz6gkLSgDwyXhHLCffVcMUM06eWo0AHJXBcGFnwSvqcBZGnSegX8B2kOC2Ycrfaqk1X98AQ3Lp9la-MMdImV45jP-FS4BNgHWe64lJKWcs08jTemJoHGIour1Zr9yTU7gIOMd2FKgCFPPbfNdpa904-XFctlc7NO-PTmYssDyRrpMr853L3ucZ4OvfARJhUMXcXMY6i4MFxhw5e3-pE6tmxXpbUP3KO3fw7HZu4qckIbPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فعال‌سازی پلن Professional برای پلتفرم Figma برا طراحی رابط کاربری وب سایت و برنامه اندرویدی با مدل های زیر :
GPT 5.6 | Opus 4.8 | Sonnet 4.6 | Gemini 3.6 flash | Gemini 3.1 pro
برای دیدن آموزش کلیک کنید
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7283" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMIqvbvS-04eqO4a9Hv8konZHqY2gsRvmBeJH29qhb_4OWOpTxdiih-gnxB1YB83wAPjzL2jULhadaZC-Zv_8Ycuc-hPiUAagnRan_JInZpSuVzpzUAaUgflKCuwdOe5A61NfbfwtJ7zuSq93gqbOoMg08dcxIf78zftdk4t340MEPVkQ4073BrqLy49f2CV3nVbMULNw2Lg5eQW0fzKxz203IhVOgx5Y5e8m3S0HAKeHVaGjLFhSVEJWS2EAQzfJlh5fxxAhrcThvS4fBL8hZXkMMEvHd3j-hA6odN6H6asRz6ZOYOMSdvkkjPDQjFXZ2E07y6fDouwjhx9tAyW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه
low_delay
(تاخیر کم) و
high_delay
(تاخیر بالا) هست که با توجه به وضعیت اینترنتتون می‌تونید ازشون استفاده کنید.
⚠️
پیش‌نیازهای مهم برای اجرای این نسخه:
🔹
کلاینت شما باید دارای هسته
Xray-core نسخه 26.6.27
یا بالاتر باشه.
🔹
در اندروید، حتماً از
v2rayNG نسخه 2.2.6
یا جدیدتر استفاده کنید.
🔄
نحوه آپدیت:
اگه از قبل سابسکریپشن رو داخل برنامه‌تون دارید، فقط کافیه ساب‌لینک خودتون رو آپدیت (Update Subscription) کنید تا کانفیگ‌های جدید (نسخه ۴۶) جایگزین بشن. حتماً نکات استفاده داخل گیت‌هاب پروژه رو هم مطالعه کنید.
🔗
لینک سابسکریپشن (برای وارد کردن در برنامه):
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
❤️‍🔥
@patt_channel_x</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7282" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7281" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چند دقیقه دیگه قراره یه آموزش بفرستیم دوباره از همون متد باحالا هست
😁
❤️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7280" target="_blank">📅 14:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS2ii2sAuRkHGpisj76-W0lCFz4PPqx4YlOxsOjWAsHiid9xH-9DfGeQ7M20dqlTfCFsBvEvpKGQoRo6P8GHcWFPSReHSW4GbkqsYGhwVu_P22VOmDIsqWeGmY3fiwRB8zJKfLxc4RSFDPNWw2zoiBe6mMi9W0lk-wnmeg0bN3ZseknAxq1USRWo8xwgOnvCmDn8ZPO3QBnQlK0oPsJrqs9bimQ_bXnq4GU3xB8OHUzo3D3D-A0MQP8mrY-y1UHFOsSygQ3NEHph-OqXioOwgYyNJreUlkaMOkwPOOO3sapkRRRSq5Qj1Fs5DDhIE7nTbVInP518n3xIdT28QCTXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی ۱۴ روزه به غول‌های هوش مصنوعی!
🚀
💎
‏با پلتفرم ‌Lumosel⁩، قدرتِ مدل‌های تراز اول دنیا رو در اختیار بگیر. این فرصت طلایی رو از دست نده:
‏
🔥
مدل‌های در دسترس:
Fable 5⁩ | Opus 5⁩ & ‌4.8⁩ | ‌Sonnet 5⁩ | ‌GPT 5.6 Sol⁩ | Kimi k3
🛠
چطور فعالش کنی؟
‏۱.
از طریق این لینک ثبت‌نام کن.
‏۲. برای وریفای، لینک ربات تلگرامی رو کپی‌کن و استارت بزن و در کانالِ تعیین‌شده عضو شو.
‏۳. دوباره به ربات برگرد و با لینک استارت رو بزن تا پلن ۱۴ روزه برات فعال بشه!
‏
💰
مزایای پلن:
‏هر ۴ ساعت ۱۰ دلار اعتبار و ۴۰ دلار در هفته برای استفاده از ‌API⁩.
‏
💡
نکته مهم:
‏برای استفاده از این ‌API⁩ در ایجنت‌هایی مثل ‌Claude Code⁩ بری ، و از یک فیلترشکن باکیفیت استفاده کن تا مشکلی در اتصال نداشته باشی.
‏
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7278" target="_blank">📅 22:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به به
🔥
🙊
دیگه جای عسسسله لامصب عسسل باید بگیم لوموسسسله لامصب لوموسسسسل
پایین کامنت بذارین پستای وگاس لوموسله لامصب
جعبه شرودینگر وگاس ببینیم از توش چی در میاد
تا دقایقی دیگر
👇
Clock is ticking
🫣
🔥
🎲
🪄
🕦</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7277" target="_blank">📅 21:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩  کار کنی؟ همین حالا این فرصت رو از دست نده:  ‏۱. در ‌Boltch⁩ ثبت‌نام کن. ‏۲. کلید ‌API⁩ خودت رو از اینجا بساز.  ‏
⚙️
تنظیمات اتصال:…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7276" target="_blank">📅 20:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtLTtcP6a3l3T6Zg1yZzOOnjCItTa72HCin75SQhyGfyNHHaLrUoBFewrz3_B-rBtfQdEUm536Ddmqoom_3Gg-8rlnuCv-sqU6zMmx3uG9MZgOhDs8RnLNGsIAxi00uYrm1hBWlpwxrpMHVWVg3-Gl29IbBKUls2BaHMBnsLGcS2si3EgV2ph4Fg3aTxStdkxgagtOqHTnkoIdka4m_y8C3fNvszIB4D7Ztrm5375DE_TxiUwsq9yzNgNQm0QBXDsXnznatxekykqE0e3TIX6XoacZ4lPUWreWOQD_FhA3wpPGTVWeD8YzbhNSjOPh1TulCT129IkfKb6WZziz2EnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی رایگان به هوش مصنوعی‌های قدرتمند!
🚀
‏می‌خوای با مدل‌های پیشرفته‌ای مثل ‌GPT-5.4 mini ، ‌DeepSeek V4 Pro⁩ و ‌GLM 5.2⁩
کار کنی؟ همین حالا این فرصت رو از دست نده:
‏۱. در ‌
Boltch⁩
ثبت‌نام کن.
‏۲. کلید ‌
API⁩
خودت رو از اینجا بساز.
‏
⚙️
تنظیمات اتصال:
• ‌Base URL⁩:
https://api.boltch.cloud/v1
‏لیست مدل‌های رایگان در دسترس:
🔹
free:glm-5.2
🔹
free:gpt-5.4-mini
🔹
free:deepseek-v4-pro
🔹
free:kimi-k2.7-code
🔹
free:minimax-m3
🔹
free:qwen-3.8-max
و چندین مدل حرفه‌ای دیگر!
☑️
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7275" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان گلم
❤️‍🔥
این پایین تو کامنتا اعلام کنین که چه چیزایی بیشتر علاقه دارین
بیشتر ازون پستا بذاریم
البته برای همه سلیقه ها پست میذاریم ولی بسته به نظر شما سعی میکنین بیشتر اون سمتی مانور بدیم
ایشالا امشب یا فرداشب ی سورپرایز خفن دیگه داریم</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7274" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvPCmznPUjiZwDZxnvwX2eSsL_xxb2LzAo3qMQzOr-5GsDO7Fu5b6mvBnHz8mWJzU8_O-gN3nS7Ooh2P5w4fZXbhxBirmHHaa8cLpS2xDcTX4YFhfva_AEQ7RZKomvwQFYnXFrpqN61Jw3567olrSjGEa4UJH0BiUBtVl_XSS9jYApePNVPkCahH6R1EJu29ng0_1IgtJmWL14c6xkZFH-JZDJgXbbQWA8hjoGeNAk8jFkEnz333BI7LFuMB5K8Mqg6MOH8ExE-uyD_V23-OHD5C84oKpdWS9luNMhYALRT-ETvgBFJSyMwtDztL1Ifb0STmiMgNrzyMTa94OQNRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
یه اصلاحیه کوچیک درباره پست متین و بازار سیاه APIها
بچه‌ها متین تو کانالش یه پست درباره بازار غیررسمی فروش توکن‌های هوش مصنوعی گذاشته بود. کلیت حرفش درباره سوءاستفاده واسطه‌های چینی از اکانت‌های فری‌تریال و بات‌های ناامن کاملاً دقیقه، اما یه برداشت اشتباه کوچیک توش وجود داره که بهتره شفاف بشه.
متین نوشته بود که از این شبکه‌ها و پروکسی‌ها «برای به سرقت رفتن اطلاعات مهم استفاده می‌شه»، اما تو مقاله اصلی (نوشته Simon Willison) اصلاً چنین چیزی مطرح نشده!
sometimes through stolen credit cards or chargeback attacks.
یعنی این واسطه‌ها برای تأمین هزینه‌های خودشون،
از «کارت‌های اعتباری سرقتی»
استفاده می‌کنن.
هیچ کجای این متن حرفی از دزدیدن اطلاعات شخصی یا دیتای مهم کاربران زده نشده.
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7273" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRfZ4PWdm9iqhjk_cvyxqbgzazPaV6UTDSAj_8tkGta7NZOoMXOnsrt1h0sobYgMmGxlZAwqr4su88V6pYK1qmKLZ5sWf-QsWWfhIQddmAtGJmJLMreA063O_hv9lIScH5svsNViIRjoCvcOSWoEesAQ-yPncZzFQo-VpQIzvuAD-8HGG_3F6V6dQjy87Cgl3MZl5q2nwBar1PrXuaQtxli37_k2PAI5lOSZkKt9rNLjQBOOB1HEpl8NnSDu7iNjFF5k2nxJWQmgUANTjAsx4ONbeZZSUXUtXPR0ILtXFXNh0ql5CaQWCumMp6YaKAPO6zrkCWlT9mwQKZwYYWQVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سورس‌کدهای کامل دوره پایتون (PY4E)
🐍
🎓
بچه‌ها اگه دنبال یادگیری پایتون هستید یا دوره معروف «پایتون برای همه» (Python for Everybody) رو می‌گذرونید، این ریپازیتوری دقیقاً همون چیزیه که نیاز دارید!
دکتر چارلز سورانس (csev) تمام سورس‌کدها، فایل‌های تمرین و متریال‌های آموزشی این دوره (نسخه پایتون ۳) رو به‌صورت کاملاً رایگان تو این مخزن قرار داده.
✨
ویژگی‌های کلیدی:
🔹
دسترسی به کدها: تمام کدهای استفاده شده تو کتاب و ویدیوهای آموزشی در پوشه
code3
قرار دارن.
🔹
متریال کامل: شامل فایل‌های تمرین، تصاویر و جزوه‌های مرتبط با دوره.
🔹
امکان اجرای محلی: داکیومنت کامل برای راه‌اندازی یه پلتفرم آموزشی با Tsugi (برای اساتیدی که می‌خوان این دوره رو روی سرور لوکال تدریس کنن).
📌
[لینک مخزن گیت‌هاب پروژه (py4e)]
#آموزش_پایتون
#Python
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7272" target="_blank">📅 11:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuToqQOCkhFkuzvGf-L3j6TWsEQqpEaEma-iuKZYsItyXU-yTyyYRh22CcZacAnTI8dufW9j6BKBl5Vht12Nv7IuqpCBSXoqDpMDH900IaX4l6RzgpGkVLMYECfETtxQLFujhOdbAp1S1zQ50JYX4udpR0Y4S4cmG2ONmV0tq_5cPC9nTJbizqVGLAUo11GyKvglnbJG9u_LLkgHTAiUZoggzuzgqiH5J-8MR3rBGshHwQ4y7kJMEnm2-yEqfX0589nw9O6_NzJXGeFVo59AWJqrMG82-wSkT5tM8zOtQvv1CV9OTqoO24yHS5trUvxFQf_aZjehw92ju77Yo74UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار PeekVault؛ ماشین زمان و کاوشگر آرشیو شبکه‌های اجتماعی
⏳
🔍
بچه‌ها حتماً براتون پیش اومده که بخواید یه پست پاک‌شده تو اینستاگرام (یا توییتر و ردیت) رو ببینید، یا برای کارهای تحقیقاتی (OSINT) نیاز به بررسی تاریخچه یه پیج داشته باشید. سایت PeekVault یه ابزار به‌شدت کاربردیه که مستقیماً به دیتابیس عظیم Wayback Machine وصل می‌شه و آرشیو پیج‌های پابلیک رو تو چند ثانیه براتون می‌کشه بیرون!
🤩
✨
ویژگی‌های کلیدی:
🔹
بازیابی پست‌های پاک‌شده:
بررسی و پیدا کردن پست‌ها و پروفایل‌های عمومی اینستاگرام که الان در دسترس نیستن.
🔹
پشتیبانی از پلتفرم‌های مختلف:
علاوه بر اینستاگرام، ابزارهای اختصاصی برای کاوش توییتر (X) و ردیت (Reddit) هم داره.
🔹
خروجی حرفه‌ای داده‌ها:
قابلیت دانلود لاگ‌ها و نتایج جستجو با فرمت‌های HTML، CSV و JSON (عالی برای محقق‌ها).
🔹
بدون دردسر و لاگین:
فقط کافیه یوزرنیم یا لینک پست رو بهش بدید؛ کاملاً مستقل عمل می‌کنه و نیازی به اکانت شبکه‌های اجتماعی نداره.
🔗
لینک وب‌سایت
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7271" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7268">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw4bDD6n9hCsd6VMnkpF9JirpODt2N_CwYVa_OLb2zB5l5pCmQuP7NWwnZBh1p81FD8fOiHKWKF2AzNMKutfClCUJ5axTuMdxNQLawdE77RFu3Vf33YIBYfTiyNG__XtVhPX9bWu3C3pETbNTLZLQjulkuON9a5goW35QJbqnLuPDBzTPKXde_QUUTBgp3rCkROz9zMpBLqAMJhGemLFZ_XOJObW_4U0h3QSwYs4D7_N5R45ivtyXyK-n_vlLUVcE1jOhW6vI9twuNJobdBYxJoC7n_-KBUQoGku9sc1m5NlvoojtX4eehUYZYSdz_lCombnaA0Tsc643qOgwBlP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر Lightpanda؛ جایگزین خفن کروم
🐼
🚀
بچه‌ها اگه برای اتوماسیون و Web Scraping از Headless Chrome خسته شدید، Lightpanda رو تست کنید! این مرورگر با زبان Zig از صفر نوشته شده، نه فورک کرومه نه وب‌کیت، و به‌شدت سبکه.
🤩
✨
ویژگی‌های کلیدی:
🔹
سرعت بالا: ۱۶ برابر مصرف رم کمتر و ۹ برابر سریع‌تر از کروم
🔹
موتور V8: پشتیبانی کامل از جاوا اسکریپت و سایت‌های مدرن (SPA)
🔹
حالت Agent: تبدیل Prompt به اسکریپت اجرایی (بدون نیاز به توکن)
🔹
سازگاری با MCP: اتصال بومی به مدل‌هایی مثل کلود، جمنای و OpenAI
⚡️
اجرای سریع با داکر (سرور CDP روی پورت 9222):
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
📌
[لینک مخزن گیت‌هاب پروژه]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7268" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7267">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">config</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ المان کی دلش میخاد؟
😁</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7267" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7265">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7265" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7264">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3DefHCyjQGyNJAaw3_qf77EpQ6t4VkpNW8bvmJZ7JQjmzURKBmqOc9x_FmkGDdo8Y_4bs5irQrfXk8Z06UaLC-Ogy61RE5G0tdSgWS5M2CQGEdjDIHKShRWhgi2VEBUtM-AEK3R4g2mKAKE2QIkTfh0US2AJB1-F2E4hw_QOSwqgaJa6XeBrXKevMU2NwGeezQNKZ_fKzgsPcR87sspMqHOg9EKAOTpBCp4dWD48Rfwa3cYHMwlJq9Vj5rr7x9FpO421IPYjMZDCa8dPqER9VfNdzgAgPPR57n2gquVQHvW35CCQbowFxkxJNIRCVZOpNrWkN1x50NUeXvvFS_ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7264" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7263">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">من نمیدونم کامیونیتی تلگرام چرا انقد دشمنی زیاده
همه سنگ میندازن تو مسیر هم
از حسادته از فکر اشتباهه از چیه
فرض کنین ی کیک بزرگه
به همتون میرسه
انقد دیس نکنین همو
وگاس میاد پست میذاره
بنده خدا داره کامنتا رو جواب میده پست ناب میذاره. تازه و درست حسابی، اونوقت یکی میاد حرف بد میزنه. هممون همینیم داریم تلاش میکنیم کیفیت رو بالا ببریم. احمدرضا من وگاس، اس و بقیه دوستان
خدایی بده این کارا
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7263" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آموزش گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7261" target="_blank">📅 13:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_EQ4Nzzht-nHLAuhYB6wGpl29SNuVSNHoZbGDK77GWfaR0YcYgU0fsPSPp2Cd50KSSTZ36uNhFOkMVN3quu9hVwYL4OYroW6ebo2GN5tV0Uv3jg-wgU14Q8ZY2TpAIhEhX2GMlGc9hXA66BoCrJ-2o_3gbKDrSV44cqguCzqDrzCF1_3L2uy5m9Z2HSeECj8JxV9ZshpRUxhxb3bx2jFhD2m8iUw8t71Bv2nfjVG_Lh6cxytE4cxG_uDhKKN1ShnkgjIS5bL6nFqakXBxIiyhNrQLsH7GauZU5sjbr62mOUGrsRpF3BngJsyTNhOp8obibjzBcMmdXBAJbNJ_gzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش
گرفتن اشتراک X20 max claude به صورت رایگان با اون متد باحالا که دوست دارید
😁
❤️
توجه داشته باشید که حتما باید روی اکانت فیک بزنید و در کل باید بدونید که بن داره
🚫
به مدت محدود قابل استفاده هست همین، حالا ها شاید متده بپره سریع برید بزنید
⚡
برای دیدن آموزش کلیک کنید
✅
متد به طور کامل بسته شد
❌
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7260" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
