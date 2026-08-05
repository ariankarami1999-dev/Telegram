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
<img src="https://cdn4.telesco.pe/file/F1AsrPbt6E-Gt0wCfTemshiOAIm4-cT3_DH_clizxQu8jEIuwXndws6CGnx9dD7SXFptFF6E2tkfdE00NPDfbzFkr_VAq_waiz58IXqVSr6PP0KT-E-lP9IvMJVk1hMZpw1l2YF207LY7fOzNajqnvknrYH8quDxTmLqkZ-51ash2KM0bmcJEB5cL0-cZN-1n7Ph4nvaL__4Vq72Aiec0o8uiuu4r-Cn8GcH3SiFK-X2qE9ZOk8il8Sekn1UZte9l6_jOksjX319rOX_k1PXA9PzZlFxHZ_ImvzcwaW5nDfog_BY8Ewbl4aWuz4Zp7UaH2mK9Z-24iHCGjYrqTUx7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-7411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOyVhRnPQdlI6nthYNrf9gUvEA9vXMRlcQVajtLnbNa9WLSzrfvRn6S63cvJDOaywHUZQQKPPxnGohP5OxyE0fpwqZ4ePuAhcb3M5R0GFDHRHsFWroS29vztVinPjYmPWyxNJO7CsVYQa6DUBPFG8lDshxgjzP2OQLZWJBG6oVAyfSNTvsxhirTBq3j5k5wsL8qQ9xSfS1ao883_KcUr60AbPeTG3TCygiC-fPHM2S_g0zs53Yv8Hx1eCZRETnXF9aXVsXRcqIvjxirvrdRnsVPC-6aTHLXfxRuOPAjnL_VjmrpDemgj52IgkdW_tG1B4amRMsWvULC2A1-Upw93bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
۱ میلیارد توکن رایگان
🆓
تا ۱۲ آگوست
پلتفرم
InferX
یک کمپین محدود راه‌اندازی کرده و تا
۱۲ آگوست
امکان استفاده
رایگان
از برخی
مدل‌های هوش مصنوعی
را فراهم کرده است
💥
از جمله مدل‌های این طرح:
😐
DeepSeek V4 Flash
😐
Gemma 4 31B IT FP8
😐
Qwen 3.6 35B A3B FP8
و چند مدل دیگر
😍
طبق پنل سرویس، برخی از این مدل‌ها با هزینه
صفر دلار ($0)
برای ورودی و خروجی قابل استفاده هستند و می‌توانید آن‌ها را از طریق
API
سازگار با
OpenAI
در ابزارهایی مانند
OpenWebUI
،
OpenCode
،
KiloCode
،
Dify
،
Hermes Agent
و سایر پروژه‌ها به کار بگیرید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/ArchiveTell/7411" target="_blank">📅 12:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTMmoPAUEXSdmLvM7LL1buwYTw6V14tRez7pEKiTBVWfBTxawxAHrTx2Ggk55BBhI085tqKopYaPmlU99TAfdmJA5laoNVR5vokZu_B29ZtWf_de3FOpCuLKvXNoRsTdWLwJpU7AiKgtkgzKci4lKG0p_hEqLS2SCPb8dXlwSBIIgnvMLN4I_a7H9NYbUUEmAhgWv7KNCJo7kyMshWesRGvfGBHatWQIBlyzs7kBcQDfbzE_6M58tH_8h002IMUQnNg9K7ZWQYyw-XpPTHKnjxBYAK47IDVmSfl5umwESnzhjvsHfo1TYv2lyIAAbV-ffnwZcxiORsklXeKPLN_FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی CloudSSH؛ ترمینال قدرتمند Web SSH بر بستر کلادفلر
🎶
📱
پروژه متن‌باز
CloudSSH
یه ابزار Serverless و فوق‌العاده برای اتصال و مدیریت مستقیم سرورها از طریق مرورگره. این پروژه با استفاده از TCP Sockets در Cloudflare Workers، یه تجربه کم‌تاخیر و سریع از اتصال SSH رو ارائه می‌ده!
✨
خلاصه‌ای از ویژگی‌های جذاب:
🔒
کاملاً مستقل و امن:
پیاده‌سازی خالص SSH 2.0 با TypeScript (بدون نیاز به کتابخونه واسط) همراه با رمزنگاری اطلاعاتِ اتصال در مرورگر.
👆
رابط کاربری حرفه‌ای:
ترمینال سریع بر پایه (xterm.js + WebGL) با پشتیبانی از تب‌های همزمان (Multi-tab) و تم‌های متنوع.
📁
مدیریت فایل (SFTP):
رابط گرافیکی کامل برای آپلود، دانلود و مدیریت فایل‌ها با کشیدن و رها کردن (Drag & Drop).
☁️
همگام‌سازی ابری:
پشتیبانی از ورود با اکانت گیت‌هاب (OAuth) برای ذخیره امن کانفیگ سرورها.
🤷‍♂️
دستیار هوش مصنوعی:
پشتیبانی از API مدل‌های OpenAI برای کمک به تحلیل لاگ‌ها و اجرای دستورات لینوکسی (مثل Docker و systemctl).
🐙
لینک مخزن پروژه در گیت‌هاب
🌐
نسخه دموی آنلاین
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/ArchiveTell/7410" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ی پست ناب بریم
🔥
🔥</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/ArchiveTell/7408" target="_blank">📅 11:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb_GZic7G7b8_3Wr5FAC3Se5ntv0pn-Ps5GS66q8MxzpEWaf17UVRrcGPUlphAC-3l9kS-FkPBriT-wRI1PJ8NuzyLLU3JyACGvPGsl2mhULqgfJCTpqnrpwIlnH__NdWrllDzivYoWgDzqiXGBQz5dKQy-l6pDqEdS09zrAt2mOJ_MI0R-WHtN_zKAyrNyf2yzLpJ3Wzt0pI_dnrrsTZYA0LfsTbMnZppwnOqFkFgOiF3fAM7Hu1p5TLsK7wV69eA1uKV1k2AcwzKICqXpW9kMpZayUCmAc2isUPYdiCws4r9PZMYU-1DpLWpOLlnBhpilWHzlNxDsmpqgo-qXoSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#fun
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/ArchiveTell/7407" target="_blank">📅 11:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7406" target="_blank">📅 02:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=gF2h0O-ruqSoTcNvQ6W4QHN2H7MaRp1STWoIBL00yCHb4iBuKvOEO5IYB72B41d_oTt65pkknUmRBKpqO-GljWS7jHN9r8AZwxo1_BgHwi39eNpElZVPTwGHBehGFBBuoci4Q8MKNJPlmWbdfkl-Y61ONTuR8dQbYKiXA8_GlYwzW95x6cFbGQqQ6gQdLljOuNmmjHCt2Pto6ahRjT61TWznZwB9NE8-HHFXaJ1g6qCuxh5Y1DyEtekla6zPGz2Da1uXE8-nHXg5rUmxP3_5OJCScYUsBBi7lZVloIKW5rUUpsTZMpmxPfWTeu1bMmqSabvDYKoRULvE2AmiIukMVWIpVUiUrujOT6dRWkUz8QeKl8pbekoXqJjxDV0Tljx4EQuJXh-nzlg0xYl8bdB9jG6UYy1d1e-6Pz6whz4QNo7PWXFq0jBh7NzkYZQghwSie9-GX5vNlvbFD_hIlKMwIat-9AnNsHj26hlABmzTXH2MFtvJpAuvZVJQ9b7M75oBde_p-1u-W4IpQFZEwnFNwBG8Nqewfr9Pi6-Zv_97E9v4SFjK_pP9ANG-UZHPJ4tXO_LIYZDpd8hk8sXgArWFse1H5HRZLUtxvUXGc8Darc1ZOIx2azlLdNOYElG1dqSNzvw3s65aa2GGdVWsHCAJw7iAKsOqno2j4CQ0fa0XwRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d56fd43533.mp4?token=gF2h0O-ruqSoTcNvQ6W4QHN2H7MaRp1STWoIBL00yCHb4iBuKvOEO5IYB72B41d_oTt65pkknUmRBKpqO-GljWS7jHN9r8AZwxo1_BgHwi39eNpElZVPTwGHBehGFBBuoci4Q8MKNJPlmWbdfkl-Y61ONTuR8dQbYKiXA8_GlYwzW95x6cFbGQqQ6gQdLljOuNmmjHCt2Pto6ahRjT61TWznZwB9NE8-HHFXaJ1g6qCuxh5Y1DyEtekla6zPGz2Da1uXE8-nHXg5rUmxP3_5OJCScYUsBBi7lZVloIKW5rUUpsTZMpmxPfWTeu1bMmqSabvDYKoRULvE2AmiIukMVWIpVUiUrujOT6dRWkUz8QeKl8pbekoXqJjxDV0Tljx4EQuJXh-nzlg0xYl8bdB9jG6UYy1d1e-6Pz6whz4QNo7PWXFq0jBh7NzkYZQghwSie9-GX5vNlvbFD_hIlKMwIat-9AnNsHj26hlABmzTXH2MFtvJpAuvZVJQ9b7M75oBde_p-1u-W4IpQFZEwnFNwBG8Nqewfr9Pi6-Zv_97E9v4SFjK_pP9ANG-UZHPJ4tXO_LIYZDpd8hk8sXgArWFse1H5HRZLUtxvUXGc8Darc1ZOIx2azlLdNOYElG1dqSNzvw3s65aa2GGdVWsHCAJw7iAKsOqno2j4CQ0fa0XwRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7405" target="_blank">📅 02:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLyed3op8pxGM2jkDwfcjX65kAGua6NSPlN8EGG2r0Ts_OZOR5BCtYuDJ9QIKOunirMzMO_9Pa3NijJ2z_D-pUqqUxDkwCDpDPLIlaDnnllxQHLrThwxLGiPcvZgPpbB2XBU_f1uk7uWAZrU6ytM_65HcZwGBw3xBlDV7CEhrFGNhS0SKWkM0wH-E1zwpfYTTG3v8oY6I17R4HUOILlJllTG5hsmrRoQryfhng2H9bjifQbo1qDLF2XBpN3pFTcLh5iX--qYivU212HhpXApnW3BLd70pQKx-Odf92xYIc0VArDSIsFfFkWde7pmLdXpSvPLkcbsxkurmMAEu3S-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
500 دلار اعتبار رایگان API برای شما!
‏همین حالا کلید اختصاصی را دریافت کنید و از مدل‌های Opus 5 و Opus 4.8 لذت ببرید:
🚀
Api keys:
sk-2UddB27hnFA1z2LKWKnq6BQaffBLe86FU0htxAHm0Q9n5vjW
Base url:
https://agentrouter.org
Model:
claude-opus-5
|
claude-opus-4-8
✨
کلاینت های مجاز :
🔺
‌Claude Code⁩ | ‌VS Code⁩ | ‌OpenCode⁩ | ‌Hermes⁩ Agent | Qwen Code | Kilo Code | Cline | Roo Code | Open Claw
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7404" target="_blank">📅 01:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📥
پترنی ها آپدیت جدید داده
۲ ساعت پیش
چنج‌لاگشو ننوشته
https://github.com/patterniha/v2rayNG/releases/tag/2.3.2-P10
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7401" target="_blank">📅 01:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AChnqAktE76kXcKrk1Y_8GrAFOKUnhklkGdLPLMLL8trER72igx5dXvVB4Er5YvCMyVzwDakjphlKejyMeSPtSCe2iEJdlBFWATe-Vwv9-p96N8mAzpI1OX62E2GkldqAJgzx5TN3Pt-8fBIXdZ7cVeRxs52-UTmM3YFbxSpkQsNBcfWzto88DLg72MTj3XNIr0yWJBTuvyJw0l-V1YraXbvJbaCHkr1xnGWrqad4o_Qh11GDSR7CojsstlNVs1BG46-uTjrJmZI1Ed2ejdbmSZDIYkpdb_U3IqDnhL68LCrjVZtMG9oRdJZF7t2cOS1Io8cjgMkt1ucSnWah9DT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولت کلادفلر خودتون رو رزرو کنید
‼️
تنها کار باید برید یوزنیم بدید و به اکانتتون وصلش کنید
⏺
کلادفلر یه سرویس پرداخت و کیف پول برای ایجنت‌های AI معرفی کرده که بتونن خودشون API و محتوا بخرن. با سقف هزینه و محدودیت‌هایی که شما تعیین می‌کنید.
cloudflare.pay
❤
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7399" target="_blank">📅 00:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش تبدیل کردن صفحه چت سایت Qwen به API
🚀
اگر در موبایل هستید از
Kiwi Browser
استفاده کنید
‼️
✨
آموزش اجرا :
وارد سایت
chat.qwen.ai
بشید و یک حساب بسازید
در سیستم کلید F12 رو بزنید تا Developer mode واستون باز بشه
در اندروید از سه نقطه بالا سمت راست از منو گزینه Developer tools رو بزنید
وارد تب Application بشید و گزینه Local Storage رو پیدا کنید حالا کنار این گزینه یه مثلث هست بزنید روش و سایت qwen رو انتخاب کنید
یک جدول باز میشه و آخراش یه متغیر هست به نام Token اون فیلد روبروش کپی کنید یا توی کنسول این دستور رو بزنید خودکار کپی میشه
copy(localStorage.getItem('token'))
اینی که کپی کردید در اصل api keys هست ، ممکنه بعد چند روز منقضی بشه و دوباره باید بگیرید ، تمام حالا میتونید توی هر جایی که دوست دارید استفاده کنید
Base url:
https://qwen.aikit.club/v1
Model
:
qwen3.8-max
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7398" target="_blank">📅 20:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7397">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaZ1nWesngobmBdk2uxKgYx48DmvHEoLOdmm4OqbXSludOxhLIfhGF7X9lddsnF3T3eUbdBQtuOdu67bXOxr01fnb23pVE-NFFU1x6R5Zj_BI02JJmtGMEy9UkB6rQ64CZeAynem65kS8hBeX8GlGiTATn2cVCXnibsnSI-sfTPZmLK98495RSS4B7X5owfGlt8aps535Pru6RDDTeiqvK0gaQBmp8P2CKuptcq9TrFEYNTXpXM5fNJhg5XaSyo8z1D-IVUSRZYrBzTfGP03wFsJ50C4t_1dcTl38WsHSZDRxtuylcKKDPbSELXVFw1ky-DS-RanVI_5s3z0zHDh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩
‏وارد سایت ‌
Cline⁩
بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند
این سایت
‏حالا توی ترمینال، ‌Cline CLI⁩ رو نصب کنید:
‌npm i -g cline⁩
‏با دستور ‌
cline⁩
اجرا و لاگین کنید و لذت ببرید!
💻
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7397" target="_blank">📅 18:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url: https://www.fastaitoken.com/v1  Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471  Model: claude-opus-5 Model: claude-fable-5  دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7394" target="_blank">📅 16:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه پست تند و تیز داریم
🔥
Base url:
https://www.fastaitoken.com/v1
Api keys: sk-1acd2bba8f138537e2f5405f983933dcbe1c16042abe5ba2621fcbf8a1fed471
Model: claude-opus-5
Model: claude-fable-5
دسترسی نامحدود به مدت نیم ساعت تا یک ساعت
⏳
فاتحش خونده شد
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7393" target="_blank">📅 16:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro
همچنین دارای چند مدل رایگان
:
GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3
به
این سایت
برید یک حساب بسازید و با تلگرام وریفای کنید و لذت ببرید
✨
قابل استفاده در
Vega Agent
✅
📍
Base url:
https://anymodel.org/v1
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7392" target="_blank">📅 16:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgivddpOfxwC9S4LV_XyQDT7Pt9KTB9z90WbFroMGf9et3Kq_smMlSFT2_kYqYOQhvfhQlY3SrW2qn0jfz-Byzsb_ZYvaJ3FRWwbkbOd4JA7s4PEOfvW0xsm902RnTgQ7bA8vUZl_WiD9YB1Ipa0m7H-Wl2wHVHJOqUasaSZbZ_Eb_zbwwnKKWRSOObIvnLnuo2Z1THaxatDoCF6agz7OndzEJDEUA4aNnTOl5iC-cTrb7SEpqQ_sn7xSL0G3qNflHPNyOEqyCnckA_9MIzvThOc-J9qOlVmQaERm3WX9ARMLt-8iUo7P8zDnOI_Eh0OY-XZgWNO035cbuR_ouSEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏100 کریدیت روزانه برای حرفه‌ای‌ترین مدل‌های ساخت عکس و ویدیو!
🎨
🎥
‏بدون دردسر و کاملاً رایگان؛ فقط کافیه وارد سایت بشی و با کلیک روی پروفایل بالا سمت راست، اکانت خودت رو بسازی و از قابلیت‌های بی‌نظیرش استفاده کنی.
📧
✨
🔗
‌
https://www.creen.ai
⁩
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7391" target="_blank">📅 14:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szqhsmqcpoMVlOb8DU-T3RWgc-y6-xYIVcRCZUTN2aqem3RS37DVJA6Qr1r0_0g6J_UycTXz0DN5ci-T7MRf576TZEPO3w3TOpEjMmR9W_rose4IDqP7FLk8yVtWUF5T7ChZOSplzO6q0rPg_WbATHJsjyn8-0761eiFFlCr7NHdU4a_YExM4Ur3WfKvqbNLFUoaTS-jKAnoQGXfQYb5WMbKS0GMvf_P7r890H2vLM8EEKSJLmXDrdH6lBWnqbd9mhQrgjy8I_sB-94ptv6KZBQcgMenb8WRZRLALyQxGUfoD5HPLjkLC8JzrrOSquWevlEgk1truntDLAZS2GuROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دسترسی رایگان به Canva Business
🔥
از طریق
لینک دعوت
به تیم، وارد شوید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7389" target="_blank">📅 12:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آیپی تمیز کلودفلر
92.53.191.134
66.225.252.96
104.18.14.224
104.25.247.228
104.17.2.54
176.124.223.242
104.16.122.178
188.244.122.16
104.20.14.15
185.148.104.192
104.24.152.74
104.18.2.152
104.27.24.70
154.211.8.196
104.17.88.93
74.49.214.92
195.85.23.208
172.67.114.81
92.53.188.13
104.18.198.203
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7388" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U38e3TxFbmxZjzH9qc0D4fH85hbFPPV8vAtiUmyUppwoUhNEDUSKm4VURfa9zom2WT69aIrback4SQho7w-3XImH9gUVlwc7-ra3lmB1pmKLECBkU_NLRJ4B3MSGrbNzbk2dD5xZvvcbj8g8h4WSjnLucJHo1ghfIJ6glOCSSSfOobxjiP8ahr4i7fsy8dkM3j2eAvpr7W0QpWgadFPaTEndJebkb80JqxxkaVqehyY59FqPVrCs5WAUNv8pvoMOLMvt3XWib2iU5zOniSIgMqJDAYPU0asugPFT_kNZ3ZHaaz9zsiR6UxyTkjW7z6oqRNJd44VkiPTk6Mz7dTQ9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تولید محتوای بصری بدون محدودیت!
‏دیگر نگران محدودیت‌های اعتباری یا کارت‌های بانکی نباشید. با این ابزار قدرتمند، می‌توانید بی‌نهایت عکس باکیفیت و ویدیوهای ۵ ثانیه‌ای جذاب خلق کنید.
🎨
‏
🔺
تولید نامحدود ویدیوهای ۵ ثانیه‌ای
‏
🔺
خروجی عکس با کیفیت بالا
‏
🔺
بدون نیاز به کارت بانکی و پرداخت
‏
🔺
رابط کاربری ساده و بدون محدودیت‌
🔗
https://zsky.ai/create
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7387" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بسیار عالی
ظاهرا سرورم دیگه پینگ نمیده
بوی خوبی نمیاد</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7386" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqFZaXiVapKxkN-W7g_LIkPwOy0_gByFkp_SZ71wqzTh16HQk_cXLO4uZqd5tyjkDYTVwHJLtYvlVKlZYFRQyLlwk1MBiJuhwTdxzHUSGlYZgFhTcJSwvq7s5WfFqN4jJhSL13vrLomHY_yeBdZq9c20uaDbhCaCHxHPOS_vXAbufHAAN2Vzw3wT6uJG4KAVvCRbaNCUFG-p49HbAwMqAiE2P5zAsXJSHx4M8mS_BF0iM5G-XBfSJFdohQVtVi_CL-gkulq4aAPPZv7ABUlm2j4cdeZAT7qSI906JorrLJSmP8Zc7ASbiusyAHh1VvIkHnudp6bQgzN2g9CHord1Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7385" target="_blank">📅 18:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnZ-acHSpuaEa3wEMqIaZOGvXv7ZYGjJOA59gYoy3QTIuVK2SdCNef68IdUOsZocrECzDeO99Kh1YkXC_Xke4XFMQam7c5vAiibpkKkqpKx9BLhwEy6N0aoXJKQtyMX8982z7y8xasUGzqZn4A7HMB7muu0Hbu8X2pXTiT46B2kdOLz8TBBTfPU_3Uz5bvYd4-zM6mQ1psZdH5DtYOZ1dKoZVy5NoEl7JXkgao2uL8_P2QyUVCYYJ3jU2LZxlg7Bp6bP_lWJRDY3vkH_2epaDYcoAOB0E9IWDhU8NSK53nKuPfBsJdn_sbHxwmwbNUKMdk1HtUEY4zYvogdHRF3FXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
دانلود و پخش آنلاین موسیقی با فرمت FLAC
🔗
http://1music.cc/
😀
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7384" target="_blank">📅 18:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوستان اپلود کی ضعیفه رو ایرانسل بهم پیام بده پیوی
اگه حوصله تست دارین پیام بدین</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7381" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg3r9LABRa4zubmG-bVP5tdHSIX020STnjBg-j_McPIBWZMoE9uj3k_tB-l77N3pem2-6NTpQyPwDSmTAB8gFZ3oVHsY_bzu8c5ihuw_fuXT1cMO2HR46XnyvLv1YwAKnGYmu0cSbc1i6BZdVxQCO503hMSm2U_8-JOITgelP9cAiPKG3ZgaE6WBufH69mnycTURba6tpph8I-Yo8llcWhKiL-jnOekb0Ft4KATaZv2Qs04ExLZk5ALtcNduQbEP1KCR0QCJeLqDez0fua0nbkVtsI91pnvIe97784ar722b7AtSiPNeyxQAqcC_1qulOAI5MioLO-Cf4Pelk_dcnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7380" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSpLrO24bbf6gWFfYRri3hIgFTTxTEhrBDcrZAunLCdwIicM06MfWJjm4dSYZxaITxxLUrRVWSqAhI5lA4wgt1vPlqlhcTl0bZp_7xYsRHnishL5AtTCexcAelvcbh8_TYUjq_elrBRLxZd1H39_1UaE1uitEp7pk38WanwPZTKBt7mZpXzULYiaXuQRQXL18wYh4wyOSJAwyAFGHmAfjxIgInApWq8VqQMFmaK--M0xHz3qD1eJIwKjxIZu0Ybf_8xn4Lg8o97nB-wOe3oqQu-pdxzm11we7wZ1ODK08cppyVDgvqcdyAAt7H6hFbu5KknXyjcM9w49cOPrzEGnhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7379" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=IwLRWxynfXGnqcUzL7Ysdu1XYF3WD6xZ_bQYAt-Wkhp61xInoULMrJ_lPcBvJvDNKODI4zaOR7wq3djY9wVrn0_Gv6n1XPhPKrO97hc3BejXHM_pt5bTjHJ3btsMKQXx8o3c_57OhWyE-lks5jNwHiYZPzouUOg00o3a3nv6nyFAZ62qlwR0j7JCm7fzB70g3Z2wgGa9doH6bByH_VRWJRYSIHKPiNkH2HZVVcsT84-0AKVuaZUwmtdZ-APPRh3VNjpsyLd-H8xGEsYoshDfhjJrUMOGzuLbAVElcjraLXimL-44tqHNSvDZPr9vpI9o6BKQTT9-kW7t-D_B4felYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f36f0f9.mp4?token=IwLRWxynfXGnqcUzL7Ysdu1XYF3WD6xZ_bQYAt-Wkhp61xInoULMrJ_lPcBvJvDNKODI4zaOR7wq3djY9wVrn0_Gv6n1XPhPKrO97hc3BejXHM_pt5bTjHJ3btsMKQXx8o3c_57OhWyE-lks5jNwHiYZPzouUOg00o3a3nv6nyFAZ62qlwR0j7JCm7fzB70g3Z2wgGa9doH6bByH_VRWJRYSIHKPiNkH2HZVVcsT84-0AKVuaZUwmtdZ-APPRh3VNjpsyLd-H8xGEsYoshDfhjJrUMOGzuLbAVElcjraLXimL-44tqHNSvDZPr9vpI9o6BKQTT9-kW7t-D_B4felYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7378" target="_blank">📅 15:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7372">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7372" target="_blank">📅 12:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=cxsaJsgNCjwcKVvhmJ7Ouba-t0nOr1mTCNH95Gzo4Cvp9ni-AOiXetqQWz8TOqSWuTeQuLPPnWkTrMsC22enx-KrYQagw4pjnID4SsCiorn5taj4eFabl6EelqyuXLP-a9V4aVjjJNjagMmWRCWxPQl-DimUs1aOyKwLOQnqicEjjM0ggT8kdUuLD3OP-DtAppm4Jp9I7I23inlIAyQrxSbFGPWTctRzxIv1AMtFqhQe9aTQONF6QtTM9FBP5pHe-9ofbXfoWoILQo-JCv9nOP3wqAMN1-hvqwn_pt2yUoF6rkekGuJlm8eQWhJ-qgDurlONb5L2DUfudJRE5VB4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d804f72.mp4?token=cxsaJsgNCjwcKVvhmJ7Ouba-t0nOr1mTCNH95Gzo4Cvp9ni-AOiXetqQWz8TOqSWuTeQuLPPnWkTrMsC22enx-KrYQagw4pjnID4SsCiorn5taj4eFabl6EelqyuXLP-a9V4aVjjJNjagMmWRCWxPQl-DimUs1aOyKwLOQnqicEjjM0ggT8kdUuLD3OP-DtAppm4Jp9I7I23inlIAyQrxSbFGPWTctRzxIv1AMtFqhQe9aTQONF6QtTM9FBP5pHe-9ofbXfoWoILQo-JCv9nOP3wqAMN1-hvqwn_pt2yUoF6rkekGuJlm8eQWhJ-qgDurlONb5L2DUfudJRE5VB4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7371" target="_blank">📅 12:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7370">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7370" target="_blank">📅 11:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7369">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJrjTlF3FaZvTcnURXsWZ_HslJbdGM8AGah6sFV8lnzZUQRLHLK_YMPcB1l4yMMIwkU8JapECb49xy6MNBce8rnxHDKIdUY99UBoV1Qt9bvPFPqXo0gP_HG52fPYU8XNE9JmrvmUKEpWBqb8DLU5Iu8YT0pILOy7clg3MsCYrF1oEiy9cYzXn3e7iX8exU-LIao8T5W5yhQw2BZZKXRzd4uFZ1r9u--VbH0eGFfuJldT1t6qvSGE4ejcrh6fDSz0UfNoIVPSUhOLnPO899_5co5MSR__Q5VFpFC2XofNpyDFM6sBm1YBt5pBGmOIUsAuDBzzVfLzVEPLExJhhzIxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک های Qwen3.8-Max
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7369" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=IvNsN766ZUZECGtiGG1gUZfvvc9pvZ2uJs9vxhRFrqHZorlYtVx3EmN21n6ZoT0HBc9aKS1jXhDbkHhHWmfR5Ezk1rTuIcALEZo2PxKYZkN07EcGnp8HPsIMmxUwecByddoBam9sq05BKH-jGMpy_5qG-xeLtis5iq-J6B4rDARfj1L-JpYUlhKTlbfyZQvOyoO2wayWIM8FYBKb3dwkXpNwm4NstpSwCDhrvDfbguK3EqUz2Sz1-oRk3Ehtq6ygiSbUvzOe-HRi9uFdla_XzOfKHCBJnq6bc7OSVJZaWVWf-pJBIDeGA2ib3WiUAuO53e2ZKZKhQ9yXov0gd9Q6DSuSyngAgoZhacYPbaG5Ph9Ht_Q8CSjNbVYLQhTXQac_VPcAHFhQNAphjQxOgCGaaRKw0hq1_VAh00DM-q1uyNnVT73JAz8cBW46FgD7yl5RHlNLSS5zJtO69J1AU0A5eUC6_76-eOvMvrDQIVPiVqbRNujTzeafK5jJO7aAt5wmwC-E9zCu4g6jkdbyzsrEY8US5DUJ5rg2IkU24JJpxi4r_H04-Ajx_fmsymPaMPW3oaJOGEGWOcgdpepwgMTEmtUJz6ctkUdtLfurPeRnpSGeGete7qrExIN5Uq4cirDYfRUvGU352VKCfoZgO4pp_nSxtmb95wEHiOkIEVBua74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e11c84dd8.mp4?token=IvNsN766ZUZECGtiGG1gUZfvvc9pvZ2uJs9vxhRFrqHZorlYtVx3EmN21n6ZoT0HBc9aKS1jXhDbkHhHWmfR5Ezk1rTuIcALEZo2PxKYZkN07EcGnp8HPsIMmxUwecByddoBam9sq05BKH-jGMpy_5qG-xeLtis5iq-J6B4rDARfj1L-JpYUlhKTlbfyZQvOyoO2wayWIM8FYBKb3dwkXpNwm4NstpSwCDhrvDfbguK3EqUz2Sz1-oRk3Ehtq6ygiSbUvzOe-HRi9uFdla_XzOfKHCBJnq6bc7OSVJZaWVWf-pJBIDeGA2ib3WiUAuO53e2ZKZKhQ9yXov0gd9Q6DSuSyngAgoZhacYPbaG5Ph9Ht_Q8CSjNbVYLQhTXQac_VPcAHFhQNAphjQxOgCGaaRKw0hq1_VAh00DM-q1uyNnVT73JAz8cBW46FgD7yl5RHlNLSS5zJtO69J1AU0A5eUC6_76-eOvMvrDQIVPiVqbRNujTzeafK5jJO7aAt5wmwC-E9zCu4g6jkdbyzsrEY8US5DUJ5rg2IkU24JJpxi4r_H04-Ajx_fmsymPaMPW3oaJOGEGWOcgdpepwgMTEmtUJz6ctkUdtLfurPeRnpSGeGete7qrExIN5Uq4cirDYfRUvGU352VKCfoZgO4pp_nSxtmb95wEHiOkIEVBua74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم Qwen مدل
Qwen3.8-Max
را معرفی کرد، بزرگترین و پیشرفته‌ترین مدل خود تا به امروز، با ۲.۴ تریلیون پارامتر.
تغییر اصلی در این مدل، توانایی کارکرد مستقل برای مدت طولانی است. این مدل قادر است یک پوشه خالی را بردارد و یک پروژه کد کامل را تا مرحله تولید، بدون دخالت انسانی، پیاده‌سازی کند. علاوه بر این، این مدل می‌تواند وظایف طولانی‌مدت که نیازمند برنامه‌ریزی هستند را مدیریت کند و از بازخورد بصری برای تصحیح خود در زمان واقعی، در حین کار، استفاده می‌کند.
هفته آینده، این مدل به همراه یک نسخه سبک‌تر (27B) به صورت متن باز برای عموم منتشر خواهد شد. برای کاربرانی که از API استفاده می‌کنند، هزینه پردازش ورودی ۲ دلار به ازای هر میلیون توکن و هزینه خروجی ۶ دلار به ازای هر میلیون توکن است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7368" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7367">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7367" target="_blank">📅 02:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7365">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7365" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA1wXqi17LjmY-Uuiv1IS9OIxMwUzbDYkvoDujMZtD2Hz_Ujy4giva9BTQcYWu-RB6wVfIHyHvcRV-noKsqC7ed4O_zxP7c-1AmP_jCaacgwBLDIkWIX1FVVpUFRTXmTDMbAgeAFG7KM4-aCgXMfZ6LpGZtd79BuyPOEpSuggCv_736KQVfUYLjZKcXGqfuTNArJDM8tu6ALPqW9fwRrPmxrrOL5Ji62eQt5aBePKbKjY-qr8HK0RiMVLUu--zeYYFNH4gKylCzNHkJFgyPD4yao4bFA6evnRWC0oZ7AxzI0e59nEage4JaG8ho7Qr-Et9vVwW_Jl9vdBH8sFQwUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از DeepSeek Flash جدید هم پشتیبانی می‌کنه و طبق چیزی که دیدم، تا ۵۵ سشن رایگان در اختیار کاربر می‌ذاره. منم باهاش تست کردم و واقعاً سشنش خیلی خوب جواب داد و هنوز به محدودیتش نخوردم
✅
حتی GPT-5.6 هم بین مدل‌هاش هست
😺
👩‍💻
نصب نسخه CLI : npm i -g freebuff…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7364" target="_blank">📅 22:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7363">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7363" target="_blank">📅 21:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7362" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7361">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نظرتون درمورد فرار از زندان جمینای فلش 3.5؟
😀
🔥
❤️‍🔥
👇
یکم انرژی بدین و دوستاتون رو بیارین تا پستشو بذاریم</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7361" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqk9JUGv6GxZsd8de9BlceS3FQipRYBORePO5OZhlAMuJTOIYagDYjEk9NyDkAacnBcmVTTZbOA7HZf6YRd1AwfQhuhvue3ibbBDscNsIiKl_scRzaJ1dCeLs7b7lavnkj6S2kX-8QQv8yCBDWjAFU3jA9V0cJUujoY7GUBspSuhMrIm0VZlzarOeb7w_SVnYnH9zgjSd1yN_qSByygkvPRyqEvahf2YBaIneoc5lg-sMtfQggBetO8PZjG_B7Ja5A0reHavImtSrVqJCG31dJBE6nx5T3kuLOdinI6KTwd4iyM7fndGgtDaNYjrs4-Hm2e-5EpvwmJLezeavuP3ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7360" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PITswzGCKrO0m-lIPepz4370MPKhm6ql9-qYACF2cnBjn28gzQNr-Ko6Q6J1cKog1O2GcbYnoy02jTdvSwpJsMQnMwZryrgj7zE9OYxjMAc1E3DYicHPyQTVzRoRgGOjE9p41VabJrn23jPnTziSAVpmgPMSb3TM7ri_Re0pJCaidHd4vC-FU-rkuKEc9FR7rK2f81Pwr1nQxE1_E9H8nhreC99nHcP4u0_FqsWcRSbR614ods4CKGj6jBW75i02S4JoyoKI7yOgNDY0Qk9rK6DgFfWQDX2nTbtWMcje6rWOJ5rfuERWQPOtah6jL2SydYwmhOVXN47j-N7o55TuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 2900 کریدیت رایگان برای بهترین مدل های هوش مصنوعی
🚀
Fable 5 | GPT 5.6 sol | Sonnet 5 | GLM 5.2
آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7359" target="_blank">📅 17:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یکی از اون متد باحالامون نشه ؟
😁</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7358" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7357">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7357" target="_blank">📅 13:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIZUXUbMsNWL2Ji4PSSB1ABefs3qDCXPw5_E3vOQv5LrS8QHZ9y7f66EMCxDpAMN_047iB7taUTdJrz-L2ljSPzZxWjZ2gmFR12WXxcQy1uH9WpBJJ5gf_eqXRGtpkdSo3rWa7s6g0g-VGZ2RA9QruMdx4YqWTpGjm6KEuvjsY9gNYst6WB6AsiL_cFBfJOJI9_fTTSe4Em3EjgQZwyCe-6KSAp5Aeh1sI0a5VEgKIQKy0LT1w7jfj1N4mnjzXbE9KVc15Ehk95ItqAYBzJqQ55a9x6LhYtnGYlQ3D_pQB6VlzI7_ooHpMYYqJ27HOvZDZ9upk-5NI4fVIPNWnB_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پز نیست
سبک زندگیمه
🗿
جهت دریافت کانفیگ پرسرعت بر بستر کلودفلر عدد ۱ رو کامنت کنین
😎
😂
(شوخی)
متوجه مشکل آپلود شدم و کلی چیزای دیگ
ایشالا رونمایی میشه فردا بصورت کاملا رایگان</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7356" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhxxUJdP3kwjc0H6Eky9S0aJhPqUAstRirPRu7sQGcZZnOXC2tqiVCad7MX2udIsqYg-QxONHaaGWgCA_gI6cPSpF6CPsrc6lD3JM2wqslGgF9Va7BdjCUX0n7s0dJdvR05mXAzH6v1eAoV9cP9vjWVUthU0h-SVh1hk3XDPMgrHgvFqpABgFHfWxNzUxD8KPt8cZewdR4IPJO51Quwv8IOK5J-JoKmZs8t50SsFTaTnGWZ95ZEbAikD0DYxwfJixOo-ke_Am-Lo93zToIYXZ8RGyAtbKDnpADSZaMucL0h_ytqDx9oxTjV6RpAqV8kj7EDbrlkOaEgM8ceVe5Erag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7355" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVhk6R-rURBsZOlufeApbJNu9K0Tf5EJ-bwd6gEqtG_-aQhvAK8lSuSZg9E-ETd9FtMNmNgXoCWgGaR8o7EU69tL6iRj8BmVo9k5H36aFqiLvqrOiwyjV4q5oGr5u84hJwb5KPq-zeZS9rjkYRDbq0VkoggwI-6y_SJbmljv66XgU2_tafm4Jk84Mo_joV-cIRggXB5TtWc9KszXXy7Y7qHsz177HQSxr7E_t-J7MSG7m4TMuYAkvfNrgkGZiVCbhNr_bHI3okr72payArmIDUQZaFzesaaOOQg6gKypDXf5-w-vmet9lx3ktqg5lPC_QdbW98uh5RkeBzr1neJ8Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7354" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYiBmvpbsGE58_TqkETcUVS3yYVjJJI3vepoCtiQ8WHQXqnAImymGb3ABhPSjp0Wzx464DQTCBHtAvVTXTQw3jPTxYh2mBcROkF8YA1-lSjrD_fDRXtkxvLuBH1L6kUwGfpyu4_G_Vb84plrCKuHBiXuhl9ECOxVyYQVS3zbELl6Qqid4vywk-IYgZ9vzDbNUx3JMC8BPoRBAzpR1RI7kStytHnOGHPIwIF8XB7HnURS_VqovKaHlAkCUcQlA-eckVdQrZy-zwXC3e0kMvUiuYin5h_jZwFBU-yqjDKx6xaC732gtPwSS30EX8rcFAmrm7mZ5m0DQEXWoxIqWk5Fyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7353" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvXQGfkVQf6O0_Zr19C2hSuer9Orca0-ISCqSkYF2wJLYl-M4ip2Y4YL__8cNMRdptx9qtYP8JyScPbnkgq5H6zmVWM95NiBN7v3ss02jXMoqmgqlw9IbD8f2wc1rOJKl_vDjQJAOGA4eg3r8Jxdx_Hy8SULDQxsBJxqPL7_hj1zVSkUz-M7z6Ol6EvcWydvu7PexSNv9wA6R53HXoYRMwN_3zvgE8iimif6MYVZ8fxZ4c24y3EEpmei334IOJ7CY0ZO-lf-cNMuILksfvV0q2-k7D2ymacEcG2qsJMp7l3hi7q543EUcOJ5RL2Z3wxspfMYWnzLPPrspUui8lJiYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7352" target="_blank">📅 17:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBQMtu2aIAobgb6GZa6csgVgDZpjTr8Rl6JEkwZPbv2JGKmfnOm4quef9CY-nTvx23SyM0IivL_SJCBOg6RX0p7HDATs8FTIvTcA9vkutYCIOAHEnVMZslgRJLHw_V_MySoQoWxv8u6kVNho71DLUKZcJ2CNIYLDl4K0rQehFxjY--FNZIkj88O0CCNXXTaNt7hvU5VitKC6udo1gqBZp7ThXVqJQ33ZA-KwmXUg86GTN2_S5cRBFTHFsHJ6X7Gzi8yQkLFdnt7U__DK0VntUfl9abExQBGTORoLyogSEC8dw0uEvmKmQuHHCkmL5zCAbOX03WCyzitAjM1NgfD9Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7351" target="_blank">📅 15:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7350">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWdo6wZgwAkLv8FyhiHPHoVoceOXLZ_nBKrzKEgiV4pFOKEXdqyecFA19Zt6y5TiBTYf0GRPg_Q2NGJCWn7_e1mfql_ArrBjCEgQva8pDSk-O2CySCMuu36t2jvzR2VKx0vaM7f5BPXnS-O22076T1_pGaOvnZJiQFS8cd4K-Xvb6mGClEBmNNexwpOo_4pA_02xw120jZleSFTmsg24NzIH5Px0xZfLY-DeM-_H07bg4FoPvlVOPq8jHf3p_oXxA2M8oPV136TtQbAEb6AmAFEOimRmx2kxj0X0acTG32ndK4g7EUA6gIumaoK7U6oh2XIy-JHeT9cPRYR-JjW3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 8000 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7349" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7348">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
50 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  Sonnet 5 | Mimo v2.5 Pro | Nemotron Uitra 3 | Minimax m3 | Gemini 3.6 flash | Deepseek 4 flash | Sonnet 4.6 | Haiku 4.5   برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق این لینک وارد شید
✅
…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7348" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7347">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihi8-Q3BEUaa4T81N4bK08XOweMhUH-JDInXesqo5MpbJYZn8_iyp9vVqzZrfmdSQNDqj-fdLCikg5l7BbfJj7kXYqcIQvj3OQqf4HtOensb4OqPb-30hGYkSAvMb_lbIFy1OOM_qfgzyY1XYmiNxT_QNrXY8c5O6pS7cQN3PIa5GMcqsUWhzIXlgUs7U3n13Wx3WvjUGOmtEkhB1-IeF1W_8Qa617mRqvDm4RYpUaNcPBJByS4o6-0HCOhK90DGCteAs_9iV_tXcYGo7cNBUKDFtAXMe-MOnLgI_eoomTB4RNur4ha_adzagymo7QLWA56kBvuSie5wC1BqUtnboA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7347" target="_blank">📅 12:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7346">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1O2iwEZ2QHA8h5weuKhYoviiUG3GxvIzMUv2q3ky8UgTsG0iU2HGrUPSVhCTc5pooTfMJvAcc9jHdm2lLWxpNBm4Modcx0ykE9MUzvNWG11uzCfPBcTamOFzmPLAUPyRR_0d3TuoZtLMYoPe8fCKciJkoN63oLZBrfZAumuwcM-SX-jBvc_wmhpkiT8vSXJEIS_W46X5WUjH7xJ9jNIqHtehQAKP4OVhYkHFe7MD6H03ocRDqhSPD-NywUf3seyA0ZKmN4_2ZAFtaZcZGZ86vpzSqEKMzvO1FEBTO57j89wbqtEtTuoItQBt_2BTncY3EHvDr_xDZZA4njiXOHkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن 1200 اعتبار برای ساخت تصویر و ویدیو
🚀
دارای تمامی مدل ها
☑️
دیدن آموزش فعال‌سازی ( کلیک کنید )
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7346" target="_blank">📅 10:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP2GnPjntpGE261x30whMlRjyLVI0bcPqafUexCy8AfpVuBV-Q7EaRYuERQUw7DtX1E_nyYDBm4gnQdxz718_wagGJtdthj_CBqCBqeUjIANUbt7m3go_P2fssKhfgEAxY1GuyOTrvLW-aBOcLFMrLnzV0DlnVfl55oAAZ-9Pjw0_YrCXpY2rfjoLgoPVGOociYWf9DmXqNZm3ofs1fGL7QIzkcvGAigV3JS1pla93pKS949vhD0ig4LbBh5g0MnPD1xW41tgXRcg6H3HsPzE0d8J2agvJxGblr2Pkdb-C7GF_JEywX8UhBavtIWCJEqBxvWIqDQ1WEy5YjrSA8wJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkQB_c2Du4fLjNWS-cnXUSdN32BWShU45LcQp_f1jslmy3HWWIn_8inIGMcj10yUkWcHIKjD6HV7kftm3u6G0cc93r4TH7MnptVkQHXvm9KfVluoVXq9QV7ebTbJwkW5hfeBp2chL6lgBFltpj9TYlqrAbym-jdOADnba4M-kGekbmudBE7GFzlOOj9_zBN4AQU4zEn30fic1FA-cKv9GrKwzjlhJbZZCY3gSkLrBHnTbb88m8OmJGYo6l6HjJtc4_s-WSaCeoTV_bUHQIW_TZl3CKE2j_aWsre54URckKzfwHwcWL-4Woq91caoHSlMwqGAawh_Zff95brrvVBN9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7344" target="_blank">📅 23:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به زودی تا دقایقی دیگر ی آموزش میذارم که فکر کنم تا الان جایی ندیدین</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7343" target="_blank">📅 23:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7338">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9QE45yVDcgm2yOyv_Mxr-Bfg9_2IMMeyei1nM7H1fjM_P_bJNCO5ZGz7xd7pPRAIbJATH4X97Vvb7bGoab280EFQ0sHit2AYJwQLgR6s-Zg5l0JEv0ljDNjwC2ywvVEFRcd6v2YSvgzlqAqPKFt-2aNGfTN9vuZHtMuPhoDCR-aAzOjMCQZ-T3fPi-fUAOXjeEd4TKHOjjVpQHb_yYI6rCRJMG-I08yyBwp1L0u9QRcsfrxqdtS6V5z4Q5OpJoaF1caWIic51Miw9CAu_R2J2RorzbSsIEmFECtBWE_N6MmoSKGNJyxrwXmeAKAvSQsejnpD15hX7yygV3rZq_zzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/so60M-LgMVKYMHhBFG7ixY1ZMD-lXMsXK6snBg6NUxS0KCpxKWvW9IVAhDbmDIme7cVC-CEgLOLdBPajlCecthYrrW4OAGtbTCNv6vIml9vYnMNEQtOm2baB2gDhvvEdj2b-HEtZItEKcC0JNJDcwy4r1MOHdO4sCGabmDmCdgG2BYEb-YpADKLbjirtUdQ47EMfcy63Ub0Up1Ki1LrD-67gE7M_x1iqDYg3VEGktycV8UIFKMxeXJqAdtXjsh0AqPYQBRxyqyJ-tt-VC0y2HXHCULDHAhMuMb7vEYrhVrNt1K9Y2BzRaoLs8CtkLG-jH2mR-wI37lXYotwS-ctf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9vUwjb748a2muepisZq1gjF1uWXAwHwDndGt_FiulBcY4IfdSz3q-JHEGe8D_jXEhAtojqvvS4t_8Nw0RYyfBtOKdT0Zdfnpv1TnP5j37LZ9QVn4xX8y0F0PxmLk1CZF6P--KgUcPtAZvLMkyzsCvm8Lh8AowYmCDvZtVAbDM6acXjeezh1JkoQLlZNOuQvqigO1OCq-yOebgMZdfve-2fARMCJyJaG2SGDI3qsN9Qv4B9nslDYGr0h6-x7QqXiTqjkV-ADSrofezsZgNf9-qz5-YYzqyPGF3ZmtrdusQjtHSf-7vjutOdy2kQOSwH63DAv2TS2iyVp2zbr9Le_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEBOYLNFwhcNKObO0Fjtyr5TBZhRZzy8ZghZZEsfK92Bt0Af1NCw3-PvJgpPnCAgVt73TqvnkpcwLOQw5Wu9Lb9Zu8jzQ7lnPnW7mKnZgvXCE6bxC3xmDiEgsWoy1sk0E1Om3Km_Whu15XVdJfk8nCtAZfD8qrdAmAxPcPy-InYxnIevXJX4KTlPe0Ar48LGagZT_YRfI4KYTpan4JMounc_kPqft1uzVbl7ybcf5umKZSBmIWLnwE_jkJe19V1Wv_ojVWNJ1bnjvYelXlr9AqPTuRZGWXOIkqf3ybt2KKM-pHXXvco0m4075zgd6jmyvv079pljfQza-AAIWmhQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3NfDH04ZpQV_QquHzrlM4QVEyvLuJxdFB2hwavm1ktcPFSrGhNtl9GuwFDO1YnXTSPXDLYqL4m_ZEhG9ZW2_hZGmWP2GG-2EvwajQgyl4n0uup6taoApVgf-Tkma8WWcD0-nujPTMpOJyYZCc_2N5rZy3-msqD27MPK3QRKC-82HqVjJvpnDRCLVydARvhmccrpfTUPu0yKYwToHpvAwODb2QfYN-tFeE9KqEfVLmWMVMWrL-c5Au1of8L90wR7bfWFkaUJtel2LRbwGVqVnpvIz2gXSYADUqsp2Q7U8Ik9jN1PbQdik8qBdCFKm2BbQI1cUyjo_jG255-ik50lRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7338" target="_blank">📅 21:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7337">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7337" target="_blank">📅 21:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بالا باشین بچه ها عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7334" target="_blank">📅 21:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بالا باشین بچه ها
عمو وگاس قاقالیلی اورده</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7333" target="_blank">📅 21:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLCZ5VkpC1X43EQNOgLkQ8EkDP9gbc2KiUjQ1D4pwuSQDvfTG3toPKmqib3QAaSfTiPtyYqvTTe5kdHT-29fPxAX6pYf1_uWbISOWdY64d2tOIOh583qzGle6ud99weageY1FItzvOj1NyIQxVFBO_w54sgJ7kpow0KToLDmNdha76T8irQAJ_RC7PG0TVlfUx5M59i24U_z4TG-85HSvIa_wl_FDKervvQK0Cr6wD7POm7OKDLNCsjIbF-y-T0pz6Y9MNymzQ1jQsANrJPxRrdN7KXE2RYGe_x6oOdLfRo5C7FVK-uwfvRe2ZjAElpPPXjNueIiZ7UR2WKZmg8__A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7331" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvth7X2_C2BARuMW9tm2rnSiEvFt5kIBJ2bZUSg0ADetfAJ99ygUAugWKCnCxVlRUEYNczDH_GC9P_mtAHXSnAAPIyG4WHinMVRjJ6OeVlquToW1ZDMrYCnCCQvsQtwNFn4ZtnNlbr1NSmEalurQuyKvAOo2HRKMu7VgXIRoi9HBXl1dpRgpIjNgf37XXn8UPcnAmH57vDpe0zuWjgWXkbppc5-KlR9r9Vu-oXfGQoSxALa7IhfhzCBYqNuRm7ZkXrFu4bjszEam_wVzVTldF3WBtWnWziDW0-HcbVFp7eiHhGpQgFZLu-N_lU3HAKOCyV-fH2-C-CtQBGEeBrIkcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7330" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ابزار تحت وب «بهینه‌ساز کانفیگ» برای عبور از اختلالات کلادفلر
🛠
🚀
بچه‌ها یادتونه تو پست‌های قبلی آموزش دادیم که چطور با اضافه کردن finalMask و cipherSuites تو اپلیکیشن PattNG مشکل آپلود رو حل کنید؟  حالا برای اینکه نیازی نباشه دونه‌دونه کانفیگ‌ها رو دستی ویرایش…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7329" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKQvbPA2qZukoY34HikB7pKvwEqcS5vFJLs3MVf0kewEdrxQBUWK3X7eLreGVXOYbBrbfdj4jSg8XUaNQebKTpC5ogJbidkoUPg-0osfWaYR_RYgyMIaj-eJjZi_CIFHdZkJDl-j8fNhW5tRqYLf29Z_wlvapZbkGKr1fhE6UfGjhlbp11ABmYwSJxREPxj3fvpgAvMksw2WWxs1V-ScWyW5g3PPDbutxCrlQ1gkh8DdQmcq4GQKOqroBXZYxsd_oPYIq44uyr9LPzdNB8FuXNvodMjqCq8W4gEL18nN3G9XN0AeKrSTCZsdQ4O6gxsWMmBcHWcHLRpvXVBJkn2tlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7328" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رفع اختلال آپلود کلادفلر
🚀
۱. نصب اپ PattNG: github.com/patterniha/v2rayNG/releases  ۲. ویرایش کانفیگ (
✏️
)  ۳. فیلد Address: یک عدد آیپی تمیز کلودفلر  ۴. کادر finalMask: {"tcp":[{"type":"fragment","settings":{"packets":"tlshello","lengths":["5","94","1"]…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7327" target="_blank">📅 11:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxsiDVj-psb_aeia26k8qigb19tHrzNCPMTggjlowlm4R07seIaLd5ekVvJQazGKV0UoFcbGDVQ6SKK-JW-0A80N9HAhO7tOUMI_PmnPwqN4M8JbunaNw5cHkDAs09rPxpwiM7N3BfAwl2GIBUmBXTd8lZFHqme5m6znaGlmGe9_hScdKrCrOZRm0v8R1Eq1gVazU53MZlOVxJ6AGP7yA238YZsTsk7c6GB0aeLZFzw0rwSIasR4RjhumgXvHUKau_Xxye7_yBsj8d-mmaBf1MP5ozh7b2TJSb1GzaHDgxc_AmSN__7wmfVjyogwldrF_N0CHGHgBEUqqT7UiGomLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC9C_sXSgTRo0AHdrWMxiPHeNamOj-AuWdVN_2wd3GsSsJ6wclvgjyGazDqETkYW7E9xRuBJH6pbwwBNY7dFkXV2b6YRZNINHFun9LIZGLu3L2P2MDl1r76vuYDE7H5qMETbanU3tWh4eOcFSsVq94H_qqZCItTt7YV12XJbJaZgzlmWhyu27vEcC_8mBw4J2qpws1oWMa8e8vb1uQWwAV34MmcWll0nEiF_WN3vxSYDip0suCFx-GFJdSqitfoIVH6sRNV0kc7SPsDn3CrNUww1tLAKybrJE7D7iSR5I7r4f5QtK-9s7G8f7yiNcr8udVZXi11AHYDGlh12Bhf5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4WGLeFwHhpspA3N3SFkGqjMCX_3eZyUCZPwqLwIQcj-Fdkm09tjEXHoVY58L7Z1LI9BrDe7XC2xlUqNpyWV0_NiM11eQs45J4Ez3l9tnGihWBUGJcUBiI7QpFDbNVVoHVsLJbceDn4o9MSdu64DrM6gtNUAOwGGUxr_igKBMMTHaCmUuP1L_sijOBCYFgh3EBWWs-9ZEm5SycenjHgvIdVl6YvcQ5IguslhmBv6LmRN8eMa8sU4M66YrZPE8s5Pynp0beQy2-7LB8cB3sc1JDq4a1Lbb_vGLlVbUtzbdyTgPhXPjcvcPudrxy3YWfk9gcQCZDGysyD5QmasgRHItw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7324" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7323">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7323" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7321" target="_blank">📅 01:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فردا شاید ی سورپرایز یا دو تا سورپرایز بزرگ داشته باشیم
🫠
❤️‍🔥
(البته از ۱۲ گذاشته ساعت)</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7320" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7319" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu3dwc0os-ANM2mv_lzTicfdpJlOpJ8hjFHuA-X8Eb55Mo0NQ2o_EjW6_cm3O5YNhymnmxyR7hfOryKR3x4_08xn9QC-UxmyolSpnFExeM1psZMVwkNRb7vZ1JI_bxkxraCq5HILKAe3IanByuK8HiglTtazXsLWX-iLoMnt0ghokg1a8qk7fCZXpzRYjpP997tYaRQMXbo21jY-HMoviFM9RNeiQYghUpI8HRViS5VYLU4cZPGkiEcm-SbhfR-BLG3t0Z0vzON0GZI9jhInWbK-6HsEWFr4BFZS9uZCZhizPNYUWYuh0eDDCqfN1BiItcI_szMpjx-qUMdAtmKj-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7318" target="_blank">📅 21:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uExZ-zPSM5VNiKywy6n0aE9pZEgRq37Mv89UkP6IsF9p6IXAt4JYsl0GZow5li04Iej68T-0wUWSnlpRHJzWq8J7mzmJfKKFrMmFZt-53BGPKiC8Ubbg18W_pJjUDwCoTE9RDkgu-IQjkfq6Z9hUrMGn7dJsSjmcrDAuJ8EC2pPLTKSpVdFuwy2YShmrsBpcGp8MUFZxZsxRuiiPD8u34eDmAqEg6LP9c1VR60jNCr4XEwo9BKIUKxON87ASf4BCCwRYXUX4LuVMadLHetuOM4LW-f0Nh0AyYHYvQzVhipmLzn5tJ53mznFBzZYdmNyp3Cw04u7DRzV370DFXTFh6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7317" target="_blank">📅 20:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC8Ty-shfC0I4lTWNAZfEYT3VKhwgcKmMquv3chdurWprGjDigEuD6Xurhy5y2JSKCOR9WxC9c2TvH3zmGxHEFqKyEBJZwycrKZPUXGK23cpkEa1tLjRfidUf81EVgu_SNp3R9qC6EsT_muzTNbG1J0lHmSKcBUHHSnXH3qCzCRJ9ZOKJ4Z9Dd7vpSYqFylTRrCFb3JJJilLQusEptPxqutFRmuDhCLEibUlotecjfQYhB15OR2n_yg438b23-RcuBevzURLS9TCpYRqXqVGihYzutuLbrN01aKf7GIKTVCPOpvTO8pv8B_cVCSs8LfHuoABz14oproohE5WhWzcxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7316" target="_blank">📅 18:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه پروژه جدید ساختم برای 3xui دارا که خیلی بکار میاد
دیگه لازم نیس آیپی های تمیز رو دستی اضافه کنین پنل
یه ربات تلگرام هس که به پنلتون وصل میشه، بهش چن تا کانال آیپی تمیز میدین، خودش خودکار آیپی های تمیز رو از چنلا برمی‌داره اضافه میکنه به ساب پنل برای تمام یوزرا بالا بیاد.
سورسشو شب میزارم.
تمام.
🔵
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7315" target="_blank">📅 14:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARjLM-yezCj1hmK0D-0Nmbwv-Ix5WhPgAGW-FLJqb33HDCpBio0D3mCYEGvsNkJQ3TYGQEc0bkGx5SFeAIrrJHXU_YUfCfNiLSxBX2URKRJlTOPsMOGtNpxo7fRDL9QTpZsLUhiuEaF-yvyDzScAPlJ3YNW0hrmoOPIr5Gn__nftsCvemHSfSp0RkLDtP5RxGccry-DH5_tgUcHZN4n-IYbM2pRz7PmzbekInrN4t7CUrlPb6xGYi8-74Wlv7Lum2VfSjEP6YQ4mdSQfA-DICCyl2dv1r3QumnMIdhD7Xw_W-lUcLiK8hRqidt9aTTjvFg83IXSHqvKWZxu-aKOdJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7312" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Lx6ux07syjE1oRJyfJXUurZBoXdzw1rsnRgjEL0ELcHAV4mK0jj5wY9Y0vwkzXvB8sZHiTfIHm7vONUoNlmvBPYTU6GS1g3TO9KZNpFzcAD0bx-YM0bsRRzBUMa68LmxXT5Uh_Ns3LE7fMa7AM5JFdt8tu8vSxHYuqhPVvZ0eidJPdFt5F7Y7XpWTdY76ktp7QhT61TegsFL5b6W8QTflajlKu86GN-5FCuQTm-x9Uthio_C9_K_o27MMnnX7YCuVptXfdRlzXXN1po3TFZP9wx2f3O3OGi5INsNbfLv7rF7L_MAcv2Ke93WNIFlQcJwP0vGz1iRq9p_PWZ6OLsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7311" target="_blank">📅 10:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjID3pLgor8w-aQ6d_JN7jU6kzKra794Vq4ao7g7EIvylD7p0ViVpD4rKIB-_kAnp0ByWcrqyL_eveOHuhvXc8yHKLYOKHZYIO4no1OFoMCFF5myJET0T-xDFUIAmzy2l2_dQsZ2w0etCO7yvvBuxnDg9nufBy_PERSJv2Mxf6BnLr1MyYn077tTvj67q_fNr3qEDbcFSx8sDbwo47FjPgeTdPzPDcHVtCQlX3GMouQ1m_1mDY_-1JpC9kulmHU_P5Rp7LRiCAeqgFgMQk5T-yvlK7oZNxiRh3aMAnFQesQSTmxLFarsiXB3C-KCaiZ1ZDyJx5NyLa8TzVhQhojF6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7310" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7309">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7309" target="_blank">📅 23:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWkt3q1CLJ5_0ck4Kq6FYktD0zobfKn5XII4NgRBL3mzA_NKDNEGJCQjx7aoCKw7OiJe-oCO3kuSQ48AWgzjtLCoinJYArCWyozVHr-cFru2NfZmhbibC7YgCSVmvCY3yB5goHg7oBc4nxJKyth9KC8D_4dhiDTX9_2EyimdFwVutThI86JKeHfm5c_NE5_4YRrhIXVLTabbQFX2W0tWn4jool65AcOoWkoe7yaVgfkdrknUXYrzFL75hNBFTSCfkb2Bv9RPf-a1MVa9SbWAUomGuBf0eozRdGg4G7xjSeeWgaCQo4cHbAjpuEHcOdPuPWEjYWUfOz1iNh656dQ5Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7308" target="_blank">📅 22:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n97aRNojH_hzDIxDGwy7fGAxGfGr6-TcFOSalGD_xk45C634Zdv1HwQX2lFiGgjNkakx3ssSUsZvFTcPTshZb4xlCh9S_Cs4n4DGVHbc1gL8_9rXRmeGWQmcALLgnIYHFCa8U6JE3ZTeVVHGW67jCg3kU4mhJZxlI_VFWEYEqkuh8HGXkr1ITK7P0jkutgvEuBAWlK6OXnTYzNNysQQR4XsmLEGykc0BybWCiPAVBAwEJg3RWo8aN8NbcOEywRuo40f1OtEbK0zuSjnsLG53prIDLmXoS2hSB2tG6VUCqrs1NaB14YUWCRzNQhVRfoi8IpuBJFprJ4Xv_CUQUwnkTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7307" target="_blank">📅 20:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNuTOe_p1YmPHpcSHq685F_X3xTK-S-aNLHIbIIZ-N2SCAM4iRA10RZZL5o1HnMcXxGYNH6_mQHzYQXhAl3Vs1AbiiQJPkxzMsaEr7B2Pyc1F9AC2HhOZTgYyrr7fD18TFThyUoxvOWysMArGOkEybmISDvlhO4l5DrGavcUdIE8-99ndVxttMKJ9Ffvz1GFiorKMDV39npl4GZhbeu5ahcBOE42uolfNlwzw1l9Bli_HVgWqceDaQK8uMTACc_HFNKB6tBxC3rc5RDXRbZGU64Q9YrwPbOybLv8fwFrqee58_RwKuotYLDdSS7--wAyzRZb_1V6JMSlDIZ8dXbGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تلگرام پس از صدور حکم بازداشت بین المللی روسیه علیه پاول دوروف
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7306" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkjvxdKvr4CmwREoB5pZlTqrJwm77ctJ5cMCmPiG0j6K-f7wEJbyiivlnziq4WWjwvZYKKr5NXwbVJ2wNpQFWy3u5RrTE4Bog0JEA395IW9vZZb6HxQqgAbmhuR4JmNAH1ANNYJQExQWletZ-Y1LRJNLxKgC_Mhc4rRk22822Xz5HFjKeFiitBsCSrhnEbCWbQg6bYOJyX20U4NDjiex1-xkZ6E2SRwz0NNVYM1q5fKr5Yox7Z0Pr72lR6B54yMS5n5FwIxDgeJdvznTsvg-DCUG8YO44bJb6jwuA-q7us0jh4PaET5Il5C8KNBcqMe5g9YTPXMhKgd0_gzhIECNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
https://t.me/ArchiveTell/7300</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7305" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4-pYswMNvfW-8mQ81a8y_6PwaQ2JenoBsvYtXOc9MoUouccbkSaCWof4SidY-1QQKwKmpwTf-N8f_9auxoxo23_TK49F0SOucb4kR52hYtXa9oQBPd_5q2YWoJ52j_lEJorPCz55K3oE3PipPuxXuQpmQGyE3CdIfWc4-9EzLVa3qpxcXAITNXOVyZdqZbCwaP_iN2ELTjXxx5P7nIsspCY6ilzVO9f2Cevp7dAw1zEUFrCp1KsRngtLk-vUtUnwj_H1OqaDLxLVrJfsY6CSlgbEG8ZQmuLVtwGTRDqBVWa1XWDyzf92MgvJiZW_ef-9KFtdw0zEG0eUANPlIf25Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7304" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZY-0TA6dL8c3pqzq0BYjYgShQduhF0REz9p2tEJFrXY7qx_SlUP2Aid11HbBSGT-mXVNbOVldCvnWgz3lJF7OuKyYaIGaewhGufEmpYwiDRlWlnDGIR4CS9PU_yUSmQfK3lYmOu7iVCvcjZyO16V-iLVS1avYNy7Pzey_MTOmNz6jvVu_JY98Xx0lKOR705BUrpoCLEhiKBNt__ZVYtMK-LC4J1IqKM72_ZTtWBNOiO1vhAdMRkUIRyPHZdaVghfQA3NHRpe7h9A0wCLKBGnlMne0dErtCys0zGkM1hrTRH-TTxM5Z0q3j8scCgHswdp_ZGDjmH-3cWzaWxgs2lzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7303" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA2lVhtiRkb9-xAxxcMps-pi2YCB4CdgePInRAwz_6lvELxKJuYiWJqNPsdeaQNbhAbJBg8eDq9aTuPHeIdUeTcmuxPBHFpq1qc1a8iyaPanKfHxWNrPBK9XKFsKkYV-TNhCcAf3pSWILB6QMhdgVjemgfhSjaly85psRhlPqvwU91HKX-cG0-9wmh4FdZ8hbtB52LANndKKlVZyQMAvE5jxwLKeNwcbkLiV-fCROdWKVAaU5UPg1wGPzZMf-NMSnQvEpp3CIhiG8MwYKr9Ub_qrmTw03F784Ke2AEBxu61ODu2UsC0DvdYJaUbDn-t4-3wT-Orm8KUqdDPYTeTpIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7302" target="_blank">📅 12:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXbSYn8YeejGRZ299dE_oT8ctj4gqSAultXqJgW21ufAOoQtPybAJoV2B05NAT4fd4WdKhZO7G9yaajyaPUjWW0rRaOl7Qw-Y8c63hlMNmoRHuAwAwEGw_49-w0E7PRY5P-KoqFD2bVSdeiPAl3frhBBY34sBuNnTkhSfsJT5scu7skTY1j7iovRsdPKFRG2g0QkoK0qrldU2JHsT5BMmFmw6hXWybQpoDOJjjL0kOiFEvSIlPr3fJCQDIr5R12WcFW3CUSpe1ABWuxi6imTHrZQ1ic6knZwdZaV1txDx-wLzMx9vjnoBcHTZHUcGO7vtawafeQvBdEuJ58oYksCOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7300" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7299">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7299" target="_blank">📅 10:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7298">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7298" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7297">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آپدیت جدید کانفیگ‌های Serverless منتشر شد (ورژن ۴۶)
🚀
بچه‌ها، کانفیگ‌های بدون‌سرور (Serverless) به نسخه ۴۶ آپدیت شدن و روی نت‌هایی که اخیراً از کار افتاده بودن، دوباره فعال و متصل شدن!
✌️
این آپدیت شامل دو نسخه low_delay (تاخیر کم) و high_delay (تاخیر بالا)…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7297" target="_blank">📅 00:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7296">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB40u4WpE4u2C-VaL-tB0AX0Hh751DQk7z96FnwtMYyEb6jLmZlZz2vJnJttsVnXtETMnfr7qlvOdliJj5Gy_o9hs8NlbNSsTcMrd45kV3p7tRyqPrtMKsedMe9y8GVATZesPgHVw41xdSt9M4TtVMeIM3jQS5SpBErqdikn7jMoC0RmQj-K9VSNOWTTjSYUNtMERBBYYvrNlxT-HTic2S9jcPupocbwbvqFvLklYSwNBpcHYPaNBK5l-Y3h_oeaJTSAodJw4fczUWVk6hyUNjPVEpwePhi8rTzxFdfeoJgiK2Ei34z1GOK6HIH47re4tKtksKvbwZWcRTxtxz5uZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7296" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7295">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzOG5AnFcqjE0-sLb5X-u4UmI_dhz_yZPMe76NhrohtQpSX8_quYFLqGMTfICRJKNbx30tA6oywNhb-x4YZ2tZm6MfEYQ72XlkUaX5nfT1LsIs5zpImGgIyfsAGdYtmW1h74IBfkxo0EcJWkZRoWXC62iXMZM0LgrGeqjYFaafzmcGnaCQW3v309hiOTnSEUC2XRN_LphhaGg3zaniNl1nmRMkg-P46E7V0_5c38GI3FQG1r9PqKzcBmB57SsXcpK3OosiFjVHbp-AYooup4C4O20SLqJ7Fg2Og9FYjavXu6jXVB5YOMxtdz7RdABgZfJB-nao-M6PAEnFaNRMaEDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7295" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaoFnye67MGLbFR5RFzP2HCHGQ7hheLjtrcqIIIsRnSqL3Hix4LjJZtSWTUw71UjiP3VBOO8zZ0U63DBx9LUPJEO95EAfWy5XgE4tSh3zQ3xUtLXlscQ2e5wi0IWLDn66jhYYLVi_xFWUC8lpc8D4wgB9YXbdEmJVvukLCL2oVMf-EkzpBMo-nRxyK58IY0WMjYEAs4IZyxTZBmEQbTMk7iSuiT0hgdSxd1ZlalgcUlBmVSSe3vGeBYjwCkNjMcUQpH0Gq9zGf4DVGWA4rcQXiY5gQ9yay-Dw_kXpJG0VPqTN9MjXKGJ4fsqNRQIsbIzgFXcO9N4oD_qZDl1epV1kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7294" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=Q3Krockr4u7xP23LaUbCOMoccPreJl2LSNYQuN_xOqtmjkzfGOPLudhKEpR6kzTaDxr_7DxFN3uWJqhSxauGSPYjqrOAfv8HhIBylG-b0lVfhtvZwrfVmcW3xa60uk8h9FdaBjhK32ZUbzpoRRT8tDBzbAeMKuMJLxvbys2Y9a_NFHGEI-BISv_1TlJW1SrNkoh7eYTpX8slmhAr1UueqUj_PhlpB8NmyH7BUdW_rkKB44m1OvXgSMh7_e2kOLCGNyKZGbxqj0xshLZTl5i5Gv5pyGnH-TVjSL43WfmGZKIML3rEUi32fe2ZNNpj_odyuDH-17VQ33FsICXBZaZ_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb979dcf62.mp4?token=Q3Krockr4u7xP23LaUbCOMoccPreJl2LSNYQuN_xOqtmjkzfGOPLudhKEpR6kzTaDxr_7DxFN3uWJqhSxauGSPYjqrOAfv8HhIBylG-b0lVfhtvZwrfVmcW3xa60uk8h9FdaBjhK32ZUbzpoRRT8tDBzbAeMKuMJLxvbys2Y9a_NFHGEI-BISv_1TlJW1SrNkoh7eYTpX8slmhAr1UueqUj_PhlpB8NmyH7BUdW_rkKB44m1OvXgSMh7_e2kOLCGNyKZGbxqj0xshLZTl5i5Gv5pyGnH-TVjSL43WfmGZKIML3rEUi32fe2ZNNpj_odyuDH-17VQ33FsICXBZaZ_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7293" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آپدیت 1.0.4 کلاینت UAC-SNI-Spoofer</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7291" target="_blank">📅 18:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLgI7lWznM4O8SBSWkMTm8ZPqp3QjJlSTKqmqIEh1Q9-b4nqeMxMA0jplS-0JZuJZo-yeW-eC7CsOHXp8rjX5em2N8UC2lJp9xuPbnkI30FwlAMTFLlgIzFsCLNc5ftISTdYibYX71nXu9r3Uy6ASi-sCTQt9bjlt6o2LHk84quty2y1Mbj3beZm6VVWV7krQdDydLAWDCQMUUwdYKzt07AIL9V4Aa5uz5x_P7MfBTWXlENnQGXTCSN36E261HifKZjk6Svxi_hysuKPA5Yo2w2jX_aqaPOiZ4owXw5iZ5ZuPpsjMTrbQpzzZUmiwgVUeMIEuIsfRX1uMKCQrH7vIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان  ایجنت روتر (سرویس API چینی) امروز علاوه بر Opus 4.8، مدل‌های GPT 5.6 Sol و Kimi K3 رو هم اضافه کرد
🔥
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7290" target="_blank">📅 17:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd6yiXg_d9HaOKMw8Vp4fFsEELfSSZTjLTH1uD8OavrPRXYz-hmmvLgkhjjbZdwXAOCoevP0qhq-hAdnDsnXfBlUyC1Zz5LZeh1FIscZ4V4emZeiJLMjEvlRpEuvxyyRCRS73WyGerRiQSNyVTSoEcLN-Jp_aUZAA3AlfXB4gK9xIShyJb0HBukvUC_N30nIWyZ1CJgGz5DqyHLanFjAYdG7EOVn-Ywr2O5gQEp4-kjqzPCGcuc8hhkSp0raPPK8lRsic9nmH8VTdxzyuVzOZB8CA7uoJg3SejTmaV_fTr8vZTFocbSZ_KN0uK8PA-9y15EwxRMIviplxc3aDzakww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7289" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🛡
Aether؛ کلاینت متن‌باز برای عبور از فیلترینگ شدید ‏نسخه‌ی جدید Aether 1.2.2 با استفاده از شبکه‌ی Cloudflare WARP و روش‌های پیشرفته‌ی مبهم‌سازی، برای اتصال پایدارتر در شبکه‌های محدود و مقابله با DPI طراحی شده است.  ‏
✨
قابلیت‌های مهم: ‏
🔹
تحلیل وضعیت شبکه…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7288" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHyrSQnIF3_bj0huKsP9WOqzHCeZrthznT7TIWH4zISIJMKqMzX4nE48np-LpJ8DRvApbyLrk1Ag3CmpQSAuGbwFCLsf7sRU323Tgiv201aavd-g-YjI0-VTKt2wpLOvDNTgbRS24rBkNBR_LRnR1xHJBRrE5PMVojQSCmV1bE5mDEU5qGsF9cDh5oaKZMZpERE-wghZbaxjnfE-yAIdn5QepQNLVAECkcJhobN5ulPUKuAT_rLh6YokRkxbc3ikSIzDa0rKNSe8bh7TYmYQJvlZTYT1UWYdx0ldmNKHx27xzushMp1x95jDoNRyVmb7_PuC9K4WqRp6LtO0TBdtMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7287" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🟠
❌
اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت فورا تموم میشه و مجبور میشید زود به زود اینترنت بخرید...
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7286" target="_blank">📅 15:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ظاهرا رو بیشتر اپراتورها فرگمنت رو کلا بستن، البته باز بررسی کاملتری انجام خواهم داد.
در حال حاضر برای دسترسی به اینستاگرام و یوتویوب به طور مستقیم و با حداکثر سرعت میتونید از MitM-DomainFronting استفاده کنید (فقط نسخه وب).
* اگر از قبل از طریق فایل certificate_generator.bat سرتیفیکیت گرفتید، سرتیفیکیت شما بعد از ۳ ماه منقضی میشه و احتمالا الان نیاز دارید که سرتیفیکیت جدید ایجاد و اضافه کنید (در نسخه جدید جنریتور این مورد اصلاح شده و دیگه سرتیفیکیت منقضی نمیشه)
https://github.com/patterniha/MITM-DomainFronting</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7285" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh830lLV6QZyqteW01IjQtKY62JJjx5tQtas-EW9gylXv5VDJje17xPhMMBXSmIcr7-XxWusUFLfP51W3xJuc0KH7nS4G5gDcUqRJkqY5dYwM2XORlY9psV9QQUSuyIN0m2Np4d2G4hmw00qDqIsm_ElNb9gtUb-wkdQXIs_B6rP5VEtP8mzbwuRS1x-5Qc9ArOhKK8WL3UrXJnatS_62EPEGGhdW_eRMZJiUM_wRCRICjIrCiBVGAieA21rpBzUlLWszHkdfmgxMKBVv0ndErXT4Ht_N4beLEDJNX5uedb4vQfPQNQhiRFODDz33i3EXWbqrq7PX1q4Hn89AZS33g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7284" target="_blank">📅 15:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWWz7PPv8HsmVQ1S_P-FIPsZWQv9raAPDKuT6uur402Q3tFo2jb2-E-ZNVN6SIqA5-QBDG9YgaWTMSmjMH065q8CNWfFKBBlHZroixQlC9qteM6MC24VHjOAyIbnCfAePCUdZwCohYAzc_b9pE2sL85pBhhn8mzkcifCQmBrddsaXTeMBlTsUIoaFYo-0IwFcA5VdaR-FPElbKhVEndtixQ6p15qrJazMSCF3PEXAut3VSfWzkqXg7oW48BlGK35nrZ05GjcUsFSujJcmlBcgCSf-jcWi-CuYSFB5o5s_sP4McwZTYEAY43wK-vx_IFDgb2aCcR7zC_E1dQA_ISkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فعال‌سازی پلن Professional برای پلتفرم Figma برا طراحی رابط کاربری وب سایت و برنامه اندرویدی با مدل های زیر :
GPT 5.6 | Opus 4.8 | Sonnet 4.6 | Gemini 3.6 flash | Gemini 3.1 pro
برای دیدن آموزش کلیک کنید
✅
🔵
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7283" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iau-cILIp3Z1m3_kAkysEnPiAOUIlDESKJhSVysiBRBTlLE6KJOY8hOVlOXhS3Z-oRXCGvsKX0XrZBi3eN9C0kXKwTLlBZQwCzTtsZ21gusphxRYvL-BDh3P5TQ07pubdF-oV6CGEtPx0f4u9XjEtIwZ6ZUAFfv5NfSoI09x7yLNgWI_Ij9OdMBe-57n_iOtlGPFSfyP1coJwiP5JQssvgQH4r1KOGOjLyro0LaZibIUYQhp74vKe5d-CqL48C9sa1Dh7a5_jQIJeCrDwOnFx0A_bvePSuG8l0TsZcp4tklQeG7FiAxpGGpakGy3l62PsPpJmp_KASzMMRkmIz7OqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7282" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
