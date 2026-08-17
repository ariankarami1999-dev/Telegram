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
<img src="https://cdn4.telesco.pe/file/PlJl22EP_--VAQlzfw2NekhSU5Awex1Jn72TU3TROoKGEPEoq1eSQSV54sXWI1M3xTGLMMz1Bafegfkd1a-sT6D0kNvh0VdtduqZUvBoNL2rNpRo2firvgKFsZMTaqQMGezkDu22m9TT9r_qDZKcPW-NMxfn9qn3WLQQK6W0z_ZLDEsQitWwRzypeCinsEKu2RS4zi0sQ7rlLaW7cL_bJBDXd2uQ8GoyRGgy6QQZidbb1Fk2HU3fNboi7J_i63oFVZ5nRourA2KFfoB9G-7P9U6xTwc2PrSOVHCOHTSf_jXtfYnx1iyGdGqxvftF_RBI0KgmIgRC6QVE4VwIcmUfmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 122K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 04:13:21</div>
<hr>

<div class="tg-post" id="msg-70168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/news_hut/70168" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Gtk9O_3v81VGY1gi5UEisWt4y8XwOwbTPRsjjR5tjn9wzmpDP4IMRkY93cNFQ4h_SwKqMNXnEz9pLRY4Dn_480xoAFYdNeEp7l7JyGqj2nsnPiFiaH1_uQW9FYPDM2ns74ETFHmsox36JEjjtZiCdRnr9T013d8rgo0_DMkFOeyhdETNyHkVQmlg3-wJYoUN82Riuwj6clLWOzyZ-Oes5kWQDsqhWqaVi_-bMpuCoBqbCIlN4vms3TNJ8UZgeh2pI6B1A0Mzg2WuZybFv7doHYgBba7SXRGxvyzzJWxBNda-bD1xus46TrEC6zBOqSYKVWC_n3meFCHRgNA0lwZzaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Gtk9O_3v81VGY1gi5UEisWt4y8XwOwbTPRsjjR5tjn9wzmpDP4IMRkY93cNFQ4h_SwKqMNXnEz9pLRY4Dn_480xoAFYdNeEp7l7JyGqj2nsnPiFiaH1_uQW9FYPDM2ns74ETFHmsox36JEjjtZiCdRnr9T013d8rgo0_DMkFOeyhdETNyHkVQmlg3-wJYoUN82Riuwj6clLWOzyZ-Oes5kWQDsqhWqaVi_-bMpuCoBqbCIlN4vms3TNJ8UZgeh2pI6B1A0Mzg2WuZybFv7doHYgBba7SXRGxvyzzJWxBNda-bD1xus46TrEC6zBOqSYKVWC_n3meFCHRgNA0lwZzaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/news_hut/70167" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQok7quRRpPHq2kXrr2B28gsW4eOhrg6iodjae0Es_DH0qygJViIWIch6qQ3TzkC3uofgPa7A9JXtuCl_bhvHS7fUhcCuOECSaUXfVr6InC0zqNAYUFY3muwYoYS-aR8fa1bx6dbKNLlZFQMYM2vjHDsPHBvoCeij8bWG67aO2AM-JaboP2m5jXIJoFAUn_yt5tCcszOzHj1Yo2T4w6s8hys6W1mO99LSgyKEqCb8vERWZebZViWXnZoAy8XgtY5IOPH0vyf_JhbnfqbaWi6NzVYfIlnJxzF0G0m2lqDMxldhqx8DgtiVfWD80GDyJcip1P_LknCu0Lj3G3yvLSLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
❌
مارجوری تیلور گرین، نماینده پیشین مجلس آمریکا:
در جلسات راهبردی درباره استفاده از سلاح‌های هسته‌ای علیه ایران بحث می‌شود:
بله، درست خواندید.
این واقعیت دارد. من حدس و گمان نمی‌زنم؛ من از این موضوع خبر دارم. و این شرّی مطلق است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/news_hut/70166" target="_blank">📅 01:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI8-YJ4bOMnZBXtQF-54SluStJDE0-AmFUtuiWGPf05EzZ3SArBc29hdAJKBELFAooBT1dMA0Db6KeaiVUlFi2_x8nw5G9fJ8hmcWGWCiAKE3c-hBa5FMj3c0j67NZmntmuEujMrPi9EY99F6KLXSUfI97w6NySVlj67qP2VsLZg_C4HUeXYwgxqIxA6gFYXHdMjGyqkF9oei45J7NBuAwioqyhdAqZeBgWLRBdH7FNIFCRTU6PU3x2ynE6QYHOmPR-rlLlF0grqT1q2blziIsdhz6YuHHKnaiaV1bGeX41rRYL30dn212QoSC8zEzYIMJHTuOuix1jz0fdT6ZDIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
ستاد تبلیغات انتخاباتی جدید نتانیاهو:
🔴
مجتبی خامنه‌ای، زهران ممدانی، رجب طیب اردوغان و نعیم قاسم را کنار هم قرار می‌دهد:
«آن‌ها می‌خواهند نتانیاهو شکست بخورد. نگذارید آن‌ها پیروز شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/news_hut/70165" target="_blank">📅 01:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOiVbrNzny_uGZkYbeCr_w68iS0Lk02dT2ojqz9IZSL1INCd_z_TObTqoaO3ymZMimtG-HW9UW2YfaRWm-kR2VUouuurmanoFnNxmeF_pdlCMJdG22pcmxHJ5bENmf_nZ-3fsOpCsphbUfCDzrR9D2fmr7sX1wSjPriWCDrtRFxC58YwCDhbvMCVNxvks_ipdQCllVdL-pqWjH6xg2SMyBLvajMv_DFhl2Aj0o7pVOQXf-DplOfiKDUnBCH4Qdqfh4_z05rnGSgpCOwu06H25_x4zTPsM58eVhZADvJLLorpJBeS8fNAYDkYQR81Fd_mZF-16FzwY_FWqzNjXZR8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
🇮🇷
#فوری
؛مهلت ۶۰ روزه مذاکرات در چارچوب توافق صلح ایران و آمریکا در اسلام‌آباد به پایان رسید، بدون آنکه توافق نهایی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/news_hut/70164" target="_blank">📅 01:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSbXlp1Q2yKX7L0DR-bpd85svGtuh6uw_oVrqtzP9v6xLCzveyF0TenKpcpTLrquQW7-DQhJ-0Bk8jA50Eox3aCIk8n0Ndty9oMZApoMhecCN0EtnoOenem_kKoC2X16kt0fh7dJ4AmO9D-Dz24k6voDSECR2A5TENDMC4wpjOa50k0MymyyfyBL5c1R9GnBJwJSoSLpfKsxp7QvDvP7fqEFPSH9QuKNvXWT0QecUbNGufrCZceVVWkot82SkQpFrCOdWFuF9LMooCv148E8USM6zM4yeGfzFu3p2BcH-NqWRShg9ffxAnP6Qx68MqDJBf_yL35naQD2AwC--vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
با توجه به رابطه بسیار خوبم با کیم جونگ‌اون، رهبر کره شمالی، از اینکه ایالات متحده مدت‌ها پیش با مشارکت در رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده است، خشنود نیستم. این رزمایش‌ها نه تنها پرهزینه هستند — و بخش عمده این هزینه‌ها (طبق معمول!) توسط ایالات متحده آمریکا پرداخت می‌شود — بلکه پیامی کاملاً نامناسب و خصمانه به کشوری مخابره می‌کنند که در تمام دوران ریاست‌جمهوری دونالد جی. ترامپ، رفتاری محترمانه و عاری از تهدید داشته است. از این رو، و با در نظر گرفتن اینکه برای لغو کامل آن‌ها دیگر دیر شده است، به وزیر دفاع، پیت هگسث، دستور داده‌ام که این رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد!
⏺
اگرچه شاید موضوعی بی‌ربط  باشد، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایلند در زمینه خلع سلاح هسته‌ای جمهوری اسلامی ایران با ما همراه شوند یا خیر، که پاسخ دادند: «نه، ممنون!»
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/70163" target="_blank">📅 01:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRLbSZ5E3PK3dptuVoKGTYmXzPT0syHan_s7jiDvAh2PHltyHLyNxO_xzJl-W3iF2wSFZNh98CI9-FpXcc8BlWnr1Wd9biHld6u_F237Ark7MIvQqb2egBYREgZur9phQOjmKKrphsKNdk3cOyBpEaLFL5VLOY4WskXFwR2-kse5yLV6KU30aeRvDLbg6RWRq6-g7xqaNSOxi8F78b3-pze7OGYCU7HfCPeGKwslnL4yjDm7l_zusgPE_XRTlmaBYTOUSjvB-bFvL6wf5fLn-RFTj9VUxkTsg7UqNT5hRTGvYsKEnEWxLNBhZr6X9RmDQJ9Klfiq5R-_JEpJLXXnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d94596467.mp4?token=nxi5QgYZ_JjCvoF1BdkM-GCkbrnGyZno2FmCxMAXzy-ipHxR05yn8i50mzpzP06KI36vOQlgVRceLJc-dFdvYaMx79ERGfCtwBYaFZPaID48NwgI_J-qGIHXiALzqmpdAfFBrKme-Hb0vcgieafFxHkf79YmQ6yMBSw_i80leIjNU2CNIgrNKaA-n6OoK3Y01OPdZwoCQU3IiuhpXZHDp2U8kgOtYCNR73YMn9hrFxMqKIogU8uDHFzY21mK7ri0s1axiiq_FVPW_OTaH00GWaI5pS0r8ESW6Uqf29iVgWWRFqvZ_A5BA3F1Lc-_kzVhrSA-m4VGV8-iv4N_YdmbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d94596467.mp4?token=nxi5QgYZ_JjCvoF1BdkM-GCkbrnGyZno2FmCxMAXzy-ipHxR05yn8i50mzpzP06KI36vOQlgVRceLJc-dFdvYaMx79ERGfCtwBYaFZPaID48NwgI_J-qGIHXiALzqmpdAfFBrKme-Hb0vcgieafFxHkf79YmQ6yMBSw_i80leIjNU2CNIgrNKaA-n6OoK3Y01OPdZwoCQU3IiuhpXZHDp2U8kgOtYCNR73YMn9hrFxMqKIogU8uDHFzY21mK7ri0s1axiiq_FVPW_OTaH00GWaI5pS0r8ESW6Uqf29iVgWWRFqvZ_A5BA3F1Lc-_kzVhrSA-m4VGV8-iv4N_YdmbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام:
یک جنگنده رادارگریز F-35A نیروی هوایی آمریکا هنگام گشت‌زنی در آب‌های منطقه‌ای خاورمیانه، توسط یک هواپیمای سوخت‌رسان KC-135 Stratotanker در هوا سوخت‌گیری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/70161" target="_blank">📅 00:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=c53RRjnrf-jw7TbqDotZAzelhzYXwlhPhUSiGXgpwQtpeGjKkC8lz_4RSz6efLkZSxGyAWnWjBXXjokBbxoIqjseuSMis7cVqKTCP7JRPlWKOHAPl2QdwPMIKn7ZeK3Jjg22DoH4QkO_Fd1cUf9z-5x0cIgSkNaS4Xi0JhYPrX0me77xQzoScBfS8ysTTpCM7ZqM7Fb_zl0_8Y_x0LgrW2Eu1zBNfouMVsdnfJ5Z6RNhJrCzKEi0ACtBjxD6jfsSAJCvLxbOhUl6paEICQVoP3xsVz0LKdbpyC_1E7K4jKJ4QT79VLTrJQT0h5jip2ruBbwbx3ACA3GuJmtyJzuE1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fddf8c9b.mp4?token=c53RRjnrf-jw7TbqDotZAzelhzYXwlhPhUSiGXgpwQtpeGjKkC8lz_4RSz6efLkZSxGyAWnWjBXXjokBbxoIqjseuSMis7cVqKTCP7JRPlWKOHAPl2QdwPMIKn7ZeK3Jjg22DoH4QkO_Fd1cUf9z-5x0cIgSkNaS4Xi0JhYPrX0me77xQzoScBfS8ysTTpCM7ZqM7Fb_zl0_8Y_x0LgrW2Eu1zBNfouMVsdnfJ5Z6RNhJrCzKEi0ACtBjxD6jfsSAJCvLxbOhUl6paEICQVoP3xsVz0LKdbpyC_1E7K4jKJ4QT79VLTrJQT0h5jip2ruBbwbx3ACA3GuJmtyJzuE1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
قالیباف:ما در برابر آمریکا پیروز شدیم
منظور از این پیروزی، این نیست که ما ارتش آمریکا رو منهدم کردیم؛ منظور اینه که آمریکا و اسرائیل با ۹ هدف مشخص و اعلام‌شده به ما حمله کردن، ولی به هیچ‌کدوم از ۹ هدف، در هیچ سطحی دست پیدا نکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70160" target="_blank">📅 23:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=PL7xrCEdBDMaN545J6G48G8tlErH8HnnPSWo3-eUXM3RlUacJ_fsk-cynT_ASQinvHYjLEyJ-Avvc_36am8T3P6RT_RaETlisT1o1vXvJFWzUR911Yx8J-OrBgaCB_qKumFTXgrAk6d1v5S2DfUzHtlzAMdvorCOjKnPZwv4TVHQL139iaG3y7tQcsWpC2Hc_7bs56vGlalE9ohD30Po05cqRV7zcEblxlXfLNDJIJpwlYE8o2xKzuaJ83w6p3hLgAIE2zZQcPYFH0UUheMTeiS50m_Yk5XZGMwy0b6eO8o4WCZjLCcoA2MmhMl6V8GmAyyTdZcf6BMcrIEYTPAGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=PL7xrCEdBDMaN545J6G48G8tlErH8HnnPSWo3-eUXM3RlUacJ_fsk-cynT_ASQinvHYjLEyJ-Avvc_36am8T3P6RT_RaETlisT1o1vXvJFWzUR911Yx8J-OrBgaCB_qKumFTXgrAk6d1v5S2DfUzHtlzAMdvorCOjKnPZwv4TVHQL139iaG3y7tQcsWpC2Hc_7bs56vGlalE9ohD30Po05cqRV7zcEblxlXfLNDJIJpwlYE8o2xKzuaJ83w6p3hLgAIE2zZQcPYFH0UUheMTeiS50m_Yk5XZGMwy0b6eO8o4WCZjLCcoA2MmhMl6V8GmAyyTdZcf6BMcrIEYTPAGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ریحانه قاسمی زاده مجری صداوسیما:
جنوب ایران،فدای جنوب لبنان،اینو یادتون باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70159" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGjzcips0jfONWvtPZy81GckeiaIiyZraf6BwxxeUYOMKwe9WAWilwICyWXzmPCDRnibkRrYHfo_rUbMeyyiAt23CWrSEzCic-t8_qknWWPLv9ToXvyxaxqEBb3p9galOsby65jPiDXiElvLjaLXLWA9_5gpVZVRPdgfUJsZTMMeMtCEcejMrZ11XTJiXbsAxDCMI7BeFVq8Or27o707hqjNDEQUKyE-iTXeI0Qmj0fpzPi-fHPM5Lf_VEbSm4S5z9mLvrQXCWt5DD_qfXT89xgLvLb9Dz5B-kJRT-USYPROqEahWt5QE8xz6JiVGtJokrEsY_6NBkwYjSU-byc_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
آسوشیتدپرس:
ایالات متحده در حال خارج کردن آخرین ناو هواپیمابر خود از غرب اقیانوس آرام است؛ در همین راستا، ناو «یو‌اس‌اس جورج واشنگتن» که در ژاپن مستقر بود، در بحبوحه جنگ جاری با ایران، برای جایگزینی ناو «یو‌اس‌اس آبراهام لینکلن» عازم خاورمیانه می‌شود.
این اقدام، غرب اقیانوس آرام را فعلاً بدون ناو هواپیمابر آمریکایی باقی می‌گذارد؛ هرچند اگر نیروی دریایی در ماه‌های پیش‌رو ناو دیگری را به این منطقه اعزام کند، این خلأ ممکن است کوتاه‌مدت باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70158" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=gF7YnldcdJfZWatEEvpiFF9CUfub6OeuZev55z2gry-b_UwL0BKzNaVRP59vaeGW_zVrpdbL3F-54ITX6uw6L4o1MKgCakvUcHnNODEguAJ4llTCDnwCudTQAbkW4x2Z1CZuCWA_kZakd4KbmxCnr1EqqK00VBjxco8jOzuj4YBVIgaBgOJcdKs1-hboE9YliDDIMJngpZOZGgfFE6ufJdYvXOgMjAawKgMOZ21miS1MzZx65LiqVLNTPEVQB9CDWsTachxims0SSs6KywrIa6z7OeWxvvWJP9zHf12QbeswaObPFQelFftFwu4JyCiXVlLN-R7Zi3DrsoTaSbucdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0bb40eea.mp4?token=gF7YnldcdJfZWatEEvpiFF9CUfub6OeuZev55z2gry-b_UwL0BKzNaVRP59vaeGW_zVrpdbL3F-54ITX6uw6L4o1MKgCakvUcHnNODEguAJ4llTCDnwCudTQAbkW4x2Z1CZuCWA_kZakd4KbmxCnr1EqqK00VBjxco8jOzuj4YBVIgaBgOJcdKs1-hboE9YliDDIMJngpZOZGgfFE6ufJdYvXOgMjAawKgMOZ21miS1MzZx65LiqVLNTPEVQB9CDWsTachxims0SSs6KywrIa6z7OeWxvvWJP9zHf12QbeswaObPFQelFftFwu4JyCiXVlLN-R7Zi3DrsoTaSbucdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
املاکیه دلقک درباره کارولین لیویت سخنگوی کاخ سفید:
متوجه شدم که کارولین لیویت فرزندانش رو بیشتر از من دوست داره؛ بابت این موضوع خیلی نگرانم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70157" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=eoBKN62tMbbxah7dcHtADHbTZnrbW6gsLKQPzjLsGmW4yxlxeTXONvT-nOrkJsruIr6hixq2OlHMtsJ889nYFdRRX46pi_AQNCiSvew5TuO9GwlN8wTKCrS5BlyZ-s0pUnDV3v6g6hSfI9lHQDl8Zz1i8e7Ll8MdlM1sdhfTyjysSvV__4fGqATBS_FHlxJnWUVR7N08EUk6hNMiWRBPaznf8GGY9X3B1w5FBWexeWrt2FOQ8mdQT-EbWNdEg89Z5pIUzuSHlNbf4BP_ypESb4F1smUQjpvPmJna2fOidU0UhiLoLYAyP5lt9z79Wn4J2Cy8JvHRzOgoAizffE02fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbbbc717f.mp4?token=eoBKN62tMbbxah7dcHtADHbTZnrbW6gsLKQPzjLsGmW4yxlxeTXONvT-nOrkJsruIr6hixq2OlHMtsJ889nYFdRRX46pi_AQNCiSvew5TuO9GwlN8wTKCrS5BlyZ-s0pUnDV3v6g6hSfI9lHQDl8Zz1i8e7Ll8MdlM1sdhfTyjysSvV__4fGqATBS_FHlxJnWUVR7N08EUk6hNMiWRBPaznf8GGY9X3B1w5FBWexeWrt2FOQ8mdQT-EbWNdEg89Z5pIUzuSHlNbf4BP_ypESb4F1smUQjpvPmJna2fOidU0UhiLoLYAyP5lt9z79Wn4J2Cy8JvHRzOgoAizffE02fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فرمانده کل ارتش ایران:
هر ایرانی ای که بتونه یه نیروی آمریکایی رو دستگیر کنه یا بکشه، ۳۰ هزار دلار (حدود ۵.۶ میلیارد تومن) جایزه میگیره
😳
پاداش نیروهای زن آمریکایی هم دو برابره و به حدود ۱۱.۲ میلیارد تومن میرسه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70156" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=kTXDiFoLrjeWlzY3OrjtcZ2urBHpe3GGY4OnqOXxfioGpde_0AcOUV9xADHTroM1W52an1RhrUYuErEmO8b_Z7m58KU0GxrqHqEhRcg4Z0fzoPYcy9TGUW2Sddme4Sdw6EuYH4O4QcDr8ovDftAS9KZBwBs35eRTxaK9FIVmfwaEhhZJGZjhJNDwMiHqyLE9KnSsu3gQ3nSRrofIp2nBgjVvEaDoSgZRrOytM625XhbaPAvvF_N1hUpTjoV2ZIbewWp3befeSb6GchNCCA0ecypElZXj12Dtctufg3SgO8d840md9ph0V9LqQiuRWhYmvEZp7JHIrcvLUrpcllDvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4c542f7f.mp4?token=kTXDiFoLrjeWlzY3OrjtcZ2urBHpe3GGY4OnqOXxfioGpde_0AcOUV9xADHTroM1W52an1RhrUYuErEmO8b_Z7m58KU0GxrqHqEhRcg4Z0fzoPYcy9TGUW2Sddme4Sdw6EuYH4O4QcDr8ovDftAS9KZBwBs35eRTxaK9FIVmfwaEhhZJGZjhJNDwMiHqyLE9KnSsu3gQ3nSRrofIp2nBgjVvEaDoSgZRrOytM625XhbaPAvvF_N1hUpTjoV2ZIbewWp3befeSb6GchNCCA0ecypElZXj12Dtctufg3SgO8d840md9ph0V9LqQiuRWhYmvEZp7JHIrcvLUrpcllDvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار خطاب به پزشکیان: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
🇮🇷
پزشکیان : ما داریم کاری میکنیم بچه ها اگه مدرسه نیان ناراحت بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70155" target="_blank">📅 20:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=XK8qJPLXJ7j1_SvNKHs21ZhuJF64Ta0f-Wm-YvHWbv3affDgnxcRr0KnZL82Ox00DWJpYUmOub93KU6G8YsPwX28CdjIZCdsgqk32S2sf4GPHuJmwrFaf7kEGEXvoLM_ymjLA0JQVcQZBcSwWzYfOoCdvcZGG-g4gi4fhj1nozdmmmduVMxMMe0RVS62XOJ2bY7qTsVYd5MES9K4Ksb6zbq2qmjprN4CC0BeNXf2-AgdSCicHmsglbguttYGdpfbO9r9yxOtxmLPYpTHxgOBCIekxtEX6j1amX878tVWlJY_CVq-PcnGquFvqvv67hnu67qh_zm24NC3uOQDp8VlxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf26ef809.mp4?token=XK8qJPLXJ7j1_SvNKHs21ZhuJF64Ta0f-Wm-YvHWbv3affDgnxcRr0KnZL82Ox00DWJpYUmOub93KU6G8YsPwX28CdjIZCdsgqk32S2sf4GPHuJmwrFaf7kEGEXvoLM_ymjLA0JQVcQZBcSwWzYfOoCdvcZGG-g4gi4fhj1nozdmmmduVMxMMe0RVS62XOJ2bY7qTsVYd5MES9K4Ksb6zbq2qmjprN4CC0BeNXf2-AgdSCicHmsglbguttYGdpfbO9r9yxOtxmLPYpTHxgOBCIekxtEX6j1amX878tVWlJY_CVq-PcnGquFvqvv67hnu67qh_zm24NC3uOQDp8VlxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
امروز صبح پهپادهای اوکراینی به یکی از اصلی‌ترین مراکز انبار، دسته‌بندی و توزیع کالای Wildberries حمله و اينجوری داغونش کردن:
این فروشگاه اینترنتی که به آمازون روسیه معروفه،‌ سال پیش حدود 75 میلیارد دلار کالا از طریق این پلتفرم معامله شد...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70151" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lyurKovoRkWHiQ9aNTpWfvIRRz22ugBNUEI_jfIyo5HhADKOOjWpVGwAgqSfB4vhyGqhfjJ_Ch0gGvRVzDftq7CPIWTtSPNM1pG48Ax-d4mdFDbcYIrVrjJk6omvAmi5k84ET73wUtme1YRUPmhMhd6UP8eEEzC1TuyDDM49HJHipiecqtI0928a7UtiMmcfIcuIvTyyFFIexYpA64IvxvB0VILGjTTYY4IfdLtlkBl3-YABjqv1cf-ZunXzT3y5xxmLJ45lxegGxOat_BMcVYcvbqD6fvA9aorlpP9ulgn1-QsrRQMPDQPEqBePemSS7fc1KveLRfQh34Ctcy-5n2GxQIM_0hhsjfyy3ZpZEsxEMmX1haYTAcGeorXQgGP8Ot2ZDv2lUV977GnOVz6RT66VIu5pXT_fNZqG4LYNeqVVwzZw4kdgD6ihhbNkhpnqppsYl5MPByvY6PnIqRWmXRormoCDoghn3ssQJDyqPJBvwgBFMP2sSO57zXkSoD-yyoJD37syNthCF14aYzteMejyLqyNCSaj1NdLWGqye5jlOnFbOSmmjF655nfia_10m3VDdJOG2eauLzkMOFaTvaWNBlozp5v4XnIPhVS76gPeq_YwruDVBu60-9VaRm5OgH7ghsrPFhTRdKgBN2tMeyib3yxDfkBaAE5yUwYu8Ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63850d9e4e.mp4?token=lyurKovoRkWHiQ9aNTpWfvIRRz22ugBNUEI_jfIyo5HhADKOOjWpVGwAgqSfB4vhyGqhfjJ_Ch0gGvRVzDftq7CPIWTtSPNM1pG48Ax-d4mdFDbcYIrVrjJk6omvAmi5k84ET73wUtme1YRUPmhMhd6UP8eEEzC1TuyDDM49HJHipiecqtI0928a7UtiMmcfIcuIvTyyFFIexYpA64IvxvB0VILGjTTYY4IfdLtlkBl3-YABjqv1cf-ZunXzT3y5xxmLJ45lxegGxOat_BMcVYcvbqD6fvA9aorlpP9ulgn1-QsrRQMPDQPEqBePemSS7fc1KveLRfQh34Ctcy-5n2GxQIM_0hhsjfyy3ZpZEsxEMmX1haYTAcGeorXQgGP8Ot2ZDv2lUV977GnOVz6RT66VIu5pXT_fNZqG4LYNeqVVwzZw4kdgD6ihhbNkhpnqppsYl5MPByvY6PnIqRWmXRormoCDoghn3ssQJDyqPJBvwgBFMP2sSO57zXkSoD-yyoJD37syNthCF14aYzteMejyLqyNCSaj1NdLWGqye5jlOnFbOSmmjF655nfia_10m3VDdJOG2eauLzkMOFaTvaWNBlozp5v4XnIPhVS76gPeq_YwruDVBu60-9VaRm5OgH7ghsrPFhTRdKgBN2tMeyib3yxDfkBaAE5yUwYu8Ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت این‌ روزهای جاده چالوس:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70149" target="_blank">📅 19:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=H59s6MPvRTb0mletiMo9lQA10z8esOn0epmvKZ6MPAd03Rt-sbNlJHIyaiI4bDrKa-Sq-Lg1yLl7voDT9tj79X63Gw4ixOLerzuSmi-4xeR5PXnES9URPJwgubgQ5P7cwUjuutt2amcItHM8xveq0973CAhtAMAmfMuDK4L7K_yC572WEhSOzt_If9wvn1LYDNVB4AJIYf2eizSmppQXZhoKhNK_ST6BjLdND2MUPgt6AWju_vJYcaB_nRUmeEC8iemQQDXfjP6jJE5jfxTyGUI9g3M86V6KTAW2pit6C4qGjWo8V6Llz-GZsyOdYCa-glpetbMY_nBL2u8BTYGbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b0bac1f2.mp4?token=H59s6MPvRTb0mletiMo9lQA10z8esOn0epmvKZ6MPAd03Rt-sbNlJHIyaiI4bDrKa-Sq-Lg1yLl7voDT9tj79X63Gw4ixOLerzuSmi-4xeR5PXnES9URPJwgubgQ5P7cwUjuutt2amcItHM8xveq0973CAhtAMAmfMuDK4L7K_yC572WEhSOzt_If9wvn1LYDNVB4AJIYf2eizSmppQXZhoKhNK_ST6BjLdND2MUPgt6AWju_vJYcaB_nRUmeEC8iemQQDXfjP6jJE5jfxTyGUI9g3M86V6KTAW2pit6C4qGjWo8V6Llz-GZsyOdYCa-glpetbMY_nBL2u8BTYGbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محمدرضا نقدی، مسئول ارشد سپاه پاسداران:
پیروزی کافی نیست. ایران به دنبال انتقام برای خامنه‌ای است و به بسیج دستور داده شده است تا فعالیت‌های خود را در خارج از کشور گسترش دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70148" target="_blank">📅 19:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=IpJke78a7KBf1cYQKMq5LShoaQ4MgMNTJMcXduOR5leTBFk019AmN3KkpX9jyHvnQvSkpF1rPK5bePJQvRaiRRHIapnXA3YfDuEJ-acYA-hapJB6UDSO_tckZOKLhQK000nEzbl-UD3ttY2ekCfA2L4SwHCNLGhoRheKukAnsznMIqiQdSpFeSqihx90j5JCTofPvbEWaOZV9QzBT_R-U4IAjZ7hH1Cfgmi6YnSScipW-VtQWT4JVTA83YC-0ltbYj4Peacw33rPFF6cjE_ZV1R6HCkKOxx0qhFhRijqbrjmPUDIYqCpwphypUq_OEtwrXG96V3x6w8-TEcHeeO4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f0e41933.mp4?token=IpJke78a7KBf1cYQKMq5LShoaQ4MgMNTJMcXduOR5leTBFk019AmN3KkpX9jyHvnQvSkpF1rPK5bePJQvRaiRRHIapnXA3YfDuEJ-acYA-hapJB6UDSO_tckZOKLhQK000nEzbl-UD3ttY2ekCfA2L4SwHCNLGhoRheKukAnsznMIqiQdSpFeSqihx90j5JCTofPvbEWaOZV9QzBT_R-U4IAjZ7hH1Cfgmi6YnSScipW-VtQWT4JVTA83YC-0ltbYj4Peacw33rPFF6cjE_ZV1R6HCkKOxx0qhFhRijqbrjmPUDIYqCpwphypUq_OEtwrXG96V3x6w8-TEcHeeO4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیمان طالبی مجری صداوسیما:
نمیشود بنزین قیمتش جهانی باشد و حقوق ما ایرانی.
حقوق مارو جهانی کنید و ماشین ها رو با قیمت جهانی بدید، اونوقت بنزین هم با قیمت جهانی حساب کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70147" target="_blank">📅 18:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsVI4d0CdM7T6vxAOVZBbWWZ5OtROam1DWgNHIkIc9NQqe1pd-OTCyGWtKqvEOEODjIVzUCeMGAT2yuSRDQBvOygE0HR5McTTIzsut3XQJUYN209A228lQ2ZJoljyS1UjwL5Kg4lPrkD1vYJuSjxk1dKGVhWAt_H16qxZ6jrcze3fcZn08rGoyUFIO4EV3Bkl0BF-pbzQ8rL8W8q0af71MgIZevhEFLdNqKWIS5Yi4OVZuwalk_ACtB0w9zm-J0LI9WCTy5q8WDN0YWsl_-JQEBPTnAv-1EoVnfF82oHMriY5iXTtkC13mB6YP1CYrtFsJKqeaxx4_-g4Tpu45CSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در ۷۲ ساعت گذشته سه کشتی در تنگه هرمز مورد حمله قرار گرفتند؛
طبق آخرین اطلاعیه مرکز اطلاعات دریایی مشترک (JMIC)، از زمان گزارش قبلی آن در ۷۲ ساعت پیش، سه کشتی هنگام عبور از تنگه هرمز مورد اصابت قرار گرفته‌اند.
دو فروند از آنها در آب‌های سرزمینی عمان در حال حرکت بودند، در حالی که فروند سوم در مکانی نامعلوم هنگام حرکت به سمت تنگه مورد اصابت قرار گرفت.
هیچ آسیبی گزارش نشده است و هر سه کشتی به سفر خود ادامه داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70146" target="_blank">📅 18:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70145" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvpIJ-0f0aK5a2Tg4Med5btWcjS52384dtIvu2NogbmzKx5krUCir9zvAzCRREEgK7eDXwkeBKqlz6vRT7IIGJ5h8jbtQC2bg1pluh_qPUcLQjl-3_OmhT3zPVP05a4vJsHvtQXXuuKFEXUQQ4GE5VU4DngTtGJxQ2r-li5LGkFkCUc2HRA3dxjWDkswcS0X4oxzEPEFrTzR1bMVFDhLVfPTpfHig_z_jYZ4ILJCYqlHPcCm7MrN-7x99EDZHgNDDj5fAJugU3jccGxPgtusDcLlkhG1ShuzkK89ZaJFCDWxBC7itzQHjEtA2POkc24wzVTyBX16GCYuJGv58F_2GQ.jpg" alt="photo" loading="lazy"/></div>
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
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/70144" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=PQ31hCICksx0sK1-6BD_ujbzdQHYAWMCPk_lmuNmv5eQ3_3wnSlG_GARpePvCZx1RfDAEqfAKBPIaSJ_2EQ0dLxXU0hM0LGHZIXzAiwCz3RFRKFVxI6yu_isKD4_52KVkdDFXOwYZ2Pc_sNysWszJSjs2V4r4r6I09DKffzCH_zNnHAot83cvO4EHRMWmEMAIgUuHMLx_Gj_9bbN-O1hMs37FplUUzt3HItw0nAffaoq2x07O8HmQ3YK-ZJ7q9015oq-3Zx26laF1u0eAloARYx3i2Z04GI2XcN4czm7YkiTIeBlRTilCIkuy0ALUGL2ohekdbaHCjAJcCtOPPzFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f965699a0.mp4?token=PQ31hCICksx0sK1-6BD_ujbzdQHYAWMCPk_lmuNmv5eQ3_3wnSlG_GARpePvCZx1RfDAEqfAKBPIaSJ_2EQ0dLxXU0hM0LGHZIXzAiwCz3RFRKFVxI6yu_isKD4_52KVkdDFXOwYZ2Pc_sNysWszJSjs2V4r4r6I09DKffzCH_zNnHAot83cvO4EHRMWmEMAIgUuHMLx_Gj_9bbN-O1hMs37FplUUzt3HItw0nAffaoq2x07O8HmQ3YK-ZJ7q9015oq-3Zx26laF1u0eAloARYx3i2Z04GI2XcN4czm7YkiTIeBlRTilCIkuy0ALUGL2ohekdbaHCjAJcCtOPPzFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: از سال ۶۴ درگیر مباحث لبنان هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70143" target="_blank">📅 18:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=LzJ_IyoAs3_XxkCuMAUpzXIpXv3_VfsHVDVIz2SNBD_zA-CUSm2llTLXs1K40GHzK1EPo5oeqCoOp94DmgnuPqiXui5xus5gUzB9kI55TwQ61up_toi2ctg-1KMRvn-VyVc9Kabe5wki3BiW6Eogante1_11eUJm6IDKCCTopHQMgHR2AJQ2f3SqM6wuxNgXvZYFTXVLtFsThqLjDivPw-pzTLGwBM0NDQNZsNLkCUTbhsa-jr3zDsJWM33VLMaFYwqZ2TnL5kP7GtUbIaOxIU01RRhEno5Sa3swh5lDdu-TwlJyYjvllLPhzbj7bfLEs_vzgZyYtaSRcQOJYXoITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa40fcbf2.mp4?token=LzJ_IyoAs3_XxkCuMAUpzXIpXv3_VfsHVDVIz2SNBD_zA-CUSm2llTLXs1K40GHzK1EPo5oeqCoOp94DmgnuPqiXui5xus5gUzB9kI55TwQ61up_toi2ctg-1KMRvn-VyVc9Kabe5wki3BiW6Eogante1_11eUJm6IDKCCTopHQMgHR2AJQ2f3SqM6wuxNgXvZYFTXVLtFsThqLjDivPw-pzTLGwBM0NDQNZsNLkCUTbhsa-jr3zDsJWM33VLMaFYwqZ2TnL5kP7GtUbIaOxIU01RRhEno5Sa3swh5lDdu-TwlJyYjvllLPhzbj7bfLEs_vzgZyYtaSRcQOJYXoITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجری صداوسیما:
تاکنون ۸۱میلیون تومان پاداش برای قاتل ترامپ جمع کردیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70142" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2UHCc7G3Jh_0EueT4rvqcS2mdUbZrFpqWQE18DuQSoo5v0deSnunp3li0iR0--A64ZzE0NZ0nqI6Rbt90MFJS887m9ES0GkYL3TAgEtIijkgNq0XtIbN91t9hxQY2uA-F69L6hNYSiNUOsap4ZPRpbWboSCTKcGq7aFJgT4g6uFfFv1i2yFHUMU17pwSJlvaP4NXiqdsgB5az8LO7p5GJ9PNsz_LnOmG9JlyrowTkI8m2WtOM6SnEVEkyvfMhYzBeX5DA302F-WDrzKZt5wPQ02vvnDjI-Cj-OrIFLGnoFjzI-jdapfJCnY-MulDgpEK2eITTfqORv4rmlPINa_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:دولت ترامپ در اواسط ماه مه، از «نیچروان بارزانی»، رئیس اقلیم کردستان عراق، به عنوان کانال ارتباطی محرمانه و غیررسمی برای گفتگو مستقیم با رهبری سپاه پاسداران انقلاب اسلامی استفاده کرد. مقامات آمریکایی پس از تردید در مورد اینکه آیا مذاکره‌کنندگان رسمی ایران — یعنی محمدباقر قالیباف، رئیس مجلس، و عباس عراقچی، وزیر امور خارجه — اختیار نهایی کردن توافق دیپلماتیک برای پایان دادن به جنگ را دارند یا خیر، این تماس را برقرار کردند.
در حدود ۱۰ مه، «تولسی گابارد»، مدیر اطلاعات ملی، با تأیید صریح رئیس‌جمهور ترامپ و معاونش «ونس»، با بارزانی تماس گرفت. او به دنبال ایجاد خط ارتباطی مستقیم با سردار احمد وحیدی، فرمانده سپاه، بود تا بررسی کند که آیا رهبری نظامی با مذاکره‌کنندگان سیاسی هم‌سو است یا مطالبات جداگانه‌ای دارد. بارزانی که به زبان فارسی مسلط است و پیوندهای عمیقی با تهران دارد، در ۱۴ مه امکان برقراری تماسی امن را از طریق تلفنی رمزگذاری‌شده فراهم کرد؛ تلفنی که توسط یکی از مقامات سپاه به دفتر او در اربیل آورده شده بود.
سردار وحیدی هم‌سویی کامل خود را با تیم دیپلماتیک ایران تأیید کرد و اظهار داشت که سپاه ترجیح می‌دهد بحران از طریق مذاکره حل‌وفصل شود. در پی آن، آمریکا پیشنهاد مذاکرات محرمانه و رودررو در اربیل را مطرح کرد. با این حال، مقامات ایرانی به دلیل نگرانی‌های شدید امنیتی در مورد احتمال ترور توسط عوامل اطلاعاتی اسرائیل که در کردستان عراق فعال هستند، از پذیرش این پیشنهاد خودداری کردند.
بستر ژئوپلیتیک نشان می‌دهد که ترور علی خامنه‌ای، رهبر عالی ایران، و درگیری‌های ۴۰ روزه پس از آن، ساختار رهبری ایران را به شدت دگرگون کرد و موجب تحکیم تسلط سپاه پاسداران بر امنیت ملی و سیاست خارجی کشور شد. اگرچه از طریق این کانال ارتباطی غیررسمی، تفاهم‌نامه‌ای اولیه میان آمریکا و ایران حاصل شد، اما این توافق به سرعت از هم پاشید. تلاش‌های میانجی‌گرانه موازی از سوی پاکستان و قطر نیز کاملاً متوقف مانده است؛ چرا که به گفته مشاوران آمریکایی، مانع اصلی همچنان سیاست سرسختانه ایران در قبال تنگه [هرمز] است، نه عملکرد میانجی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70141" target="_blank">📅 16:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6YAwKtLHqG6XavDB2xdGU2IaE0P63DWPIWfZs8-wRUe-n7Urv1PwxkNbhh9wtTRRGjje1On0OpafSStyna7YshL8h1ESYqwuE0MNIAS-dUp3KEP7T1-BY8FDX714bQ9SIGpYMHxAUC0RByDcyE5QmYt0oCJBlmouiSF7k0wLHnawiFiR44xCDnxHmdhqPFin_wUFJFy2oA-nLSO8kS7p5NeLV4QVmxvfn8w1sSNwoSokS3uwn9JB6h5U0WPIRSv0C8E2kh6BbmCJjTmapLBRP0aDEkB9sGFEFMtRzP3l_s6qEaRLRfk6euQcmOr_YHAMoDB7fmhtdks2X9HGdmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کانال 14 اسرائیل:
🔴
ثانیه ها به شمارش در‌آمده‌اند:
تنها ۲۴ ساعت تا پایان مهلت اولیه ۶۰ روزه صلح/مذاکره بین ایران و آمریکا از تفاهم‌نامه ژوئن باقی مانده است.
توافق موقت متزلزل بوده است - موارد نقض، تنش‌ها، و هر دو طرف قبلاً آن را لغو یا به حالت تعلیق درآورده‌اند. هیچ تمدیدی تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70140" target="_blank">📅 16:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=BRJPMG_Tbk8iUTRukAeryf8DZYNlJQ-HajvZhLyHJ7Id64Ja6xxEjpFT_F6EKVDMCzzuZxknS4cX-kcf_5yyZYDhEmkydzBW37N736Nl04O2Z9vw1uS7_Ljj3wI7g9g-6rciq7Ip8T9E6wNRaI_nA1ToBQvtWwYGkCNzADpKxL7VrjKTvEXE3Bcfy3OL8IrCqBySC2cyo0NoSVyguvbm7oQmUU0SJn1ALyhQxeA-CYet67INYavcmIyUxgpImMeYZlXUJun99m0uiLXvrio6M0mJKPm3TPFALgmal-u-ZrN2SigG6YrlOixqKCJezbGYDtLdsT8BDe-1lq09C5fjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1685ca6213.mp4?token=BRJPMG_Tbk8iUTRukAeryf8DZYNlJQ-HajvZhLyHJ7Id64Ja6xxEjpFT_F6EKVDMCzzuZxknS4cX-kcf_5yyZYDhEmkydzBW37N736Nl04O2Z9vw1uS7_Ljj3wI7g9g-6rciq7Ip8T9E6wNRaI_nA1ToBQvtWwYGkCNzADpKxL7VrjKTvEXE3Bcfy3OL8IrCqBySC2cyo0NoSVyguvbm7oQmUU0SJn1ALyhQxeA-CYet67INYavcmIyUxgpImMeYZlXUJun99m0uiLXvrio6M0mJKPm3TPFALgmal-u-ZrN2SigG6YrlOixqKCJezbGYDtLdsT8BDe-1lq09C5fjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیف شاهنشاه آریامهر و ترامپ از خمینی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70139" target="_blank">📅 15:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=ZhJzygHyNnCCcNz3jrZj3qBRf1EySpd2RNXpCa1c0R6fB62dZWeCctGpaSjDsIN1SwJOVi5mPp0jZoQzBZhJKiaSW29Z2C1IdipRUoBazMpZmoxSOrsoV2bxFpIC1st04fT0DRGK0nwZvDtPT-rheRQiEbhHZavp_0pcWxX5dpmzsmTkv1ooF4WNJG0K-YeH5OVfOIECfpzAU8eknUWMUNllEbZyertv3PH1HeW4ggkquIstAivTSYrc8KYO4eBaKcGsJwSRhmCgFaS192we_gA31LVbKxpX_wIkWH19eUfHrSMalK9IcKSTDm38-6Rv3ThjOhdn8qMF3daNp8iyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f147bdc.mp4?token=ZhJzygHyNnCCcNz3jrZj3qBRf1EySpd2RNXpCa1c0R6fB62dZWeCctGpaSjDsIN1SwJOVi5mPp0jZoQzBZhJKiaSW29Z2C1IdipRUoBazMpZmoxSOrsoV2bxFpIC1st04fT0DRGK0nwZvDtPT-rheRQiEbhHZavp_0pcWxX5dpmzsmTkv1ooF4WNJG0K-YeH5OVfOIECfpzAU8eknUWMUNllEbZyertv3PH1HeW4ggkquIstAivTSYrc8KYO4eBaKcGsJwSRhmCgFaS192we_gA31LVbKxpX_wIkWH19eUfHrSMalK9IcKSTDm38-6Rv3ThjOhdn8qMF3daNp8iyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مایکل مترینکو و کاترین کوب، گروگان‌های سفارت آمریکا در تهران، درباره معصومه ابتکار از اعضای دانشجویان پیرو خط امام:
یک عوضی تمام‌عیار بود؛
هنگام تعارف شیرینی می‌گفت مرگ بر آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70138" target="_blank">📅 15:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arCzrcRV_6bS83KAZXHUaBHftwIPysJtQki4Jhex9Cp9SAKqrGZPczgjkraIoGezTkm55011v0kQieUkyJMRaP1b0urgdNZ9EBg8LCZRCF1FhiASkx56NpDnr48t0mtlxieJ4D_bIJvZXMUFXC9VILUGjsJ_r4GQ_K6pJOXn1lePFEpBpat3g9hg9nZmKfdJR8KK0Gpv-woeNAylKMBZU-C4AYqI_nM7HA2hx-0exWFpswxTEWr1ImM2mTUmFM99oorfBrzq7BmdaJ_J-cmR-e_zMuMuzAMlFOr_4lLWr7jEe21YnXTcELpPvSvwbXpLaUl6kYC4bSNoWnbdzIZ0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سند ازدواج کریس رونالدو و جورجینا:
در صورت جدایی و طلاق ، جورجینا ماهانه "100 هزار یورو" تا آخر عمر دریافت می‌کنه و مالکیت خونشون تو مادرید، به ارزش تقریبی "6 میلیون یورو" هم به جورجینا واگذار میشه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70137" target="_blank">📅 14:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Obvc03cHEUNElZ623XzVDc_BKTOUmw_KdB9i-0n2iYAK471fQ5plWMrAuBFUFgqP8brHGzptLWMpOWeDlqA_bypDXsPNuYShZv5-g-f7RehSY7UZ40U4lDFufVKt4tqOAC2p_VXwzBQlf-HLQu0wb-yM2tkRWo2y-voOt8IdDQCjuVDy9H_PM7kNL-UX6j_BzjPOJtNvclnni4PJoRJTPdJS9lHbv8_AfVsQkArD8WMJPnVkALZUiRJKn6NW0_OdBPLDwMKJfGtJP6kMlJBPnmqXLxbAPp4wn0mQFssXdo_o9IGvUkHTtNG3vAwyauSRzIbJpXG0ZKOz1onmAyjcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lleE8uyHAyoZS1iYVLGzcoWByDvWx7JbGFAE8eFB2PsRuWLOoQgIbRVb-HCGRgtp4Qc4lFR0BZhA2pFYJz141lZG5V6ZcYpisG19az0-faYY2hn5i65iO12T7gyfAgntNC0M8AvD2SH5aodyvBiwiJqwfKbPe0YeQ6S5NB2uKByZUA0-WZAGvRislNTprOKLkYBr_SasXk-4Bt72HIN0f819YjjdK3dO7NCIWa0gB4VKI4dxDR-m4m51J_NTzTEX4uKoAe_ZjVa_IFr-5RmjnACijxsM284WwTtTWUR4bSUQk9X1P7eHdoAClrfoo9vQevmsaCZRB_Z2RS49vC-lQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=vhmaImlYph7Zfa4O3L0WFAWjVXaKbTvXtpIZGFte0DGhmIg1Ig8GoB1rMPR5OwnbO8Q_LiyQyNBYiC49_w149tvko3t205jNuH4_WBcYPUVKs4jm-nFfxPI9VTAws1DvPDngZXFn6boB6t8fBg1lWUmkzjGnMOjIc4YcGMP-MSpilj-4cOVSKYCoaKw6Xp2M1VyTW5_3_b1q3vN-wRgKKQfH5SfHRpu_Y5-IQi0-40lSvA1Bfs88PeLkZCdOOPiawlq9rBHDZLaBsYzAaf5Ce3TqwfmEF9bbF2cLfIOqQP9C7LgCzNQPbBja5eXHHlP_a6uC8I4qbN8_A1pn8bYBvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b276eb7f.mp4?token=vhmaImlYph7Zfa4O3L0WFAWjVXaKbTvXtpIZGFte0DGhmIg1Ig8GoB1rMPR5OwnbO8Q_LiyQyNBYiC49_w149tvko3t205jNuH4_WBcYPUVKs4jm-nFfxPI9VTAws1DvPDngZXFn6boB6t8fBg1lWUmkzjGnMOjIc4YcGMP-MSpilj-4cOVSKYCoaKw6Xp2M1VyTW5_3_b1q3vN-wRgKKQfH5SfHRpu_Y5-IQi0-40lSvA1Bfs88PeLkZCdOOPiawlq9rBHDZLaBsYzAaf5Ce3TqwfmEF9bbF2cLfIOqQP9C7LgCzNQPbBja5eXHHlP_a6uC8I4qbN8_A1pn8bYBvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇳
اختراع جدید چین؛پدافند پشه‌کش:
این دستگاهِ قابل حمل، با استفاده از هوش مصنوعی پشه‌های درحال پرواز رو تشخیص میده و با لیزر نابود می‌کنه.
قدرتش هم خیلی زیاده و می‌تونه تا 30 پشه رو تو هر ثانیه بکُشه و تا 6 متر هم پوشش میده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70133" target="_blank">📅 13:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=gu-EIl9-43owfeMV5LrxnzJfpM1fs3FdNfO6Xr8UNY_GNn5-_sdkvOWVaBf7398_trvFC73QkJKbVTcoZSkdeEpKUi_c5QbVBEMzMl6uJGzFm12HR0VTaWHgOIPKOvTM7m5-ByeeGNU9wfoRpmqvcrKB6EovQYyPpOQI_t8lxA-kh8_Z68NpyahnxOTk_oII-6fcJUptB7NKigCNfcNK6dyN30x82R7dpAomYx0F9z-7UHFjAvbkEWHg7xeGae42gAxmXMSxR_BQ2k_s38Nbbb1-6TK45-4GFs84B0saHZ5JB6APiugkw4hS859cbU0a7vI62s7XOqaEDoQw2IZxdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ff4c5f43.mp4?token=gu-EIl9-43owfeMV5LrxnzJfpM1fs3FdNfO6Xr8UNY_GNn5-_sdkvOWVaBf7398_trvFC73QkJKbVTcoZSkdeEpKUi_c5QbVBEMzMl6uJGzFm12HR0VTaWHgOIPKOvTM7m5-ByeeGNU9wfoRpmqvcrKB6EovQYyPpOQI_t8lxA-kh8_Z68NpyahnxOTk_oII-6fcJUptB7NKigCNfcNK6dyN30x82R7dpAomYx0F9z-7UHFjAvbkEWHg7xeGae42gAxmXMSxR_BQ2k_s38Nbbb1-6TK45-4GFs84B0saHZ5JB6APiugkw4hS859cbU0a7vI62s7XOqaEDoQw2IZxdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
صحنه‌هایی بر فراز منطقه مسکو در روسیه، پس از حملات پهپادی اوکراین به کولدینو و دوموددوو.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70132" target="_blank">📅 13:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
چهلم بعد از ۵ ماه؟
در روزهای ۲۷، ۲۸ و ۲۹مرداد  مراسم چهلم علی خامنه‌ای برگزار خواهد شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70131" target="_blank">📅 12:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=CDyME8H6YP1JybpA0VdMcg6oEOGNQ45p8jSI3WVGc32RMGy-1zS-HZMtnwZj8yxII0MRUlZtfm-JSRuAJ-ePrW-SQqpOz2wioarvWwU0RjHdF8i3FsVLWNF2xUdEF8IxPyOMEgvCmCmp03YNyrs5lmolMB-HyRlmH5G2mWrKxYFA672wyZ1CioZn6LxhMHs6iGUq6IVgEWlwwWJ8tGM0l4GH5U9yKSvQG7oARWoPGhpgnh9jkoBbFebTG6ggN7uQkjjuyjeSqe6GUeazYObMpsmeaRyoJZh7Zw9HWca0cIPWqTvBG00R-9OTfqQz6Nz7w9sdVotbZcYNqh_gkhYyBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e871b80a60.mp4?token=CDyME8H6YP1JybpA0VdMcg6oEOGNQ45p8jSI3WVGc32RMGy-1zS-HZMtnwZj8yxII0MRUlZtfm-JSRuAJ-ePrW-SQqpOz2wioarvWwU0RjHdF8i3FsVLWNF2xUdEF8IxPyOMEgvCmCmp03YNyrs5lmolMB-HyRlmH5G2mWrKxYFA672wyZ1CioZn6LxhMHs6iGUq6IVgEWlwwWJ8tGM0l4GH5U9yKSvQG7oARWoPGhpgnh9jkoBbFebTG6ggN7uQkjjuyjeSqe6GUeazYObMpsmeaRyoJZh7Zw9HWca0cIPWqTvBG00R-9OTfqQz6Nz7w9sdVotbZcYNqh_gkhYyBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به یه خانم گفتن معیارات برای همسر آینده‌ات و مشخصات خودتو بنویس؛
نتیجه نهایی عجیب و جالب بود!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70130" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70129" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70129" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyAZN2IkFlW19GLj4v1DcKJZLeDBG4rIPzswfdkhUHnY9Tn5GaqDsWtMG5Jn6F4KHUf-93j-y80qvscIbtAm6x_M8YEqhKSpJ3Hsoj1EhdJPJ6TnG7P747j14ZzMxuPjghSXKwjnWHGllWVSWoBHOf0MhMd5fheD5xN9yUKTlXmEgFpKH5rO-OFUZPMkmkX0FzQEaXCnv2jMyNuwapM9qXtTEKZLNukT4N2OJpEImQeYwnluV_HQQ20fnA1Qe6PufjtdLQffdBRQ3LEqXsi09l_RvEsWpP5EWilguSeSFhdHv44pBhRQyoQWQ1-vaRfv__zq504stHkoZgUfVOML2g.jpg" alt="photo" loading="lazy"/></div>
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
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70128" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=swhDmo_zZV6DWv2bqo0gMD2PoGJfcWq1l0BfnyKTJNuRlBj60oq710NCRgKpImd3HQafRIOc9N--amkmWAYbMpvt-NqFnJ005rkqyL3uApDUqGzmJGzq0rTxhjpdMq7iNonN8soiXpeQjY_48CckSsv-HVsTsaOa5GPS4pKAv8-uXVVkqNyAyy697rKWS6BnYAmZh7Kzhjb6h2tGGbhL0pRumi6hWouKhigbGWcDimf-JLYhQomImc282vlO-QD7_TowdxJ7z8GiTVgENrt4npWpFC0tn9LPHobSl6YJzqQELCxhbFYLPF_l0UZZzwE2rEdhgwAVdsNHUKxB25661w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a53c7e6e.mp4?token=swhDmo_zZV6DWv2bqo0gMD2PoGJfcWq1l0BfnyKTJNuRlBj60oq710NCRgKpImd3HQafRIOc9N--amkmWAYbMpvt-NqFnJ005rkqyL3uApDUqGzmJGzq0rTxhjpdMq7iNonN8soiXpeQjY_48CckSsv-HVsTsaOa5GPS4pKAv8-uXVVkqNyAyy697rKWS6BnYAmZh7Kzhjb6h2tGGbhL0pRumi6hWouKhigbGWcDimf-JLYhQomImc282vlO-QD7_TowdxJ7z8GiTVgENrt4npWpFC0tn9LPHobSl6YJzqQELCxhbFYLPF_l0UZZzwE2rEdhgwAVdsNHUKxB25661w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
شاید براتون جالب باشه؛ کلیپ سمت چپی برای یه پسرایرانیه که بعد از سال‌ها تلاش، این حرکتو زد.
اما کلیپ سمت راستی یه نفر اومده با هوش مصنوعی همین پسره رو تبدیل به دختر کرده و گذاشته تو پیجش و حالا میلیونی بازدید گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70126" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpOhV8KuVLPd8vSpvg5d73cCQx48ht6GGvgFuNB1jTTevVprUTSzGNcWXB-TrWB_ZD-nxdlSuf-WAZxCdjfupCc8DlDmb5FVHiRgt52QnHKIVQxqUOBrUHKjiy3KnpwEpEY-m1M63ua4TmJQsENSeyGtwRNJLr50i_kFMIU_1a9IxxOVB5h1p24W9OwJ_SzzCqh4667d_1azbeF6nt6_NkI5EQFSOO3YZXRC3vPlP4Im5pQGfNYqo6K4RwQaXk8_yfltn7oCVSBEuKO2Vv-wpve8nnliODaIlw26IRBgeXFXNwu-pX1egP4WKrReisntqderkHzfX2CttBmNrl_CSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWOD9fNEzxlfwe6JCiVDRI9_WndQTMEneoGn-gaI4sr7d0ABxLWOMbqb3QxA-oppeMbNRmp_7p-S_MNtGgwJdRWl2K7CgxiXen2ifCdmts76f_h0uH4bafl2-WPQ-yq5ROACp1UU3CY7osRMcpOGl_tmhGcCvVwVxJayQuLb66c8grxwaLvDmeN5JT9h9auymF9WSEbg7a8Issw6NnfJ-aCAmZQZMqNLnu-CWmdNYKB4rJr4TmHChJO3Prb3C4SC8NlfiqI1NqCMrWz8CqnwQYmQgI2S_hHW_iIpPjXwWEt5xKnd3Jd4mHbD-Zh_WHRILhvp8thO_A8sw1QeCwvSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSY0zJhyrg4iK1GWTZ3hupGO0DhPz6zOe6F0gOxA-F3H5XXoJ013ID2-lP0KA6doWW4CGrnyMXS_sGy1uSSzBvCao99IlozyPVnkEHRxOV_f5j408r2a6fknqfnvEJa-VwzfVfAEnah5JACtNPrXsL3Cd8x0BitCki6UPrIu83udDtmau6KleUvItFdDHapGGon0Kt6JfMe-RmZr6Q43fcHnjFgykj8yY_qkSE1zTgM1Ha3kFqUEQ12eK5VdH-u8Xdm4VMmx9QBzo_YGxwQ5-vo2hWtNwWEuj2qgHsKBEIkBGXBbIrnVD77t_eNqfQL0okO6IMVifvgf8QID_Rl8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAvK3ZJZpUZh6HHnFvJ8UgUMFw9ENCE8iBhZHo_ew5tekgIqde7GqVQyd_LbCRzFw3-XfUrow2Jg1MQFQhR2_r1QMkWIWnJfb82shr3Cz6gjnDfGHj7VKHqc9OmnHtGHHTi5aE96PTyI_BTlXvYNwERdTLXwdHNjEx5kiaUH4R0i9y2zD45SjuQk828KnglugFGlh0ZJk9FsujZWlmz11rbQPggUs8gGqFGnWdc6hBmrXhyEWHpAio4lExFeeMcQf8O7MPjmb5h8Mt5iqU9Jsb5dZjjtI0il64Q4rIhbuhdBptSCnoRIE7MvJSaeZKkqind64guZ-KQbKHUKxVASeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
رامین رضاییان رفته دایرکت یه خانم دو رگه ایرانی-امریکایی به اسم «جول فرشاد» که بازیگر سریال ایفوریا هم هست و ازش درخواست نود و ...کرده.
خود بانو "جول فرشاد" هم با استوریایی که گذاشتن این موضوع رو تایید کردن:
بله میخواهم تایید کنم که این شایعات درست هستن. به زودی جزئیات این ماجرا رو با شما در میون میذارم.
اون (رامین رضاییان) جلوی دوربین گریه میکرد و از مردم ایران طلب بخشش میکرد ولی تو دایرکت از من درخواست هایی با موضوع خصوصی و نامناسب داشت.
خطاب به رامین رضاییان: میتونی منو بلاک کنی ، عکس پروفایلت رو عوض کنی  و هر روز سعی کنی اکانت هام رو هک کنی اما نمیتونی حمایت ملتی رو بدست بیاری که مدام بهش دروغ میگی و بهش پشت میکنی.
‌
‌
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70122" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=iSUguVjKIP5CxzAlRzW6NKEffR2kcyPUYsIZlnKxdLG6RDyhAXsxf_CiTdG8GrmBGR6gnGVf2n8TDvVSORe6BbP9lov5SDmrQfbzWOyRQvDKdaW09pFn-fBpZQsSfwVkBJYZa6Q1IRfJhczRWLA7WqYP2Xy8DvilIVqCBcfehpMgd-F1Mq_pW39pjZBRQ43zEuPS1xnWUBTJF4Ez5okt81i-L-AHkIf2udqqe8Bs_EaY1s15fK_BrIUK1w6uwEnoOiNbIo4l_DnUnhBa2EipIHT1A3zYNmisSLLRKwUHrXQfVPlZR199rippiymQkygNPytI3FTgTLCJYgS5vCux2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad5ddb268.mp4?token=iSUguVjKIP5CxzAlRzW6NKEffR2kcyPUYsIZlnKxdLG6RDyhAXsxf_CiTdG8GrmBGR6gnGVf2n8TDvVSORe6BbP9lov5SDmrQfbzWOyRQvDKdaW09pFn-fBpZQsSfwVkBJYZa6Q1IRfJhczRWLA7WqYP2Xy8DvilIVqCBcfehpMgd-F1Mq_pW39pjZBRQ43zEuPS1xnWUBTJF4Ez5okt81i-L-AHkIf2udqqe8Bs_EaY1s15fK_BrIUK1w6uwEnoOiNbIo4l_DnUnhBa2EipIHT1A3zYNmisSLLRKwUHrXQfVPlZR199rippiymQkygNPytI3FTgTLCJYgS5vCux2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی چندین مرکز توزیع تجارت الکترونیک در مسکو را هدف قرار دادند و طبق گزارش‌ها، انبار "وایلدبریز" در منطقه کولدینو دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70121" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=Yn3OWGayv-CUH7IyIGvNLkMnP6SN3AfPbGApIy1ZkaIsrzpltudC82Ogf8471b3WZ5AGoL5gItdq7e8hwsv-AjTWZioDLo3EH4sG2YOFq50rMrgU0XtAu9s-yriH8mWMGZPbu2n4zwhICqRwxhQ-Hv0SEdafXEZjv9AvrgWla3JnMp1hfcjullUuqYofM61iQf9xuL4ERE-Qkv6u1M_bCPS4BB-CMm4KGkRUFpeZ-ddL5MRktMwpB1-cm3KnBPXkVpo-x226DHmywvcK44EyitlwOFLCsFJSOb_BxHk4lQpaL8TB3_Vft1AQK4TV5MarWdz08IL3pisFIXiSk5DUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61d35336a.mp4?token=Yn3OWGayv-CUH7IyIGvNLkMnP6SN3AfPbGApIy1ZkaIsrzpltudC82Ogf8471b3WZ5AGoL5gItdq7e8hwsv-AjTWZioDLo3EH4sG2YOFq50rMrgU0XtAu9s-yriH8mWMGZPbu2n4zwhICqRwxhQ-Hv0SEdafXEZjv9AvrgWla3JnMp1hfcjullUuqYofM61iQf9xuL4ERE-Qkv6u1M_bCPS4BB-CMm4KGkRUFpeZ-ddL5MRktMwpB1-cm3KnBPXkVpo-x226DHmywvcK44EyitlwOFLCsFJSOb_BxHk4lQpaL8TB3_Vft1AQK4TV5MarWdz08IL3pisFIXiSk5DUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از افرادی که وظیفه نگهداری از جنازه علی خامنه‌ای رو داشت:
زمانی که محل نگهداری پیکر رهبر هنوز مشخص نبود منو بردن تو محل نگهداریش جای خلوت تاریک و تنها بود، تو اون لحظه تمام غربت تاریخ شیعه رو دیدم بعد با خودم گفتم خدایا مگه میشه رهبر یه جایی باشه که حتی یک نگهبانم نداشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70120" target="_blank">📅 10:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtMCxb4XIJQ-IXKYOkgYPeiaYyoIL3DVhDjsdRKhZ9VSc816V85m_u4pF1Yum3HivCkSFH_yWfYHfRfkwCi3OlRwMmUwTtfv2_Z3NmXXGEUs68_NbV9w8cA7iF6wGyNra6UXODts3H8YMmE-h7jslubmi8Q11mb5xkKv1j_KZDiEB6znPHGxbL0wjFmmvqG6HyE5EBVo5q55qnmTF4yJzq-AbaAdN5g9O9vc4b-D9mqtza5UWUuVFPW4OiYcF9E7me2MBOY6SfpXoanFjRLMy7r508T-ksoUfZXZov_Iu2KAybqeqPLm30sQhr-00whFzzcSIKChkAm-bBwD6cdftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسره:
۵/۵/۵ با یه دختر وارد رابطه شده و نزدیک ۱۳ روز باهم تو رابطه بودن.
بعد از اینکه کات کردن، آقا پسر یه لیست تهیه کرده و خرجایی که کرده بوده رو فاکتور کرده و فرستاده برای دختره.‌‌
اونم کل دنگش رو داده، البته جا ۱۹۰۰، دو میلیون براش زده و گفته فقط گموشو...
لیوان یکبارمصرفم حساب کردی مشتی؟ باز خوبه پول اینترنت و شارژی که مصرف کردی رو تخفیف دادی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70119" target="_blank">📅 10:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=MiVifhNUOurG0df8_SF2-s-fD9Bad3EyWRfRXxI_gfQ2RF_jEQx0wV7vjW5r50eO9IJy-MjlZJlNwQcZUvgLDdcO5eRy8OW94l4tQmCHmT3b0Mi9qoxOdFUATG6fybilQ-NFvsVhH6jfBu47T0K8WyOxyxQvu8irnGnWb3q-4MhCXv59rzJVUavkeC94fNC7SxqiuxvR7566gKnGg8-Qmsnk3AUhkQXyxXCJEZ5MrtRQEc-PR2Nx5V8E5YF1w6v-8zkjdDkCSdQ--kpLCLR3KJaOvoEUO657ufNvdy6CdhxkP3oCvefmhPg6aEcSLu_v8Xw9tJNwDxCVRIpz39O-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6731c5b6.mp4?token=MiVifhNUOurG0df8_SF2-s-fD9Bad3EyWRfRXxI_gfQ2RF_jEQx0wV7vjW5r50eO9IJy-MjlZJlNwQcZUvgLDdcO5eRy8OW94l4tQmCHmT3b0Mi9qoxOdFUATG6fybilQ-NFvsVhH6jfBu47T0K8WyOxyxQvu8irnGnWb3q-4MhCXv59rzJVUavkeC94fNC7SxqiuxvR7566gKnGg8-Qmsnk3AUhkQXyxXCJEZ5MrtRQEc-PR2Nx5V8E5YF1w6v-8zkjdDkCSdQ--kpLCLR3KJaOvoEUO657ufNvdy6CdhxkP3oCvefmhPg6aEcSLu_v8Xw9tJNwDxCVRIpz39O-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
احمد آریایی
‌
نژاد نماینده مجلس:
مهسا امینی به درک واصل شد!!
اونوقت رئیس جمهور قبلی ما اومد گفت مگه میشه یه نفر همینطوری بیوفته بمیره ؟
بخدا یه ادم عادی هم میدونه ممکنه یکی یهو بمیره اما هشت ماه برای مملکت تبعات اغتشاش داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70118" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=MvWJd2EOHwJGJ7Jhb_GyGwOevXf6oI0x35-X3zTv09PY-E6TTJa-C_IZAcjYX2Ogh7UzULO8eZI41ccrucgPL-mJLoDyM3Gku8VT3vaNpE-FRHzwFpwxuS5km6RnQ06PmTXzzq0B161UuQQuiThCn0z-k2pudzIM18kTxx-G_e5g-bkebhDLsVi4OyDMYDi0CVzYb3q05SG5WwAxKp5ODk6DkS4WcM9M0nMKa3N77z8VxL_OjIN9QL3U-kDkW6ifgz-rxS2LN9rid-C4W1g2S1j2O2TAlUD4ptASUad8DdSlEgn-QhLne_Y96URIVfQ7mm5x9tSb-lJCcrZY2gcteIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=MvWJd2EOHwJGJ7Jhb_GyGwOevXf6oI0x35-X3zTv09PY-E6TTJa-C_IZAcjYX2Ogh7UzULO8eZI41ccrucgPL-mJLoDyM3Gku8VT3vaNpE-FRHzwFpwxuS5km6RnQ06PmTXzzq0B161UuQQuiThCn0z-k2pudzIM18kTxx-G_e5g-bkebhDLsVi4OyDMYDi0CVzYb3q05SG5WwAxKp5ODk6DkS4WcM9M0nMKa3N77z8VxL_OjIN9QL3U-kDkW6ifgz-rxS2LN9rid-C4W1g2S1j2O2TAlUD4ptASUad8DdSlEgn-QhLne_Y96URIVfQ7mm5x9tSb-lJCcrZY2gcteIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسنپ لیستی منتشر کرده از حواس پرتی های مردم که وسایل خودشون داخل تاکسی ها جا گذاشتن :
261 هزار کارت بانکی
178 هزار کیف
137 هزار موبایل
یه کنسول PS5
لباس عروس
یه قابلمه قرمه سبزی
یه قفس طوطی
27 هزار ایرپاد
و پشیم ریزون ترینش : یه نوزاد شیرخوار
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70117" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70116" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70115">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=UEYVO5qfldyKiiv8DGIgu3i9YrFR4qf_imYEXu61ig3RZDTUFFoA-MjiPW6I0YKoqLTov7CW6ZseYGSmEK-JrP6TOrIdCMc4PwNhzm43mjoGKWsQFAlMhq0OmuLV5dzXW8SFjcxkfFH0S5ZQOH1xEIFE6OwDpKbs4a_x3DZ3-wud-tq2uwn_66K7wvVWCVpS8qhCXYPecydUPJzMJZ7W4W4VVFMerKk5SsPcAXXpA9RSi3s_50od2f2MDwScuCCxnVQ5tKSUv9gfFaNFlPwKEXf0dPtXe5i0iE77U71OGHYURWO-XpGHIag2JXq_IZ2rLq9PkXBKideDyXvXlkPQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=UEYVO5qfldyKiiv8DGIgu3i9YrFR4qf_imYEXu61ig3RZDTUFFoA-MjiPW6I0YKoqLTov7CW6ZseYGSmEK-JrP6TOrIdCMc4PwNhzm43mjoGKWsQFAlMhq0OmuLV5dzXW8SFjcxkfFH0S5ZQOH1xEIFE6OwDpKbs4a_x3DZ3-wud-tq2uwn_66K7wvVWCVpS8qhCXYPecydUPJzMJZ7W4W4VVFMerKk5SsPcAXXpA9RSi3s_50od2f2MDwScuCCxnVQ5tKSUv9gfFaNFlPwKEXf0dPtXe5i0iE77U71OGHYURWO-XpGHIag2JXq_IZ2rLq9PkXBKideDyXvXlkPQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70115" target="_blank">📅 01:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70114">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOgm9s180WqEy2oxuGFJVbqoOalUsY5GDF4SyMzqqN9kqtUgRA1RvQtq84xj4EI0vTqeq5wW8WIQ8e0gIuo6tZyS_n7h1ObA-Dre_WpQYKtGBLShQTaW2OW9fWFJXDdxJF4dUjWAKCfaU4VOPB7Xk28vBtuDzwLe9gXK8aIQVGl-mKFU63UY9nqwNXvqeOqzlC-ag0w6eMOY8wXCKm3Q1ncRaw3p4keLIwO1kZYL3q5ORd1YO27QKLhdbNdz0_eMrgPETQO6wzYBX1XDbBduuS2sNdZcXYxN3iRLykQ42KnUnbWvqGCIwEFpPx9671d7-zRmNWhjDSOLh13oYYzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):
در تاریخ ۱۵ اوت سفر ۱۰ روزه خود به خاورمیانه را به پایان رساند؛ سفری که شامل بازدید از شش کشور و همچنین یک ناو هواپیمابر نیروی دریایی آمریکا در حال عملیات در دریای عرب بود.
دریاسالار برد کوپر با مقامات ارشد غیرنظامی و نظامی در بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات متحده عربی دیدار کرد و با نیروهای نظامی مستقر آمریکایی وقت گذراند. بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول انجام مأموریت‌های مختلف هستند.
کوپر در جریان حضور خود در خشکی، از نیروهای دارای عملکرد ممتاز و کسانی که قرارداد خدمت خود را تمدید کرده بودند تقدیر کرد و بر مراسم انتقال فرماندهی «نیروی ضربت مشترک ترکیبی - عملیات عزم راسخ» (CJTF-OIR) نظارت داشت. در تاریخ ۱۱ اوت، طی مراسمی در مقر این نیرو در اردن، سرلشکر کوین لمبرت فرماندهی CJTF-OIR را به دریادار دوم لیام هولین واگذار کرد.
کوپر در زمان حضور در دریا، برای دومین بار در سال جاری با ملوانان و تفنگداران دریایی مستقر در ناو «یو‌اس‌اس آبراهام لینکلن» (CVN 72) دیدار کرد. او پیش‌تر در ماه فوریه به همراه استیو ویتکاف (فرستاده ویژه آمریکا برای مأموریت‌های صلح) و جرد کوشنر از این ناو هواپیمابر بازدید کرده بود.
در جریان آخرین سفر کوپر، او برای تمامی اعضای تیم ناو لینکلن سخنرانی کرد و از فداکاری و شجاعت فوق‌العاده آن‌ها تشکر نمود. او همچنین با نیروهای رده‌های پایین‌تر دیدار کرد و به افراد شایسته نشان و تقدیرنامه اعطا کرد.
کوپر گفت: «گروه ضربت ناو هواپیمابر لینکلن تیمی قدرتمند از آمریکایی‌های موفق است که با افتخاری عظیم و بجا، به دستاوردهای خود می‌بالند. تاریخ، این مأموریت را به عنوان یکی از فشرده‌ترین و تأثیرگذارترین عملیات‌های دوران مدرن ثبت خواهد کرد.»
ناو آبراهام لینکلن که پایگاه اصلی آن در سن‌دیگو قرار دارد، در ماه نوامبر برای انجام مأموریت اعزام شد و در ماه ژانویه به خاورمیانه رسید. این گروه ضربت با موفقیت هزاران پرواز رزمی را در حمایت از «عملیات خشم حماسی» (Epic Fury)، مأموریت‌های امنیت منطقه‌ای و محاصره دریایی جاری آمریکا علیه ایران انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70114" target="_blank">📅 01:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70113">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSIXugHQApWMG-fbtuoP9vYSiLERbe5J_QM7v2vCUA1YzzhEt8YKdIq5k4nZ8qpt3L4mH5dhxlwfnhzWwuuondDe6HBF7k-4iOqnYLlge6SoUzxJr1yH4rJI_qP_0qVN4rGQgczeeg0o2r0rYF1jkdFIX6BOLJk98LaQnU9cN3Cu6XG2HWA38YX18QjXSXaJcVKY0P40gFXPK2c49lHxe_xiFvSV4jLFSLNjxss4o3k1VdXfoUUmvVYmeKUDSUci4hN6p6xBSk655bFYvTrm_zcpRhoGELKMoEZVN-WkabBrWDBMOD47maln0bunAhlDkV-YoWSOLAn770V7_QpgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ با تصویری از خودش با کلاهی که شعار «ترامپ ۲۰۲۸» به سر دارد:
«ما پیروز خواهیم شد».
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70113" target="_blank">📅 01:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCpK4V34cn0y8zNNp6iEedA2u14qbKEqGZh1lUvTiyxwTLaUL2-mrInqWFijZlple9phZ-Hg5r_yY0rxFF2SY-66OskoiorgCDEatweKmUu1o84y3MakY-p7PA9qoAqZGU3J_Lmb9NOhKaiLNa6IrA3FTO0Jy-uA__fLVNtuthZ4jDDZiuhSdYurz_YbXZie5DzoM2VkekEXkKpkV7rOL_Xp-dJGgNq7Ig4gnE3PUKkce2qIdokXRNGCORVNTpn11i4ulgOYuUNnudE4kQL3A-fMR9YnXe2UyvJaUj542quUllSvYVc4-4ACs1xtTUM9PrRAKMnkquz9m4WpLnJfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=hr21bQW_J-akl7uwKkFcI3Oq4AFIg9VV3RFNppYbh8b2Hk14Sj-XzezBzNZu76lwjTflWX9RKq--H0_D3T_oQ36Q0mODQp4VhMCeLylKhxZMVtU5fyqQW30qrciKNgrIKr2Z4zDaaMlokfa_rpMiYTz4WfuDIqPPu-vYvPD5Y4QO0glsN0mJhLe4WcyKxb9BhJobiQsaxBsh-N9veCAs0z8Wd10oBv8K-SL76lg3KR6yrOuYfu5hnzSqv4NGw5gn8_QDApDs87PkymdSuTA3u0dCx3wB3Iu270-2K6TXR3IxvuA5ah4fE-INZ34Jtx_gnJBNpJiFIAD0CEItMwPWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a274391.mp4?token=hr21bQW_J-akl7uwKkFcI3Oq4AFIg9VV3RFNppYbh8b2Hk14Sj-XzezBzNZu76lwjTflWX9RKq--H0_D3T_oQ36Q0mODQp4VhMCeLylKhxZMVtU5fyqQW30qrciKNgrIKr2Z4zDaaMlokfa_rpMiYTz4WfuDIqPPu-vYvPD5Y4QO0glsN0mJhLe4WcyKxb9BhJobiQsaxBsh-N9veCAs0z8Wd10oBv8K-SL76lg3KR6yrOuYfu5hnzSqv4NGw5gn8_QDApDs87PkymdSuTA3u0dCx3wB3Iu270-2K6TXR3IxvuA5ah4fE-INZ34Jtx_gnJBNpJiFIAD0CEItMwPWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70111" target="_blank">📅 00:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
رئیس سازمان بهینه سازی:
🔴
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🔴
دومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش ۱۲۱ میلیون لیتر تولیدی روز بین خودروهای موجود تقسیم شود و هرکس بیش از سهمیه بخواهد باید بنزینش را با نرخ آزاد بخرد؛ تقریبا مشابه روشی که قرار بود در کرمان اجرا شود.
🔴
سومین طرح پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
در این روش سهمیۀ بنزین به‌جای خودروها به مردم اختصاص داده می‌شود؛ چه خودرو داشته باشند چه نداشته باشند.
روزانه حدود ۳۰ میلیون لیتر به حمل‌ونقل عمومی و تاکسی‌های آنلاین و غیرآنلاین اختصاص داشته می‌شود تا قیمت آن‌ها تغییر نکند.
تقریبا ماهی ۳۰ لیتر به هر فرد می‌رسد و امکان انتقال و خرید و فروش آن وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70110" target="_blank">📅 00:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3808337972.mp4?token=ODjQD44UigYhArwmFkqYDo0SK6voUvAutRbFTl6rh7Fwmxbbrp-x-aC5uvbCV9ODHBw4Gdx4W1gGeEkJIOMkK9CRqTYWzV2n2lfndBTQH047uemZvIrvsDueJLlOtEizv-BQ6M-zrrhF5PPYX8oF_Th2hi22WCkoP3Cm-O5H4ixxmzExYShgaRC-khCav9AYZeBhEYLUdErRtc1aYgpcrGZt3iAKDjQGbUxg4kYEIa6LDXN6IR4SOM-VUtafOVjQn4Ku-GxRZjBDmpAkaVfEuuOcILDxM5w80XtFIw30oLgRjH8I_V_Lj9SLsGuxKA3CCH1xCsFKYFXeMEQk6j0HEzL-hUIrEk6fTb5Bau68sHWTI4kPHfWM1E05giPRIb-Jw-4phwHSVKQUoSy9X0a2MJdXocvS7c-tmXXvMrQxvmFf4YZQ0zG5O6LeON98FPlt7j1hLpYKsiCPwDJIP4Fw4T24fG5nQNhpTBVV-MpPj7B1nf1OW52fHK15LQVAUnZeyJMZg5APjkDzPieoXbU0xaNGuaLKMyFlit9yXBT5glN91ZMszFAJxpHklp3fFCCXgA3ZpKw7pQ-A-RvucQIRkfqd06RC-SNMauSn91Xie_I8rqJBkHMQAYuPpx9EVeh2cTnwO8gI9TRztkn8i1wdHqWNrm7_EKgwsjXIbb9qPUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3808337972.mp4?token=ODjQD44UigYhArwmFkqYDo0SK6voUvAutRbFTl6rh7Fwmxbbrp-x-aC5uvbCV9ODHBw4Gdx4W1gGeEkJIOMkK9CRqTYWzV2n2lfndBTQH047uemZvIrvsDueJLlOtEizv-BQ6M-zrrhF5PPYX8oF_Th2hi22WCkoP3Cm-O5H4ixxmzExYShgaRC-khCav9AYZeBhEYLUdErRtc1aYgpcrGZt3iAKDjQGbUxg4kYEIa6LDXN6IR4SOM-VUtafOVjQn4Ku-GxRZjBDmpAkaVfEuuOcILDxM5w80XtFIw30oLgRjH8I_V_Lj9SLsGuxKA3CCH1xCsFKYFXeMEQk6j0HEzL-hUIrEk6fTb5Bau68sHWTI4kPHfWM1E05giPRIb-Jw-4phwHSVKQUoSy9X0a2MJdXocvS7c-tmXXvMrQxvmFf4YZQ0zG5O6LeON98FPlt7j1hLpYKsiCPwDJIP4Fw4T24fG5nQNhpTBVV-MpPj7B1nf1OW52fHK15LQVAUnZeyJMZg5APjkDzPieoXbU0xaNGuaLKMyFlit9yXBT5glN91ZMszFAJxpHklp3fFCCXgA3ZpKw7pQ-A-RvucQIRkfqd06RC-SNMauSn91Xie_I8rqJBkHMQAYuPpx9EVeh2cTnwO8gI9TRztkn8i1wdHqWNrm7_EKgwsjXIbb9qPUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
وضعیت کنکوری های امسال
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70109" target="_blank">📅 23:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
❌
طبق گزارش های غیررسمی سپاه لحظاتی قبل از سیریک به طرف تنگه هرمز چند موشک/پهباد شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70108" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmcwrnJE6RpoLQ9K_XfK3TsZYvUMygsJBNeli2FyPSOu66ZuwKFC6QcUFHi4Nfb_ankyzZgCB9RsSRPLIbyLprH-KAWyzO5Ya8nNMMAQEcddngu-lSVE0bX2CrxyugqvLnb9gYbhcKvSPg8iS5WlMHLm0I_IP-QxHCa-rQ55O2Fr2VOlW22UGZIVtebL1Q043WtErLGEihRtwGSOk1vANPetjbF3RVjbKwLNaSiNjoKWlqcpaRuxaRIoCXEXtqtXNhHm7S41QHeZo1dmEomOZx10NfXUi4hmJaxgFBj2eTDuNW0Ds7LCwa0wgjvaDWRHTp4ThuThCgRbOysf_ommNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
با وجود آن چهره‌ی غیردوستانه در این عکس خاص، عکس‌های بسیاری هم وجود دارد که در آن‌ها لبخند بر لب داریم؛ من و کیم جونگ‌اون رابطه‌ی بسیار خوبی با هم داریم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70107" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c505095a40.mp4?token=BN-OH6kA8Ww3_UBkewbedFF3vQiPp_fIrlS9Jpg40ArIaeGbUT9GEzBR6TE7MPhTHldLLx5th-T9UHDHsLUvCtt3RHa3R3jiM0XehCuOkD-7BdYDgafj58KBaTicig87KGkFcG9DSyf3hHmyuwvey0Dkrm5KRADJSc4Q5xWyv69P-2gXMfBnsRmz3F1CK2D0-oL6nzR1ofEQinudHZtamgE4qdlmKN5BbRBi5bJ_K3jslqEs36Nh7hKsS2vA3BNB7nodoceyMWEMV7T4zdrLa1tjMHQV9eij-lSJdiDbiavkemXbNBw40hEfp0r8blfgbpUPrjfORBjDBW6dVkddRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c505095a40.mp4?token=BN-OH6kA8Ww3_UBkewbedFF3vQiPp_fIrlS9Jpg40ArIaeGbUT9GEzBR6TE7MPhTHldLLx5th-T9UHDHsLUvCtt3RHa3R3jiM0XehCuOkD-7BdYDgafj58KBaTicig87KGkFcG9DSyf3hHmyuwvey0Dkrm5KRADJSc4Q5xWyv69P-2gXMfBnsRmz3F1CK2D0-oL6nzR1ofEQinudHZtamgE4qdlmKN5BbRBi5bJ_K3jslqEs36Nh7hKsS2vA3BNB7nodoceyMWEMV7T4zdrLa1tjMHQV9eij-lSJdiDbiavkemXbNBw40hEfp0r8blfgbpUPrjfORBjDBW6dVkddRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یکی از هوادارای استقلال داشت شاد و خندون از تیمش تو مصاحبه تعریف می‌کرد؛
که یهو رفیقش تصمیم گرفت این شاهکار رو پیاده کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70106" target="_blank">📅 21:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzdXBA1fdXYDNrZ6NBsfSLLO_e9b3bglmhw4_2H1BohnAPQW9Ge3qwsQIyGYl2h57KPXmJqeJn5vlcBy2rW6lebid1XMi8vpRrYjZOO9kPjK9Q-giRSUqUMNXCkpwCF7EyA95Hom53mPmWAlV8qaq-SHTmCJMMecg0I6PbTWbO_GxNEUvOslwZRWd5gCRbN5V-_4PNHrn001xUN7tlD3AHBhyjpIM8_gANLT8FnUHzRX7qcziOIDYowCnuWmuvUQl8EeJyN5bav6NHNu-IBpsz3h71cg3cJMGOr0o2immBJVC342U_Ae-kUAunHr5iUnslv7FKyEuLQFOhSYpV5ulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLbVvrVHi3e-jiDD6qRFIkb6Msp02pUwEb203mepziYjbRNtUnfoQ8o2RsDfOg-BF4FsB1Cx8rNZk9KpAUJ0Hhw-9nvdFu85vHApd6MBY6eQXo8s4BHrcgtdmh20xexmPO2sSkbzZbecm8ofuGjNDUXegnGPSPloENjSkAPXS0hjQ87-m8Pu3qnwa3dGFUdopFgHfS_aimg1d8ZDSDJR4EkDyz3NMEeh1JjDGQn9UbBOGY7p1Iwmidbt3y7gmVEJZWsYyIfUlcsnREzMhfRN6xR_ZNNyV8QxPUYrhh51ABlFWotjzlCNfQaC-VqNvmiIY6nVPKM5LYhaiRYHRxIbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxX21Z4p_W01b0bHtfqnPlMKwziqDnb34ixxr4_4QbIk4uiBdissip9ssZU0rpHwnMecpKyjmKgxnZTqxCfWgrCu4OAip5xBxMWJZSyarb_PtmN8QPWr6W0njibzmh-B0cxgZIhrSvmfGYOjf1yJ_XJScXDW_rIFzYiAU9T9Kx79_b_qHmZrX8IGPXSuY69QszMCz5IhVwPOqbTCKtdiWwtlIe5oalPXmY4AdkdVy7yxa06sBXSp_UGAAa5kbs75v8OPU8y1bQp88ZO7roy7I7efL5Fm5XiT3lKU4H86GRoyrTtma-6CWWdIMtEIQIwUwqUvorP2MHDTm7waXLr6Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست و استوری نوید محمدزاده و حمایت از فلسطین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70103" target="_blank">📅 20:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
میدل‌ایست:
به گفته منابع، ایران معتقد است که دور جدیدی از درگیری با ایالات متحده اجتناب‌ناپذیر است و تصمیم گرفته است تا به‌جای دیپلماسی، تمام تلاش خود را بر آمادگی برای نبرد متمرکز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70102" target="_blank">📅 20:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=TWg-jEqEBrCHEi6mTHA0JMcUoThvrE1UXAPnOv1TcUY_sxUkoxPU5kyhZYc4CBmAbTklpDkGEkhN0jg4Z3Kq2462hhHGeZ2t-2jfjG3phaxiTUMU39bCIuo4QVBFZNCPLNY1Q8rA5emgqxs2CmAlyDF6AjKQTm9JPZZCGs7sMSGmYEEDEIHe-ii2letA5TkTKtRGuBCV5zUz9QCvVFxRZ00fDxXnYA-6RypDXPDEUmLl700N44Z5wr2vhnkST_vxMs4HIdx12StQPN5F7WPezHlYBZLEDQvUPTzvlmHxQRMLzoBfoTcUNHV9gyYdKvZk5dlYNhYmn4OP5NSe8AdsbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39fe384fd.mp4?token=TWg-jEqEBrCHEi6mTHA0JMcUoThvrE1UXAPnOv1TcUY_sxUkoxPU5kyhZYc4CBmAbTklpDkGEkhN0jg4Z3Kq2462hhHGeZ2t-2jfjG3phaxiTUMU39bCIuo4QVBFZNCPLNY1Q8rA5emgqxs2CmAlyDF6AjKQTm9JPZZCGs7sMSGmYEEDEIHe-ii2letA5TkTKtRGuBCV5zUz9QCvVFxRZ00fDxXnYA-6RypDXPDEUmLl700N44Z5wr2vhnkST_vxMs4HIdx12StQPN5F7WPezHlYBZLEDQvUPTzvlmHxQRMLzoBfoTcUNHV9gyYdKvZk5dlYNhYmn4OP5NSe8AdsbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوتا گربه داشتن دعوا میکردن که یهو یکیشون تصمیم گرفت گرفت خارکصده بازی در بیاره و تا موتوری نزدیک شد رفت جلو موتور و باعث زمین خوردنش شد:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70101" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMyEdRj0S1jx98sJsc8rpc9B9EvFX-qQmlV6qNixWbEv3-2hlAutecRfbS_nyVtQbRks4WPoOd8H0r8CRzfo1aUvo3rTnXzUtnVg0fmYRnIAVc80_VUHAjQpCozff-ztpwbrP0bLWGdQfaFhzSnZH__r3nxSEsG8BllvHofkpU5CzkCIiVeOzX7R6WoNrmdF4bGt3RoZ6Fn4mgagXUNCnsFK0oCOOQ-JhBr1oyrp0csRT_w7MJk0QWF8RL5Ccxnr3TGjr3wbnyHdgSpKXhPKmlIYLjMyftZAetIMFs8SBwZeBblwdpIjJrH_4U43zH6JGyDzXKsTRYVTs9QJQmFpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
تصویری جدید از سردار عظمایی فرمانده نیرو دریایی سپاه که توی اتیکت اسمشو نوشتن عظمابی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70100" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=r9EJkUIAEl6OCCuIDut87UOnVcE2VgFZCxicE6rvAUq2isZZeZZSbP8Np2FbmgNa1-krKJKlkbclpn_yQcY_DqOnnQFcnesnIyHcDGzf3lD8o3P3kGd4L_vBT2vIc1m7ilFaxNlLYz6Uy4rLQ0CkBgHaTVoUnupW1olRRt3LBCVrzkPjXzz99-hk5v9PMY6LKc7rTk6l4AUq9Yw-ZDIm_P12-mxfVoqM63e560BiGE1LqDquYJbfiLmOwPv3tsUmi4CNI6THg9f9xrezS6LN2pG4Way7C7oFPAk8bJj5PUsdp3_aNNmwvDvNQbPiGTRNQOpWSSkSZ7wokHraDlpBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e3b71c01.mp4?token=r9EJkUIAEl6OCCuIDut87UOnVcE2VgFZCxicE6rvAUq2isZZeZZSbP8Np2FbmgNa1-krKJKlkbclpn_yQcY_DqOnnQFcnesnIyHcDGzf3lD8o3P3kGd4L_vBT2vIc1m7ilFaxNlLYz6Uy4rLQ0CkBgHaTVoUnupW1olRRt3LBCVrzkPjXzz99-hk5v9PMY6LKc7rTk6l4AUq9Yw-ZDIm_P12-mxfVoqM63e560BiGE1LqDquYJbfiLmOwPv3tsUmi4CNI6THg9f9xrezS6LN2pG4Way7C7oFPAk8bJj5PUsdp3_aNNmwvDvNQbPiGTRNQOpWSSkSZ7wokHraDlpBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کص‌مغز بازی واسه ویو یا پیک‌نیکی بودنِ خایه؟ مسئله این است
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70099" target="_blank">📅 18:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5505f54825.mp4?token=QtUb1p4iWVizVmLsoyY38lViqpXpoLAxpXEanPw-hLBFXcTp3bN96VAFSPmyYhMqvn0yo6-wQZ5Uc4XPaYvqUSrZW8LndzhoNfnZq_XseJX03iWdNJttKWphMUjCApj4LdiHNxjiyrRVXBdiH6Fe5eAbzaEfxeWEDuzWqfb3oeXPsK9Ou3s81ncBQYEbzbyDjRsTQ2M5j7u-Y-tgIu-FQc_Qqj1wkymxqMiVEMVci9R-VV5H_4tC4ncnvNNzFX_nFRA9Dn1s6biVR2Ip81Rsye_lxh8ICNQ7lZZfadmQh5uIFyMPr8GlbFGEziV7v-mitgz3IeYqnNV0MbqrQoxYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5505f54825.mp4?token=QtUb1p4iWVizVmLsoyY38lViqpXpoLAxpXEanPw-hLBFXcTp3bN96VAFSPmyYhMqvn0yo6-wQZ5Uc4XPaYvqUSrZW8LndzhoNfnZq_XseJX03iWdNJttKWphMUjCApj4LdiHNxjiyrRVXBdiH6Fe5eAbzaEfxeWEDuzWqfb3oeXPsK9Ou3s81ncBQYEbzbyDjRsTQ2M5j7u-Y-tgIu-FQc_Qqj1wkymxqMiVEMVci9R-VV5H_4tC4ncnvNNzFX_nFRA9Dn1s6biVR2Ip81Rsye_lxh8ICNQ7lZZfadmQh5uIFyMPr8GlbFGEziV7v-mitgz3IeYqnNV0MbqrQoxYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بعد از این صحبتای پزشکیان موجی از انتقادها از طرف تندرو ها به سمتش در حال روانه شدن هست.
دلیلشم اینه، میگن چرا مسعود داره اطلاعات محرمانه کشور رو لو میده، باید باهاش برخورد قضایی بشه و...
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70098" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70097" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjruQvT_Kwl6JB4rkvp8hGPzJN4sn_5-o_MYnqGmlLJQx8aawAp9wsjM0gYPMioHsbmSy9zSpEfxHwzBOEZs1eIf05KyeY615D2w3GJ-rW9U6Ywb25HZ0oIuWqPm3LxgWg_TYIemdrqx8acG2hEaff6lPLTaJE91KveifsthPYR4NhiGb_kVg9cTsuVGD7dkKs8lSU6vmgJ2uYKHlS3LXBIPcPwajbG55BYMp3RxUqyaz0ESWDj9lyY5vsrwQew6FMOV3fWN3ZEt-_eHAE5TZHuiA_m5nn07eIiS9Bfslg5N5onHND7JZRHI9hr69PICclB4r0DlyTjY2RsiKKWttA.jpg" alt="photo" loading="lazy"/></div>
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
g24
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70096" target="_blank">📅 18:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2573e39307.mp4?token=YX6neWbg1SHCz9ab6yvq_RQrfeE7Lj4XOXRe30mqrBm1EFKxL8ZuZAWzPYY7uPF_4paRuVLvYLoI7eIwX8G02B-QjWc7j6Il7h2Z7VJCXMe3akjQQQbX09GKgN22AyEk6EJdHPoHCLSmGOUiW8sUc0jD6JEOS3wU7sTE8L18sXSX48oq0XC1cTam0jyRrgTnaI3lUsPT0bzamBLFGKm056J8_s4U9ZIwTgc6kYdYHHVnECyq2zG0FXPJvvSPxvEKJBbFRWBMEiWM72QQzwOCrhSP-V4vWdKK2snMCYyfXvIb_thEiYyOadrfS9onuoyRVpq21jNIbuKujO1_ilekgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2573e39307.mp4?token=YX6neWbg1SHCz9ab6yvq_RQrfeE7Lj4XOXRe30mqrBm1EFKxL8ZuZAWzPYY7uPF_4paRuVLvYLoI7eIwX8G02B-QjWc7j6Il7h2Z7VJCXMe3akjQQQbX09GKgN22AyEk6EJdHPoHCLSmGOUiW8sUc0jD6JEOS3wU7sTE8L18sXSX48oq0XC1cTam0jyRrgTnaI3lUsPT0bzamBLFGKm056J8_s4U9ZIwTgc6kYdYHHVnECyq2zG0FXPJvvSPxvEKJBbFRWBMEiWM72QQzwOCrhSP-V4vWdKK2snMCYyfXvIb_thEiYyOadrfS9onuoyRVpq21jNIbuKujO1_ilekgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش چند تا جوون مست کرده بودن و توی ویلا همچین کاری رو کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70095" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=iHW_klXt_cOWF5KZCtL5r6GOWXj_Ez_3vU6PUKhMTEE4vdLXQd16CgGkNhTv3pSjmDFb-yu_M5EBoM6P7AxvtpdYCnSNVMWjX1UFPLQvJv4tAWIl60fcp-SKT5avOS0UCOPTxBxq9ZJ0ZO4i95c1IMhyOrVIaJiMzZ2UqX7H9rxci0nt-PtgnX7rQ2y7GRx0TG8X5-RqOK8z1lnvykj_nMCXdg8MuZZ9JB5SdqySxM_gomO-Q9ODCyrDYDOYR-LpGgterqHTdnEVLz0QgXfPChQHyST6KgNCk3EJJEO1Ysi9_AI8mRM4O8AGaWGvgppstPFxtGu3fwA1x1m6H1KCGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532b4ed793.mp4?token=iHW_klXt_cOWF5KZCtL5r6GOWXj_Ez_3vU6PUKhMTEE4vdLXQd16CgGkNhTv3pSjmDFb-yu_M5EBoM6P7AxvtpdYCnSNVMWjX1UFPLQvJv4tAWIl60fcp-SKT5avOS0UCOPTxBxq9ZJ0ZO4i95c1IMhyOrVIaJiMzZ2UqX7H9rxci0nt-PtgnX7rQ2y7GRx0TG8X5-RqOK8z1lnvykj_nMCXdg8MuZZ9JB5SdqySxM_gomO-Q9ODCyrDYDOYR-LpGgterqHTdnEVLz0QgXfPChQHyST6KgNCk3EJJEO1Ysi9_AI8mRM4O8AGaWGvgppstPFxtGu3fwA1x1m6H1KCGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صداوسیما: پنج هزار قبر برای آمریکایی‌ها در اطراف تهران آماده کردیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70094" target="_blank">📅 17:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc6yvL01yaeUTX1QgnOWXK-iQz7iESog5OrR-UuSTrNcNaTpYFLKaqjOjlIACRb2Y0g6BQaCsYkqUcSECGaNvePl4KYsxSqjmBior4DJdIiUjqo2kCpZUu_YXf2GfTQAyhuh1LaKobmJSw68L9WN-5eQVFJEHi-4eIGDcy34QGxcRb91rM7jiU98DuDWbpxofyAkG6bP6ZPMhPL3swk3aDG1Zat52p18zkgchLl_sss7chTgezc0vAUk76VkwEsgB1g6xf_YtW-jc8hkBA4imQFbqrKmB8t_hm52pOjTfyF7br1WGI9OpJOEWBlqHE7t0K70AiytFa0lofSEmGdGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
🇺🇸
کراسنشتاین خبرنگار آمریکایی:
دلیل استعفای لیویت این بود که فهمید ترامپ اونو به عنوان طعمه مرگ توی هواپیمای اصلی سوار نکرده و با خودش نبرده(ماجرای هواپیمای ترکیه)
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70093" target="_blank">📅 16:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIOzdvmDQQ4V443mfGElOPNT477f6-8q-RTJShLjSNGl07jy_DBkHea96IUuRYQL9FJ1Xei1Hsk4dzLDJ0WXPRamY4Jv4LFoFEXbv5ZQkk-iuBapJ_qhpH1tViqdsNw1S4g0-lzlRuDZm1bTj6kZzZpvKeke2vINcneoA_EFMryA_gS4co2Ims56lhG-NRbFWKtadimAlwNVYo0xYPzMqDmSsV4IQYUKIrEScOM1PNP4w-idqaioxqzeRSeYS9jNla7_jfq6J_ONsXMyF40qcwMPdXeCL1QcxzX7TzYQa-1PgqOfhw4nbfpQKyGfV6Tu74-D37xMk5qk4N0ZSpHtuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70092" target="_blank">📅 16:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6444186749.mp4?token=PoaDnzPDF90-ZozB9JTZQnE57ME-DMBeC5GZGqkoBr4Sz7xJ2fdePElwRW0hZManrCreoqLCreYw1rwh6ocEeW5x9m9SVYYECQMz5SxEgKt1nMlFJCgRJ_5sZ0LYG7laCRO6Lv3KQVZhsr7zMVC_vO5cxuf_-ED8OyhweRZBK_c3cUoSLqCjR-1bZlIn7FQ1MD-Yhae25xjVIyjDLLNLSYN1u308BXI8loV9N1AkP7BpsvizqtYYgLGpxTkzNytrnpdgfCtxuNVKnA0QwxEikzSTqPyjgoY80Ulvy_AOLIs3zc682x4hhyjwAeZTdRQ9WowvMmBWWSiXAsk0XUlGcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6444186749.mp4?token=PoaDnzPDF90-ZozB9JTZQnE57ME-DMBeC5GZGqkoBr4Sz7xJ2fdePElwRW0hZManrCreoqLCreYw1rwh6ocEeW5x9m9SVYYECQMz5SxEgKt1nMlFJCgRJ_5sZ0LYG7laCRO6Lv3KQVZhsr7zMVC_vO5cxuf_-ED8OyhweRZBK_c3cUoSLqCjR-1bZlIn7FQ1MD-Yhae25xjVIyjDLLNLSYN1u308BXI8loV9N1AkP7BpsvizqtYYgLGpxTkzNytrnpdgfCtxuNVKnA0QwxEikzSTqPyjgoY80Ulvy_AOLIs3zc682x4hhyjwAeZTdRQ9WowvMmBWWSiXAsk0XUlGcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
رسانه های اسرائیلی با انتشار این فیلم‌ نوشتن:
خیلیا فکر میکنن پرواز جنگنده‌های اسرائیلی بر فراز ایران خیلی سخت و طولانی و پرتنشه ولی کاملا برعکسه و زمان زیادیش شبیه پرواز هواپیماهای مسافربریه.
چون مراکز اطلاعاتی اسرائیل همواره مختصات پدافندها رو به اطلاع خلبانا میرسونن.
فیلمی از پرواز جنگنده های اسرائیل بر فراز آسمان تهران در زمان جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70091" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7ik95tsEydD9pXfpS-BzFMoaJr1uPfcKZI9Ynqms18-YQxf4O-5KSwW_39O-vIk_CQYsZqeg-J2fg-Kath0-ECJrvAEpCntGf8AiyiFZCcYza1qB6D5wUy3mfoC3MpPozLGwbL1CMy3w_dOgLH-EwDeQFN4AOIhc5fFYJHcBR1YHa_nuzCeRTqJN5T_8jLtlRahlu7jW-1kM62rGrQVfYrOGprniTg0hb9Oht8-GSctsbs5ntonh8iHzKbVHtcgGhsqfH7_ibsREBnNXmkCFp5roxB5q3ISAlfpsThysnbsoKEMuEseMmbX9GkBM5R1GjKhWwnPp9z0aLDN_vjJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار باقرزاده: سه خلبان ایرانی توسط قطر به اسارت درآمده‌اند؛
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح: ۳ خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند.
«جواد صالحی»، «عبدالمجید دشتیان» و «عمران به‌روشیان» از ۶ ماه پیش در اسارت نیروهای قطری هستند و دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این افراد با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
طبق کنوانسیون سوم ژنو، صلیب سرخ جهانی باید هرچه سریع‌تر با خلبانان ایرانی در قطر دیدار و درباره وضعیت سلامت آنان تحقیق کند و شرایط آزادی آن‌ها را فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70090" target="_blank">📅 15:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=Rz3fMiFEgA58qP3KsQ-c2wDpZyfEMoR7BvN3sJTa6cgG4gLGBINbiImTc-QB_cW9ZXzC8qDjefbVLQ2Ra3eSx3cdHYNzy0Sv_qUgm23FDPAdkQTJHLEivGcxiurp84wNwX9YS0wW4JOPrymmVesSIcUhmo9S1_H1BL2JivQuRvNJBnQg7V8zyWMromb08G71sDFLUXFHTwDPOo0gnuz0N-MF-HrJlQwYoPI2ChCuluH4el9bdWoa__TMz4EH4wpMwbYndc0T8liL22PGr3I7TM9mWPlHq_k6hyAli_hnMekpHFSyp1WvCP6ZdESpYnwsJ4lAely6jL_ntK-Ebvws2C07E_knhgSuaUHaKChr9hEkqGVhU1iMXBFqbrBOJ92Yd1STf--3FdwPSo5oOO09li388pZYNu2KBYSyG2zeGdMJLe2dXzWL63WB0a3t742E8IcZN4Rf2NnUz8rcpxOotBxHIido33mvW7ecXftKTbdDH0drQpHduefzyqfm9ukE-lsor0UjKXsITDrfocYYF_KkM_KSQGZ5VSBHVWqbVVgDqwL2y8J20EbtXmuLPxeuSmo29sfblmUE5KDEyswVmfIk1M6_WjY9vWdkOkElCofMM08lrOm6NrnJjJ-0O4UHH30Ao_S4sQa2yj8aK_PCilkKJRySCPGpeQOQB_sHB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a18fbcabf.mp4?token=Rz3fMiFEgA58qP3KsQ-c2wDpZyfEMoR7BvN3sJTa6cgG4gLGBINbiImTc-QB_cW9ZXzC8qDjefbVLQ2Ra3eSx3cdHYNzy0Sv_qUgm23FDPAdkQTJHLEivGcxiurp84wNwX9YS0wW4JOPrymmVesSIcUhmo9S1_H1BL2JivQuRvNJBnQg7V8zyWMromb08G71sDFLUXFHTwDPOo0gnuz0N-MF-HrJlQwYoPI2ChCuluH4el9bdWoa__TMz4EH4wpMwbYndc0T8liL22PGr3I7TM9mWPlHq_k6hyAli_hnMekpHFSyp1WvCP6ZdESpYnwsJ4lAely6jL_ntK-Ebvws2C07E_knhgSuaUHaKChr9hEkqGVhU1iMXBFqbrBOJ92Yd1STf--3FdwPSo5oOO09li388pZYNu2KBYSyG2zeGdMJLe2dXzWL63WB0a3t742E8IcZN4Rf2NnUz8rcpxOotBxHIido33mvW7ecXftKTbdDH0drQpHduefzyqfm9ukE-lsor0UjKXsITDrfocYYF_KkM_KSQGZ5VSBHVWqbVVgDqwL2y8J20EbtXmuLPxeuSmo29sfblmUE5KDEyswVmfIk1M6_WjY9vWdkOkElCofMM08lrOm6NrnJjJ-0O4UHH30Ao_S4sQa2yj8aK_PCilkKJRySCPGpeQOQB_sHB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اجرای یه پسربچه ۱۲ ساله ایرانی از آهنگ ترکی «NAPIYOSUN MESELA» حسابی وایرال شد!
اجرای این پسربچه تو رسانه‌های خارجی، مخصوصاً ترکیه، کلی سر و صدا کرده و خیلی‌ها معتقدن حتی از نسخه اصلی آهنگ هم بهتر خونده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70088" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhrQ8GpBU-gAoizJhQJfowj2_fo5f8JMnBcXhOkLu8IrEVym3xOA9C1FnRaie_YRvmTmByd3ittAJEhnZ0FIa0CHTlIGcZZi39h2geGPKGmhCbUK0PCDLiMu4FWl3GK7bWMNnqFv3l4f-naSo_i6-ElP1IITU1pB9epIQOaqLt4vPMilFzWww1KV3QMhrIOo2PCpXag27u1KaUMrdp1MYuUNvhfja39bQrtsJCPD5MsYxx_iEsnlYl6PW3DkbgS6LAc9Gb2yYnQYC7r2R0vFjAs3crx7n9qbYXUN8vLwwJKAYLZfEVp5UEfPt8kIhXlZN5B2oUf8lxG4LFpIbjnT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596d386743.mp4?token=EMSuEszDaF3tk06YdTzZkAhB9qFtrKzsYimTB3wRJLT7HvlSQMfZKe1Q2ByyDQm0mjn8OO3W1SCpuynI12Vz7uzr1nvciwvfSyPl-SoQFvKd-I3vwEyj-zemUEQiqpHVUiCrE_Fw5JPYhDmx158P1275Chd3KyOj7j_6O-_w5Moz2-xXbCPygN7M8XqdzGoqn9XQ99QcQv3E-AOzAdIgN6F1FWlod0y4p3a6Xfk4yqPtvpaAEg63y2Qr1bH9FKzzTzGY8OO7CpW_9jQsuZuE0ddx0RM3CUfF4ewplqLF5b0Octl6Csz37_bwvlMeMNW60vTAN1UWTkGaGY5ryPNMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596d386743.mp4?token=EMSuEszDaF3tk06YdTzZkAhB9qFtrKzsYimTB3wRJLT7HvlSQMfZKe1Q2ByyDQm0mjn8OO3W1SCpuynI12Vz7uzr1nvciwvfSyPl-SoQFvKd-I3vwEyj-zemUEQiqpHVUiCrE_Fw5JPYhDmx158P1275Chd3KyOj7j_6O-_w5Moz2-xXbCPygN7M8XqdzGoqn9XQ99QcQv3E-AOzAdIgN6F1FWlod0y4p3a6Xfk4yqPtvpaAEg63y2Qr1bH9FKzzTzGY8OO7CpW_9jQsuZuE0ddx0RM3CUfF4ewplqLF5b0Octl6Csz37_bwvlMeMNW60vTAN1UWTkGaGY5ryPNMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70084" target="_blank">📅 14:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=LtCJjwJ66h_sZr80q8WdHU8wIbNSZzZf3PdTXX-azHlHDYTZ_cn8QoA3VBZhQZZllTVMpi3TVIYeu3yk9VhGv24Ko6F3gShcBChNr02xrPWpIP3LwEyGMSzqYu6cyMpK3iZ8_ap5glokLdKzWRXTFIGSRaAtSDAbWrQRqojVmmd1bneFLVmSlclQ1h2n2B2NN0tVg0LV9kTtdKlgb1rCetxV6rS3g4Epp9QvdYXKPOQF7yPYYUQ6Olxeu_ZjP5A-ZhJ19QBjif5AmdE2UGYURdmeQIUSDDJZ-xI5cdpTsscc1ClXk4a9WGPgG0h4x2gvvB8Zw0H8xCBGsQuySWMZrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fbd8e1f85.mp4?token=LtCJjwJ66h_sZr80q8WdHU8wIbNSZzZf3PdTXX-azHlHDYTZ_cn8QoA3VBZhQZZllTVMpi3TVIYeu3yk9VhGv24Ko6F3gShcBChNr02xrPWpIP3LwEyGMSzqYu6cyMpK3iZ8_ap5glokLdKzWRXTFIGSRaAtSDAbWrQRqojVmmd1bneFLVmSlclQ1h2n2B2NN0tVg0LV9kTtdKlgb1rCetxV6rS3g4Epp9QvdYXKPOQF7yPYYUQ6Olxeu_ZjP5A-ZhJ19QBjif5AmdE2UGYURdmeQIUSDDJZ-xI5cdpTsscc1ClXk4a9WGPgG0h4x2gvvB8Zw0H8xCBGsQuySWMZrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مم‌باقر قالیباف:
همون روز که به ضاحیه بیروت حمله شد همه چی لغو شد حتی مذاکرات
گفتم امشب اینطوری اینطوری اینطوری رژیم صهیونیستی رو خواهیم زد
اگه اونا جواب حمله مون رو بدن کل منطقه رو آتیش میکشیم
ترامپ اومد سریعا توییت زد محاصره لغو شد چرا چون ترسیده بود ولی دیدم زیرش نوشته تنگه هرمز باید باز بشه
به میانجی ها گفتم چنین چیزی نداریم‌اگه ترامپ این توییت رو پس نگیره دستور شلیک موشک ها رو میدم
درست بعد ۵۸ دقیقه ترامپ توییت رو ویرایش زد گفت تنگه طبق تفاهم نامه باز میشه نه بی قید و شرط
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70083" target="_blank">📅 13:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98817f7767.mp4?token=jdxwih8QOc0osyJOuzzFTTf4Q_w4LIoaJxc-Stw0yCeo8iSqZ450KXQkAGx2BaU9ne2eWmG61fZLYIvMYVJJDb7jUG3WRW-RPRq3QHUrfXbrni4s9rlyKsm2UgwbCBdAdFM-opULE3mOznSiLFXFLy1br9C1eDOejxbgWvJB2mwTEv7-z4v-uPcWMvs6RR9_DKLI4HngOkMVj35QIfF9qEV2gRUsnN-AVQ6czMQ3dQ3Gp-yDiTL6Twp5UwM8kV58ZLAOwBcwuDV38NORIU_gDjpeT7WoK9izHc-OUZS-EGSOXCdMXMSYbDXvg9h22zAjGfk51Mb9A3y6yM2if7bdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98817f7767.mp4?token=jdxwih8QOc0osyJOuzzFTTf4Q_w4LIoaJxc-Stw0yCeo8iSqZ450KXQkAGx2BaU9ne2eWmG61fZLYIvMYVJJDb7jUG3WRW-RPRq3QHUrfXbrni4s9rlyKsm2UgwbCBdAdFM-opULE3mOznSiLFXFLy1br9C1eDOejxbgWvJB2mwTEv7-z4v-uPcWMvs6RR9_DKLI4HngOkMVj35QIfF9qEV2gRUsnN-AVQ6czMQ3dQ3Gp-yDiTL6Twp5UwM8kV58ZLAOwBcwuDV38NORIU_gDjpeT7WoK9izHc-OUZS-EGSOXCdMXMSYbDXvg9h22zAjGfk51Mb9A3y6yM2if7bdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزرائیل این روزا تبدیل به کراش دخترا شده!
یه انیمه ساختن، عزرائیل میاد جون یه دختر کوچولو رو بگیره، اما تصمیم میگیره ببره پیش خودش و بزرگش کنه.
همه جوره ازش مراقبت میکنه، مثل یه ملکه بزرگش میکنه و میفرسته مدرسه و...
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70081" target="_blank">📅 13:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=jl_Byxz2hmOWVlALSo6EEe8WYyYfxBdWD3OcCy5htbgphD9pxhxk7eOxjKQGBq0hKwuI7bG7IGC6S_S_ml09tntCGnfRyXWPf4e1lmyOdppOiPTZK2VanyPG2D-Fs8LqgU8ewYCWycYVPI3KXR4rYT9hCX7dEY3AtYBYj_CIljaGMSNmLuGIGQD1hedFrlHStBn6goa_6JPdpbT2QbCXik1G-OJ6dQLxNlD9TzN7wiSTXnZShvUt503nyDPDMTG3JhhSJYLvEtGaCIAPextPr1qwWWfOv66rWSb2oKvpS5v6RSnDMRfKbkUtCx9-PgSZo4fp0O5nWUJAUzsixIXxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1ed49791.mp4?token=jl_Byxz2hmOWVlALSo6EEe8WYyYfxBdWD3OcCy5htbgphD9pxhxk7eOxjKQGBq0hKwuI7bG7IGC6S_S_ml09tntCGnfRyXWPf4e1lmyOdppOiPTZK2VanyPG2D-Fs8LqgU8ewYCWycYVPI3KXR4rYT9hCX7dEY3AtYBYj_CIljaGMSNmLuGIGQD1hedFrlHStBn6goa_6JPdpbT2QbCXik1G-OJ6dQLxNlD9TzN7wiSTXnZShvUt503nyDPDMTG3JhhSJYLvEtGaCIAPextPr1qwWWfOv66rWSb2oKvpS5v6RSnDMRfKbkUtCx9-PgSZo4fp0O5nWUJAUzsixIXxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
با همه وجودم می‌گویم که برای من هیچ فرقی بین امام شهید و رهبر معظم انقلاب نیست؛ حکم، حکم ولایت و رهبری است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70080" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqcS4t2-jJqMpYKMv-QR2AgCBGgzogoQuoTojmK3xiyPbbjNsvOdQ-4tn-I7T4KrX-udn8X56SuFdBSVHhuSEDHGkzjjQ_wSNBrfuhucGMej_tLueTq2PgYgX6S8ZypSzDnsU6SJ4UHLwd5SwNkKHbJ9D1_hWb-RPWs_vMcCk06pS4As3mkx9CwFexWBVGUcBwDDQEVzCGb7NGU6cRE92FykybMUshTG08ng4_v0MQ6emDpU9rtCtLmYHE4B25DtZwwFv2URnV-qIcysApt-oNW_J6-JjQ8X6ijIRnY3EjhHr3dEkGC0U10v-ov3x8Hi4BIyBhmh_wngeYH0fIDQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzzURinBG5FR2ibmKz26dUCgUaUT1Q_XL358sYLOfR4rzBRDrQ9E3EAMeSgst1_I9vIMjGyjdZM4guLjDvmz69GdduguAqu46tmDbzzbBwA5DFX7j62YNZ4aFYOuXZY0MSZuR7tMMMzdzYdp8KOhff6eA0r1iGjRtVSPqY68bJ8j5wBVtk3yRuSakfwbf_V7ZYZE6rcWGRcljytlab7zmazKzMPjUYmmfvwNADmIIEK_RkpJgyOn7m8HH_tPj3L9vcTkrdwSlr6o4WtxbnT1hiH9rexU9NqF1tq7io1LSxKF9Y9WxhzsVlBGHZ5hsHtWNhwMtA2O0Vpau2K5b5FMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tl69qgBFnEt2v9MNL9wOuCmnycftowg3rfWA5s9hFynvyxvPjeeTkyPUf41n92pUG5ZjTTZWb6HwSRvrTPPvTj_OR4WmEtbkRQ9Irm5cTqHekn0rEjjFaX4ujFPRYh7dxorFHoaebMwRGEpnjNxnyyCckoaraaFBz2yPAlkXgeitNfDRPKkx6uNi_6nYD0-tECf5XS-lcmz2Qtm4Fmj1N7c5nsLrxxzsLCzbRqwTtOjFx3vGQNOVZfGkyM_azhTRNfLuNzTPtIFkx29uP0lz6k9F7S2Wwu3RNkzqD7Si7cpgePqlCODo417SmBq2wiHoO-fugs9P0RG2KyZOHeKkYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
〰️
❌
ناو هواپیمابر USS George Washington (CVN-73)
یو‌اس‌اس جورج واشنگتن یکی از ناوهای هواپیمابر هسته‌ای کلاس Nimitz نیروی دریایی آمریکا است و ششمین ناو این کلاس محسوب می‌شود. این ناو به نام اولین رئیس‌جمهور آمریکا، جورج واشنگتن، نام‌گذاری شده است.
🔴
مشخصات اصلی؛
کلاس: نیمیتز (Nimitz-class)
شماره بدنه: CVN-73
ورود به خدمت: ۴ ژوئیه ۱۹۹۲ �
طول: حدود ۳۳۳ متر
وزن جابه‌جایی: حدود ۱۰۰ هزار تن
پیشرانه: ۲ رآکتور هسته‌ای
سرعت: بیش از ۳۰ گره دریایی (حدود ۵۵ کیلومتر بر ساعت)
خدمه: حدود ۵۰۰۰ تا ۶۰۰۰ نفر
توان حمل هواگرد: معمولاً حدود ۷۰ تا ۹۰ هواپیما و بالگرد (بسته به مأموریت)
این ناو در عمل یک پایگاه هوایی متحرک روی دریا است؛ یعنی می‌تواند هزاران کیلومتر دور از خاک آمریکا، عملیات هوایی انجام دهد.
🔴
جنگنده‌ها و هواگردهای روی ناو
هواگردهای جورج واشنگتن توسط یک بال هوایی ناو (Carrier Air Wing) اداره می‌شوند. در سال‌های مختلف ترکیب این بال تغییر کرده است؛
جنگنده‌های ضربتی
1) F/A-18E/F Super Hornet
جنگنده اصلی تهاجمی ناو
توانایی حمل موشک‌های هوا‌به‌هوا و هوا‌به‌سطح
سرعت بالا و مناسب نبرد دریایی
اسکادران‌های معروفی که با جورج واشنگتن پرواز کرده‌اند:
VFA-102 "Diamondbacks"
VFA-27 "Royal Maces"
VFA-195 "Dambusters"
VFA-115 "Eagles"
2) F-35C Lightning II
در سال‌های اخیر، بال هوایی مرتبط با جورج واشنگتن به سمت استفاده از جنگنده نسل پنجم F-35C حرکت کرده است.
نیروی دریایی
ویژگی‌ها:
رادارگریزی
سنسورهای پیشرفته
توان حمله دقیق
3) EA-18G Growler
هواپیمای جنگ الکترونیک:
ایجاد اختلال در رادار دشمن
پشتیبانی از حملات هوایی
اسکادران:
VAQ-141 "Shadowhawks"
4) E-2D Hawkeye
هواپیمای هشدار زودهنگام:
دارای رادار بزرگ روی بدنه
کشف هواپیماها و موشک‌های دشمن از فاصله زیاد
اسکادران:
VAW-115 "Liberty Bells" (در دوره‌های مرتبط با CVW-5)
5) بالگردها
برای عملیات‌هایی مثل:
ضدزیردریایی
نجات خلبان
حمل تجهیزات
مدل‌ها:
MH-60R Seahawk
MH-60S Seahawk
اسکادران‌ها:
HSM-77
HSC-12
اسکادران‌های نمونه بال هوایی CVW-5 روی جورج واشنگتن
(ترکیب ممکن است با توجه به دوره زمانی تغییر کند)
VFA-102 — F/A-18F Super Hornet
VFA-115 — F/A-18E Super Hornet
VFA-27 — F/A-18E/F
VFA-195 — F/A-18E/F
VAQ-141 — EA-18G Growler
VAW-115 — E-2D Hawkeye
HSM-77 — MH-60R Seahawk
HSC-12 — MH-60S Seahawk
🔴
دو رآکتور هسته‌ای؛ بدون نیاز به سوخت‌گیری معمولی برای سال‌های طولانی
.
⚠️
این ناو به احتمال قوی جایگزین ناو (CVN-72)USS Abraham Lincolnخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70077" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdQbDIMk10SjLRQslmgWSj8P63HN92KsHMTu3elrjre-wDKokJG6t33Csu66d9ImPui6hY2lAdpx5QUhf1uHbJBw_U3llR6rNIA2mekc9VXFXt4FdwcIC1k4HVd3KVi4yXwUpQIQMD5cN7vq1WR33tP9iMTHii8uwfANppdGKj_WZoIYuZx56vvHyyJuH8I5pnvi62-MQ44_EMSRLz5OSUzzPEGl3-IsormAJm9VGGPOHU8EmBTZNQ1PmCnNX4OrMXeBnaJhDKG7LgDBWmnV_rR0vKiozWYl6R9SHCY6Oyf2ywz19eujVSemjO-Vcsf9FPjxSoJ-OPe7khYuDzu7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70076" target="_blank">📅 11:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDBGR7A21eIwwKSXDfHX2Wl2tvJDjmcGx36x4AEDJza_W8Hu1uRDHo9gBKfPqHaSdvvCp2kctfb2HtsbEQf0L2qX3XNGyoAppuNn9qLh2PAWT-6vjc0UMzF96h_h7n0Eaf3cuNe0MMfd0q5RR6t5YvFDEYil_J_MVNpgQiQNte2yrZeTSbgrEFVohPsXR0NHQyKyRGt3GCmueZOPI8hNjBbH4s5ULmNZCTPHNxwcvMOxkJkY8vaFrCE5HF6-m-ROBh8jcYFj6xd6CwclHCtgUhvMgv3DDcpDR2-yI2KwFC3ATjmznT16_wdXXs0RlnsHRn5m6FnJNj0zBToLTvQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
اکسیوس:دونالد ترامپ، رئیس‌جمهور آمریکا، در آستانه انتخابات ۲۷ اکتبر اسرائیل، بارها از اعلام حمایت صریح از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خودداری کرده است؛ این در حالی است که ائتلاف نتانیاهو در نظرسنجی‌ها از جناح مخالف عقب‌تر است و تنش‌ها میان این دو رهبر رو به افزایش است.
پیش‌بینی می‌شود ائتلاف نتانیاهو حدود ۴۹ تا ۵۳ کرسی به دست آورد که بسیار کمتر از ۶۱ کرسیِ مورد نیاز برای کسب اکثریت است، حال آنکه مجموع کرسی‌های احزاب مخالف بین ۶۷ تا ۷۰ کرسی برآورد می‌شود. همچنین در اکثر نظرسنجی‌ها، گادی آیزنکوت، رئیس پیشین ستاد کل ارتش اسرائیل، از نظر میزان محبوبیت از نتانیاهو پیشی گرفته است.
اختلاف‌نظر میان ترامپ و نتانیاهو بر سر مسائلی همچون ایران، غزه و لبنان افزایش یافته است. ترامپ از رهبر اسرائیل دل‌چرکین شده و در محافل خصوصی او را «بزرگ‌ترین دشمن خودش» توصیف کرده است.
آخرین مورد اختلاف آن‌ها مربوط به مخالفت علنی نتانیاهو با طرح ترامپ برای غزه و خلع سلاح حماس بود؛ هرچند نتانیاهو متعاقباً پذیرفت که به این طرح فرصتی بدهد و از شدت حملات اسرائیل بکاهد.
در همین حال، رقبای نتانیاهو از جمله آیزنکوت، نفتالی بنت و یائیر لاپید، از طریق کانال‌های غیررسمی پیام‌هایی به اطرافیان ترامپ ارسال کرده و از او خواسته‌اند که در انتخابات بی‌طرف بماند. ترامپ در هفته‌های اخیر چهار بار با این پرسش مواجه شده که آیا از نتانیاهو حمایت می‌کند یا خیر، اما هر بار از اعلام چنین حمایتی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70075" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70074" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70074" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbGmkPxY7_hdDTdE5axQS6X9A4sRwXi1Y_Ig-bNZ7h6MqfEfdri8YRvD9D44TfjQCgK8Fgub3Jvi1FtRpIRFjVvZbO0ipsydn0jy-SNzTVs5nQFXV9dCjGyqdkAFNw2Wu_ZJAP1Lx8JvYOUE9eM9vq0q9wpcKh3jHt2lrRw8l45xa8eurizErpB72WeB_laWB5wrtBnHbjUe9rfVTX8uI8aA7RDeQ65_Iq_YwlHlUzxgeZ8CzcgCIxUXh_rCfKvmlLNa6PyUHKH1GJUQaJJifwTPANFuy9XzSAveeh7tbrVR2rXwPfZlvhNkp4VBw-3Ee720gBZy8CV2V1SNzk8igg.jpg" alt="photo" loading="lazy"/></div>
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
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70073" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=hQCGpDYNrakPa5w5hz8-kvacKLSVJs7cxQn-UeSDowodxNqylNwLZgteRpEr2_ug4F2802Rs--w1_xtK40qRsjDT7YPEPs69YrrEix6vebfXm051rMnwRK-QFSDVSU4gqUyFsOa0AyEnh0kWYcSh-AP84dOoMztU_WurYFsb-OtPH5owm2ZAeDmud4OXrqXgtSAJTqV-lObSevAIu63qxOTHSgicby3E0KO5j-94eGakziA6j1mG1E31zF6oKbb8WRMd3UkGG2yQ_kI_P9erN14tQcJ9i22CoDQG31vDiG7hIsnqQ11pNZg1FjR8t_OZxfji7vgc7qRHkjsZini9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f783bdf6d2.mp4?token=hQCGpDYNrakPa5w5hz8-kvacKLSVJs7cxQn-UeSDowodxNqylNwLZgteRpEr2_ug4F2802Rs--w1_xtK40qRsjDT7YPEPs69YrrEix6vebfXm051rMnwRK-QFSDVSU4gqUyFsOa0AyEnh0kWYcSh-AP84dOoMztU_WurYFsb-OtPH5owm2ZAeDmud4OXrqXgtSAJTqV-lObSevAIu63qxOTHSgicby3E0KO5j-94eGakziA6j1mG1E31zF6oKbb8WRMd3UkGG2yQ_kI_P9erN14tQcJ9i22CoDQG31vDiG7hIsnqQ11pNZg1FjR8t_OZxfji7vgc7qRHkjsZini9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیروز تو محل دفن خامنه‌ای یکی اومد به ترامپ فحش بده، حراست زد دهنشو بست:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70072" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=YJO3_K0kbAz0Yn7zh7KT2TFSwK2USPe6-X0ly2MPan5lnHutxMHqEihWgTl1v9d10H0kGCOg1Mg9WkLr0fhNeTcn7x-uyOjXdM7b-bl8T2UN-2cQOsI4HYmzFtDjbplaAztOFHvZGOpOcUQmd3de0KtK3LUVWDQ6b4ZluRKzL9BnSjhQKfG18xP6irLgV-COIsYiYkGaRDJT0v1w4Vny-NpnNG9g4aHc_VbSMMu8i4uk3ddpaePf4YPZeELBh2qBrTkg5mf68KEK9mI2bfnjVQEawn0GcsqljASxdi9_QwZaO0GYAL0eQFjwCWob2RuWjeymDH7-YkIc8d49oSj_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/59dbb77b21.mp4?token=YJO3_K0kbAz0Yn7zh7KT2TFSwK2USPe6-X0ly2MPan5lnHutxMHqEihWgTl1v9d10H0kGCOg1Mg9WkLr0fhNeTcn7x-uyOjXdM7b-bl8T2UN-2cQOsI4HYmzFtDjbplaAztOFHvZGOpOcUQmd3de0KtK3LUVWDQ6b4ZluRKzL9BnSjhQKfG18xP6irLgV-COIsYiYkGaRDJT0v1w4Vny-NpnNG9g4aHc_VbSMMu8i4uk3ddpaePf4YPZeELBh2qBrTkg5mf68KEK9mI2bfnjVQEawn0GcsqljASxdi9_QwZaO0GYAL0eQFjwCWob2RuWjeymDH7-YkIc8d49oSj_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهارتا دختر یه سفره سه روزه رفتن شمال، حالا چقدر خرج کرده باشن خوبه؟
۵۸ میلیون تومن ناقابل
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70071" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💢
🎙
صحبتای اشکان خطیبی درباره بازداشتش :
در حال حاضر پناهنده سیاسی هستم، از ۲ سالگی کتاب خوندن رو شروع کردم و وقتی ۱۷ سالم بود وارد دانشگاه شدم و کوچکترین دانشجوی دانشگاه بودم
من رو از جلوی در خونه گرفتن و بازجویی خیلی خشنی داشتم؛ ضرب‌وشتم، تهدید و فحش‌های رکیک و جنسی به خودم و خانوادم
۷ اتهام مختلف هم بهم تفهیم کردن؛ از توهین به ائمه و پیامبر و رهبری گرفته تا دعوت به اغتشاش، برهم زدن امنیت ملی و ضدانقلاب بودن
😳
حداقل ۵ بار دیگه توسط ارگان‌های مختلف بازجویی شدم؛ حتی یه کارشناس مسائل تروریستی خاورمیانه در وزارت ارشاد ازم بازجویی کرد
به‌خاطر استوری و فعالیت تو فضای مجازی این کارا رو با من کردن، ولی میدونستم دارم چیکار می‌کنم چون دیگه تحمل نداشتم.
تنها چیزی که خوشحالم می‌کنه اینه که بدونم یه قدم به آزادی نزدیک‌تر شدیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70070" target="_blank">📅 09:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
این خونه فوق لاکچری که تو سعادت آباد میبینید ویلا نیست!
اپارتمانه که شبیه ویلا ساختن
واقعا اگه اینایی ک این خونه هارو میخرن زندگی میکنن
پس ما چیکار میکنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70069" target="_blank">📅 09:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94046ec789.mp4?token=enVYsc6KM90SHnVnBASXHsbp1LDf8YWlficicOrBrIejSaOJQnAtfT-gsnALlrWkKJAEvYugZ5CpI9Dht5nsVv7EPuXyl69oHAvKuMMCO3w3eGVzfL0vzpsttesrNKBPGzdXVaIVLdwDtvBw3dZNPGrlHtroudHJsZ1n3It5QmY3oAMnGJ8FtAxfBjTp-cxbqi0QfI5SejuqzGrSRmCqPadY6DS8V_q6QjuWNV5dQ1UjY9bXUj-FBZGwwmKH0N7m6PL94BXEZrjPO1p20r-y--PfqFNpvHM9Ba9GHMalMo_WQHo_jCVUFoMTNoohXgph9cOhfIEWyjG-z45-QkSNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94046ec789.mp4?token=enVYsc6KM90SHnVnBASXHsbp1LDf8YWlficicOrBrIejSaOJQnAtfT-gsnALlrWkKJAEvYugZ5CpI9Dht5nsVv7EPuXyl69oHAvKuMMCO3w3eGVzfL0vzpsttesrNKBPGzdXVaIVLdwDtvBw3dZNPGrlHtroudHJsZ1n3It5QmY3oAMnGJ8FtAxfBjTp-cxbqi0QfI5SejuqzGrSRmCqPadY6DS8V_q6QjuWNV5dQ1UjY9bXUj-FBZGwwmKH0N7m6PL94BXEZrjPO1p20r-y--PfqFNpvHM9Ba9GHMalMo_WQHo_jCVUFoMTNoohXgph9cOhfIEWyjG-z45-QkSNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
هزینه‌ها چند برابر شده، مسیر واردات طولانی‌تر و درآمدهای ما کمتر شده است.
نفت را نمی‌توانیم مثل گذشته بفروشیم و با تخریب برخی کارخانه‌ها، درآمد مالیاتی هم کاهش یافته؛
با این حال مجبوریم برای ادامه فعالیت اقتصادی به آن‌ها کمک مالی کنیم.
مشکلات ما چندین برابر شده، در حالی که درآمدمان کاهش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70068" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70067" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=aG4Ms1NNW7_Ggwol9mRo3OOP8GWC3sT0vgf_h5JXZ4GlMbW-eavQ2hkJa2zm1C2a3sfC5DKTN9dXaaUZuammahy2l8LaCazH26hyQsMDZb4LhgqbIh034RqIxYU7a4nUBZcrFXYYg-SaK8wl-oYKskQZ3U6zkLF_IQadP28teR33WkPWtJT-jtYHqpcV_A0zUUoG_q8IHkKBFtVtn78IlcSTb9KlDfGh7tsYFjCixuxbMeiQA4iGAuFnORaeLsRQJX7ihvRuc5GUomvOaao-mb-rZdjjvojU3LOyuUAbUdYGI-V9F2TC6rr0JvLjwAlAppLK9-Fhh_T8d_o8dZBe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=aG4Ms1NNW7_Ggwol9mRo3OOP8GWC3sT0vgf_h5JXZ4GlMbW-eavQ2hkJa2zm1C2a3sfC5DKTN9dXaaUZuammahy2l8LaCazH26hyQsMDZb4LhgqbIh034RqIxYU7a4nUBZcrFXYYg-SaK8wl-oYKskQZ3U6zkLF_IQadP28teR33WkPWtJT-jtYHqpcV_A0zUUoG_q8IHkKBFtVtn78IlcSTb9KlDfGh7tsYFjCixuxbMeiQA4iGAuFnORaeLsRQJX7ihvRuc5GUomvOaao-mb-rZdjjvojU3LOyuUAbUdYGI-V9F2TC6rr0JvLjwAlAppLK9-Fhh_T8d_o8dZBe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a23
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70066" target="_blank">📅 01:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=l_49n7PiJrAGpe15G7XqbePgdw2HULKw1P8VYHYLf4YeODtRUcN-G3Q7HbWhaJsAG66ZubRNG23qOK_p8SAeAWFA7dlHORvb8WZMghFatUSMxXpGwUM_3GsXWgLzbtol82N-TRN_ykrZ6xdjanZKD7zzlF_T0mdQg9_E72EJG7As-CMK9an3AJGBKUI1NJg3CtPMHTT1dMbvQ9pm0Ia23Y3atAeiJkdD-4QYdWRMNPCEAOc0tyiV9yX3D0UH94P0cDXJ9HYw2OuzZVsj_Pnts33M_VaMvMl6gIomo_YRLFAvST9bVHyfvzflz-9QAEn6fFny4DbOH_G8OE4tsp794g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a20a8bef.mp4?token=l_49n7PiJrAGpe15G7XqbePgdw2HULKw1P8VYHYLf4YeODtRUcN-G3Q7HbWhaJsAG66ZubRNG23qOK_p8SAeAWFA7dlHORvb8WZMghFatUSMxXpGwUM_3GsXWgLzbtol82N-TRN_ykrZ6xdjanZKD7zzlF_T0mdQg9_E72EJG7As-CMK9an3AJGBKUI1NJg3CtPMHTT1dMbvQ9pm0Ia23Y3atAeiJkdD-4QYdWRMNPCEAOc0tyiV9yX3D0UH94P0cDXJ9HYw2OuzZVsj_Pnts33M_VaMvMl6gIomo_YRLFAvST9bVHyfvzflz-9QAEn6fFny4DbOH_G8OE4tsp794g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
ترامپ:
ما قادریم تمام آنجا را نابود کنیم؛ اما نمی‌خواهیم چنین کاری انجام دهیم.
ما تحریم‌های اقتصادی بی‌سابقه‌ای را علیه آن‌ها اعمال کرده‌ایم.
اگر آن‌ها دست به حمله بزنند، ما صد برابر شدیدتر پاسخ خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70065" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=doWpdgptbQ6cewCUFcE2xYkUP4pMjQabjRI-fcnNcsxNfepO5tRwT4lfHTJg_7bc1wMK3uSyTWxqQ_NkdPWdiMRsr8877sD8i3NZ4ij01DI5ctQNJj9xfbEVGCaH03PSL_Uv9EYweT9WyEMlWi4G4qwTX2hYJGJW0bYursRqsCx9jQ4MITaGVmGlc6Juez4Nq7H_SNY64Kpk0TR21BgfrQIBhIIlu8d3sB0XXjlYhVFAoBSc8JPfxYZDij-RnUKb3z7_ZNh2h0Ys5RdxXvRUDQLPs1_erfYHlm5NQ5x_R3yx7iOsglz2V6xQvCpXbElU8nNAWGAIe0uynW_DGGl9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71c06ff85.mp4?token=doWpdgptbQ6cewCUFcE2xYkUP4pMjQabjRI-fcnNcsxNfepO5tRwT4lfHTJg_7bc1wMK3uSyTWxqQ_NkdPWdiMRsr8877sD8i3NZ4ij01DI5ctQNJj9xfbEVGCaH03PSL_Uv9EYweT9WyEMlWi4G4qwTX2hYJGJW0bYursRqsCx9jQ4MITaGVmGlc6Juez4Nq7H_SNY64Kpk0TR21BgfrQIBhIIlu8d3sB0XXjlYhVFAoBSc8JPfxYZDij-RnUKb3z7_ZNh2h0Ys5RdxXvRUDQLPs1_erfYHlm5NQ5x_R3yx7iOsglz2V6xQvCpXbElU8nNAWGAIe0uynW_DGGl9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:ایران تنها کشوریه که کسی نمیخواد رئیس جمهورش باشه.
«آن‌ها هیچ رهبری‌ای ندارند.
رهبری‌شان از بین رفته است؛ رده اولشان رفته، رده دومشان رفته و نیمی از رده سومشان هم از دست رفته است.
این یکی از مشکلات من است؛ کسی نیست که با او مذاکره کنم. این یک مشکل است.
من گفتم: "آیا مطمئنید حال این آدم خوب است؟"
اینجا تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70064" target="_blank">📅 00:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55686a2794.mp4?token=AUSNnWWpDrkMokXhqPSzX-7AO4KgbJ4RzMy79ggO35n3SVISObkRedf8cRd29OAVgW9zT0-xK-OQqlc6bM8iS3TeCBpX7ZeR7OWlz6zaA0kEDwRx2ZrQ9mxec2ekITSagciM2dumERAyAK_-b-K908qM6z5eCxBSZjP_Et6d43VA5fflHhjfwtUNBu4Rl_NaXuz0Kc6uR_cgce0VhT1pmkl8geasa9Tf-Gdex2tgp04xA0a1Emi1fBTze-CS9hEfGMyD5m1szhDAEN3gon_cojGe9lnvLRafs60Nhq1SOKDnrA_UkHDWXAfvFULwVjXKT5TEPlFcFNj1iu5DzOxeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55686a2794.mp4?token=AUSNnWWpDrkMokXhqPSzX-7AO4KgbJ4RzMy79ggO35n3SVISObkRedf8cRd29OAVgW9zT0-xK-OQqlc6bM8iS3TeCBpX7ZeR7OWlz6zaA0kEDwRx2ZrQ9mxec2ekITSagciM2dumERAyAK_-b-K908qM6z5eCxBSZjP_Et6d43VA5fflHhjfwtUNBu4Rl_NaXuz0Kc6uR_cgce0VhT1pmkl8geasa9Tf-Gdex2tgp04xA0a1Emi1fBTze-CS9hEfGMyD5m1szhDAEN3gon_cojGe9lnvLRafs60Nhq1SOKDnrA_UkHDWXAfvFULwVjXKT5TEPlFcFNj1iu5DzOxeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«آن‌ها ۲۱۲ هواپیمای بسیار خوب داشتند—برخی را به برکت اوباما، باراک حسین اوباما، به زیبایی از ایالات متحده خریده بودند.
از او شنیده‌اید؟ باراک حسین اوباما. و هر کدام از هواپیماهایشان ساقط شده، از بین رفته.
آن‌ها هیچ رهبری ندارند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70063" target="_blank">📅 00:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=RBPFMBaMtBB6dATm40TbLkS75hu0gZMKi897EimONlh2g7qpIm2DO_4UXukrboAOjv0dfmq7bruesI-D6esM_z-XvgDzprCNZ_aa972V4Acfgnr4eomY40aOEticS78qDzgOD9-CqbqobjEJdH3cNwcEEU56bJrBHoZbX9P1vIsy7iW_SrgHzLEyMLbyH6cH0BEtTPjmL7Hp1l2e64NJbgqadzFH_DmEgtBBm0Hjw2yUSAGVFDO1jLYWNiIZL6Y_oD5jIXtNGcdeh1PJ2Wk0NXCmLoq7Poxb5dNXS5zeAt4zrMzpxVyEIuS7RpwTSBTJ7EtnVuxVrCA1_Em43OhFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ccab4d33.mp4?token=RBPFMBaMtBB6dATm40TbLkS75hu0gZMKi897EimONlh2g7qpIm2DO_4UXukrboAOjv0dfmq7bruesI-D6esM_z-XvgDzprCNZ_aa972V4Acfgnr4eomY40aOEticS78qDzgOD9-CqbqobjEJdH3cNwcEEU56bJrBHoZbX9P1vIsy7iW_SrgHzLEyMLbyH6cH0BEtTPjmL7Hp1l2e64NJbgqadzFH_DmEgtBBm0Hjw2yUSAGVFDO1jLYWNiIZL6Y_oD5jIXtNGcdeh1PJ2Wk0NXCmLoq7Poxb5dNXS5zeAt4zrMzpxVyEIuS7RpwTSBTJ7EtnVuxVrCA1_Em43OhFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«و ما در مورد جمهوری اسلامی ایران هم داریم به موفقیت‌های بزرگی دست می‌یابیم. هیچ‌کس نمی‌داند چقدر موفق عمل کرده‌ایم؛ آن‌ها نمی‌خواهند این را بنویسند، اما خودشان می‌دانند.
می‌دانید چه کسی می‌داند که ما چقدر خوب پیش می‌رویم؟ خودِ ایران. به این فکر کنید: آن‌ها نیروی دریایی ندارند؛ وضعیت کاملاً یک‌طرفه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70062" target="_blank">📅 00:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=ESI8DfHekBZ5QV6fi3HGzVNIse2da5nXCVbVNGBhIYG45-WW3GoodDOilEmPtuLpWE3Y57F9N-T7GUj5mQUS2HNIarubp2ian4pWRjV2pA7ap09R4Ml5QDD2LiQBXUNhahh19A-8Un55mWfVQdPcTSGm_WvAfGvd1DFV9DbWUbG-zh99-SVIVsE_-nnRlGRzSR4HfrBEooi5ZgPFXmAplw0vkiOJyZIG63J-3q0O-OlismdTcADBUiNsiCvHcWeVyjea_ySda8woq6vaNaHNM-jYE2G-G_d-oEIc6WsRA3KWtjotJTPj0_lYzgbZQjUpS0jHm9c_4myFq79DuHxblg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b256a73ac8.mp4?token=ESI8DfHekBZ5QV6fi3HGzVNIse2da5nXCVbVNGBhIYG45-WW3GoodDOilEmPtuLpWE3Y57F9N-T7GUj5mQUS2HNIarubp2ian4pWRjV2pA7ap09R4Ml5QDD2LiQBXUNhahh19A-8Un55mWfVQdPcTSGm_WvAfGvd1DFV9DbWUbG-zh99-SVIVsE_-nnRlGRzSR4HfrBEooi5ZgPFXmAplw0vkiOJyZIG63J-3q0O-OlismdTcADBUiNsiCvHcWeVyjea_ySda8woq6vaNaHNM-jYE2G-G_d-oEIc6WsRA3KWtjotJTPj0_lYzgbZQjUpS0jHm9c_4myFq79DuHxblg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«پس فقط این را می‌گویم. اینکه کمی بیشتر برای بنزین خود پول پرداخت کنید، فقط به یاد داشته باشید که این کار را می‌کنید تا یک کشور بسیار شرور نتواند سلاح هسته‌ای داشته باشد، کشوری که واقعاً حامی شماره یک تروریسم دولتی در جهان است. ما نمی‌خواهیم آن‌ها سلاح هسته‌ای داشته باشند.
پس وقتی مجبور شدید کمی بیشتر پرداخت کنید، حتی اگر به چهار دلار برسد، اشکالی ندارد. من هرگز عذرخواهی نخواهم کرد، کار درستی انجام دادم. اگر این نبود، منظورم این است، من در بسیاری از ایالت‌ها قیمت را به زیر دو دلار رسانده بودم، اما کالیفرنیا را نمی‌توان شامل شد چون آن‌ها مدام مالیات وضع می‌کنند و وضع می‌کنند. شما قیمت نفت را پایین می‌آورید و آن‌ها در نهایت بیشتر از آنچه پایین آوردید، از شما مالیات می‌گیرند.
فقط باید به یاد داشته باشید که کاری که ما انجام می‌دهیم، خدمتی بزرگ به جهان است، نه تنها برای خودمان، بلکه برای جهان، و ما واقعاً کار بزرگی انجام می‌دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70061" target="_blank">📅 00:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPKk3_tAPrbyOyw6aWL4dxGoYzc1cEiOzMJsKs_1eYCKiMHIUX2KrPXs2ks9a2b55Qg9ThKhQbp30SWUaT78E0mAWtBDLFFCXq3VBbzfvOGv4G0jGI1JBYzN7DIGpQCDbMl5wQCcEdh6Be2W5L7EfBb8uwKp_zbQJ5q2YYDF96oioUdLqOKnCLVZx339pB_pTSvGlANhpMRtWNT1MmXC8Dyk21ME2zVV1Nj3Aq6uCUvvnTAhhTktAbuJ8JqKqKEx84gelpqMgQ6IAlGwV1KYyyl3C3H2k65pA0zqwRmJEyhBNAkWdOrwdXUtUXdYC_09wS0zyeHG7bBHO3Lifj_Clt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c189273f.mp4?token=VMfsM3Sv7JSZgbHbyxRGeWg5dLe4q-ecz2ahtRCC92xIoFS4kwjL1v2Nrf5lHZFlj5dtrzLtaVkhIF4to4NCCZ_PXD2CHUgGKa24u82yGledOo-NobMRyuFmUD7uVGmYXeKbBGotO9ngeD3NnF7dVTzlxtU2GZv4vpoD36hnAV8hW1M4cdpWh3EG4euWfTayaRLmwBftf3i12sF4f7mo3p8T-4CkLZMNY2NWZ8g4YxByqncJQRAowgMwZmrS8pt88LlaCVEfJA7q-_S13P6qARgvoU-hKirpMc4s3ULIcX0CN7MRZMXKlo7IQIQZPsiihtCQKcc2TjTieSUJYC-hPKk3_tAPrbyOyw6aWL4dxGoYzc1cEiOzMJsKs_1eYCKiMHIUX2KrPXs2ks9a2b55Qg9ThKhQbp30SWUaT78E0mAWtBDLFFCXq3VBbzfvOGv4G0jGI1JBYzN7DIGpQCDbMl5wQCcEdh6Be2W5L7EfBb8uwKp_zbQJ5q2YYDF96oioUdLqOKnCLVZx339pB_pTSvGlANhpMRtWNT1MmXC8Dyk21ME2zVV1Nj3Aq6uCUvvnTAhhTktAbuJ8JqKqKEx84gelpqMgQ6IAlGwV1KYyyl3C3H2k65pA0zqwRmJEyhBNAkWdOrwdXUtUXdYC_09wS0zyeHG7bBHO3Lifj_Clt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران به‌شدت در حال شکست خوردنه.
به‌زودی اعلام می‌کنم که تنگه هرمز به قلمرو ایالات متحده تبدیل شده.
به افرادم گفتم: «باید یه سفر کوچیک به خاورمیانه داشته باشیم، چون باید جلوی یه فاجعه احتمالی رو بگیریم؛ یه آتش خیلی بزرگ، چیزی که تا حالا مثلش رو ندیدید.»
وقتی مجبور بشید برای بنزین یه مقدار بیشتر پول بدید، من هیچ‌وقت بابتش عذرخواهی نمی‌کنم. من کار درست رو انجام دادم.
یک کشور خیلی شرور نباید سلاح هسته‌ای داشته باشه.
کاری که ما داریم انجام میدیم، خدمت بزرگی به دنیاست؛ نه فقط برای خودمون، بلکه برای کل دنیا.
ما واقعاً داریم کار بزرگی انجام میدیم. محاصره مثل یک دیوار فولادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70060" target="_blank">📅 23:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj1UVLpnzGi2xu2gRrvkRei5kce5k6Nj2BfVhRHJzBjGfoxolxCE37mfFBeCEVKL1VGvuer3txfzwZlGgdG8CzM4YptUOGZmPhdt6d8oZhIjp7nC7El4LjB5Xc1lH5xkpNyEr8Jg12HkSFVJD2E7KlJUuqcI3bpeIWiN4MUDzGq2wrgwFXpS8u7mrCck8-MEkGpzLO8s9p6ztExoAUDkRgFLDw8N2wUHq5ck2KsMJU8IVJZ0v-FQItf4yWlScQA8APLWFMpbAL1vOZ5GOYhLaavzWu6eo98sqVpw2-g8FtbOaI7qOKZPvtQ18CK7Gyvlu6AKHAOw5E8mPkMcs9Ng-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70059" target="_blank">📅 23:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d105db041c.mp4?token=eXUuIFdWQYxCSz3UmX07g1QFMRFvgSUmxro23l2saPOlgd8kl--rItOHmtkHotAEn03RUWYjuL3101i3LE6RWGgX4nwiG9p1HWJqi54liyYwpgk3qvrY2DO8S2mdLLo0WqfcFh7sxofrvyxd4UlyvcCIfBRdlSJgC4VcQBzXlYuy21LaU67e5dH2huCuYrhCXCUs8Z7AmW7BoAvC3d5kzRrlE2z78ZEWSp3zpXxDXFrXKV8Qg7Tq3dFMOK6CDmqauOvdHfjEd_ivIr1tSkea7UWta9Ue7ZgNnMpuUjBrUPuEX4TbVyx_axmX5ALLFtT-rJgJ4TpnH84RZs2jdN6MDTVdrNF2ZFB7UFVi-AbYDGt7Ce7Ly8hFzFY_PyQrDTzKaXonBruDwqNlGBHVYeP0L0jCsvV_H8jA_sQV1DoV-9BI8yCgRAN3ZO2dqZrMJ4-xoMmYwOrG3NM97oUiVQYkZUsy30YYCamj0CRv7unvKMCxWYqK1OgB3G4e8q4WBKkcyCl5toNCFKJ9UbYyYZX0UYQMzlLCUUa4RG8x5623QLPvX0ekxP-3mwg2_8SK8VhvUEGRzsZK1AwL18sXeRZVc4xtcrecjSefbdvei3SftM4s7tM61KbOi8RvWwJ-iuRSpqX6QPcFoR8WjLxMzsM6xixD755zTcT69T6j9ODezgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d105db041c.mp4?token=eXUuIFdWQYxCSz3UmX07g1QFMRFvgSUmxro23l2saPOlgd8kl--rItOHmtkHotAEn03RUWYjuL3101i3LE6RWGgX4nwiG9p1HWJqi54liyYwpgk3qvrY2DO8S2mdLLo0WqfcFh7sxofrvyxd4UlyvcCIfBRdlSJgC4VcQBzXlYuy21LaU67e5dH2huCuYrhCXCUs8Z7AmW7BoAvC3d5kzRrlE2z78ZEWSp3zpXxDXFrXKV8Qg7Tq3dFMOK6CDmqauOvdHfjEd_ivIr1tSkea7UWta9Ue7ZgNnMpuUjBrUPuEX4TbVyx_axmX5ALLFtT-rJgJ4TpnH84RZs2jdN6MDTVdrNF2ZFB7UFVi-AbYDGt7Ce7Ly8hFzFY_PyQrDTzKaXonBruDwqNlGBHVYeP0L0jCsvV_H8jA_sQV1DoV-9BI8yCgRAN3ZO2dqZrMJ4-xoMmYwOrG3NM97oUiVQYkZUsy30YYCamj0CRv7unvKMCxWYqK1OgB3G4e8q4WBKkcyCl5toNCFKJ9UbYyYZX0UYQMzlLCUUa4RG8x5623QLPvX0ekxP-3mwg2_8SK8VhvUEGRzsZK1AwL18sXeRZVc4xtcrecjSefbdvei3SftM4s7tM61KbOi8RvWwJ-iuRSpqX6QPcFoR8WjLxMzsM6xixD755zTcT69T6j9ODezgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار
: اعضای خانواده نظامیان درباره شرایط داخل ناو «آبراهام لینکلن» نگران هستند.
🇺🇸
ترامپ
: نه، آنها نگران نیستند. این ناو همین حالا یا خیلی زود حرکت خواهد کرد و یک ناو بسیار مشابه جایگزین آن خواهد شد.
🔴
خبرنگار
: آیا مأموریت این ناو بیش از حد طولانی شده است؟
🇺🇸
ترامپ
: نه. نه. نه. اصلاً به اندازه کافی طولانی نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70058" target="_blank">📅 22:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70056">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=nL-Tk5ooq2NLiasxjqPPCXplaQ9sO_NcgKCy55_WgLOWHLAGrF26h8-0t2K0ehKLO68sPP21rakKPBD7BIhCQInrlz3yXjERjKskzTM9R2pfbnGfAknFSR6paL_LRFt_jF9SCK8061lSXbsoixH2-THs2yxGtyZgMXI0aD7YqZlFZ7wHsoTw13MnqJdN9ZxSxJ3WkPbpMDKHvoa9LUX8dWuCBoEwTuUsi01lkdX5al6je8Lr67yXIkE5BSv57WDPE8VpLjaxFcnOBSspZBQfUmNaE5hemddhpHcQ8xayyIcf8nA5eJkbPk8J_XPuaEMtpuy96ay8V2Pt5RjNydEHnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=nL-Tk5ooq2NLiasxjqPPCXplaQ9sO_NcgKCy55_WgLOWHLAGrF26h8-0t2K0ehKLO68sPP21rakKPBD7BIhCQInrlz3yXjERjKskzTM9R2pfbnGfAknFSR6paL_LRFt_jF9SCK8061lSXbsoixH2-THs2yxGtyZgMXI0aD7YqZlFZ7wHsoTw13MnqJdN9ZxSxJ3WkPbpMDKHvoa9LUX8dWuCBoEwTuUsi01lkdX5al6je8Lr67yXIkE5BSv57WDPE8VpLjaxFcnOBSspZBQfUmNaE5hemddhpHcQ8xayyIcf8nA5eJkbPk8J_XPuaEMtpuy96ay8V2Pt5RjNydEHnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت جنگنده اوکراینی مدل میگ-29، امروز صبح در حین تعقیب یک پهپاد روسی مدل "گران" بر فراز منطقه اودسا، موفق به سرنگون کردن آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70056" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDl1b1purOgADYAG_AvcU07496SCailqNAOyvxlpQxFwxeVlHjSRgqljwF9qzwohFLsw-GVJG8E3tChYDaoHIizURv447si5U76QJNITDE5buMuJdHL5DluFsi4zfNimjQhoaomvYtspf2Res38GSiyqFvUKuw5o85Q-Ew8XnKKef0wlK16auaYnWOdoyVJv3tD_VQHffaVq6AwWGYITVAHzexOPjQBT60Wz6_JyY0elPUO8ZT_wGtDpCFBSAdQwkR0cyctMYnm018Rh5VCCKX-FXAWIfzdG6rs1zmoKmGbOPF7v5uxfz9rrq18aJRw-sW6pJeikabIpr4VigfKh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQt5aMeFpYUSeQ0ziW9ozQJeFgaEVSYnfmOC9jAB_Uss_cJOSdXnOwTioOjHHDQl3U-CSoNUOKqDMtXYpgm6W7PpG4b4UVFhluRgJuHFsCaFVyCMa3rgOr2boBu5UCIjBkR18dCoVjjzXY207IyCBtK0pYkEkjqZXheejuVwfriqkdO6OPISg_mLd7Qpn2gDvHCe7G-WJjnkzbFlnjsBDTqA0LuIzhwEP9K468BnpPvluD-aFkPIQ1CVfIjjaOv8nLdB88e3engVr2f9_2e9R_OypbX0nMReAd7ypGRKb-LaePWql8AsFJQIrFjUoOvedvWLB88G8nZ1n2HshVMNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vB3uHlL0bi9xqHJuAyvGM0wG5044RWcQvxXnswIp3QmZ2ZlOTtDVGHhiXFkZGGDutee-OMDc4Yb2bVZfpFVGnRmaxXfLFe3wye4TgcmtNNVpywmGz71Awe1lhEZz0olMg0kVY5dgqSXZM9uTX6_2BIGbaxZf7X0-3SAmF4uc2J5jzhI8i0-QkNQcU1L8QCW6FnCoK-Cep2HOG1v2hg4Ku9ylS5_eJEqG7ytUXggUWv37dyv3xyu_ZYQk1mo9sj-WdmSnToSy3g0VOHAQaVEXGgKM1JIee4vKaKd9ji9QU9pUanBYLCMcCZPEOyByYFNJ1YRryYWC07PAgDGOPgVhGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=f0mKxhONdVIbTnTb11zVsG3AnYICjDneSYw-3k6oHcT8GjfD2s9xvKNhCzH3RogWmiIAb09Z4gcGyI-oAA6Oh_C6vW8PDGbrkcamY2Cb14i1LDlxZ-cakkG08mrsHVJtsPI9FzaHSOg6xb95GVYfMw5hxT-ChdZfrC6f2y2HfhjIh_ipx_Zwr9sfrqCC1Yv0EIDzIixMYHXUdjSSxa1t6c1rfvCcVDncE4D8kgbeyk9imRZpds6NLONaLVH-ecM-6zwJuRPia1N43PEXDb1K76NLYGZmPOh3lGPt6p17nOpd2Mq4oQAQ5aZ-1zHvEcTh-usqEI58ylTmtSHeuioGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cd1ffaaa.mp4?token=f0mKxhONdVIbTnTb11zVsG3AnYICjDneSYw-3k6oHcT8GjfD2s9xvKNhCzH3RogWmiIAb09Z4gcGyI-oAA6Oh_C6vW8PDGbrkcamY2Cb14i1LDlxZ-cakkG08mrsHVJtsPI9FzaHSOg6xb95GVYfMw5hxT-ChdZfrC6f2y2HfhjIh_ipx_Zwr9sfrqCC1Yv0EIDzIixMYHXUdjSSxa1t6c1rfvCcVDncE4D8kgbeyk9imRZpds6NLONaLVH-ecM-6zwJuRPia1N43PEXDb1K76NLYGZmPOh3lGPt6p17nOpd2Mq4oQAQ5aZ-1zHvEcTh-usqEI58ylTmtSHeuioGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
〰️
صفحه اسرائیل به فارسی در پلتفرم ایکس:دو مهمون خوشگل از ایران
🦌
امروز صبح جنگلبان پارک ملی برعام در منطقه گالیل شمال اسرائیل با یک منظره زیبا روبرو شد. دو گوزن زرد ایرانی که احتمالا از اندوخته‌گاه طبیعی که در مجاورت پارک است به آنجا آمده بودند.
گوزن زرد ایرانی زیرگونه‌ای از گوزن زرد است که در آستانه انقراض قرار داشت. اما با تمهیدات دولت ایران در دوران پادشاهی پهلوی، موفق به حفظ این نسل شدند.
سازمان طبعیت و پارک‌های اسرائیل در سال‌های پیش از انقلاب وارد گفتگوهایی با دولت شاهنشاهی شد تا چند راس از آن‌ها را برای حفاظت به اسرائیل بیاورند. به موازات آن، اسرائیل دو راس گوزن نر از آلمان گرفت که پیشتر از ایران برای حفاظت به آنجا انتقال یافته بودند.
لحظاتی پیش از آمدن خمینی و در آخرین پرواز تهران - تل‌آویو ۴ راس ماده گوزن زرد آنطور که دولت شاهنشاهی وعده داده بود، با کمک تیمسار منوچهر خسروداد به اسرائیل انتقال داده شدند. اکنون چند گله از گوزن زرد ایرانی در کوه کارمل در اسرائیل زندگی می‌کنند و تحت حفاظت قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70052" target="_blank">📅 20:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7gzx0SQtv3yn65bsh1D5gIfbzMcLDtR2juOp3yrhwHC0SvsLgfdRz8P6yils9tpHECxv6mZ06xSFb6_iP4_byJdOEVCq9xS6KVYlzf-3cE5mwARN9vZ2WEJnhmQiCy7UFYkhjHpMHsIdyd_PYl_qjC9djgIkQ5qxKFK78xaafe0GPOpLINQthRIivp7YLoPqXi4zirjoliqmMziMHfK_rPqZMh_BTzhB4oSSscJW_meUIhL6RLxPNEnz0zsmdLJ0MDJKA8p0Ai6ZXQm-gcd9yyPKZaygWGnfxkhvIk8ckJH0QKvkvMOI9Pm199o09R_XFTyuTCGlcTHpiZjAVVKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی
CENTCOM: اقدامات آمریکا علیه کشتی‌های مرتبط با بنادر ایران
:
🔴
فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نیروهای آمریکایی از زمان تشدید محاصره بنادر ایران:
🔹
۶۲ کشتی تجاری
را تغییر مسیر داده‌اند؛
🔹
۳ کشتی
را از کار انداخته‌اند؛
🔹
و
۲ کشتی
را برای اطمینان از رعایت مقررات، بازرسی و توقیف موقت کرده‌اند.
به گفته CENTCOM، این اقدامات در چارچوب اجرای محاصره بنادر ایران انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70051" target="_blank">📅 20:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=EBBjdNdz8pRWYUwna0ktbit0_hv1FM-ApXnuHxDWF3_KZhlnq6MQT83SQ9I47N5cyuYv4q1XI_eL2sCDKjJkZSgLhqn9Mtk7ic5VUjjLWEL5_b_Ag8TYJwX1gOreqLSH2Vw7RuGPc0nYPM54LQJAqg5X0gIm554yvQedWIsuy7Qv555Kw3fO2qbVIpcFBfpbV4ZDMIY2AH6flX2V_uKgi4BpqSCf7UC68LjAjdnBeTd34-239V5XS7_y6_OjieeHprz2RZ7fW8iXQsGiUL8c7DQZYvAxKCydbAqqotmR2tKU34kjQ5A5KGZvwOVKHBjPkpuE_12IlSllA-xFeQlckA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1768f156c.mp4?token=EBBjdNdz8pRWYUwna0ktbit0_hv1FM-ApXnuHxDWF3_KZhlnq6MQT83SQ9I47N5cyuYv4q1XI_eL2sCDKjJkZSgLhqn9Mtk7ic5VUjjLWEL5_b_Ag8TYJwX1gOreqLSH2Vw7RuGPc0nYPM54LQJAqg5X0gIm554yvQedWIsuy7Qv555Kw3fO2qbVIpcFBfpbV4ZDMIY2AH6flX2V_uKgi4BpqSCf7UC68LjAjdnBeTd34-239V5XS7_y6_OjieeHprz2RZ7fW8iXQsGiUL8c7DQZYvAxKCydbAqqotmR2tKU34kjQ5A5KGZvwOVKHBjPkpuE_12IlSllA-xFeQlckA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسرا وقتی حوصله‌شون سر میره بالاخره یجوری خودشون رو باید سرگرم کنن دیگه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70050" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=EAOlqn2ERexqnOkMEJf0dxOHIT_jEoM8EUETIC8KBOTFZ17z9MVq1gkn-AUMam1YUUiWYdGzEzkCTwWgWoOMJhMslbcaQn6mNdPFJNyftfk1PPcLJeJydoUWxEIqrgkoCVDNVvDu4tEErT_gUrEzikbO0XOtugDdLhIhrOawzYXtFtGP4RxlxAY0AXmkHvr88QDcAWTe-_Vkl4BYzhs0v0sKuGOb0gNeCqO7frHquTDs80KeMGQbWU3jPzUFCoFdH-B_CvCl9MHB5L0jwe_S6WJNebpXC8H31IZuS_5s4gZdQpknp5RwUY023pnTiWpMbnvUS5-AyGrsneBEnADH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9b730cb.mp4?token=EAOlqn2ERexqnOkMEJf0dxOHIT_jEoM8EUETIC8KBOTFZ17z9MVq1gkn-AUMam1YUUiWYdGzEzkCTwWgWoOMJhMslbcaQn6mNdPFJNyftfk1PPcLJeJydoUWxEIqrgkoCVDNVvDu4tEErT_gUrEzikbO0XOtugDdLhIhrOawzYXtFtGP4RxlxAY0AXmkHvr88QDcAWTe-_Vkl4BYzhs0v0sKuGOb0gNeCqO7frHquTDs80KeMGQbWU3jPzUFCoFdH-B_CvCl9MHB5L0jwe_S6WJNebpXC8H31IZuS_5s4gZdQpknp5RwUY023pnTiWpMbnvUS5-AyGrsneBEnADH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
رسانه‌های دولتی: ایران لاشه جنگنده F-15E Strike Eagle نیروی هوایی آمریکا (با شماره دم 00-3000) را به نمایش گذاشتند؛ هواپیمایی که اوایل ماه آوریل در جریان جنگ، با استفاده از یک سامانه پدافند هوایی جدید و تاکتیک‌های ایرانی سرنگون شده بود.
این تصاویر همچنین پهپادهای سرنگون‌شده یا توقیف‌شده آمریکایی و اسرائیلی، از جمله MQ-9 Reaper، Hermes 900 و Hermes 450 را نشان می‌داد که علی‌رغم قابلیت‌های پنهان‌کاری (گریز از رادار)، رهگیری و ساقط شده بودند.
ایران علاوه بر این، پایانه‌های «استارلینک» (Starlink) را به نمایش گذاشت که به گفته مقامات ایرانی، برای هدایت پهپادهای آمریکایی و اسرائیلی و برقراری ارتباط با عوامل و همدستان داخلی در ایران مورد استفاده قرار می‌گرفتند.
در جریان این جنگ، ۱۷۰ فروند هواپیمای آمریکایی و اسرائیلی توسط یگان‌های پدافند هوایی سپاه پاسداران سرنگون شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70046" target="_blank">📅 18:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=n1KAkm-QzEXkOeVtJZbd-rKdA-v-piWxS5AQpY7Tp6I9QPZja340v3GcrALigaTJ4VTienzR9uHKn2CUMg5BOKcgEmweF3JE96nE0xeaPIyKnpcXBjQPCqNwSadurpgRvpqw79Wj4Tbxms-psqxMtZ8Z46TpNPfdTdxSBO6FGsSq5XJvzRNAv67lgwUXiq0dU5QufmScnPOaBxTpMGM6Pnlr1g1WTg3wYRd-tjkBGLtfi7CGH_VJS6vxvj0o8qUmS8_qBN60PugARgI0b_uLl2CAslvIUDY5UNGgKenb9XjcYIemRpGs-DqXtNTSu1WQIUj6p7GXc2gejJ3p5dBu_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488afe5f03.mp4?token=n1KAkm-QzEXkOeVtJZbd-rKdA-v-piWxS5AQpY7Tp6I9QPZja340v3GcrALigaTJ4VTienzR9uHKn2CUMg5BOKcgEmweF3JE96nE0xeaPIyKnpcXBjQPCqNwSadurpgRvpqw79Wj4Tbxms-psqxMtZ8Z46TpNPfdTdxSBO6FGsSq5XJvzRNAv67lgwUXiq0dU5QufmScnPOaBxTpMGM6Pnlr1g1WTg3wYRd-tjkBGLtfi7CGH_VJS6vxvj0o8qUmS8_qBN60PugARgI0b_uLl2CAslvIUDY5UNGgKenb9XjcYIemRpGs-DqXtNTSu1WQIUj6p7GXc2gejJ3p5dBu_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو تبریک تولد این چند تا دختر و پسر بچه، از هزار تا سکانس فیلم ترسناک بدتره!!
😶
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70045" target="_blank">📅 18:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70044" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmD_VCxKIdQqNAqzynu6apJvtuyvg4AjnUQA6nIMGEea21WsPxUPey-2XB00EZSLYq4PTSzDNEYtWnuALKiptjeChfERXNNhc0nNsU6HySZB-8MESRPJ5kCgAz3DUOoRUDxhuIjVsNNMdZNuOwUyXXqoAWy--DT0a2mKMdCWTvUthcmXkuNhrZvwemMJc9e0IpaoZkYHNpPpOjPZlZDaAEe9ZB7jXBj48YUQIjt8xPTcs013rJKB8oAyFakZRS-X2s-0AKTg-LRYF0IHnunbNY6rpIzye6vzRYYhz2-lAtcDLD6Sj3rheGRFuIdlMVWcCTcSpp0FqbGHSGLg0HjtLQ.jpg" alt="photo" loading="lazy"/></div>
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
g23
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70043" target="_blank">📅 18:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70042">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a464071683.mp4?token=JZtM4sk9XSgZHixZjh2uUntYNhlyNVpAkEUnZe16ueFf8c_B5SLrflHfoiG2zRV60ZuLzBat6pIk1CVhTR3DRMQtGHYI-K1qtQuJoZpOoy8zV2gObAkB3-VZVGzWtHkrPsaxTtK2kbRGP1afnQQLQK_Q0_KjfLzyuB-SBrVboNFRcsMNAuSaclW5wnxD5IdrxHhTNe7wBOUO0p1HcIgCgpgxMtCW8MjMLnkQgo3-tQmiHQNOAxmp7E8MUSquAXr1UU9Lv_aYOtsNpEgJp3Z2kfKFC7vdNi8Icv40NkaEramz1ZVkcUM2kfxx1d5jMnPvGO6Ru5JAUlAU4APKtwWlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a464071683.mp4?token=JZtM4sk9XSgZHixZjh2uUntYNhlyNVpAkEUnZe16ueFf8c_B5SLrflHfoiG2zRV60ZuLzBat6pIk1CVhTR3DRMQtGHYI-K1qtQuJoZpOoy8zV2gObAkB3-VZVGzWtHkrPsaxTtK2kbRGP1afnQQLQK_Q0_KjfLzyuB-SBrVboNFRcsMNAuSaclW5wnxD5IdrxHhTNe7wBOUO0p1HcIgCgpgxMtCW8MjMLnkQgo3-tQmiHQNOAxmp7E8MUSquAXr1UU9Lv_aYOtsNpEgJp3Z2kfKFC7vdNi8Icv40NkaEramz1ZVkcUM2kfxx1d5jMnPvGO6Ru5JAUlAU4APKtwWlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
یک خورشیدگرفتگی از فضا چطور به نظر میرسه؟تماشا کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70042" target="_blank">📅 18:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=Ex2C6txTERVAiiLgmVF73ow1lbdHuzhgzdkjVL2tHQas5WKKfzOcK5OkDxgIVqMrb2F2j88f8X7XSsAkfgc6_1pODPW2rRyES3vUG6HbnhhVJY11zN4_oEINX502QPuYYpmb1-IuN5Ft8WmHAJ3HVFdnbwHqwUshZHrirGUy-C1YrDQV_TPsiprU5MQfZcQ4csyCaZq9MzfxkGrLax6R_HoddrW81jWJxShlqsitAiQymsgqRfhb2794v6t29aaNNKJXNvAkzbq_MZdgh90RWGDQSyrX3Ey4zkJtKu2zsdNH1MIJXgURoiGCPQUnRW4kwfrIEdq6PWo53b0UI-LAtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36594ef37b.mp4?token=Ex2C6txTERVAiiLgmVF73ow1lbdHuzhgzdkjVL2tHQas5WKKfzOcK5OkDxgIVqMrb2F2j88f8X7XSsAkfgc6_1pODPW2rRyES3vUG6HbnhhVJY11zN4_oEINX502QPuYYpmb1-IuN5Ft8WmHAJ3HVFdnbwHqwUshZHrirGUy-C1YrDQV_TPsiprU5MQfZcQ4csyCaZq9MzfxkGrLax6R_HoddrW81jWJxShlqsitAiQymsgqRfhb2794v6t29aaNNKJXNvAkzbq_MZdgh90RWGDQSyrX3Ey4zkJtKu2zsdNH1MIJXgURoiGCPQUnRW4kwfrIEdq6PWo53b0UI-LAtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این برنامه‌نویس یه شلاق ساخته و باهاش هوش مصنوعیو میزنه که باعث میشه هوش مصنوعی خیلی سریع‌تر کارکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70041" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=eWL3nGEdVj5sFM5JFzE-75vSPdxs1Wz1Sdog3s37ILSY8_lRmtZ1C9LyNaXIL1oWyCFQY-DKRJcSLjXAHaDaRc0B3QEadrulnhodJ5Y8L-7k_5spWRIPRJVyzpnl5KFHold7jRTfdLZOE-ZkA79OT6xzT-02QPvVEjVL7LAEmeYH1888eJysq1Elxgp82xtVzGZO8lWW-3Ouhsvsj6iAderek--3te3ceS2Tp7e3F6Blob8iy73VLQ_AkDiOOUDajfpvP7FqaZfoayR7G1sxlUQlQz0IUfuFJr2RzsZkxLSeQnHiHAGpwZ9T3bKxWHW3RXBXMZ3En7Hj3d-uROy78A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ee0155b21.mp4?token=eWL3nGEdVj5sFM5JFzE-75vSPdxs1Wz1Sdog3s37ILSY8_lRmtZ1C9LyNaXIL1oWyCFQY-DKRJcSLjXAHaDaRc0B3QEadrulnhodJ5Y8L-7k_5spWRIPRJVyzpnl5KFHold7jRTfdLZOE-ZkA79OT6xzT-02QPvVEjVL7LAEmeYH1888eJysq1Elxgp82xtVzGZO8lWW-3Ouhsvsj6iAderek--3te3ceS2Tp7e3F6Blob8iy73VLQ_AkDiOOUDajfpvP7FqaZfoayR7G1sxlUQlQz0IUfuFJr2RzsZkxLSeQnHiHAGpwZ9T3bKxWHW3RXBXMZ3En7Hj3d-uROy78A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این چند تا پسر برنامه گذاشتن که مسافرت برن اردبیل رفیقشون میگه من چک دارم نمیتونم بیام ولی دوستاش هم از بس عاشقش بودن اینجوری بردنش:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70040" target="_blank">📅 16:54 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
