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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 697K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-96595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTPm4KVxjbJLfKTLE-m7qYABWXToHF5n472dm6WXve03gtydC8v4ZXuJYhY2gT4wAxquEkjc708hN3KID64oNH7OUiVgCTjGnTdlTgPTWB2Q9COSu0EOmW4DhjAUTQ-qClsd4vJfgrVVtDP7XJipB-cvbY5zhiUwK4yYnUjcYDq2Ia5Hs0M0I3wToQOKh-SJ0GdFsP3AWCmLerKzy1IvNnTB4kX7lSwg5GH3xGAhrGz3Kqk2MML7DqH5g9siUHMlBRgOh3Md_RdILEDgvWbFrxTks1KIsE3ExItwkW-icqJySdks7wGFG0V51x-E0ybB_NORs0at_KBmxpcRZD8big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/Futball180TV/96595" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
ایران رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/96594" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قشنگ قلعه رو سکته دادن</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96593" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پشمام عجب بازی ای شد</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96592" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اتریش مساوی رو زددد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96591" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96590" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چه دقیقه ای زد</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96589" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پشمام الجزایر سومی رو زددد</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96588" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EgKzbpfzvt4NPFL4Q2mfA6hvmTSBGbQdJR2_uhphL3_pGspL-iQIrREA5NyA4uo8_rz9OOvb8vmvaYifGTQ6tyy9Huac0LR4-qfjo4mC5eqHGNXF6t8CvZSgMTqF4Nrc4WX0iwFJUFq3Csq9dRMpUU8gi8D6dcyLMEhNrysmnbigIk33pDnora7u-8n4SCMrWSDTibV_ubbWnOv-jrQW3BgeU-6wzBYdhQNJNOGaWxLd0nl8JNtqFvGa4nHHmIU7yxAX10f3iHIqEaHG3DUE4q01j12CXX8fA7-uM-EVKtX2U-YMPUTQRkhHuYdEuNr81emxsVlJ1bsQcCC6Ynnj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HFKjhkUaSudenRFKqusI11lYA2A7E_tElRLa7DE89K1QgHpc4boQAU5szIyXnIGuhTgaVx2SsMUpmEDkUi8WAh7YxQXoNXHvKzVNK5Np8ozDidyu1_GNnk86QolrjNDwwqLIECSN0MgZr_UM1fcbftB_set28XgT01h_SXp_4lavPjs7rgm5YYFTJVbKDfZ--heQ9Gnr9-a9egKFAt2glgfYs2Ijce1__6yhmwa2_QnISqkg-rGkRRVSiO7amnHW00O6_h7x6gVxCPlZLj0CtBm4diDF7ZA4CfqczumxDB2IDv2p0oKQr3bcgtu6euO1fACFqs0SpfIYJpxRcoJ3Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی مسی و بانو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/96586" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHezYqdEY11DmNJJLGCWz-ppwp1qpzbvCypS1Tr9XHN-ur7sv5LlqvMaGoAmTtrreydUA7nqDrvi14ClNRhRB1uFxDEMS9UD9LQKz3MNlAB5WM1hnvjGv0lO_CqGiZ8JcCoqcK56VYHW5BJgcVGgLzkeOmpiQpFGiz-X280zlQSTiJTRPHosLWelkaRKCYK71gMNnaiPHHVKyxnAlhcu4QLg9ZlOYVZpkgorkZD5MugGX8iocsYABbVhiD2SFzIqW08Rj8srx9mxaMQaU13j6xYVfui2CadwUQocruKa4RGnVI1QScSETqZgTU5Io2NsaAZa5a_aai9TryIkVuGh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
1331 GOAL & ASSIST
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/96585" target="_blank">📅 07:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=LxjRpFZPW7WHp9563XTnzp-MDIZqsdU5lZ-DRkACeHmnv5crbHmUJ0mIlUBTnIFvZcyUMCnhLrOao8GdoUIAj-Svf8AlFYqEQtqB1ujIFPnJcTjLWnVFLgv-x_B0V6q0KdBGZpOswdlpy5OxcFJjHCVKw2O3pUDCfBJUraktAeYe8xROMOmQCXq6_uyD6rwnXhJs0L5AlnuWOoWpq6mdq3935q0l8myHwVNljUbepYrG7iB_Fs2IIkoJxnWZULGXQk4uBJFtCSHnaBg60rAzEhangyeozjI3ktQbZqXVmu4vvzHWt_4OZYBl-6c2pre_cu4MV2K6xnSych550YOSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=LxjRpFZPW7WHp9563XTnzp-MDIZqsdU5lZ-DRkACeHmnv5crbHmUJ0mIlUBTnIFvZcyUMCnhLrOao8GdoUIAj-Svf8AlFYqEQtqB1ujIFPnJcTjLWnVFLgv-x_B0V6q0KdBGZpOswdlpy5OxcFJjHCVKw2O3pUDCfBJUraktAeYe8xROMOmQCXq6_uyD6rwnXhJs0L5AlnuWOoWpq6mdq3935q0l8myHwVNljUbepYrG7iB_Fs2IIkoJxnWZULGXQk4uBJFtCSHnaBg60rAzEhangyeozjI3ktQbZqXVmu4vvzHWt_4OZYBl-6c2pre_cu4MV2K6xnSych550YOSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل لیونل‌مسی از نمای تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/96584" target="_blank">📅 07:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udv7rfXWdlWEh9ojT8tS3MxCfrDA6llhwai28FPVecKH3SZp6q9GOMYbwjuyE2lwuq1CtWxe3pxUEyeyCghhZRF79J1HLzOXXAWTsKjfDpThX6eBvidJdWwn9-cn-sx5VHKyOyAyFNnlqUeABH-Lsi4pzs7QdmK00TUM4MWXTt3NMGp3aDN3QW4e9UCkUFst808iZQ7vXUfWjQuaXLHomqz8zp7FjRjQNFrfSDS3hb4pendKnzpXajUgLJ56Z0ydVISog-M4LcJ0VctlNCcqDxaXeX9wVIQt9ra1YH8tQRItkTus6CM4zt6IRyVx0uvJ7xp8ONQbP3KvsrJe1dgwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/96583" target="_blank">📅 07:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=UQpRCpGhUtEjeLU-B3UqW7liSD4LnuNhn62DddT9rWBYhbSTAg4ZBohXgbbakY2MqXjlOyXuzdJyENncQT5KoH3nPWUyM0bx0YFSLw3hZ9nI8BXzW0JaAt6ywj-g80rKzw7-DGSUXUzDjB9GubF4jwK1dM75iSU9xVW7BUgs-RUo-_FmbAPTuPHd1ZIeg269wsiTIHTKV4bm0y2tlPqkBi6p1_afWqwflGwqMG03l4Wmh3Vr_XGlVOQ4gt6O5Nt71Uvw5tADNRhIKw045vvG4tTDXBaRYzBQTrGtRxgIFiy7lueYbnlK6573yoX1WY_AvG-X1CCikDwl0rPde7IEDqdzBuzKBM5k9uuAuRlim7UWc2hFHD-_QEm72J_-IrHBJayF_TghQadq4wdbJbIbaTL1Dq882cY610ayuHpwJCerDUa0npYNXv0X2QXPvfgFd2RoEEqquakhHR1rwCGLZQ80uZRYxq9_hJe7sdAhzck8qcZuOwF_WuIpqjRz3UQooR9YYXk9rvVw6sU3UcJDzwr3BKjYOceeDiLT2BIiu4YV9kNPXnyuQ807sN_7O-HgxRyiSnskMkHolKcNjrbcurXY-4SEkSbq60wuMe-ZRZEE-hCJgr2vzPmHYmsC5T7_rwsWbeSNFU094wMRyNrPNov1Tpyhe2SQi2U8Uj0yyYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=UQpRCpGhUtEjeLU-B3UqW7liSD4LnuNhn62DddT9rWBYhbSTAg4ZBohXgbbakY2MqXjlOyXuzdJyENncQT5KoH3nPWUyM0bx0YFSLw3hZ9nI8BXzW0JaAt6ywj-g80rKzw7-DGSUXUzDjB9GubF4jwK1dM75iSU9xVW7BUgs-RUo-_FmbAPTuPHd1ZIeg269wsiTIHTKV4bm0y2tlPqkBi6p1_afWqwflGwqMG03l4Wmh3Vr_XGlVOQ4gt6O5Nt71Uvw5tADNRhIKw045vvG4tTDXBaRYzBQTrGtRxgIFiy7lueYbnlK6573yoX1WY_AvG-X1CCikDwl0rPde7IEDqdzBuzKBM5k9uuAuRlim7UWc2hFHD-_QEm72J_-IrHBJayF_TghQadq4wdbJbIbaTL1Dq882cY610ayuHpwJCerDUa0npYNXv0X2QXPvfgFd2RoEEqquakhHR1rwCGLZQ80uZRYxq9_hJe7sdAhzck8qcZuOwF_WuIpqjRz3UQooR9YYXk9rvVw6sU3UcJDzwr3BKjYOceeDiLT2BIiu4YV9kNPXnyuQ807sN_7O-HgxRyiSnskMkHolKcNjrbcurXY-4SEkSbq60wuMe-ZRZEE-hCJgr2vzPmHYmsC5T7_rwsWbeSNFU094wMRyNrPNov1Tpyhe2SQi2U8Uj0yyYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آرژانتین به اردن توسط مسی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/96582" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مسی ایستگاهی زددد</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/96581" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/96580" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مسی هم به بازی اومد
🔥</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96579" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=FuY_0BHz_z9eJ8JJJQsjTyuWNsB110y8Tsyiqo9ougvwywJpJPwxcXWfNKS_mpMbIIF3aPfR88b4vqvFNXeaQ9MSSEB7NhYHmc-n54va1lb0D8zO8y-rQL_ZP2CLBImugYb0LuwCNzDX3sI281yusurTERPVy5TJxGyEFwZ4at0eNQnT4134eBg3n5gIeS9zZJorNyi_jYwFZJqQvN-aLJ_CGkPXKMLVxn76WEoUEFiXnkeEXutZhipSPi1PusXZ8sxoZU0aZxxNxitH4LtDmkOo7KFfdBaEyUIkrA8igra5gfHV8dDSuT5j8wYotHXpwZw57tls_cWIsi5JtdwZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=FuY_0BHz_z9eJ8JJJQsjTyuWNsB110y8Tsyiqo9ougvwywJpJPwxcXWfNKS_mpMbIIF3aPfR88b4vqvFNXeaQ9MSSEB7NhYHmc-n54va1lb0D8zO8y-rQL_ZP2CLBImugYb0LuwCNzDX3sI281yusurTERPVy5TJxGyEFwZ4at0eNQnT4134eBg3n5gIeS9zZJorNyi_jYwFZJqQvN-aLJ_CGkPXKMLVxn76WEoUEFiXnkeEXutZhipSPi1PusXZ8sxoZU0aZxxNxitH4LtDmkOo7KFfdBaEyUIkrA8igra5gfHV8dDSuT5j8wYotHXpwZw57tls_cWIsi5JtdwZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
گلللل اول اردن به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96578" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الجزایر گل مساوی رو زددددد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96577" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=ga1QEVY7n2JMg-y2SoV_uX_nKFIwzOSmtz7YczgvJTEobFQXj0KkMTP3gG7zkeyXExUOWRkAClMy04L602tvtN6UeviMoL_BvkmMCr3RWiKXetU36rIRCJDpnxBCRjAeeBg6C_cYMEuvdWcNMiqFCJ5BfMidVzhpIlSC6P_RRyCyYf0gQ1T86ifnQx5nQtkNpCAQMGog_dBhduNzfjPx-KGCOJUeUWFrsPVHaRRyV09VVhE_kmkPjYeD_r568HdIMeD7k6MjP2siFVZenFylGjVMzHJJ4Gpozc4wtqP0j8wcd4AsIA0m7XYrqhKFR1HGePauw9zQzPtWPBFQqRLtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=ga1QEVY7n2JMg-y2SoV_uX_nKFIwzOSmtz7YczgvJTEobFQXj0KkMTP3gG7zkeyXExUOWRkAClMy04L602tvtN6UeviMoL_BvkmMCr3RWiKXetU36rIRCJDpnxBCRjAeeBg6C_cYMEuvdWcNMiqFCJ5BfMidVzhpIlSC6P_RRyCyYf0gQ1T86ifnQx5nQtkNpCAQMGog_dBhduNzfjPx-KGCOJUeUWFrsPVHaRRyV09VVhE_kmkPjYeD_r568HdIMeD7k6MjP2siFVZenFylGjVMzHJJ4Gpozc4wtqP0j8wcd4AsIA0m7XYrqhKFR1HGePauw9zQzPtWPBFQqRLtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل دوم اتریش به الجزایر توسط سابیتزر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96576" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/96575" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سابیتزر</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96574" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتریش زد
🤣
🤣</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96573" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96572" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اردنننننننن</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96571" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/96570" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/96569" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzc3anQ-v5Ol07qfxaUVLXYoat20A_ONUgK42giBjk0O4VAD9z0iR1d3Iroaw8fIh4r6H9I-ut2YAMh1bKV0OBOuWuViaOpm5MD7z0QPYpsKp0bkQp3l36UpKtSg3wYvmQjiAwE6ddFyJnuHGHdB3HChqUwjRP1bPPoNwNl7BXLWb5sSoOXQjcQvOCGkb8xTu_BYQEADHO8sBNRcvyvtQ3BQLRK-pcOwouuHRB94FvdbiNdOuwpU1JePEY1u3XMZLFVarGX4eT_gVL_s65PO1HBkhsLd9xqOndXsJwh-rcaIifpvK93zRmfs6NHUgAXhZWcAEAlYy4bdAKgHba5nGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی داره گرم میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96568" target="_blank">📅 06:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96567" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/96566" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گللللللللللل</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/96565" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPvpD2lJo-f0R_NgMnpGJwUJQ3Qy78C5_RoaMXe-i0icOv5Iw6w1l0aAKJOhxe16uOLO7orvR4yN4S3ApUM-suq56_JP01MyJsHayQ6-oIjrfxVvkGtY539BToXGMqfygvfxgygTM4rz2QH73HQ-Cm6CnQgIQ5J-kqq3zxNqWYqiFW_Gnm2wN1ZJd1JCyllUdHzhL-RdohcfKDEZmF6z-Pg2r5EHObSUoG0Ywv_zsEkQSKHhLpBHStKpjbFnhyeIEPzJelMt6y8N-qjGhMjZNSK6I2HULqiDfmH2JvOR0NDfh2nEE4SNDVCBbdKxXRfbWgpP3YUNv6ZQFxZTnI-RrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
آرژانتین در ۱۰ بازی آخر خود در جام جهانی ۷ پنالتی کسب کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96564" target="_blank">📅 06:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوست دارین شاگردان قلعه‌نویی صعود کنند یا نه؟!
بله:
👍
خیر:
👎
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96563" target="_blank">📅 06:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پایان نیمه اول بازیا
فعلا با این نتایج ایران حذفه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96562" target="_blank">📅 06:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=F-zd4socyNLAC0o1P5ytkUSqGAuqeyvJ6Vpxvfgs5MlFMIpWMolDlSE0yRKew4HggERDkuUhhwab6DXksOHi_HXcX4mWlF0XE0Czc0ciLjUYm2YxJqhZyc3Tu6DJ8hIYJcgA8gLIIpjJscAIeS3_OmfLj9teQOI8JtUPjEftce3enLTXNfKS61ixDZfhiDuQwnVaIro9RC1SSSI8Ip8DnYYR8a7TqFqOt1mxVSURwI3WNq8C5a24uJvfSg6n2o90NWcVWC8zX3_qX7QlFcgH6Ip_bGMgXAxQi5KsWZuYQqiB2JajzXLLOseXTOuAEBq4QynFdzBk_JibzOT1dKAoyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=F-zd4socyNLAC0o1P5ytkUSqGAuqeyvJ6Vpxvfgs5MlFMIpWMolDlSE0yRKew4HggERDkuUhhwab6DXksOHi_HXcX4mWlF0XE0Czc0ciLjUYm2YxJqhZyc3Tu6DJ8hIYJcgA8gLIIpjJscAIeS3_OmfLj9teQOI8JtUPjEftce3enLTXNfKS61ixDZfhiDuQwnVaIro9RC1SSSI8Ip8DnYYR8a7TqFqOt1mxVSURwI3WNq8C5a24uJvfSg6n2o90NWcVWC8zX3_qX7QlFcgH6Ip_bGMgXAxQi5KsWZuYQqiB2JajzXLLOseXTOuAEBq4QynFdzBk_JibzOT1dKAoyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل اتریش به الجزایر توسط آرناتوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96561" target="_blank">📅 06:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توپ خورد به پرچم کرنر برگشت.
همون توپ رفت تو گل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96560" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96559">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الجزایر گل مساویو زد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96559" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96558">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ریدممممممممم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96558" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96557">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDyNZf7K9BjjynHgTpyu4YKzri-i33H7fIgKvyFcDk1LJeYvbXiJy8Ac_FDh58NkVQXWrOzTCeRxrkVdoIB1nwoHMi4b-jBX_iGhZDU_-dtEv9GE5G0SW1Zx6dLFmsSDu4ZK7arbdeHTwLVD3emv5eJcbvGJno2keCEtDQXTcYdLMANGyZ3gnO-B5IreK0v8Qt7YbSbXAen035pQh-_0n8CEv1toFuMNr3fu7KSlkelySkiJf9DY5I0v9R9h7eCLsR5cKs7t9F16rcNrL6Se0bqoA0VYQCKyy4VUXeltwSFa7eVsgHiX8Tq3lDMOdhfY8a95oddzBLsTja9Xrunt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هوادارای آرژانتین تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96557" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96555">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4AiqBswptrsORVPswhogFssNe7Ic6ISrAVd9MItnFDYKI8HkPQ2iKbn9lQx1Uz5uEOq5-ltN2ba_Nre901E2fjfsjJiNFk-V8ewb5cFrK6j9Pi7UkuRb9qnlp4CFLe7j-_yy6qyWgotMSWSdNNQL3F_au3PMUMdtU3_XJi6JCmxioeqknvSBi3tDkweNBp4NrYA9pXjPihjsCcJKJ1ja6OaD2kdJFsemvZ2VCT06cEfQ7V35r8cSdIfWhHOYdDFa29EhQqnZmOtD-xFjIVZNBsRdm874Dl5S_y9vQFtrtqScgqmUYQ_Suuot53BKh8RHouDzVjzUNMV-McGac2JdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUOl1PCcYEtjybTxl3topoLNYO4zab3hhNvNvbq-JQDs4w_C3wtHxsiC0S8xHKF0fDBO8-TZAM3WGeJk6SqCHAzpU_1rd6IABsV16KD4cuPyYrjdBNpYrQcv-yalXg0gbh5N5UB4nQ0XHrHoljlvwWllbKex1nH1q0gIsZQjM_xNoWwjspWE7LJPbKI9JdlqOLGuSt2eRefsW7Wp1itVMvQQL0HCO8jH_HbfHyvBU6ywTsnZhjfj0qdv59e370gLyXqo33z1xEUKENUk8OJ2gn1_JpJ0DTnO7B0qtK1PIXKiWIYDkTqXnB6XkOm9XV2OLG2-dn9BAaachzM5Etgg4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🇵🇹
کریستیانو رونالدو مقابل کلمبیا:
🔹
0 گل
🔹
0 پاس گل
🔹
0 ایجاد موقعیت
🔹
0 دریبل
🔹
1 شوت در چارچوب
🔹
2 دوئل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/96555" target="_blank">📅 06:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96554">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385982be9b.mp4?token=cBj-zHwjQMoejtGdYQ5LieP_aTTThUC-lBd5gg72NPMAqTMgYkCzNBqh7aOK3sx5hfWr3Cbl-rOCNvQjXJnFRrTAC18W1yTvU4IO9r1wCDv_BJGKwjzNSuEJ-QObK0fIAAoDR1S_XqhV_vgBBckuJs45-pnWxs4YmlRPHx1gZ6WaxFxjNlP7CCFpz4d5LM3adLczGRhJA2GC7BEi6JlxJLgY6cUz_tHIkGr9pn3XDSG4_XYq1e30JFnpUowsPn_F_IyR9cWqDNdDA7tZ7dmROMe4-x80FE8kHqXwQgEFkV9DoxQnxxNIKqKtzHW2XELyZJMjgHa-QtDBL6PqC-KAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385982be9b.mp4?token=cBj-zHwjQMoejtGdYQ5LieP_aTTThUC-lBd5gg72NPMAqTMgYkCzNBqh7aOK3sx5hfWr3Cbl-rOCNvQjXJnFRrTAC18W1yTvU4IO9r1wCDv_BJGKwjzNSuEJ-QObK0fIAAoDR1S_XqhV_vgBBckuJs45-pnWxs4YmlRPHx1gZ6WaxFxjNlP7CCFpz4d5LM3adLczGRhJA2GC7BEi6JlxJLgY6cUz_tHIkGr9pn3XDSG4_XYq1e30JFnpUowsPn_F_IyR9cWqDNdDA7tZ7dmROMe4-x80FE8kHqXwQgEFkV9DoxQnxxNIKqKtzHW2XELyZJMjgHa-QtDBL6PqC-KAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گللل لائوتارو مارتینز به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/96554" target="_blank">📅 06:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4889a222.mp4?token=JhmYGzMS6qYb2EVeUQq69nWXJkf4AX9VOLHkIwPL1IiIImoJMtNiOUqTzdDbBhu16v50B_jxUcZLLpp0nEkHqpjmS3_d52Xo8qwLIkKDJrAzA3uO2UWxwUOZYC9mP8RfHKRh_NXcJ0dze-zaSEq1kRTGL6HVMWiXMSFoM_wMd3lId4AjUygf7Lw9kpMp-SRiCbWIXNU4xUdoalPE5jI-z52OtH864Svdel4XcjFwOgNBuqrIjEGBXoLxkPV4jRaNeyWbY1EEKP3Qdrn7VPuQ_orFSBw1Z3BYZqWsQ6e0DCgvJJZIO_iGhHdRLUMUX-E3Ag9sSulZGvke6-rXFreHIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4889a222.mp4?token=JhmYGzMS6qYb2EVeUQq69nWXJkf4AX9VOLHkIwPL1IiIImoJMtNiOUqTzdDbBhu16v50B_jxUcZLLpp0nEkHqpjmS3_d52Xo8qwLIkKDJrAzA3uO2UWxwUOZYC9mP8RfHKRh_NXcJ0dze-zaSEq1kRTGL6HVMWiXMSFoM_wMd3lId4AjUygf7Lw9kpMp-SRiCbWIXNU4xUdoalPE5jI-z52OtH864Svdel4XcjFwOgNBuqrIjEGBXoLxkPV4jRaNeyWbY1EEKP3Qdrn7VPuQ_orFSBw1Z3BYZqWsQ6e0DCgvJJZIO_iGhHdRLUMUX-E3Ag9sSulZGvke6-rXFreHIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل اتریش به الجزایر توسط آرناتوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96553" target="_blank">📅 06:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/96552" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96551">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">لائوتارو پشت توپ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/96551" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پنالتی برای آرژانتیننننننننن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96550" target="_blank">📅 06:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96549">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آرناتوویچ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96549" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96548">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتریش زدددددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96548" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96547">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96547" target="_blank">📅 05:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96546">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnXg_p6fGdjPeb9PD0T7H0tL35LjHXs2NFG8q7sSw1nFs5UeTpgKNn6Pd-dX-NF-odcHnlb0coiYKdAlF-IKkwxeyx9O3gYFY7DsnS-XE6_IU7FS89h2hbjirkDU4C9Dc3xr87jf5rQtf2uIEFc8oXLuu8kU8JhecE4JPDv3qwXwSwyXvlLBxS1iFLByzHHxvnoI0hK0nUmrpOj4-fI6AD5q8vusr929hi6SUdl2Gc6_6q61wvQtUr-solFmD2Kot64tVceJ639KDzaT15Dj-PRNiZUr5lYrYyoMTKgzpciNxMkh50a2Zf9rGqiTZlAwDurV49Npdczc3MFT_0CkNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/96546" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96545">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e86b5b3cd2.mp4?token=AxWK8eFZXDOZd1vjT1dihIpyZoUUmvZq5OMc_aSSZE2eZvxKPUspX7Z1YnrC7hcnVVg5ihnWGIpiXZPb29l6jATL6v4vcUnnR9PHCYqTKi9IOmkKzIp-KLmGx6aFVoK3DqaMzuj68WNRrLyz01s-nxte4W6S2C-6Y4MpK6xS7J-qL4OBLvHWn79VKwWr_tMJHKIlONHGA32pVjawAm4NWeTX1HfIisdmWXu93FUPp6sJsGpcyh7PZcmWMuL-WTidZrfsNuO5Kbnf3w8iupBM3v0yicXb8Tz2sNUXa83ckH-nozpIiEpTdk2AGz9zDj-actZJ7oy8a4XwOI_rBAMdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e86b5b3cd2.mp4?token=AxWK8eFZXDOZd1vjT1dihIpyZoUUmvZq5OMc_aSSZE2eZvxKPUspX7Z1YnrC7hcnVVg5ihnWGIpiXZPb29l6jATL6v4vcUnnR9PHCYqTKi9IOmkKzIp-KLmGx6aFVoK3DqaMzuj68WNRrLyz01s-nxte4W6S2C-6Y4MpK6xS7J-qL4OBLvHWn79VKwWr_tMJHKIlONHGA32pVjawAm4NWeTX1HfIisdmWXu93FUPp6sJsGpcyh7PZcmWMuL-WTidZrfsNuO5Kbnf3w8iupBM3v0yicXb8Tz2sNUXa83ckH-nozpIiEpTdk2AGz9zDj-actZJ7oy8a4XwOI_rBAMdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپر‌گل لوسلسو به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/96545" target="_blank">📅 05:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96544">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عچب سوپر گلی</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/96544" target="_blank">📅 05:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96543">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لوسلسو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/96543" target="_blank">📅 05:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96542">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللللللل آرژانتین</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/96542" target="_blank">📅 05:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96541">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آفساید شد برگردید
❌</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/96541" target="_blank">📅 05:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96540">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آرژانتین زدددددد</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/96540" target="_blank">📅 05:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96539">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/96539" target="_blank">📅 05:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96538">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMTE3c2K4k9EyucCMkRy-rfeyDU8rRTO4YOFwsf8G9Po8R_43nV0DckRjuWYK5JDrE7dl1VjyxXExxPFTWsm2qqlMsocPhwnXIv_Sr_H698dao-rjUTqvdB7aRmUaeqsrZWdFYbpCA8hUfl2ScMTTzSgLJxyDzbqlaPvSsaNdkWxleaQyJU7tYZsFtP57gkDQdm0aBpzxbs06VQWGleXvFvcjF8wKwSOsHSJIrBKDSMFw-POOGvjULEKuX1AnBeW-FDc-7ZO-oi4kjF-Cu8L2zlfTNMWDPA3woXJYNA7npOBjwIJ-l7TXMnGr9FwcP0Nsu7qhqV4HuCaZUm0G5c2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
کریستیانو رونالدو مقابل کلمبیا:
🔹
0 گل
🔹
0 پاس گل
🔹
0 ایجاد موقعیت
🔹
0 دریبل
🔹
1 شوت در چارچوب
🔹
2 دوئل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96538" target="_blank">📅 05:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96537">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بریم برا شروع بازیای آرژانتین - اردن و اتریش - الجزایر
🔥</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/96537" target="_blank">📅 05:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96536">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm6HKJR8rODinpNVeLjSCWBh2tJ_PQ4CDCMpH-U_5G9MtF3usWgb5WX9t4y5WSJZrP71YmGhAsC4-S74fSWh6fESYMwgX9GCLrT4WWAX_ymLdQYg4rbNh-bsx5_-xi3lloo_Al5dwsb4QKRooZ3kLGJNSpoIMzvY3CgFT6ycWfxQ2C4Np9dMoB7WhBAEhhbu8jisJfqTuWfBkBKEKoZ9BqJ1fbSghBc0MbSZH5pz7i626uhJC88Y-zHbz19ojQV954cgzrXBwGIedH9Lbm4_f0eQ5be4GjKgrtZI0WH8wkgqjFgtKJ5r4YFAaXnw0Lni7mw0zGl5TVUtRwAr6bDPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاستا با 6 سیو بهترین بازیکن زمین شد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/96536" target="_blank">📅 05:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96534">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idsWQE0kVCE85lhOc--aFpQg-DIpYJ7dj5zDnw3rezti9EVf2WM_ECNvWu5oy6HO8q0JKZVOJMqGtyLP9lb_a2oliRbDCxrzqauzxv4ys-VzVYDMX5mHYpuXfuSBpWlkuZFw5Sksa-KB7pQsHdld7G78T_Z-bUJyasyRjsiyNUnD8SLFfiJqTC2r0zR4aJE2d297RFYKxp9l4rYOXyncT6PtVJ_g-aB0XFK4E4yQ2Gi6XfVGw3ZRUV4LA5MXjQArU4Yp_FqhMsUWNIeY_VHThRF0hC_67fxu6kkjpUOPgxysr4jFf98p7v7jbeW9D9oGBfHr6d4tLsEfLEB8eVcxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSA9_JRuQFOSEkVC4W5kjCQPVnlsQqlsz8rG8pmxDcQuKdDllkkqgf23m77ufRPxYcw1W2f4kggkRRYSRHoU-CTKVexy3bMXdEwzDpSt24j4QUSo8wn8sI5Qz72fT-RYl1cQTEnvqJ8aOlqGbwBoaE_IcgDkPQdHgForbNB9RSvKGryn-D5x94RhQ2bhW3Z4kdJoenU2SGZwI6i_1xiy_e6dEOl8frkhrPXngCs60vGYpi9mYDFKKqEO-mRKRrpR8vM76GBLVexDRae3hD9Oyb1c4cBUMA-PYCKYfEglmjNa7FMAyRnH1Xndi2Wv9bJYkJt58IEbydyI0ERY54UEmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
مسیر احتمالی پرتغال در مرحله حذفی جام جهانی:
🇭🇷
مرحله یک‌شانزدهم نهایی: کرواسی (قطعی)
🇪🇸
مرحله یک‌هشتم نهایی: اسپانیا
🇳🇱
🇲🇦
یک‌چهارم نهایی: مراکش یا هلند
🇩🇪
🇫🇷
نیمه نهایی: فرانسه یا آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96534" target="_blank">📅 05:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96533">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7mW4oZGpmF3VSkdXAph645HKrlamd05phXJTOA3Q0vMz4g5PM1SUNRbkZGZcbZEc1CKM-JlarswXRxocZxqE-XU0xpa1qMGSbWczjQDebuyjgnGwW4ZwgiS4oWqcuoVRoXhAlWHB38h6fD29w4m0oPPmMOd6eU3I-V89eVh1IpPcSqphL8vqAEeLRma3Ypf49xhiSXpt46t8j9aNI38fKnA7U68mZJbCuMD9q5DIkHBDS69jXIvIDrWFbnNvHMrbqWd-ncspYQwkmkHVoRsw1zrfksxddDsd8nGDZBcUtvsb9Xk5HxxFZHnFCE3DqoYZ33RPgrowFFlKFdj0u1-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسیر احتمالی پرتغال در مرحله حذفی جام جهانی:
🇭🇷
مرحله یک‌شانزدهم نهایی: کرواسی (قطعی)
🇪🇸
مرحله یک‌هشتم نهایی: اسپانیا
🇳🇱
🇲🇦
یک‌چهارم نهایی: مراکش یا هلند
🇩🇪
🇫🇷
نیمه نهایی: فرانسه یا آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/96533" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96532">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2B8t6QfqqcyH2vPARHRgpzzJ9EpSEwshpr6NsxW5dt6Acqi8Kt1oFn1X1Lg_wKJLrqb_k5XKrEZ873L-l0byY6e_NopNzlwbCzw4ScJ4wZEXcbyyrRR70KR6wkr18hN8diYua4V8dCsQaT7PHGk2XtLp3wkRwVydxGH9fleqZ-_xowcYkVINwspKysOm5GrPlCOJcAPqx-KAJVoh3AyKYEn1B0L9NHyReHa2MRG7RhQu1nDqmNEkZIMZECWnG1htuf8j6slSJ3o0WCtjTxNXbBb1HlqQDxSSzszO6oBey-897W3kyXVdXSbrLEh1RySsvJ9xE7sqtcqsbASPKas8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
براکت مرحله حذفی جام‌جهانی که دو تیم تا کامل شدنش مونده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96532" target="_blank">📅 05:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96531">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdy2R7V9xVLzR0MlA-f9MTpAET3OdrZ2HXY6ytlb0M6ZMhTinYCvW5SRvXu63pdeVQW01p00sow9bbtbtmOVEMxe-RfyeOv5iq1CHMf9ky968frYce_mEZyNcOScqPXFlOoShSTRhMrefdxqG3JiEPh1TjHr6s_PIkRTjh7vNFan-6jKYFR_8UJL7tmgARp1JPh1DIIt5X0CsP9qIvrB-7sdZpbLaJHzAeqwiQoGuNQhvOQNBCN_dDCWnBuSizegUcgVt_fKjp9d0UL4bbS4DMI53EQw-Dqxxk5OleQYrwGMgjjM1ddp10Ns1rzuWIeXLICwZhhx-wcBRyfCH1qdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه K در پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96531" target="_blank">📅 05:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96530">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V38VEFouLo7a48XXE8xBivN1ra8DffCti62_FgXhuVVYikvCSUyz0i9kjs-xqdjJjt3L7jRqdv2IhnrmcSHJqjAXqqcWOfVzVaqUFkSMTVGtjvVzgMb1AMTIdOwe4hAOLwv_UYlOGaEqwlvViY7ULzxZFI9HIG8aT2RBmnF5NJ83KZ4ChXt8jbCgITTVgTPPcht-MkEIF7dVfxrstB94caZb6yga4C_iy_Z0IRHAZXRNk1q95uw418X1j_xxhgSKJUXl30MSsheuf7Olz8C7ca-Idsd-NuJ_LPjTJSIHWN5fo1MX42iHCWhiLTf4gy8rEz8eUuwjakNWXBfCMfRokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | ازبکستان و کاناوارو بازهم روی اعصاب امیر و پسران!
🇺🇿
ازبکستان 1 -
🇨🇩
دکتر کنگو 3
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96530" target="_blank">📅 05:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96529">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_5G0MXjh32opiLy261PBDLpcdIEfADfM2GC232B5cpwDwGN8x1w14-nBsLdYoZVRrV-ZCJtiJbnSS9aW_ckKNHpCAbv4FRDAaD08CZq3oAriFS_bwWk9pseCj-X11OPEDeVSetQgnrhYAW062lXy-J1H2Fm6ld-cYEYkm0e906UvlBvXZWDsQ3lyMMLX6yAySrJaQnXZmf4LjH67NaOF-GDagMOzz10jsdhKRAa9zPt3jM5ab6k_lol_5IHE9YH_9nm0fnbgGFnimFuGAq7bUWMm298MemVnsdrCPyRWH19B0GNGpFOpoUU6lZ8nVmOnJ4cz10OlLUeU7qZRjiLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پایان کار مارتینز و شاگردان در مرحله گروهی با رتبه دوم
🇵🇹
پرتغال 0 -
🇨🇴
کلمبیا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96529" target="_blank">📅 05:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96528">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaSv1dcUSl9lmejlC4-f2zgOQpAy03O_U5aysKeR_robUm-AN5hv5AeHZe2IImKLL6TwAV47O9HolDizgWZK_PKypAIuaqRX-_1tEhUysj9Tu1OmXCaPJKFXyqMd-gpvgnGIQJxH2b1l00FfpPCkI3ErUqKjrTs_p6C66BuyBzyyjGOth0NpNQ4OfCzbImraSqCPEnzKyHMVakavCaOA0M-7tqjCO1oe1fISgeql_tUwal7qgDey7vCNEJLmP6Gslhx7hSuCNne92GOKhviODe_YQicAz-ETJyTP5cq69USQeIYCfEyouH9XUgB5hlvkcPfCBG2JiR6ZFXpS7lD_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گللللل کلمبیا زد ولی آفساید</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/96528" target="_blank">📅 04:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96527">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e3af31a5cc.mp4?token=A3TuvDTz-MDMUkjiB6wDmNDuRiVO5rHQM4OJcmJVm_OtmFKebm7-5_vCZP2we6UG98Bk9yGojw8z6n2GYAWrvnuDXvVKr4V81oZTc_SyEAH2euiN5PSYFb9h9nFr_R3AUsDb9TBvWoqZvNgYgPbgQsMUf7Yo4HuVYY7fF_dy_8qJbshvxm7A4MTjbcfOgKxtxEB4hXl3BnMDpj5gbhpkt3d4U9Gmd7wDtmagLzx0GV3JzAY9uZKJicZ9GkqvrNYVh2lmKP303seo4vEDceO9sDCeH6ynNbssSQx07NmIhcuMAT7I1pkDtXGOAlDmrTSQa4hotsveteq5QClJlj1Mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e3af31a5cc.mp4?token=A3TuvDTz-MDMUkjiB6wDmNDuRiVO5rHQM4OJcmJVm_OtmFKebm7-5_vCZP2we6UG98Bk9yGojw8z6n2GYAWrvnuDXvVKr4V81oZTc_SyEAH2euiN5PSYFb9h9nFr_R3AUsDb9TBvWoqZvNgYgPbgQsMUf7Yo4HuVYY7fF_dy_8qJbshvxm7A4MTjbcfOgKxtxEB4hXl3BnMDpj5gbhpkt3d4U9Gmd7wDtmagLzx0GV3JzAY9uZKJicZ9GkqvrNYVh2lmKP303seo4vEDceO9sDCeH6ynNbssSQx07NmIhcuMAT7I1pkDtXGOAlDmrTSQa4hotsveteq5QClJlj1Mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇩
گللل سوم دکتر کنگو به ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96527" target="_blank">📅 04:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96526">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دکتر کنگو ترکوند ازبکستانو</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96526" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96525">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سومیم زد:)</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96525" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96524">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96524" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96523">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کنگوووووووو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/96523" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96522">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گللللل کلمبیا زد ولی آفساید</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/96522" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96521">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d4d020a3.mp4?token=pgQP5AXKfUM6Ti545Vk-BlfDvNh93UcFeI-NIBhDTHPb9ZIN7vQhCw0uqaafCafi0QQfNlFtOBUQN1uwat0iGmSOyfVw7h1KFUkI470xPJcaEL58LKDbHZMVM2E3IQxuuZsvZfjhRVcjkzrHBc4k4ikk5U0R4kwR0TrlA3DlPG1B6oE73z6uVmovAyiSEqrKXoAEoP4v0Hw_awD8NX_pd5B9J-D6VqDj8o1rskkV-hdfFIBEPZdOmRCm4DpX1yPk_8Xm3j5nd0q19sla5-EpEgxhTZLfr_WS3q6C6pCy9u9s8PoHEww6-3Hc1ZpEmSNObqclkRjxOA80kx_2nmYq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d4d020a3.mp4?token=pgQP5AXKfUM6Ti545Vk-BlfDvNh93UcFeI-NIBhDTHPb9ZIN7vQhCw0uqaafCafi0QQfNlFtOBUQN1uwat0iGmSOyfVw7h1KFUkI470xPJcaEL58LKDbHZMVM2E3IQxuuZsvZfjhRVcjkzrHBc4k4ikk5U0R4kwR0TrlA3DlPG1B6oE73z6uVmovAyiSEqrKXoAEoP4v0Hw_awD8NX_pd5B9J-D6VqDj8o1rskkV-hdfFIBEPZdOmRCm4DpX1yPk_8Xm3j5nd0q19sla5-EpEgxhTZLfr_WS3q6C6pCy9u9s8PoHEww6-3Hc1ZpEmSNObqclkRjxOA80kx_2nmYq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇩
گللللل دوم کنگو به ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/96521" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96520">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واقعا خدا داره قلعه‌نوییو میکنه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/96520" target="_blank">📅 04:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عجب ریدمانی زد خط دفاعی ازبکستان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/96519" target="_blank">📅 04:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کنگو دومییییییییی</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/96518" target="_blank">📅 04:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB8wmd8DyRHf4ZOSz6hUEQ6Ffi-kZh8G0Xgd_2bm02jQMIWl1fbefrOuRb2opu-XcQD7l8UXKXTd9bWmIdlVtXi-rf5-XoYTH-WordaUXTVhlaa-6HqXNH4K-q3kozslnMHxWOPFFx-WwhxtC0_BPY8NHLIuD98bkwh2kYVqX34iueFORoaMo3rB47LHMcf0Of4KipdQZptAX5WZn2htPq7hnw7fa9iGtDIJ7F23TzUEHkUKB-y44je2MyWiFf3yssitWeGQQtz72dBJz8pW-N8W4MFzjbeNUVEC5-jr2idlzd7ofvUT0lMLqnfp7uYkc3HInrv_dlW8xDI_Jx_psg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانیه یا جنگ های صلیبی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/96517" target="_blank">📅 04:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خامسو کشید بیرون</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96516" target="_blank">📅 04:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلللللل شد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96515" target="_blank">📅 04:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خوسانوف چجوری تو سیتیه؟
😂
😂
😂</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96514" target="_blank">📅 04:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشماممممممم پنالتی برای کنگووووو</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96513" target="_blank">📅 04:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPPm_v9y9-4E7LRkgT0SoC9WB4WlkDeNYGao3bV98Bhn1jyG_bzadHah0jG78wJDEGKv11PYTu_vr6tmiogIJXWN2Eb-bX2lYK0o_P9ZXB38ZO-CqRAhLYOGerrm9i6NYmbsZ-ePewiaij5p2x1RiVSAbw8vic1QqhF644Sy_WJQ1beZEdmb3K9z4YNq3iDX_1ww_MAEDJuEyRlUTg4QdR4V3Szzy2XjtgP-ECUeXXNp909Cutj0WnddWRW026W8d4OLdOWhwgeTVqLLRvtAUPwKn_fOAgNzDsBfdGzq2gTfCmcNTUNuxIO8j5AwdybKOiRDjOuiwosWkihZ5Oe6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e653LhO6RuNmAGs_Pn3OTLOztnonME3KaiXBMBTjCEzQWFMvxiJSwtn0YoGVWCM3byf0IOowU5bsu4UBjnsDLV6rXxkMpx2pbZh2rT29wOTSgpNqe2p9s7ebdLKmuQUwFBypw_b0tvAb2vHRUBkx6ZeOaq1bV8yP5tgU1GmxrUdDlCqSHsYrJEv844cyJEqbOPv5D212saKyLRPO5jCeTeoEa82Z08ZVNqnr5rZCseg3KNDd6I3jBgCx_OTdSOggMhAuhQNxGhHtFHYAcB8eBB5he1L5WzLcHHlTOras_UpiJfD2gTX9NVLirsbQd_8PuAI50eojnliSRNuyWxwxQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو مادالنا عروسک ژائو نوس هم تو استادیوم حضور داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/96511" target="_blank">📅 04:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96509">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLQGI2kn-traWpsaTNHHmtbvcr8_-h5qVMJI2t-1MjtwEtqfeYB5HqGEbvxl8Bc5BhMB_00yYi5sJOfNxSQqwf1ZwhVxVZz3lPB5bx-HksKicemUKr6FpjVe50iUKDuotkA6dl_hUwhxhm7Em13xrlVQH0MjHZ2x--msoWaZFgS53IEQlgzR52CrCz3NuSaaOGQR7oj_gRrgP2IM9jGD-yBOVJUDgQm5fbLEBaaGZIBeQMKQwflMgTGtS7fZ8pep-aCH6Anup_Yjm6Xmg-LV5iX6ERqLWmirvVygVLwTqHHNlBrX17nqs6ZpedaOaa3KErO2PlKbkU3P0_O1_Avr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iy9WBpQxWzRyPttwmuZnaxSmie34HK_KcQjAqnQiAGCquVoB24y1pvjyB7nvicfJ-hWcPI33pIp7BZouHV9UtbvC-vwQMdDsmTXoG1j-MZImOxXRjSx6KzYiRMtsfFY6p_6SfPPsTNTyoJFelu_5g8UcJ4OtWPaNd06KcdO-2TEI1ouf7h1fpwRSE2XWPK4ZoMjUTevKoOvFEakvhn4H3kp4WllA8B-PwJTmJWVlOv8lE0u6ql1UPKnn0qafEtOF0FvOepJiAaHr87bgtH7XuOxmijGplQOAVCiZA5PVq78B4cCJ7sAcLZZGxnSyoOnYn3O4l_rd5i56x2fDwAyPPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇿
🇦🇹
ترکیب اتریش
⚽️
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96509" target="_blank">📅 04:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بریم برا نیمه دوم
🔥</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/96508" target="_blank">📅 04:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpTHRvb52gM2IyxOaH2gYsZqRMeSrV0x_E9dHZ5oI9V27gj3DBubkMnt-znu_QDJIAE16x2jm_HFlQArzOL-EIJAkVCjB3K5bQKBb82QQe5vN1tkumNRodvq1F6ysDZTW1RTz79Wu9gtjJ3TWLJudEDqxZx9-lPNsAEoiX7THuRuficOG6vo8Dc95afwUUYJbHT9HZOlj9zBBR_22sb6kM9X913pCoHgViMGv7gOAwff1OPmZqaEnaFTkXouoC3CEY6NjKhTBYfw2IEDzMRdXaIbS0QlNPaCllPchn5bah3JGDucQFyzxeWxPJcVFXUjuVu_DKxCjOr5DbIV3Rm1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظریه نامحبوب: پرتغال با این سبک بازی این جام جهانیم قهرمان نمیشه.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/96507" target="_blank">📅 04:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96506">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/96506" target="_blank">📅 03:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96505">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-dwINku4bPRf66yWg5AuNqkKtqDYvrXakbN3G12-Uj0Cj6Wnt4Y9mvGZLUw2LGa933Tt8iinLiSCHF4O3CPZW5kq9NIrDvYjCjFKbSUGnt8_6Tjg_TuxdN-G6hma0bDG_LrKYvL26GZd84vtvMxhrDzL_Fem5BUVcwaL-EUdFG32VQpwM8ONOwcJG-p96rsRh9UoZafdMZU3loe4cymG4PCftgt7moFRzKU243MPziCqeVZM9yB_UxV3tT9kjicQ2h4lO1aooHdxfZJADTLpaHdoptgSfNIjEINtlpOj9ihPwspwsQq9cDi2yAqQL65jcqQg3vmzDT5GTlBbc4A8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب موقعیتیو برونو رید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96505" target="_blank">📅 03:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96504">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfmpZ-iLWzaoAoj0_QUCXLGXzwfpI7zRp2cFSnWIx8Dt0k-d7YGDAgG0IbK3xUgBLHG3Nb5IU3lVr0i5kaH2-a3YekZcBCA_HtlVr46OE6j8DX_nq4-Kpaeh7D3mN9aq39e6btpFtE4lH21GZiZ1LVKaz0MOOYkmA4meMJ3qqvcvZQuCiuNkq4PuOmBM2cuU1ENkBqxUKIYhLT3Q7Y1wk08gq5vZZyp00dr8MJFhUkJ01fG6HzEKeKNB1cqeYgM9G_-pgl8kKZtGcnChU9ayXO4-x5uQ7fy5LDQt2eNW5ki6mGQxZEHxv5TttP6pDLM5DMqpeXOV8dofPGa-cMiteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب موقعیتیو برونو رید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96504" target="_blank">📅 03:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96503">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cfab8ed22.mp4?token=Yn4kvdO6j4tOCI8UxObt7oOzG1KfwJy0k3Aynhu5gtFw3z0gPA7hGZgkKpAmVfhXzrNWoripU5gABtNwtcutBBmmX4Wy8uRaGLwwn2H3XktxGUJmz_GjyBCbZi3pfRLJXyzJBeXpuSenTZhe8wmaUP1unbFNFJ-zR-ocYCFPbxpE9hwVNXDXV-PfnmGQTHExmpJemzlBzCjrKOHYXvJSGyp6Z3syMfmtW_1SOlySHiKxTEujBmZn5CwZesL6d47ANE-MlgxCRS-71F_oRRtIPZPU0DvdqesMN9-p1eSuxhvgjmODW6BpwDMJKkYsOP7j1gC1gp4KAZD3iYjKo2hJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cfab8ed22.mp4?token=Yn4kvdO6j4tOCI8UxObt7oOzG1KfwJy0k3Aynhu5gtFw3z0gPA7hGZgkKpAmVfhXzrNWoripU5gABtNwtcutBBmmX4Wy8uRaGLwwn2H3XktxGUJmz_GjyBCbZi3pfRLJXyzJBeXpuSenTZhe8wmaUP1unbFNFJ-zR-ocYCFPbxpE9hwVNXDXV-PfnmGQTHExmpJemzlBzCjrKOHYXvJSGyp6Z3syMfmtW_1SOlySHiKxTEujBmZn5CwZesL6d47ANE-MlgxCRS-71F_oRRtIPZPU0DvdqesMN9-p1eSuxhvgjmODW6BpwDMJKkYsOP7j1gC1gp4KAZD3iYjKo2hJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهل هزار تا کصخلللللل
👩‍🍼
👩‍🍼
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/96503" target="_blank">📅 03:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نظریه نامحبوب: پرتغال با این سبک بازی این جام جهانیم قهرمان نمیشه.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/96502" target="_blank">📅 03:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96501">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگه ازبکستان با اختلاف 7 گل ببره اونا جای ایران میرن مرحله بعدی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/96501" target="_blank">📅 03:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه ازبکستان با اختلاف 7 گل ببره اونا جای ایران میرن مرحله بعدی</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/96500" target="_blank">📅 03:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f7de6f56.mp4?token=MEUkNWs5NOKw2cBS0SK_ugkPnb36EBdxl7HzhNZZtxK41JUqJnSC8tNQLd46my0WDbEBGRBsUsYx50ylIAvKXFWPndCoDr0hNyB0TIZORLgZsbjOUCZcMgkiaHN9Q-64QL-MuyrLhQG_0_D7E17VJpcfDa--AhcGPYYUsVDS1tSD4YmE09wvJPJGKt9FSN0OUBy1CXvV-GgteTrWpr5MYZAoa6mcliMe36awiG_hOpuKSzU2En5mWNwOIsXUOt5UvwZw3ynR1PS2lDcrDHfCUKRipv7GXAjlBLbm3kwMPRYlO8ns-BnTFuplOinSIaAdsQYovgYfxA6DZGFLDnSGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f7de6f56.mp4?token=MEUkNWs5NOKw2cBS0SK_ugkPnb36EBdxl7HzhNZZtxK41JUqJnSC8tNQLd46my0WDbEBGRBsUsYx50ylIAvKXFWPndCoDr0hNyB0TIZORLgZsbjOUCZcMgkiaHN9Q-64QL-MuyrLhQG_0_D7E17VJpcfDa--AhcGPYYUsVDS1tSD4YmE09wvJPJGKt9FSN0OUBy1CXvV-GgteTrWpr5MYZAoa6mcliMe36awiG_hOpuKSzU2En5mWNwOIsXUOt5UvwZw3ynR1PS2lDcrDHfCUKRipv7GXAjlBLbm3kwMPRYlO8ns-BnTFuplOinSIaAdsQYovgYfxA6DZGFLDnSGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سخنگوی قرارگاه تیم ملی در جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96499" target="_blank">📅 03:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📌
امشب، با سوت پایان آخرین دیدار مرحله گروهی، پرونده این بخش از جام جهانی بسته می‌شود.
در تمام این روزها تلاش کردیم لحظه‌به‌لحظه کنار شما باشیم و هر آنچه در این رقابت‌ها گذشت را با عشق و تعهد پوشش دهیم. همراهی، حمایت و اعتماد شما بزرگ‌ترین سرمایه ماست و صمیمانه از تک‌تک شما سپاسگزاریم.
اکنون با شور و انگیزه‌ای دوچندان، به استقبال حساس‌ترین و هیجان‌انگیزترین بخش مسابقات؛ یعنی مرحله حذفی، می‌رویم. امیدواریم همچنان افتخار همراهی‌تان را داشته باشیم و اگر از عملکرد ما رضایت دارید، با معرفی مجموعه
فوتبال ۱۸۰
به دوستانتان، در این مسیر کنارمان بمانید.
این هم خانواده بزرگ
فوتبال ۱۸۰
؛ با این امید که در ادامه رقابت‌ها نیز بتوانیم بهترینو کامل‌ترین پوشش را به شما عزیزان تقدیم کنیم.
همراهی شما، انگیزه ادامه راه ماست.
ما یک خانواده بزرگ فوتبالییم و میتونید در هر بخشی که بخواهید خانواده ما را دنبال کنید
⚽️
کانال های استقلالی فوتبال ۱۸۰
@EsteghlalPage
@esteghlalfan
@EsteghlalFans
@Tajieha
❤️
کانال های پرسپولیسی فوتبال ۱۸۰
@RedStarFc
@Perspolis6
@RedStarFc2
@RedStarrFc
❤️
🟣
🔴
🔹
🔴
🌟
کانال های عمومی و خبر فوتبالی فوتبال ۱۸۰
@Futball180Tv
@footballbartatv3ir
@FootballUltraBoys
@ExtraTime_Fut
♨️
کانال های اخبار جنگ و خبری سیاسی ۱۸۰
@News_hut
@KhabarraK
@HutNewsPlus
با فوتبال ۱۸۰ ( مجموعه تیوا ) جام جهانی را با هیجان دنبال کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96497" target="_blank">📅 03:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6362053e4b.mp4?token=VEy-LhOtsTb9IGt1fgkYBMJhBCx56s5lM2c9qMfuVOdhF7rCTh8hNbAaLNSzIIDniqGK3cIYAi8VXEPBMLAU581PJTwO96i00vhoX2zf2y0LSutL1XYxQ2duvF1v5w17t6zc-Zx1jPVucE5EAS7FyivRn_nosgceKiZhn-jrALZv1aYDnwqon-AML8bFz_Eda7zTitc1n_Dm3BgZeCT0cWoND_vjMml1IiwOsA0CIY-fN9uOq45Nv8JSpOOPnWV2Pp3y8ZlEg13wKwIZQBMnUjiNoTtESZoXqoK_0cDLJrag5U97MUQHfUCFK-_GNEMq1OIL7QKbmUWhb5LUuJ1TlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6362053e4b.mp4?token=VEy-LhOtsTb9IGt1fgkYBMJhBCx56s5lM2c9qMfuVOdhF7rCTh8hNbAaLNSzIIDniqGK3cIYAi8VXEPBMLAU581PJTwO96i00vhoX2zf2y0LSutL1XYxQ2duvF1v5w17t6zc-Zx1jPVucE5EAS7FyivRn_nosgceKiZhn-jrALZv1aYDnwqon-AML8bFz_Eda7zTitc1n_Dm3BgZeCT0cWoND_vjMml1IiwOsA0CIY-fN9uOq45Nv8JSpOOPnWV2Pp3y8ZlEg13wKwIZQBMnUjiNoTtESZoXqoK_0cDLJrag5U97MUQHfUCFK-_GNEMq1OIL7QKbmUWhb5LUuJ1TlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل ازبکستان به کنگو توسط شومورودوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96496" target="_blank">📅 03:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پشمامممم رد شد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/96495" target="_blank">📅 03:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رفته وار</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/96494" target="_blank">📅 03:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کنگو گل مساوی زد
نیوکاسل بختتو
😂</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/96493" target="_blank">📅 03:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ازبکستان زد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/96492" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/96491" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsBdIMAeBk8cLAA3lwnzrW2bg_FL_hKKSX_6KtKAy19SltqH68mPwvkLPcC-9cLsUb9xv8AmixgkV1XaHXWPvzgLamuq7MKbQwFZqBU7e-0bf5EIY8qHAgZJRtkWaVDe1YMrSzXwDbqNpMOG-z8-DY-bArWSs6BdFIRaDEGnkK1n5QiMyU4bbzLCxAz-Uk06d6xujikDlQ7zrTXRMmktSTwvIn1tQnXmGpDE_610Kxhmbv2SrV0m0J9p3Gz__9DpR3CgPT5dG78f6YpDcBXxRHbf0FdEMhURrzqu5XhxYQy9z-5dlXBYeq_taJNsXMvozw-9EC_ZRfFZR-TxbFAx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
ترکیب آرژانتین مقابل اردن؛ 05:30
‼️
مسی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/96490" target="_blank">📅 03:11 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
