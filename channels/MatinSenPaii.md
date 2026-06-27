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
<img src="https://cdn1.telesco.pe/file/en5oWwCKFx2Pct6_gLO88CvtPybsGMML3QdaNUcxDBe9jlmvMPh2jDczBhtwvozp0vVUT0nTmTkNanHP5zsguQgvfhkQHxgRZVMpEdR3XVuh8xiuIcLm1DG3JI7hVUrrx5VE-2NwabP4ip3Vq4HpDl0zNSaiN505NbiJ2aXE9xK4hkzvHhROgtxK-Fzc60l7miUI88VLPuTnScKKJSiksHAZykj0n5HXD0O_2916bhDtw-jpib6rwSFxEIwh292B1wwfoucgKMewDRN6efTvCz-5bJMk-x1uJrH_G9kSDSwtIb1fsvMETGFO-eiCmC7CV1n4GtBkER0AuB7fhHAs-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/umGEmum8OVqwnl1_uf7ZfQS3F3Or1ejiUQRtcilOHkraBMtq-4OnuGvr02jOatK_7PKs9g8lPDUvxtts6RuETvjw06_Mf5ahTxT0C7UyTKVcSs7PeBBPhmbvMkFmME6ZZu48TLIpobyv4_9veEQD8hXzvP2xO0dl6dOkOPrchk_d__hnI6E7rgU-EgDl-mn3Sa5owBm8lfwrt3RvSCbgUfJiXwwk6RFGh_1kgUW9eQreleZvpK34rvY8kOrYv7c-85xULojY--dBHFdOX3JiZ81nKPVYIfjDjIjWneIE3Vsqbb29L1g5T5RtW05c4dsBF0Z9UT5GJ-WDtEX9xsscmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NyTTJlhwipzeUdU8OfDkkCyuZxeyRREtmpBTqNNuxzOJ-W_UeF-xf5FOFzet0tPIfR-JfMIPEnJ6LotBu7-PoBEgqHUm7Iqa9NiZENdbBfqxkHXrTIGz3MS3uf9XDEHUKpV-ckqtLLzMYvSGJNO0ROkl0QUwymlApxP4s1h2891TNoxDWZiLPCzuW1PZ0RaXhG3XKawHZVV4llOSSV_ApbR0lYb9h-alpJTlHvxZi_iPec_cNVflyte05GciNvuvlbN8IwDNdRVVBxW-1o0IFx1babyMZmmbRM0CtVzPR3oE5appV5RlFiznNUJPQqXrI9Y_cyZDsPZr2iNyRMmSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQjbM6lnGKnjqqUuRXTbK7ydBfb067WUnnwUjiKpA9EJeg_a17fkuaS5ta1478Fd0EF3PYS0YtumO4k_CpfPN6BQA6noy3KwRSr5Jfy685uE3O0u9-gUzjREjVY0m7PwQLv2s22fpfv7_W1JTBPfhEAAa8qo2TfAMCwpx6cW8Kuq9W1nnAk7IT8kOK-PFZZtOvhQdh5wp25f9VkiRAPllxK0QT5UgJE2YsQq2CwbdTUWXju1zgYsDcDyI5VdC6Viz1jNatnGofwM5L2-nW7-uHnkPKbTv-fgUcajgzsYFTTPXccU9wdjhmQy_dSZWO0YNoJzpt4Ci2pp6doeWS9frg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnNHDYv5vkeqft7uElPEZp41DSwM8xHaqHSXi1HGzbHmnyW--VxpzLrDjhXm-GmGjmuNUfpqVm8y46aCLgceUFJEqXbS_4VKMV_fddB_zA75z07MA9zI9ZaC7RMi5Ajno_dLA8YvDHYGbm5YgsyO40TDh_oEfDwo5u5-d1dIlhcmW28R5P14vw4MHnPTcNWcrVB9RyEFmDfFdSjbJbhJFNGmqCndJ9Y_7YxTxX2-BJtWG1d7_6Ux2IFbV_l39CKYMYFjKIQzjKmuC2Ent1wqUcjkExohPmZkjSLwugIjtzv0XzrG6DfDwpx88eSd0_5WqG-4ze0x6AgbzrByF4N9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eqDwaJE0zZ8jbyLUsgdOrYzHZUDxxO0l32mgBqKYr3kqYPDMUCdYzb1SIZrDc0VOYECatCb-Kp4PlAUHHUip3HXEBEa4xJZIBnVls_sSR4_w-PcvCcxC2xZSNljvNXUuP5hHSz_tdL4WyZURORQnEpWHCForFDNOcL2qTWPVbrbspIVCNbW4gszFkgNd8DXkAvPxgroSjXdaD8EC5AYoIzPKFazUkwZWmsuk1EDB5rsnrv6YYR_cXcBQ1R-0wb0UNf2yFW8SAPbFVj9s_uvh_w30mI8S0cgrzxJ3g0OY1D4FUDlHtrQGL1zOcaPvz8Hzp0jPKWYARgRhoc7ea1o7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NEgD8Rgwf2Vr_PoA9pvz3HEh3ShYELwsFDlWOzjSt65x36wXjlxn9PVGSySoUDzFSWeCNX78Ig9mrGGjcA78LXenPCZ4ASTzTIfD1_9CG8QXDGQCsB0snRhGIw3xunvMCOpn-n5mZy6GPGRB_rKhc9s6XqgqE5MABqMMIucLGwWcF_kj2TwIuu6U23j0vEtHp293ajJsrLzOFXI-RgjKqNGm7u83fwn_UC2Z6_FWcSW1u6Qbcc-dftWd9dcza1L2sl4YvtsipA4T-LsOmxM9jKI5novXOZoRtFprI-95Lb3uZJFVfBUqyxyhSAc5SrxYQM21QiI4E-UIROR229ffhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=h5Wkgab5-kvOT2PYVY7iJ6S2Ic12DXwgl0uXCyuiCHL1vJevM6m63gYyqRFNordp4ELJ8kBMrQH7MUNXJ9BYQq_hanR-GdnOhPrWdOskzyULesi21LDROLeGJBInjBy1ibzHLny0rNp-iZ5m7YwlOkLlKh-qn449Sm4ceJE3ZtfsKOqoor3zGKzmEWNXqXhLCj7fBjoyG8pNMIbF-QT_Av4UUAC-7oTGxKrqfgRTgp0vU8WD2_q_DoHEsRTqWJduOM6Hue777HiLXruPh34AJlDF_vZM-hg_E0hwXOmuXlCh955adbsk4qcC7dlEnGCQBKBNyayxC0Wk2XyOemUFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=h5Wkgab5-kvOT2PYVY7iJ6S2Ic12DXwgl0uXCyuiCHL1vJevM6m63gYyqRFNordp4ELJ8kBMrQH7MUNXJ9BYQq_hanR-GdnOhPrWdOskzyULesi21LDROLeGJBInjBy1ibzHLny0rNp-iZ5m7YwlOkLlKh-qn449Sm4ceJE3ZtfsKOqoor3zGKzmEWNXqXhLCj7fBjoyG8pNMIbF-QT_Av4UUAC-7oTGxKrqfgRTgp0vU8WD2_q_DoHEsRTqWJduOM6Hue777HiLXruPh34AJlDF_vZM-hg_E0hwXOmuXlCh955adbsk4qcC7dlEnGCQBKBNyayxC0Wk2XyOemUFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxG1_OkMQBy3S8e6w1Ulb86R9aB9wH5zxez4wA_l75AMSihE5yELVoXC9NJEiWcvEEyx-vIK735aTwi-tVKY21-E46xMSJdEwBxVVyFpjEcrs3xhu_wC4W1bR1EnMLF7RESvvnkPWF-IehKQz1YAp4qc2uxUJO7825fUJ98M55JCAGlKs-W3X4J0VyaHmC4U8muE2M7EkiwspixnxeqW-pYw0HKW2vWWJYVYjMlnSoAMcPXSlDvMBCBzLeFtyBm9-YKLOUqeru8qqGxxSbDlWTfb7gv0fUUez1SfySDiKX0RrJNHOrzVTjdbuGTnCq1PH-KkZ4NmkkrXgx49ftY-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HzVYyvSadG9EZX4x2diAVRquMDAe4cGXdHlZXyPrNDN7so5FgDCG5HPjQODb659YfTekGzcNhDJ0e8OneVJMTfmiKr9T1e_bLsCF2ZxuyLvIhpjKyN4b-5cGL31Cn4Du54dbpPCT-7RMCJJz-GM9qR12AxUT-gG2SHTVqb7GItRpJe-2Ilcsnx2XCnjLoSh7ZwuwHJNMtATEym8ev4Ni5e9YiEsjtp3eZ9wELmlbKpIG8juXxWgTLEFEPEGbHIZWz0GarjyoMEfFeane2PY-zAroTagwMQNvtsDsoZJtXAPI9nZZ0DJ73MO4KxYCoZxjXOtSn5QlshohsQUj3-XHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIkEmOeYwVWjLk5YxeZr_8WEv1K5-pBDNDvJBzW21zSqJn10bZlXATEt1Mlyd5bh79eKpk1oU1QF1tk7vRInKaILKbNFl-PteFEVPrOQrmcifpWtqQ8gy8GvEbJpBGs4NAae9dbtVnVziGg0MmtpJpVPbGBwcincQyrxEetsmbDbTmvwadyH056fUCSv_Mp5rtA3Q2QhrV_8hCVw_yDX3YMrQ3IgqgchwUXNI_1s6Aqzch_MdmLEe08y601Yn4nr9TrngDiZ5xnFIkVcNUSzjwtLch0D-chM3DUE3OfC8nYYsRkND64SeRpDO7CBqgVyou-kjNra5vZMGmYCI9nrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/boBM0zmZA8KeFTvY_VbQQoQE80s35Lzn-WmXUYTfvR7JxSG2NSX3J7lwNWVcy1hVb8Ogq-uwGHmBGmTY9D2HkfYIRa1NzHvU8j4rrH0HnHYWWvBUlUTLoEqt6pnFdq4OafZ7xVRKS9sAgnu3Ng2b1iCZe9lG6nhql-pOpEnYlgpAT25xP_rz40SN_DGXNlAvnWJsRm_LY0t6KLF78G0MK1hDOwXz9ImBLB_fsRFmkm8OUhoP9tTvNyA7QnJROy-Yy5cqCsJLYylaogabVKIDEWy-JlAz1g-gVK02M4LoFxDa3KwTMwBNaS61aSaRpYpwsg2p5bL3R2VqMshPVfWV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XITxbi-NQD4ETx_iXINib1nPnRHe7DLF6Czo0PuTe2Axl-HJmJdMkk-tTgrSL8zX77noj6Pt_TELpVDSk4A9NiuZA8EgMRYimc03yLg131O1YQLq3g7vFYpSPrQxK_GxwcubJIvv5TdCuZVnwq8pKJSLmNEUzuLP5P1alZkTy5h9eeiH1OYebEMrSIdNKl5247nBOxvnm58RuDXmtAP1vY7LuUKqCvpT4eYamNyGa81gTChmkuWeUAruVp8XUrZeXBIoUwHG_8XN0BCZzz8TmykP1-BoV9Wcc5kt9hiFQXIDKuCAvXxQPdfpdULeeJ7WDPoDowDeDAbem2Fn4MaHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oVlv2Za80VQ6Q2gN6F3SHGQT-1E-AvpztTWA9NE56tEjnPnscP-Lzi1IAFzUmJpWN-tpuXevOjBvQfaVy_EoN7o14Pf2312wcjySnApkHaDtKnCNu2Tjtu7caeA7xtIzrWJwgrbztthroIaL_r9j9oOlzp2v6LSjy9Z7LL-9FtI340-Gv_sjpyVNmYOqFR1RJvhDqXZQTwfaApj3009zSVrjV7_ruKU-Lafmo6dA2-CWSX_1KuoeDwSi3_SFqbQLdoNxspMH1Fsgxbf6JStDMZacMn-E5HeZhGlndJoeLV1E9v18njLaufjBKi17bB4e1HJsowdSKHvVpp2yI0Sfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NAk2B17YrqR1SWAhi1Zeo3XvRfxQMJo4IwUP6hXfXAOhkcVV6hLJhR7kAnsSRJxUoawOoCXrVCZySDXDjiWwpysWlMV3y-CLyR09Cw6n6GhzRAi4N7CeyqLeekJeLr4fBCNAvT5P0pKV1-o1FC6S_vd3q5pHjTPnHEVmeRSB6NiNKCK8LBuYuykJomPajz37ouPKK3KNMw3Rk4_KwILqyZ75PFmUGfspex9hMqoIl3tBtLYWTZR_J1SYT-7qCufq9hgC91SCzb9j9kQ7mhvWAfWAxqlBbY-ISFbC0Kty9PCIkSAsM_4U6KUpbtmDcY0FdObqEsm_KOS2aKpr7oQjsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcL4dyUUVt_QjkIoIRcSIUXEFsjDTcsBV91NWoSGoPsBjCT1a7vfP78UWsZZrNUZQDCZNTjzZ4Q0ulvKyCWrNnPuamf4o3Va-37nnw_v8Hs6bbdSwSp_AG6QSaUHtUixRZGVbBne9HnvKZbG5CFX7iTtF-Qd1KQ-DcsFT6_sU_IVdwVXvbrdVQ_YyGTU1O-3N8jNQ1euJdmPExv4rYFfYehJ49OweFJdUY_Gc4IjKqlQPPy_geXy-MI_iApz-0-HIyvQkrTU86Lyhm_BcpSW57Dyk2TMWtQplzMXdZLuYatpXKdaVJf2nP5ARwNOt4ax6ICeo2hftv99xd4JPs9GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=dQiQ3vwD2Mu8btU3HavZEjMIgiF9cuK-TbC4SzDxsiSD9nPOf19icy8PH31roseD_MW9Xn4TU4tkRPfn-0hP4aBNdEGCpHPCgndDjmolJTKMzroCaY1q9El-vT1wYboN0sSIN9r3CzNZ0LU-rLel-O8UUqFuTlWVO6Fj1Nh3Chf4Vi6b5xobKOKICMcKd00SCFez7iG2kf9R2m3f1afKEkCK6Zn0m2VlySCP_Moxkr-I-Sdg4_c3Fm34uw_NNzLD086oCIMmc9K1bDKZ6Rg7JIIc9szhe1f4_ujdRmQbiziF54hO2xJsxQOTV5LH25P9haN0VtRpiQWHW-4__BanJLGGuAR6BBr7VwCVjBZGMYIX0oaLz3WuJR5kofN-ywqbhejp02lN7ll6lndbwqOWTNrNpcz19BaiZBlrCBXAMpRueX49XOc5fPaGhS78tD3hv7_eULDuDGGNrUlJbVBUkUXrPN7bRQcHh1K8tlWxvBn-Ry_ZwjDMI85jpoXAuO_XM4YXy7arfFgZh0230cp3InK-osk0Iim74qhQ37YFcxRr4A3VSiso9gCLkQmd1eGHwohzrRfJtFKr7KLhpdRca812gX6Y-VfnpyTAx-3gI0fytmNLh8naGIJOzKFlSyccPg8A6mn3uoALNSd-SEXd3gXtBPY2SQK6OxYQoBXbT84" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=dQiQ3vwD2Mu8btU3HavZEjMIgiF9cuK-TbC4SzDxsiSD9nPOf19icy8PH31roseD_MW9Xn4TU4tkRPfn-0hP4aBNdEGCpHPCgndDjmolJTKMzroCaY1q9El-vT1wYboN0sSIN9r3CzNZ0LU-rLel-O8UUqFuTlWVO6Fj1Nh3Chf4Vi6b5xobKOKICMcKd00SCFez7iG2kf9R2m3f1afKEkCK6Zn0m2VlySCP_Moxkr-I-Sdg4_c3Fm34uw_NNzLD086oCIMmc9K1bDKZ6Rg7JIIc9szhe1f4_ujdRmQbiziF54hO2xJsxQOTV5LH25P9haN0VtRpiQWHW-4__BanJLGGuAR6BBr7VwCVjBZGMYIX0oaLz3WuJR5kofN-ywqbhejp02lN7ll6lndbwqOWTNrNpcz19BaiZBlrCBXAMpRueX49XOc5fPaGhS78tD3hv7_eULDuDGGNrUlJbVBUkUXrPN7bRQcHh1K8tlWxvBn-Ry_ZwjDMI85jpoXAuO_XM4YXy7arfFgZh0230cp3InK-osk0Iim74qhQ37YFcxRr4A3VSiso9gCLkQmd1eGHwohzrRfJtFKr7KLhpdRca812gX6Y-VfnpyTAx-3gI0fytmNLh8naGIJOzKFlSyccPg8A6mn3uoALNSd-SEXd3gXtBPY2SQK6OxYQoBXbT84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKuZU3F5A2ehww9i7xDVVPWbzOseb7Jwh8UQzCAgBosxtd_ZvVH5j_KhdW5pVGAQlHYOemfpe5yLhLJ2PnJEjDlgFHjw5gIficDcwN63ntqnl21tSIlYZShAL9CwJsL9E9QpmiCaFxSvMSyv2GWahibj0plBzWNpPpDT4ZiaB3lBYu__TxvVxLDcyAAn3V9TUh0ayey0fvgIc3KKnuzJ00XmoJVSsoRBPiC_pHctPvjlRXpYwJ8lQlsBaiGIjc_H0-cHEr6JJ7xNT4xAxYlCFneu5WImyVrPi9aY1ZPRVsR-Oj-LwyUDgfqVA-Rpve1kVxYU2bq2kDTJVDf2lTInMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hUMR69rNQqyB6q7xQv9DoWCTbIXMNSofXE6e3tgDACKVsHrzyZZPAFHz1c0YmK4GeENRvI5oZ29nO1tPbXYk7tmhH9-1djWb0_YPoQwC6Cm9UZL7ZPXWlfjNylM9a4skR7NxKF1635SYxgdUDeq2zHVNdMkpduFdreokyvpgHnru9X214Sp9n_6ZwVbMwMKSMCQ4PHerYsOzymHpWadKUKdCvcnyhviXtpNYA5bmLQqifHt0iTE-QErp6xxvuzFidanTpu9m57_v9zeQIF9u5OgN-HfTc7nfDF5h7RpWgsAuKVOG8Nyh2l-hGoeo2qd6Y6ucD7vQthEAtAqXJdL6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyB9LPDZpS-o59Ovbg02R56t8WycQ3wKu8aGPvPM1tppAErQrLzMy5BaCQDQOo7cornSoKrJcsvecSp59bHgFiylRGqnZAo78P7ezdptan5D_DecE5vYe91pW0FmSz-iuGbGr0FT8Ipd6peXdFRdkH-lTpj9SGF3WejkJJq4JAemEJMU5er3QFlU8j7qKLxIBeMn1okpui6b4CeyrCwB5YD67VgY9DpKAjJByjgxVg1LfX9nxFNm3PFV_Oq6HDIUcGNxoj9Plg4Dq7N3uk-7Il75QE2kUq3dvb1G6QiR1shmmkOPFyzvma40XGOggymnXeYGsmsipLoFoxFQIlARew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T31TnDnLFzlF4Nwzc4gT4gCOwGqXITPdaxHLAJEJXgSb3MIhBatmeiTwOVVk0apYN8KWwV5QqqYINyKyfsoxQZt7rPEIVECGinm4gSi4i_F65s7GIcQb3T3FdlqnUb602JLZYW1i1pn56kB_XbmX37j_10eKKeuMOlD-OtT5gAggboJaqjif8ddVNrnmSB4YRYw5yPQSo3xh9eU9Qx6s_ZRmYhgwRdSaZAorc_RQhXmlKyBT8MgW0CBt7dWR8H5bm41xwrJeTOOyXz1nQ7XGwltkh4UavTDVrLzUA4k-TXxdH8ywJZ_kERHwAG3-WbZ15asNrR2P-Z0NtWE8J5Vmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RKIGLYO-804IOP7Zkrk_J_ERCaZbTm_ioEq9o4YDQK4SxKrle8SpgDpE-SzxQvsSWnPTzbMPSyJ7zPDQCVwG_ZYoYrImeibwseMYjfwm-sc0C6yAM-_8rWlHwhZ01a_fzluZCvKxyYPNGNk2bqs47lHGPA9ulbvdu6YlB3NPfEK7buu_32guA_tDzAEKMH0fEOkONNKHbIxLGF2vvTUaOJHULP4eCTeCaVetjj1CtTHgvizD8XIetUlxA9PB6uIPGldWIy28XksPIQVRzN7UIoBCpUtd7f16Eu0mkhwfzqaAKptIF9BWuVCOG-BxHwkkmOgitqHq79kLwwUrcD53ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdxbIaDW3jxGYy5edhu8qY-Ey_gE8S63Y4IHcd-pYyk8EhTwxBl40t06qpXyy08TJHnnRyj2tpJgUtRRkIF6QciL3NmKLrGmbl1dEA_9A836-MZqdPflunQ3u1xmL5rf0yQHqknyK1e_UinrhAm_aLwq2Vfy_NXIG5sGt6YtA7kpcqTwepy06eSWVeb3YjnskzyXqDu4ZqhUy16vIf6PP6RHIYhEpQ06MUEqI_1mqAiN0PNmk-B0dlHCqCgXstE8A9FMLKkOqvmTCjXcbsBduW_vGqaV0eZYmCz0_aka_CM-wSkhy65YKRp0-wBN6WEUiKgi7-92xrRLUmCmpcClAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nvbmxx5GzTQhO8iXJAe2jttmjUp9mav64TFJpAG8NQSMg7yOfPlt6WELtRFEiJPsc5ZkarKSpLEuexm9RDgj9SxwtASpbenGMCUBhI83mH428c5ooNl0RJM3lKxcVNoV8FCMiuFOaiMXkd4RXWDenrJsnaOYyTJXmjVoteqmH-BaYkct6RERAFwL1ZgqCC_T4hoyisHUTmZd2cnA3GrEh8mHgu8ehuTC384YgJPboiIx-8-brlX5s2aSNaAdLq9ZR301hT8YzZxz8OejEmRiBpeNWjmKWThX8ja8WY1Emg63t9lZyicWmOqsTZDTm-cs22dyqUbDqt8i3aG1zuyYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CME1QJvx1he3LtshRp_XCYPsIJsy55Fq7tuFZTzyQH94PwWq0PZVsYK1mhNbFFDNmZp0nDRcWZG9OqBEdvo9EWlcRuzcSm_TgxVMtKGKQv5bSfO4SeAUuV6YFvr6W4c874W9xnEs1R1h7ag219SLrf-5rFVTLEcJ_KI5EoaQtRkeB80D23quL_Dwu5LgQC0vrsk8YnoUysv7X8nbWai4T6Rin7joVPXdptSrW0g-1TPyvhwF7m0r-YxuHnvJ6Fdi62IOsern19usbGzh4RuUT2OhHJsiUQ2zaEg5vScP9UIDBlRtpX78j48-yEjjUePi-wZNzivbsIYlSTjDCMJyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tj4PQlF5QiUil1TCeRdacQW-lC1kfoTaBa84nsDCc_M9gAWZJ9mSqHTH2JeSm12T1SjXHXmkZgMhHeAErpAQuH_u5TkJieYxTwheFIJTB-7_CBMpDaNm_XntCTwTbzVRld1dJ_p8G8JZmfbFgE6_u4sDX4ruh0I9_Ye7XQP9_PwsCpvCEHLfErA66KvT4vrrmB16P8A88pdBuAUktVpoXuvvbW6tmecisuqEDj8Hqsi4F5IEgtnCLOqzaia2Kw52AKsxc9HCG7wyA2X5lYz0eb0chDsmHAyzKyyOq-S7Tvu7HYmSzys0HTfOPz5UJvT94-999uhcMWGRM99717_LYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IVVLjZLtbet4zEGSRggN-Cvw7FQA40zXbhZ5VACvsVix4YzRQv2T1grSGwvh1Gty7lqe2SIBGN1nPh6zoYet5IcsxL9RCXsUIMHEpaZsaleLfbY0zIcSYL5fjEkMW3qvW46HA49xlL_-Ifx9Vydg0aURjNdYaDuyiBVjsN5_aJk6rsU_1DINXifS_7lXFSzjGRbXKWzf1iZIY3IAD3gyvaeSx2qjZW0ko-wP7FFzcsKtItmPlpxnEOaA1rd41ZgkyyFPHm9v8X2n6w8vByQcdwRoZv2mtKpkB-DvZXPoLl8kvDNv-l40jY1D6Yd32FMn7lGqEDIC_SBoeec-f_O_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FVAj5fRTjoRWB1n6aV37asX3SzChEgchU5UhKyPeNkleDZW1TOZNtNbyNG0rkrj23G7tXTc0XJyUM9XAUNU6DIdlnk0DrxgVPzLxosQE7bQHSbgcmGzVfWw0nRa5S3W8kY8LPhVe-i7rwVzeetKU8aHNN-WW-LiOlqg3s8RPQaLIV8f63zrRexevaLDhkqpafvixM1yedFDh-DOpd-s_OQxZO39M1rPRs65DNXZtWarUZOqgzBaEomqOvrChE_OrZ3WFC4u6ZQJHlL6gmOUL6oBbXEXy_38rSiv-X8zNNGk4HeaKdPwVCDl-0hr4hfIDVzyMYzq2fSlQV0trt_JflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TjRJMrrA4oY6h-T6TgtroXIB6KfOFW2C0wGYSgJjp_ztfMCai6TGxS51zXIWKu7y_DXt0HnujWUXxuAT7NVG-QduUz3EzcoWvhjiwM20W2Y7yHLXhRNgasTzfycuV0LjBrjmT7gtfnieGH_snK3JwHQyKKB1jluVNcOKtpyn_wo38R2iCuZbz3kgytFD7Px15U39E3fFfasz1zrUn_KrUVQesEM_SbXojvQnKs71IgJvb8Zz5O0QhzUh4_FuvFo0JQKJUNCZm0aN5j5i2h0yNiyKApnAD6GqYHo77z6c8mFd-5OXtDgNsapqgKDnP8zPj2h6SrBa7LEt33s97D5yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qqvdjIPkE4Sv2ZxoJad0VoZhagg5gIgxQn0B7L2mMRNITvHyVEo6KamvU9VZ6e8KI3Fths5tAJMR_C6GkOnFqZkDMizkBKNzuW0k_g6nzcERCqm4ivcGa9dHppBTj5nx2tuCrA8ecMiFpocKQMbb7_2GtmUUIhW5-nXugfTqYAKze6a9PozGF6TSnu-pW6lU36ODDv6Qu_03O-4ZrPg-A3JB7RyZFTXXyXl6v86jzlhojjojR7ILcaL4zTirVHhmmTvaVcO1Vl9gNQi5X5Wd9qHwIY3FDBvUVdZsEJAnp-TJH63RPElgkXlhhqjxMXZPeHzNy_-eUWFSAautOgIivw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
مهم: به این نکات توجه داشته باشید
https://t.me/MatinSenPaii/4042
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WdVt1RXZiJr15LFFsGJ1hcFZuvFMjRj6xqsz-hTb4pYo_n0oFTb3vWj6Hl-UGMv37nRhZ9Nbb3XWd0Gj4FFRRwxjy1b12nFhTPvc2JWUg_u9jWXKV0lJoRUijV61q-sMf6_T_s23pyzzX5tVFZLmC6sh5MVgDM_JY2TSbvcIbMCZzuftyzTCswwKqiVMJsvzPhMx0dK_A1fKqfr1E8y-KycIG1y9TWk2XzWVZ3hkWeF-gJguu1frD6UFQ6B9DPsbbFUOz9rTKU7fumHKrHe90ws58GsJ8BWjALXZiV8lcGue2ucxApDgUXXds66jBQf2f58dShzNZftF5v59JtVgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jy7YbSkB0ttG2IJZknmzAr55Wyz36SsSqp-CuBt69obiXu8ZyMTdMwUfWQuPCMeovBX65k32Fb6LRhEqy8YkwVte__OzppZnh79fsvmeQ0aNJBA6I4Dl91snXRjK-v2e4Bu2OH0nEHOUijO83ZmPWAp3YR2-jmcjEQXWCiCQ6zBRNz1CYjtY4fTcP_88ULd34ScBpliUl_ACDuaEpKL8P5wlb5WY8ef5Ufq6VnasxXv0pg2HW9oNq3ViIHD930bckutPIcUjQa1Yn94Qb24ybNafhnah9GWWXHwSPmTJls3eryBRN1Wb4OgUJrEp1P6_b_xzp_6FzStQ6DioxJKCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuM8Rb1oGJ9QAhBws_XQ_YtzodC3KKefnEmQofDboXaXd_ZWftVNb1ZNWcFQyP4vzqzAG6Ih7uB0XfBNKAYNW_AdcvaPWkOEXECOxUMKMhOE2czG2JpPotckvBkotYKNvno3CyRACAgRfNaeWzdTvVVl92_bYGUjv5yO-LdJTkYhLjamqYl2WLtip1F4inwMWyLQD-3M0FjM8Z3A4BwYDyuQ1C9C0DFY58w0mRdH-5GpyJrhWxFIntzPLZSyaBDNEoZGTXWoQhdzsHseVtbGc0PsSjZFgU1wFfZmcCu0PUOZ6R5rHmujOhOVv0e4IpTLJXP8j1libRZqy-TkUTnvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mR-o64vZZPPlYPjd2Tvx7UL9ynEdoVO6F8E1hVsfyu7rI2IV2hS31nDKY828I0i3iuyNQDm5e0U0Yutxm0FdgMuKUe0CNHtemOME-9orDlIAoZok3R0YuzJgQlzYwvW0NnHQPn_Nruvn9Mss0DxIkJnnfAYWMw2M-Qqg8W20ABE4dDKCKKnp3Ckf4ir-KTT7ss8hdzmNRqAPZYk6VY07iYa3ox3VIxeNVjUsnTeFM-vpzvLAb-iKJGR2NFUKl33dbL8AcFNHokj3xUqU4T_2fZK0pm-TCrBY4FfFlWNt6lT0ahC2xaETIwg3c_lveOGInJKDI0Uszoae25jpYQFIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYughIPE77omU64pBFHlnGSZvBO8O_-DBBbNQby72b27mpe6IbG6IoqiHyJo1T9iGPokFPhF9ersY9E3J-G4ddLq2_A-hGifR5uGPpnyya4zGoFXbiLLBy1wkI4864QkKk2wyLNMaDkqL0irXP10UShpSPYe7Sgkm3oTl4QAONRHX8yt9p2FEknoFsDB_TjQTBDLqYUNNWDlvx0CB_hWmkSKdh7hJW1Y-We7ugmig7xJI4SS61q0Sl_BvHUhyRjgr5cFo0VBg4fAfsJ1pAQuL6d51gEfMJ6MSquVrS1pqNzY6mYDB9Mja-kBms-jWEtTC8nUziKDBHg4CFopHd8fZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cQdnefmgRr_2K8MO4QEmXgVHhWgl6vO0WQ7gG6i_oWOCbFjmFlQyW9rhwq7nGf9LzuE6XUUPGRLmbh8mf-IVe1obIPy_E33RyPECEk0yrjgLoFP1zy3jNgd88EcXvyyZAejTxuHZ7fFRJY6bZVmYTrAAi7UWVFBDP3AMzESuYcSnVTz1WzaicWRc-t3nxaZK8vm9ckyLU5th24g1QiOsjlwdkwjRe1lSfCRvRzR5mCyE5qszbNrjHSB8h8kXGp7g6Tp03b-m54JjubQKcaF0M08i9R4n0RW-hn88A9xHqcPJH9V81698RJ8mIQ3Zw9yIinp64e_IfPAErS5o-pWweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/imtVqvv48-Fd1NgWZx48n6E3xzWdxaPO-3ooeajsjnwqDWNwkLuJL70dBzO9p6pT0nmNfMQLojqCeCdpLZtzaQ6_xiGszl5BoxWQcMdD4qMcXk5dfQACzROAvQFUHpLBkcSv3r74oJzzeVLuhEhyr0HTIrL3uzxTCmestAQgrGX4x6RPM0Pg0V8NM5A5x-fIqlQ2vvSIr7I_eMUAVAl7pZpHcoMJtRJ_aGszDVn32IWAh8nYm4b592wzf82Os6og-a8tl-s-qnWxyXw6-oN_Q4FCYLoETBX9aDH14N4Tw5UFDiunIFsJh8KSLaQOrfDpzQqbO5uZtdCgKW46LAnr8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFAnPtYrPvis9oz3Vbu-NUHd0fVvlWMvs32f5f_QXuu9BvNm3097VKXqXAq8FORwTybIXKNVOeIuagfq44z2PyHL8mle_KemHpsjA18p9WLPzqYpfYqRLiRCor8F7M-36rzLRnjVIFt5tbsinYnVbGQGGx160PqzQDywHNMUoMdg_Ah75WKYTEtHSkJyUnZcW7euRD3tPO9PX4UILy_9-q2qJjTU_KDXik5591JabXWGDf8Uc58Z6lanRigam2OIYebUl_hv71-EOTIR_wGmjRxCEAMugrapyWUg43zgz61bDTsR1sjX_QRAb_0dkQAEimbYnkKEouBqciJg1fimJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IXOYgLPXXhbl-tHZBV3EOW5B9VFde2V9YUHK-F4s0vCXuaNxo_NYKUeU3rShx19_-0A_Xlpk8lM-T7XJwKLgBG3zEonjJKpAS2TtM7Q74ZNpjHM8vbD4M7MBPTXwYGdXzcKBjopG1KBACSO33SI4mFyuR8hLYfZePWXE09R0JXjs9Gr6sD4-0GaD9RcpmnZzmJdi038P7EJLMGV8qfOD_wXvigfj1Fd5-1ChN5qYyX25M3M_QoE9F-kWhCF1s9MjUWbrXBYvVM2c-4V4fky5lRD7r0kT5rboRUQ2R-C45-RxlhZlnTYboj6RtASda8VIPl5-LhdHNzbtgrQvpR7bgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از اینجا مستقیم میتونید برید سراغ آفر دیپ‌سیک رایگان اگه گیج شدید:
https://www.openmodel.ai/event</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3992" target="_blank">📅 15:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/3991" target="_blank">📅 15:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hWcJ7x5khuLoeCbZJLc6WhbfKPMQ-lhB73yDnfh5ourDQlpRk5WfAHTmiKZEH15wBb1rH7hcAQcrk5gev17bl9nKrC65Rt8RLMKnor5ORlIZv2rjOrrExE1SzbyKFQtgdKJMn267W4u0iu1Ej0VcwnaEEQ3TvBOfE8KQBLC87Waq6TuaCCcgP2zCPApA1C3fihb72oAL8HdxHaCBHevZbdHh-SUfu0koZcSqltzi1GO-a9dj0TJeVDGn0wSDJjmU6ERQ5WVfRBqdTzVd4S6_l6GWcWlPMqgNUsgwPkKmFNhcORTjDM0PcfF77zYhSybmSOdykYn-Mw1bY1KGRUM6ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال API رایگان هستید، OpenModel مدل  DeepSeek V4 Flash رو به‌ صورت رایگان در اختیار کاربرها قرار داده
https://www.openmodel.ai/
✍️
0xdavinchi</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3990" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5ve87ajNnHRNlVsk8u-dldAveyBZ6fIYkFKjTMVChvV8Yc9OiHkmjEb9kU6VeQqMLzIT0FyjvEtHKeOCP3k0jtPQP4qmkAV58pK2IsN7IH4C0xDuRhy1DnXzWvkP6jAnEYYdGAwllDni4CNbb7PMnXTD5tQTvc7nusk8yJSh6fqrLURuPJWKCmrLeSnJHtCT3TFtNzGXH5iGyNT_0YclaBCf2ztw-7y-X10-_s9N7hbgrWcExVYaY0jLLtx1HWW5P2N2zrGSvP4Jbk9H4cKSx22Shb4fFYLGYTV-88K2FD7gNna9P5y59CLcDFF8h4H_ZE6a7DbZ0tc03LtGdm1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..    Site 1: retrogames.onl‎ Site 2: retrogames.cc   @Linuxor ~ fireabusefyan</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3989" target="_blank">📅 14:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-upIz4pNqKiRsxLOqpIe4Haxrdzf0VcCLkhgVW8cewClbUjrn_USvlp637rOHXjlRtm3oGPIfiIUk9ZveGIPh8qBpOPsL14iAbHgQo-Ltt34MoOLZnIMfyuiJLr_IvsrhNcKI6EClSMa1W-27zD9Ogbf-WSKCfemiZ3BBAQwsOsluHP7OFtAbhB10pJsz22oPnx7iYRV3vt6K04bZRCm5goADe3P-OTPskjTrP9InxPsQl7gn_8F-IfWbIteGWtYBxwW5a7V0r3wx2rYaEp52YpbTeNckY8hrwpFNjunYENBpHC9CuN31QJl0D6JVtpPF8TV78phaJ_M6mYjXpHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت اومده همه بازی های کنسولای قدیمی رو یجا جمع کرده واسه بازی آنلاین، از آتاری بگیر تا سگا و نینتندو و میکرو..
Site 1:
retrogames.onl
‎
Site 2:
retrogames.cc
@Linuxor
~ fireabusefyan</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3988" target="_blank">📅 14:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده
اول باید چک کنی آب وصله بعد کارتو بکنی وگرنه ممکنه گیر کنی
✍️
ادوارد وانیلی</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3987" target="_blank">📅 13:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogvtFbFOLFr2cMSjxhiFh79rwoJyhZzYkgXi5RRIojXdNFBrBHEqZQZ5rfDqD-gEOfCOA2bUqyowRXWmTwQBNAK-yp0pqUt4pg15fuoc3eIi6xDQutf2_AMk3wsdFFQeTiB4J1cOooAipsgkziNSwy8WyqSnGTcabuIdpjZakk-qBYVR1FhuzjUK71z8OR0pe4N780w6Iklxhae88sqEgghsT6OKwFRAeamYs3dwiQ6bkWfZ74Wr5OckRnFnafaZ9FlVW-E0DK_3AM_bo111KhgZx2HuFf7jxb8LQBRXhIb1cboh0MUyQPu1U8hv7v5VUdG39ye--Z1jGxScVJJR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید که توی توییتر یا جای دیگه، ننویسه عکستون توسط هوش مصنوعی ساخته شده(نمیدونم چرا برای خودم رو مخه) می‌تونید یک بار اون عکس رو توی save message تلگرامتون بفرستید، سیوش کنید مجددا که متادیتا پاک بشه و اونوقت اگه پستش کنید اینو نمی‌نویسه</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3986" target="_blank">📅 11:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cv-Z7H6oakQHzEdQfWWxiwmzzLpd3MtF_ejxz8-DHbIBTSuW-U350XPljUIj0DmpqvPMqzrnfkqixb65FN4R3ocxvVFabjp3Cxbzmv1e9XuoR9_L6Kr14xdsdiGDVTVhmeHcrcb1C4zbe22E8d_Kq6yiBm-ADZWrLhIZ1CBCWWEf5wWp_IWHqZ9WLmRkUowQA35Y8LWqUACNebrHE81vTbsjKOSc1M7vXOVA5WtjqPYc2XmgBM3YRe6XxN7DOBdcUmCMDg_64-igP8UUME8DhhFNq-megtyypTkKGHkthkRC_uP7H5RlaV-qw-AvOoCvGHQ52GFLZhv0PWPRdL99zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیستم بانکداری و کریپتو رسما تبدیل به طویله شده</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3985" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3984" target="_blank">📅 17:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3983" target="_blank">📅 17:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Iwana Proxy_1.0.apk</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3982" target="_blank">📅 15:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIwana?</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Iwana Proxy_1.0.apk</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔰
Iwana Proxy v1.0.0
با این اپلیکیشن میتونید به سریعترین پروکسی مناسب اینترنتتون متصل بشید
✅
آدرس گیت هاب پروژه↓ (اگر استارز بزنید و بازخورد بدین اونجا ممنون میشم :))
https://github.com/Iwanian/Iwana-Proxy
مثل همهٔ اپ ها نصب میشه، ولی خب
آموزش نصب ایوانا پروکسی
@I_w_a_n_a</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3981" target="_blank">📅 15:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">با تشکر همه‌ی بچه‌هایی که PR زدن و مشارکت کردن توی پروژه تا به الآن</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3977" target="_blank">📅 15:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3975">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VIxITNOV32wjSrvabC4SxOsvOZBLsBvvvWNMCPkr94c1j1AHsLkXFa5HK9looSsc8t4006VU3PgCjS7iNDia2bw8fW5niUIHXIkCZoNwkioY1POzyIUn-wfbPgP6WfyFImtY1BtBlanMWGkT18qrQGHNIohPHxiXsy-Ev6fsJVIM7cPo_5kbPxZIpPNBM_JYn4Brq_cM-huZDr3OUZWWC0-ulg-J517tBuba6mF8EawQaAvbIslsmvUvcE7YcQHxhpr9PsAAmHLUh6y3Fs84aJDfVq9_0D4pvnw27K6l-aK35U9xRfv4j0m0nsnOgjkcsvBS9ouMX_qWIo0amHzcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIUdBSifD7E0HimECXM5jc-_YN0r0hWIpL7ehBZzmlVfpMSYi4SN2PVJQAM5yXG_pbTg_r_jMkrRVaKGoeaJBJNd8uGks7TBXttx93ZeM45ByTgD6gFiDavceEEtb7pilkMbRGX9m0a6OGqe8ZeoEz0Gte0rh8F7wmY_bcdV3uvY8v76ZUq-NL8Z2w1QrWgbwDTceVm3DNpcT89zqQHRIdTV9cruWR0FYqJ5eWFqOmBPSSl62iE13sN72a7m6YADNUD1MWq2KtrNhw-IhdKEcbfy3Lnj1xssKh8UlJ4vqFVurHSQ3S21WYA4G6tVo9YoxMnoI4m4M9Y1SDLNljx9dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متوجه شدم که SenPaiScanner تا الان بیش از 60 هزار بار دانلود شده
سایتش رو هم
Samim
معرفی کرد. می‌تونید آمار هر پروژه‌ای که خواستید رو چک کنید:
https://github-release-stats.ghostbyte.dev/</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3975" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3974">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3974" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بانک‌های ملت و کشاورزی هم Came to the party</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3973" target="_blank">📅 13:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3972" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3970">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XSKqav459646kj29rifCXQ1Vc4-UC1_DDiWKm7g_01PPM7ibT_3eSxPhH2U8HmTR4wVry8Q50K61T3Jxy5rsaLtMpgVvs9VXHKXgUaAH7jte9BWvhJkvNiGOktsqbRVV0GxLpmPoomeigafjDUNfD0Ui862NAubyUB-GolHcANM-f2XWT_Kv5N8tuSEEN-Wjb1eEkS_nI0dkJR8aisscEMxlCNGtVg1P_LHbI-nvk958CppovO6VnHp9CNwZHXwG-QhBPv4L5iA5fbV79QILE_b4DFjL1O8mrihBlhbNPdfpGygG0sAh6af9muGB2dmpkHabYHUWlmUiHstSpxrBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kuy0UdiSqIqm_Y-UyEC_4Bsq3eqQHLeSy3btjbqHidwxCx1TGtTd3dinrFsNOzfoEnhg_vboANS-53PNPvMw8HwYT9e6VhukPANqo9yaIS_ap978_Y3DrrIhe61Wp5y5SdHu_FFW_s4juChckRqbbtbvmuutRQK2sAgDlBOCePbxzmXrCYO3LQuj9fmyyIuwNeF3elLMV-9zjzCnkFjssGEtoA6-1idRfGhiJolMV_8JLxkIji434t6xN-qjMDZM_Q9k8UcYCD1W9uneYnB5zCEqiKyLMXG8ELTNumnyu9345cDyzFdXOC2WQG7Wuy4QHsJmzeb5z3a9NkVJvCAAqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس اول: یه سیستم که تقریبا همه‌ی گیم‌های پی سی رو بالا میاره با بهترین کیفیت(عکس از
glock saint
)
عکس دوم: لپ تاپ tuf a16 ایسوس که اون هم خیلی از گیم‌ها رو بالا میاره به راحتی.
و طبیعتا با لپ تاپ شما هزارتا کار دیگه می‌تونی بکنی که با Steam OS نمی‌تونی</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3970" target="_blank">📅 21:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IsXVBh-yYcCN11ibLM7HkYq9B6pooEIYyMG31c1Vp8XytnithjalXtZWpThiKSlqtlBL4lHYyS4HiEF6ZXOZzKRLDx9xZWea5gGXlDyXpXMPJlm0hukRR_JXBATCVbetU3L_Bisk_teXUWRC1QYXyhsDGtwdXoFh5gR86mhF80IEeVCVCOI36JUHtGl2eLNtysVl1TK5nheJKQ8LJEz_t0KVJDUayZzA0oH2bHXLHypiQxhJPsxGgc4RFY0VZ2DLgddainPdKdqkWBWPXSPrVeEpljl4gClOXizPuiGjg9E56Fquf27gBz56bg-oVx10-LHe3Q_hEDvJM6eGRMCyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tHcb4GLqT1m_d_siumiSbnNNYGf_BWLCOAxN2KUPKpycUPIPDtEIJTobOXVqDZxhEfmS5gri1sNZjyidbJtb9PGG-GLMorfZGL4B8ZowjYr-zalLAENL_SpxLeYXrf7Tu5RcyORIidDP1R4jqnRnAVxGfE31TdIvAZEHBPesEC7l2UB-fvLreC0UyI2hLbFtvjFNz2iTgOnvQDUVtMM2wv-UKo3jIj1qIEjxd2mTpK55fFNu1ihe7aRt_KNTyjzGiqTwGrI808sqdbEASRargGwJFIUSUiUGyFhawu9qQIO0ggvhdVodML76WtlDjHAcZChDy_tim7xf594ocquIWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنسول استیم ماشین معرفی شد، با قیمت پایه ۱۰۰۰ دلار!! تازه دسته هم نداره باید جداگونه حدود ۱۰۰ دلار واسش پول بدین
🤣
تازه پلی‌استیشن ۵ پرو با اون همه دبدبه و کبکبه قیمتش ۹۰۰ دلاره
نسخه معمولی ۵۰۰-۶۰۰ دلار
خب خارجیا می‌تونن با هزار دلار سیستم اولترا خفن ببندن؛ حتی می‌تونن یه لپ تاپ tuf a16 ایسوس بخرن.
چیزی که دیدم، کاربرا هم توی ردیت به شدت ناراضی بودن و انتظار قیمت زیر ۷۰۰(با دسته) داشتن.
میگن که به خاطر قیمت رم و... هست که انقدر گرون عرضه کردن، اما هنوز هم در عجبم از قیمتش</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3968" target="_blank">📅 21:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه سری آموزش راجب ایجنت‌های کدنویسی قرار بود داشته باشیم به زودی، منتها لپ تاپ لولاش شکست و دادم تعمیر کنن
😳
رسید دستم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3967" target="_blank">📅 17:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from᯽マティ️️ン先輩</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=Yyt4XS9dUlh648aBOOCxDA7Ei1BFEJCGyTKLL_igd1hkyq379LlJpkcS68ISJY-KvcRQ4jy9M2bZRF0oLsgAskd4T5BNL-0-G2MPRIENyA05LlyoK26dUU0vu1kHUGyXr01eF2b_eMWcUD9sLGqOZF-PshV7AHjPQe1o0lMsjyTyqHwifyYX7bpEqTaPIjjTwTWzMoycuIJNhH_3jt41f1WiK0Lf1PcbJ2mqANFg8GO0FOmBrJ9xBgnj9lpisEgmZEcpNDBRR8w5pzEp1UBskWj6a3rHnjGav5aZ2D83nk0J6qI0wV_HMBRdwtRkJ9bhuXz-eMGc-pe7AV9Zv9SYUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b23c2a33.mp4?token=Yyt4XS9dUlh648aBOOCxDA7Ei1BFEJCGyTKLL_igd1hkyq379LlJpkcS68ISJY-KvcRQ4jy9M2bZRF0oLsgAskd4T5BNL-0-G2MPRIENyA05LlyoK26dUU0vu1kHUGyXr01eF2b_eMWcUD9sLGqOZF-PshV7AHjPQe1o0lMsjyTyqHwifyYX7bpEqTaPIjjTwTWzMoycuIJNhH_3jt41f1WiK0Lf1PcbJ2mqANFg8GO0FOmBrJ9xBgnj9lpisEgmZEcpNDBRR8w5pzEp1UBskWj6a3rHnjGav5aZ2D83nk0J6qI0wV_HMBRdwtRkJ9bhuXz-eMGc-pe7AV9Zv9SYUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر سعی کرد عملکرد و هزینه‌ی GLM 5.2 Vs. Opus 4.8 رو مقایسه کنه. و با هر دوشون با یه پرامپت یکسان، توی یه فایل Html، یه بازی Backrooms بسازه.
نتیجه‌اش جالب بود. این هم پرامپتیه که استفاده کرده:
Act as a senior game developer. Build a technically impressive Backrooms horror game in a single self-contained HTML file. Embed all CSS and JavaScript, no external libraries. Raycaster (DDA) with textured walls plus floor/ceiling casting, 480x270 internal buffer upscaled with image-rendering: pixelated, infinite 16x16 chunks from value-noise/fBm with a guaranteed open street grid, procedural textures. WASD + mouse look, F flashlight, Esc releases pointer lock. Dynamic fluorescent lighting ON by default (never hard to see), warm yellow fog, vignette/grain/subtle VHS, Web Audio hum + fluorescent whine + footsteps. Psychological horror, dread over jumpscares: footsteps behind you that stop when you turn, lights that flicker then settle, a far silhouette that vanishes, rare spatial anomalies, randomized timers with cooldowns, slow escalation. Save position to localStorage. Return only the complete HTML.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3966" target="_blank">📅 08:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">امیدوارم جای بهتری باشی الان...</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3965" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3964" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1IhoBgkfJWWxKHEdijvWQBKuqOX_wZ3n1iZCJcrbhr6ltUSGwMBRk8XanDH0VmkkOVTJkhweHn9P8qPSiJQUpafDVqPN1SuWVmDdeAvanabGs4brbUOBTUWIbeNC6cBBE8eB_lJkppsOUpu5jGC4aAFB6PGmcaP0OMKc1rkERsqUiz2LiK-B6rALCW4xuhhNC3BtELlxjSvSz2sbtvKz5CkLcdvh6SMdwa-3JsqYkT2ufSqwlsZF93a00GRrNa2QjL173-CQ2CYURnMABmz7uy_Lxi7l8hz8lT5-YV57FW0eEueWH7BZ2DqEiTYnCMiKJlBoF7qFP_psSaOqOmu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
