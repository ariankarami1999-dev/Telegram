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
<img src="https://cdn5.telesco.pe/file/HGpMlu_zNCOIiUKqQ5pU7BKAathb_V3C3T8ZwnUdpy-LEXzWQqt8HocwaHluBq2vsQDHY9oS-0Za289gkeePbJEkmaMwlYkh0ME-2Pvk-NhTarJaM9sbO4KUXb99MVLjzL7M0I7QWruie3qNXXAwks2ltlCMalDmzYLujJlk2HlHZKjpHiIi2PfkX48BEvV6CVPhcFswN6WktqCWmL8D04COjH5BExli_HPxMYJYZ1Qaeu1I1vQFjYPoUnQO9oGIAkxdnn_qNAZW4x--dluXRIYJB9eARVnoJU-1WQlqwDSasNHdr1B4Cs7kpg5UsbZuhfWe6GtGFOAREL9fLmY7wA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 470K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 04:40:56</div>
<hr>

<div class="tg-post" id="msg-103633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFRmVeQGEeu4YxXz_mfSszq4zxbBpUUshEHz07f49TWoCO_MMtbybSdD50a1UrX0Otaitr-6nyOnLMTKZbnNSefHbBaG5hbGibmhPl81sw4D4lxyLoOQQLQtzbR0CBpepqDcJLoV4jUucqrug0TRyrKaBqfBJA1uViWqG4G-DmVqszX-PVSuafV19Ibf_46UEEdXY5Fs7lov6EuSElNMmRMaWdwylQnwEDeawc08yDvw4Fv_Oe1L1qpgubPdLi8a2IwH3fKqkbvp34X8e64fxlCoeissBcXSs6dv-oIYAK91cAdqKOBGyoMbU1IRJV74ueXqe6R_PY5X5ja_8wGgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه کادناسر: خولیان آلوارز در جمع بازیکنان اتلتیکومادرید عذرخواهی کرده و اعلام داشته که ۱۰۰ درصد به قراردادش متعهده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/103633" target="_blank">📅 02:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e844a831.mp4?token=rNcSA9dqbEksoguGQtq1yIzcVa9q70C9jcqPBmfxbhnCwwyrWui9ogjy0RGngNubV61-zVZbAcRiW2aQQkoUbvptDIPN8gRqMeBVU99Cucn9-pLN1GiwRtpBhAvkV0waOeB8fiFLL_cIACWWe8DnBH6-VIku0pDL0hjLox3H8qvru2b75FRi4W-_3H-c6jUmSMCIzH8_GwoAOV66rgxhLoW4867g0NPhO5atLB5JFNsGsA_1G1CIKAyxSHme9z_nO4Dwbt2VX0wZ1lJ1cQkzq2XCWXzeAvoP5w8gsuEWRmopjjxKumkSpoPFYz1fwRRLG2b-OFbnNRaWaW8zzdr8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
جرارد رومرو ملقب به جرارد بنگی:
😳
😳
رودری تو هواپیما جفت جاسوس من نشسته بود
😐
بهش گفته که آره داداش این هفته توی سیتی قراره ویدیو خداحافظی بگیرم بعدشم بریم بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/103632" target="_blank">📅 02:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از جرارد رومرو:
🔻
رودری در هواپیما کنار یکی از دنبال‌کنندگان برنامه نشست و به او گفت که یک ویدیوی خداحافظی در منچستر ضبط خواهد کرد و سپس به بارسلونا پرواز می‌کند.  +بیشرف وسط هواپیما هم نفوذی داره لایو میگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/103631" target="_blank">📅 01:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-rpF1Njix9lqSCLLxpcz6t0xJ4hiEw6mDFGqLaW_N_uAZVJVYQ7Nq2AcW0b8zcONj4IxZ4j7yc8XdZCCzG3OHqE8MWon7XEhZGz3UVrDpGqsTxJfvmJoTLcYNSrf_NXKtpW0x62tE-RBoE9-g5HBybJ88MYyo0hjGODXQNDXeCVqCAkAavSceyG4LjxAm1GdjokYCAxgzS3CK5JFDUodEnoavAxtsTCXZrvIXfevTXqdYeX_Y_OpaL4eKz0kjTvSUo5kQkOqFf1Y54r_aHXXku6GZ18LI4nLmVJDe4aI-9GvoQad5pE6enspZmgqG9tmDbcGLWJl0avTlcbmjmkYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/103630" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2a0VT8TbBQhyLNGm6zvGORTNFPRyWHi-lGtNP-I4zKKykWeLyuVnokHWqr_ImJvpn7odA0Gq8a0mbkpGXBzIuUuXsIruxnFjawFSWZLEm2O3dbV7Qh2Xuc7Y_rfb_pDStnW595s3ihFAxgE9d35ZYk85_dn28UHE1hNC817MLK8dew4ATkKo8i1w0iUwDYtk5YsKdGB-MHR_I7hpWtPXm_trgfOH9PCadUjZdmILFz2qn0LIAk5zMi1CZ0AoP4bI64IGSYsy5qrwWMwHZzse1OwAk_Sqhl38TD2P-ZJWS7Z-b4p0g_IOg9f7W9_GdNyM5g4Gf5vJhYClmL1ke5Efg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🗞
#فوووووری
از اکیپ‌ فرانسه:
🔻
لیورپول در ده روز پایانی نقل‌وانتقالات با جدیت فراوان بدنبال تکمیل قرارداد بردلی‌بارکولا از پاریس خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103629" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNf3rW8eErqt6z24Y14xOhAR5WBKFDpForDnpTZAUndWVXxNaGMJ9MowhkN1QHS-UxXJlBHcV19-ijfkvO2FGYIK9ksHqwhsmGbFg-3IczZm9lNQi3LqWp3dcZ5nmzTCEKtdAs56AP6zFp-WoG0kfqkUkARi4R4UDfuaUoPYmeZAkuYTdsswbd5R4tJJoIrqH5kcTFGPv8abmsNG2NUzoCEG5I8UofXiOUMw6x80qvVyd8_TjRE_ckvtAmDi6MVJOD7MbFQU3pD2zTJeZnk2XgnRleVU5512BCYUxyT6qPL9NafdenRF7LILIuCPSuatfgWGuPKruRIqkTar7Tua8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رودری داره از مادرید برمیگرده منچستر  برای حضور در تمرینات تیمش از فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103628" target="_blank">📅 01:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEsRoVUfkmauCLgBHJ5P2-YePbjsg_NSntWcHSWUaaE2fO8szY-lS8ryLulH5YNUDWUWBagc64drFI3AGLKHRdJAYyElfCGkakLPi-hGvX6wbZZaw0oSF-pCueGpkfYba97EpGUV1Fgh3ni8MJ_Qa9m82217WW9fiqH3YTM_LtzuEn-1GMOJHDR0OwAIZxM6M27pyuM4kuuFyqoFlr74CqX9B2HJf5lmVIXo0EPOGsaXpbQ_jnJ3TvGKHs7yf8SkLbj4yZocWq5nyrRsmpw4c7Q47JINAYhkKo7rrKyVDpR340j0S5Y3kRtCZ1DhqvB78X-zKGwGLaQAPXTpskctdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
🇩🇪
شش سال پیش در چنین شبی...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103627" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4393410638.mp4?token=SlPv-uYLW6tpXYvbIP2qI3mOEUm-gUmWBSBZtzswsIuZtT2Z6iM0SKpVkvv8YqZJN0bwtIlbH6gK3qKowHP6-zH0PLa49Tun00UYwpLI1S80Enh1N_KqQDivJbGTGTmi10rqA8igZTYjFnTjYcXZAbtpaTZhzB8cg4-WY8XINpFB6WhwqrfDRJrB2vdTPZZPP2OveuKj7MOLnDsPJIe4UZjEdsjFh1PbYe2TYy5ny8tc3yvRmiZsbeLikk6AptCRflBCl9UYp7XkQtJqEmZGfjdlwsyuRju0XqQtZB9mlkz5Zc9__iYfdBy7Ne3cHsEJhn7YpVBvofFbh6PPynjffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4393410638.mp4?token=SlPv-uYLW6tpXYvbIP2qI3mOEUm-gUmWBSBZtzswsIuZtT2Z6iM0SKpVkvv8YqZJN0bwtIlbH6gK3qKowHP6-zH0PLa49Tun00UYwpLI1S80Enh1N_KqQDivJbGTGTmi10rqA8igZTYjFnTjYcXZAbtpaTZhzB8cg4-WY8XINpFB6WhwqrfDRJrB2vdTPZZPP2OveuKj7MOLnDsPJIe4UZjEdsjFh1PbYe2TYy5ny8tc3yvRmiZsbeLikk6AptCRflBCl9UYp7XkQtJqEmZGfjdlwsyuRju0XqQtZB9mlkz5Zc9__iYfdBy7Ne3cHsEJhn7YpVBvofFbh6PPynjffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
ویدیو خورشیدگرفتگی دیروز در اسپانیا که حداقل ۱۰ میلیون ویو خورده. واقعا پشم‌ریزونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103626" target="_blank">📅 00:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST-y1tKCh7gKJMvH1BWcANCbvY0Hr1WT41MPtaz6og361zX6NkaP_IWoPSYGyMZMhOzL--HZgf0HMl4-NKMD5AC2K9XFfS4hqQXmgVd7-egh6xqKvy_TVGIVLC3qEKCun9urQ-JnQfBCuknoS_WYguyhAOu9WhHyd3bhYRczU13GbF0IZgUdLfkKJZHl4lPqaWJf333yATfcBMkgQtdhmle_4vT07Jf05EV5AGply5Q6jCuFuT7slclf4fWed7OJ_pU30yPidXV4_MYjPTIWLdll7vtiyBH0Wg5bo1iKQ3rktKCK2TVxfDgBsBzDkwslPmNVpgg44JaBAkzkDgONCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎂
❤️
بهترین اپلیکیشن تاریخ، امروز ۱۳ ساله شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103625" target="_blank">📅 00:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvptbPh7rkUXHByFVA9IuYXFelX-BlOvnSD6bABPvjnswQdmUoCsAgRBF_0ClABCUfM8q73ng_Yw5dBgzGRuqv8j_S5FzdoCC0VpjZ6v-d_EONfKO6QeRESAXYCbAiWqPwaBjk8AmV4jEdvILujVyrkSA2_QMjhqVbvwBsucqpdAfh3mSsBYjK6azjkMD5RYu7_E1S00_q0Cl880wyUyFLZDJUuUyDQE3RCpbWNr-XNwnaPeP8MKe2tUFNc0PPhI17Q1FBorxFwg9fJa1XBa-BYdFMAa0TWh5syegeua1gcVGgmKiL83DQOkjf9PPYqkAjQDJXeGyCZmfJHb75k8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
جدول پریمیرلیگ ایران در آخرین دوره‌ای که با حضور ۱۸ تیم برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103624" target="_blank">📅 00:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104964544.mp4?token=c3q9EGrzORIGi-c_LqoHVfyEJihVq__Mew_5lrYNOyLl39AQiKp2UJ1DeEAxxcsy1DVwfnOlhmnYPzsuyHA-NCEpZ7_gue9mg16lZ62d3z-bTrP4Jn_tLU4eMBDAVeRXEJ5fAR9HSqwC2zqs5NHYSDz-Cpvin-49UnXSBoS09_LT2Me4r3ka5n5QZhwQzGwvizdV3Q10WqBPuvcHQHG2KiEulP7PWqyePDFzBKF3SrPVrKOHyOHWz3Ft12OJEW3a9bNbiiie--5wo6052b_P8rFqv-isoAVgEE5Pu-4Zbt_QhqC4okk2ruYoWkVUJEVQbAHGhXoKt78cVZSl_L1nTozE3Y9Ph5S0bLlWWU5qByAYLLwEPXwsT8JdB_6llUUjiiJ150rCuUFNIqfUHhWFdBBR61wsrs4prN-ndmoVhIM556qjk7nphRf1y7O2qsLj9dujUuo0d4aRrHYRUbQGAG3R9NBBWE0SsXfDAkgQbLOK1W0rSOb4CtjOxno7fJz5lOJwIlfwUtarUj8Jqh_98lJRKDTK1FnP4GQkFWM_cUr8jb7VJsJWlgqHeGeaaVpmhW6vTK9T9lhFJ59Zo-QMOQboynnm9U8agnpxSYFTiNB-G1-SGMRfabplfXeL6JhLctjGYNkl2sd1UjmZWiEtsnvh_0FRUOKt3owqoqoG7ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104964544.mp4?token=c3q9EGrzORIGi-c_LqoHVfyEJihVq__Mew_5lrYNOyLl39AQiKp2UJ1DeEAxxcsy1DVwfnOlhmnYPzsuyHA-NCEpZ7_gue9mg16lZ62d3z-bTrP4Jn_tLU4eMBDAVeRXEJ5fAR9HSqwC2zqs5NHYSDz-Cpvin-49UnXSBoS09_LT2Me4r3ka5n5QZhwQzGwvizdV3Q10WqBPuvcHQHG2KiEulP7PWqyePDFzBKF3SrPVrKOHyOHWz3Ft12OJEW3a9bNbiiie--5wo6052b_P8rFqv-isoAVgEE5Pu-4Zbt_QhqC4okk2ruYoWkVUJEVQbAHGhXoKt78cVZSl_L1nTozE3Y9Ph5S0bLlWWU5qByAYLLwEPXwsT8JdB_6llUUjiiJ150rCuUFNIqfUHhWFdBBR61wsrs4prN-ndmoVhIM556qjk7nphRf1y7O2qsLj9dujUuo0d4aRrHYRUbQGAG3R9NBBWE0SsXfDAkgQbLOK1W0rSOb4CtjOxno7fJz5lOJwIlfwUtarUj8Jqh_98lJRKDTK1FnP4GQkFWM_cUr8jb7VJsJWlgqHeGeaaVpmhW6vTK9T9lhFJ59Zo-QMOQboynnm9U8agnpxSYFTiNB-G1-SGMRfabplfXeL6JhLctjGYNkl2sd1UjmZWiEtsnvh_0FRUOKt3owqoqoG7ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
‼️
⚠️
انتقادات تند رضا رشیدپور از شایعات افزایش قیمت بنزین در روزهای‌ آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103623" target="_blank">📅 00:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=gXikedu_OvzN6tBqHY8n6j2J08R7vPC5TttktOrNtggu6fQOJRaZ3tW398l3xRj5_NqhJemfimfconXrwxa8mnHfUu1PaVrebiiRpo0-fKSwoTREYoYw7uwx-pBetiQvsOViupDtgkMvN36b7clkZxtgqOtGq9zn13O85lKvzV8xgf_BhnguRqpsRt85MolW13dKfEy3s7QyspZRwoJPoDvH9lzj6ZYvUHfe6oo-hOUqjA0A07oUUaVwC4LIuEkADEBNQoyy7zw4NSC7YuejD_Hh_Qafixsy7NfGWn8X2594YTSZQPtj-FdmDa7NctM7Hrt9IxDy9LzuHkS42jZ8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0689eacb78.mp4?token=gXikedu_OvzN6tBqHY8n6j2J08R7vPC5TttktOrNtggu6fQOJRaZ3tW398l3xRj5_NqhJemfimfconXrwxa8mnHfUu1PaVrebiiRpo0-fKSwoTREYoYw7uwx-pBetiQvsOViupDtgkMvN36b7clkZxtgqOtGq9zn13O85lKvzV8xgf_BhnguRqpsRt85MolW13dKfEy3s7QyspZRwoJPoDvH9lzj6ZYvUHfe6oo-hOUqjA0A07oUUaVwC4LIuEkADEBNQoyy7zw4NSC7YuejD_Hh_Qafixsy7NfGWn8X2594YTSZQPtj-FdmDa7NctM7Hrt9IxDy9LzuHkS42jZ8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💍
🌟
تشویق اسطوره رونالدو در تمرین امشب النصر بمناسبت عقد و ازدواجش با خاله جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103622" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103621">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103621" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=SS0cYK8UHYOAmhEyCB-PvsaXZnR3n7QFz0NeCB6tKJ3KZIibZL5muC_SkdHdv2IX5p2Au4VLJjbRQ_b6cwrIPktopno-ITcdlisvn_wQRMCFGDa1pNugouUEoJIQYZ54cYEMn3f8qFsC3XQFRjUOjePcLrXMgeiUzhT-4JQQG-p7bRHi6oJGEn5NPuCWXy3yT083EqW9Al3ePLIixfcXIkvYCngjW71Ipi-XY6Arv8-CDXlN_XfE5ThYanGOoXREO_WKv6a9P0eeliuyz3hn125kSKzNjYcd56JEz0qy1hBrYNeqdd6tpuIDJLcjabdQ8gr4k6OHjBUJVaoHnAWyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=SS0cYK8UHYOAmhEyCB-PvsaXZnR3n7QFz0NeCB6tKJ3KZIibZL5muC_SkdHdv2IX5p2Au4VLJjbRQ_b6cwrIPktopno-ITcdlisvn_wQRMCFGDa1pNugouUEoJIQYZ54cYEMn3f8qFsC3XQFRjUOjePcLrXMgeiUzhT-4JQQG-p7bRHi6oJGEn5NPuCWXy3yT083EqW9Al3ePLIixfcXIkvYCngjW71Ipi-XY6Arv8-CDXlN_XfE5ThYanGOoXREO_WKv6a9P0eeliuyz3hn125kSKzNjYcd56JEz0qy1hBrYNeqdd6tpuIDJLcjabdQ8gr4k6OHjBUJVaoHnAWyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a22
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/103620" target="_blank">📅 00:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeyEOkQtmt9x7f1CnYGw7KGvSJnsve5uArDx5FlaSTkwUV_CzWitQnr8R6Ru5JRVzVyPrX0UmqHt6TW-JQxn7_Rr1AlaZj4J_Qg_m8b1yNvEb8fA0kCheW_qWqKSIEQOlOv6cgt2Xj5Zv71NPWXcscgx1T_S8WRupFFu0kZMHSUzv-TekNGGoJpMUWMen9NEXuM00sHIfEvkJ60GDtwkPXMquKfM4kOFxfS2o9I9xQIMMKuKSkHphk3pHdHOnYfIYZMlVSn_0CacCOYNIsIMnL3XJX_zvHM8xaTUR6e5Wt-ifCuBXtbdZx0a6dMuZrcS_-uX8DHevsXzwp8RjA3vyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
📊
فران تورِس در طول 5 سال حضور در بارسلونا در تمام مسابقات:
🏟️
201 مسابقه
؛
⚽️
64 گل
؛
👟
22 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103619" target="_blank">📅 23:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5dbVKEkf1njM_Rm1ihbJgI0wGSZhhT-NW3jAjW2EviAFRcv6yxystPlSIgtS5g5YDavexrCx9GYei_T8EV6N9FCQ_WbU34ldibrqfUqrGtldKUNzwkAXctCTnPqv4MqTHULi_YSSd_rp0K5LxrQ5pJr9apVM4x7aEy1-kLvxQIUnUNobUiJmQIymuOo3yEXI3sjti9TcPigNYc6YR21OwuSa5Y2-c5T5zqtTXKI5jUDWMeoQQsxlkc9SMqds8RVcjGalZZmp_gfpnroj7ZKEVQCfE47kvg1AuSKTeghMYO6I6kr9ckC_udE8yGPdYW-pY4yqIEuuVLZvE27MF-y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری و #رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103618" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
و
#رسمیییییی
✅
🇮🇷
رونمایی از کیت‌ فصل‌آینده پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103617" target="_blank">📅 23:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0NhnNmavj6wK0xyqkasuQTLwhmZVt8GFoZ5ULD5qZS9KWBbZUcR94h9Y-5FBKALCUBzihgiKttKjzVzeMPd98Gflcy6kiESHgImgOeYJiPq4kdVwEoeVGbo0vRFUiSTmyc-xqPX8kS4vvGbOLvE_ASJbxH2t74-R1QvSkuYd__GWnHLXEQjgT4eIwXE3uMlGGVsjb_ZALME3q3Iaye4TsFz0AGNtrS-eMtGvzmMr7aQJto54PtZOjpj76TlY_mLX08ePo_-MhTdC0A5DpLoro62CK96CZ_cutCWGlgMshjZVvZrvPhqClQSAdrwfCo4f-dbLEF7zrw_iYQPdgILLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ پیام رودری به منچسترسیتی:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
«دوست دارم برم، اما قبول دارم که اگه قیمت مناسب روی میز گذاشته نشه، در ۱۲ ماه آینده همهٔ توانم رو برای این باشگاه بذارم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103616" target="_blank">📅 23:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
😐
دولت جمهوری اسلامی درباره قیمت بنزین: سه تا راهکار وجود داره که یکیش اجرایی میشه
🔻
راهکار اول: قیمت افزایش نمیدیم ولی سهمیه مشخصی در روز میذاریم برای هر پمپ بنزین و اگر از حد مشخص عبور کرد، پمپ بنزین در ادامه همون روز تعطیل میشه
🔻
راهکار دوم: روزانه ۱۲۰ میلیون لیتر بنزین توزیع میکنیم با همون قیمت قبلی و مازاد مصرف رو به قیمت ۸۷۲۰۰ تومان می‌فروشیم دقیقا مشابه کاری که در کرمان قرار بود صورت بگیره!
🔻
راهکار سوم: چون ۴۷ درصد مردم ماشین ندارن، میتونیم سهمیه بنزین رو بجای خودروداران به همه مردم بدیم که بنظرمون عدالت رعایت میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103615" target="_blank">📅 23:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK-buHU_q6_X9R9JGb_OJ2tFbDjvPuBfRLT7cbt3f-KIVqyhhpiddwIVeL_-_2m4I2voiums4S5Yc6i0_OEdmsBA_4Tu43r056hICkAbJGsYDVfOV9ko9JgAsecdT-SGlaNve8nkBS_Kyu9RMZD1dGV4S16DFuTFj3C_f1bE-OZUFP8FngrjcEyfuH4aZfcShc74z2d6hnCwbU1x8x1GXXwIsuGF0_IRSWNELJrSCgZ9r-4CpvarRvnhoiRCFuzoLPOfD7P_M3cBB0Lf-aFH7zAxfM2fug128GPkMblNvO-BrEkGc9bMWhRmwCEXBG2Ijjwxnb_FeqRiavXSxwXsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
👀
9 سال پیش تو چنین روزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103614" target="_blank">📅 23:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👀
لحظات فوتبالی که هرگز فراموش نمیشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103613" target="_blank">📅 22:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veCe8oCPnfBEyVUQFhZh8bzz6P3iLGiNchBShtmSFdD6M1KbJg8mPQEmxal1ZvpKkhqHaOPudG2LODb-0RPN3caHbNnKhRhFnrJrwInaSq6EQBk4IhqbTBlGFaQ0Q5ldTWGrUOstDZIzQAwJZLrtGY-Y_L9tMu39R0QHapK9iJTAvGaqp0VabG0436l2diN0gbb0DpjcOfhq94E5RrsZK83999h-8CQl6or67l8Gmb_Sh2UoXzrwWIawyZyQZsm8VJQTsAu2x9jN4MWtgadZxMrFp9pPX0HJs26L1_CX9Lsx6x8MJfRNE16FeOMJOiw7X-NuBZXZQsj6wqdfxEcrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
باشگاه‌هایی که از سال ۲۰۲۰ بیشترین درآمد رو از فروش بازیکن داشتن:
1️⃣
🇬🇧
چلسی: ۱.۰۸۴ میلیارد پوند
2️⃣
🇵🇹
بنفیکا: ۷۵۷ میلیون پوند
3️⃣
🇩🇪
لایپزیگ: ۷۰۶ میلیون پوند
4️⃣
🔵
آتالانتا: ۶۵۵ میلیون پوند
5️⃣
🇬🇧
استون ویلا: ۶۴۸ میلیون پوند
6️⃣
🔴
رن: ۶۲۵ میلیون پوند
7️⃣
🟠
ولوز: ۶۲۴ میلیون پوند
8️⃣
🇬🇧
منچسترسیتی: ۶۲۳ میلیون پوند
9️⃣
🇬🇧
برایتون: ۶۰۶ میلیون پوند
🔟
🇫🇷
پاری‌سن‌ژرمن: ۵۲۲ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103612" target="_blank">📅 22:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103611">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_FgnRkBubrFXL83ZEUKLtW7PeCdb1swcQLu50zovqy1Hq6jQVXYao8sQ2zqbJdni3nbYWpKDd2NdSepesN2__Y8O32H-aKFaH_u_ohy-m3bV3LJDKDdid6HEnnsWEZrm1TCC279xO4gU8PV5T-M_hiwOAhfzCzyuakhScxNO-ra-DxYHkF3Gyx6edtAymPetjdLAVbSuJya4opmzE3zLbgifyCXZhv5gO2Pemv4ZvCHV8MZVK_D6TTRl1UULcgVfMHMEIu1Oq_LpfFvuBH7SdWTfxy_L-QTqNcceCvzZ42VoXJh4NEcKwHTN_BdlIQRt7jKzelbqx2W33eMivWA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویکتور اوسیمن با وجود پیشنهاداتی که دریافت کرد، به طور قطعی در گالاتاسرای ادامه خواهد داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103611" target="_blank">📅 22:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103610">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlgP3vlp8VO_XcyX4RbpKms4oxjV0BhaKpVoJO1ONLz7V3M1NgPTbL-unKCPsKinKgJH-frxqWa8JI7hFqfV29lWEKb7RMxO-_tSnmftTyiaD__r-R4Jg3jpQRtjGBNrogKfl2Ub1aAz8x7Rr5dImWRHcHCjC-6MWUzvHbcvXicsNu4kNsr-9zUbyesWb67eSxtA2_ObaIo-3bBnvcCD28jA5kDRxqHLiIdOiCxTK18Bqgg6lgzkr-1tvd-a-KZRkT-gBUIZGtKk3AJIqk9DSoWhhZWAHNpEHT7kjcBAjGTup9zXUiZiyE0GdBJ4UX97jtwLqbjWA0-SghFUcUiepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
اسامی بزرگی که سرمربی‌ تیم‌های ملی شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103610" target="_blank">📅 22:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103609">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEs7HPfd4ZHeK3AdleViGdLSDuI0OAHLzPX1pAQN4CNMspy14yHBB-ymTcrez3ZIlCxFHjy2jg5iidrjMa39aJyfZCDEOpjbFq-EvAr_vbi5jlmddiRL3rC57lHHFwd2FN7ano71Q1cSROU_StqDsaPR2KmMoq6ZjfYwyxTcQR4smaOzd8JGAYiRfiy_pOyYMIlNbfbyUkV4QyEBdXA6SOBfQtTkfY4dk1DUcMWzTNqINmnFnu28Qey8wsH1fAB0bDmbhMFcLV_m9LjYnr8SFef6rGfVz7TRUmcdC9acp7gM_UVvTqgrl3ANESWJdWZ5WaiKs3zMd0qUiyhHbmudfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو:
از دیدن مسی تو رختکن سوپرایز شدیم، اون تعهد بالایی داره و برای همینه که اون اینقدر بازیکن بزرگیه، اون جزو بهترین هاس اگه نگیم بهترینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103609" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو: فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103608" target="_blank">📅 21:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSH3sTW1Beae3P3kEkgxN4817pxFMBhjHtldFtjdv0bL32E2Huy3F_cJ2erRizvBHRHUdoGQfkwKKCpgSvhteDSraCKW1NeM2OcyDpt6yFPYIfB83fuDuwc0yHsKNm4lZh3bIh4NCt_mUDWy95LFZOzUP-_W4XVE2qTt-bE-RKNK8iNxEUYIDe--d5OE5UPRq9XDAfAZIt71Q-0du8K_mJNazRYKGMSGH4GTMwSNYsAJY-nH9pXp80W2SFmjxBnvWpVxkINuFoSJfT1-GuCvLt9hM0XKyk4wQH1s4HfvcxqUHsRZ2K6yH6R4KBZMMMvAWMtfsVNV1nUyy5ZJiCvnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری فابریزیو رومانو:
فران تورس به پاری سن ژرمن هیر وی گووووو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103607" target="_blank">📅 21:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBchBK8Dopk-Wu2oU__SN7IROp8LFlzoxF8I1fwhKuvxBSqaNahKsk-qfXRyN4Jryuac4QbD7_sRo8LNySjx3wZpnGrkfSCeGnAdhYpDiumtinXdl2wjsMlcs9frhxkrsP5_UQKx9hZzRnOpcvSS89Zzp_7WY3owBe7xHTWkUhvLrG5haxbjsxL8t2Ag_b7em9IcVhzKIY4OXdwqoOzUgdJAxwW1YB5JImLXAA6vrzUCTPLsKw2f2CqSuUdJoC40c-EgDMGblKxHE3tKfQuLukCcBj9bAPcx3vPV1ws7G1HsBGwJQUmcbSfbC-JDCP1KZiVe4Q7FhcEObocjKOjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مالکان تایلندی باشگاه لسترسیتی امیدوارند این باشگاه را با قیمتی بیش از 230 میلیون یورو بفروشند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103606" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGKID7Fm-YOF5mKNkpEDG3ds479TFFYTdTl_YWg2PzBrYWFIGMKDQhw_9vV1179mMuY0o14wfvrUwKawgTZDnOw0qcH8IzqBMTjS1Tv9PUklr4a7598Fe2YaMACRuXh86cfDuBuEb8myDOR2piT-WRvmuAUIqxbEiMdzSFZfKTWd8DIgFDZHk4cRtPv1lhLSPFR7PiLCqC7T1Z0A9JmeVzzjBukO_Z02zVUTShV4ltbVC6YdyBoUMXnTqY_YnmkwO6VJR05ZBhDJ4gaMWiLbhWnLkcvw5jqLKnDazqM_HahoCyjFFtiLrx9Dk3nJ0rX3sfiehLvGBkX2GJGfgznjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد های هالند تو کتاب گینس
سریع‌ترین بازیکن تاریخ پرمیرلیگ با 100 گل در 111 بازی
رکورددار بیشترین گل در یک فصل لیگ برتر با 36 گل
بهترین گلزن تاریخ لیگ ملت‌ها با 19 گل و زننده 5 گل در یک بازی لیگ قهرمانان که رکورد این رقابت‌ها رو تکرار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103605" target="_blank">📅 21:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awiGuGH5D6jgRPGOm-CULRu3JyfgreTDJo6mRtefA9micyLVUncVVoP9bljbLDfEy8VHaO35vfVAZwM_eVDZzfwhzGeDil6uZS_ywi7nNf_3f3H6KOI8S_xq97RY1TwyWqgVIvLLhiPmaStKVt6cVG-qzmQt89AIVz5-7E2okYIIpyeg1S1V8p4jhxGdV4_U_sYdZoP55JV09Aedu9-7oShvNpyv5KMht_S-Bx5eEzcKFGFRFgVJn_9EcP6iakCBCcLFVa1XI666z8EjFMoaP76NJXUXG_fyQ_iQ9xOj3KgVlUR3nTCvoyXMOoHLUHFZzzAd7W9wzwYxapw-5kX1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5FE01qxwpmjzJfS9KjcInlr7NgCay7p-nwivi5wwauEEQCL81GpHARfGb5Fq4ZO76mm_uxym-ihnPUz7wMASvkh2LZeIAl_IP_1dU67DeGoFKN7XKYcxTf75_ghbO8LtGFZy0VJBJJZJ6IVTfd4BoR114BGZzuFZ676GFESmjptmk8x226jQDbplf3OwDv7NEQasXqOk4YY9_TnMLKad0xCvsWWyDYEyl45cqk7DHFQCVy4f2YtmA89_9BvWfdNTK124DKbETv837mbbsV4oxo0rZhXKzqaJY9yZVt0DtjXdMS8QEQze4eNFQPKWeEEjlrwp8OslPpYkmtPWmzA6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇨
مقامات اکوادور ۴۶۹ کیلوگرم کوکائین کشف و ضبط کردن که عکس ارلینگ هالند روی بسته‌ها چاپ شده بود!
گفته میشه ارزش این محموله در بازار اروپا بیش از ۱۷ میلیون یورو بوده! مقامات میگن قاچاقچی‌ها گاهی از عکس افراد معروف برای شناسایی محموله‌ها یا شبکه‌های مختلف استفاده می‌کنن. هالند هیچ ارتباطی با این ماجرا نداره و فقط از عکسش روی بسته‌بندی استفاده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103603" target="_blank">📅 21:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
تاجرنیا و ماجرای ایجنت اندونگ
تاجرنیا در دوره مدیریت خود تا جایی که می‌توانست از ظرفیت محسن ابراهیمی، ایجنت اندونگ، برای حل پرونده‌های استقلال استفاده کرد؛ از کاهش مطالبات جنپو و نازون تا بستن پرونده زلیکیچ، آدان و منتظر محمد.
حالا اما به ابراهیمی اعلام شده که سهراب بختیاری‌زاده اعتقادی به اندونگ ندارد و استقلال او را نمی‌خواهد.
جالب اینکه تاجرنیا پیش‌تر مدعی بود با ایجنت‌ها کاری ندارد. گفته می‌شود اقدامات انجام‌شده در این مسیر حداقل ۵ میلیون دلار برای استقلال صرفه‌جویی داشته است.
کسی که استقلال را از بخشی از بحران بدهی و محرومیت‌ها خارج کرد، حالا کنار گذاشته شده؛ شاید زمان تلافی فرا رسیده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103602" target="_blank">📅 21:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys8NmE0DhzeUDgKL-xRgop4064PIsSIboe5-DvringKkxA2i2-G_uHeMJWlaC1LmeRVaj2jc_OJl5divw2Ja2CK6gSzjfplIw4lkJl6p5tZ2_4ZwMrWnlZPG3BWi0-j9Fy48AoIrx9Adox0ZX4VA-zjxKNiaHBkibaY-opQ3ua-DiYGTUUcTtl4NHEZ5vfmJQhMUqa7LteQRkc2MLySYbtQEdYIfEKc0tketNe3SD-YeVCiBa_ozbzBdMMbll0ETybk0vESdZMTaI5Pl863ki8BHD0UKmGzOg-7PZ_AUZrVXohfg-2Xj8AGtz8gPPhFd-XWuKFRyycD_ThRloSt5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از برخی منابع انگلیسی؛ دو تیم آرسنال و گالاتاسرای درحال مذاکره بر سر انتقال اوسیمن به لندن هستند. آرسنال حاضره بیشتر از ۱۲۰ میلیون یورو هزینه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103601" target="_blank">📅 20:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ariA6oSJGmg8gwwA1eWu8jP6PfYRAU4qPFD_Xn43BZUlNKVCIB3-jsCcRfp8RoQlRrfeB-mSHWrLhJ8Go7J9GESORxBKynenuW5MeaNJwbk5cFFxwxGYkmUhPm1tgMEW72kd3sLIRjtgUHw71v9jGnSrvDsKLIrJKSf3Rb_0MYUA_veWT9oZxBzNHbzyJz1XmRnjd52If1dnq6tMg4GMzvl9-kke4PUXCWWVJ6m9GiGY98YNMnm96wmKAhPYi3lFd6n5tNtg2cld4xIrXxaMXNerzfY6V44lshDb3753eEuN-PjQA4GefvWBYQOWBVhXl_4inRUYyt7kJQ9vIY2BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
🐐
رونالدو بعد مراسم عقدش با فیس و موهای جدید وارد کمپ تمرینی النصر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103600" target="_blank">📅 20:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacd65c8d8.mp4?token=bOJ2zrDc8nCZBRux55lnKglk4VzePUiwom1SpuNz3syRvqU9rs3D97Gw8ClC05lrQjEtY0a1SAD7UYuZrw9mAGYXtEkMgLwu8yqXCczaiKUkg6HWWwPzhjTGBGBb6KjIFKyZd1YFIQCphPSYcHYBASQcSSD75jhkfiQtk7IH_lHXvLO493wSKtBCn1M0I6jvGTJ6elsexyt1Exwt8SDIXEwz2oKVn_Sfl32miqFgP45z2eJ-RS0uH5fQ-L978UBqgutCwlr8sY4mtxB2f0XUVe55CGlzNznYpIO6Swz44RPyi4UflXqV0u5wGUSot8373pEqARzYY6SXEtqzpPdbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacd65c8d8.mp4?token=bOJ2zrDc8nCZBRux55lnKglk4VzePUiwom1SpuNz3syRvqU9rs3D97Gw8ClC05lrQjEtY0a1SAD7UYuZrw9mAGYXtEkMgLwu8yqXCczaiKUkg6HWWwPzhjTGBGBb6KjIFKyZd1YFIQCphPSYcHYBASQcSSD75jhkfiQtk7IH_lHXvLO493wSKtBCn1M0I6jvGTJ6elsexyt1Exwt8SDIXEwz2oKVn_Sfl32miqFgP45z2eJ-RS0uH5fQ-L978UBqgutCwlr8sY4mtxB2f0XUVe55CGlzNznYpIO6Swz44RPyi4UflXqV0u5wGUSot8373pEqARzYY6SXEtqzpPdbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
قدرت کریس‌رونالدو در فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103599" target="_blank">📅 20:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d2c02eec.mp4?token=PCqf8d84luvI_yWJBDX9zzHrLp6K-a2c6aNngyRrp9xGRIstqkk5aqAynAaAt5P5pIXfbmrlbJug49HwrmoJQSUUYEFJdPemUdPScQ3r2rvY41MSJ1DOIJqsSYoCcXhcFGCM6tDyOoI6F_LV1rHI4HN1x4sw9s4XnyNr4O8RfTCgPYaNNiM6smJ_HE9oVKefmhX88dleIhV2vO0YXRJjU37MZSThEwG2c_hppvklNNeqqUH1WMJVc7FSKkY9Q_5Gkc3Av763-tzhirj1a3QQzwui_2iyKXrn6M0X5QX8Xog9zoz3aYsliHH44fvK5vfyrUeIEUdzYBKUxxl1u_IfBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d2c02eec.mp4?token=PCqf8d84luvI_yWJBDX9zzHrLp6K-a2c6aNngyRrp9xGRIstqkk5aqAynAaAt5P5pIXfbmrlbJug49HwrmoJQSUUYEFJdPemUdPScQ3r2rvY41MSJ1DOIJqsSYoCcXhcFGCM6tDyOoI6F_LV1rHI4HN1x4sw9s4XnyNr4O8RfTCgPYaNNiM6smJ_HE9oVKefmhX88dleIhV2vO0YXRJjU37MZSThEwG2c_hppvklNNeqqUH1WMJVc7FSKkY9Q_5Gkc3Av763-tzhirj1a3QQzwui_2iyKXrn6M0X5QX8Xog9zoz3aYsliHH44fvK5vfyrUeIEUdzYBKUxxl1u_IfBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جا مونده از بازی پاریس- استون ویلا.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103598" target="_blank">📅 20:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxogK9sgjOMcLDMARHGcGyzpjzoBxOo-_13S0p0HzjCuUcPdzzU9kAHt5Vyy0teoLIAWs_uMYsDYecQGalMBzDmUpqua4wqPxfIxxjecbzrm6nV9S1vuyNtrSZTVAeqVtV26nBjR-5wPSTsgXJ93BcGRAjjfAck5-tl7IB25bj8_gEOIzI3xOWCKMBYEMDi8x47mavmhs8yv9L2v1JORJ399j2lF2La7QNux1uNoFy8FQQtxaFs4vipPCd9Kw19e4cUMqc9u7QZ4BciV5OZHrT0WuNx3i1F21nsd-KapNkA6dKhL4DRboO5q_qFkBT0YRnJhlW5WC24GqKpHSH3NBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز جمعه ۲۳ مرداد
🔥
آغاز فصل جدید لیگ برتر خلیج فارس
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103597" target="_blank">📅 20:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3xrv8YhSmCflq36qoaykMgqtVzE0_EJ3AlFPwRJWwp_LRN8KQVny4azWJayQo34pC8H8sGnxphoj27s1AcX95VoFdy7j4WX37nxiTeejQ2J4OB5e8djwZ2dE76oxUpNdDrDNDdYycLNkQpPGrDvGEsrL_fkv-N6C1wDd2W-I7rQIPzoOKvma6Oti5-UyBk9vKugXY005HvHyyuo-5wkPe2Xlw0yVMoT3E4KOHNZwxLaymbFRF4WGRgZrFjKAhYe0NxalwMnAfzuHxuJ8DgQ_rOrPIZJnm9AVsA731TqEgCmRhto3h38N-Xj1_EsZXF5rOwJH-K9HcXp-DsbGFUoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لیگ قهرمانان اروپا (می)
🏆
جام جهانی (جولای)
🏆
سوپرجام اروپا (آگوست)
یه تابستون فراموش‌نشدنی برای فابیان روییز.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103596" target="_blank">📅 20:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyZ-9Cb-Nb547yRaLHQsfux_H9guNt0gxERNVqmKMoGVGr9pur7AqvoPGnfMN8lie9qxg7hfys1copvSG75Y3-vHLHiS4hrcXUqYTZEFspedAVaYdl_PEQw58oFbiPnqazRnKCN1dvrqn5ioRXfuSWjEGe_gV7tttKbvQ6wNZoWPq9vc1wY8kIYeb27UqCyv97UqK9cqJmi5C9wHPzkQcQu0-wQXe1yNbNaE3ZIXyv-bUWI9TL9IP24lk3aw6AS1FNVKt2Q8yAMqtDo1BqcfUxOBrdvaNJm3IxWlxViwFNWxNNsKiBGLX0wmzfzXl1_Qp0UhnH9C2cTLoBEMYBl9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توماس مولر درباره کریستیانو رونالدو:
من آدم منظمی هستم، اما چیزی که کریستیانو داره یه چیز دیگه‌ست. همیشه خودم رو فردی منظم و باانضباط می‌دونستم، ولی وقتی به رونالدو فکر میکنم، می‌بینم چند سطح بالاتره. من تمرین میکنم، مراقب خودم هستم و کارهایی که لازمه رو انجام میدم، اما انضباط کریستیانو تقریبا غیرانسانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103595" target="_blank">📅 20:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_XvbbQ9DJyetPNHuBjw4KhNOXTvcHN8_5f76goEHL0wco5gXFryICBaratv4DLVz8ey9hCZ8lZg_In2PBFhng4ATY6U_2-_8ypY1h6XtFtq-jBcnQrnGORE2RPscGK6junqUC8HwPatyrA_RPf8MknS7JROwysXrzWBv49gof4visUsyglM2TfE3Wuu31-spLDpA71yV6Ube5gUvl3sz29NG187zxeU4wyRcmVsCNM-UIdVSjsdOE2v7u46UyejaL0MRwA0OfkCDyjzZBXggk0mNNySuMyOS0w4mT9JdQR799sK1IrsuVrIpLjzBCDTHXcWTCTs_2cLsmxHS_oE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو؛ تیجانی‌ریندرز از سیتی به القادسیه عربستان مبلغ 61 میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103594" target="_blank">📅 20:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
رونمایی‌ از کیت‌اول باشگاه‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103593" target="_blank">📅 20:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn8nuzKhartRyy2JZ9QDIf6VYgrUNrf4TCbPSVl3W9p4OXSN1g5DEhi9zxgb36csnnqZJXVZITQpJELnpUS2JUFKOnqeXx1KjnFsdZwVVWlcFXblPvq6-CgPdXfZWzEE0ANkaPZtsvPKs0G5GWUXVgp4ZzABRrWxsbRQhZSyx1lC2ShWQ5hzYoM-zKxJ6nox84qfDiW2-P1HLjeFYC9UdqF_Eo_cGaxeOuBYuWLQt4ycLMkjDS3D8d-xGlTrptfFMZIyjasO1Zv8og_5Yrec5VLlHy4Hcr_hdZhEdWV2TKh_3Im9ceR2yp0R5_uage5X0qFb7g9ShFlNacqBUolhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
164 بازی.
🔺
168 گل.
🔺
49 پاس گل.
🔺
19 هتریک.
کریس رونالدو زیر نظر مورینیو.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103592" target="_blank">📅 20:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuJtVMbxwPxMFemfslvCBkJUqs-z53P__gdoiUUkl-ZS7UpaRosnLlYPY1qM-F4denoinVb83lBtRYNwcisBUKhBYFvMIRMt4QU6hK0yaipiTiKZu0gpOX01C08GZ7-n_YxaWG8GScvGXc7WbmCuQjmr_kG56wVu2ZLvzbfmmiXqn1GnB6KIDz3gRsYfeqHk4D80Kokq41Kmk40irTzfuKTR9dXOyCKZIaktT_VIEF9x8tsNstai9pdl3cBEabCY8B4TgDDbaay1NAVKs8FvoffCOaRrrOEcuFuIPvbadRSiHn0tNgbdsPf0VjZolsbHuikVnT8dh6NcvVlWJfdWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👀
اتلتیکو مادرید تنها تیمیه که از سال ۲۰۱۰ به بعد، به‌عنوان قهرمان لیگ اروپا تونسته سوپرجام اروپا رو ببره. جالب‌تر اینکه این کار رو ۳ بار انجام داده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103591" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897693b97b.mp4?token=n8GDDxrf9FOiLzFljwNQ6wWHfUkXjbHBY3xsgr3JRKclHvDiRWaXWZMQZ6dKHa_GzUbshYWxaMugFbEGgaB8e_Y-422Q5VCmlQG9q27CLFnSrS9H2h6o9_Z9yl_PMEtA5aYc5ef2DlknNUaFmf22GAcy97ipIltYATB7b7Qlj7qXi2b1VrzZS0QK_o-lvF_6cDve2wmwBPm8ioGUmgyhA3DAkigra3MJmmjeUfN3EW1BdkwBVofgu4ZMcnAatGFsLOu4_NLZ73FpFbIB8QzHurmfvhYBDiatcoaUvbPqf-x9X8RMQ9u5IJPxLVZvK4dbwqgO3rb1dLobLiLVf_4VNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897693b97b.mp4?token=n8GDDxrf9FOiLzFljwNQ6wWHfUkXjbHBY3xsgr3JRKclHvDiRWaXWZMQZ6dKHa_GzUbshYWxaMugFbEGgaB8e_Y-422Q5VCmlQG9q27CLFnSrS9H2h6o9_Z9yl_PMEtA5aYc5ef2DlknNUaFmf22GAcy97ipIltYATB7b7Qlj7qXi2b1VrzZS0QK_o-lvF_6cDve2wmwBPm8ioGUmgyhA3DAkigra3MJmmjeUfN3EW1BdkwBVofgu4ZMcnAatGFsLOu4_NLZ73FpFbIB8QzHurmfvhYBDiatcoaUvbPqf-x9X8RMQ9u5IJPxLVZvK4dbwqgO3rb1dLobLiLVf_4VNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آنخل دی‌ماریا ورژن رئال‌مادرید؛ یکی از بهترین وینگر ها و چپ‌پا‌های تاریخ فوتبال جهان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103590" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1dd51b6b.mp4?token=c9JpoBTlG3zhuZYtR-IAGjFSvd84cN0bPbzAHm69d33uyunKYo8Tu2mYq47WrlAZTOIPMI_XNvd5HcDzsexGxmUJL9cbVfwmbNgNihGvnQDeqklSdB55t-X9qGCg-VuMgi_83eNpW2md-YVU3M1KGQdd5Fm08GYJieA5L0gVUlV7vfbz_h3cJnEaWOrvo5hKyioEZJk2pTSFroRMC0NWneFoZuHU58FQikcduD-b3G6RQfQZbEWuI_JKik1sOdFI5u9UwvO9n4tDFfxUgX7YEmRKORtAPqOvgo80KyoIuqwjaEhYA4vUUHdQnoMs2AuPanUSm4Zs98z0GO8O1Jh3Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1dd51b6b.mp4?token=c9JpoBTlG3zhuZYtR-IAGjFSvd84cN0bPbzAHm69d33uyunKYo8Tu2mYq47WrlAZTOIPMI_XNvd5HcDzsexGxmUJL9cbVfwmbNgNihGvnQDeqklSdB55t-X9qGCg-VuMgi_83eNpW2md-YVU3M1KGQdd5Fm08GYJieA5L0gVUlV7vfbz_h3cJnEaWOrvo5hKyioEZJk2pTSFroRMC0NWneFoZuHU58FQikcduD-b3G6RQfQZbEWuI_JKik1sOdFI5u9UwvO9n4tDFfxUgX7YEmRKORtAPqOvgo80KyoIuqwjaEhYA4vUUHdQnoMs2AuPanUSm4Zs98z0GO8O1Jh3Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مالک مروژ: ۸۰ درصد دوبنده‌های کشتی جهان را بچه‌ های اندیمشک تولید می‌کنند. ما از نایک عبور کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103589" target="_blank">📅 19:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c064e81c06.mp4?token=Y3dS0fhIkYkIdKXtV0b0cDMdI6zmHTWwcWwOhZe2wK_7I0-PQb-QIfZ9NUlvM4s2s9YBT2MgpWH5pzy_S2RpNHyGgZiZIEfqQ1q242wql8ZIlIAsmPavCSnt0H_z-wi10Ray_qyqnv-Gyl0UeR1JF2evzEJKCXMkQ8ZZzHNjprgI0AlwbWy0t_K6_x1hQWy3_mtnaOVvJGNI1mOOOhNMiKb1fAPK5bJFmkfOJZrgN-9TSlPuahC9b2A9xvSymRmNdpdwblugVL-lqhApQ4e_i_uNp2yIEOkEHzd_g8_HJfJ11G4oxwJRxSPZubyPKVSZ6WG3mVjaYNM48oEHSA3wqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c064e81c06.mp4?token=Y3dS0fhIkYkIdKXtV0b0cDMdI6zmHTWwcWwOhZe2wK_7I0-PQb-QIfZ9NUlvM4s2s9YBT2MgpWH5pzy_S2RpNHyGgZiZIEfqQ1q242wql8ZIlIAsmPavCSnt0H_z-wi10Ray_qyqnv-Gyl0UeR1JF2evzEJKCXMkQ8ZZzHNjprgI0AlwbWy0t_K6_x1hQWy3_mtnaOVvJGNI1mOOOhNMiKb1fAPK5bJFmkfOJZrgN-9TSlPuahC9b2A9xvSymRmNdpdwblugVL-lqhApQ4e_i_uNp2yIEOkEHzd_g8_HJfJ11G4oxwJRxSPZubyPKVSZ6WG3mVjaYNM48oEHSA3wqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس یایسله در نخستین نشست خبری خود به عنوان سرمربی جدید نیوکاسل، پیش از پاسخ به سؤالات، با تمامی خبرنگاران و حاضران در جلسه به‌طور جداگانه احوال‌پرسی کرد و از حضورشان قدردانی نمود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103588" target="_blank">📅 18:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bimi26ZWP78dzZwjeJ9viGIrwI1ZV3pXO9JNZNQWWPetcThm9ntxscZlSfd8jffxQwXWvvWqXPSVKdxjHReWkHyL0tZG-SM2p_gldIGr_turwmO7Qxvrc5OOvgDaJOv55UHNz9YhB1xiMqWH5yZscq5OW_dv3vjkmAv3yIfay7VZA2x-zPjsZOs8L0PDUqQjwbsfpbNeccoylRaLHAXSqlWIW725hpKKB8K5sjRf95RB972NM0IX8zBR6fVGH0i0H8EZfJNFnCyR-74TDQfT23NOYNiLCfgLkrDAdDZ6-_YXgOzzrKbl8t2ja8ap3onYClz8mzOLuXS8PgwCCs3b0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی پیشنهادی به ارزش ۱۲۰ میلیون یورو برای جذب انزو فرناندز ارائه کرده است.
📣
سزار لوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103587" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264b04fbb.mp4?token=NzNCeTM7Oxz5Xsljdb8-i0sbAoR9apaLU0iCAvabuXhQ0np7mkoDMvDOOB1DLKDOPxQpkr_iEDITY8EJDh91158osx9NaOOCMqGT_tdQQNWm5u5rwboSgoEhN-Kr4RBAOzOPj0DxAp7qcr1CGZ2K0pnmSpDKObC47_Pzg2Z1jq3wNsnht2leGTu_frBrwdCQZbfIACdftICfLXYDXzy8bYQR1Yw23a6ZFZ61YaebTZXCc59CDn9eeUsGUHRJ-XpcLBBketPFMErcyPiF6xpjElx2JTjGeqbOxsoybiOK3oO4M0asuQWVdVRXTK1-9StM97JhKsxCNVDQKY6__LiHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264b04fbb.mp4?token=NzNCeTM7Oxz5Xsljdb8-i0sbAoR9apaLU0iCAvabuXhQ0np7mkoDMvDOOB1DLKDOPxQpkr_iEDITY8EJDh91158osx9NaOOCMqGT_tdQQNWm5u5rwboSgoEhN-Kr4RBAOzOPj0DxAp7qcr1CGZ2K0pnmSpDKObC47_Pzg2Z1jq3wNsnht2leGTu_frBrwdCQZbfIACdftICfLXYDXzy8bYQR1Yw23a6ZFZ61YaebTZXCc59CDn9eeUsGUHRJ-XpcLBBketPFMErcyPiF6xpjElx2JTjGeqbOxsoybiOK3oO4M0asuQWVdVRXTK1-9StM97JhKsxCNVDQKY6__LiHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
عشق‌وحال هواداران فنرباغچه از دیدن لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103586" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103585">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103585" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9gtW9RtHGCe_a4nWrieobIIuOoEPZIuaK6g8SfE7qkb7T_I-I9A8Q4_l4u8Dx0U6HER0BpTMTzi9QcK-MUeidN8QVVc4K78Wr6BdgsQ2OWRhgWgTQrEYv7qOlcUjIOaxpxqzF698giqJbVzSrs3kWE9vUOCv1tAW_vkDkfj_zWbp5xBuuOSHMAPq_-EQDebLjemyepyZtmUjBsBESb4-uGFaZ753PPeTP-i8FuFqh8zC5TCzS6gjXBQ94JgoC5vtDdamn79NzemhH723RKRPtA-gw7ZDjPwmMwaEsbnQFp4_za2vVIPxhLmzaJuCsa6R_Q0BHgJsCLNIjiMNqkeew.jpg" alt="photo" loading="lazy"/></div>
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
g22
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103584" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی پیشنهادی به ارزش ۱۲۰ میلیون یورو برای جذب انزو فرناندز ارائه کرده است.
📣
سزار لوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103583" target="_blank">📅 17:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=IEkPHaQBby0d9CT03V5bnRdRvcngTGkllvP1hfMJYWTVmo-uPmeb0NymIpCo56lxgQSpOuOZZ8MJFlnskaD1oT5U_iiguTR3_Of2pkADywreR-5Aeh0_PMruyVpFA6bcfJM5AndIkqVcMP8DVBXgHTOUNhBi_HG1feTON4PvJij6c8bcBiQzuUI5L1AuVaSjm5ASIYbqBOVs2FnEkaFoGARyH_Pt5Fianp34TUZZXWDwxyijRw3OHvQNU6CQcD46W8ToLBLrLpJxCqKtQTyWTblew_8NnzeXLL2rgr28RqAEI7519Dpv_C8-KbGzaQGnSuvOyvoYO9qT2ONSIYJMhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=IEkPHaQBby0d9CT03V5bnRdRvcngTGkllvP1hfMJYWTVmo-uPmeb0NymIpCo56lxgQSpOuOZZ8MJFlnskaD1oT5U_iiguTR3_Of2pkADywreR-5Aeh0_PMruyVpFA6bcfJM5AndIkqVcMP8DVBXgHTOUNhBi_HG1feTON4PvJij6c8bcBiQzuUI5L1AuVaSjm5ASIYbqBOVs2FnEkaFoGARyH_Pt5Fianp34TUZZXWDwxyijRw3OHvQNU6CQcD46W8ToLBLrLpJxCqKtQTyWTblew_8NnzeXLL2rgr28RqAEI7519Dpv_C8-KbGzaQGnSuvOyvoYO9qT2ONSIYJMhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو کنایه‌آمیز رسانه رسمی باشگاه تراکتور به استقلال: اولین بازی آخرین قهرمان لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103582" target="_blank">📅 17:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8Ln_vB6sE6R6VnW7nQdIA8BKAYyFssbV5rQ4VtaqqK2uKcJ9f5I-A7C8musqLgegmQvqFdj6cKDCz3Fzu5OWj7IbULiLHsc1ZiJ-C2aHwVLFAZ1wp7GZ30LHZZRZrQ2gnzRxZr3RWi7e-Y5a905b7GvKEaLDiYdLVUv2Ny0UxsNjLgPhlkMj5xeyP286YAQlSoUT_IF37Jw-Rvzmwx-3_ztjqT1x_6f97gyE8pa2D0i873DVw2Pm0WDOBKDQNe5oJYYiOoZJSlsc-k72q05aTsLTq_qILFt_Wsm_OtqB53Me56try0EWnblfCT-0kjL1RDptWCFKWM8xOCHDHhoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاری سن ژرمن پس از جدایی امباپه، 10 جام از 12 جام ممکن رو کسب کرده در حالیکه 4 تاش جام اروپایی بوده. ولی شرایط برای رئال مادرید کاملا متفاوت بوده؛ اونا پس از پیوستن امباپه، فقط 2 جام از 11 جام ممکن رو کسب کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103581" target="_blank">📅 17:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AegEbis7EeU-CW6-5gIQ_FMCqEwL9LAZ-9ow5vKoxctxAgSbSc-2dTXQfkgILGEyT01_WV0mwuzEEpTPx-z4anD3zBRUTkqV1egCcf1EfJpNOY0Xu9Yi9BhHqguVbiCx2Kfus9VLN15k14hznSkeKdNmTZMv1toGenMpMZSAouxBjwOZY6QBYjGEJ3boZCBYy0Tkdv-a_ZBJcF5axzi932GWXSXwzk5O7oZMdv3VedXw68medEmNTh7tu100lnCkI3aCJdQm6I6sGcq65KNIVTJHyIBjnWYAEmXpQnTmz2-LRDfm7Dtf3zsqPQV5c6z0f1JsP3XlLDy19rVnplinPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
دریا بنگر، دختر محسن بنگر کاپیتان سابق پرسپولیس و سپاهان هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103580" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
جرارد رومرو:
خولیان آلوارز همچنان با خشم و عصبانیت شدید به تمریناتش ادامه میده.
باید منتظر بمونیم و ببینیم بعد از بازگشت خیل مارین به مادرید چه اتفاقی می‌افته.
اما حس و حال کلی در مورد سانجام معامله خولیان اصلاً خوب نیست و کاملاً منفیه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103579" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=Cepi1RtLUhaA5G1kJKmqFJIFCflVOK5XvGAqZ-dIgnWar_vCfIkH1JGzFYgU4F3hyIiXNY8_e8_GmTzzoJvzo4Ufth6ktq4j7QadFq8r7O4YVerr-m8kLkvjQ_TutZX_P5wmU-IT_tmNnL9tEnZrIdWUQuUzManSGh4U7ekhf1e_rNxxJZ5L32oswjXsRLclzelBfjw2uSDUikyMpuz6ZJERsggIwi3weazs2791GzMsF9dAtf6vMsqpO7d-l7U3A1BweFckRP0xIYmLUPPpf4Lpoo8a5kOMd0QUrqX6q3VWtQOcZgnW2JD6gcmwlMsrXd2jtXMCLc0mtC1C-cSwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=Cepi1RtLUhaA5G1kJKmqFJIFCflVOK5XvGAqZ-dIgnWar_vCfIkH1JGzFYgU4F3hyIiXNY8_e8_GmTzzoJvzo4Ufth6ktq4j7QadFq8r7O4YVerr-m8kLkvjQ_TutZX_P5wmU-IT_tmNnL9tEnZrIdWUQuUzManSGh4U7ekhf1e_rNxxJZ5L32oswjXsRLclzelBfjw2uSDUikyMpuz6ZJERsggIwi3weazs2791GzMsF9dAtf6vMsqpO7d-l7U3A1BweFckRP0xIYmLUPPpf4Lpoo8a5kOMd0QUrqX6q3VWtQOcZgnW2JD6gcmwlMsrXd2jtXMCLc0mtC1C-cSwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب سوپرلیگ کشور ونزوئلا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103578" target="_blank">📅 17:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103577">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
📊
🎙
🇮🇷
جواد
نکونام: یکی از تاکتیک‌هایم امسال هواداران تراکتور هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103577" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103576">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
زلنسکی رئیس جمهور اوکراین بالاخره دست به کار فیزیکی زد. ابتدا تمرین پرس سینه انجام داد و بعد تیراندازی با کمان را امتحان کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103576" target="_blank">📅 16:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103575">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5uLVnn1mPRL_1lFXtDXF9Is6I8Fsxxl0nXBb6Qo6zUk4SQ8dkTr7tLx22myLyfFcYT4ZnUe5SYG_70IlX_ChbfguxpvdVJXQ_MPTNpWUii_YjV4ZrSsOr42bV8JSg4_AD3LrVKku1NNSfj4ocDhgHwlzE4SjW7LXSm4mT4baoqsA-EYyGlnw7nrNpLhwOfVJcEwhOiHs-GjvhOdSpfnSTsrxXaDPPOokuvkf8XxKnR12eNHaK8mEGTrBXK34GOjNd9fY_kXR8KJ9fbISBOvrR3J5V0qNOKEpkW6MRgpRtIwkJgssGX9IRFNWpN4rQUmyHqpVdFLOl6DTanayUH5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پائو
کوبارسی ستاره بارسلونا برنده جایزه پسر طلایی فصل 2025/26 شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103575" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103574">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=ei1f_rKOnNEnoUApj6UweY5Ry9FMGbPDEoPQ4CwwE_AkM0s4BOaXdx85JXXm5Qr2KWjJdCWR1lDLV1p4l_cAs_RBqZjjm9vD87RFhfQ4gY7shkfRZn1KCW4Cahd1CnFHjBg3dUqWCviGeOS1bDufsUo_z6RANMxSEzWq3qtNccgS4E201rQdfJKFfw9e_OjZvpfknw0mE1k5eoDmBIcKHAmKAEg97rpU34WbNm1b9mtmhnzWu85qq0Ryevs3BKv7yQNLyRXXvbkaijkXg6kq2wZbkQtJSewusfGJ0NsyaN7FZBKLbXcKNnhhBh7m5CQMPJBcJJoRmWS3gC31qj6CqVdBrtO5WScCXTNFniJoMmCqbmh0neUBz7NfYopE8FNkbC_LXb3yp4eIGA9hm8CcvE2ndwjV3mcfETWekoEWZeqTfciJLtwTYY4PTAYBUR5MiF2auS00NCxJV9D41VTFASs-SlnIsKwKaatiB8ScM5jweV4TBMLOzm7sCU4gNLVXXWvT7SMR1zKEVePe2lyhoVtol5F5I1QjEDxtIMgceW-za3zHNvzT3j3DvuxUuLRNSvzW4KvToFxNYVrU3YokIBYQM63fIHspCrz6sEgjbjJcXfhoEgah93znYSjyuEOmcVXxpJIKi1PKHTxb1glIGLk86Z01wPJ3lx9onLP78SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=ei1f_rKOnNEnoUApj6UweY5Ry9FMGbPDEoPQ4CwwE_AkM0s4BOaXdx85JXXm5Qr2KWjJdCWR1lDLV1p4l_cAs_RBqZjjm9vD87RFhfQ4gY7shkfRZn1KCW4Cahd1CnFHjBg3dUqWCviGeOS1bDufsUo_z6RANMxSEzWq3qtNccgS4E201rQdfJKFfw9e_OjZvpfknw0mE1k5eoDmBIcKHAmKAEg97rpU34WbNm1b9mtmhnzWu85qq0Ryevs3BKv7yQNLyRXXvbkaijkXg6kq2wZbkQtJSewusfGJ0NsyaN7FZBKLbXcKNnhhBh7m5CQMPJBcJJoRmWS3gC31qj6CqVdBrtO5WScCXTNFniJoMmCqbmh0neUBz7NfYopE8FNkbC_LXb3yp4eIGA9hm8CcvE2ndwjV3mcfETWekoEWZeqTfciJLtwTYY4PTAYBUR5MiF2auS00NCxJV9D41VTFASs-SlnIsKwKaatiB8ScM5jweV4TBMLOzm7sCU4gNLVXXWvT7SMR1zKEVePe2lyhoVtol5F5I1QjEDxtIMgceW-za3zHNvzT3j3DvuxUuLRNSvzW4KvToFxNYVrU3YokIBYQM63fIHspCrz6sEgjbjJcXfhoEgah93znYSjyuEOmcVXxpJIKi1PKHTxb1glIGLk86Z01wPJ3lx9onLP78SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
آخرین حضور اسطوره اوسین‌بولت در‌ المپیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103574" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103573">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103573" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103572">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103572" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103571">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=Jupv-col1BH-NdEvcn-CyMawg44onJLn2g1nGjadwOHSum4JKEJIRXC9mB8pzYn3XQEAoJgcNHxP3CAWOf1YMonYM7tInrdkp1PSbTL8DyN8BTwqsJaxuxCDDLF_td_kuJxVTp3bHYTjGDZJ0ZqdWr36hN9dT_OgGTlzjg1WN-93KNZHVhAahk35FmdmXDf5TbnmuSY889-7dys3n8eaurHunKsDUiIT68BJ1ahbirNXn9zSdgVScA3SYLAeE8H-LYHNj2g-Cmen-MoLYsnoVpZRP0r4uHCJyAlPfk4MVulFlg_RVfNX-HKnYBLuqdvKj-A-Eb_VByF3zy5f68NzvwPWp3rk_q7bLzUPylAuQL3bl33tkivTPOkypjjUd8JgF2oWUrM3Km-BGxT5UuYTQFPrsSxXA6QhF02GVLPouXUrv-0ntVOeYdNaWwp2f1EEy_GEDAI4jwU5svL9PqEoGKAcINY_Eynw4sN-cZcZ6zJJN7w6Eo-GvuvoG1qhO1ZTkrUOBms6yI9r6nXGJCdD1AgjhH5wXyZvhPkepLwQjkHL_KnBY4r3bArvsfPz3xTFZzbRZ4yGo6ONJOJL1x18S_INv1QFN8Vbhj7SLendMF_ETm8J7G_FZKnvS_qw96JxeceMkIcj9wEKi1fQB8eXzToTiJ1R3B-29Wdp8kCzw00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=Jupv-col1BH-NdEvcn-CyMawg44onJLn2g1nGjadwOHSum4JKEJIRXC9mB8pzYn3XQEAoJgcNHxP3CAWOf1YMonYM7tInrdkp1PSbTL8DyN8BTwqsJaxuxCDDLF_td_kuJxVTp3bHYTjGDZJ0ZqdWr36hN9dT_OgGTlzjg1WN-93KNZHVhAahk35FmdmXDf5TbnmuSY889-7dys3n8eaurHunKsDUiIT68BJ1ahbirNXn9zSdgVScA3SYLAeE8H-LYHNj2g-Cmen-MoLYsnoVpZRP0r4uHCJyAlPfk4MVulFlg_RVfNX-HKnYBLuqdvKj-A-Eb_VByF3zy5f68NzvwPWp3rk_q7bLzUPylAuQL3bl33tkivTPOkypjjUd8JgF2oWUrM3Km-BGxT5UuYTQFPrsSxXA6QhF02GVLPouXUrv-0ntVOeYdNaWwp2f1EEy_GEDAI4jwU5svL9PqEoGKAcINY_Eynw4sN-cZcZ6zJJN7w6Eo-GvuvoG1qhO1ZTkrUOBms6yI9r6nXGJCdD1AgjhH5wXyZvhPkepLwQjkHL_KnBY4r3bArvsfPz3xTFZzbRZ4yGo6ONJOJL1x18S_INv1QFN8Vbhj7SLendMF_ETm8J7G_FZKnvS_qw96JxeceMkIcj9wEKi1fQB8eXzToTiJ1R3B-29Wdp8kCzw00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
بیاید باهم چنتا رقص دوربین تاریخی ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103571" target="_blank">📅 16:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103570">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار ترابوزان‌اسپور خوشحال از جذب صلاح
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103570" target="_blank">📅 15:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1t_9g_Ed_a_YgH56petum2vQ16K-Ht0nNMcW0z_BUDB9iOb4UBmjJowwDdqWu3ql6HaWKV7va87DtQNVECkDvHRWcSJtUD9qudVva-6BdnlowJupUlxGGR-pa5T8EOXRFxe7sX4voP1pjLGeaiNXG-IopaD79qhjwNz1R4GPS4TqUMvdXey_QvXGdsN4EuIvcK-6-NF6PtnbvbT5FHUN7YZ1c0eTleV3cbffSZiSIWzwQL9umJVy511aEdJacLhjprH1rZDguV0OM5bDw9MBLoTHKU2T2I5034_-EBmn_xnS0Llk-2eh1xTADQkFs6aXDKg_EObXM18RXk6NZjudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زمانی رئال یه مهاجمی داشت به اسم ماریانو دیاز فقید که از لیون به رئال مادرید اومد. جالبه بدونید 12 گل برای رئال مادرید زده ولی 13 تا جام تو کریرش با رئال مادرید ثبت شده
‼️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103568" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
کنایه‌های تند مجری تلویزیون به مشکلات کمبود دارو و اختصاص ارز ترجیحی برای ورود ماشین‌های خارجی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103567" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدویی که بارسایی‌ها میتونن هزار بار پلی کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103566" target="_blank">📅 14:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لحظاتی با مهارت‌های تماشایی کیلور ناواس ستاره سابق پاری‌سن‌ژرمن و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103565" target="_blank">📅 14:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw4Jbwy2vX6yIMMUKNT-tmRzoz7eVOCwc_9Ljd_QTxvIqyQC07PYKWNmGRkETKGeyEqpeacBCUPoJlKSmzNdqZkF5tNdSVz5ZdQVCGdxTsgb_WbkUopT4yo2dTUs4AQzEfn73wnx_7hQHrwTUUNStVvVqsKR_YB6DY0mYLLTIUMxtinH_a71WWOR2t0yF29IXJBLJKVGOQqA_WHW8OGVtgqhed2ZcUN9XFm-TeFVwWZ1xM_5cfYn6SP7nrLj1LH2xeSZMPZ000HLFI5eZdZyb9R-k8RKoywhgpTAiCOZX8g2D8wt8G4hK7zTRvALWl6TeYc6I0kc-dseBgbwr9AS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103564" target="_blank">📅 14:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhsAAkGjvBIRyVRLSOrXqaZxsC-mMVY9zclVE2ua6KepMy4zc9jcocCnMkFfOqXg8WWuW4iJIwo4q8h00IMWYIZxyskwjEgmVRuiNzKBn7LQgQeyQr23ZLfhzRcmOXUe8mNdsufy_lKUREP_Ojz2lwMYvmdfdaQwRjyL_siqpkROElwQuTk0fUPd1ajUE3CJjHczp5rjQop3rJsaMVIT36v6HPY97pPP6b7NfmlxZOFVgs5rG1LmzbjbgyUa9JPJ-IjLI3LPIL5DsDQ3wBleJRW08OMxQYsM_u3DmGNwJzcmTLugyBKtRBVipDSy3umZBRmzWnbKsN-NGiHOkv7Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سوپرجام اسپانیا در استانبول برگزار میشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103563" target="_blank">📅 14:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان رامبد وسط برنامه ۹۰ رفته دستشویی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103562" target="_blank">📅 14:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPVGjUu4vYNb5dSlerfER5vp1-UPEKNJ0o68LPZZ1k4hKMTmc283d95kPGNAgxRRj47ZGAyn5F7OTizBPsxU3qZ1qeaU_yBPhG2bk-Ux05BmUO__6QTxy7mQdPRKakZsJA0v4ijL_jyTxsnTNSTvcYB1pc3MKy50ABEk8rL7Xl1i7A63DkyG8W4rBxbL-BcJvEaHTADY0fcquN_uBYH8AN0Ub7yZFT8FXQyrxLnWlFdfvF2cA1gQg_S_AF752c_jjCM9IuFjPTrMunCHf3hwa-4aMmSEFJbAh484-sDWHQLEjSpNDV9rCErLQreUP3zL5HL7QpJOu3ERIKwYOG10FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ جرمی دوکو تا 2031 با منچسترسیتی تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103561" target="_blank">📅 13:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=iyLp-L0VL8tCH46AXhXFp4DvJbkvMEInO6XgzKTWnV-46-tHg1yDMXCmC0p3dtWrBeyqqvuxE9CgQu4FcMYhzEPZx--gsNE3gxa5VQaHJp7nzemMeRbK7ZgHu9WuHPXxR-cFFLl9JX_UW8M6QExaunQAO2_xpvRtfoe2bsWanTZ8TlKc1akmNylx-nn-a4tU5UkK8xjfj_pvkY6qp2Cm6AXBTtJkV-v6_tHOxKtnMNgD8Z65GAhQB2VIUVAHsXVWF3aFzDP5vRwZyjMiTYp0CS-fVHDaZIr45Hwa6ebFanIHyJVeY-wbygU9O7PEhUwVkcar2MqaIzKbWMKZp_Rl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=iyLp-L0VL8tCH46AXhXFp4DvJbkvMEInO6XgzKTWnV-46-tHg1yDMXCmC0p3dtWrBeyqqvuxE9CgQu4FcMYhzEPZx--gsNE3gxa5VQaHJp7nzemMeRbK7ZgHu9WuHPXxR-cFFLl9JX_UW8M6QExaunQAO2_xpvRtfoe2bsWanTZ8TlKc1akmNylx-nn-a4tU5UkK8xjfj_pvkY6qp2Cm6AXBTtJkV-v6_tHOxKtnMNgD8Z65GAhQB2VIUVAHsXVWF3aFzDP5vRwZyjMiTYp0CS-fVHDaZIr45Hwa6ebFanIHyJVeY-wbygU9O7PEhUwVkcar2MqaIzKbWMKZp_Rl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو: یک آغوش بزرگ برای تو و خانواده‌ات در این لحظات بسیار سخت، لئو. قوی بمون.
❤️‍🩹
🫂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103560" target="_blank">📅 13:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzEaY5IU827KnCrUO3kH2NHVOxNisXkY0BDMl2EK064HJSLC6TfBaz7K5UyIfMknIOXVLPa03HI9owhMCzvK4rqi-jyYTnJQG3gEmPhQbgZaUyA12yqWEDwh3EwSpEf5_ekONKULXE_KfWTDQaVy5k43wVuB2l5jjlGWoz1F70caPULrEHY_T6zk4g1mUgwmsS2FE5mUclZjM20ZxgtNfuZtHMysHcpNG7HJUZRQQOBJesWqkNLgaOKu-VvcIoeDNFhh1ipUv4xxLFj3eKSXb2fm7T3kJMF9X9L1voiVWFwfWU5sZVnaivqPq7e64PCKXhCpmG-yRbbSOqOFC2DMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku0C_2qW2awoLsavkDlmFZaqYN2jpIZHsBNLdW8-hcFEiaNfJvZAD-Kq6SZuqNbL57nrKlsjlqqnUtGb86CIl9m4hlMWEcG5BOjpfsH_2LhGrbrDTTc3mXMg1u1f-lAPpd5vhKjDjnAtZ3hgkXp7nCAfuqYN6EplRnmOAdUV5M4ZQNauguixtJv6jlggpdfE-URJ0j3vDRDv37jwGXx13eWvDGOyK-AV4Qlyht1mm1xprFPo-Cno1F-J85zjyTdWMu3ppG3RuMyu670vaMUfQARQGXxnHMFJLIj45HsioNyC4rGJCNblXL1a5taPbcJiW8a71_Ll2cgskipHet1gyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کامنت‌های سمی ایرانی‌ها برای پست رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103558" target="_blank">📅 13:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44077de54.mp4?token=CFjLG5VhMZogap-mOUI9vVNGxA6hNECP5tmOyeZ6JdySyqlwOTU_A0sP-XZJmm2eyynr7oZxKLZf3Rela2TWSMs7RjKhEmLy0Q6y8nuklwwOUPNTzZTiFPYGfkn-QeZK9rGy-aj9djUiVQSd-qC_R49CsUjiw1E3XVkPNPUKqWO5UeRTzJwcXqvAGCS98KEraYw45hcKrmoEZXQJmikad6uVITzW1hq2fG1kZYafYEgUXNt-cvKWc5JIctK78Cok8_mYL1xso8po-a08cyt5PmSWZYtpSwLqEMV2HRvyjx646oW1Yi3GW4ySF6j95JUIxWXgL_Ds42UHag8dlbkB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44077de54.mp4?token=CFjLG5VhMZogap-mOUI9vVNGxA6hNECP5tmOyeZ6JdySyqlwOTU_A0sP-XZJmm2eyynr7oZxKLZf3Rela2TWSMs7RjKhEmLy0Q6y8nuklwwOUPNTzZTiFPYGfkn-QeZK9rGy-aj9djUiVQSd-qC_R49CsUjiw1E3XVkPNPUKqWO5UeRTzJwcXqvAGCS98KEraYw45hcKrmoEZXQJmikad6uVITzW1hq2fG1kZYafYEgUXNt-cvKWc5JIctK78Cok8_mYL1xso8po-a08cyt5PmSWZYtpSwLqEMV2HRvyjx646oW1Yi3GW4ySF6j95JUIxWXgL_Ds42UHag8dlbkB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
ماندگاری، مدیر رسانه‌ای استقلال: درخواست سپاهان و تراکتور برای برگزاری تورنمنت 3جانبه غیر استاندارد و عیر قابل بررسی است. جام قهرمانی حق ماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103557" target="_blank">📅 13:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=Ukt4OwxpyG3cqNTm4OIotZfaI8s9CCE3QByZpX4PIwJ2PMQGhX7tx8nvHpJRZ05ru5RDzS_mqHclqBGakmbufRbrsagIiBrwKGgsvG4bfXx6JBX11sogIA5Q7W0WLwTRuajyhTc-Stt9cqTls4FwlwbUXGkmyCKhT0eAhZvRCt939GweUdN6oghSDvFVH_BjnbaE2GDxPzhtMFIgXw4a4Y4hrOfhbO5c-YBU-Ela86Txlcb7RyO-V60SILsLQv82jlJMqkP0Ml29UvT_sGKfJZBEu4FgLKTxPLrMdZ6iXKCsCTr5B9EaBao7t5MSvEVrowFVvnDN5pgZWYMdNSHXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=Ukt4OwxpyG3cqNTm4OIotZfaI8s9CCE3QByZpX4PIwJ2PMQGhX7tx8nvHpJRZ05ru5RDzS_mqHclqBGakmbufRbrsagIiBrwKGgsvG4bfXx6JBX11sogIA5Q7W0WLwTRuajyhTc-Stt9cqTls4FwlwbUXGkmyCKhT0eAhZvRCt939GweUdN6oghSDvFVH_BjnbaE2GDxPzhtMFIgXw4a4Y4hrOfhbO5c-YBU-Ela86Txlcb7RyO-V60SILsLQv82jlJMqkP0Ml29UvT_sGKfJZBEu4FgLKTxPLrMdZ6iXKCsCTr5B9EaBao7t5MSvEVrowFVvnDN5pgZWYMdNSHXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روایت ژوزه‌مورینیو از ترس‌همیشگی‌اش مقابل اسطوره تاریخ فوتبال لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103556" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85bd08121.mp4?token=cdZZA-lXliZFcRcaPZtZXwUeZBZoG3mFpeLQ89spJz-VmljLCZlqYqXuYknLnsIsq9mk1HE8jR8_lgC9mNG4thE_vLLApV_OBo_HiMaPZdRBxjZmgl1AgIeounDmHo82Zgvu3TfmLMQiov4abWpEBNXhWWovOi3RiM6LkYUFcn5oukVQrgChZ_ptG9aBmCL-LSgU4dEwMUWuxkMbiL7EO66aHOqwDuXTbBE_A_xtFVa6btDNmKz4TfzTUSBaI4xWcKqxswaPl7v06ak6Fo8jyASBCge3zmxuOqH6kSOw05JBRL7jqtCQiRWGxP87bcuw52xvxNgOlS6XS1ekyZ8mcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85bd08121.mp4?token=cdZZA-lXliZFcRcaPZtZXwUeZBZoG3mFpeLQ89spJz-VmljLCZlqYqXuYknLnsIsq9mk1HE8jR8_lgC9mNG4thE_vLLApV_OBo_HiMaPZdRBxjZmgl1AgIeounDmHo82Zgvu3TfmLMQiov4abWpEBNXhWWovOi3RiM6LkYUFcn5oukVQrgChZ_ptG9aBmCL-LSgU4dEwMUWuxkMbiL7EO66aHOqwDuXTbBE_A_xtFVa6btDNmKz4TfzTUSBaI4xWcKqxswaPl7v06ak6Fo8jyASBCge3zmxuOqH6kSOw05JBRL7jqtCQiRWGxP87bcuw52xvxNgOlS6XS1ekyZ8mcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
سهراب بختیاری‌زاده: شرایط‌مان عادی و خوب است. نمی‌خواهم مداوم از شرایط باشگاه انتقاد کنم و گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103555" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84923651a5.mp4?token=Y6joPDAKJc-WRkWRleyyHg-cxgVpNEZGINKNJv9irzroi-UW2vKh5hJIEYFVo20mOSYnC-KwiqR06eS9jII7FQuVrC3X-sxrj_MKaDeB_pjnGCHDpKpd0A-SuL2Fzug3ZZTm93AHCYAu6kU8bHx_w4IOyppj71viQJJ-BkbXtf2beNJClcoev_RqIOS2qc7K4L7SbXryNCjYVqYLYPDjdca3EKFE8dEY9iiCu_OBG3OqzQDF11uXVhhMhBwhmhWkPUAtXaPLv9211y0p6dD4ZOs4hNkQM0DQbsiGh5OeCYA-Jn_X5_LqYPLyxChDwu3fJFHuLPu1RLz0GtMeCUPGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84923651a5.mp4?token=Y6joPDAKJc-WRkWRleyyHg-cxgVpNEZGINKNJv9irzroi-UW2vKh5hJIEYFVo20mOSYnC-KwiqR06eS9jII7FQuVrC3X-sxrj_MKaDeB_pjnGCHDpKpd0A-SuL2Fzug3ZZTm93AHCYAu6kU8bHx_w4IOyppj71viQJJ-BkbXtf2beNJClcoev_RqIOS2qc7K4L7SbXryNCjYVqYLYPDjdca3EKFE8dEY9iiCu_OBG3OqzQDF11uXVhhMhBwhmhWkPUAtXaPLv9211y0p6dD4ZOs4hNkQM0DQbsiGh5OeCYA-Jn_X5_LqYPLyxChDwu3fJFHuLPu1RLz0GtMeCUPGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
اولین کنفرانس‌خبری فصل سرمربی استقلال با کنایه به رامین‌رضاییان
🔻
سهراب بختیاری‌زاده: بازی دادن به بازیکنان پایه در استقلال سخت است ولی در فصل پیش رو حتما این کار را می‌کنیم/ باید به جوان‌ها بیشتر بها بدهیم تا اسیر بازیکنانی که تحت تأثیر فضای مجازی هستند نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103554" target="_blank">📅 12:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyDBQXye4HozU8HIACddjQU_-8buOFtRRJePdBNcOMI1jPyKSuI7Ow1Q0gg0oZXwHOZ80p5zqZNn-UoKKEHx_C11_VIojmXOZ7g4VMOalqs60GPlzy3DC4e_Z6R8y1ZHyUH-BLhAO5U9KuDLsd_uNPyXCJTtTERcIoGYkk5yBR47G_959LJZXovzGkGsN75QRbRtDbzpX1qxnFwbf5E61iEm0GCJ4RKxO7Xt3rL4YUvbp0CiyEV_xqpmk-0tQfOac71ie-gmeNKupAfMQq0mJlxi5YPxjhEdgitWxojFOl81vs5c78Bl8Th4Li_jZTBLePe4trK_t2DfP29jHManHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇮🇹
رومانو: بارسا هیچ پیشنهادی برای جذب لائوتارو ارائه نداده و اینتر هم از طرفی مطمئنه که کاپیتان خودش فصل‌آینده در تیم موندگاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103553" target="_blank">📅 12:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103551">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=WdDHufqQfAOcnNBqerlPLMMArw0UzIF5sSVxwc3eKxBtuUM50E9sFLBG9beawnWwr7SjEabYcow0liu_Gi5mNYL8V69hvC0H8fND4c8qPlDtP2OxF-Ji7pCqDdTniJOrOaItdmHuNTCxB-QfQuaat6op4QCYgUXjJWy28gxuK_jufaNdm3IGGfgNV4VLsCZQSm8kjfoo45j4O0PWKvSg8bqf109ROvTpdn_wTscJyYQku9OjGXl2Vl3fPmSXkosSlCKMigZ8lpjDB_Ke2QmmvgY7V1KhiTsYkFvZyHSk2gt3bx8J7nVdUO_iqY8M1ZmsPj-pCO9s3IodJ_YVckkMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=WdDHufqQfAOcnNBqerlPLMMArw0UzIF5sSVxwc3eKxBtuUM50E9sFLBG9beawnWwr7SjEabYcow0liu_Gi5mNYL8V69hvC0H8fND4c8qPlDtP2OxF-Ji7pCqDdTniJOrOaItdmHuNTCxB-QfQuaat6op4QCYgUXjJWy28gxuK_jufaNdm3IGGfgNV4VLsCZQSm8kjfoo45j4O0PWKvSg8bqf109ROvTpdn_wTscJyYQku9OjGXl2Vl3fPmSXkosSlCKMigZ8lpjDB_Ke2QmmvgY7V1KhiTsYkFvZyHSk2gt3bx8J7nVdUO_iqY8M1ZmsPj-pCO9s3IodJ_YVckkMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
تصاویری متفاوت از خورشیدگرفتگی از داخل یک جنگنده و یک ایرباس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103551" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCIuovaqFnVjjsN6JtMcbMX7cjCnj6gndwn_tpgis5LpGcKaBWKLAmC6pFskpnyubvM86dHP6bCq__d9WSMo9eP4AqmaKm0iDEea19fPx_e32S4i2eP36TgWbOeOAH2F12t61XMLJOdZM5lS8jKA7ur0b56gQ6JRKUoQK_6uyi3evUER9K-j0tzs0GMf6jMmp4qiyi5wGogHElv0ZJQXqtWUdgVKxFtkyMSaFaPwhdopWV3VlQNUCgxbGQ_c1LJYGuFEIOSVNDlmb86mxlAkvpyIl9gcLc8QSDVQC5BlPI9GEwb15Yr_a5dJxYovjjlMi56qxWeCPmGzgw0iuIAN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
برنامه‌هفته‌اول‌لیگ‌حرفه‌ای‌عربستان که از امروز آغاز میشه؛ رونالدو بدلیل مراسم عقد و عروسی خودش دو بازی اول النصر غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103550" target="_blank">📅 12:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954fdc44b4.mp4?token=nvkn_p35SHcvVbeX_E-peDvqRSxeiX0p-dL8SjBsUtUBAFD1IMeRdqX49fDKJqU4NAM08OOo15Eanpo10nYwd364c8BUFbD711FuvbaRy0IKoCoCBD-uh6Xs16100e4UQv-6D6EO2-dEVmCODoe200orCwWMkv8m9ephIrTrVMPYrIG36PnX7lAYg-curX9NZElf3etHp3jDUb4XR25Ju-zf2IEPt-tRpR5tr1u7dOpGyO_1S4NcZp3-3HGFFe4vCyjUFuYR5oXSiNF8rw93yS1J_QKvi6R6hjKSbpyMAJf_CFYjaOmGrl-Jb2PG7lE9d-Uy8ndkTc_3QuCavBCrHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954fdc44b4.mp4?token=nvkn_p35SHcvVbeX_E-peDvqRSxeiX0p-dL8SjBsUtUBAFD1IMeRdqX49fDKJqU4NAM08OOo15Eanpo10nYwd364c8BUFbD711FuvbaRy0IKoCoCBD-uh6Xs16100e4UQv-6D6EO2-dEVmCODoe200orCwWMkv8m9ephIrTrVMPYrIG36PnX7lAYg-curX9NZElf3etHp3jDUb4XR25Ju-zf2IEPt-tRpR5tr1u7dOpGyO_1S4NcZp3-3HGFFe4vCyjUFuYR5oXSiNF8rw93yS1J_QKvi6R6hjKSbpyMAJf_CFYjaOmGrl-Jb2PG7lE9d-Uy8ndkTc_3QuCavBCrHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
ویدیو بسیار کاربردی برای‌دوستان باشگاهی که تمرین پا قراره انجام بدن؛ سیو کنید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103549" target="_blank">📅 12:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-97XaHZ-AOTc-F5M08fWPs_xu9ESQ-aBawVOJuw-l-xoUSjRbDkXJUQbTttk0YiYnu_5WaB_dgYiIr-_WdoXXqfrDR-cf6hTAwi6E5ryDd8OSzKILrelqqtDuEgZ14IPhLPQQOOo0SYBdSprDWUMfTBMNJfbXbnbo12D8kMf6BwCNBu8PDv7bEHREylO26q21_9FYVWYBf_prbZ_3lrfFcpFA92-19szz8-5aMQFApmJlEtvs2AVijhQdodOaKrT081qIReSl7SNl-H9DqfGx3DhIzBWeEmLvv9c20nBZ1_R9KYbVAPYOOdjX6YweIxpTEA0cadYzW6WLMLd_Eekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚜
باشگاه تراکتور از کیت اول، دوم و سوم خود در این فصل رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103548" target="_blank">📅 12:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gme7wtmMPosTeUa_2KPwzuYq0NxB6Q63lm9UDg5QVZtEKIRVU1HqjF8I7fNn6MrUD2a2nLiSvw2wDCJeJiLy8Y-hUschEcji3pS2RsCGlXnu2HdndlM1XJzz6OjWXsdCvVceyt4_3DsdUC1cE6WC6SR6hYbKgcnUd30rjXQqvFaJScQjcN6rUyJTaAuRY1GlynI1Oa1vftAn1EPWLujE9zDQTsujvLBg6NRvDRtXLlA_PoywUHt4WN_sPD5j5WJkWs1fmGNgAhIfo2ddM5jpmj_pHmtF4UAhPPWauJIPuHSty3edivFLYRN94yWMj8rX6aRFqsNdNEPgsKShSqax6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن جیکوبز هم تایید کرد:
منچسترسیتی پیشنهاد دوم بارسلونا برای جذب رودری را که حدود ۶۵ میلیون یورو بوده، رد کرده. مذاکرات بین دو باشگاه همچنان ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103547" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UllOQ7iCclfjjBXgmZxfrorw5ZqY9K7U_H0ZPTkdeRScCl6TFJW7IGEsKq2ey8IO_JxXOZLcUnWrQasFrLf7j5lFnulXGnfba1fDGVTtITOa1jo90fhkCxPdeeMJQq1xkIjLxobfMHZjvPpBi9kNOELlbgHekzH00yn9xOcZcZOtBrPVxmK9OoTXywpSwrGaRnNufZishmyLP2VcOEe9Jt83R6zFGsboldS7JsztckgNK2BWG8OV6siawcDaJnNV9uPUY4gjCzIq6y112KOOAcGC-I-IVBYUdWF1lRha7qjRBeUha9uddnHtZ9jhdKXE9If9TxmMvCDuigZMtHhrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇹🇷
ستارگان سوخته منچستریونایتد؛ بازیکنان بزرگ فصل‌آینده تیم فنرباغچه ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103546" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk_LkYXGJ9aqn_tdOXHvUATMihK_TC4oATOHCIcW9xMK7vmxvp9E8TxYg0iv8IUWqNgDhBJROuKMcrVpBLoSE2Lia-LExVIJlBDREKZpFons_GMtpwhP7LwKBBsNBc1I8uvd32f-Ii1Tf6Lb9atDnlwT8T67QJuEo0LN2gbbItr4ZejQNRQQR79fHDvUPfVj0yET6dTtFbRIKeja33mG6h9cTmjwdCpYrWS5cfyRa6HcNiwl0nVMQeqUgmOvHMgseXHqOseg6QtoP6kE4vJUUIJZRgnS1ZLFEHKiSTBUpwLHmh9Rrxzsce_2pzpbChN8RF4Jq7JFqbz3qNkHG9LfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e13d26513.mp4?token=DBgZac1MBsX7zsXt5f02QzhoYUgqIm0TMcn4Q7MM0j6g4LEySDLpvF5h7p8-5pVU-7e1ivTGIqLTsxRVO5smm8O0Ki97ZcMlCkOCO_uW3FmJ0EfTh1A-TtCCYYmXBpy_ydvMA5BL2LEgHhCKVu5px0o5EO4txPROeWs5hEJBBXAR2hGHi45TKsKJbG8h7wbFY3JUPahqwyRZ99aIvsj4DKzF3mSEYUi0YT8K2g9I70-tiQN5pXr2ktX7u-3YEVc4mQrU7XXRKuTbyF-Zm8wmL-pFD0MzsNnC-qotyKXfDinf7XigJRX1rMKMuSna9UtEkoVnEKpDm7U0j4OxErRftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e13d26513.mp4?token=DBgZac1MBsX7zsXt5f02QzhoYUgqIm0TMcn4Q7MM0j6g4LEySDLpvF5h7p8-5pVU-7e1ivTGIqLTsxRVO5smm8O0Ki97ZcMlCkOCO_uW3FmJ0EfTh1A-TtCCYYmXBpy_ydvMA5BL2LEgHhCKVu5px0o5EO4txPROeWs5hEJBBXAR2hGHi45TKsKJbG8h7wbFY3JUPahqwyRZ99aIvsj4DKzF3mSEYUi0YT8K2g9I70-tiQN5pXr2ktX7u-3YEVc4mQrU7XXRKuTbyF-Zm8wmL-pFD0MzsNnC-qotyKXfDinf7XigJRX1rMKMuSna9UtEkoVnEKpDm7U0j4OxErRftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">9 سال از این سوپرگل تماشایی کریس رونالدو به بارسا در سوپرکاپ اسپانیا گذشت...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103544" target="_blank">📅 11:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e210c19682.mp4?token=J96iAcNENZxlw0yaiaFnx9mzU12xZu6cZt0Th2ukey_ZmEUKS5nI7g37iTxg_lRrTuAX9D6AZltoG4CatxEnNjkETdqZ-pweTKj1-USvGpz8AAefUz2sfOFhnh7124Sb5u-qmjGQfY0UMqP4wL2iAvuk0dlcZGkDk3Es8WQij5n9pWx3AkavkpGvgG9oH2_UUFyPbaMG4i8GT0FT3_A794cYUDpkHxP1Pc65_pE93AAT8fbSPayt0oi5hCCgCYMqHcbKW5b1f1bug626Nrth2MwoWYK5lgdXoI2rk7BBp3XgnXNB1ctFs6Q8lC5jwLaDNTPl4T8T0765FopDA_uKIHk_-U8gsb_gef4a-HPE7VQ4tx2tTjBntPzuQLE7n_Qf9LbbG3_uayeORT-K33g4himPFzRgx3QJ-InksPUUElzsECPrZ_k4NIvREDsCqexFZ0N1aCtReBf4SLV6P29TVPa2XmAhuOkp6yCGIF91ZgX7eOVP2sOW7ch0XBks84hvOD07mZf2dEFEfbyUxTpVNH0TavQ1iYr8zRb4SDTolL7V86YUO3M_3bzhiPrDWkZ0U9DbO8feul5FasoXu9dNOQdI7jSQfkww6EVFPmfXSOOPsSgGBxdC6sdjIFH8nrWAaZ8kH5kGsdryoKUaWe4mo169sRdpB9Qgf7lJApuR9LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e210c19682.mp4?token=J96iAcNENZxlw0yaiaFnx9mzU12xZu6cZt0Th2ukey_ZmEUKS5nI7g37iTxg_lRrTuAX9D6AZltoG4CatxEnNjkETdqZ-pweTKj1-USvGpz8AAefUz2sfOFhnh7124Sb5u-qmjGQfY0UMqP4wL2iAvuk0dlcZGkDk3Es8WQij5n9pWx3AkavkpGvgG9oH2_UUFyPbaMG4i8GT0FT3_A794cYUDpkHxP1Pc65_pE93AAT8fbSPayt0oi5hCCgCYMqHcbKW5b1f1bug626Nrth2MwoWYK5lgdXoI2rk7BBp3XgnXNB1ctFs6Q8lC5jwLaDNTPl4T8T0765FopDA_uKIHk_-U8gsb_gef4a-HPE7VQ4tx2tTjBntPzuQLE7n_Qf9LbbG3_uayeORT-K33g4himPFzRgx3QJ-InksPUUElzsECPrZ_k4NIvREDsCqexFZ0N1aCtReBf4SLV6P29TVPa2XmAhuOkp6yCGIF91ZgX7eOVP2sOW7ch0XBks84hvOD07mZf2dEFEfbyUxTpVNH0TavQ1iYr8zRb4SDTolL7V86YUO3M_3bzhiPrDWkZ0U9DbO8feul5FasoXu9dNOQdI7jSQfkww6EVFPmfXSOOPsSgGBxdC6sdjIFH8nrWAaZ8kH5kGsdryoKUaWe4mo169sRdpB9Qgf7lJApuR9LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
این داور فکر کنم اصلا کارت با خودش نمیاورد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103543" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103542" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103542" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103541">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhgUIh4MOjMTuwSVsgFI090b6wmX0IZzN0W2-alDVHnf1Z8rjWzdy9e4OI73uBKSTFkfopmlSfI2vx-lTENqWRRRdi7Y_7LbCd-Xz_dfOhCauvVGN3EhOMkZ1nEjoLAHWFUpiStJ9GDA2RNSwXibUDy3fTfZ9_FA3bJdpcAeF5Il_iQyDwElktdUxRGpvD4PkGD9zTPnZa9V_f4CZLaymZDKW925DoGPSjg3Rczwa395-IL5zm73_g2zovDx19n60VrOP1VXfdnlK2hoi09dwEH4YOCitAGXWSuVpI5nquYyshI26pX3kDjVpY_d-MQzLfPMGSgpthwrkRXCNkzMzA.jpg" alt="photo" loading="lazy"/></div>
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
️برای دانلود اپلکیشن کلیک کنید
👉
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103541" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_OnI88bVNS0V-j6toOHvk2HgDrpt5DRYvE93L4xfY0erRwj4iX0Q_tztVdACGRoamguGOOaQN8uBYQTV6fmOOzDJsCGN4j8cJhCfS3ctc4P3VJehBmSnZhmyTiLKYltNt4rDxLPPgQswfPpKdMIdW3bRVy0sWcQ1MO_b40a5EggZ40TWseW-zjKvdJ5w43RncmJrtNpywYH3AO80eU9njyeVtAunNx-hbBSPHDFm_NdbrmxNp-revoDPG9EsYUNC_d0o3sew6xv8Cj0uXbjd6nhuJqrUgn5XR7yXB4JLgOIdTn9DlrdZw3HPvLNyBcxEzPoQZIggZ6CXs-ResoUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
بازی‌های موردنیاز اساطیر برای زدن ۴۰۰ گل
🇧🇷
نیمار: 653 بازی برای ۴۰۰ گل
🇫🇷
امباپه: 537 بازی برای ۴۰۰ گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کین: 631 بازی برای ۴۰۰ گل
🇵🇹
رونالدو: 653 بازی برای ۴۰۰گل
🇵🇱
لواندوفسکی: 632 بازی برای ۴۰۰گل
🇦🇷
لیونل‌مسی: 525 بازی برای ۴۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103540" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎙
تقلید صدا شنیدنی با استاد علیرضا جماعتی گزارشگر قدیمی شبکه‌استانی اصفهان
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103539" target="_blank">📅 11:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C03MgwXO2R4bUSWX-OTjzw4xcGQA-nb31R3UJwxQDTtcpS24nvFFbyBecNVyvHXC6yspw3OtbHrLHotq_RTAOvODMvulPqhukaCjvhyti_qKAFDhfuPS2_NoA36SJrhN4jQwVHPp7Hl3Uv-MASGymsm8dRYQtfobXIa-sUjKhW5yYzi_P6Nyfbbpx_M1lbiI7BKInuQzXUkrhFfysZv_HxY8xQrLpo64_wieiveo4Zn5iYPeeVeUOKX4t4f7MzChhZiSBuprxaPGrTzGQHn5srLGxQTQRYkolH0BwR3GlwQdZNYIJft2krlZMAXV82eNvTEe3GE1q0GzWVIbzkNVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: باشگاه القادسیه عربستان که در لیگ‌نخبگان آسیا حضور داره، با ارائه پیشنهادی نجومی به منچسترسیتی خواهان جذب تیجانی‌ریندرز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103538" target="_blank">📅 10:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">▶️
🇮🇷
ویدیوی دیدنی و جذاب باشگاه ملوان برای رونمایی از پیراهن خانگی فصل جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103537" target="_blank">📅 10:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvF2ImCdnmSvXbjPFYqb-QsLrBBDInYrEVRMrk5ATXTsdS3Nn-gJPFryk0jhRWy9u_LvG6LNtDwT4m08ZHMraCyCtrosgpUlaJZLXsCydkg-Cb9wd8xFUxPAAkqCn7powe45DkARSJ_efFVJt32B1BIamMp-LjDJsBeVSwp22xmFRfPt6WCBkNJRQ7_GSS9b7jI10fCE_-eOIl1SHujDQbIK0xsvywUdQcpLKgQX0FvQHPgGjib_5S1u35TTLWATiHyHxjDuD43sk5QTfiUEf6ax0QU-GVTInqRDOPubFdiZ9Rj_48pVLBr-pjXje_Vb8Ni0XFCH8niHadJKWctsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💫
تصویر روز ناسا
پنجشنبه ۲۲ مرداد ۱۴۰۵
🔸
عنوان: خورشیدگرفتگی کامل در اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103536" target="_blank">📅 10:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a4112b9b.mp4?token=Hqm-hpQTQs2ZxRjDgCrnoTIep088xQKLlX21Aw5KGbpE9maOwuIhhD-t8T-foh0umi7xACIz-sabTd7MK9EZ_feSP9zVUn--lhtBYtwPTR_w76mnJqOGSiH9b-OoY9xXRe2dBIwoLY-mbsI5Rc7qYCg2VIqB0QGnkgBYbxm23TVZbghN-8GWG4Smk_WNiH-dR5740sCgwu_2zAmRsDpSxymHT0iB3Vx3O7Gzca_piytcUJB0DUFgMvj_oQED_z-xbSBQTNLv_aa0kZcIxs0b22RTDR8y9JZjQPrrHtpD4jOfIM5qmKVoa3v0mRehSrSJg6rtq0YtStUe445ePPzm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a4112b9b.mp4?token=Hqm-hpQTQs2ZxRjDgCrnoTIep088xQKLlX21Aw5KGbpE9maOwuIhhD-t8T-foh0umi7xACIz-sabTd7MK9EZ_feSP9zVUn--lhtBYtwPTR_w76mnJqOGSiH9b-OoY9xXRe2dBIwoLY-mbsI5Rc7qYCg2VIqB0QGnkgBYbxm23TVZbghN-8GWG4Smk_WNiH-dR5740sCgwu_2zAmRsDpSxymHT0iB3Vx3O7Gzca_piytcUJB0DUFgMvj_oQED_z-xbSBQTNLv_aa0kZcIxs0b22RTDR8y9JZjQPrrHtpD4jOfIM5qmKVoa3v0mRehSrSJg6rtq0YtStUe445ePPzm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
تاکتیکی که قراره برای بنزین اجرا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103535" target="_blank">📅 10:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srVZCzJ82dE9R6lVRUpg1pSMT8HhkcCeCsTHEMHlSTzkLmD0hGTCREFPVDW__CjqriB7wn4QE_cWz0cHMazQay-g4gOjj-nl2td4ZsxBktP0RIwixhS77WXOPxemOu1twSsXGGfFzzHsWfy6E7v2AhofNiGSHUoLyNi1Odyq73mcX063ZSHWfrT7OB21RZpy2n9gtZ_LzHqHZakM7Yb94uz6hAr9ZDvVa55HnwIDpSZrXTmpbwLzUHB6NwsdghkgrVe7Lj7LQVWwobeNmCXSQGvcezkDi2KD9VaHBx1y8doK7gYLQJkvDrLLhZt32E14VLqwt0F6DJvbP4RujbCFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
علی شیخ الاسلامی، دستیار فصل قبل ریکاردو ساپینتو در استقلال به کادرفنی این فصل مهدی‌تارتار در پرسپولیس اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103534" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc4d6fef6.mp4?token=mnSM_apb_p1YIrJXysW-9qroID9Ygw7_bl2-HYYDOo1M2wRQp1gjqkCPwaRP7HR-p0hmW4ArVqxYpIYNtXPwhZi_bpy5bat5DohEzhvSf-eXCkid6ov_RBBQEdQPynolJ5thBJ3N6ZqqAPale5ZtJUPyQSmSepO-DkoptI5QY0bVkBUMRGqsPRDTdZJuQ65ga_L0EjFLfRttrQ23QBvz00AjTkP1rGA_8YT-4PQruM7v_l4641VRKdF6jvULNIgZ4m_HQ_0X4z9wd6V8Nv669D6TtUrAzliNN6kLvIK0iL9_zCB8RnAUHDlh9qJnUnKrOg_DC2F0kwigLca__jOtQl0ixU-TmJq9iCXrMytMH_nT7mwrRFcdzwZyKtieABgNcPWN4e4yuxBEBascxOD6kO4Su52o95wRX14JsSmEL-SdiQ3jncZQqXHaKvtww-3j53-q8hcNQdOPoSUgzqXEytbfEHiJEgIWtKIIVxzd2PeL0nmGBMpHSKtw0apT_Cdjqe1qW6f1AmSJYCRr_1EOrHujYgjniZ1YQaf98XdBWt78f3v9hgm8O8rdun3ICUbK_a_k7kMcHTJwl8gelFUWnuwmgktodOvGedLBDcBoKNsawvUhRPweIBYolaF2DQr_d3y8tvXtdZe4K23dyyOaoUmsfFtmtHKMJh6KtmaWn9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc4d6fef6.mp4?token=mnSM_apb_p1YIrJXysW-9qroID9Ygw7_bl2-HYYDOo1M2wRQp1gjqkCPwaRP7HR-p0hmW4ArVqxYpIYNtXPwhZi_bpy5bat5DohEzhvSf-eXCkid6ov_RBBQEdQPynolJ5thBJ3N6ZqqAPale5ZtJUPyQSmSepO-DkoptI5QY0bVkBUMRGqsPRDTdZJuQ65ga_L0EjFLfRttrQ23QBvz00AjTkP1rGA_8YT-4PQruM7v_l4641VRKdF6jvULNIgZ4m_HQ_0X4z9wd6V8Nv669D6TtUrAzliNN6kLvIK0iL9_zCB8RnAUHDlh9qJnUnKrOg_DC2F0kwigLca__jOtQl0ixU-TmJq9iCXrMytMH_nT7mwrRFcdzwZyKtieABgNcPWN4e4yuxBEBascxOD6kO4Su52o95wRX14JsSmEL-SdiQ3jncZQqXHaKvtww-3j53-q8hcNQdOPoSUgzqXEytbfEHiJEgIWtKIIVxzd2PeL0nmGBMpHSKtw0apT_Cdjqe1qW6f1AmSJYCRr_1EOrHujYgjniZ1YQaf98XdBWt78f3v9hgm8O8rdun3ICUbK_a_k7kMcHTJwl8gelFUWnuwmgktodOvGedLBDcBoKNsawvUhRPweIBYolaF2DQr_d3y8tvXtdZe4K23dyyOaoUmsfFtmtHKMJh6KtmaWn9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اشک های غم انگیز پدر طالب ریکانی بعد از پنالتی معروف از دست رفته پسرش
🇮🇷
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103533" target="_blank">📅 09:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7815ca585d.mp4?token=Xe86elQ3E8MvzGHbBXt2zxEd9KnncZ8KmC0rdlEXItM28xr6zEQnKO-BZdYS5iFfhTXZRdz-bqVMbk3skvDFqyah6I7mHHLZuOOD9jyptHOUpRqrQu5xeHBpBOuuZi5xzzMc520N-PW8Ud3TKxW_YQxAn1Gq0XMf3WuMJuSqZOdBFBEubj0XVB990icfG_MFv7XxHjnEmaSa5OBikvounzOyeaOICyqRlgOj0UIS4vli2T043l4COGzWeZc5p9q5HVyWDteaWs33xwWf5OUK8878PrDrpCLlAVCRTz8GHJebD9OPBIT4JOSNgrSZMe6xed2VjgyByBIgEUrCZDpcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7815ca585d.mp4?token=Xe86elQ3E8MvzGHbBXt2zxEd9KnncZ8KmC0rdlEXItM28xr6zEQnKO-BZdYS5iFfhTXZRdz-bqVMbk3skvDFqyah6I7mHHLZuOOD9jyptHOUpRqrQu5xeHBpBOuuZi5xzzMc520N-PW8Ud3TKxW_YQxAn1Gq0XMf3WuMJuSqZOdBFBEubj0XVB990icfG_MFv7XxHjnEmaSa5OBikvounzOyeaOICyqRlgOj0UIS4vli2T043l4COGzWeZc5p9q5HVyWDteaWs33xwWf5OUK8878PrDrpCLlAVCRTz8GHJebD9OPBIT4JOSNgrSZMe6xed2VjgyByBIgEUrCZDpcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حرکت فوق‌العاده زیبای بازیکن تیم‌لئون پس از تک‌به‌تک شدن با اسطوره لیونل‌مسی در بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103532" target="_blank">📅 09:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df00ddf89.mp4?token=tzgmryxDBH5c6F_6Yx1FxRipcrhXRbU9xPjkKRKywSzPrM8a1EsY8MyOkJ_wSUE-I23Z1Wq4jvniuwPbLv-Ia4ReWDWPklKO92Q8abdOg55Zc2XrR6ziYSb6qJwpzeKcLRxpIBUEDEK7c7BGINblG-uzd0cYe_Mz8cfsc8DMR_ldXFe_ItoMryKxdccidA9BILvJZ4hQEmpdKrGAAgVF3dNVPKD777jOyLjt0C55ATfuUNO6XyedQ4UHjYjTLE1wWErPFsXn_OR9Xso3hswykbPICsp1nY85YuB-5-fwIlC7hlAFe3jv6weoXoEx6ltIywY8O9_75mDMFApCqJUhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df00ddf89.mp4?token=tzgmryxDBH5c6F_6Yx1FxRipcrhXRbU9xPjkKRKywSzPrM8a1EsY8MyOkJ_wSUE-I23Z1Wq4jvniuwPbLv-Ia4ReWDWPklKO92Q8abdOg55Zc2XrR6ziYSb6qJwpzeKcLRxpIBUEDEK7c7BGINblG-uzd0cYe_Mz8cfsc8DMR_ldXFe_ItoMryKxdccidA9BILvJZ4hQEmpdKrGAAgVF3dNVPKD777jOyLjt0C55ATfuUNO6XyedQ4UHjYjTLE1wWErPFsXn_OR9Xso3hswykbPICsp1nY85YuB-5-fwIlC7hlAFe3jv6weoXoEx6ltIywY8O9_75mDMFApCqJUhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
مسی تنها ۴ روز پس از درگذشت پدرش، در لیگزکاپ برابر لئون برای اینترمیامی به میدان رفت و به‌شدت تشویق شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103531" target="_blank">📅 08:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT42BemnPaI9QWdPEj-b9Yc4I_S6MDHkPqnCMjW-phV2byjyzg7r9JlqC4Efr5Sbb_meBzwY7eiuaPmzLxqrx0T587YHc74f3dqUVDtFGOJU88kmEvopDheLR0ci73XNMJfMxURaczVbyoCjIizDQdLnVv88BBMmEMMtosDOZ4o1w4hMqA3d_D7iwH45hrnRHcKkM_uDAqXYK-fFVKKOPN8d2Xn4QZnUm_bhJREhXnZAL5NeIWW5bhaamxVoQD-hFz505stM5uabMCcpFSMDFHlahRGN7cCktnIHNHX4_ZuHA2hqYgE0jY1MnkCKlyoMPYImSbxUl055Lk-lKCxcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
سم آلتمن مدیرعامل OpenAi:
احتمالا تا 6 ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103530" target="_blank">📅 02:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad3b95df.mp4?token=T97jgtX0IhSdqYK4_xXjgfoL8YAlvYU2dKZDoUyogeWJ8u46Zp83cgjbIImKrGC5ggO2quiZaDeG1wqrOmbEC8VrQZvxERMI1yZ9G6iDz6edcQ2XVPiHkDaHk48vY6NlVqFLVDzhJEQcd10avo_en0f0KiYLSKapSO4A-96-LG143VlI6vCPuTacwCAmjyZtHPyP8W8Vj5uclbvIkVzvoV_DjjL7pTrHWHuD5QnQHGAHSc2wYsy1_fkVfxxMrObSp2bOOVeVm1zUS8TJeci3msT-YyVxXG3EejH4aNbNHi6YaAttREhaOd9R9f3WKvQk2ymTJRpow9Ao4SDoSX-fAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad3b95df.mp4?token=T97jgtX0IhSdqYK4_xXjgfoL8YAlvYU2dKZDoUyogeWJ8u46Zp83cgjbIImKrGC5ggO2quiZaDeG1wqrOmbEC8VrQZvxERMI1yZ9G6iDz6edcQ2XVPiHkDaHk48vY6NlVqFLVDzhJEQcd10avo_en0f0KiYLSKapSO4A-96-LG143VlI6vCPuTacwCAmjyZtHPyP8W8Vj5uclbvIkVzvoV_DjjL7pTrHWHuD5QnQHGAHSc2wYsy1_fkVfxxMrObSp2bOOVeVm1zUS8TJeci3msT-YyVxXG3EejH4aNbNHi6YaAttREhaOd9R9f3WKvQk2ymTJRpow9Ao4SDoSX-fAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
با قهرمانی پاریس در سوپرکاپ اروپا، حالا رقابت بر سر توپ طلا هم جذاب تر میشه.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103529" target="_blank">📅 02:04 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
