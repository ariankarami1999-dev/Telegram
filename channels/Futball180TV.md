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
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 681K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-94760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7d1NqAIYlHLHyrE4CdhYsr1RV_Zee0xdH91VyiB4KBMqIWBDQRFc6H_auSS_RLnmCzhZkt1EtdOrKn0ugKQ0SvdWxWg-BMhQ7yeKZASZf5hpGoOxmf7nbi3h4q1l-4kEPK0vSwG_kbtoPgZrfSiMROztmF67WbQCG9L81ADC2_NK-RMwXtkfSxyw9cYqK2lKQeN3rls26LoekJ6Kx3u3Q-pwGBPzuvpY3ojJHADzj3-Z0rPt8NMnyKyAKXWlRMy-TkiK5TChRZaVfFC5jFlVbmWatVLUY_e1JEJEtV3d4oAGTqrbyrdTqEGKPlUyIAPGUBSfQ8MXlQkpJuohEIhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0iwzXYI_DqDSm7ihVL0l3YmdLIbsszCaxPOxaE-zyXSNbvNO87U2aB_tJS88-ze5qKFSlWhBEGR0bkqT_IVutXxD2sCo91OOTZ4HsO27vjwGgA4i-uBEmKWAproq-OxGpk0R8FN0r1h61QHCizi8mXIIYrHqEUggyLuJRilJGDbpVp5wpI3LtV9fTVG8SRqVvy-hTqA0dwSdsBqdO81pljzPCCwHbnJfz6QlCwV-1GzO9Jepspump9Q5RCBSarF8fyggZ6knI382fMWjD9DAz-enZHoRcRIAPYhPEenU9o75WDOhEshppFPgrD2in7KNP3XwOeLqxJiDdUw5-wE-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇳🇱
کودی خاکپو با گل دومش مقابل سوئد، از آریان روبن عبور کرد و حالا تعداد گل‌های بیشتری نسبت به اسطوره هلند در تورنمنت‌های بزرگ ملی به نام خودش ثبت کرده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/Futball180TV/94760" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spzpX3CBFSr258iP5JcBlNHtwOz7Irq_Jl1oQw0Ittyx2_qDPfOMEtmkAzb_CPoZm-OLSxYMmvOHoYt7KqXC0IgYuy6tE2y9DmFpyM0Flt8mnDDUxN5oJYZmL1g7sGjBkJYewJJ-rDd6jsdAYtn8k7Glpfbm819LgXcbcwtgx81cnVowgH0K4k0Lq-5DbGJCDVtnIaVo1_0RBWy0TTyRJyE6S7x9R773L2rQgzoWMs8-3XBOEtiYq44-VmFkMpP_mRlmPiMl8YdH9lA85dafCaOtxKkRQxuC1JNanAsZ7iwcTKINC1q-tkNz72pYlFAxBRbjVnXcEHTJxISN-2AI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر دی یونگ با پسرش تو تماشاچیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/94759" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAJXDcGXcGb8fyGp0q2CuIbtSLpdq2nTgAjqp1tbLmuB8KFAoOFWJxBqVwxkNfMXnZ4bmnJAOXR226LGttw_x3EkahJI2O54hOHedb_0tt2q5dsmSmHXmivJeQmKOYm9_f9Vdy-DJsRsYUbns3-earLwDr0_f_wqko88yzSQCktod8OXuQ7bRn03Fi79HDIKDbtTGXWUV9YYUtjt4oFNl5s9CCrcmqZmlisu4fNV1lbe9XPvuR1JS2PZ_d2l9zK3UMpOJdu1Wde8sLS23o3AyjsU-690pVmMfRg91klUxVHnxzErdp_kfqf0obvyCUsAKA-ZbAdv1TlauEpxwBWPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
با یه عکس فوتبال رو نشون بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/94758" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد
به سرعت آنتن رو ازش گرفتن
صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم
مدیر کل شبکه خبر هم مجبور به استعفا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/94757" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLX03-eD1gJw5Gs8daAC9DPALIPPv3D2x0dsLFNXonoCBi91vLgxxTLbkipOAPlqV8LEYRKnxMw3gYuryDaDEIeNNEYLLiYZ0YQEpg8ax84lDo5yiWUAN6H1eCol0N5nyOnv5sM-gPdSok_6_GMbQJ4F-qg0N2TsqwbScNfVRTJ3tAV7HIWJEAf3e6lsXsgrpC-Be48Gpmui-Gsr3V1FiIdE0Mt7PZGPBq-cXe2FfpYHBgt5OZRtTQ1aFaMmwgGLDPHRlAuGWpZJdwfYOcUO6SyGUVJlp_cQzTTozR4D2G-N6VKzyI6VwwyorGE3wp7TqGYOG4dfBJ5MrwmeK3GJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/94756" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است/ اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/94755" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94754">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akq5T12SVHxHSbJSnjIcmVqJV6SlNVFVSHeW6EknyV2km3h3kVdN1jFrIXQFQjJTEZ4Os12OLSxxfPOYF9AzMkK6ATlWM_eHyrE4EnXzYhSW2uI2WL6cn1ro-ZELUhZ5rXCmQs8ogYjJdjRk0MdBLMWHoXSHTwQypL_cSweRb84q9DHKTcA0yVUfL3dPgkXCSOldOOEQSWjaCgewNCdlYcoN5S6yOiXouwul5mlcHHJZkiyS1Ocvsc6myhm8Si8ncj1RqO7Lz181TfSlyyygYZSMR2pB29Aoa9s82RzD-F2e63btVp3H-7FXCSgbb0ZRCsD5BbU8wA5RrM3vZbRQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش قدرت هلند؛ سوئد قربانی شب درخشان نارنجی‌ها.
🇳🇱
هلند
😄
-
😃
سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/94754" target="_blank">📅 22:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل پنجم هلند به سوئد توسط سامروویل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94753" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گلللللللللللل پنجمیییی هلند</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/94752" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhFUOb87k-KN2PYsEOjPNHRE4Qr9plzvZDERMisW__H8tIBazq3hQylmjPqu0aYQnYHUwvJd9ThPvpfibsgZ1We5KxaHI0pLIvNdP-nfFi0WGzGYO9HmIFXZqRWUu62aEjF8F9-hS-xgQltOMmLeWIaaRu5kxhN7bgf0hOr9aZKBeKFCplB9pVdC_HWoB2CoZwHq0dMA5qJK2e9JL--LspxxMjikYq1zlZ2aEmbUASG-nHIdTY9r7h6hoccFlM_nJPftEiBJr1Z6DOfeT03xhJKfnKoQMFjMhHWvj3kYb7DB9eK11v6uxS_LRbU5-KHpsGBnq4cgTDJODYKeovvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHToEGBS-fExwp3oBEO552RqZTwIysFjcIEKJwxCc28FK6yi5SHfG4s_G_dqrOq2QxHXFZ-8UmLaZOn-1bf6Mhu3djU-1EK--MeRI21hBYsRGKZm9s6iPfis02zCLLpplFyX9-4hG9gthId2EtJTDnW19AlLNX_MSmQX6RebHlF-ZGP7H4CVeT1O6B3v2fjzAWJAq6EQzCzajnKhYULghkqrvTZ5xRzI2I5bKQCgaM67kE6sXMApwmPZROkENH75ry55mEp7-HWzqJMmPN0nQq1ULkZR6FbWq9laSZQw4LIISEjWOEXp24HGjW5521sofoauMJORgUhDcQ70Y4rTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇩🇪
ترکیب آلمان و ساحل عاج، ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/94750" target="_blank">📅 22:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAxi3LGazbi5DbSqjLuzThDgpMl6Ps9VvVkr34Zc2CJ-fleuw4QJhiJ9U0RQ6WShfn4hp0tydzMdS7LH5-Ca3Vi9w808gqhuaWTvoiGERC_wq8ATKw_wbFj-BIFx6q6peTp4Tvm5NvKznpTorKQRGrKtyGs_H86Fa2Mh5LwQ5Koqr05apYr5Svwo2MhDIOdK6aip6g-fVaXT9i8fljtDwIRhS2oKLH9hQqYgVf9pZjBo5-rQX4CMZIfx1R2VO-8jAt84N8sOZwO2bnm28V2xtc4bEMlP_Oram4A7fMZOYZUIaR1aWpa2PRy5ZxclCwFKoFuCExPeUbGwaivtz-GpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح تونل ویکی فن دوین توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94749" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این دخترای سوئدی چقدر خوشگلن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94748" target="_blank">📅 22:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه لایی خوشگلی انداخت الانگا</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/94747" target="_blank">📅 21:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇪
گل اول سوئد به هلند توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94746" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللللللللللل سوئددددد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94745" target="_blank">📅 21:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل چهارم هلند به سوئد با دبل خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94744" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چه تیمیه این هلللللللللند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94743" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلللللللللللل چهارم هلند بازم خاکپو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94742" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل سوم هلند به سوئد توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94741" target="_blank">📅 21:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلللللللللللل سومممممم هلند خاکپو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94740" target="_blank">📅 21:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWiUUhoH-4xVP2iVc-xYwKRWG6SNN9GPVyOUWYS40sW7UT1igZyLG0sBixf-ihWp9Zv0aV37QyKzL8RWJAZTCKDZKKrIhL878QV7NonvdKCYharBuYheWKgWkiZ5lGXzCaFziIGomVo3rb5emYagnviM-jD0DrO3MlEn8lH2085e8MgY6_3ImT8qKXquy8aJwRZ56AHRitJeonNkBwUPgDsMqyLFDESdkw3aQiSWELLDEzk9SKPaHP36z_eQRMtOd1A15a7b0SdrYEtwUTMnqAyyZbrZfd51IsQlgU7W7xDD2gR3SgFURYRA3EDis4JLprLp7wjoRzPVzjF-2WVNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇪
#
فووووری
؛ جرمی‌دوکو ستاره تیم‌ملی بلژیک دیدار مقابل ایران را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94739" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94738" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOFwvts6oZ28hOQrztvMPOWZ4eZm4liS3yiG94UfLQ7ZZlBdVQAGLAaIqMiMjCBbymqkctpnoZtg9x9zZQhD5ONd5AV22z_lohA1v__FuHCcYU3Ozp24KaxN0zbj0FHeFD7tcS3znk_YkV_sd3zv1ELwZCX_A5wKfnOKr--1zFB6_2bEsLqGXdN2F1ecbP2W9BVJT5W50YvUjOxFHX9rt93gmn2frVhMK_3JPc8IGb68YOgs0mjqy8702U3pQWgaCkai13tbL0Qu3qM1xu8vmlcTidQe3Oxzdz5RteW3bBZgXJsiaNkI8L1Bl1R4QFrO9toSPUlou0zFN0DC7x8eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
‏
📊
بروبی مهاجم هلند در نیمه اول مقابل سوئد:
‏- ۲ شوت به سمت دروازه
🎯
‏- ۲ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94737" target="_blank">📅 21:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZb-icbeZpN4oVBIcgsrkJkgre2_c2MY5QTPVF22mlaEpZAs7NdsF6fOhU3I6NWn9g-0-BG-DwxB55cBoe8-ZSOkjY-gvuM3AJK8WHldK47-LhJZ4vZX7yev5S0J98u5Rq7QSN6ro29GBr06Jk-JVpP7VkwftyM1I5oGTK6HUh-Vyk_CY1qn-qM8pi2KHXJza3jOO7lB3jUC_N2b38QvhCnzhKYXZAsIpQ7eqwXP3Uf__9IC7yZ8cldeVJZne2aUn68r_svg-R1Vyz948ypPorWsfJRkNiqrvYtSE8TDhF0xRg8K8rOKn3YESIOWakgfFktIX_Y92XNCEdXJLgMS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇪
آمار نیمه اول بازی دو تیم هلند-سوئد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94736" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIpqx6JgC7eAvmSrOGj5hZAW9zhiX9Ol5YhGdZN4d1yvBIwRL3knb5PVH-ls_2VhSd2vA5rTc-Tw-Xg-7XtsOcNbZ9pc9Kvw_0Zk3u4g0uHt0h9_ruKIvMZfB4LdYGFYQBEa8wBI2ikNYCbHsTQeGbxvoj-DFQkPVW3Pda-PXdgYkLi7iXW__J0S5k-iaQD5g7FkLpOCiKGFndG_vMosu422iwZCHLKoezxwqqhd_p-H_-jYTtFCPPe9Fmlrjw4nEQJzg8QWABSKX-7__cdGKYToe2l4GYkgMdDHUsqKAY5TY4q2pHZnz47VyDs9gwyJvHnZcTNti0LEol6ya6zdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
رومانو:
انتقال انزو فرناندز به رئال مادرید با سرعتی مشابه داستان مارک کوکوریا در حال پیشرفت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94735" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پایان نیمه اول؛
🇳🇱
هلند 2 - 0 سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94734" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلر هلند چه سوپره</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94733" target="_blank">📅 21:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94732" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94731" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوئدددددد یکی زددددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94730" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگاگگاگا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94729" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY44kEbFaZw8bl_EP7oOvlBuylWk9y7LW_q33iKXw848Pdvb7wgNiYGrXv7sbtGc_U8xLWIibLst76URi5vrdCG851yQFt2_VD2e-uOHGCHNQ_QLTmr9h3v626BuDxj66fEGz9yNHueKwpyJOPryi0j-T6-tEShc101MH9fPrbj_ztWaGlf0XdCPY-odKLu-dzDET1WfgWAsyFFjN_n_fVKaj2LXej4igWxqZgJQvevKaIebdEMglKgt87Wg4WWVT9VxO_X3kT702fxE_eeuIvk9cqynDhbdE9n73ZB4mrtT5fhj2giVA84M1j6M69rfEXB3FPas2ZJDegKeBsoslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب شاهکاریه این
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94728" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رفقا سلام و درود
اگه محبت کنید حدود چهار دقیقه زمان بذارید این چند سوال ساده پایان‌نامه رو پر کنید کمک بزرگیه.
شرط خاصی نداره. ایرانی باشید کافیه
💙
یک دنیا ممنون
https://survey.porsline.ir/s/ngmblc2l</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94727" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واااااای چیوووو از دست داد سوئدددد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94726" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل دوم هلند به سوئد با دبل بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94725" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب بازی ای شده
🔥
🔥</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/94724" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دبل برووووووووبی</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94723" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلللللللللللل دوم هلند</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94722" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل اول هلند به سوئد توسط برابی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94721" target="_blank">📅 20:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چه موقعیتی داشت سوئد
بازی جذاب شروع شدههه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94720" target="_blank">📅 20:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برابی با پاس گل خاکپوررررر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94719" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گللللللل هلنددددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94718" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آغاز بازی هلند و سوئد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94717" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان بازی دیشب آمریکا و استرالیا داور بازی دچار گرفتگی عضلانی شد. حالا با چه ترفندی به مسابقه برگشته باشه خوبه؟؟؟
آفرین
آب خیارشور...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94716" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy_Xg4ahjD7sKBqWO28KE2UMObo9DxbI9sYvGSFISpaBrsypGpcZawuiRBBHXncCqbwTL0B3Nh7aVUnDlHzCdgC2O4vA0QxUQTWsBxwOJsuOWijVBw--eOyRb60OnwiCcft9Hxkao7dfgwKRNxGd8hZH9lb7NJID4lh7ZxVYZgF6gUwatkmJXHO71i0iSNvHjI3IJYKbhtXNthE6DjpFLyQxJQdVocmUrEeic0DB4Mc-ueiZs9JV0FoPb7s9HYLVOQKhZRW3oLzRklN0v15EuMxlDvuJRIEw_C4RDMiMFaODbu8HCt1P23Vf_vzRva7xMwPZBwHacRf1SeJ8X5OQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایجک‌از آرسنال و رئال‌مادرید؟
🔴
شنیده می‌شود باشگاه تاتنهام با وستهام برای جذب متئوس فرناندز به توافق نهایی رسیده و طی روزهای آینده رسما اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94715" target="_blank">📅 20:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2b5xJSA5gkoJeggtLt4ONHOI0PuMgiOQVkw3qnIrO0KAaLSK_aji4g4hD02fQXttdXPnUP9ZkwhBxieFF7bsNUQSurLiY3hqrFsb9S-2P2D_nKnsSDfxyxxMcfavboSKPM5KMlc6SkVTe7g_E_c8wmctzbSFig_35eiQ92On7D9_IBZVgluVJf0JFBBBwXCiciqHhtRir6MGRZrUN9e2gnMl-lNwOUUhb5OfO4_-7HmMCxwnCDjgnx6RYpaMK3p6rKDdqPE7yXw9ucV-L15p9tz_HIFWNc1T4tp1aOCrnmTRpoSiPpqKTUhrODKRw-42aRhuqKeJ8ryMdQMRe54lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLQ-shqA0Dk2DPkqXzsrf0Qo1rlqHIfWNrBPKbCjfAbBKPaidx_ogUXUr_3-kpDV9_L03I-LV9fjH83ZVgMVK6b6rupTdrO1v328xkfdLnakLgZnvCOEpqzxiMiHX12sYgV8q5VM6E1c1rp2cCat_Ajrjb7RqAtg19GPdu1mS5uPhljeHY05jhTN4jRhbvlW2xH1UZYciIs9Tkix998tkaTAwgsDec4MNJOxItmt55zRCTizPopjMz68u_ypToXW_EV9Fuw3C4YI5qIIv6s223HEd4Z9MNI1e31kD08K0r23JuC7a-W7TEYX5nhXk9qk-WwkXInI3iY45vArxwapuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای کریس به پیج مرحوم دیگو ژوتا هم حمله کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94713" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/94712" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-yWqqXyTjVpl6cWRyY-SluWLwisvRelHifUUPf3IDewhxzTYPfkE4_6JuS1HnWzmmdE6mxIQpP_vGrCfUubNtymGzC09jfhe-ptNE2i1lp_E-AmbehJk_1l_dSIRYRiCiSNmlHDNwY6DD4USK1B1Eor7jEdTZGsjc1XF3F9D0FKuS48AsDNOorpPXoRvaOmn8DhWkS6RC_SlX9KksKAb6OOqpOlbMwnnWsHUiqMxzotx9G_MkXo_MWWKuQ0-H6BRpDZlFqncu_qCoOb2LokEH7CRgOzVyle0KQE94trqaHeFGOPtZQD1lKcDGm4tcd4ZhbSK6jYSFb9CWFOZBQeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94711" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXfDlLe93VZqerqgIBT1xNpHonawONt4LH4vxErLzCGDyMbQJ0IY3REElNjg7jZLxR_wUF1c0KvNyaECTLxEijsadr7N3DTuUyyrbCacSyoJ2-XCn_fmO7_PCoaS8QRNqYk1MuW8W7tpoYzklUgvoipK_4RKdpBxVdbnPIvvHRPYmWh8OBsx49-dA8Sf4NDI0DZYE2IQ1OIvKdIH6ch5LSMrrrJwLbmuBaaxN65wUS5xaPmwfDAykuJL1fZMC5EYMzj8OUa6ewKFbu9LHpC9nc4SL3Kdfjty783lxw_GOczSZHJ1U6XPr8nPXVuAQKbbPKqxaNYRYhpIQwlS7SNJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ بیانیه رئال‌مادرید: تا این لحظه هیچ پیشنهادی برای مایکل اولیسه ارائه نکرده‌ایم و قصد وسوسه کردن این بازیکن را نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94708" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت اسم ژول‌کونده و امیرمهدی ژوله
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94702" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
صحبت‌های هروه‌رنار در رختکن تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94701" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM05B8QocGXAyRug3I3V8ujcPDmvS_shUkA__HHbXo_vfvMCAqZnEKmDOXO_GApgKXGk9YI3ac-L6Lo1Ravcd3CrA8xxbGyB5j9MgiifYepqUJK6NLq0KW13s8_Zmv5xvZx_VhWfZkiiUmWIUpwkZ1HJLmGOlmYvZ1R1Gpi5TM_9Vr8o7GcEmaxs9GNhZlHvbqZJkkI9VjAWbq-M4ppCM3mg7KbjJutUJb9NHTz6n0ElKAZG2aQB2vrXFUFnx0xtLOaF7JWqnwBc54q6Ont0HudOPV4hPCFAw3Nji24W2QaOrER3m-lyzY-7rpXAV-UYnZuUVKbJEXG7FCB8YCG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇪
🆚
🇳🇱
🗓️
۳۰ خرداد
⏰
۲۰:۳۰
سوئد
🆚
هلند
📌
نبرد دو قدرت فوتبال اروپا برای صدرنشینی گروه
؛
جایی که هر دو تیم می‌دانند نتیجه این مسابقه می‌تواند مسیر صعود و حتی جایگاه نهایی آن‌ها در جدول را مشخص کند.
⚽
🔥
هلند، یکی از مدعیان سنتی فوتبال اروپا که پس از توقف غیرمنتظره مقابل ژاپن در هفته نخست، حالا برای جبران امتیازات از دست رفته و بازگشت به کورس صدرنشینی به میدان می‌آید در مقابل سوئد، تیمی که با پیروزی پرگل برابر تونس شروعی مقتدرانه در جام جهانی داشت و اکنون می‌داند با عبور از هلند، صعودش به مرحله بعد را تا حد زیادی تضمین خواهد کرد.
🚀
⚡️
آیا هلند می‌تواند پس از لغزش هفته نخست، قدرت واقعی خود را نشان دهد؟
یا سوئد با عبور از یکی از مدعیان گروه، یک گام بزرگ به سوی مرحله حذفی برمی‌دارد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94698" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrXQFNHdS35nJJzUjyqx4gPwmgksjW93aaYtyuiP6rFDjTClbW35UcEZYPEe8FT09z4_NHgrmJM-Si1VUWbxDh9yRF0pGdxc_GMlTxyP3-HhXxrcnB5d8_7jldm8QmfNYB1aTJ4yiaM9W11NFRydIKRZb1oaL390WGmbWChvJzYa5pJaP346sOU1znB4B-MIK9GQ6ePErhzitP2KHNgJDOJa8ZQEKe-GLMO1xg692zcFgEBvf0WqJuDuNdjXHXT74lZj0aIxdz-_SZYQmK4L72108_fCXnGoSYSsa3HO5OWfFR3NdV1_H4BU-UHrkGC4glOeCNboXRkqw8BlUFEuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEF6C0e_lM7bUm8tpK-Ev1w7Ew_kt2gg3S5b8A5w-AfWInKLOiOGP8rwP4TtawXtorvvJKfzBKjRtMjoJXgt0F_uuWkshuq__ClkG74hqSCezm8aDxBd9L8C4gj8T-vSM0s0_uhkPraEGs9rymNiuT-nlKLw1eave36q1JvhRKgFzGwc69uGIWolNIpybInwmj_AcIMNTyfiiaC2WAqHoJXKKK_UQdlE0Z4KkpifVcADkvN66AwBfJlCHM8BUExmxQgjeAEKW9ELh_gLtWvqXG2N3iIJTQw_OZ6uHeTSrPGZtseqnm0sWO_-8oo5EIlnRlkxZYtmq_UWthKIW9jFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJI5REtV8IKJRoNEGonxRhPNniR076_6U_9JBR5lMoun_W4X3XwNfr8XxpqUYc16mO-jhNlQTslKwRXvn-0mB8HPx36FjipLcWueinBCin2hW9x15DDMa7ZaAmxSYx_meWXvGgSMCX5o2YfuzVq5bBnzDh-8pqsc3yj62tOfiW6F3Dshz4tb3NZYpV3Y0E_fPoXwsxigrREk-SKnrfzy8nm-gUUBdZdO96igjYcSM9GLKaw3TsjZ5r51yXoNIRV6AGW99oto0QflzmfOVhX3b15l7_QewO0KQYPAqeOaLXHZ_dR5f3TlHqU6noaN2HIiKIeNuQJRlIiABH6qW59K4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TVmtmetuXbkkhFbR_ZVnuL6RBAyrxY85xAbor5Atxx2G4t-2sIrQHE37bQ2C1AhTPY2jpaoHB-oC8BX0fY3jVoA5lEmM01UnVKZQbr8dUKuZPPoPguNn5hEvv7f2m8AUn5vdDDSM69jZTXyI35T4ebyp9NAwWp6eV_8CsMmcNXSpYgyzUUB0dscVMY3K6a3y500gLH9YkgDUdz1dxjW3PwfGwxRI3ISqU0N1pdwTrQti-3EFyH9UQxlYYp6wMLv6LlVYCm9NqWGmP56ye6o7UfILRTNTSOFNLKB-8YFFamr-3KktzcIMiUWOMy5Ic3lsaKk7uZbeLSg3Pwg_BfJWOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم ملی چند ستاره فوتبال در یک جهان موازی
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94694" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPy9AP02UUZTnsz4NjL76sBRShwz3NVlC6oLEBECq0Q9oG34wnPpd9NV3E9Sf1HkC7rpT7VQNLEj_U9EXeR4G7H-WprBszaw-kCt3NK17QaHQXd15qVLjqtVf1w3FINZmhVrR7mNEpbuF6HCN-jqt9YgI193HEe7q8SkiQwlUIx4lAjaUSY8ZkBcSuOi0aI80PaIl3KM7FYh7YEc1s7vb6jl0q05AwjuX9cRZf3F8ROZAzAJ64jBXCccUVc8F1ZCsQ7iILMRU2_gGpnKnp3aRfiRHwP5zZnBqb8a0r_Vvmlm4uGvu0ybn2yeG7L4KB20ZMUVD1prxLK6q1uKd05D0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94693" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNwpYhVBM2n4eqweqoltXGDh9lP789q2uU-qFJDppQSG4T-X95lh79oYx6Z_5BWF2hwLT6fFb8cP0cXZZ5wH38f5kQlxOEtHFovTYuduWZBSDhprZXRezbvfXzNT1AG28l-lwpH6RxkLE3Pj43hLafpSIsW0d07lQi0Xn_NtZr9hzr-SPxuqPFXwpw70Z9T1JMYzFbmO7lt03MqJcGLAbRd2y3X34PK7_FA2PmZvVIqEZS14pIuT4XB0j4957oaRt9fPVtxlnBNPWn55Ee6YPa5vkPHYUipyeh0Z6Dk6XM2qAZXHpMQbkQGFlipV_z7lfVHhD6EZkHBN5JCEbLBwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94692" target="_blank">📅 19:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juuuZYgbL1G9_Uq4ZVtPapAur0W6iJh0b3sFFune1mDvCUZvgu9Gk2g5N0DKfzdueF7JT73ZDxkO8BjaXgMT0PTvNgANaauEHXuwrHCwoqS9I95kFB8cXS-l5dkwfRvD6HJszqXLFqjN8pkLMxgKJkukYP02T7iYF6MNHcjVpRPxUywetEAYH9VsDaqnEc7O8Gr56SY51DaWPGq3ugQRClG0_F3fbaAaXy-T7NZunqevY-eYPogeSGPdRb2a2sNyaMkTNkjSYncyQc07AltUK6QIkylYeSoJTRgy0WY10fQlCHWKM1CWTiSkg42vzQ1v-WSA6VkR2whD8x5iWOq__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
هوادارای هلند قبل از دیدار با سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94691" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94690">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpdY5HAP-MTiqvuMkMZk1i3PMl5KqwoXgvAgf9IzdUR7DBhrOgfWsC7LQmHz4COqASZArb1NaI61F8gDHLb85xni5ODKKuoA2MCA9GmRjnoXECMgCYSIYVL-80B9UuRMdHJFuZiBXwwAwq7NL8BLCUSP8gjdtnIq34q3yoEZ7cAw-jxLGp7nwnlwg9dnZAojuM-0XvQiL1AlNE3BctKuRhoke4EQ_VyrCA5vNF1Nb7ppq9T-W2lWfpnmU9zdC-lmtmgVofNEGrJYjEhI1YwvTmCHSCWKc6yIhVB97yvlU89Uas1co_XItkPWlGEIyqTaQ2e0AchPSedsRGmo4AD6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در فینال با چه کسی روبرو خواهید شد؟
🎙
نیمار:
اسپانیا.
🇪🇸
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94690" target="_blank">📅 18:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8aUjfqleeTEkBwuUArcQC5jHt-JpV6ekZpvXnpNRlTX2PboM9vzbJP0WFkjriH4yLdnEBc4uuf4JQSGEBd3GeYaX1J5WFzbHGChtKjqOtyp-tssNd5vCsiRiC5b2cZBA7NK0lPiNiOblanyLHNkJINcqeA6cN7mVM3YMdn-57RYMIxscxS9MAKnlzIBP56nBeJK5aHzM4zwPmkMSQyP-e50xuPlIWCDHOxGkfBfDg3V_dLNf3qv6oADipiYtNX6IQHYgM1LLrVk_YoK0ZcGehbjWleTvGf5mpkhtCea3RXmQWmfTinrWcrBu7qODi0AQzi_VJen1z3t0ODcH68Ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94689" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHTtbFO5gfn-KJQyCqVL3iF8CUYkq4ngWGb9ofzULg5rx_R95Rw1LU4e3I4IyFDYe4BwpV1GtgNYScY4h5-K0VfvQGy6e9JB4VeH10DwE1zfHkWssvW_B8QTCGK3fjIjiv6GWBBQVxyHs4iwjKHxd9zXlR9aCbcxWZA-cM8Tlv16RNZ5nD702wx1EU5lIA9ybtbNyMpOO2nr7_QjUOnT0zKLesu-BuXXg1kZCnkc2xKZXbCKWqUtDjY2vUXxARLRxELBZoF53SzqRx14qg5PANrRoBX23nDUVlBLamNyJMh4bX37ryGWPCYuE8QLrsoJU4mVDCjv9OMHmU9tLD6cNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇺🇿
هوادار جذاب ازبکستانی حاضر در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94688" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsNWAo4Y3No8SkaJuN2iXh92_d4XFVLGp0DLCm4lrHEIfNkUi6FITVxpAXGn9SU7uut-jcepW0qRE4c36qHfZq9gPpSKtKfnqKtsCW-STsCf1u0Rip_SaYtwV_g0NP7P_9peMNIjRcRflaMBwYXU_4rvO1b-SrDQT8-7M0THD0z8CdDkJ7kvIBpJ8Uk_y3pUiis33G4QsoA2ZToizlEdnW6YeqKeZgik1hB2lQZCoZIiW8CPAmHHTRfC_VwEQpE-pJbUGETZMiF2cvCvJZp-xAcD48LujsTeQra2y0foeaiBHDHSk82xrhhnCdkPXRiFmCyHZMBUDv-gwlJ0Xt0Jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇳
🇯🇵
دیدار تونس و ژاپن هزارمین بازی در تاریخ جام جهانی خواهد بود و داور مسابقه پیراهن ویژه ای به این مناسبت بر تن خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94687" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
آمریکایی جماعت اینجوری لب‌ساحل کنار زیدش بازی فوتبال کشورشو میبینه
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94686" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94684" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آلمان عزیز امشب بازی داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94683" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب‌خطاب به رونالدو: داداش مگه ۲ سالته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94682" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94681" target="_blank">📅 17:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX75PdT0AH9mXt_HJRjAXqjTsO18kXcwY1fjfVUP97A96FOj8rLustSGjlQW1sJxPAhJMFlZh3EO5k8WUw9gca9MxRu7lofCMnp0JSo9LCTSGCcdjmJlSxaaUzpXGgisApoxH1u47f_HYjYA2qXQCnzdwe2E873YytJFVD6E0C0hX9-GV6zlHWvdNNJyY0a-FwjCpPJxlkSSCHSkWQUXtibj_imUslixJS-wTDLFF9v0kplfVyh4VYYqO_pdifDRGKYDWNveJC4Ejh1LtB3ioiipTDMBpetcOleFJh37OntB1196rqyQyhWBhKMGpwtEQGbHZdqB4l-EkQIwAUJICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا:
بنجامین ششکو گزینه جایگزین بارسلونا در صورت شکست در پروژه آلوارز در تابستان امسال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94680" target="_blank">📅 17:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🏆
واکنش تونی کروس به حواشی خطای مسی مقابل الجزایر:
"این احتمال وجود داره که اگه یه بازیکن دیگه تو همین موقعیت بود، کارت قرمز می‌گرفت... یعنی دقیقاً تو همین شرایط. حالا بذار یه چیزی بگم که شاید خیلی‌ها ازم شاکی بشن هرچند فکر کنم همین الانشم شاکی‌ان! ولی به نظر من مشکلی نداره..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94679" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
روایت عجیب یک هوادار فوتبال از رفتار زشت مدیران دزد ایران‌خودرو بعد جام‌جهانی روسیه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94678" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94674">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl1McCaNY2nfpXlnLzNsN82xuCp7fmJHZm441pL-fX7RJFvxfymxQf6dLYbnOHSBJEIrsgBERNDWoUv5yoSko8C9EjoM7sHpi8KHBDFRi1TjPVFxNxX5AYEQSJ09_oi8bwiFL8oDIWqC_WQDkXcb6EWozSqhB1phPaqjyGmqt3voQQ15g-eZHNjUQHx65j8KJU2_myNSA6zmRYJfwxlY9Ig_8awLz0jxlxcxlUILmh_NnFM3CEc8txi9VJYLENygeVSXVr675d15wuXO9hfJsqTRch-U4RO--8TS52ynj-uHJADhKBg3HuCftandb0mdZ5Pr0p-5nCWnVdSyvD-cqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IveCkmjXkm430fwpMdIL9EEEB_4B3_avhgnKUl_WSj4wfpSDnHxyHDFjcLzRzlOuvdXXqnxRDvfD_NC_4JBQZcjuv3x9sxTcXlc_HbSPAIBnabxl8R0WQZLwpTm1khCv6mAXJwoSGS0oOUJhAzY2jbZ3ue0Fj0EfQDHplJm4tXQ1XibjptvZMtO7u2b4mYNJEn25tRPGbTjoLCIoWeqPr04N29EK1Iic7IjweueygGsMwpcVRFw1bHM8FqGUrwvI4Uyy2GAc6pVb_z3Nd02wxdKX22Pi5uuLWat3dYiH5yGOvnp_rLPdjGkdx3pvlQhC_le-_DopyD88uRLUHqQaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxIUAM57xcTtQgltI1EA110xiq5R4PsRTDx_y7e2odXDRJMHQlGsUwBssU2ltqhH_L8RR7RgkJoyQhMQeo4nOVwm3sBguV6VBo1MA7BBP7pn8h8_t1ujFMLqLdB82Jl1A7VcHUf9cQPm_OZcdMp3naNKxtVuUzRVG9h2Tlt1Ppaej5lrxnYDAmYyaSmd21FhShdwgsftY7gcwooxGiMCeH-TcQNhtsx-Oq9SLL_JEqxa3Uk4T37JANFuri8qXYLyp5mG2V9Nb40bU0vDjH5uBJ93V_-S1P888VflabmnfV5PvZIyasctFWnL9N-omY1Z4Z-EwaiRRLgMhtUagtKtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5Cp6jFrdX6Qku6px4Fbb6ItHuj-fMpr6QCpSYSAZnc99PEAK5rlhwuWZr-uB9cHsRDB-P32C6oaX23s5GzuZxrRXKsnFs6kZ6wkSYs6-nr-uiuSgdb1GYyDgyNa2swcb0CSb1uC3BIIUAIzVO-RXeaA1XCsyYX1of9SmHztl--N7iwosdKDjJ4xTkD_yd_9fvYutYW9KPDVsHX0gcUzoBM1uktpixCZPTO_AFReTIdREpD-ICNpUWnpq4C83vsT4Lzw86WgX7Rg5tBcStQENJHBlvfKQMCyqJIy4pt1ANzq0d3QNnGPTkacnT41_kWvz-8pWKtGLDBdAklTt_ZoCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌐
اولین پست‌های لیونل مسی تو اینستاگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94674" target="_blank">📅 16:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فوووووری؛ طبق اعلام قرارگاه مرکزی خاتم‌الانبیا با توجه به حملات اسرائیل به لبنان، تنگه هرمز بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94673" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94672">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇺🇸
ذوق‌زدگی این‌بانوی آمریکایی وقتی کراششو دیشب وسط بازی دید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94672" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94671">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEENWu9ZfVG86dpHInLDoKTkqAc-oeQ11qllJYpe0DbZTu5sjoTkycnBPet_lXQIv7lym1vvgeouoVl95w-PEscbt-st2kd0X-vtnck6Zx4L0XP56M2f-0JSNFVmy0m0ZcbX4uEab6zKeulSMsrck7cE_VJbMIbjkxRg2y4MK0IiWXt0K361mb4JrZy2JmC1seifWTz6vxCOChr6ryz1T8cKHnmCdnW3uaLiJ35M6i-Bbf6PumuLMJuJh4BMLnDtkyZJjYrfIW9BC2WMmiWExtp5uHmf5W4hDJdFjJLJVD0LTisHO-cOzSpXnCjUUco9mnk2JKhEAMDu9kkaVSTIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کول‌پالمر و زیدی تو تعطیلات؛ ایشون پیشاپیش توپ طلا رو برده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94671" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
سوسن پرور تو برنامه قیاسی: ژیمناستیک خوبه چون میخوابی پاهاتو میدی بالا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94670" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👀
🇨🇦
🏆
در و دافای ایرانی مقیم کانادا که شدیدا از موفقیت این کشور در جام‌جهانی خوشحالن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94669" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94668">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
بازیکنان آلمان قبل بازی امشب مقابل ساحل‌عاج این شکلی تو فرودگاه تفتیش بدنی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94668" target="_blank">📅 16:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94667">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
وضعیت عراق حریف بعدی فرانسه بعد شکست سنگین قطر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94667" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiMFsbcvxBozwhq3fs4fpe9qCyOkLrAy1T0ZsYgVOJRuuPV81kxx1bMu2Lv-_HHzuNTfFcNxdVvWIk4jZsoqhWBzFth2QfPDcT4X6AqdcMQZGNL9Keg7fcGXJVxfGOOerX9owwFnopqr_m-qVsQ0FFes-FRIYaDjaqvyN_jQZHLLIeU38GfJLOh5REMPDuCgO1eYbZ4XRZB1SlF89nSvwTr9i6TtwBaNJ13F0dm0O9ggxEs_x2O4dpk1GpqLRtSlOJJM7XAgM7zWYLAfzyUn9RHY9y_CueSxlNdQc2t8j4UiKL5EbDYaLSUmnoWlrLQUDzVH5hOskGuAPx7lUIJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
پر هزینه‌ترین میزبانی‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94666" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3LvZOD9xu46K-b6gPP6UgnXtVgj1dS4hwDZ4E5GtwCIT_xwBrBJNToxTUd9SlysQZpR5p7erXPHAr3o3nTqd4vJ27UAYM05ITv8XMDHwRkuMBlXgcMG3Tt3OgxXdqVJhS7nQsJfmnU9gnckLKrMeE_f9Gl91eYJe8__NS42k_L44uRP_jZjSji6BbiVVaVuP3nOzd5V0-JgRUXJIRL3wrDOZIL0q5nFWL8ziZ0ovm0NMMaABzonS2sDgMpG_k3-jC_B3bpm-I6fIudEr9TNhCbiH1HyD_0-OEwff7H4MHC7I6E_179OdXscYbyjiyH1JBWfTPaPonU88sJ5Ini6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🟣
رومانو: کاسمیرو به اینترمیامی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94665" target="_blank">📅 15:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDYtt6N4-up1cIOoUFe9x_rpFQds2nT4iTVw9ualcP1_TysON5m2D_XMba2WrdENkTdg7xQ1PePHRh285dUj8eoPc85qT9ra-V86dKwgieaiHIV1HjwP54yDJFA9ZGMyWIyBFC06OpueXLw5s8Wpz6mseO2tr-EPdiAbXed4yCbfJYB91cSJdEHS8VfioeyPN5niwgsHd5fcDSYA5UVw23zn52LMx0LrOm_3oDYZ9QYCprfKha6D4JFvJOEHmfw5Qk8JcmgJ9Rm1Myr0MmqhdulAeYWBmfrQX1nIjx4pr2aiufbcHzeKCGZldglnNrpimELpreKzR0utOszhu2q8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توی فیلادلفیا مجسمه راکی به مجسمه بدشانسی معروفه، هوادارای برزیل هم به این شکل رفتن کیت آرژانتین تنش کردن تا آرژانتین بدشانسی بیاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94664" target="_blank">📅 14:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
فلسفه کولینگ‌بریک جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94663" target="_blank">📅 14:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94662" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94662" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_5wygKxvHXbBsOnhhpieV4fNqXswX3wXDOZE7w0FEBVtbTaj2FcLnQl-mhNwmNoKn9m36ntoIvCX6d3WHwmaYeFsY-78KuvEvTI4XDkO_RpgON0SjE8s_XOUbRbkpF6K05AItAF4sF83AXPpkXBC9bqylDqI2yIBQDyqHGN16TxMCp_L8kKnU4rQmSWTIjWYzVEtS1WrHDxSZm2EHkcJ0aRZKOulPje_CTeayahTgiHIdrZmDcTtYSi-y8oCEsjmXm49ur2yWQX_5aEqHgNvT5xNEYAEDJZhHApcD2GsBqctk_nMZCx_Qg9rLhBV-TnArTBic6Bs3gbO3ZjzdqL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94661" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94660">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
انتقادات شدید مجتبی‌پوربخش از مسؤلان فدراسیون بابت تغییر کمپ تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94660" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزا در خیابان های مکزیک چه میگذرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94659" target="_blank">📅 14:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎙
🇧🇷
وقتی عادل فردوسی‌پور، حتی بعد از گذشت ۳ دهه از شرکت در مسابقه هفته، یکی از اولین قاب‌هایش در تلویزیون همچنان به برزیلی‌ها و اسامی کاملشان علاقه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94658" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPxCRsudOXG1VcFyDdfZ3NOEaV6Gmy58Kv9YgQd8JXAwN_8J61L4mYCaY3S9qYFdN8Vnqvzih9KkHweOgSPGTSCnXDPtNgIJ0Ss7g2Ey5O6oGNjzLZr7CKVT3OiGWQa3oxaHIfKhJCa3e6t5fEAoxk_3XfuiO0yz95m9fEBFNhFNKD1YpBinMvgvQIRLxRDkAnsnu-NNcPamMXfRxFiL8yF15aSpOp4LXqAU8VDOZbAfuauNJlgOx1QJ0ofU-4ElfBU1FiHwyg64hmZlntEgrJS19Zb6VxDFipPgifMznQa9MgRWjwgp4mVWqZQ11SLG7FBVbXYz8LzfP4dwopz-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
فابریزیو رومانو:
آلوارو کارراس این تابستان در رئال مادرید خواهد ماند. مورینیو با حفظ او به‌عنوان جانشین و ذخیره کوکوریا موافق است، به‌خصوص که احتمال جدایی فران گارسیا از باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94657" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">😐
❌
فدراسیون پنج ستاره ایران تصمیم گرفت که سهمیه بازیکنان خارجی لیگ‌برتر رو در سال آتی به ۴ بازیکن کاهش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94656" target="_blank">📅 14:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI3IICUraYlgjcGVn41WSuzX7LZecoRngpp7aor2ND5M1DIhsurbLq95XyyLpSRZQXpzPTlJHCplU7nMkjxCeh-hUW6ekAOrPzgjqJug7OYZzDrkKnjct0O94aUBGKgEee8KgzJlz94RpDt5rzupBgcZ5LLEs5Tu-ByC975Duij8TAaUk2ANvA6xLHRlzmLDXc_acCcKw3V2_pe2IUINB_0lzO2-Gd2ByR0f_5go8QmPg8TLM68XEjvsOLkEJBtXX9mZaQGqYwNDR4kwl_NAzPvTwIsU9ArjlSqe9iy-njEKK9OcI_cyGEt-q7vWeDwM9IYeuSnzzIt26np2UioBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووری
؛ رئال‌مادرید بدنبال جذب هینکاپیه برای تقویت خط دفاع خود است. آرسنال این بازیکن را فروشی نمیدونه اما در صورت رسیدن پیشنهاد نجومی ممکنه نظرش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/94655" target="_blank">📅 14:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو عجیب منتشر شده از مراسم محرم در یکی از محله‌های تهران
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94654" target="_blank">📅 14:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38da867d39.mp4?token=peCYCzJ5WpmTWkAMdaC6tH_qBnJoU2jlNtyI0sFcyXrZyiY9d84EVKMO-mU6BEBQFAQgA07U_57OG4uXdWvmQq57yj0tRXIbrDXdN1wC2OdtCZj79uvMBcTF0I526h-HmszFlL4P0bPveu-jJPgAWbv08drIi5FsttUhWFVCghUJT3EKUadmZ_AeQgDB-gR61CTiCzPf5d0TugIzjth2bWeH2uh5jIFUq4_urms8YhCNot1OJbuaITXsxYF6_dO1EIJK8pMT_HJI_8ZswF-18IyLqt4Lp6mYntsUeKWP0i9IwSKgQMviC5JI0kN-ymiFGBHFmVZIxhNUNVbbXNKXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38da867d39.mp4?token=peCYCzJ5WpmTWkAMdaC6tH_qBnJoU2jlNtyI0sFcyXrZyiY9d84EVKMO-mU6BEBQFAQgA07U_57OG4uXdWvmQq57yj0tRXIbrDXdN1wC2OdtCZj79uvMBcTF0I526h-HmszFlL4P0bPveu-jJPgAWbv08drIi5FsttUhWFVCghUJT3EKUadmZ_AeQgDB-gR61CTiCzPf5d0TugIzjth2bWeH2uh5jIFUq4_urms8YhCNot1OJbuaITXsxYF6_dO1EIJK8pMT_HJI_8ZswF-18IyLqt4Lp6mYntsUeKWP0i9IwSKgQMviC5JI0kN-ymiFGBHFmVZIxhNUNVbbXNKXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇹🇷
حیف شد ترکیه از جام حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/94653" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🇰🇷
درسته مکزیکی‌ها داخل زمین به کره حال نداد اما خانوماشون بیرون زمین حسابی جبران کردن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94652" target="_blank">📅 13:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=slMntuTI8s6FysBntWcFkEQOJqPN2bVdnDUa2mUw2UDe9QEr_LUDBdQYLao1s0m3OUU5b3rqXqywem_8KD1ZBosOlZjx3-2HUNZbw1DmD2RUJDVA4jAm-M7GTXPLqs27dEJ-CUkeB4HwORafWHSlc-YPZ3k0YuYQE66SoUf1ex1xh8wA9d-P2dyDCrVc9wS61lBhKDB6FWUVRuRkRbDR2bWdY3am72IaWY_o6I-w_PDkQn8o3zOs6tsxdP58XPmZAETlSUQzSLThEc8k1fQG7ZaWOErqjsPrmm3s04maY-QuossvT6T5RK-O_x-_1LGfZ9b9gOS5UX2mvn5ckb8MRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=slMntuTI8s6FysBntWcFkEQOJqPN2bVdnDUa2mUw2UDe9QEr_LUDBdQYLao1s0m3OUU5b3rqXqywem_8KD1ZBosOlZjx3-2HUNZbw1DmD2RUJDVA4jAm-M7GTXPLqs27dEJ-CUkeB4HwORafWHSlc-YPZ3k0YuYQE66SoUf1ex1xh8wA9d-P2dyDCrVc9wS61lBhKDB6FWUVRuRkRbDR2bWdY3am72IaWY_o6I-w_PDkQn8o3zOs6tsxdP58XPmZAETlSUQzSLThEc8k1fQG7ZaWOErqjsPrmm3s04maY-QuossvT6T5RK-O_x-_1LGfZ9b9gOS5UX2mvn5ckb8MRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوشگل ترین بازیکن جام جهانی از نظر خانما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94651" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vao1o4f9I5xrQL_VxUbu8iN5KqRSwo7hj2Ln4v8H7tb8oTwP54hDkhCQfLSkbQU6EQLXu0V262S1yYUjEIuHPV0-pSscvWrswGXRFlFqKTl4fRYyduUkv31SwMT5OryZO6-P-J8__Au-sPrRPzKiYYseesQl0ZCqyjC8pQg6vTgqXDzCfE0VRfpfj-Q7Wz4qPsOawx1BITO6FayBoxFMJtRuVNI5HqHyidoPOObrQ_fudA3Fz3dtbLD9NK4f6dWRxL6qddUPat3lc7LyfsFFPZ16avKrbPlV7-kHL5IQiK-tx9PJOPB_GFB9nKH7u99QletP02dKRSj_0N_beIuGyRxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vao1o4f9I5xrQL_VxUbu8iN5KqRSwo7hj2Ln4v8H7tb8oTwP54hDkhCQfLSkbQU6EQLXu0V262S1yYUjEIuHPV0-pSscvWrswGXRFlFqKTl4fRYyduUkv31SwMT5OryZO6-P-J8__Au-sPrRPzKiYYseesQl0ZCqyjC8pQg6vTgqXDzCfE0VRfpfj-Q7Wz4qPsOawx1BITO6FayBoxFMJtRuVNI5HqHyidoPOObrQ_fudA3Fz3dtbLD9NK4f6dWRxL6qddUPat3lc7LyfsFFPZ16avKrbPlV7-kHL5IQiK-tx9PJOPB_GFB9nKH7u99QletP02dKRSj_0N_beIuGyRxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏆
صحبت‌های جالب یک خانواده اندیمشکی که هفت نفری با یه پرشیا در سال ۲۰۱۸ رفتن روسیه تا جام‌جهانی رو ببینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94650" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94649">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=QObxDdsdtgTLZSJy_PGrfUJ_1RRvnMfcFIUsN4gvmMYeAkMVj-VKEeFxG52fGYXTABawOZVLS7Zxz6qKoWwFlzDc5Q0N8yrOtXv5O0fB37tRraNitoIEsjvMCgk9ghtOVxwV8OdMgXa2JhhHsNQc9236N_CIVaZ7U6MsjR56t-DnWHrFsfoyMMRrEEgkqEEqfrDCV-n9PgC_pA4mjY1K1kWQ8sH-wCAWAoNe_TF5zteapzeCoTzzUGfTqLfRIzvp9n_9ibF_UcwzdRXO9h8dycXibeVUIsZWaSRfZx87A3l8Q8_0XrwwFKMudOISs0lgjPM0VveqvCLvmAtZkpZjrhKerJTsEFNessw6tdm5HEgf77PF7ubUD67lcJis899I8Ebw_gk9tTsathYcqYOIVSSxydQxrAuQhxI43bVVcqIeY-JCni3H3FQyNlHHUjpmhKQT7-CRfral0KIK03ocUDRVkfn1ZOuyvpk8xYH4w5qhpjUQw6J3JjJqVRBBTmZ8bB7Qj-MI9ZlME04qeb_i1_UQD0RphzIH_x6lWctssx1Cwt9H-eoZVEafHKYle_gQx2gMO__iTtIZzowxM5ONQiQ7rzjl9H2yOIwj7jrWBywnGwMyJYqbe6tX4CeJIpM6HxL3fSnvR4duL7G5uHdOJkkSMVtz_1Gq2MJdOzCPqjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=QObxDdsdtgTLZSJy_PGrfUJ_1RRvnMfcFIUsN4gvmMYeAkMVj-VKEeFxG52fGYXTABawOZVLS7Zxz6qKoWwFlzDc5Q0N8yrOtXv5O0fB37tRraNitoIEsjvMCgk9ghtOVxwV8OdMgXa2JhhHsNQc9236N_CIVaZ7U6MsjR56t-DnWHrFsfoyMMRrEEgkqEEqfrDCV-n9PgC_pA4mjY1K1kWQ8sH-wCAWAoNe_TF5zteapzeCoTzzUGfTqLfRIzvp9n_9ibF_UcwzdRXO9h8dycXibeVUIsZWaSRfZx87A3l8Q8_0XrwwFKMudOISs0lgjPM0VveqvCLvmAtZkpZjrhKerJTsEFNessw6tdm5HEgf77PF7ubUD67lcJis899I8Ebw_gk9tTsathYcqYOIVSSxydQxrAuQhxI43bVVcqIeY-JCni3H3FQyNlHHUjpmhKQT7-CRfral0KIK03ocUDRVkfn1ZOuyvpk8xYH4w5qhpjUQw6J3JjJqVRBBTmZ8bB7Qj-MI9ZlME04qeb_i1_UQD0RphzIH_x6lWctssx1Cwt9H-eoZVEafHKYle_gQx2gMO__iTtIZzowxM5ONQiQ7rzjl9H2yOIwj7jrWBywnGwMyJYqbe6tX4CeJIpM6HxL3fSnvR4duL7G5uHdOJkkSMVtz_1Gq2MJdOzCPqjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوری در باران بانک کشاورزی، از برندگان
۹۳میلیون
تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94649" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=WvDzIwmBP_KcdJpM29-U2Vv2K02EKcvH9DMiHi7SvO6QdWUL6UJxP6cVmDchHxVVcQ2-JG-sZf-xqAktmzX3okp1uEkATFDSXftPv0fphgsaE1wn12vH9FC58nEazfpU-1ScLnT145ABKNWtTWLFKfSqHl7XYbxoWqyEUPMOr2BcdY-4cobyoOzWk6zYiqSZLRgVn_VXV6yAz7QdGao5vj4Dfl3ok5SWMvrObyxnyLI9M9m6dDITEgsQRGOL3ZMJHmU_Bzok5QmIPjTMnfFiFAsCXv0nL2s4N1a6JcbDZLUNaWhY9Q9e5BLiVkp5KDJbmmN9S0cSZnxixUn_FD50WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=WvDzIwmBP_KcdJpM29-U2Vv2K02EKcvH9DMiHi7SvO6QdWUL6UJxP6cVmDchHxVVcQ2-JG-sZf-xqAktmzX3okp1uEkATFDSXftPv0fphgsaE1wn12vH9FC58nEazfpU-1ScLnT145ABKNWtTWLFKfSqHl7XYbxoWqyEUPMOr2BcdY-4cobyoOzWk6zYiqSZLRgVn_VXV6yAz7QdGao5vj4Dfl3ok5SWMvrObyxnyLI9M9m6dDITEgsQRGOL3ZMJHmU_Bzok5QmIPjTMnfFiFAsCXv0nL2s4N1a6JcbDZLUNaWhY9Q9e5BLiVkp5KDJbmmN9S0cSZnxixUn_FD50WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇭🇹
چالش هوادار آمریکایی برای منتخب‌ایران
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94648" target="_blank">📅 13:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=AT2sKUp4r-pV-dWw8LLf6z68WFJflRwVH5a-YLu7NmnV5nJpqAQuxE98FKAlvZ42PIG6FsaGH2S57boKKgbnFEYI0xpAXwPRFTEpgs9rhJ2UZzr4BYfD3zhSMO0UfbrnAF3I_9dedZ1gSkO0GUwQOYPca5vt0-iMOscY-jGeKPoH1ajUf1Aj3h-nlqdiIw6i3HvWweposjunt3omqSbrkmgFkGOB1K4O2cnFE3U1J9cVQPBCcw8WwdXRIu3huYk-H3twOOMegLZyprLInG6hKLyf1LcqAcnzvtB013SSywB31zbBwSRKfxOkiZ8-2h_OmeAOxnrvD70anDq03QPvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=AT2sKUp4r-pV-dWw8LLf6z68WFJflRwVH5a-YLu7NmnV5nJpqAQuxE98FKAlvZ42PIG6FsaGH2S57boKKgbnFEYI0xpAXwPRFTEpgs9rhJ2UZzr4BYfD3zhSMO0UfbrnAF3I_9dedZ1gSkO0GUwQOYPca5vt0-iMOscY-jGeKPoH1ajUf1Aj3h-nlqdiIw6i3HvWweposjunt3omqSbrkmgFkGOB1K4O2cnFE3U1J9cVQPBCcw8WwdXRIu3huYk-H3twOOMegLZyprLInG6hKLyf1LcqAcnzvtB013SSywB31zbBwSRKfxOkiZ8-2h_OmeAOxnrvD70anDq03QPvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇿
🇦🇷
رسانه‌های الجزایر این‌شکلی به اخراج نشدن مسی در بازی با آرژانتین کنایه زدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94647" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXNevojVWnFiU0XhsIY8fh-0SYBiRw1T_o4gQTgoH5o9kL6BSumB1PmDiyHcg1s0R1Kw9x0MYphd9OcqEWNetcqOgB3v4ETKLknkJrD8aHvt3kmzpGi2hq6sK8Ar3biVHmzCj4sNpJLsHeN7jWXIB2f_grQiC97O4oBZmjdDOIRvvq5ldL_cagtXJ5oQ3ZMb2lcyQQN3CLI3aYJBgKzeAaf-LbrHntntvZKVe97N36arHZGPt2ZseVBfq__e81YB-aYAQtWB3sBhwNLDNY2ahHeUCD0rSu6P1WxqzmvXxszE-sIGd6EIK5BTC3pOnUCkT9at1xKwtDRMBRXu1NKPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
آردا گولر:
در دوران بازی‌ام با تیم ملی، هر کاری که بتوانم انجام میدهم تا این جام جهانی را فراموش کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/94646" target="_blank">📅 12:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=Nlsc7sXjdizoP6QYKyad3vYV8T-kpkEVQQj7sBtjQtHUjsNGad_CEnM1R4Rk_Kr5USiut0JUgXtAst0P_xufWbni8lV9YRC-Y9i9aO6P_Sh0UhhM1ATPsEp-GzNim1LMP4rwGPMyYh9R56iC0oZBxY12ykuu6BNjtlDoxaaYsL0HGxCobGJxaIV3ityfjxKgHYx-GY-fUkFPlwA11PHJaKyM58TnavVlRl6Gj8Gz43z1r9b6E82JzFQJD0VhQyvvfWZuCLZZwvBNdLUelFsX6yoVvGocNF1OW9vg2N85SSerij6BIWMQVtSrtoGgHyldIzA-enYeppplhpNh4Ktapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=Nlsc7sXjdizoP6QYKyad3vYV8T-kpkEVQQj7sBtjQtHUjsNGad_CEnM1R4Rk_Kr5USiut0JUgXtAst0P_xufWbni8lV9YRC-Y9i9aO6P_Sh0UhhM1ATPsEp-GzNim1LMP4rwGPMyYh9R56iC0oZBxY12ykuu6BNjtlDoxaaYsL0HGxCobGJxaIV3ityfjxKgHYx-GY-fUkFPlwA11PHJaKyM58TnavVlRl6Gj8Gz43z1r9b6E82JzFQJD0VhQyvvfWZuCLZZwvBNdLUelFsX6yoVvGocNF1OW9vg2N85SSerij6BIWMQVtSrtoGgHyldIzA-enYeppplhpNh4Ktapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
اقدام جالب هواداران پرتغال بعد بازی کنگو در تمیز کردن سکوهای استادیوم محل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/94645" target="_blank">📅 12:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
لیگ‌برتر فوتبال ایران در فصل‌آینده با حضور ۱۸ تیم برگزار خواهد شد و این فصل هیچ تیمی از لیگ‌برتر سقوط نخواهد کرد. همچنین بزودی تورنمنت سه جانبه میان گل‌گهر، چادرملو و پرسپولیس برای سهمیه آسیایی برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94644" target="_blank">📅 12:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=fYjZtBwkVTzf0Zb6CMug_ESAkv6vRkhoy5oZoMOt9SkLPDBLaUjTZmcXdMAdIaqnUSJue9gQox1_2TCJF2MpZ0upG2itQyvtcxnpi7dqV6DGV5AsftETbJdvsqf_Qg6pJGxcikx8ntzAIHzv3Mc2iEpymmGv3HMKSlI1a-WQkWa5xvSQN-GaP-MDK9zebHSaW7lpGZ_ao4g7LhNe7nTcdl6LXSX8rpWG3xh27IHttE0lrc6-fEdjgqZyg4zoELqxwyvxdtxEtNfLav3OGPp0BeBxARbDjsRskSgP_CmQzFFo56_-PgVo3nXjU6utMx6CMLQdvA0tP28Uf9tvnP0pRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=fYjZtBwkVTzf0Zb6CMug_ESAkv6vRkhoy5oZoMOt9SkLPDBLaUjTZmcXdMAdIaqnUSJue9gQox1_2TCJF2MpZ0upG2itQyvtcxnpi7dqV6DGV5AsftETbJdvsqf_Qg6pJGxcikx8ntzAIHzv3Mc2iEpymmGv3HMKSlI1a-WQkWa5xvSQN-GaP-MDK9zebHSaW7lpGZ_ao4g7LhNe7nTcdl6LXSX8rpWG3xh27IHttE0lrc6-fEdjgqZyg4zoELqxwyvxdtxEtNfLav3OGPp0BeBxARbDjsRskSgP_CmQzFFo56_-PgVo3nXjU6utMx6CMLQdvA0tP28Uf9tvnP0pRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
🇺🇸
صحبت‌های جالب هادی‌عقیلی درباره دلایل رشد فوتبال کشور آمریکا با پوچتینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/94643" target="_blank">📅 12:01 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
