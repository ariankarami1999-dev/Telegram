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
<img src="https://cdn1.telesco.pe/file/Oqg-bDqvEI_1uxNp29-VWcccL-Ms9y0UkU-mxHv4cLdqd_WT5zhGwyKkS1-q3cCf6XRpbdPUEtRkSn0F6WgulRexFVpI9x1lZqLocRnTl1b8V44kbME-FRzwJyqj-8tZFUHFHFqNE2xPcrG6rIUxLL-Qye74rh_uGdbu1olB1y-BbmPjlm8nyBc_nzpYtQmSNClLNp2g2t05VvSasDUBbvLg68n4iK44iO46QNHFBeEVxZdIFQT9_BMvKknozIEQ22MzChycH0fxmhyiNDkeb3ZZxdQ38mWTrUARjkmtStHW23G1U1FSMxu36VYEIrF5KaCxD84B7c8zUm2iMhKdhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 00:09:02</div>
<hr>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4384
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DmIcn8PrEKupXgm1yLZcgFF7XxzoMp6rLSdpff6IgUxqiud3b3r5rFmey2lhzTPEI_MHHtL1C6zIJ-MJoq7DvYw_T2WMK2P8Vj9rrvDHH0i5r8MSMbgXyOZGTtLZya5dI8aoB-wqosi7P3aEvvgN1TCQf13KYxSu6j1KkQGcJGfLJqojhQ3zLGGBXzPDvYdlhccNo1Ew3du5uQ_qD2UD4rJUd0fuTpUFONujXgPPDSlK1Z44uirHaIagqEgnls0oq1hsMyQEYO7Fq-sBKQVxN7EOzXKsh4rI1Yg3f_ZNpH6ePirWHL1J4nTtP66y6TZpIjwTKIgRyhV4RnIMoMMBXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4384
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t4Ii-9YbJLGvRGdIpwVQul49Qqo3o7B0iXAvcCC98EmH1MHfnaaFA-gqTBXm8P-mDq7dVL8zmadiPPa8H0FYpGYRc1RjsR8HzfISdvp1_ats12GYDE3Fc0wxw9qjgjU1AP-AZ1pMCMp6wNwyzkuGY9VeTgsxjRxSo5WrC_G1_3IZ9U7-y_6oDe1kIQ59XGmymAKo19MRjIjxRfVsCjcqXy-Vslo5-82y9NeE6ZCFPIxU-7taNmUeIOSqtTXJJTp5ReDDPgyGbLJipyW0E4lW-LFVsBnld3NUh50lQxzbeziCsBAhfaA614QnaBfjOhF860r0kKAa7jnhwlOe_77PVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vmo7vMnYNGx1FAJLnKgdknLP9qTtBUfYdHKTPlmmhdSFkhLucVUfvSzO1VJUYXhOgaeArMtJxhJ6O2lvWVEtkeoEXsVm5dGOobiBI-T755bIK8JbQlgirMmKvr1KQHdkyHuDSpPxcc5YRIpWSM5DAyepTGeCGCjksFbDpdvj32tC-UANU7E25GuvKEOBSebHRuhv5BnQ4M5TTc6M6I7RyWB1sFM2XZa5SR9syK_su8Q2PQbFOkfTTwp9l7hTfWhjABbMvUAHWrQnFPy-RYCdZboQ_RnsuuUcusMtGCN8G2MQJnf1vNJZniKg_wfQlsuM600VkMsVJNTvBzT5_3wptA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8GKzn-ZMVJcwolk2bCSI7z_zVgEonLum93UyD38NaKMB-H65D9SCkrz2TbAi3S0sTiRgYdvrZQ8fFvC1NpOlo6bSniD6FU362a2WfMCf7GQakkThycLxhlCAV7wQoaCeoUrISqpqc3GFgHLAI1a2HapgxTlQ38WG_3d5CZLav6gnRmE1LUH6XGGbNTtHqj3qYHhaHyC2qofJuRqOSCEKmchFTCmpiNZVgIZp6H_MYII7kyIFVo7Wcjyfs5fsT9wgPCF-vt8Rdb-d9jWJCl1EjAzK1Y1UP4B94uyLxIXOgB__I5HKL7ZF0gBdXArPM7EoMvhUSpLlyDtWVWTkAOSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FgNabo1M6zf6JyPMhTJnpTyfkPSny8Tzh2oSMgfkRnAllGFGMmGNNdcUVIVBNLUG4o0GQA14cgN_Q239Q6EygVS4rmij0q2vbayXc4KmCw-mBT49zf1vPJ8eltfKSiaWrWKkxclCbN8wucHRsUPjiFli8IByq1My-EPn-k9_T8Po-BVWnQ8SS3Fatd0oLBdRaWsPn-CzOiVYxZYGSd4rUWnZwRB9oo14nL18XeQMNewvbtfvx8fDj-X32R8DnI6uk463rsUGpvG_N55WgX023ohBbYWDTT1_aCTbFzAjHmfsAd3lEIg8dROjTGJ6cgk3-MiFZx_LDSlHZ28cAKGGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdRTurk-nXJ9086y09BusejwWMsBuQ4TO7P9CKzvoVzomiE-MTQX_PggzeHt-u8LmPKwzQ1pPGgbIOin3tKoV5DE8UX4D2sUbdPs_isrgw88NU_XqgUneHIKrQQG8OH-bOGlOp3JaOsid1DIz2J0KupRSztG8PqZ1fcCcB7UNaLRhdDRqGj3eZNKSOTKa4JSesMfNTlbV_w93uoAD0APdmKikTbdS17rhsGWG-vi-fazueGDSMT8W423ELJpMue4A3MsIIPDqHNk13iC_fpT1D-LoPTeQgdBYdK0sDT4YE0w15NcS8fdmNCwggSPA7vaX_0UmPIyFlcjF0RBF194Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVIiCx1FEzjLEK7qpnF7a3vlY0HiIH9aZ8RdaB6BDW3Ek7TXSKb73yjlMvYOCnQTn8GoufPCmgMz5z0A8dKcphEuoG5Qrke1_3S09qGJicjxnKcLk3pKThdXD8fgqC7_qQfoaL0WE6PBdzj-Px1DCQYtpcKC-YsuweeD31LZB3J2BeD7eUvHHmu4ffke304So5LrJpYrKDN0v_KXMKGXeE33W3n9v9QSNQiwrozfJhFW9rv_tFVLr9PXyUpvgxTKYap6biTRD7wXUi0HAG_2zmKvul0I-1Hk9pHhz0sRat0kBX-CsY8a_ScuFowVVX5J98mbAaUE5EEeSJrXRHKq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYk6s6yuDdKB-F6XdnkbE_F6mIZC1pWs5CZuBMbFyzGVcFcjw3MUIMV5dArcFkYv5183xHJ7o5L9dQbpY_Aaw_LYVv4OU1MUxv1Es8JbDqlt50DOthUhsFxeXociphgWN5MuqYcmKWN0VcSUuqL6t3UGnm5TPagyDbRuxNl2aR43SGnQHYr8Pq6JpeuES701bFMWe5YMicleP0M_bree7ZLSiUrs-Bfm1jB-72k5UYwt7cY6FsYZ5f4LX4Mob6nUNz_7N7f3DRDMoPAcJHK5APT89dPq1pfae2bHWr5lmlmXOw1FjrcGmtjTx_IA8uMePu9f9mCgp-utP1-2kkCMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4371">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر
که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که خب باید بگم نابینا مطالعه کردن
🥰</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4371" target="_blank">📅 14:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kS2MZyoCopgSSKGFejEtGmjH6E2OykWmHzaZbya8skmaTJWTvD-sRb05zx4RaE2OIwr28pOvzVw2_8QPxlR-QmkZeSRbrMAjgnQbgJV5ZcPUY5K0ErXBs-mDMSAFlXhSZK-uXYpf6z-wYG1AVgNQYKpKWTcwk2fEpu4i-_8n5EMrKwUsGFtDnuvUohoGsvzeVEs36tM_lTECtU92hsI-TxUV_f-miGqBTAJVB1-I2sltvWxneH3QlEqdJKlYh3gntfqsQoFUd5YXEDE-3zBoqU28jIAp4-OIhDWjCGiFUdhpnXJIZXQGDKaKY9SCgR70bQPH_5cHC-AmXDKasInMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F-WlV_UH1mUE3IbsH7OeURWTmju61fJ9eZPi9CV77zdIcModVG_cxUoTMWmbSDeNXkWGpTLwUbtZ8NO9Jyf8J-LIhBpOKxDKqlTTd2yU0AA4oLdHfcaC0w4IVBSNcBAErVa8wV62PlMlre23MZVSxb1jtYbaT4feSUxbPUB4rDn6NBFHgZ1Da19oL0OuSp4vcwZ78AOpl9ZaEbsk8IqiwC7Ya7tjkOaiTMSKcDdNScdDi_k1ZgnqP81VRlSewm2BJV_cVnxrr6Nt9Jsg8R0oqh4E4qz1lvVLh0YN4L4dnDK0dNGzxHJd7G86NCMJsXDu42oT8IEL6dPZzWDfT7zgEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a406hjtUggNg6RIEwmXfFTrtG0439ai1wxehzjt7hNFbhO97vdypQ2EED_MRQhwFCnzbyyjuDDjGt6xhW1eASAnZtEY_2gMQe2QDws_SprNMeOH0MVxTznwniVgAABwH4n51sn18wXJfSXb56UQrjRWzsDCk62apDqTNYJPgeWlBQ9zn_7Qcvx5hqIHD6XM7NgllQecoi5l1J_93yIQmhIj8aJxmcwnipg2XvnQvu-GbVYCHTHhyHQBKRk7pHfCTWEd5VBox1D9D9hMtgWFr0CQc4r_3Tob8tW311Qm9Rg48z-pjyvNvSdLz3niqir_JU_hE3KDCzUYTWiiHYJtkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vvOq9wlwqERVVIU49s68IjMBzo8MPXZ_qmsKA3QDsB2jtlGv6O4g_WsaGHOqC9vSoZngcUbcqJcMFmpK3HIQuBy2msZabnEIKBBs9WZ3C4QLisGaXzIXXp3CBVUBpPe2RSID-sHRVuw5lQwK0IwWz955EeXnu0QylyIQG1jXa93lllVSVRNoOnnIUaR-KbqNJLQbpwRzYYnEfS7K-5lf2EoGrZXiKKDhfAs2X3yJ8h3-YVbcns5tSieLjt_n-u9FjoPucuLLYvh53aqAkXDMUiwnyz-mzVY3FCgV8y9PzfZwlvJZtAWQXRs_4gtSa17LEAwBezXHUBS3uD6pnOXDGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک زیر رو به هرمس بدید و بگید:
اینو نصب کن، فعال کن و بذار تو استارتاپ سیستم تا با روشن شدن سیستم اجرا بشه.
بعد از نصب یه محیط بسیار زیبا تحت وب در آدرس لوکال زیر برای شما فعال میکنه:
http://localhost:8787
https://github.com/nesquena/hermes-webui
✍️
بوکانت</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4367" target="_blank">📅 07:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فردا open design و claude design رو واستون یه مقایسه میکنم از اونجایی که روز آخر اشتراک کلاد 20 دلاریمه، آتیش بزنم به مال(توکن)ـم
ولی ویدئو فعلا ازش نمی‌گیرم. صرفا اینجا بهتون نشون میدم
چون هنوز به open design مسلط نیستم کامل
در عوض تمرکز می‌کنم روی ویدئوهای درس خوندن با ai و بالاتر بردن efficiency</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4366" target="_blank">📅 05:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720362863c.mp4?token=MoTQTNfSWx5aLmck95iG8rx7wVZoAXC4j6mSlGuCrnSTrHwkHLVn1Ca2dToJ02ZVsCwsyXIQo7CkFSmHmVrcj86U_rObrqDFS6jGW8-_K6VBZ6nIEHtW2ukfciGAHAH4zbBuMvcSpboCyYRumlDCsZlgjY7RUrEJiFWe23jFGb_znpEa1YG1JDvKWoOaPkXCLtFm02enU5E3Y1k7Co29nG1qSsegYTpLN_aW1aNi0jGi6phubtUR-hX4w5_-mzEOHa-iz9VTbq_m5FeD9v_1pvQuybobvZAsyPpI0xtszbOLjth4iT8M6EQmuvj97Q_iYyGiVBL9L4uhIf2RKmLByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720362863c.mp4?token=MoTQTNfSWx5aLmck95iG8rx7wVZoAXC4j6mSlGuCrnSTrHwkHLVn1Ca2dToJ02ZVsCwsyXIQo7CkFSmHmVrcj86U_rObrqDFS6jGW8-_K6VBZ6nIEHtW2ukfciGAHAH4zbBuMvcSpboCyYRumlDCsZlgjY7RUrEJiFWe23jFGb_znpEa1YG1JDvKWoOaPkXCLtFm02enU5E3Y1k7Co29nG1qSsegYTpLN_aW1aNi0jGi6phubtUR-hX4w5_-mzEOHa-iz9VTbq_m5FeD9v_1pvQuybobvZAsyPpI0xtszbOLjth4iT8M6EQmuvj97Q_iYyGiVBL9L4uhIf2RKmLByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ردیت یه نفر یه پورتفولیوی کاری ساخته که رسما مرزهای فرانت‌اند رو جابه‌جا کرده
😂
طرف طبق گفته‌ی خودش، فقط به Claude Fable 5 یه دستور خیلی کوتاه داده(که البته من به شدت شک دارم):
"یه پورتفولیو می‌خوام که کاربر نخوندش، بلکه توش پرواز کنه!"
نتیجه این شد که کلاد صفر تا صد یه سایت سه‌بعدی رو ساخته که شما توش تو فضای بی‌کران اسکرول می‌کنید، سیاره‌ها و پروژه‌ها از کنارتون رد می‌شن، از تکسچرهای واقعی ناسا (NASA) استفاده شده، گرافیکش روی مرورگر کاملاً 60fps ران می‌شه، و در نهایت وقتی به آخر سایت می‌رسید... سفینه‌تون می‌خوره توی خورشید و منفجر می‌شه!
😂
این پروژه قدرت وحشتناک هوش مصنوعی توی ترکیب کتابخونه‌های پیچیده مثل Three.js با کدهای فرانت‌اند رو نشون می‌ده. که اگر بتونید AI رو توی مسیر درست هدایت کنید، خروجیش به شدت جالب می‌شه.
لینک سورس کدش تو گیت‌هاب (اگه می‌خواید خودتون تستش کنید):
🔗
https://github.com/AbhishekBadar/portfolio
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4365" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4364" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.
آموزش راه‌اندازیش روی
دسکتاپ
و
گوشی</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4363" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub(Afshin Karimi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbO-GKh03DOUKuBPr_iRh_Woo4c_tSmGJA7RITLvN3j_6r-FzAGtJ9V5yoVklDVZ6h_-6A9poljYRdyy_a-JL9CdClbIb46QYyowN3mi1cH4K_5a9bnrINZJJbZCk_8A6ISA4CJD2swatAiIMpqRmuM5l3uLxeW3f1iazkYGQdbWDIts8tqO2qRD9zNI-V1nwdSgRc043JV7v8reIlpuB108leJR4QU1GuLAhsY3kgMLeDm2nMwA3bdpHKsIXMLCPCAeTYmiDM9xV5eMlQx9nyjhnoLSas1uP41g8WBCOSKDLDBjx7JnD3SbFIApUW4DpIoBpVC9uoQg9PSIqNE6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه GameShell یک بازی متن‌باز برای یادگیری دستورات لینوکس است که به‌جای آموزش‌های سنتی، مفاهیم را از طریق مراحل و مأموریت‌های تعاملی یاد می‌دهد.
اگر تازه می‌خواهید لینوکس را شروع کنید، این بازی می‌تواند راهی سرگرم‌کننده برای یادگیری دستورات پایه باشد.
https://github.com/phyver/GameShell
@RepoFa</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4362" target="_blank">📅 17:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bSPGtd0wnuWIWjpYSRjKf0VO1ZxOK9b_eG7QsogrV8i_Vr5X-7ZBLDXEPV0URVYWKEbwex1I7fQ8wfqofKZhVo3xnMgX9HVY0332Rbm1rtdoKFo9pIJ_Lz7bTRp57t6bh6Nns9LB57dMCVC14iDq5_ogaPySQWl3Xbeg1Rrs2sflKH0Y2j1Nv2O9VcKXPmbgErcTn-ftUj4ZxglV9OJKf3dtsz6pBcdcz2Osjv0UuopPucfn58mO0WNj_3kkQ2sgJxGcdd7_i_Qc5Ubfbf7IkZKnaNv3CsZunL_uY954wmTYINxWCbURaxduuYNd_qUIjOOI1bjzVgP1vD7peBQQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4357">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNYMunLhDweQbsBh3U_zM1D3h_NXw4UBuP4_z6i7V9fniD4vrhFbiZYkMWru4zqESEGaQqDFao4GdsD06SAAM_sz0IsXxaoFSG_y774jn-zkp5rw1K_bLGrtCMMwV9HT0p_zp45-AlX8g8siK1--24s9MvlChU10ZJPzY_jd0AcxnfyH-1AjtfvOEBK6HdU1tW2E9DLHUJJNiSMsnCQXulOitQyTkbFI9BVi1kM0Y2PU6fHmrnP-hIWhOhSy-G1YOC3NgLaHfyNe9DIUQbRU6iUn6nxEruk1vo-YFYs9VuHwVkZNvLR2fgRGnv41nu_SatHmQ-ZYMdmXQx5z7-AApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.
داستان از این قرار بود که با
Z.ai
و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو C ویندوز پاک شده!
این اتفاق یه یادآوری مهمه.
هرچقدر هم Agentهای هوش مصنوعی باحال و قدرتمند باشن، وقتی به ترمینال، فایل های سیستم یا دیتابیس دسترسی کامل داشته باشن، یه اشتباه کوچیک می تونه به یه فاجعه تبدیل بشه.
اتفاقا متین سنپای هم امروز ابزار Kastra رو معرفی کرده که دقیقا برای همین سناریو ساخته شده. این ابزار بین Agent و سیستم قرار می گیره و برای کارهای حساس مثل حذف فایل یا تغییر دیتابیس، اول از خودت تایید می گیره تا AI نتونه هر کاری خواست انجام بده.
به نظرم تا چند وقت دیگه استفاده از ابزارهایی مثل Kastra دیگه یه قابلیت اضافه نیست، بلکه برای هر کسی که با Agentهای کدنویسی کار می کنه، واجبه.
تا حالا Agentها چه خرابکاری هایی براتون انجام دادن؟
😅</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4357" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4356">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aubye9f-fCUKfN8WIM7KPYTsA0ibmfwjNpZEQR2YyIqTAPC5YgBE0QS3TP2P3MEJcR0EYdEIcFE0RiOFnM-Ug-Oxe-BpuqGTTutAHi1vz4ctnHZHWOThY161jBXn5t22kWowWcYCMYBtHxXCZMlNJPpROg8NDWdXOoe5CaV4U9mQA7L6H9FKohrp2__zJ4e0h2QnlDBqYsmBhxOlFxZFmUvmA3h1luVByX9QeVDRjxwLRo0RQ_FP4mnrcmGjchgbC0BRLF8GhA5Sd1eYshdCgG6U2H23nDUax6cX5OEYr2YARkpfexwYIZcQR-YIBs9DW0yEXhkEXxLlOMq-UQXrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Kastra برای کنترل ایجنت‌های کدنویسی
اگه با ایجنت‌هایی مثل کلاد یا هرمس(روی Yolo) و یا هر ایجنت دیگه‌ای روی کدهای حساس کار می‌کنید، استفاده از سیستم‌های نظارتی دیگه یه آپشن نیست صرفا به نظرم، بلکه واجبه!
توی Hacker News یه ابزار خیلی خفن و کاربردی به اسم Kastra معرفی شده که کارش اینه که به عنوان یه «لایه‌ی دسترسی و تایید» (Authorization Layer) برای هوش مصنوعی عمل می‌کنه. یعنی دقیقا روی فراخوانی toolها توسط ایجنت‌هایی مثل Cursor و Claude Code نظارت می‌کنه تا اونا سر خود کاری نکنن.
چرا اصلاً به Kastra نیاز داریم؟
ایده‌ی ساخت این ابزار زمانی به ذهن تیم سازنده‌ش رسید که ایجنت خودشون نزدیک بود یه دیتابیس پروداکشن رو به کل پاک کنه! وقتی به مدل‌ها دسترسی کامل (مثل کار با ترمینال یا دیتابیس) می‌دید، هر لحظه ممکنه توهم (Hallucination) بزنن یا اشتباه کنن. Kastra اینجاست تا جلوی فاجعه رو بگیره.
ویژگی‌های اصلی:
- پشتیبانی کامل با mcp: تو کمتر از ۲ دقیقه می‌تونید با Cursor، Claude Code و پروتکل‌های MCP وصلش کنید.
- گاردریل‌های امنیتی: می‌تونید براش قانون بذارید که ایجنت برای کارهای خطرناک (مثل پاک کردن یا تغییر دیتابیس) اول از شما اجازه بگیره.
- مدیریت دسترسی: مشخص می‌کنید که ایجنت شما دقیقا به چه ابزارها و چه بخش‌هایی از سیستم دسترسی داشته باشه.
لینک ابزار:
https://kastra.ai/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4356" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4355">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=G_FmHZ97Nkq6CTiPHNum1Zq7ApS0AYYxKMAnH1QRVzb22d93mhUAD-5xomZFZ5V_r-O17am9-_QalcscbaRIhH-v9xHs4_2twAImhPIcvJzovtG8w1c12XS9SMdIqvzjIBzlew4R_l3a7j1xxL_Skh6jSxjyviIkg0Ld96YoZy34ChKC2QvZi2mecdiwcVSmwYw7dICTK0zgOMSiz0NdgdI-e0vcb7lrqdjfIZIb3gaZgXCExnUNzL-_t-P1__HjyZdZRVIi3e7yLM3p0Izx2h9NgQoaulXQDB7SUbzrZ3uPUJH-j-MUvxZ2FFRyEqKNy16GzPnfNZCqzuzgIXRnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=G_FmHZ97Nkq6CTiPHNum1Zq7ApS0AYYxKMAnH1QRVzb22d93mhUAD-5xomZFZ5V_r-O17am9-_QalcscbaRIhH-v9xHs4_2twAImhPIcvJzovtG8w1c12XS9SMdIqvzjIBzlew4R_l3a7j1xxL_Skh6jSxjyviIkg0Ld96YoZy34ChKC2QvZi2mecdiwcVSmwYw7dICTK0zgOMSiz0NdgdI-e0vcb7lrqdjfIZIb3gaZgXCExnUNzL-_t-P1__HjyZdZRVIi3e7yLM3p0Izx2h9NgQoaulXQDB7SUbzrZ3uPUJH-j-MUvxZ2FFRyEqKNy16GzPnfNZCqzuzgIXRnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه. به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4355" target="_blank">📅 06:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4354">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه.
به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن تبدیل به زبان طبیعی می‌شن.
شما می‌خواید، و انجام می‌شه
هرچند هنوز، مهندسی اینها، و نظارت روی کدی که AI می‌زنه، خیلی مهمه به نظرم.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4354" target="_blank">📅 05:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=VaUptYFrwXMiONAqUpJgaQocvrSo8yiBArVWXbXN-V7UKwpLiiafuOMn756OdN60hMrO_ot_I47CxYfzABCWk_dmIiy-ts_IEKcq70U5P3ZO4eVUDHzseRut_2avRQQrzDsKBNgakt-_oxYbd0E_9djkJBvNHYvC35ihyWV5hP12XkS1ho4xFiaCW6vgqG2BiS3XEXRnskY-tmhmFbMzIBNFDKP2aSV3yjGQ9vV04HAW9tKzwWZ5HJEhtACifkqyTITlSTXXWnd5XmrDQ09T4xZ9TsL6tiY-t7DHlRewJGdglE769zGCGdlbXtsnPhLIpUwAPn4GU49exsa6XKD1TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=VaUptYFrwXMiONAqUpJgaQocvrSo8yiBArVWXbXN-V7UKwpLiiafuOMn756OdN60hMrO_ot_I47CxYfzABCWk_dmIiy-ts_IEKcq70U5P3ZO4eVUDHzseRut_2avRQQrzDsKBNgakt-_oxYbd0E_9djkJBvNHYvC35ihyWV5hP12XkS1ho4xFiaCW6vgqG2BiS3XEXRnskY-tmhmFbMzIBNFDKP2aSV3yjGQ9vV04HAW9tKzwWZ5HJEhtACifkqyTITlSTXXWnd5XmrDQ09T4xZ9TsL6tiY-t7DHlRewJGdglE769zGCGdlbXtsnPhLIpUwAPn4GU49exsa6XKD1TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=pI6jBrkNaOSMS2J9NvWQMCwtbXXjflcZJIf3sEsJhINrYFrkBK17tEHljWYYjC8Da9PSWgb1gFROqbtWlZ4MfycS2yRn0DbAqSYomYingdsDJtCO6vdkDSa7p06Af2o-cedBHSc5XgUzVr_qS9IBoiz4E8ha1eq7QQpFOmmacWZmCbsHhweBJ46mBOnMLVsUwWILJfURz98RPGllFTOtR_QxEqIVUYy1yCh3g4q2T1zfNPAh8we5zk5RPBc8cy4ypD4Vuieh50g4jfdhQlxQeT3tAvnlC2CY4tqsmE-j77gGRFtYmMvzMyJsxBBE09U9Xs8Hgn--9fEd_VHMVDGeFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=pI6jBrkNaOSMS2J9NvWQMCwtbXXjflcZJIf3sEsJhINrYFrkBK17tEHljWYYjC8Da9PSWgb1gFROqbtWlZ4MfycS2yRn0DbAqSYomYingdsDJtCO6vdkDSa7p06Af2o-cedBHSc5XgUzVr_qS9IBoiz4E8ha1eq7QQpFOmmacWZmCbsHhweBJ46mBOnMLVsUwWILJfURz98RPGllFTOtR_QxEqIVUYy1yCh3g4q2T1zfNPAh8we5zk5RPBc8cy4ypD4Vuieh50g4jfdhQlxQeT3tAvnlC2CY4tqsmE-j77gGRFtYmMvzMyJsxBBE09U9Xs8Hgn--9fEd_VHMVDGeFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LzASId66_ce2SxOG4Gi8tBUNcKtrLRqbqOF16fbbwJnNUm3pEaawP-bYyBBJcWiY8COv8cnKVRO6vAav_77ozZmKDlg2K6QCcFFOsL5zd0en3e2bPxMcq3a86XSQB-gv8c6na79C-KTH4XF-h9nVlwPXQnyr7FGrC3j_p_1yphQIuXFT7ew___eDXKwrPy3tsZAC_JcTmlKI4tOQwkedX65YMyEtN3KYjzfdn_m6zu6fEZs3AkO4pN18mei04NQfhBmy5nbCnz4wn2l3cLpVjSExyaGi71pmysDBat22_j1nzvn01cHclcNHlR9olhZKaK6Ewby6GC9IsFe2h6DfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XgsUKwftHI5VnBaBPqMt-cRLChvhjqvnZ7r4I2nmX3EuOyU-iPySbVhuZMbApOSS0tw08PBSyBjvM8D8pZSfInkh704bgpBDt2GD9bLaf5ZOx3OapCHJFQELagCOrXVzQCOIAauPrOEPAH_vjwBNznaZuxKzGi5eLb2rTIo3hQw8iu0Cbkyj0FIj6_ETbc1SmK5V1kMsNYmoKtQTEHKxEtZCoaeTaWhbJDY_3wW88ajcFCOwq401Ez0XwYPlPsuk17LXV8xas-7h7Zcx_d5ckvBhFb4lLkoZ_KmcwmVnAYEbrHygSkAKnK4uqGooG9NTuAqwJt_qgCeG5cH1iU-mEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=lBpatgM3GhEiA7kK31zeC2IaWHKMXiaM___SX7dfmxgFhou4djfBD-6amx57ICQzOhLNo4wkUAu9E65fkpwsQhuH1D-K3-ZRgXJK2ImkFRuXPLsKhQzowVLCUIlLzNYcRvTyK-FgU7-blffrqrBd3-e8AoajJcjyEyMtaa9Yfb2XI2AjFfXxV456z05-4tXRDKCRhmGpTeQ2AUt4f4tWfJ_36ailJa685FTuhs4Ln4LoaQAMSSjRF-9x2Fq6xBOtNhJSY2vVHOSBSr2nkTcVALT-wbPeOPV1_m6BnQSloMT-FwaMqrMl4NYMrawJcTvprgBo4uF18mjSbOHmp9yKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=lBpatgM3GhEiA7kK31zeC2IaWHKMXiaM___SX7dfmxgFhou4djfBD-6amx57ICQzOhLNo4wkUAu9E65fkpwsQhuH1D-K3-ZRgXJK2ImkFRuXPLsKhQzowVLCUIlLzNYcRvTyK-FgU7-blffrqrBd3-e8AoajJcjyEyMtaa9Yfb2XI2AjFfXxV456z05-4tXRDKCRhmGpTeQ2AUt4f4tWfJ_36ailJa685FTuhs4Ln4LoaQAMSSjRF-9x2Fq6xBOtNhJSY2vVHOSBSr2nkTcVALT-wbPeOPV1_m6BnQSloMT-FwaMqrMl4NYMrawJcTvprgBo4uF18mjSbOHmp9yKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMAABdoQVOXacTrBGw6xZWph1TwSo4CWo1SQMs6fxD0HwY_z33aof90JzeUTGbriFqQwgffgMPAzdxamwOtQLIOT2qDq5I5_PsKNb4ALVA9cWV7XzafOC0r6nWn94T9amd0b8fPgtvdXtEwKERfQzj2KlAhGBEGE05I7c76CZIsTHKhPEAjlh867Gqn7vhAUzJbcjYeSuPINvlI1LK9-UQiESKyzwxE0WzXqzgp0O6TG4sMcSjfieFVgBFxqGjB7dwTLzM84X-jtc7EXQN4yVizChEPfZOMPqLqw91O1cRdqV43JeL09FafQ5z6aUEwxAOV_jPoUE2PNdsliNC6kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MPWzZ_fNQXsZXxplHPnGwhE5fhlEc_GKBFRmkr74cbLvG4dmq0cKPbeQIICJTk3FUCJZIlaW8p4PTtqqEKpN8GoB9IgxAlyfDsdDV4LAsnVb8lJ7ZgShBLr2pZ-JtN_7rlbn_HFUyaH95MZqz9Hzy6wkIWufRbUwKbszqdC4LaRVgln8oX3mSUnJPmmXXg-Yr7nl6QUCEzkRVo8CCKf7M-B9Hnp457ZdhHA1mVdFDL3F_N-6N9lnPV8Y3d2kN1t-wK2FkQPvVd3Jvzh4fVHCl4VFXFJclwANZ4ezIsLxbYAw4un830LJqm7UBFd98yPUP-kx0i5-d0Shc42TQscJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nJTc8g5Km94wFgxsdQTWbzm87a4QHn5gPVVIpvz00iTRcJYLqfhKp7cMOrwFMf9b_7cZ0WwPfAFJI8pzHCsWrc5iO5_WNGqrSkr3QR1oroLNSRzVRBt4Iqb6G98botYGJMLQl2RHxx2avYCg2BUfjlIsyq8Zs6Z65b9oDz4iUNUa5QNIdc4KuD7Q_wcdb4T3XhXhDAfISKJuF4Vo-HL7mewjbiiJdU52Voy1LLitZ-AxsjN2zXFgdqxmrX0WWiJBn3hvD312SxqNFcKkCnjfqRzNLWmNcyUc_tMv1lV7egB7yrWOwjLzgpNJhWbjakZWn6_NfIAjT9g2ldpXbVbDFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=dfGYeDztCA878fgLpCV_WtlgWIJLsZxEkBpt7AV-yA-OtHcfVPxaaND5xgVMb55igZG9UEji2mpYQ0YTECoWaf12yOx3NMbMACWCPZfhU9ZmPNqT0wlg7MEOBcBuN2wI3p_OFzgKeYchvxbYfrFXS2ziC5zQGpu5ulagB-pgvhBtMqvSmSXF8NNxnsLfMQt9psvgridnw0c-F4E9emgVMR0jpzuejMj5-MnZb1wxQ23SLHxuQic8zXD3VeAb8tJKTpWQYDOBrnPVSu90nt17i-DADKqNA1qDPR_EEQhoZRmzjTOuDB10Yvf6cUojQ3md-wfSqUc-2b1Vt0lYvId_2me2kNmawh2KlUFEt-Ru6riNttTxgt6NQuVwv03L6fbXLCexbJUC3BMM1emQG8ypCncPNgak_wNqjcopDyjqecy2Ig8Njb7P-1t6wC6JZD75IcjT8ZhLeb2O36ub3R62OI-fpNEaGoypAFh4-pa_zqcXu4HnY5ZCl1k15kVCSrNbqCgBm7EIyQchXbgENtU-FxKtIW1tGUCBZW-r-5YLGr_ShOFU_7-6naf0Dp_GqDVIw2EfTgQ5WMPhU1HiswQ9ooKkQ1NXzIV-Y-8Mg8ihwqYMV0ELFUBxeUuTiEjkfZ1QRd377qYLITs_dUXJ9HBAaZH4LS1hYi4EWS1Nq1OsAfk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=dfGYeDztCA878fgLpCV_WtlgWIJLsZxEkBpt7AV-yA-OtHcfVPxaaND5xgVMb55igZG9UEji2mpYQ0YTECoWaf12yOx3NMbMACWCPZfhU9ZmPNqT0wlg7MEOBcBuN2wI3p_OFzgKeYchvxbYfrFXS2ziC5zQGpu5ulagB-pgvhBtMqvSmSXF8NNxnsLfMQt9psvgridnw0c-F4E9emgVMR0jpzuejMj5-MnZb1wxQ23SLHxuQic8zXD3VeAb8tJKTpWQYDOBrnPVSu90nt17i-DADKqNA1qDPR_EEQhoZRmzjTOuDB10Yvf6cUojQ3md-wfSqUc-2b1Vt0lYvId_2me2kNmawh2KlUFEt-Ru6riNttTxgt6NQuVwv03L6fbXLCexbJUC3BMM1emQG8ypCncPNgak_wNqjcopDyjqecy2Ig8Njb7P-1t6wC6JZD75IcjT8ZhLeb2O36ub3R62OI-fpNEaGoypAFh4-pa_zqcXu4HnY5ZCl1k15kVCSrNbqCgBm7EIyQchXbgENtU-FxKtIW1tGUCBZW-r-5YLGr_ShOFU_7-6naf0Dp_GqDVIw2EfTgQ5WMPhU1HiswQ9ooKkQ1NXzIV-Y-8Mg8ihwqYMV0ELFUBxeUuTiEjkfZ1QRd377qYLITs_dUXJ9HBAaZH4LS1hYi4EWS1Nq1OsAfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA-fumRXlht4fcRKCuQbf3w_00Fcu4LyNN6gwirKrT0xPuVDQQoFq5YHi4qFp8eRVkTEhZMzYbfmfSE63S7nGT-E0GmO2toGglXlA2zOSI7V1fIwT-c8xqlqWmKrTVolOe12PDl1B836SKvNbxoc3J2KcWE6kgUIuxJCQZ5RXIvxV1kRDtKH67qniLJWMn6UPeXF78QhDRoAycK83tHEVRu2AOjq4XByqQOXq80cCYh3OzQskxHi4n3HWaZm5XYw9q4AJsWAjRKU6_xeSFQodGMjdbGIPIdtwTn8bSO-B7F21gjEqoxwrsk_7admfsu3SLuyYpCOjHbVqlR3necNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kvfRpi8E-R5IsOjZ0X2VHA3bMBHo5oRLyUzqWVr0k6Kv52mq5CagA5SrcXGWQHKZgiDnOfS3kvZGS7FerNAF-W_Wd3hudES6C0FVTR2FP4EAd7BfAceity9oNt9aMtJUyqlGszpb74r31Q_lJeh7OyKQ1NVSBXUzSI0Vtg1fvzcfhSlDr5Nkc94xtXeuFmEIBZtN8FiGHWLUHfDBdAN6CusJjh0AR80PPPSLV-o84IG4ooHQm-w2F05xjr3Axit7bePTxMgK765nlO_AG0iWyNEhjGToi8lXEIDDwQ8ouKIW7OrG52LoUfQRZZqxHMHF8zxtXUVrw-kUwtqvOQ-IYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jm5mhZ_dcpChVlwfl1uSkUJyvAooKFCCaTd_r7Jip7RI5mF-6hjzK8Ip93SFMMIp8E2TwtZDcHx32wG9Gs72V5T4ntkSiYs_oeJJX5eqvVnVeF0Uys2PvQZ7BoYJRqoZ_LmBD7aYFneTt-iAJgSJiC3jOfAWfT1xr-WyE6tuw_Jp7ZK3APbxY3nSCzLH-GptRhg5AdQjC1rxrFXeXJ70CF4Nk0twFVdpaFgkmRLpKDKOFGaSwlz75TNVulxUro4KyxjgzsTkeZYrIsrNqWKY30IQ_dD4N74RrOZnKejdPr5Z-OQ8sI0-OgMGt_90VVfL7Ojlj1Y1TV57MVBN_KWiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=fz1PKrojdJuzYq6wLCmRboUC1N9cVbJYeq8BeBHdoj8W3fXAP2ws_cyPvviGQ0GJhJMYy2PGAc5XbkylrY2_gzF8yiZ3A99vwQKnyVnqrMUnDn9Ax1CU_7IW0Omsdd3mf1RyiATOPMoY0SdLRPMAdduL4u55yi1_eFpNn9qfItAFN2UaYhc3_W2-_iFBTJZWXDTAPHmYmkrG_ZcSYrXGH5xCF5RMWNNRABd0u-qJiIa0AFVIy3j2FFBCA4WMFnNe5VmoMUf8nGt_TXEjSJlvUH545cwP3csZRrd32MgnF9xwGaJsVqDjFuTCaKaOrVZIUI5AanTP8pl2pXJKWfo0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=fz1PKrojdJuzYq6wLCmRboUC1N9cVbJYeq8BeBHdoj8W3fXAP2ws_cyPvviGQ0GJhJMYy2PGAc5XbkylrY2_gzF8yiZ3A99vwQKnyVnqrMUnDn9Ax1CU_7IW0Omsdd3mf1RyiATOPMoY0SdLRPMAdduL4u55yi1_eFpNn9qfItAFN2UaYhc3_W2-_iFBTJZWXDTAPHmYmkrG_ZcSYrXGH5xCF5RMWNNRABd0u-qJiIa0AFVIy3j2FFBCA4WMFnNe5VmoMUf8nGt_TXEjSJlvUH545cwP3csZRrd32MgnF9xwGaJsVqDjFuTCaKaOrVZIUI5AanTP8pl2pXJKWfo0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pN9jNnpvnmWghgGT8P3Lh5h9UIVAvBgVQOTvv06cCWm0GWzKiQNzt-AyJi8G9eHYAv12NXg-elgnomgnPomSQi-GDmT62fPP4Hn79xSo1NG1awkmiogOi0L9V48eXo0N97A-UTVxPw6c4ABKLRWMYIsdvcNBYpUDpJbXYc_AZ_DrihcPTL_tcn6o2nga2gCIbUbEIgflQzcY56aab5ZZ1MsmcU8omzyFC_rDC-3vZp3NSthWuqDke-_0UDHbdGNjvJdxLRUef63F05Y8-z6JZPwWX5dGirh39Xbgd4bJO1VBrV9cHaJmH6i0yXJzNtNjK8X5NC1BQL8O0A9Q97spVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/os11ns83SVQ9Hf2FaE8EYR0iHpLgN__iyUs9a_qhnH48vshdXcSvDun1cSkvppnKIi0-skdQ7GuVYibXEMOyshfjqf-ugn2i0uGRQn6_UYkeYf1OFYzRqixD5esyREsO4LS5K4kL0IKO7PhDcyzb0cwXrBJ5NgY-8PpXJEZcT0gntMYDETDJXrh7NYHfmCYff0731X37JFXiy7JInZfHcff_7Ria0bYC4u_Y0NKaI0mlrIWf4jAN42tQuAmlE_Gl6I_ND3mGvRMZ-kFjIIUGI0FDCMIovWZers7QOV0A591HtpuD5TRRplBKwZwB7scrlyaviMoPY_I3SQ0MF87dkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UjuQ-r4109X6-DmXXUHivZ9kxJ78h5kvwC_Eao8Z5cDy085OmqsIdZ8D5epZxBmHsYglEBCfwbPHKJbabMFQZp251C6_y61WGBT9ktcssPBZ8EI_ZTbOuD6N8wGWpLI1gOvqRv6xZuKWlnUMRxg5lUdn7IKi6GP56cqLntFHBe8HqrCcC3PIhsfCvv2fNRxhhmpAPGYmGTybfEsYBQbf61_63fWwavEevSeRnbwb3llRfgHMREt0VSRNzbd6tw8_sZ_ybqXAVZff8uDSQbDMpUGBvvAgYdWABrWp0MSI7ETciz8BtUw8JnGl4ZNv5v83ZBhKx7zZOS1cZaVNGK4t7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BdJ6JS3s4-grc2L7MJLa3OjRYkUUTt25xCCHVR53zclDxW6oyGQDUu7Oir7Xc5w3QN4HokIQ2zqlWKXG7qLShoyXPVf39Xah4NfGhLoY6yW3t3rec5fgEipfor_xYmE-PRIac4MuYPWX__t11mD5egv2uVT4fOkOGqvPXgf8iR1OCUiEV1T3umTp3965D5VcH3wrydVuOSDLwPcRmzIDxQhtYbAiPMytTcW7vENDYsamla8zRd_H0HvdZMpTB6YA8ZAywgtO2O7qa4ZI7RWdjge4MlR5qD_yCahFmuWsP28n9NUcrQ0xu31qzthmTG9D5xFp-YKwyuE2gcHisgEF_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQyoNs6_8EFyZwpXSDRZ_4gn5BQkEnuIAtf83iXmIgTLF857QA3MH2bd8dHfQuRLz8HfaCwlqBeG7Qx5m2932cL2hLfs49eKrCY9AdCRlxAz4auOyFJp423oTJhsxna0C-1lXVvS2srmtWSh9Hk9jUUJ8wn-m3LBsiXqFc0IhpbV6LaR1prw-60RLYNvI4n9OwdX0NAWzMmmLyw3ZSC02tSzMmDYC2xajrxTqQomPIECgqvnrY9hCarlqQ8m86hs9HZijizd9e2HUsjELhWY0CKXbNhMSbCWd347AbQub9FmebEpv4n4EmEqryOnNJGwzSs_7vfyYdHSc2GQ8o_yYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cG1YSpWtbtP3hW61mgqkjgga080HbYH83N_FRr26jg28Id4KCVvEAPcU-T8Nza4NJHTsZAHYxIz0KkypS_9XbUD1Qli1bX1MguRZBxUR9UrJTZGgrRuvmPjCBdNEcvailfHBo-ewVIAxGD4Fu9UbGmArt0OK7xlVwaqCnpQaBZWtyQOuIAYOda8J91yA3zBk3wz1BKA_xtzFFpuz-Lh8U6Adeqk_JUkCQ9frBR9jNNawphDQW_qCa45SEPWui4vgF3PGOIeLGb8VmKq3YccZpPOSxcfrHHL0J48IX9urMHJhKv2p7HU1az1xmI08MqnhV9ti6cyFFhLHvfCAf4y9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l75LLRlvPf8hzmogmMVz8_GhAKwLn5YpS3nTHBx3TrYZ_NAXdVkFJsNsABEzWZ43cLcSc5YIyWOJ3ppS6T8deRsDJNcJJMEACjuUCevF068KqfGaiLpRtg8PAIr9ZakpRlEGO1M3H5GIB0nxN3qqFuVHuYpEErvwedA1lJeEcN9hrPGfUuCfi2-Si5YIjbVlIgPJww419rsKvF6JDRCK7Q6VeKGZlEDgMzcsOR2EZOR9qBPqXbj9idzUdSWa0AotgND-bpmWiBDMZ7Uq6OnWMSilmBB0jXAtekTZKdBWMrU0n0ldxdlzLUY3JUB7_XsidM23SWiR61ED_kZGc__QdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UwghIvnacT674etRSc7ClUlosJdhsbkz9UJpgJhovWBr1cuBJ7uSD5IzzBH9lkztyRNGUqf7zxb5wwg05zBs7Mdc8lzQDKOwLWy7NVQJNox6A0jZk5OiqeWSu76E4wnnu-O9w-VsvR27XVMvdnH-tHVV4n2VXiArfcLSVbdvJt9KRgmG6IZdXHF733y7udgm50W2O9EOjTkZC8zrNYiwPEGT1kgsR6Chz0IyZiIYk30IN2F7Ac_8ypwe-K0Us4-ghNxEeQWi8qdRUn_TIKvTeUUNt8HuVdEFgTWDxi-CY53bP7CqfMC1SMwCDJmz283Pwsfu_TMNXcjithgsXJ5BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HtJ5uIDinILsZT33qGVDiQTl_3fLW_sFm69-W4aQjkiUrAGvISpk2qb3fYeO5B9YrPk8xYRu0YVneCH7LWsh_BwLYrroOLP_UsD6kwitToPOS_muLPlmvadNPfLegsniOu-R3dzWRqBWVSt_HrQdLbMH-ZGDBHZZBytUYBtnpatQl3y4NTfWkwcr-W5o3QZ4-sZkHmKClsxja12stiiFQ7o0G9hH_CJ9MAt_ulHCwYeKcmPtB5KFqX5kG-1xLsrGOGwb0GVsXLCV7f2vXdJ6IaylQg-VCFPmOk4XZ8BDf5aU7U6La-ct8EkoIomoP0VW5wQGi1ZM7Dcdu6ZQlB8B4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NOdjjvAD_0okWTsYvXo_aozK7JCh6Oa2OIkSIwY7TThfFL0FKRJPyFzra_5gwHFqNMvO9HzUxh7gT9cS6Ba74sg8xGUlCshHYoFWk0oztcVjbiqe0omwz0JstkzGlj0GzeZmk59LilrM2Buj5cJlIg7IBtPCNVAQO8N2RFyCgACuXoXsVR-Xftg78-jDaEBjk8ZJ5irTub-pz9wPDBF_MZtHaPbauI7TSnMjZvxB-pp3ni8TFqvXoLP8_gE8O1K9WfW-OAzVPf5Sws0zC66U1_aod88a7b9WbNpi4AO1D6INF_DSYqaLjekBf66Wu6yQxUrVx3aW66HapjRObDadcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dbvBCYC5f8Ur4c5PKKwB0g7k2BzCkHJX8WMZlO5l1rfAnT9RhKhIybZAhtzAe-M_4vHQZF0QhScFu2ogu2heIVi-_aKHn30goQnve09abgvw7lDdbKbhZHPG5EcGjtwLFVo5F-6YEHP8KY4_wsXjF1giKudoFLY1hd-_d71rHUNtd5Vx7ImcuUGpjdVadApZfylOGvjx3mxdhdcBUyRZvUMz2hX1_5XOlwIidk86CoajIUh0bAubfucxJTXXJF6e3QEoWYq6rWsoVSsM8R4Ew680mTdEA-yqVWOlfuZAAvh4CGAZz89rOKe5unMRGU-HO3Nb41ZSl-iseWs4fsBq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Va-rlbBWsHV5kA2h6bX2oQA9ktYkI_A0ncnY3wfs9agEFS2ph1OVBwfyaEELMZioVlfetalTBxbAx0Ml0Pf2vYbjkHW1zG71tpoydW0Wfm7dmg9I7zcnNlhjKYcVyEwHFnkuZx9_CwCkvD-OK0xk7RuvKf0mEPdA7UF0EZ_ZnGZN3HfxF6w6RqKcjF9N58iU9KN-Q-oB2UbXpdzLhne5FWTkgw_Jv6isWh3hoFKwZ7xsKLwYZFlHicvqZFIdHT9pp8XXOS1hcX7_wQFMzJUhW3x8cndCfF4Bvx1ygyPpDUy-5FCGYLJ2SzAqNzXQS3EPonz5MI5Vf8iHUh4oV_FoUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=b2Z1szusDqpsAJ6zur2B9FULzk6BJ71BUjKZuvCiYu6hmiLI-JCP6mlpCFhLWHAUhC_XMu68egmJcovjMjljhH_lTzLMj6wkAhItRc9N7M9QbHVj__Di5ss6hTN6Rh3wZtuLypjGArt16lotH-7QXaAXFAuDhHwhS4jZW7qxeLgYcDAhpBHkRzoPeyi63o8F5xVqyS-5FAFHAVUXfUT7yDVjMHA7Q8ADJNGgTEIRfnmlsJ67B9Rt9x3win7mOynDo1ygShCt4aKfgDhMjmggE5Zc7vTlW8BFgoYeE8x5ABIGbhcEGCl18E0ZZSuncwGmaDRdRpMrHaYYV3_ppAPhYQKp5ZwjsuwTrDBfWYR9bn07cim1SnEmvlHW6D3qNt1zSIG3xy-E9CWoekqCPAMJxzW3l0ofWo5Gn9lSKAlxSQlDsY0QNoBc9n267r3PsHa2hnUXq531MmgZQw39Npvl9pJV3E8qI10PsGR_7tx_a7FB_PHYvxiEk7N--fmtu2P2BrVnRvChyzzR8TrIoPA8FMkJsR37drHQwOMnVm4MNb3IpuU0oG9NwNJJb4jpekWFzE6ctWv3h2oxLOvJfBs5x48uZJweENv4Kpzsq0fLIYB9X23BdocpWaQ4OYY48SokMqaUlPFKUTogDqC5ORd9ewlIdevjrMZatcuhzRVtFYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=b2Z1szusDqpsAJ6zur2B9FULzk6BJ71BUjKZuvCiYu6hmiLI-JCP6mlpCFhLWHAUhC_XMu68egmJcovjMjljhH_lTzLMj6wkAhItRc9N7M9QbHVj__Di5ss6hTN6Rh3wZtuLypjGArt16lotH-7QXaAXFAuDhHwhS4jZW7qxeLgYcDAhpBHkRzoPeyi63o8F5xVqyS-5FAFHAVUXfUT7yDVjMHA7Q8ADJNGgTEIRfnmlsJ67B9Rt9x3win7mOynDo1ygShCt4aKfgDhMjmggE5Zc7vTlW8BFgoYeE8x5ABIGbhcEGCl18E0ZZSuncwGmaDRdRpMrHaYYV3_ppAPhYQKp5ZwjsuwTrDBfWYR9bn07cim1SnEmvlHW6D3qNt1zSIG3xy-E9CWoekqCPAMJxzW3l0ofWo5Gn9lSKAlxSQlDsY0QNoBc9n267r3PsHa2hnUXq531MmgZQw39Npvl9pJV3E8qI10PsGR_7tx_a7FB_PHYvxiEk7N--fmtu2P2BrVnRvChyzzR8TrIoPA8FMkJsR37drHQwOMnVm4MNb3IpuU0oG9NwNJJb4jpekWFzE6ctWv3h2oxLOvJfBs5x48uZJweENv4Kpzsq0fLIYB9X23BdocpWaQ4OYY48SokMqaUlPFKUTogDqC5ORd9ewlIdevjrMZatcuhzRVtFYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQKODdhvlY4-Op8LHcqo32vaVXzsW7FoErL3ToLnlGjGHtYqRgQevdlPdkRUKClEurQUdu8LZvDi1-_4_hDhq7OkT_NcxeLJ7po6MKm4d_ZBGTC9Q8JdYWgSDqpYxRBlJTYd-jauKwjdrBFzQICxFKQRCkPmhistbPThQ5ZlIGFVggQACrPB-BUhY-VT96Ue_hfmH6zzQf6WujPtUmbYqQqdkK9xkxREgLGVZxQHSejZCmSS8uocOpiGl4wdEY8vrXMo4EUVWVYxfvCzR4lKBxYxtY0yGI6sByqynMHd7QiN25dmVpia2CVRyGR9HT26pxA-S5-AadFERIFWOK9hWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yb4z63WQDLPTLJdEB4xsF5EO5A2nzj1cCHavY68ruD-88aAvZt45m96jHB4yiHVW89YMu44rdld5gyciZbHGEZo8WnrjK7Ap5cAIbF8CkMho7WBcNCVq6cMX92M74JCQcfTBNBwp25CWSM5n5cEym4jw1ktf7EmtyGqShvlMZ2q_2NZLfbuds3iqnA5GDljYH3f2wwUdQ1VS756DCsJIutey5LWC0bwITsF6oOAoI_CtvmXWk2Yc7bPS_hs3QWvpuRrESX-u96gpjSrsSDy4hUWqhhUETJzI95MNf3OrdbCIKf3CdbYwBxaSeHd9kj__rGCON12plANi_yyws6vIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vByKAFJekRRodfCP4FYR9W9JWisCUoWRn4WXuujYb9lNhwdkR6tg_4lZmn4umkTwzccP4qSYIATBYhDHcLAK09qAcIGbgMWruBHAUPBZj7JduBgNWJibp7orGcWVOI1UY6QKtujLAj2E81mdLcP5ahXLr-Qx_qzBYwCP1VGMBnCfKEqzEkmdE9dk7cUwTGamp25bVdvwPKKUKZvPfiqmpniCTcf-oxShlIyieVhL3lyfiYqQiT1FJEyQwk99HsKIZin9HWre4tC2q7UkHSXr0o6ripv36GNZPb4NazmIft8f51vFDz8EOHvxEb57sTUL3S1vW6nj1gXhGRlgM5j38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-wCJXaH54aJlT9oTGA8csX9zzSgKvIiZsODoqMyORV4FPXOLp78VXbtTs5bL_eeu0RxAThhdg__7CQ0X5b-0BpwIEHQYiyopxEeDNdJLaWZD-VXZbBxEcQYTqPskOqFussbzvUn982mjilyY4FrW6N0ubS9lBVPPeyqfXqr2EhnUuz8lSITF4v9x4oQWQTMl8L2bx8JQmS1NnZwYmOivBJMqMxYVjMRHcIY7whKEtCicXtw2Zui479aBYTI9m3Hz_lvO22ISlho3rCvxAI5BJL6cBHvPeHfTNMZhWA4JsDJDLift6_LXIEiaGCdt3-VoytmdMMcJCv-T5G6ljfNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DvKCZRv9lkCaQK-UX00NkkfaE9OrWo0_wO3R0BPaIaXJS7lj3NaJnMJNi88nBcB46IRkJsQxsaz4DXw-EvWBwBmu-NCG0nptmsQGgHASjnBBe7AqgexOsV-RtCtHhJLsa_PgY3W6k03_Pb9hcZfbk7bX66vsmsStiBHghaMVjfECCU8V3rjh7_pUJvULlp0VnbZYWeM-alxhnnF0SuJvlfCnzQRBGsDNgoJQY6Ji689S0dLxp6lbEKVC1C2AAO04GhJ7q0vUVtZeVwCaXSA7-HqARZEmJ28lfW12gAhDqGIKSlUI0HDbGYOADzYl24C_lSZ7vKW4Isd0lAjWsJI5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
