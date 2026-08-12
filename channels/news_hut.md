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
<img src="https://cdn4.telesco.pe/file/fqcG5RfpsVYHIqZrI3_9H4bDSdhiTiZg5mSHK-bHT9QE8ob1bFnFNFRMfguH-WLyBjMPtg5LVYKJcT7r2T0YIzq8iXz9V6CykhXiP0QkJhY9_STBEqrXr-nwA35b3sWLggBrHJE5WGRJLDUAgXsisZsHu7-cBvcP1Ns4ZfznKbAv08Vxj34xHNuUfVzq0Dj1q39lfLwSe_SsSMeZqVOIWaiWHtLQryQK-RxOqflpGFFXLj7yDiITIU4w8q0Pt5i18V6KgYGJaejFo5fruS9otrJIV36y-G0FDhc4vpb0hS74M483R1Ig_cguJGlC1M4KZbeND3eWJV3epF6X0Onn3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 126K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 20:55:21</div>
<hr>

<div class="tg-post" id="msg-69949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4147c4b4.mp4?token=CjRTLuhLMTfBpjdhhbpFaoYOzVe54GGIP3dF-KyOV0DFn4VhqHjUa2HxP9uK82ERv8rv8R-raFTyOTV0fGsNaWM82UgdOtFThKrAauRObhXEGT30mECjzhb74sdR00TcUyFDj2RIyrmWZ98KhhNBhDyRIisYRG6QdSyp8ffuQp9ydTvMIzpfV2qZdcrHUzbwhI0XnUMNCyvUcujgY_rj6T9YNJfyFX9D3hZ_4hoLGpoFXB9fcZq7oOCb-ShoqlO-zD_5DEgiJLtjavG7qi8nQSGWsu5rLKHe23y7FlR2PGkUsQDA6jvsM3Uh3YUukuH6mVxVovyrSNkf2Rt_Nf1rEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمود احمدی‌نژاد درباره حسین طائب(شهریور1392)؛ «مشکل روحی روانی دارد»
ایشان [طائب] تعادل ندارد؛ همه مقامات کشور می‌دانند.
اصلاً کارش پرونده‌سازی است. از وزارت اطلاعات انداختنش بیرون چون دوبهم‌زنی می‌کرد. باید معلوم شود ایشان بر چه مبنایی در این کشور کار می‌کند.»
❌
حسین طائب به دستور مجتبی خامنه‌ای به فرماندهی بسیج گذاشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/news_hut/69949" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4396720d1.mp4?token=uadUvIq8t0YjiADglF8ghWaodTdD6Tl2Hg_SjHM_sb0r4kE3aeN4ns7wFhYlTnOvXA2hEo0w-NDOpfHLEfSf2pgdI4lZCs2NU2pbsO8yDNCrQYLhBtwh_7DsHh8uws0PIYFJl4Epkoo6jdM2gETvayouo-V05WqFWTGYS_RaT-NjcNnVzClfj9JHbXu-jDr9HuS2AAkxLNsdUQzNxhgpohwYoukdGhHajvLuArxgUbzfbO-3-rZzc4XsY5YuUTdkTjFy5zsMP-3As7-tOSJj1QugvS35JUxhbEdOzXNrPVDepRY03FeglAlYNsGxUf2RADumbFZi1JVSkw8KjjsbXGWmiaZF6PAaT6Y6ElR2hxPHoLIpdYfFiy5NY6SXDOqd4H6L0stA-AWrq8HrP9YxaQdTW3b06pXiZvzrSxfdfhrNPKVERvK-4qVgEB-Ih7B5VQDhJdx6nW4H2TytJdzNc56nVUNDuVwhHAQRsAvO4zsdxlemavJ4sJBYbL81fUOvP_j8nCwACA_UkVLqBaEp4yrBeCaMLDM6lU_JRXlNxMrgDTSPqv9HhNvbFc5Ri9ylpw5pcAxbcwc1mwneVaEKaGDAWLp1xDA3UUyy58Rm8aZwdkPoKZQWsxTBEteFPQbTy5Ud3MvMROzDydcPpNxpoprlgh_bQHPcRj8JO5QkA60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش شهروند اماراتی به شلیک به پرچم امارات توسط مجری صداوسیما در پخش زنده:
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/69948" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=TcYoQtXBqJljs8W6exvvew_Dw_l473HtOXLFn9g1OFXiRWE5Cmk2A5-4pI9PlPUjSI4ySya3zlp6Td5e7MWtdH9qB5ucQ24O6_Vb73-KJpkjkg74DZySuA3mXdagsIsmTc7upEn8sYdOKkX4uCyqwgF3WTiIQrohpwLRh6EgOc59O1znxALPKkb3YK6T3rRIPrg-OmNlLYr-PYhTBLB-pXrLGDoKsTSaqLiFb6J1mG8HvPd6zFZkWLUCmAJ18Mg7bMTy86mv-TENKB9NIRjtw47yLYxE8RAC_omxqu7UsSEWho3UYgRKsb4OdiB7clppuN4C-TOUbnHFc1ayUMPjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/news_hut/69947" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/news_hut/69946" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiTMKJ-i1IN51NzH6U-yk4IOK-t658PnDdtXE8ADFeD3Sew-ibwCcEmGge8hV_1oR92o5SSoojmFPKc1Vlu7c7QbYXx-1X3MjIQIN4rtHN-gcW54N-4TkyaFkb9MDz_eLarnjwsAPOWuUrGpmFh5pBqgyU-4DD8ntH9T3pmGIV69j59a5MOF5CnGc2VmKJCNBjqwl0CkSTNdDxlhFKZvdhWoYMit2q9fs4xVFSAC0shKFZBvZijtZCMOJofbAfS9PTXTsSfOjutSo0JsVtOA7yy_NGSqJ4R406-avJmGvF0TiAD1Wf73eEReacndp1v_F5cdSTK44ueIMPOx64EXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/news_hut/69945" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et06YdsKblZNEbnI30xcjHRLCeHm-D7P3InAioByjMX-7Mpwe-WrsN_pHBFlKYx3nZRIxhiQtp4zvYzNfLRvV5Ztk9ECYygL19Y02xktiNotQj5-hVLl89GafYrvmRQkJUXZvbi87v5juynh-2nFngUDgQeOjQpyIpfPncYooQbLw4UiGHrU8-KO6uxHpOaFr8HbqONz8Ooy2OM9b_Ko14_PzdyUNjTIxibcU1ksj82wN8yE13z2F5v6Ktzs73-6RD7resQ-2TmbGM8Z2P_YHjV4dd329UCIOMAKzS8XQQ_5aHehFuaE2XOB-xlho6P6d-EIVipH110uwxIE-TSghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
همه، محاصره دریایی ما را «دیواری از فولاد» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد.
آن‌ها نه نیروی دریایی دارند و نه نیروی هوایی؛ سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران درهم‌شکسته و در حال فرار است و وضعیت «رهبری» آن‌ها در بهترین حالت، نامعلوم است!
آن‌ها پولی ندارند؛ کشورشان «از هم پاشیده» است. تنها چیزی که دارند «اخبار جعلی» و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر هم می‌شود!
ایران فقط حرف است و عمل ندارد؛
دیگر خبری از آن قلدرِ خاورمیانه نیست.
ستایش از آنِ خداست!
@News_Hut</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/69944" target="_blank">📅 18:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265374f5d2.mp4?token=Tjj2etU0CV57zVYau9ww8HIGMtbxSeA5kHqyXsidmm4YKnNk2cZpi1h-03v2Jy_HLclE_BUfa0gfnsiOLVyTKQL9brv9U9YZJF-nPrxSlrpDID2morVkML-FQtFSH7kIyG1Eypv68Pn5sx7DslG8-_teDvyH_ZG-Ytiq26_7qUOjNLQ80PFyUMKb5rLj6XI3pbfxiRqtNf6V9ymxoOb_rusJS0TlnUPTmgHHd-TwoeP7IUYcx8awZ87hnhTbkbk3MWDBiJ6JQUjo0df5k2TT6zHUR6bazyKSCtD9RoX_sehbKQIUAqTLNlNueFV3QoWt0zeL2nMIOup4mnXAZaspiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
روایت دختری که در 13سالگی به همراه مادرش از کره شمالی فرار کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/news_hut/69943" target="_blank">📅 18:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c105f96b5.mp4?token=OjWgwcuzvMA9VpranliBrBDijRD_uVMocpNZP8vq7HViKblx_Z2fFSUti-P514J9KHONuVd3MNRgX-LSs7DNBQur2sZ-NyKCfmCbk0FxPhDrt-c-OywLbLIENDDqG_PdOHT7Am6ZdKtPlCQjnp2TA8vMMJ64Nd9SZl1AJxRrRiTzX3m5VcdZbJCvtv9vTjbIMfhQaTb3a4SLRzO0UWMmRKHKGr5nIJ4te41NQkojIHgfyUV0FrEDNUbVfrkoYr1BSfROaG2_nHoPUvZtGdmIOA_tn10wrSdNDpa8bKDOVfDL-SjrDbcJzvljRhrCiLTCWh0ez0Aodow8x-ElZp5tKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه روش فوق العاده برا تقلب در صورت آموزش تصویری
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/69942" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kff3DGmIM667V1c1190JiDNQ7YEZjWrETCjyA6Q_2m53ZfvJd69MeeXJWSauUXhS3y6BCiXs6h7Rwf6dIPuUL5e3Q2HMz_fgVTTntMZ56TRbcgtAHgoH2aXcHeDcaqQvWffK58x82zyfKulx5bFkzRHCBGMObV8L7zLA2cEM2PhObjQExwd2c6kYC0BFCtVpHan6A0UEJ1oLnVpFkT8orUL046lfjByi1JX38-AjwP2fb4BXJM61OQLIyaDV1E5dowFtzcznosADdli5vOCRVGCxJ-EM-lxfNWhBoaHNVtqHG-XdaGpYip_XYlCABdafggq-oE2Dx9O7v1tZ24VAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vct1DEK63YEq8hVqrmXGLoU0aqtIyoaVMogkFZNxnHbIXa-vojxxGRarV8sRheYViJkeKvuFuLZX6mjI-7gV5fFyc1AtbKnaqqnJKWrmBrRGUoO5CulBwmrs8me2QIGdJSf0I5X_Lv8J88aU9qhIO9ocVhwCv14Y7bkqbPfNXCFWuwjOEhOA_74gUlKheapY0fjqRMDrgC44l4sSt9hJ3PVqcGkntJpjNwGBbHEU5WhAuLGhphPbzy66kdfqu4cPRvf4g4p2Qg2KqXjNtyw8MS6-h6JJHbKIyUrmzAcL0vpH0u2VTlFp-lik9N9kZLhA3TFZtY2oFDkfGdTINY0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCngHQYJ8Px8QVZzaC9dqLFTCY3mLChmHEfHpit-3YQPbsBYsWdJB09e2BeFQIHMh1Em-k2IDxj_4Sl1PIK8MSFz8x2XQDGxb8YL0z_QeFmTCfYeL0P1TvtPKie6P9qWUv6KBg46bm2fgz52Fa0yX_wyUBFa71hiF7HFWCkBDrLAuLEwVir-WfjHox9R480UXfMKhZAh71RkFsQ-LPMAEB5DUkpkF9FN7-mwhve-_azG8PuWNQtCb4ksMfOhbIfH7N2haOkX0LeIaleocPzFXC8uDCWqOXs0awpsmZc-xd2dSQrA3Fl7xbRcehrlLFHHHD_CpnDH7_1nWclz8FLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=JCkxd3lQk67uVs8_fKWVWAJhTPSbeGiIGSiR0r7mksDJWQBBHKnzXrFNXaVpegcelAtke2Zl2vKJgv7R04Tzn65yE5ghAQ-phC5U71qxeRuOPUrJNW7-oZCzyJxpcMgjaFIeMuqa-CyHmmt4RyXrf5SOHqlQgLbi6Lo8huAm9leeIfSnDoek5o2Bm7gDXaizs2l9kCpdM61X7mcpxOiG1F0Zmmmlhuu84ylaWZU3PPTVENdlyicguC7a5N08yuHzCuzYGiqDUtNaOLphmld_2X1RDorXOSOHVtDqcepcI3SSVtzhBkFTjvx9hl4xCADJ9GW8c_9ipqVZJkwNkxALCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=JCkxd3lQk67uVs8_fKWVWAJhTPSbeGiIGSiR0r7mksDJWQBBHKnzXrFNXaVpegcelAtke2Zl2vKJgv7R04Tzn65yE5ghAQ-phC5U71qxeRuOPUrJNW7-oZCzyJxpcMgjaFIeMuqa-CyHmmt4RyXrf5SOHqlQgLbi6Lo8huAm9leeIfSnDoek5o2Bm7gDXaizs2l9kCpdM61X7mcpxOiG1F0Zmmmlhuu84ylaWZU3PPTVENdlyicguC7a5N08yuHzCuzYGiqDUtNaOLphmld_2X1RDorXOSOHVtDqcepcI3SSVtzhBkFTjvx9hl4xCADJ9GW8c_9ipqVZJkwNkxALCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=q9GBT5BiWp2VCYUqFSMRbsBbNF4eI-aJy_MujK8-rasVncVaSb5jN-JCOIiPmbg6DOHkUlIw2PKy4Gz21wyc-KQieC24f8Q5vUn1FIV_cthbGMIONjmlg6i7OEe9IiJtQ5Lqjs2xccu2u-l78XQwWJiR22Q2kq457PZG9zwqRQ-9Ss8mJJiI7sEoEZrPA-5hmLUyeQ5iLDdovw5mSrSWxi_T_e2FCDmz-1w_nd1FtpkxkOCxON5ockd7_VGroosw7deu-PVdy2KXOMjniSLZ1wBdc638Zjun3d2SMb8_6AZz2UbEPVYHBQ30iBDul5O8lGpPw_CiFa-Lk91B2ctVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=q9GBT5BiWp2VCYUqFSMRbsBbNF4eI-aJy_MujK8-rasVncVaSb5jN-JCOIiPmbg6DOHkUlIw2PKy4Gz21wyc-KQieC24f8Q5vUn1FIV_cthbGMIONjmlg6i7OEe9IiJtQ5Lqjs2xccu2u-l78XQwWJiR22Q2kq457PZG9zwqRQ-9Ss8mJJiI7sEoEZrPA-5hmLUyeQ5iLDdovw5mSrSWxi_T_e2FCDmz-1w_nd1FtpkxkOCxON5ockd7_VGroosw7deu-PVdy2KXOMjniSLZ1wBdc638Zjun3d2SMb8_6AZz2UbEPVYHBQ30iBDul5O8lGpPw_CiFa-Lk91B2ctVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDuFZoTpqjGwTTwMgsQDdA5h7EhYmmxmn3nSiJWZTWszCNp-LGzrU_frpxsrMQXzS9-0Pc3Dyf7YvomjxOb9IzCRims1dsvLUqn6vFneho_UJKVSEaeHViGDIJV3J0MIHs2PH912OmDiPlsCskX3Rio3OnzSRKTK1XunYDrjDn7zq3Vee-sEpDqWGlY0u5DBOEV6ndmsigtOdE-JlAqAsB2uo-sHz7f1OopEPAFTulvSgLa3OEpe-VYdrdLxTiGq5J5YeY5odMrFgNvz9rcXc-NlU9rtzWpC7NI1HSegQh7aFEroML_WLUimYxbKakx2KUV_LZyNXBds3kWh8yVMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFYFA6TX-GHFfrL0X_FL-HkG7dxfeX91pgevZNM-SAjVhOQ4-AtluzYphOVHXju8O4IpEAQaWF_m-dNxUEa-O_FKW0nG4pBc60YW9_7VVd8lfZMpwoGaIRX6wnCrk4vo_rz99c0oKqZafCxHDzZsU7vvNL1vLMfCsQBlYsM3gcMEX65nvEnIVAd4JPR2Qcq-pgRAzrq54LEaCXB9-KwtGdz02UaXWtWss3bM9JMoyKg8of-krDF2qeIrFa4tkG7vu0bcce3W1vHaCkbThIREdemoMm2c6udhVAkUDa5bQzhoQbNpOjHTmnH7b5QoTl5J5Hydi62ZGMt-x6Cpk_1_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=jbf6UjfSeKJvGQOCHuqWRzFmPoQT1CsYqIrYfRW3fk6iP91mP9di6oNmoU8gb5jAjRD7Sep6rHAV8YoOFAr8HEgzmbfnpbDSp9tyksvs--TyehrLkG-P9gs3AkJSfAPtjnnYBX1F-OzloXZt8AGo1q5vlyz6tMhdLZv1ngEuLIU03JGdcBijBjeC4memUDnUmdSnJvlnbX5VYGAMnK0gnLCXHqDAUeNtb76EBvmpovZHpugbs5w94WQD5eyh-G-CDXCUogeRLdBGOX-Rq7djFparmfAKbAR1mMrBxpkKX4NatgbhRZMD2iFsJWcyiHYyGo7s-6_wLJ_1bzTcqpJVU0siAQabRwmSh15DAyAaOQRhnhx9sjnAj9ovqM3O-qSJAObHEB4BcYSnigdysxQ__ZRdW6eGKK97AT6RkAl9AdtRw8MmkxhKA4GeJgnZ9si0yAq2-uDFM_31-71KNm31w95s_fZbKOOzF18Gxnt4OqOYxJLj5YWoLE1fs0e1-IU6R7Ak8q0WZ_iCRkNSmebFwhbGVuEMvivGjgE22_D6Er9OypA3x-pYpHY0Un-814hKPJLMMuqO4fHSKw0Ruhq9m-vxLJQtAHZmE_GijYx6wXLP0HsyF6H6gB8WFH49geOn-iZyLwrfkYSUsfm4hNmNZ2kEqXFopzh8gZ3XCcgdEm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=jbf6UjfSeKJvGQOCHuqWRzFmPoQT1CsYqIrYfRW3fk6iP91mP9di6oNmoU8gb5jAjRD7Sep6rHAV8YoOFAr8HEgzmbfnpbDSp9tyksvs--TyehrLkG-P9gs3AkJSfAPtjnnYBX1F-OzloXZt8AGo1q5vlyz6tMhdLZv1ngEuLIU03JGdcBijBjeC4memUDnUmdSnJvlnbX5VYGAMnK0gnLCXHqDAUeNtb76EBvmpovZHpugbs5w94WQD5eyh-G-CDXCUogeRLdBGOX-Rq7djFparmfAKbAR1mMrBxpkKX4NatgbhRZMD2iFsJWcyiHYyGo7s-6_wLJ_1bzTcqpJVU0siAQabRwmSh15DAyAaOQRhnhx9sjnAj9ovqM3O-qSJAObHEB4BcYSnigdysxQ__ZRdW6eGKK97AT6RkAl9AdtRw8MmkxhKA4GeJgnZ9si0yAq2-uDFM_31-71KNm31w95s_fZbKOOzF18Gxnt4OqOYxJLj5YWoLE1fs0e1-IU6R7Ak8q0WZ_iCRkNSmebFwhbGVuEMvivGjgE22_D6Er9OypA3x-pYpHY0Un-814hKPJLMMuqO4fHSKw0Ruhq9m-vxLJQtAHZmE_GijYx6wXLP0HsyF6H6gB8WFH49geOn-iZyLwrfkYSUsfm4hNmNZ2kEqXFopzh8gZ3XCcgdEm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PO_yvzIsLDEBBr6vqU-w1XA_ZlATdFJN91JLxye23FwtbRPzKJgc-0RkS01KX4PXcFWCHgHjstkxyXjxhqz6IJzQ_StBKykP_DYmYNvZ2dPtNgrEK2XAzmPe0XwKjeE1MKGhXDsJa71MGICgtCOGcjooWyEkHWvHyaanY8aZC7hmg4DjV5XVDPNw3_V7iRyYj17CN_3cSIQMw_bAkBgYhS5NOmVve_UzaUo5pJ5ECTMtx96ftr3LqJfUjoNzwJekWx-bZPOT4L2QQOjoRlBU3xg-IAu8RbOnfOJxYSHzgofDNimz_zrbA9v9xt8bcXebvK08QAi1Y9nq4bT-heNxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rM5PUQsmKg2sXstV7vNV7-IqPI_xtMW8VDvGwqO4K52RgU4RRhomEVzTJVLUMBNATEQAnItoN0CIVolyeiBxH0z6WwX16dJ1AnJPPKAi7qYAnYe7K_s9wq9pO2mNqcEhHSA3FBiOUCijMv2u3RAHI0VnmQ1utNMm50IW-fXjsKwRE6pzoJVkGy937eAIIz8K-wUKDlTJN1GBu8vXfyFrmuBpLNAgNbDD0Qu4UH-F1niyFVtx9-bSQIc3UnxTfucLMpNed1X2mZ9BfG0oJsS2ME7m2mEPSM0WeKrTcflL-jb3RPZxMNSmf_pSnyZzwiC6V8-VQBDTMSZT72xg1x1Npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrAbjhuLc5__yQUsQKPjO_BG1QOLpqHRrYKoyXN1tflx4L9K4qvgjpeSthimYpmemEm6nyerS1H7Rye-KOVF4oaQRSBnLNx2wwymJrwgnzEcojKJdbaymYvou2KNf4MRCVg3VL-CgcBF3VULaNYWcr21_rwD63hxgXvCROIARWUa6rMqX_h_SkcH1oSx2YS1ow-mkYj6D6YEmgH8-Rwj6zQVixnicXKS_n-MoTQIVDLuxIxe_S-p--lTQ6Yalj5eRXRlXOk9MBOImg9xlccH-W_UaJRVzreDJUBqTWx0b9Iy3OpCDtUXmBtqlqySDTH4kxFkuYa5MURKJP2uG3B93Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=ZhFN4w2txrJGKzhcR0jgMigI9KzJSUiQiCFgSUdOcsTD9-_xrv2MmieAV-8mDsLJ_nCWkuLl9EnG0H_WqKWznAE4nZh7t2sKwywTtPBWeRHwLNaNFaBcx2TeReuRESeINgm1zOJCBdACt30J5ft6Dq8GmbKPSsR06MKSE7GgDiG4llY6ahfV2p5GBXuRKPye8gk1kwZsJKl8vgPTrHwBRKZayalUhIXzVLg7h1axgRCGGowD2l4DqCaa5-zq_VoMTrucl_auE0JSZ3IMkmcLeVQBKQ6w0VEqrJfj5FRqYmn8S3gNgGoeLNe2hfEeG_3zPItxca4cm3KhPXbMhki_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=ZhFN4w2txrJGKzhcR0jgMigI9KzJSUiQiCFgSUdOcsTD9-_xrv2MmieAV-8mDsLJ_nCWkuLl9EnG0H_WqKWznAE4nZh7t2sKwywTtPBWeRHwLNaNFaBcx2TeReuRESeINgm1zOJCBdACt30J5ft6Dq8GmbKPSsR06MKSE7GgDiG4llY6ahfV2p5GBXuRKPye8gk1kwZsJKl8vgPTrHwBRKZayalUhIXzVLg7h1axgRCGGowD2l4DqCaa5-zq_VoMTrucl_auE0JSZ3IMkmcLeVQBKQ6w0VEqrJfj5FRqYmn8S3gNgGoeLNe2hfEeG_3zPItxca4cm3KhPXbMhki_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=Eutha3YbnNlhFC0MuV-XV9_-dWJUdAhsWK1QmjKXwmb_rXIgCf5XET1wfSP6mE1tgU1p-bRr_mA3_V5RzvJJlhPKvBxIJxpN-du5Hj8er5lNhG9dDdmQ030mY4j-iildkLSnIJYBzm4GSu37L4yPxdosn31hhJCzt2RgTZOuVzMvECYxlsJ2ih92i3rzJ2OKf6DjS7TisQ27lUlfD3QYbqPduEDrenc4ECkHO2pXwXGA1ktQBjVQIVsoWEgUjb4e4plmO-Ycwt745ly8yGxOJEEzZO7s4aO70ONw2bE1sPwDwvrHGVy02xOomK-6NdRwFJrJnPJbv29fi8RfCF6bhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=Eutha3YbnNlhFC0MuV-XV9_-dWJUdAhsWK1QmjKXwmb_rXIgCf5XET1wfSP6mE1tgU1p-bRr_mA3_V5RzvJJlhPKvBxIJxpN-du5Hj8er5lNhG9dDdmQ030mY4j-iildkLSnIJYBzm4GSu37L4yPxdosn31hhJCzt2RgTZOuVzMvECYxlsJ2ih92i3rzJ2OKf6DjS7TisQ27lUlfD3QYbqPduEDrenc4ECkHO2pXwXGA1ktQBjVQIVsoWEgUjb4e4plmO-Ycwt745ly8yGxOJEEzZO7s4aO70ONw2bE1sPwDwvrHGVy02xOomK-6NdRwFJrJnPJbv29fi8RfCF6bhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n--r724nC1FTy7LF6v-jHo2SG69BAVwvodc3UrbwTrJ5vDICPA9n5uXOQNXH6_2w-OqSEadXHT0ZcdwgCdTNmKXcpENqy1Hre9n-7igrdewrlhbVuyO0RdFoJTx2j5TCHbnCpXzWKNG1IuOgiw5Op44AZY0szXw7PTt-5WWRE7zDRg3oVEVt4iYOxdkPX78s_qTCFDcSRfL5x8FNh_qqRz7rwncX1JstXgCgBxCxRwGRwgQb-yX2RbhBVRmb_27-xHRxl5iNHpT88j0MmdfqFB6XuxGj_phlQwCxuB0M4Y_e-Q-NAafGk3a07e0-epVgqyiLDTKVyvFCFl2k2yqHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=itTF4iUbcCfy4qLEPxloP0JClfK9AgU0gUxkmHyih1jwWv40pD28oN6wpc0pPw2a49ndhL9Zpm7kF33c2VVv2lcaCkGPEPC7Q52TVeUEmqSNvaa0nwSgBYZzXaC2qCddo4i-mDjIkJQVHOgT_LuI8dQ_7GAtgR7ZUziTqitcURLiBptdFBlbCra4072VF8ztu25cAJHwuvAl7GEZalJSqTONEfWJy0Yh8chil3_-sI5hotwiGbKuvXqx2kBDse69VdryPX6LIWI0qXqDUm8qfOEnzVwL6ypa5pvJE8EW5qcUfiGFAp801VxTI2u0CsisaUWR_q7GB_7qW8pfRKtdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=itTF4iUbcCfy4qLEPxloP0JClfK9AgU0gUxkmHyih1jwWv40pD28oN6wpc0pPw2a49ndhL9Zpm7kF33c2VVv2lcaCkGPEPC7Q52TVeUEmqSNvaa0nwSgBYZzXaC2qCddo4i-mDjIkJQVHOgT_LuI8dQ_7GAtgR7ZUziTqitcURLiBptdFBlbCra4072VF8ztu25cAJHwuvAl7GEZalJSqTONEfWJy0Yh8chil3_-sI5hotwiGbKuvXqx2kBDse69VdryPX6LIWI0qXqDUm8qfOEnzVwL6ypa5pvJE8EW5qcUfiGFAp801VxTI2u0CsisaUWR_q7GB_7qW8pfRKtdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=V9xUjOmSroKN5i2bpi0km7PGir9H6OIeVvYbO027EfuuFr6blfbrma0xZr43JM9PgBIr-8huFsfKL7Sr75W1Z7d65oiCJGN6bqbsl6KnNJ9ag8mWuoeUbB33VYZmOOdc1sN-G2J_9LPWZuNlpekNY1hvbLnhAgwd3CD66GQTpH-18Sxfsoo-EZy9Ds2ZUtt6JOFnyquWCF6o1cebzMvqqc3CKLfFNqAcYhzhVIpbSA7m1gmy1OMbwy_wItlucU2wAiSxBNnnpDw75XAv09iOZpIzOHg_GvqRpspjN4m7J4Nds5JYvI6BtboiZT6FXLjzZOHnhW07PiIqlsfEj0ZCankPWzrsGeD3UuhRDUXaYes2GDhh8CkV2NZtG5JkqFucVXcMc1w7rU55pytW02mNSsGxfCjyVaIot8gvpCnd2RpaPmpcHIF49cGnzOEhXuH8tYR6zi4Jc2gd9zn2grfL9TydtJd9bBEBSSFUENE_ur0meTtAVJgc1XI7jLgFtvm3La5QuH8mQUWscFjSpGll1GKASzPzqpp16wsqy4NhDI1pgzMaIutVBC8WUVw6Gb_A9XXGFykmp5B7c3hJm93g209ktJf5ai72RCRtKcxPCeuyC81l8bvNwxAyyvM3T7EgpAXP4vZtgYwe3cs6No9PVYoVVmZTnhIgeAQwCBheluM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=V9xUjOmSroKN5i2bpi0km7PGir9H6OIeVvYbO027EfuuFr6blfbrma0xZr43JM9PgBIr-8huFsfKL7Sr75W1Z7d65oiCJGN6bqbsl6KnNJ9ag8mWuoeUbB33VYZmOOdc1sN-G2J_9LPWZuNlpekNY1hvbLnhAgwd3CD66GQTpH-18Sxfsoo-EZy9Ds2ZUtt6JOFnyquWCF6o1cebzMvqqc3CKLfFNqAcYhzhVIpbSA7m1gmy1OMbwy_wItlucU2wAiSxBNnnpDw75XAv09iOZpIzOHg_GvqRpspjN4m7J4Nds5JYvI6BtboiZT6FXLjzZOHnhW07PiIqlsfEj0ZCankPWzrsGeD3UuhRDUXaYes2GDhh8CkV2NZtG5JkqFucVXcMc1w7rU55pytW02mNSsGxfCjyVaIot8gvpCnd2RpaPmpcHIF49cGnzOEhXuH8tYR6zi4Jc2gd9zn2grfL9TydtJd9bBEBSSFUENE_ur0meTtAVJgc1XI7jLgFtvm3La5QuH8mQUWscFjSpGll1GKASzPzqpp16wsqy4NhDI1pgzMaIutVBC8WUVw6Gb_A9XXGFykmp5B7c3hJm93g209ktJf5ai72RCRtKcxPCeuyC81l8bvNwxAyyvM3T7EgpAXP4vZtgYwe3cs6No9PVYoVVmZTnhIgeAQwCBheluM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=HVdf5lOCW1taW856IblmxoFfmQbEUFIZlT_uR1mVB81lGCTtDBaDRmBq06ut9sE7UYU78FLIvt2FGvPeSoSc5CG7qkRm_8mptReDW0CKdLSFlbS48WIELClWwvtaLvus9ahnuZTc-ggWJWfbEvg_O2LeUUvpX9OFruY3r4mcWh-hNvttHnJVG7xWVKSrDjaRG4xn_K3LXT5JUVjD5OoZGGeeY2HNxvss1o0X1ACxhmuybyZ9Iw3whGd-sqdx2NAQ0gjYV4mIySiyMxTEdoHDjyJLZQ7ixGwKYFlgd6fVLPPc8KUeSOr9KBRjzLWAbWQpbeXmSawG49Y37BOpwmPzyWvrha0P02cIVH19B3eNmuY96oeZsbK9wzR5ng-hJhAFvLE8IgnwniD7fbRqgzoiYZjspoBvQ5kTRY2Z0f0h_1FN2VNcwwCw45YcdS5oLTi2iHdUjjqt_2T5AokqcofnTt0PCYx0I7J04UghnWTjsQ14KgePWqdGElqwwZTAEBkRIYWiJ9I7YbJo1So0HEU3BvJJjgM8lNNKdTNqSCG7YZTTEHj9GmoS3EWi75_4EyWpdPln1STY7Icvz1gjmL5UpKe1NOmqKsWunpp0jAbYTTWwJ-VRuVbkPkY0PznqZgnm6YIjSGsf23Iir7iYY8o3HHRm4-zzVuGPY0axeZa099M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=HVdf5lOCW1taW856IblmxoFfmQbEUFIZlT_uR1mVB81lGCTtDBaDRmBq06ut9sE7UYU78FLIvt2FGvPeSoSc5CG7qkRm_8mptReDW0CKdLSFlbS48WIELClWwvtaLvus9ahnuZTc-ggWJWfbEvg_O2LeUUvpX9OFruY3r4mcWh-hNvttHnJVG7xWVKSrDjaRG4xn_K3LXT5JUVjD5OoZGGeeY2HNxvss1o0X1ACxhmuybyZ9Iw3whGd-sqdx2NAQ0gjYV4mIySiyMxTEdoHDjyJLZQ7ixGwKYFlgd6fVLPPc8KUeSOr9KBRjzLWAbWQpbeXmSawG49Y37BOpwmPzyWvrha0P02cIVH19B3eNmuY96oeZsbK9wzR5ng-hJhAFvLE8IgnwniD7fbRqgzoiYZjspoBvQ5kTRY2Z0f0h_1FN2VNcwwCw45YcdS5oLTi2iHdUjjqt_2T5AokqcofnTt0PCYx0I7J04UghnWTjsQ14KgePWqdGElqwwZTAEBkRIYWiJ9I7YbJo1So0HEU3BvJJjgM8lNNKdTNqSCG7YZTTEHj9GmoS3EWi75_4EyWpdPln1STY7Icvz1gjmL5UpKe1NOmqKsWunpp0jAbYTTWwJ-VRuVbkPkY0PznqZgnm6YIjSGsf23Iir7iYY8o3HHRm4-zzVuGPY0axeZa099M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=vFo-oP4cLiAQs5NySZGdHL6XQlm2x54vaajQdgO1Z6zL_fEmsFvQ-oN2v9ZNIJG2ql1EeTGf8fW5VDE1KvkeuokjwBRIb0gxiR354rkap60OOJgYAKSxh_LSTiqNIf1uqsLCVEX6NcIDuwxE9MPicUmrnXKQ1au89nlAauTnA9SPXqOE0_2ZSww-MkWP2ynQ5-mEKZbtHvwx2n4Bf1AO3k53Hsz22g_mdfWYfGpRBKAhGq1Ldr0xjyLG2b2_n4aBzDCZXQ7N5aY-sdf4ke7R5NmZpu_vCDKbr9IqDfsjnVxYa_ynk82S3I4cfMbVhojsAihmK5poSdukCDe0sHN94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=vFo-oP4cLiAQs5NySZGdHL6XQlm2x54vaajQdgO1Z6zL_fEmsFvQ-oN2v9ZNIJG2ql1EeTGf8fW5VDE1KvkeuokjwBRIb0gxiR354rkap60OOJgYAKSxh_LSTiqNIf1uqsLCVEX6NcIDuwxE9MPicUmrnXKQ1au89nlAauTnA9SPXqOE0_2ZSww-MkWP2ynQ5-mEKZbtHvwx2n4Bf1AO3k53Hsz22g_mdfWYfGpRBKAhGq1Ldr0xjyLG2b2_n4aBzDCZXQ7N5aY-sdf4ke7R5NmZpu_vCDKbr9IqDfsjnVxYa_ynk82S3I4cfMbVhojsAihmK5poSdukCDe0sHN94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=aCgZTmLgWK8Br0cpgDuauiWzjPCovg3m5qxDUj71t86FSHket2J2c9ivtVL9OWU_Ykq2aT3YlSmZ1Orhvh8JZi1xKDT6dxcSDPnGq6mdo3apDxi-euBSYyFRzede8ieFFMcCyT9zbXltr8dQoNrwIZkZY9UX0dosTO6NOyqZ3uMVXCmaO7S_LPdrBOeqzfJXPmvQYaAEYKv-BKd_D9LnmTjpp8zfQFAE6rKltL0XtstLpZXkoOwbQ1gx13tVU1A-r-oPeHfV_WJ-m1vl8MtvxSG9rTPhjevGIy1xr-IqtcleZXcuEB-G4LzDFnUhUS_FiQLsQuDk9njZ5_5zX6jedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=aCgZTmLgWK8Br0cpgDuauiWzjPCovg3m5qxDUj71t86FSHket2J2c9ivtVL9OWU_Ykq2aT3YlSmZ1Orhvh8JZi1xKDT6dxcSDPnGq6mdo3apDxi-euBSYyFRzede8ieFFMcCyT9zbXltr8dQoNrwIZkZY9UX0dosTO6NOyqZ3uMVXCmaO7S_LPdrBOeqzfJXPmvQYaAEYKv-BKd_D9LnmTjpp8zfQFAE6rKltL0XtstLpZXkoOwbQ1gx13tVU1A-r-oPeHfV_WJ-m1vl8MtvxSG9rTPhjevGIy1xr-IqtcleZXcuEB-G4LzDFnUhUS_FiQLsQuDk9njZ5_5zX6jedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=T8FexhBJwJmC1qhLkpGqCHLu7Tz47ztKtHxj9XNLolrCb6QZhAYoi9TsP1dHvnG3udcztVo_WepxSTfUJ0UmoyaCBuSUgTA3AKHv-zGRpc7RZ55hXRaESW5hEBF1DilHgC2gNLgqq4ewAsxibpcMHd2mcQG2uWudBeS1DS4im9UQADg2eeNdruacx4Ico8MBggkKMPznk4U6bSGDF2653JL2diaxM2sR0i_Ger6C3M8hjJrsbfPBxxE3BZkLUy7UHyuKn8iZfosppJBJoptGsTpsgxC9xtpGAEQHrgOYClcJ2I4cySD1GeOVkLAqGyM2MsGJsu2kSsf_YLifU-UEVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=T8FexhBJwJmC1qhLkpGqCHLu7Tz47ztKtHxj9XNLolrCb6QZhAYoi9TsP1dHvnG3udcztVo_WepxSTfUJ0UmoyaCBuSUgTA3AKHv-zGRpc7RZ55hXRaESW5hEBF1DilHgC2gNLgqq4ewAsxibpcMHd2mcQG2uWudBeS1DS4im9UQADg2eeNdruacx4Ico8MBggkKMPznk4U6bSGDF2653JL2diaxM2sR0i_Ger6C3M8hjJrsbfPBxxE3BZkLUy7UHyuKn8iZfosppJBJoptGsTpsgxC9xtpGAEQHrgOYClcJ2I4cySD1GeOVkLAqGyM2MsGJsu2kSsf_YLifU-UEVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=GleCbDQIS0UYuqfxUOt-TG1CJW6iB4UFnzQlEv_fJ5J8ooeHjtF02IFKfqqdQWPDbHjAnFkeKAbwr4uZt2if8MEUtynv4I1dtklUUkyNr3pf1zJyWSXXaEFLURO4EsbZ9paVUihVMbuuvm0MO3Oe3y2psrdGofvJNt0blkLcmOnJbAbBdy9mTL6FmuM-2lfHBSBNUT-fckYYr250766cU_A5O3dBBg_c8pquh8T_trGeSatZUTHuNcMGEXc2-cMmEfjMyZpX58KBkYMM_4YwYlqDPU7BTEnOhs_enVHzQ7VrmrcBXmhtxcgS3F1msAk2_8X9DzofbJiPuYXWFScZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=GleCbDQIS0UYuqfxUOt-TG1CJW6iB4UFnzQlEv_fJ5J8ooeHjtF02IFKfqqdQWPDbHjAnFkeKAbwr4uZt2if8MEUtynv4I1dtklUUkyNr3pf1zJyWSXXaEFLURO4EsbZ9paVUihVMbuuvm0MO3Oe3y2psrdGofvJNt0blkLcmOnJbAbBdy9mTL6FmuM-2lfHBSBNUT-fckYYr250766cU_A5O3dBBg_c8pquh8T_trGeSatZUTHuNcMGEXc2-cMmEfjMyZpX58KBkYMM_4YwYlqDPU7BTEnOhs_enVHzQ7VrmrcBXmhtxcgS3F1msAk2_8X9DzofbJiPuYXWFScZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps7cGJmOC5sILQa9cnOIzqvgRnZ6QnifaeJr9Kvvlt2cdG-_aNfZ8vKatVEG7Ma1xKQWIYnz2tCDKa64Pw3L8Jk7k1KJRnFugr9qsM5rC4NzndKYr0vRbuelosTNyxSZypJNmTjbC4f7i_C7AAkC66K12SS6zKgktPD854G2rsvvA0bZd9B6rDbx9t9zs5WuaXgncl3waS0UccPvByvtn_uWk-21oSSpg8HFrT0-Y-rYiT31OQUF_jPYeT33uiGBKLyOHC2GsCpn4bTPh8dTmXjma5PqrE-mZs-OGoaIHLW-dSoKpbIjCO8GYgRm7Y9B8ol5weYJASX2B3O6TCk49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idoKYDXiLVpbEw4fZku8XyMPPaYWuKQstpIVLVRaPgZRokTKkKW0mxNyvvlC1Q8bVyyf4iWIel7QUL2ish7PTrDaWgPJSXxFklvhQYcA_G3tgHnxvNp-L7-7ncWNL68c26Q-QH8d1YNPMafCnniUAo-HgKwWUUQQ3UR07GFmH61e3dsNKizhq0oyDFrO2jqhWaHoP0FWM-vb3JBxhWJCiuCk4dARYVyHnQyfcBH2H5ygNMeODz3qcLuUk7ZGlv3DroMH5N-CQzuV5ZuVHxnrrHZzeOo8QoX8v0xa0kZ0-b_-569MGjJmE5Jgxm6lida2qvNVy7r-2WFCOMz-5thHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=o60FDgJjczcRvL3EaJguCztQb6Jio3ZlF3NCDCqJBexZhnLYLAWW6JPpPY-0U3EGCEYYDfuoB-Zf_GJmxaukPDTuiLqv3LAB6hhPHnPeUK1v6i2yddLGMSpG3GpkDwe9HBE5lZLkrkytNNV0Q3me0KRBfVxt8RBQFd_cSXK2AxZs8hwGr8ssFplfEyV6Pe4aVBB6KIc6UqsRAz99vsJMQ8vQON8xhbCa0EWC6-tnEr7NSpNCCXYNVCcK7oYp3zQmnVROb7g0RemVKvNaqXXuyGTlbTJ33zGnY2DqyA1f25m_1MH5PaMfJVJCrUaScwYWOqcKblnnVBqm-hOBSqqpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=o60FDgJjczcRvL3EaJguCztQb6Jio3ZlF3NCDCqJBexZhnLYLAWW6JPpPY-0U3EGCEYYDfuoB-Zf_GJmxaukPDTuiLqv3LAB6hhPHnPeUK1v6i2yddLGMSpG3GpkDwe9HBE5lZLkrkytNNV0Q3me0KRBfVxt8RBQFd_cSXK2AxZs8hwGr8ssFplfEyV6Pe4aVBB6KIc6UqsRAz99vsJMQ8vQON8xhbCa0EWC6-tnEr7NSpNCCXYNVCcK7oYp3zQmnVROb7g0RemVKvNaqXXuyGTlbTJ33zGnY2DqyA1f25m_1MH5PaMfJVJCrUaScwYWOqcKblnnVBqm-hOBSqqpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=UbSMuJU2GF3MLEu9WiM1L5RhN8QJR7Nc_tnjR1Jk0Dh8DF-7cNWL0XrA7lzm9YA5-qcIgHP9fV2rMffJ3n0y_PrNZzou2WKEokmhXuU9wU-TurfB88LP44EMG2dHG3F6iMUFo-wG5r8g85OX5-nfwY_GLo5iguHTiCz4KZedbZKifyyWBfbNJEzVkzWLfrz4VKMIh1fYU7zCbDYsQ4Wt9CMqjVtL6T5W6d0zcfnvIutH708oEFCuhWPCbDvGDF5-ITtL-y6_Gik66Sl57Z6vC4cLPpkCjRyFaNRmKfZeKazNPrJXxNSyht4DaSfh8ISSaKLBIAqTMlAs1yn1JhhQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=UbSMuJU2GF3MLEu9WiM1L5RhN8QJR7Nc_tnjR1Jk0Dh8DF-7cNWL0XrA7lzm9YA5-qcIgHP9fV2rMffJ3n0y_PrNZzou2WKEokmhXuU9wU-TurfB88LP44EMG2dHG3F6iMUFo-wG5r8g85OX5-nfwY_GLo5iguHTiCz4KZedbZKifyyWBfbNJEzVkzWLfrz4VKMIh1fYU7zCbDYsQ4Wt9CMqjVtL6T5W6d0zcfnvIutH708oEFCuhWPCbDvGDF5-ITtL-y6_Gik66Sl57Z6vC4cLPpkCjRyFaNRmKfZeKazNPrJXxNSyht4DaSfh8ISSaKLBIAqTMlAs1yn1JhhQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=X_JtWc4EVw0RdeO0HlQjX0YrENue2oNkxbqq4JAFvnP-zbzY21YcTh4XxHrPVe0v_-ts4OrX1Snny6gYfutdMS_68bDbl9INpRkuXtUL6xB_kdg_Hq6PeYlkkK4q4aVoBrx43dHUlb1F5sX_RUVfUE77i7EnQgSsYNQRNFzeigUeJPN459qf6V5Yihr-DobXwEsdFA0wRjSIy8vKDVz3snI4NpLtdAiATOEm3ttOaQDTSL2k4027qLzDON88tpxt_l1SKsnThHlvWAdM9G3MaQVuxe5P78scNKevc50P3fETFTdA-Y3Tljg-qlWmid9fpfUCuo3TR3guRPLliFecQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=X_JtWc4EVw0RdeO0HlQjX0YrENue2oNkxbqq4JAFvnP-zbzY21YcTh4XxHrPVe0v_-ts4OrX1Snny6gYfutdMS_68bDbl9INpRkuXtUL6xB_kdg_Hq6PeYlkkK4q4aVoBrx43dHUlb1F5sX_RUVfUE77i7EnQgSsYNQRNFzeigUeJPN459qf6V5Yihr-DobXwEsdFA0wRjSIy8vKDVz3snI4NpLtdAiATOEm3ttOaQDTSL2k4027qLzDON88tpxt_l1SKsnThHlvWAdM9G3MaQVuxe5P78scNKevc50P3fETFTdA-Y3Tljg-qlWmid9fpfUCuo3TR3guRPLliFecQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7YVmER-suyU1n0L7YuigW4SSvo_j3KOB5vaJb93LKBJGxxxxeuANpG5HrG3fTVPMH6UqmytoEJDF2HrGKn8fmWb9qm2WaLfnO3SGZDS0yCFQpvjigGxvvQvy6mnkNmrQxwiWbepgsObAqaXTgru6QceWSg5j_d9PUCrz1Whl6wd6Au2KYnYzInJriOBFb5nQg7UpVFJLNWZ0a4IwEkf6x-cnQ76TI9PqNtrfXXuYPeZfDLydAnJFFhGkOL9oYNdXd5_PsU-4a-z4lx0IyUB9i3vXNuIIMh2GV_8oT35qzpn0QhxZ0q1ZyAbOe9uozMAR68jYUMRrcVppb_SeEsEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=k2yBTMcpMUR9TccGUcIosg42NwITCz5wTTTM9qru6AVUzSnVZ6ldS3Df7PDlOqW4Qsj58kkq9cPWxky8QM7dlJmtzc9NS4JJFXr78dKCY9hO3i7jdcAMj6nY182qjuFDrsvIOOPwLVfIiKBp5sVJh5MWmYO6Q01UlRkZTa5RTVkgPX-PIXMJSbQrTokOJGAOrp2dGzJxO_bIUEzeQRC9HPizdedkr_LknA8QB4W70VH7yFPsIrI-l6jmaW3UttNoD418wh3huqiR2HkNzuuh6pa6c-rZ_YhZ-T31xcRlkc9-MkEKcJdJxuB7WSd2U0yXc1jmvONlCDRHePTaeOH_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=k2yBTMcpMUR9TccGUcIosg42NwITCz5wTTTM9qru6AVUzSnVZ6ldS3Df7PDlOqW4Qsj58kkq9cPWxky8QM7dlJmtzc9NS4JJFXr78dKCY9hO3i7jdcAMj6nY182qjuFDrsvIOOPwLVfIiKBp5sVJh5MWmYO6Q01UlRkZTa5RTVkgPX-PIXMJSbQrTokOJGAOrp2dGzJxO_bIUEzeQRC9HPizdedkr_LknA8QB4W70VH7yFPsIrI-l6jmaW3UttNoD418wh3huqiR2HkNzuuh6pa6c-rZ_YhZ-T31xcRlkc9-MkEKcJdJxuB7WSd2U0yXc1jmvONlCDRHePTaeOH_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=KGziUdO-waBYU--JFKbWiKvSzT5em1BUr2whOXViuoyyGYa4EhoxHXw7XQDrkPkvbLNcqMLX9pgLyjYHqjM1Nn_5KtByfPD_GtgYd7GYqMwBAbTV_Fye7A06iTa750reuf37UfW8t7j__-NlHJBH5GH7TQl17A7rF5Wdrs9NBuf4NskE_Fx-ufOOkXlRZsXYfblLBJSDkhUdAIW8WTaMTbvOnOPBC2ZLMewqJ3-g8K9NThWVeL-o5bL-CyE44EXw_1LVxteCsTvSBfukRg5zsjYGd5xCM6s7q24KiYalpHnRojf0eLmoGEOeWYIsCRr2ArL1IP93aKQk5eiCb8R0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=KGziUdO-waBYU--JFKbWiKvSzT5em1BUr2whOXViuoyyGYa4EhoxHXw7XQDrkPkvbLNcqMLX9pgLyjYHqjM1Nn_5KtByfPD_GtgYd7GYqMwBAbTV_Fye7A06iTa750reuf37UfW8t7j__-NlHJBH5GH7TQl17A7rF5Wdrs9NBuf4NskE_Fx-ufOOkXlRZsXYfblLBJSDkhUdAIW8WTaMTbvOnOPBC2ZLMewqJ3-g8K9NThWVeL-o5bL-CyE44EXw_1LVxteCsTvSBfukRg5zsjYGd5xCM6s7q24KiYalpHnRojf0eLmoGEOeWYIsCRr2ArL1IP93aKQk5eiCb8R0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=ivBhc26ApWPFGF3G7qXRkMgwVE6uvWouHfvBUfSAYLOoJBRgpRs8HW7hst_2sOJnW2GCP_Tt5vxtUcbaSaCZ9jEpI-XvZvRId4s6nQzaTuLiMzsG2bDl3s42pz_iIZOgPsWLg9Mk92dy9T_T7r3DfPS8XkkoIl7VIKb9w8FHNEjhz_AJXXTd-BE1kYGhdMLi4DtmxMmWUuVLiSoVFI35uQNu9GeeLlOe6D6JwpF1RbqVV9ebGKjM2xybQqAx-NAmD9sRhAAbYfqORQckVFBwepAMH94IYw6Z1WMoKC6lhdeD_Nd5N8Th1h1XInOmYiH_x5GNbHEnaEfshMr8waiYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=ivBhc26ApWPFGF3G7qXRkMgwVE6uvWouHfvBUfSAYLOoJBRgpRs8HW7hst_2sOJnW2GCP_Tt5vxtUcbaSaCZ9jEpI-XvZvRId4s6nQzaTuLiMzsG2bDl3s42pz_iIZOgPsWLg9Mk92dy9T_T7r3DfPS8XkkoIl7VIKb9w8FHNEjhz_AJXXTd-BE1kYGhdMLi4DtmxMmWUuVLiSoVFI35uQNu9GeeLlOe6D6JwpF1RbqVV9ebGKjM2xybQqAx-NAmD9sRhAAbYfqORQckVFBwepAMH94IYw6Z1WMoKC6lhdeD_Nd5N8Th1h1XInOmYiH_x5GNbHEnaEfshMr8waiYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=KdtEJdpSmg1cnccgqTTNziYtxj18OfStJw2K2QAFLYdiRSNAKDX5IVxaNVokYo-0zkjI1CZVMh7yenUmIb7H9tUchkWbRS1upC5kCdBpTi9e86rFvqxVpOBcAOpY1ZNqnJ5dXNLT4Wm4tAFQAsl9_z8x1qH0_tkO5fZThL6JGl1fuPqQ785-j2fwtzThLVwRAAHmJEjyf_-shj73YQDxijBEiQJw7BTw6hCMIfFmUUjdQ3wtXaO-UbHJf08ALQXwh2NvGCYrRf9PLAbReX2roE3NR78SVivpFWjMt7izwzfxXxn7iOU_zW24rcYx11vG6Nv5cNbU2OyfLvko78gDlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=KdtEJdpSmg1cnccgqTTNziYtxj18OfStJw2K2QAFLYdiRSNAKDX5IVxaNVokYo-0zkjI1CZVMh7yenUmIb7H9tUchkWbRS1upC5kCdBpTi9e86rFvqxVpOBcAOpY1ZNqnJ5dXNLT4Wm4tAFQAsl9_z8x1qH0_tkO5fZThL6JGl1fuPqQ785-j2fwtzThLVwRAAHmJEjyf_-shj73YQDxijBEiQJw7BTw6hCMIfFmUUjdQ3wtXaO-UbHJf08ALQXwh2NvGCYrRf9PLAbReX2roE3NR78SVivpFWjMt7izwzfxXxn7iOU_zW24rcYx11vG6Nv5cNbU2OyfLvko78gDlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLrS_0FtLZuhVH0mMJjx4h2gLtrxrtJD4VNjk6a9FDHj5P72RhcsHfxSsVF5OyxmVbeZfbQVo6Y04TT22wYeeve7InrxCEpwvUgQ-Kkbiz2kqZ3Gv7k9wPWfajaRCv8pTsv9te5AQ7mMaqf_CqcascU8gE032ruROTUMfL2BzzTKZMqzFhUA7sb7VK9cVW4lyQpgj850oeEKJt0Fy6K1mutIK0cKEt-4cSI4d2Wfw0AR4td7yJfagVrS4ZQMDviX3O7nCT_SqPQbsjfWiDrE2iN6obk2pZpq_Th8I8BYpj58cD8daJQN97xMoq-cijA1KdRKFPJv8ohzYChoBzj_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=YMD7uSda7Qk5-IcDpwqhMZDazeStO-RPSVBJo8eB9KP4yGjeeL_4fK02oV8tLxUYcSU1-HbkCQXE5BdOpZu0Su78WPoZ3JICR6jAFfCRGe99HuDTPNh-PkigPLNNuzLeftrik7fddJcCzmFuwElIV-BuoON6TZiqZcUyeIP_2J2KJgfgswYNsMZHswnQ_NMz6LZozNXgk6ykr40bgrRH126KTo5Q9pude6pqr72hNl9L8jRnSkw6mvZvs5_R0aUAQnNOg1HVtRCv1mutdkbquFg3AexCO854QJVVmFuLhsg2SJUu3miHA3BekpWT15Gv9nRPCULqbzBwz3gcGIqHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=YMD7uSda7Qk5-IcDpwqhMZDazeStO-RPSVBJo8eB9KP4yGjeeL_4fK02oV8tLxUYcSU1-HbkCQXE5BdOpZu0Su78WPoZ3JICR6jAFfCRGe99HuDTPNh-PkigPLNNuzLeftrik7fddJcCzmFuwElIV-BuoON6TZiqZcUyeIP_2J2KJgfgswYNsMZHswnQ_NMz6LZozNXgk6ykr40bgrRH126KTo5Q9pude6pqr72hNl9L8jRnSkw6mvZvs5_R0aUAQnNOg1HVtRCv1mutdkbquFg3AexCO854QJVVmFuLhsg2SJUu3miHA3BekpWT15Gv9nRPCULqbzBwz3gcGIqHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=CGqNUIw3g9e8-_wYF5SmUG5KWjvNnOxvXzMlHFjXsFz-lph8-PIXCyMhvLAb3eNzbfhk-iiqJQynQmVAe_412JW9CaYgURxvpDCwdGS1SRPmygMOIwvmSZdPweLvIRLgncJCVJVNABHydUKfZhnVrno9RwDEIFkpyTogsmM14-5bdT3b4dGbNrLL4jj8-koUdpvsCQAd_aXs_a0ImKK0Z6HHKqLHICfr2Ys2f_8r1cH_ZdCfBbh4NAQDAT_PdUKGz1aH05u9KdIq3Jdk_pSaxKxn_fguvJTELY02hjUSJpyHW8kXujG5AmW9wY-gMRTyM7W68Eb2KGZOdQUvs0UiTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=CGqNUIw3g9e8-_wYF5SmUG5KWjvNnOxvXzMlHFjXsFz-lph8-PIXCyMhvLAb3eNzbfhk-iiqJQynQmVAe_412JW9CaYgURxvpDCwdGS1SRPmygMOIwvmSZdPweLvIRLgncJCVJVNABHydUKfZhnVrno9RwDEIFkpyTogsmM14-5bdT3b4dGbNrLL4jj8-koUdpvsCQAd_aXs_a0ImKK0Z6HHKqLHICfr2Ys2f_8r1cH_ZdCfBbh4NAQDAT_PdUKGz1aH05u9KdIq3Jdk_pSaxKxn_fguvJTELY02hjUSJpyHW8kXujG5AmW9wY-gMRTyM7W68Eb2KGZOdQUvs0UiTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=iVTCzkgys2bRdG-pi7Oij-K1ZB5c8ddOMbzdKVLqTWuHI5HP01nctM_clg6z7C07mUryUlkHfgXgtQsQehawiDTGzgZonNDo_jModH3ScuH2pniCPmkrVB8AETGrLCKwFMvJ5fm-NyagNgXqah6UAGwG7qwuJnN-7PeugZ9e78tj7jZ1kNjSf3Gd9g3mIEBmKRonbML0MAZQ6VnF_d91siY2XW6Gn7j-DUeSIA5ywz9-0pE11J0SPtD2wgno-nsOcM1fRFc-kJD6D2UzebcSofhK0TZQkrDuYZce7d3TwflFZEqblph6qPkbUlThlbnpK_SCP66wZH2RlAEmxInIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=iVTCzkgys2bRdG-pi7Oij-K1ZB5c8ddOMbzdKVLqTWuHI5HP01nctM_clg6z7C07mUryUlkHfgXgtQsQehawiDTGzgZonNDo_jModH3ScuH2pniCPmkrVB8AETGrLCKwFMvJ5fm-NyagNgXqah6UAGwG7qwuJnN-7PeugZ9e78tj7jZ1kNjSf3Gd9g3mIEBmKRonbML0MAZQ6VnF_d91siY2XW6Gn7j-DUeSIA5ywz9-0pE11J0SPtD2wgno-nsOcM1fRFc-kJD6D2UzebcSofhK0TZQkrDuYZce7d3TwflFZEqblph6qPkbUlThlbnpK_SCP66wZH2RlAEmxInIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=um8wIEaO4u1C96H8pi0yyjpOCDllr0cao3RRsnTNW1VwQOXFVav-jPVkVNKEu4NozOdftesj2T6JG41w3kWaMDXQwYl3Ja6LoFtB522elwr-pRY4M07OFv0qmAtolVFJwnUFQDbUbQ-jdodJj-AXeRnNVoGRch6EJJuvnpketIHll0XXgMDhleCF2XoJICcPe9FWfanzjk_pdf1o7mXCNco5wtj_8GWtC4C1cP1jxuJvxiL8RWxz1dQ05U2tg4yeVD5f8cO0dKy3DMeAFExaV4BEYHBa0lvSXOYPkaXA8I39xGfQVyld9O4pMwfoIyo_jPp1kBSMQjb54bJOnzYSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=um8wIEaO4u1C96H8pi0yyjpOCDllr0cao3RRsnTNW1VwQOXFVav-jPVkVNKEu4NozOdftesj2T6JG41w3kWaMDXQwYl3Ja6LoFtB522elwr-pRY4M07OFv0qmAtolVFJwnUFQDbUbQ-jdodJj-AXeRnNVoGRch6EJJuvnpketIHll0XXgMDhleCF2XoJICcPe9FWfanzjk_pdf1o7mXCNco5wtj_8GWtC4C1cP1jxuJvxiL8RWxz1dQ05U2tg4yeVD5f8cO0dKy3DMeAFExaV4BEYHBa0lvSXOYPkaXA8I39xGfQVyld9O4pMwfoIyo_jPp1kBSMQjb54bJOnzYSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckymImMYpJx21IctbDJ6t3usEfqsDHQyOSOgabNj6YO-EdZiwvItUOlpir0xf6sI7WXUX0JVS6mnnP8erNpIWpW5jFZbb7Fo3eZmdluDs4tyydNzarUFuDMdNv_1sBNR-IiF3mzbAl7KxuOM7jRih2OUj3V_Tb4847R1moTljdQMR_T30TZzN2VSnAqsTv8y8IDX74hNGxAnj1ytFn2DxLYOvX4485S0zPILUksWXj-iSLUIWkNXUlJnWHjP5uoZKiznjeKkspJn1MDJ02mK3B4Jlm9MlmrzBipFhKLo2UKdpwXSVJcYlMMtVs02qu2PITm3um5_aSuVV7mmL1zpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=jTB-tLJChpKDiLDs0JV_h-3GxUFXLxzhd6a26BJg0OczgPnsjzPoX1IMt-MraVVfRCs6tidmNXzWQQ8iDFuD2Cs5LzK6lt6fW9nEobbaGvmQbyyzrarj6GpUpyw8iEO2DL1VkbeeqvQh-cqPV8pFfRdm99mAxTcCVmc0rEFDcrRvxR-JpBEBE5Hrb-2_pC-Op3n-wWQ7pFSGrrg5oU9tWK2mj_ayFxknSl2oXQdxfndmtGSpYSoRit7HviJ5ggvNjUJMNG3HeMxdhTZfiQebjH1F99_eEpfavzdXVgF-_7vU64_b57QS82gQ9ZZvUiSfL4FVeFceD_PGQe1do0xvLRQIvQcFqqx_hZ0Sj33lmG_Crf3CcW4raoc7O8jNa4Xcsxy3V9inlttbIRezmNjs052r0v6crtZBc69J8KYjVPD9MN6w0iraDSxKdgoNu_F8QuU9L9iQkreFiEqyB3nJ-xPS2JlpGROfaM5JHB1swg6nwOmpKcAASvOUUgGJirtEC6QqYmzph0sBZldOGEuTdiDsBkDzSNJ2g1lot1TxovNWtySe64Jx45rzGNOoJMgsIH6qi3ApZfFSCkQmyotmvm5f2P7sNp4PKYflK5D8jLPxYkvtt85vfdJHK4Xe_jPe-JxznPuNeayM8ilssgaWCl0A2uoJMVJG-JVPC3X3__Y" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=jTB-tLJChpKDiLDs0JV_h-3GxUFXLxzhd6a26BJg0OczgPnsjzPoX1IMt-MraVVfRCs6tidmNXzWQQ8iDFuD2Cs5LzK6lt6fW9nEobbaGvmQbyyzrarj6GpUpyw8iEO2DL1VkbeeqvQh-cqPV8pFfRdm99mAxTcCVmc0rEFDcrRvxR-JpBEBE5Hrb-2_pC-Op3n-wWQ7pFSGrrg5oU9tWK2mj_ayFxknSl2oXQdxfndmtGSpYSoRit7HviJ5ggvNjUJMNG3HeMxdhTZfiQebjH1F99_eEpfavzdXVgF-_7vU64_b57QS82gQ9ZZvUiSfL4FVeFceD_PGQe1do0xvLRQIvQcFqqx_hZ0Sj33lmG_Crf3CcW4raoc7O8jNa4Xcsxy3V9inlttbIRezmNjs052r0v6crtZBc69J8KYjVPD9MN6w0iraDSxKdgoNu_F8QuU9L9iQkreFiEqyB3nJ-xPS2JlpGROfaM5JHB1swg6nwOmpKcAASvOUUgGJirtEC6QqYmzph0sBZldOGEuTdiDsBkDzSNJ2g1lot1TxovNWtySe64Jx45rzGNOoJMgsIH6qi3ApZfFSCkQmyotmvm5f2P7sNp4PKYflK5D8jLPxYkvtt85vfdJHK4Xe_jPe-JxznPuNeayM8ilssgaWCl0A2uoJMVJG-JVPC3X3__Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=DHZ16o6gO1CRizR_Fvh7FV6UHXUVcGtaaYVKjRiy7a5oU8MR6VmaMQ5U3GKbNitCM9NtFG7m42IT1w-us2XLfuorijfKQeA5VWpGhcgFreVvzsdtS16L76ZvuHQCDvZzdCsI80PCX9zcEPz0tKXThhWVwcJO77H2jWqbCjZI6C3nHcUBerPaKeZ1hEfbSVPAQcUbLukv55QxvXAf7ZRvkMqwq00RmK8tkLymK3Xnt8CVuygM2G3iZhUy-wTfgW3rJ4NkUlkuNIX2LEtgffu1HJ7s54ru7O3HV09h0XVXiBxlHMMvs1D92GMp6DR7eXaLFWtyaAufBJjTChakuIh_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=DHZ16o6gO1CRizR_Fvh7FV6UHXUVcGtaaYVKjRiy7a5oU8MR6VmaMQ5U3GKbNitCM9NtFG7m42IT1w-us2XLfuorijfKQeA5VWpGhcgFreVvzsdtS16L76ZvuHQCDvZzdCsI80PCX9zcEPz0tKXThhWVwcJO77H2jWqbCjZI6C3nHcUBerPaKeZ1hEfbSVPAQcUbLukv55QxvXAf7ZRvkMqwq00RmK8tkLymK3Xnt8CVuygM2G3iZhUy-wTfgW3rJ4NkUlkuNIX2LEtgffu1HJ7s54ru7O3HV09h0XVXiBxlHMMvs1D92GMp6DR7eXaLFWtyaAufBJjTChakuIh_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=bJIUyabsVvrAMOViob7QJ4ekGbTs8lZufRr1eWI9g9S5IhFVYS-sz-JYrBukCJjLgusUaN3TYBvXNn0uDoF764q7yHbDgiLa_HcWgc-T_4dPfZ7GJfkl-Ji6WRYrUK_T8TeZ2fjprDXcXqUm7BrNywcqF8XTYpqPnvxE2QDF999paTYtN25ESCw-W_YOEP4Du23ASqKkmYkMT4yeHZrdQsxMee5dO3pTAs1HeiSkg84EU73aSonlSVfxY_MDRvEslFx9fXICOtBVpl7YOZ7svTQ35p8L8Ek2ur7ZOYJCGgGXE-bERMWbWr5DreL-8fvL_crp9oEBWAz2Ajyd6gv6dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=bJIUyabsVvrAMOViob7QJ4ekGbTs8lZufRr1eWI9g9S5IhFVYS-sz-JYrBukCJjLgusUaN3TYBvXNn0uDoF764q7yHbDgiLa_HcWgc-T_4dPfZ7GJfkl-Ji6WRYrUK_T8TeZ2fjprDXcXqUm7BrNywcqF8XTYpqPnvxE2QDF999paTYtN25ESCw-W_YOEP4Du23ASqKkmYkMT4yeHZrdQsxMee5dO3pTAs1HeiSkg84EU73aSonlSVfxY_MDRvEslFx9fXICOtBVpl7YOZ7svTQ35p8L8Ek2ur7ZOYJCGgGXE-bERMWbWr5DreL-8fvL_crp9oEBWAz2Ajyd6gv6dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=WaRmCHcaJgt5FRxqPNGiGnB37pnwyJiJDlSA0iH5O0kWwg8CXzkMDWU2ZFp84AdqmdMIiLOXgrlU5v9g6fDt8Po1hvn-y_RpBCk1N_--f9vNCTsdV7A2OiGvzfEXZY3TtZVvYkH0LJSvJ7QhQLCc9NDOBU0rBnmOZJR2MZOwR914iPxccE28QP8VZDT1Cz3SpaY3X7UO6_YRqvCzGvp38OLbxHDPMLtFZ4NXOh13-dcpP0CWxLZ0nUWYQ__yzskh7hKgze4wc1b3bpUmVWqITYL1Se2nNeEy5ZyJtTJdwAxKldNMCZIfpmkXMnZooMqeKoJSHw6BJJse1x7jKX5Fgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=WaRmCHcaJgt5FRxqPNGiGnB37pnwyJiJDlSA0iH5O0kWwg8CXzkMDWU2ZFp84AdqmdMIiLOXgrlU5v9g6fDt8Po1hvn-y_RpBCk1N_--f9vNCTsdV7A2OiGvzfEXZY3TtZVvYkH0LJSvJ7QhQLCc9NDOBU0rBnmOZJR2MZOwR914iPxccE28QP8VZDT1Cz3SpaY3X7UO6_YRqvCzGvp38OLbxHDPMLtFZ4NXOh13-dcpP0CWxLZ0nUWYQ__yzskh7hKgze4wc1b3bpUmVWqITYL1Se2nNeEy5ZyJtTJdwAxKldNMCZIfpmkXMnZooMqeKoJSHw6BJJse1x7jKX5Fgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=o72IfRpcMRXJYAYEejJjXSouZOQpX40Wk4xTq9oXDjauwdarRENt_SMmqmyrrkW_uDbhf2aPFfwojUxofIK7MxMUzMISxp2cB3o3KngTtYhj9wRib7MtO0QUBX2o2Bwz904lSbIdgQoMQSvIucGo7LqkqtLJhWAwv7r8lairtWctkRg4ui0ynepMgB5PlqDhxXepqZ9uWFF_YT6LRWjTNl7h56UVOknVdKJHPaRlj2zJSo6GwfUr4SbV3PU57AbCypTElYgXp1fOXskzrVc3337P-EIjMdbfsaVkzVD5Hy3bQ9GQdDHlFpN5a31xFr57PJ9LMdtitGVDcYCelzx0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=o72IfRpcMRXJYAYEejJjXSouZOQpX40Wk4xTq9oXDjauwdarRENt_SMmqmyrrkW_uDbhf2aPFfwojUxofIK7MxMUzMISxp2cB3o3KngTtYhj9wRib7MtO0QUBX2o2Bwz904lSbIdgQoMQSvIucGo7LqkqtLJhWAwv7r8lairtWctkRg4ui0ynepMgB5PlqDhxXepqZ9uWFF_YT6LRWjTNl7h56UVOknVdKJHPaRlj2zJSo6GwfUr4SbV3PU57AbCypTElYgXp1fOXskzrVc3337P-EIjMdbfsaVkzVD5Hy3bQ9GQdDHlFpN5a31xFr57PJ9LMdtitGVDcYCelzx0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=XfNCShajoRGNucEXZypin_hqkcPCGfmkr4kPKMv8G4xCTLwXtfhB1nUG-x2CPa4tbPPgCANCT_WT6hC-f6ZuxaMfPyIZ8ECJzRoXZpvHq5--wiQsfM2eAw4PkyVomVOfrRQjyjTKlgGvrSh8tZVpvmTOvViDFd4J8JuuMHyRyraRXvXAD67A-K40T5oEJwcs3MV19RpCVkU7rsqLM31_5ZuBx5jTSzM3wXY9CAUhzNb11fFoIMf8-swPasZ_DaqKq8SDu50m8YCjw3mk0YYSdYk6oJB-El65tvCyF5ZriOelOfnu92UMJoiLSAQUcUsklnGGvhXGpXoV4DKKg2jEBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=XfNCShajoRGNucEXZypin_hqkcPCGfmkr4kPKMv8G4xCTLwXtfhB1nUG-x2CPa4tbPPgCANCT_WT6hC-f6ZuxaMfPyIZ8ECJzRoXZpvHq5--wiQsfM2eAw4PkyVomVOfrRQjyjTKlgGvrSh8tZVpvmTOvViDFd4J8JuuMHyRyraRXvXAD67A-K40T5oEJwcs3MV19RpCVkU7rsqLM31_5ZuBx5jTSzM3wXY9CAUhzNb11fFoIMf8-swPasZ_DaqKq8SDu50m8YCjw3mk0YYSdYk6oJB-El65tvCyF5ZriOelOfnu92UMJoiLSAQUcUsklnGGvhXGpXoV4DKKg2jEBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1U9NkMYz9Yfcm-0rlAfzotbhqP6AsYob-HjwhNZx2BFMEpxGKmoKjZTt_Idqu0RhwmyoQnCjRiLr23IKtLVmB4tUzPZpDbrkAIFtGCFkGcKde-vJ4z8HIf2EClco9ROqx0fQ94Tm6SQK0YuBlUANQIJynfequWLdm3ifJC1zWfC0zOR9lTpcfvDzWLguLLw92b9gZzIgyGxnnJFWoo0rfiO3lgrWxFyk2Ndq5EXCU46EDVV8qzMpTHaW3Yrt5NvibqntU2OhN8FqA-_Y_Qh5ky5YFLZ2wLnZgCmvTz17eX0tiwDWsuet8hfuA40DLv9JCo0cNuDBNT5co_zPyG4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=bUpKIFOdvZguTMJPP-0vyLxZs0bbTB5PBC2SF_ud5OqsqY6quDzhr0n2OOoydY0wa9VFw5IrUr38V1Q7EyIso-VVlRfXgBa9OlnI8GYbsfDVLbR3BJqMS8s07qXE7WkHgHPfNAXN-RTMlh8dVXYDnJb-RBsN2VfbsQTP6QR4gTT39guze-8P65cIM-NmAeflQx1i5u1eP7AzBQYbYBlPXprK9Z0c9uVOQC6LyN9mGXjhAnr6Gyo-OWcSxFUVChYS1X_TPQ1i_u4ATElS5m7zKggyqE8AEU9t6tliRwv2VH0l7bKdisXZH1iDfJ-Sb1agCO6UBnYhSpgxoF3YG_kfWqaHRnGg_AcN_1ab33qgDjSnF10pyt7q30U9SZb4TLRtLalShjyq8s_pMdwBVRFXx1iR9L6OoNv_hWmG7DayASjWaakuuB01y78RvRWGIuRPjrDCmmO2c5_EGYV6LYOEv8anh1dkr87C2zYA0YmiJgnkfBAZS7YmDRI_HVwIJVNTdzfA2jsl8dJ1keEN5MJPQU9r2Xp1d4sfZ0tOVk_jcRSLLwpzyb-LpxA1UzyOjKMOKu6yIA0XcvDoWA3u_ttgm7jKIMOThvp8WAOJtmwn6ZBscaBFk_wnCtPC5jDp35CYsxOk063lNHI8f5_nkk6Ri3zuuphRCyC1CS62kbjv4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=bUpKIFOdvZguTMJPP-0vyLxZs0bbTB5PBC2SF_ud5OqsqY6quDzhr0n2OOoydY0wa9VFw5IrUr38V1Q7EyIso-VVlRfXgBa9OlnI8GYbsfDVLbR3BJqMS8s07qXE7WkHgHPfNAXN-RTMlh8dVXYDnJb-RBsN2VfbsQTP6QR4gTT39guze-8P65cIM-NmAeflQx1i5u1eP7AzBQYbYBlPXprK9Z0c9uVOQC6LyN9mGXjhAnr6Gyo-OWcSxFUVChYS1X_TPQ1i_u4ATElS5m7zKggyqE8AEU9t6tliRwv2VH0l7bKdisXZH1iDfJ-Sb1agCO6UBnYhSpgxoF3YG_kfWqaHRnGg_AcN_1ab33qgDjSnF10pyt7q30U9SZb4TLRtLalShjyq8s_pMdwBVRFXx1iR9L6OoNv_hWmG7DayASjWaakuuB01y78RvRWGIuRPjrDCmmO2c5_EGYV6LYOEv8anh1dkr87C2zYA0YmiJgnkfBAZS7YmDRI_HVwIJVNTdzfA2jsl8dJ1keEN5MJPQU9r2Xp1d4sfZ0tOVk_jcRSLLwpzyb-LpxA1UzyOjKMOKu6yIA0XcvDoWA3u_ttgm7jKIMOThvp8WAOJtmwn6ZBscaBFk_wnCtPC5jDp35CYsxOk063lNHI8f5_nkk6Ri3zuuphRCyC1CS62kbjv4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsReDc42Kt_f49RZY3Eqiyt9m8sUAMJzqqDGn97YTL9uKJMUwvL4eNbwbfDHyK0tkVgjlTmHIeuBZtEc7-JOfl7BF39A0kW2urLqoGMAdoREIVeNyJE9IMyGQw-2ovMahGhtPYW0Ax-HPJXD5etyIP4-c8V1xY-mlCtV2TPoqC5US98JRLrZtRrEOW2KCWkbFLevrwqQQKsC8wIT0nqqVGIrHPbEueEJl5MtAFGp9_-jCW2HtTfu8EY0qfXrH7mZdfe_-3M24CzsRLZF20TRMJd7EiAakcWh1s46Dg-AYqaKHUmmBHEKTefv0aJez8176FvHj-q4IDITESP8dMhPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvfY_bF98JdozVaOstWMM8j9l5fKugZBZ1WM96HCd7yoXrLtBaokKVTdLvuuifA6f6x5rBYg38L8pMpfms7HmIOm0B5BIJxyGoyS6F1SuqQq7DaoE2GoBSqe_XHsQNvH0jyMYQBhI5yCDHBEvQ4v3vGVZqiQS-I4ybSivqG_1zW0UXo78l9nxl-65Zzvjtr0bBMuShOvIZXXTwMCNraJw6BE6sZ-plglmeB-Kuy1IorDTCLwUssrxrEMbcQQdza-qH1y8NJr5BiDgUfF2dCoTtkjnBqu1dzRy-biUGc-elowhiU90uAUcUgQmdiV8BWiNjtWmCybUQtwGMcW_hEfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=VJ_FvxiQClLYgUgHw_ldPkZtIE_CtKhjkuIRq-Aoh_Siwe9NOyvPtxhfMhKL3AllvgGpSjklDXUBEd11h7ni71C0zKKm0ZTiqMZH0fR_WgWxeo0_UDjizJK46tMwnDXrDjM5XocxV6zzxs8YpVOXcD1SyeXhgpfBpiR2uWWUwKik99IM9xC6jZJ3kBH8biNZ-AZNap2OcWaS1Lc3Tl5Jh_Mkr2D0UuC_1V1V_vwqDElEWIVd0W79fA-HkIerRt7tHzGthhYLOOHY_IXDaXtxIUkCS3Wu8j9i8YMZtECulZh-E3t4BYanP1tzQYMdFVjxnA50c-uUJTOyalM_nqqjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=VJ_FvxiQClLYgUgHw_ldPkZtIE_CtKhjkuIRq-Aoh_Siwe9NOyvPtxhfMhKL3AllvgGpSjklDXUBEd11h7ni71C0zKKm0ZTiqMZH0fR_WgWxeo0_UDjizJK46tMwnDXrDjM5XocxV6zzxs8YpVOXcD1SyeXhgpfBpiR2uWWUwKik99IM9xC6jZJ3kBH8biNZ-AZNap2OcWaS1Lc3Tl5Jh_Mkr2D0UuC_1V1V_vwqDElEWIVd0W79fA-HkIerRt7tHzGthhYLOOHY_IXDaXtxIUkCS3Wu8j9i8YMZtECulZh-E3t4BYanP1tzQYMdFVjxnA50c-uUJTOyalM_nqqjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJvbJ4O7-GMmKAIQwfZzP5dR7PCM1pf2wQjX7K4SukCr1RhLbOZCUI-9ZA02tQfvCq4T0NE9TunNII34yoQkMn-OO3CwXKzGqINiW_G2g1dGThcUNeNPDHJb2hOgr-EqtV407TaV-jdj1QOZo9hsSa68-dDRpObxYX0RcobA-P8GqoBebCC91SM5h9zxa4fIBn_PlN-SE3UGj7J2NlxSkZRuG9AhTnHvfGFsGNqM2Z6vwZMxOTss5Ds6dKC2Vo1JD0S9jDMWcpc_hZ-j2tmmI-mTcRvKrOp5h-9C4639uz1DsmP7mbIQqXoCXLjoplQpU0JnCvhZDycOMoyGzvsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=sUSubnQcbxhk13uTN25qGQqsKJZtrAGlIf_OSZr_LHUheHfAimuPxaUj4pF4QxKgbo0j41ZE1RP75PhEtTH3CcgHtS65ZaOne0SOxRHJZ6PkoDrS3xj45Ts7V3Aqzf04BRw3vHA11hkDlTZZbf3IfTI8TLJCJO3qn9CHqBMDGzrJOreCO8wbgmv0pfP7auF1RIr6VKJ66VCTI-kIuIjRft_5yGmT3Dhi2OGVCxGuIvIYchi03PbHs58hbptCtmoufbGERjGrn8Z-mLfc73UJPqlEnkgC7vTtJ44lXuBb3rDJwTaSwBPCnenQ2DXJ5ZR-0yWZe4m_eHrZr2R-wBAHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=sUSubnQcbxhk13uTN25qGQqsKJZtrAGlIf_OSZr_LHUheHfAimuPxaUj4pF4QxKgbo0j41ZE1RP75PhEtTH3CcgHtS65ZaOne0SOxRHJZ6PkoDrS3xj45Ts7V3Aqzf04BRw3vHA11hkDlTZZbf3IfTI8TLJCJO3qn9CHqBMDGzrJOreCO8wbgmv0pfP7auF1RIr6VKJ66VCTI-kIuIjRft_5yGmT3Dhi2OGVCxGuIvIYchi03PbHs58hbptCtmoufbGERjGrn8Z-mLfc73UJPqlEnkgC7vTtJ44lXuBb3rDJwTaSwBPCnenQ2DXJ5ZR-0yWZe4m_eHrZr2R-wBAHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=jnESbovzE_iWSWskWRy58fL3_Tm2Oc_XEzNBDVAe-qkeW8ye_3M_mqyO_s-2H9m8kGre1PSM4dVLJirdt-yDvjegXNf-CMhB8CuuJiNv4-xriuWRA4qeevCPDwH2D__h10l8XEXW5vWo3IDh6iUk23xcZWV9iTNITdrYMz8gg6mMAJ2jNn6r83Ahp0cchEsdSrfUzW2WNuxWUBapYNb3EqtV3kYKGmx2YYRzvEY3SzQ5S-17rsjy-pjFdtYRZ_Eijw-YwZkRkaHkiqlj8-Tv_YWVaM22JiLEDyZKZ5cJmYYU7tJ5ldfh50O4KE87LoVM-PCtBaIURwUY7iXD2RQrSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=jnESbovzE_iWSWskWRy58fL3_Tm2Oc_XEzNBDVAe-qkeW8ye_3M_mqyO_s-2H9m8kGre1PSM4dVLJirdt-yDvjegXNf-CMhB8CuuJiNv4-xriuWRA4qeevCPDwH2D__h10l8XEXW5vWo3IDh6iUk23xcZWV9iTNITdrYMz8gg6mMAJ2jNn6r83Ahp0cchEsdSrfUzW2WNuxWUBapYNb3EqtV3kYKGmx2YYRzvEY3SzQ5S-17rsjy-pjFdtYRZ_Eijw-YwZkRkaHkiqlj8-Tv_YWVaM22JiLEDyZKZ5cJmYYU7tJ5ldfh50O4KE87LoVM-PCtBaIURwUY7iXD2RQrSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=PDFbnOS5XhBWPDt9KW4lGOndZgZc2_-4-OKU7-WI5Z3RtfaHbD8uJDEfl_pWjH4cfVJ0KQxu-Z27j2SbMtnr29bTttRZI9lSoaMYXcZ_8HGJ6OX1rFhOqy0Hp60Ys4ztGmxtobCFp23x54psytzKgo0MOvWVjjgd83lQNdITvc8dHefIwhj-Lt4BvKN9u5UP8Kj74Gv3X_pmNltdGZQZzLQEYHrs3SH12Kx9TZ9stNcuini5_VlbdC1sp9eQ3KKDsAzmumj-m-qk5JBGCvP9Trww0LK4IFquDLDOMr0uVGPeoC3xofcK4tqbT8cm8m_WvJMFXXu90kFwK_sPz0UCUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=PDFbnOS5XhBWPDt9KW4lGOndZgZc2_-4-OKU7-WI5Z3RtfaHbD8uJDEfl_pWjH4cfVJ0KQxu-Z27j2SbMtnr29bTttRZI9lSoaMYXcZ_8HGJ6OX1rFhOqy0Hp60Ys4ztGmxtobCFp23x54psytzKgo0MOvWVjjgd83lQNdITvc8dHefIwhj-Lt4BvKN9u5UP8Kj74Gv3X_pmNltdGZQZzLQEYHrs3SH12Kx9TZ9stNcuini5_VlbdC1sp9eQ3KKDsAzmumj-m-qk5JBGCvP9Trww0LK4IFquDLDOMr0uVGPeoC3xofcK4tqbT8cm8m_WvJMFXXu90kFwK_sPz0UCUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=FOqVw3Eq6lwk0eAup82AHoMSzkOyGEmCaFtm9FPOqNBVodLkbrwYx93MV_L-aZc9TMKwIDPMbAf5AmF8BtYv7hniCpZl9bDFZ_7mpX0rKdZLQBtiwKLc1r6IGN57FFttOKLgkUjr9rLAVyNJvniOF3RDmChWuJK79uqLPAShr95xOqyJMRB2Qw7jZOjvvt8guaaXSJ0jG2Y0IEYU9BgrhFV6nwJ3Z7pSopl6Z7vLoSxLEIOv7EniE1kviYUgTlG3haiLLVcbmkGH8Y0RCu57_kZa-6xG_JRVh0qC5UP3vPgNazmN0KpzQgkPI7lznH6DUCD2xpSCsBk1rdOw1il_AY20WcSrI91o0a9yKL91GIQj5g0Zx-yZ4NN_SVUNJH8b4bChlF9W5DjVWkB9O15Xu86z1bvonGvguEMMmhUFlQy_ZcoSg5ki5MDcAM2d2WtISJZ3QlZhZBME1Ksy7Xplr7DOHOIB3zVUhs5oBKkQrpiR5gVJTKfarHIX1VSaKkRv9OBIbn-ZBRUO3Z150o25-2c06S0dnZW2XOC465C4sUMLqpDxDgS_Bjgmec_N5YUUR7WCVMsqTP__MxVpaAXe5I21hrHcooUVYBfiT8CKnUAukMXm5VI2QDEb3O2U11Gl8JWt5xpPGmS-mm5T8w85cbesgdGjSNmnCCVdZrf2sj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=FOqVw3Eq6lwk0eAup82AHoMSzkOyGEmCaFtm9FPOqNBVodLkbrwYx93MV_L-aZc9TMKwIDPMbAf5AmF8BtYv7hniCpZl9bDFZ_7mpX0rKdZLQBtiwKLc1r6IGN57FFttOKLgkUjr9rLAVyNJvniOF3RDmChWuJK79uqLPAShr95xOqyJMRB2Qw7jZOjvvt8guaaXSJ0jG2Y0IEYU9BgrhFV6nwJ3Z7pSopl6Z7vLoSxLEIOv7EniE1kviYUgTlG3haiLLVcbmkGH8Y0RCu57_kZa-6xG_JRVh0qC5UP3vPgNazmN0KpzQgkPI7lznH6DUCD2xpSCsBk1rdOw1il_AY20WcSrI91o0a9yKL91GIQj5g0Zx-yZ4NN_SVUNJH8b4bChlF9W5DjVWkB9O15Xu86z1bvonGvguEMMmhUFlQy_ZcoSg5ki5MDcAM2d2WtISJZ3QlZhZBME1Ksy7Xplr7DOHOIB3zVUhs5oBKkQrpiR5gVJTKfarHIX1VSaKkRv9OBIbn-ZBRUO3Z150o25-2c06S0dnZW2XOC465C4sUMLqpDxDgS_Bjgmec_N5YUUR7WCVMsqTP__MxVpaAXe5I21hrHcooUVYBfiT8CKnUAukMXm5VI2QDEb3O2U11Gl8JWt5xpPGmS-mm5T8w85cbesgdGjSNmnCCVdZrf2sj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=MWZls5dsw_0-ic-hoPu-wHn5J7UW9ff5Q4t2nSJxN-m9KQNFoVeHfxfwmuv6xihefBU1LPykkRjR8ntDiN3UuXM0naB7W-NpeBky2A5SrCG16A1fyQq0HtncHXMIEcJYMDD4RyjyjpNxzSvOV6LyOji57IhwrXGZV_4M_qSFZFpyPmSAxffuvXBZ4T-8z8vdYWNdBhpRRPngteRCDBbixC9dwFU8NiJSBYkvvf3WQNQ9_uK1f-hTpQUU597X0KCYq3CKEvSZsKUEPX_MKRsegyx_eYhRW55_cV90gUQ4UJ6cQKQ4mDCb2NqsA-atIlMAWfUxtW1aDT-x5LQ1fGyIZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=MWZls5dsw_0-ic-hoPu-wHn5J7UW9ff5Q4t2nSJxN-m9KQNFoVeHfxfwmuv6xihefBU1LPykkRjR8ntDiN3UuXM0naB7W-NpeBky2A5SrCG16A1fyQq0HtncHXMIEcJYMDD4RyjyjpNxzSvOV6LyOji57IhwrXGZV_4M_qSFZFpyPmSAxffuvXBZ4T-8z8vdYWNdBhpRRPngteRCDBbixC9dwFU8NiJSBYkvvf3WQNQ9_uK1f-hTpQUU597X0KCYq3CKEvSZsKUEPX_MKRsegyx_eYhRW55_cV90gUQ4UJ6cQKQ4mDCb2NqsA-atIlMAWfUxtW1aDT-x5LQ1fGyIZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN33QlttVe9lG7GBVYE_X_Tvm5ivd3Cw1-DK9EzdhXgDRhdZCv0o6dGOEMr0-zbJMVSL77bd5wVvBXYXfhqcaKox93D2j9xHvOcfRIogSyReOmA5vhSeppDTXIm7efSUOE0wODrTCw-IfzyfKlR5hcw4Tj5kmHoVUBYdjsRwsOXKlJb8iSdkA9Ae_kHBkZCn4c9B8MwvSMoiTGaGr_eHzFsBL5i57poF08WqLmIS3g2BpE6ot7xKHGQ8kwLXULWs6OfQ4JqBSZ3ni_5UNrR44fP2iInkv-WOQ7CNjmSRLgSXd6cKzqeQAB24TWGqUqGCZbugLexyJ0fQ2YBMZGiC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk8AR3J31RcoW-ZlqRQw8q80ami_d7BeL4piNRYRbsoXRBn7y-v21UvOtUFiQhDyLYgw4z0fUxb9FTKHHFWeOkj84n1D0mnQ93XrKTFGfjRE3yb2qEmeNtAcnG2Eps3HZUHxstype58a4eZxZlbAbu6jK_BJ45BLc_JLSZpVky8NpOLWX6BgIrEzXxEvXZ8xRl3mK1-43BQqMxqZf_TknRy9LEKBiLI_BkeotStFvSVrEJo-E8Seo656f3y9nXr6vce1oGwrb5Z3dXA6toFgB-GG8_6HAaK5FEqBvP-oi37XdbRg_In_X3ooo8t0shwB9rNN25WoObme4j4pKCLJhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=Ciyg85oJgFBWGwfB1iC2Q09EqrwACKgx9xENfGPoOfyzjRbhPmk07LGSTF720IAMKwhN9XFf3w6n0YFb-9WACucIrRFQVECpHY8s10AnSxCGyRi54FnyBrBWBwHo7LURFE-y9GSxKs0XeoACX6xRQk269UH07amYSMxbPWXCLnbmuhoxVuKOPNpZx6m8qM6eqUIBr4DR_gvTZt3olmHdnFYq3iQ8g5-tGv1iGwSZgLtw5scfttN4zyV2fGF2DSO2Lgv2lu01F0tJs6MuCDxzTPUwbN4rzrhL3wQGmM3LhTbnxtEo0AgKXztq4nkbYrwQsatypuus-PTQXyPL6NbiYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=Ciyg85oJgFBWGwfB1iC2Q09EqrwACKgx9xENfGPoOfyzjRbhPmk07LGSTF720IAMKwhN9XFf3w6n0YFb-9WACucIrRFQVECpHY8s10AnSxCGyRi54FnyBrBWBwHo7LURFE-y9GSxKs0XeoACX6xRQk269UH07amYSMxbPWXCLnbmuhoxVuKOPNpZx6m8qM6eqUIBr4DR_gvTZt3olmHdnFYq3iQ8g5-tGv1iGwSZgLtw5scfttN4zyV2fGF2DSO2Lgv2lu01F0tJs6MuCDxzTPUwbN4rzrhL3wQGmM3LhTbnxtEo0AgKXztq4nkbYrwQsatypuus-PTQXyPL6NbiYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=hpNG5DcYOXEPQ3cG9fk3KE1cb_uXuheeDmUT0f9grvI5_BgTUxMz5uQHlK2mwbqx6f8ZxlQH5tEjuu07IUqJA7AExTVX4sMqf8XmrCgr7emLJEfmzBxsq711QtY4i3Ckbai02hYA7A7MgWj5vbSspYirJkSdcINkIQ70FWhr-p6hwGJY5Jx1OdQ1Z2pBRhVuQwPeYJokEGTKyzzocDwcJMjJtP-MvSLp9ksmGBs_prxsoQQOGe3CbWHLph-OWBN5Xr3QAeTeMYFdm-tzrbXMcViMz-2vgmjNSouZVo8FE49mWPg3LC23WaAvNYxq4iKPVZgJd3hSerhHaOmdgPGdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=hpNG5DcYOXEPQ3cG9fk3KE1cb_uXuheeDmUT0f9grvI5_BgTUxMz5uQHlK2mwbqx6f8ZxlQH5tEjuu07IUqJA7AExTVX4sMqf8XmrCgr7emLJEfmzBxsq711QtY4i3Ckbai02hYA7A7MgWj5vbSspYirJkSdcINkIQ70FWhr-p6hwGJY5Jx1OdQ1Z2pBRhVuQwPeYJokEGTKyzzocDwcJMjJtP-MvSLp9ksmGBs_prxsoQQOGe3CbWHLph-OWBN5Xr3QAeTeMYFdm-tzrbXMcViMz-2vgmjNSouZVo8FE49mWPg3LC23WaAvNYxq4iKPVZgJd3hSerhHaOmdgPGdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGBfZrTegaWN2PxdXHj7EUuIGnBF2xPvjfFJpGDtu8B09-nb5I54r6xOu1Ewl482-pjPSpVMO1RrU1sbvD-Bq_aMFSs0Qw41xdP7ZAoONRyqHH3qiVdtAQem2q_gXimuubkuk44fOFrUtxaUKBaaR_W_i8FPCu4NmSPncQZFR6elmBdIqg_Q0NAsyPRRSPzTcHUXzz1jkIe8ZGEX8qHZ5CYru5p14WBmPEfVMEwJgvRoVUwcDaEQOeFW446xjR9eeN-kdd4oin33YBfJ6Veseif7suBrpM3RDKSKj7IUqLi1EcEApuddMPeHv3fLtKgkAQECRgvYZDrgX7BX0EurDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=od76Z-CrLFTcQDULcXwG-oKvOdlTHFYNzrNIn0yD47VbHyatgrAoQNMFSWOIQ7GJ3BT4CMJ6iWrpFG6iVP0FZZMSY4SJ9WvfhUbKsFhpybjZpp4BPFvZCzRV70i_ts32YiaKhcTN54VDPBxdsCx5Bmo8oowtsI9Y2zV0t2vom26EjKjUfVm7POHUS-na7MnwO5YA4PFNz7fr7SkyzMRIBeHQTPtiPfcQ8vLo-dUgp-k0LRr37mf2WXquiK2wBarXOwUA_C6JTs7NrD5sHcIFawcE5AU6qWrDeMUYUMuIw5yCMAQsSaxF34BBDt1H8Wsin96WXlO8sQxkL81FlM9cFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=od76Z-CrLFTcQDULcXwG-oKvOdlTHFYNzrNIn0yD47VbHyatgrAoQNMFSWOIQ7GJ3BT4CMJ6iWrpFG6iVP0FZZMSY4SJ9WvfhUbKsFhpybjZpp4BPFvZCzRV70i_ts32YiaKhcTN54VDPBxdsCx5Bmo8oowtsI9Y2zV0t2vom26EjKjUfVm7POHUS-na7MnwO5YA4PFNz7fr7SkyzMRIBeHQTPtiPfcQ8vLo-dUgp-k0LRr37mf2WXquiK2wBarXOwUA_C6JTs7NrD5sHcIFawcE5AU6qWrDeMUYUMuIw5yCMAQsSaxF34BBDt1H8Wsin96WXlO8sQxkL81FlM9cFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=b8UKHWwNa89r0-X7JdehsoixGpaKdwABz9bbn9u7VcEMZBsN-oxE52YGI8TdqRXQVd_JTmTBnQqbP3SVxoQgZSm9FCZZYEg2bsGsiHDOvwv55y9z7YUuZaNQ32bcaIkZz0GAALCfdWT0LD2pK9J8svc6EDeQ-qxv5K1suIWxw4SFWx5a5SvuZMDq2PRLV8hwaALsaXhFZpQnic2FhnOfPuLtyB_r-PA6RkN0zOC96uDzXLMd0CXIWdmE0z3PPyCy6JJFP_WhBcMI-wb8SmGi2UDb_XoJlsHAs7q-Htfeto7jdPN8c-H2rJ9BaT7-sm3bhWDvaJCeacLkscgbKv7tsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=b8UKHWwNa89r0-X7JdehsoixGpaKdwABz9bbn9u7VcEMZBsN-oxE52YGI8TdqRXQVd_JTmTBnQqbP3SVxoQgZSm9FCZZYEg2bsGsiHDOvwv55y9z7YUuZaNQ32bcaIkZz0GAALCfdWT0LD2pK9J8svc6EDeQ-qxv5K1suIWxw4SFWx5a5SvuZMDq2PRLV8hwaALsaXhFZpQnic2FhnOfPuLtyB_r-PA6RkN0zOC96uDzXLMd0CXIWdmE0z3PPyCy6JJFP_WhBcMI-wb8SmGi2UDb_XoJlsHAs7q-Htfeto7jdPN8c-H2rJ9BaT7-sm3bhWDvaJCeacLkscgbKv7tsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=pDr6TzBCcTlXzP-o94lQaJB_hSkCyjoP6ke-Qr1hOpkLwmtSAJTvxATmalsCtbjMtCZVuLs6Gb3qM5FisGFZ0nYrbr83qsDxJ6E3NtgN9MT_bthEtMMvpQin_QOj648Rrg9uKPKcW-dtgOdiPvlARWqsUXgOYa4a7uY1aJEUhRdEEz879Sk17Mfw0NOZIvdb8R2PmmtuzsevoJvrx811Bp6jhCZB_N_Q3MWebssoH-Y38YxT-MUOILrZqRHyjjaaSacpjb7gRGir-2hnNqz5nVTaPailIy875P9Hl54t4Xl2jQ4V7_AsCfMgVOfhtZnn06wXW7snSKUgK3Ts4FjAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=pDr6TzBCcTlXzP-o94lQaJB_hSkCyjoP6ke-Qr1hOpkLwmtSAJTvxATmalsCtbjMtCZVuLs6Gb3qM5FisGFZ0nYrbr83qsDxJ6E3NtgN9MT_bthEtMMvpQin_QOj648Rrg9uKPKcW-dtgOdiPvlARWqsUXgOYa4a7uY1aJEUhRdEEz879Sk17Mfw0NOZIvdb8R2PmmtuzsevoJvrx811Bp6jhCZB_N_Q3MWebssoH-Y38YxT-MUOILrZqRHyjjaaSacpjb7gRGir-2hnNqz5nVTaPailIy875P9Hl54t4Xl2jQ4V7_AsCfMgVOfhtZnn06wXW7snSKUgK3Ts4FjAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
