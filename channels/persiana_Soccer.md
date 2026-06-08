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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 171K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0MPrhWISxO6oYWhy4nGiRGR7Fx3tXst5lw3DiYcnsevXcD_lXSgOTKgll59r5gADQYe9X-ijHDU8XsTFwBIHsdXJOvl7kZuvrlE2euoSWDsqeZNe-oVFy3ExVb5tNL640kwil1PK0yxRwfbk0kBOCOaMflO7M1I8A-Cd84sJpcwfwMd8hebqMMzQRLl7gWAY_qLG8Unben2n6pL3Am6x0DUx-hB8bNVzLKLtFPJCqLO1P0aMBhQoGjfV2jifjcXpjQh-wAXnplQM0xL6npZuHBwH-3imRaM0MreqIxJHNx-2gR7dOqYFRxyvM_45UJrkA_DIhkIs3NEHj8clGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7q-rGHBgR5xIrV7cr9jpNUSnCKLtfqAgLMPG_QzjTdHEo9m1g9EGsoa6vCBD15KYvnvnGZL0nZ_q6yU8WJUuYoabt9dmT2TTCWC83oUSX7qeX8rJ_HOLI8t2Vtx2VN7ez7gEYjGd4GA7hcnasFNRfNHecx-Jdp-GLbWldBckT45XjPjqeW-cgX8U3Rrss3C-umQngN6c8CcFcssJ2f6CaG1xghb79l96HQa88OFMw7oiNVr26l7t8SpTmVFNsaP4A10503jYuSIoGVV6gLCDvDV8AzQ-WsdFd9BNj1MJQhP1mr_kYGNSb9cNb7DhvtMX6LcNw7_AIwjUwZCkP_dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3s7Pqn8dZkWsMbiqN5lgvl2TdRBTxonj38inyyxSbprHaP7iRW1iiaNsu7L4FJ_Ecn9ij8uEV_RwQG2-C7HF5NZLQmEkR0wAXtmomvJlilo_qpqRtrKNcbbXTIVP_bF99zc_QPQmKelEud76HKh6S5UYPLUjUH8_cwGsqsepEen9L-7JOG1zi5Jya8D4y1wLde_2XU8LeSu72iWDs-uPWXzcbmpev_5XYgABSPgfETZwRwLemLskbu2z-Ngy31Br37V-DX1jNSUWZnC1-BBnTyQannFTCXwm67VcfZjxQMjIYowchS33Zm35BUsjQEBheJFgnMqk_TZIT6dC-XJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if78YwhdSQxhgOn04K5H48Gi3etGTAZFb9TJ8PW-4rJ8j43UWxobyINVjDe7vRmGrhnqMh-AaQbcsHkj--YFqF857gZkQhJ92eXuUlG-9OWLqINNTqS8BB6X_WksjpdK4tSvKbHsMsYDUHZGs7LvLC_W9twktzvtkvtl-vIHMi_AFMNcsl-Kg_TjBztvrV3t71Bp8e2vFwPIAGwsnMgA4gEdi7d73yOFHm6lOGF8iEtAEVjT4jmSYdvV84O2RQcvGZ38tGidoHGDBLO70bO_YOsc0T3JqZUHVeUuHuJyVIyO7yRDCPcHrS1zPRynA1CKfjjILyO8jPZSO208pdUMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با 1 گیگ کانفینگ بین المللی چقدر آنلاین میمانیم؟ خداوکیلی‌ این شرایط حق مردم ایران نیست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22990" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51L8pvwybOBjv2Leig4GykKBwj4IHde_SQlye_pIahCAU1MIur3w0xGfFRWSk_M-L_kla3RqmuHkOexRu7v1X12Nxm-r6zMipfiK9tWrG47KqGQ58v-txZx_XXPrIaL8fV9bi8zUumhxek2-dVToQzgZUlf9ZW3XQAgEvLaTHipXmTp4IUDosWJArKbwJEOmtFiIEaGK-SZ5Q29Jw3xZszXr1tatK7vBZDGpW4Lvm49VByTas1K3u8-n1zFG-ob17V3a8XGdxnT0T0VACad9SJQYhQDDlS_L2zgJfuzodGsjOT_Dbms4hsuZZuTOK4aWg8DQGZ8WGDv4wc0WLLGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HroeOGKFzmue2hXxkbEN-2eETIiF5RmjA5G-uHooE54NdKWQKUpdY4a9DNu2MA6FfyJzwDf3PSsAM70e1PK4zGpZbqFBAoLoBiksAjXwrsCS1aziHJw9ETXcZqDkRoztmmiqBEvDxbzG-K8m9JQAPh2P8PJRJ_LSACSIplihPhx7w1aR9DEQeJN0NWBODiDwf76_eH5E-iFwKEfZ6os8wmSrOQ0C-ImIzon3-WH5lNzYU-9JMGh7iFsW9VkYcS7Xvg1PXrKoBavsD_Nq3n3KQPfqjhinhA_woJEoD91bjKUYjrhTRZNQrbTnpjWyXW1_cM-3WAET965VzP12ICa9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PChUvRqqhNa_4Is8T0QoRgpQm8s9rnmu6q3qV5FxN144zetcl0fvrMf2DU2_7MtTqhvPke0QtFy-SDRoQFsHAOheh0pLngdT7CTIO0GNyNAPKr4b0GKnej4CwXnXTM3ARj9SSGcB3mEVb18WHeInYJ38LB8fasG8eGIFkDxAojEfEvEYgsLloci-yfqipPIp5F31Yz9__D1dyKCxs7m3l4vIuI3OvmfsTxxOU2ck-6lEKycDUjFB2GWPKpNJaVb45LQZYxWHGTwok52tsZ6tFe_4A79r0EjRGMZ3i0s2ktnYRTArXs7piBJDzDOJoPHgB1wZjbUBo6C79qZiu_uRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTAKaB0cPjya096uX43_1y9KYKgPdLPY57GkIRoyipS640kEm1muxSBrBRyX0cBqcNS61FpqlMtUEo8p-z7TFhwvH7BoWN7VR2agKfNMLrOgU_SWY0B-PkrWWIJoGaUm_zm_vqbCyj_GgfCV_to0A2X3UmI6N2fvp2Lcen95mFkyLZPIGvRiyNAEfZDdTcmM4gceWIOzrTDXbOCO7vU1jX0-WYUwxeluQ4tXWAGeoVnMDzKzG7tlTOnquUQt1BQCGbIifup-u5yKusygJ_hTsGUUgndY6Gee_een-otYss1glHH7n5zdrpfUJQJSCtjbruTQlcQ7kUTQZuyNd-Owwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=u9YtXgU6LmwxFlv90YlXSjkatpQHXJg2oKb6QvOuFS-oB2M_roqVIU4jE2e8JLwVh7oJQcx7xwVGA7PbHhwrkOOjjzULOhtT9TfSCkuPERRlNNxvMwPnDV0KES-xpt3UEWOCsUlW-YZWUGnUhic2zpKjekfk-ISrORbIVJ9pPzJy6T8nuo5Is-uq9xjfIdei58Vz9kFzpSSTXb2Z57dwTkBepverwT7qbBY4fcyip1hAo3MecStKTL760QW5j-t2CelTSgFcCjmcO6xtQtkb5C9js8jl1ezGanUXwq4E29WAEq73LIDJdcylJt6DNEzuK9K_ZdbTVjJ7d9t0Ws34FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=u9YtXgU6LmwxFlv90YlXSjkatpQHXJg2oKb6QvOuFS-oB2M_roqVIU4jE2e8JLwVh7oJQcx7xwVGA7PbHhwrkOOjjzULOhtT9TfSCkuPERRlNNxvMwPnDV0KES-xpt3UEWOCsUlW-YZWUGnUhic2zpKjekfk-ISrORbIVJ9pPzJy6T8nuo5Is-uq9xjfIdei58Vz9kFzpSSTXb2Z57dwTkBepverwT7qbBY4fcyip1hAo3MecStKTL760QW5j-t2CelTSgFcCjmcO6xtQtkb5C9js8jl1ezGanUXwq4E29WAEq73LIDJdcylJt6DNEzuK9K_ZdbTVjJ7d9t0Ws34FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22982" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkeTgdkyu5iY03pN_dgYnPfCWS0WjxLcGG45WjUm6-4FJ93RWvgWa-Runxp5V57T481w764HJVtF3LCrDvbGl9Pxu9FE6PaBWPH90AkiepSjVFSU0pGT2v2k-mfO1B0ND_83bRThepfWpUcrxgMBX0yms85FDu0BPN15RMF66Izw_ctJVNrQVWs6jvyJttj3hplbTeOROXE-UCL00iWCsVGIBzty6ifO0mB3cRh5Jj6_STQtna5v2yKy4O1WPR6ttx5OjxT7pfZrJGbRVxfF2zXIPMDmBRf738BQ8U19tcvR-PB9tCGqcAe0k4BHvT2fIKeJ7V9wyNJ3YQFYZ_-YPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABFqe0H-uFihG2HaTn2h9KSkStoaz-YIQORI2yTLezkaEhx8kyo2Ip8gqUPEDDPdEfjuH52C1ADBTZ2xXpo32IVzvNId2RrPENCDTYfSr0TkDfAOanSDh5l19A9XUvuXBjw782c5arQx9wXmtH1J2JTDXZ05y719QlVpMN-RLkT6HtUYisvpI0CykOqmEnBTZelZbOWZrBCyevqlqmALDoGY8qZ5RPsU8uiPkHtZ2-C4qUXRaB5wZCOARuTr03umSZIDq1HZxqv1ACwJwcN92gSqiyvwAVBW63Ffol9miGfxKo9kHB-61y4WtE4-kmnyesIxgD_q8VUprFGNu4TqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzAkWB1DsOlrW_k0KtqBK-AGZWFeDPsnapwCm4Oayl4U9loSg7LPYostj_PBFykrWEoRaG-DdKviOkmmvgJIp931TMC565A6UazmF99Ywz1sLNXiwNITFCByyg5Hnm1OXufve_OBN7x_0tJFROYvRQT5OZdXpaDvLsbr3fuxsO3BJxVqV-WBs5KtlEyKiXp_95oPUFx1yL4FnbEUhYv-D7Tk0tgZENh80s7U3JaoJw5gKf-c1CoTm0I_ordSISx0WTkE7ZLwTNFU51l_iYYb6Me_Uy_fEDwkH4NyyT9S-49cpylZnuLGx21vQzCu08t1vIqiSMHyKrSBY6Th3w7AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIE9vQmgE1qoW2rf85IcfpRiUndCYoGEWKPivsR2VDHq-gw1mUkuhjT4cKqc8kAXYVDU8oWrc2upECrAFYGPhorCxj1JF3ZZlL98DdKWm06BxAjIM9HsYDcQKZoZYRSGdS_ebokRiHdaJMhmt2Tj4Nzi-86PQ4CWK7i1jhrG6_20165boovtfIlZkvkEXKzmiBW7W_R0PLyv3WXLGYbVozb4AVDOIp7v_BwN45j3OA1kVR78MKNLC_44CVyZw49P1YIENrtqVNfyrGzZrhka00VZ7DfnSUqK5CefqfJC-Fndpo6VkmPm292Tp-G1GaYYvqeDmo-BbU3KNHxj9w1MwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaQCrrPK8s2Qbqv19fem8IUU6mEpdT0F27Cc8hi8AW-PNkZ1UF7JEzCjxls6Icje2Bhwx2QYvTNLTmfQA09pqMX3yy2UIUxmnVhN1PkpA6nFHds5AWKZwBDf4CuAek-SdOponpd9gqRnRFSD1mZ9_qs6CLc3qrp7mYuBBrkrll2vMXK2-aLGHZennjpK-8CzfrucPas6guM3O-OvLHp3hSTIRQuz8wWDuKi483c_ll30_vZfFdfSkul3KESfYq9TSVJ5vau755acbMEtnLvRDz7yEUEHxtAXorUkhNoeTQ_UPmcNtyNQOjrK0kNTyTlMdjD4iQcEKwbeNrEll1rDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epXM9Z743yxwr9HqDlH8gMkJb1hQppwcLqE6Jua8b7aFsSP_0xa0S5walrqQhlIqpDweROqPeQHtkLubQxbEQuy7VughmlxLdA4njIZmJjzNG11L2B6TUSaEgJF4HbTiuAAOi-qSpJLvqcTLmaJBLZp34k7SN2b1Jzb9eWJBeSkFC7_LHmsoijR-ib5LTS7Ycp2vt9W7F1bPoPdPj0RezIDPEVGQNdaJ0zGpgvCwagQ220vj8Vj5cUVLLS6_XY-XOMi1i9nqAZz4xvhrfimFp0EvX6PFGLMwaZM7UggBoUYKVb_oEBTn9b1AjFpGkych48omXVBcPvQFjEeBT2CZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH4NGGtslGiOpVbFM2qU7guRchiWiL2u8gdLXj3hW__n3xUjKL2f4KoCqOmDo3hGmvQnezxCUFuH7hfVPFs-_O0PNyRfaF6quXNhqYE0FuQXFVPw4xrlxOqkd53fOBM3rOvWOEz-rQTookPzU9Fk5s8YJxv2PTyrXsBVgGrQ1YrQ6NrT2xWcXipWzkjEv7X8GyeCIX7wkqjtUsxjyszuS3iei3pjW--Cx_dLfB1yNVeY7NJY1eSRucn_IQuE2CF94eJRMlYo5d3WfwfoxNhNzXvOU211ejzpoAb-ofxkrSydPn_HwKozMfZxrWSqomtiCvA5DuNJ2j7dxAvfs9-8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q88iFgAdV9f5DsmgSTXajP90NwILN8UwZIKSpATBC85s4LSfJ4JqxoX4tDiLBs91rd_Ld_rci2vsw0pvPal8omDxqdfpZ6HUNlwIjm8OCidzyHH5dTvNQIxSJ0ELTQSlGotq38v9HFhXTkfDpkUZhuJR4-aZHy0N3Q8o1K6O63D22lEme_qxcN0ilvhna8FWLf9h-L-z0rCDTdG05240DIva-2cDfiBUDh_i4RnQeaLxuepzX4qC3lNOYHFzsveeIFrBh0tNDaHa2gNJBkqO69hVZuE9WRm3eVpb2KSFYLKIZ1vs9-hQj70uH50lVNpSnLR22hqvjWRuBcmqfWIV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsg8CEDKDyY1pUG7hP7_2DDQbG4mcF5iVS8GuNEueNSkInR6-_jDYxsiqfqBz395Wn7CjozIoTyX3a1ZoCSjekYyybx_4UqJs3hL2CSDfY3bQmcnL4_hN-lHo8uoN01FW1EltoXhH80PZhLEF62M3GTGyiWXv-PRHmxTm3YfQffl2t3btAV8pyaa-zZW8yndTUellN1WUPS4QFFNErpKMK3Dm5ycou7Xdg8fjq0Ig_vqLnwUoANQ8IMFhM-H9-uoybXRyPPN3woRpGDNcogrkv9cjoWz5PNgoOpBmFEQxv_8mY-e8zhN_kfy4w8oJ0CMYbggJEY7EpaVzBLixCKHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=VvoOhBOqiMN6WjwJ2h_SyfD0lZo14flYy_axPPKfPZ6TXJL14nayypH0X5eG2pKECizP1ik4x52gHOegsiwkPTxP8HYMhHB1FvSRghMui-VAelXOqvd2X87FS9_rMlakpjGz5B5GCdpb6UXSG0otjo14RueoV6cckRY7rjk2wqa2KNhrYZO5UcRsEhQW2oZ7-sncUMtQpElysPKblRO7iMBSsGDkYzBurK4NvSXiWvWEITrrtKiyFITV8FivRg8Rsf1zEEuO2gH_frnP1CNFcsp-KYVIYvHvZ24ZI-fXjPVAoOw_v6Pubh9ACUAtayFksav5h2Ih60U_9EtYBx3JxXzzKZX5stWgq3QjDVXm_d8YLEdWuodl0S1nuDtueQC78s5rSYD9J0iw18UwEM_H034hLwqyc87IZ9ufdj4V8B1MCATWEgWSk5qaU5gIdbdhEf1SEPcnzBP1blKnfU9FkXrWRIItyTs_tUwOMW-chECuBI8wPxa6TNlCsHE3CYwPJVgD22s0Sq57-wa39w4nRRLs9hyotuYpTO5hgPeABYphrHOF39P_ubsZuU75CpjbXuR3tPSciQ2c6ismurxXztlhMTfa3WZPmIRzdzv8X2pDS6f9TqKnPg1ak-R1Be7yJhqTsvSQ638wOCSWSXUH9h7JK-06waAnNrHTo-JsWlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=VvoOhBOqiMN6WjwJ2h_SyfD0lZo14flYy_axPPKfPZ6TXJL14nayypH0X5eG2pKECizP1ik4x52gHOegsiwkPTxP8HYMhHB1FvSRghMui-VAelXOqvd2X87FS9_rMlakpjGz5B5GCdpb6UXSG0otjo14RueoV6cckRY7rjk2wqa2KNhrYZO5UcRsEhQW2oZ7-sncUMtQpElysPKblRO7iMBSsGDkYzBurK4NvSXiWvWEITrrtKiyFITV8FivRg8Rsf1zEEuO2gH_frnP1CNFcsp-KYVIYvHvZ24ZI-fXjPVAoOw_v6Pubh9ACUAtayFksav5h2Ih60U_9EtYBx3JxXzzKZX5stWgq3QjDVXm_d8YLEdWuodl0S1nuDtueQC78s5rSYD9J0iw18UwEM_H034hLwqyc87IZ9ufdj4V8B1MCATWEgWSk5qaU5gIdbdhEf1SEPcnzBP1blKnfU9FkXrWRIItyTs_tUwOMW-chECuBI8wPxa6TNlCsHE3CYwPJVgD22s0Sq57-wa39w4nRRLs9hyotuYpTO5hgPeABYphrHOF39P_ubsZuU75CpjbXuR3tPSciQ2c6ismurxXztlhMTfa3WZPmIRzdzv8X2pDS6f9TqKnPg1ak-R1Be7yJhqTsvSQ638wOCSWSXUH9h7JK-06waAnNrHTo-JsWlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=sPvGv-vkOODcw3GCBhNwhDXBRL5TwOY2v7W8FVEJRA7SMzois5VGgA-a14SvTO5MQkoGNa4PugaR1YI8GUSh_C5vk8HvCUu8AuKl7LbHK3RtIWmGKhkzLUEDd20tA3ZYsMHwtexY0o3C85oiNrHMRaO_DdhJll5Kw02RjHMBI-3TdaNY74UNhHN1xzTmOxZWOpHoTnsGHFaLHsqzzoWy6j1GkFtt5zHbIoZn9vxkaUSOUhf0c5j2xS-HdOOJyOE4cxhuIeRKtc7LM4EdyfMFj1Om4LF2LfufADhhUHx5sTI4QOY9VQqMDH-VfBmUA6uO3tQILvylWUrTPaUF37S7Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=sPvGv-vkOODcw3GCBhNwhDXBRL5TwOY2v7W8FVEJRA7SMzois5VGgA-a14SvTO5MQkoGNa4PugaR1YI8GUSh_C5vk8HvCUu8AuKl7LbHK3RtIWmGKhkzLUEDd20tA3ZYsMHwtexY0o3C85oiNrHMRaO_DdhJll5Kw02RjHMBI-3TdaNY74UNhHN1xzTmOxZWOpHoTnsGHFaLHsqzzoWy6j1GkFtt5zHbIoZn9vxkaUSOUhf0c5j2xS-HdOOJyOE4cxhuIeRKtc7LM4EdyfMFj1Om4LF2LfufADhhUHx5sTI4QOY9VQqMDH-VfBmUA6uO3tQILvylWUrTPaUF37S7Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0MnaXh1_IFicR_6j7co0TyHJToiYKUEXI4eGWsCjD0XZ0GWyikuPpE6Kouzh9lAW9wabDO2z_f7kgiU0F3zfTMXfgsArEpMHGjcwx32ht3a7FexT3CPlC_h4G1KQjo4qvTVTLDNf5Od2LjGaQtMSuhHszGRlOwEXpfl8enJm5rOM3VNLE5VpcktWXtqor9Qtw-tJR5-fYxj5c0XzkXzMx2yyEoODZTsjfVL2VJBwtO_u2p0EGLC5fARl_4RMObAjZdRyBpBodSQaLOSkKSpKSKdue6PKb758gBtKmC08wlZxGiM9C-2Do1OxkIdvJTrvmZjv1GQ_71RZzEIyxD5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22969" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq1RjzQn-wZ8b_E-cZLfBKX7Jjn9aORmGj2kZzhCkgnhoAfmZfW7dbqPpQraKxOP-09V4NCkhbW4gRUrEglPd8ziYb-_PFXHJvPPVkAutHPFvkMNTaFzhE5d_NvBFa0-P2F0oZKzqlqWhytql4hSfj0iF90gAouDvB1B0YQf9OrL0m66SyK3jMUwEa4SfAZh_jHMTUB8JSX6NBZh1209H2PhMrP9bRNjkXjQVwpWt8pRQ6M8vFOz8HBzp6QCWWnS6aQCfF7gGVTB3He-Gt6DTRRqm_oZsSX0GZ28Kcc0huvJQ8qeAuPqg-Dhzyoim83K0Rk7V0V_WbddCQTio4z9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=EpdOlkOInFblBRhvXt6CjTC08aIJtbaj0h5BKXk28imvK5LCNuXhLmWWyoAnx3G3q1b2Ku1VbPgGiFw3ulQF7vboKlC4Hvb-NBrBw3yzRR5kImTLg8fs6Zr3T8w1WpaFmzBSwbcGuxlw6gBg72NcCcQCnmEKyMkf19F1b6pHYOdMxkw6U4WGaN4LvtiPknnA-w3MMHXQhBmkYHB0qmdzVECJFBTkWnfPl1qnn-W0teaHMyePRDBPFFhRljbsqkSHE0hQRcatn274pGMlX0uSt4E4st7xLsO9Rs-GsLbHaIOz9XhwKc-W1boEeNj45fUzci4A1LAZD1AX4Xos4yfMuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=EpdOlkOInFblBRhvXt6CjTC08aIJtbaj0h5BKXk28imvK5LCNuXhLmWWyoAnx3G3q1b2Ku1VbPgGiFw3ulQF7vboKlC4Hvb-NBrBw3yzRR5kImTLg8fs6Zr3T8w1WpaFmzBSwbcGuxlw6gBg72NcCcQCnmEKyMkf19F1b6pHYOdMxkw6U4WGaN4LvtiPknnA-w3MMHXQhBmkYHB0qmdzVECJFBTkWnfPl1qnn-W0teaHMyePRDBPFFhRljbsqkSHE0hQRcatn274pGMlX0uSt4E4st7xLsO9Rs-GsLbHaIOz9XhwKc-W1boEeNj45fUzci4A1LAZD1AX4Xos4yfMuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpJnbABluyjc3JrEmd93LBA3x2ynjE1jQun3UvJ-qKKrJXlOQYyfQWWY691-mmaw-UQ7CopdUdNBUwWwd69KpWdoWOmplvUahgpTMPn0z8apWpMScmzvKVUgIYsZARje-_922DMiQP06Ip_4yJ8QSh9f00KUdNRlqpdkidkGu01KhRrF2ekf0OWGGX0dXQqpVJFF7zU0GkpSqidL1hgFOHiOW3nr5SyAaoCVOf6XCoPcYk5q6JjH-__GDSJ3ECXbHK76DBMVDgIGeKOZ0YggOZZfKRQXWkaDozxoFzPhO4PdF7bnUyihEpFXnpTnxetlcT-ltNJUiaVZwLDJoYEQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsL7UPnGelQeukQMJUSIN5_1LuMNBqkOimgBw_5U84smvYFbyUvN8BWop7yZD6L7CB8Os-q9-8L6BkGQXEDPY4pkhNJz319rilQ-TsS2AVCNIzWa8dUf_NpceX4jZk7nfGar-FZIIdkjTzjrAwr1FR93SfjfazmDwDnONsd_hkK5TvaCjW8Y0r8wbxRvdSVtF8cdnc4LDCDNYvTHQRXvh4fcTrtnug-rh_CINpcwYfGPo1VxsoMZ7OMWM3VhW-gAAdG7PVR3FxTQSedm4PPwMDxN6FG_0Zcf51aOx7tZtwXV-rHmKMAIM9AJ7yut2f9Fip9WsoE9TsSQv2Pel4VlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=YQhDgRbS8wsXA_snXZfi9XN_Jw64DztU4MoVpXQ6D_h1deyqMHqWMUrU0hXApp8mFMElK8Seh6sRBG_MBra2denNHtaIc7Y7A-J-E5kxOS_ETiAavB0_YjGRAl82abLlOnIk8WSH6gKH5clFT09gSXok6T2Edzf2_0HSjpJsFo00Z6ceoICgEXjKWm_Hace6A5PR5r0rgvR5kN3QNhnOLF9WbsHMDb0y8iQ59c9FZ96fIGXoWnKCZwFCAVOxhreCqeNrpSUDf_lB32hFIcE4w6R13gUfkS02cKw-7-KuRnocnL1gqjxavY4cTbLiifimKhCW_IS42vNcA73HcKZVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=YQhDgRbS8wsXA_snXZfi9XN_Jw64DztU4MoVpXQ6D_h1deyqMHqWMUrU0hXApp8mFMElK8Seh6sRBG_MBra2denNHtaIc7Y7A-J-E5kxOS_ETiAavB0_YjGRAl82abLlOnIk8WSH6gKH5clFT09gSXok6T2Edzf2_0HSjpJsFo00Z6ceoICgEXjKWm_Hace6A5PR5r0rgvR5kN3QNhnOLF9WbsHMDb0y8iQ59c9FZ96fIGXoWnKCZwFCAVOxhreCqeNrpSUDf_lB32hFIcE4w6R13gUfkS02cKw-7-KuRnocnL1gqjxavY4cTbLiifimKhCW_IS42vNcA73HcKZVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDuZLbwD9SjSkBTrCV550uAOfKQP7PJzbv7lyFxZ3T0WdZOMkzzrcwkUZPr3D6YAxFzcFjIAxLRWQfF3q6Dg6ybu0-rLLZ4oBkqW3EOWqinedo5PJxH2j6UG59ziXSoGdciDdFgdsRDPpJxX1OCWjmfmnStXaY8HddBXaft54H3fl3JOrL3HsKaI_Jbc7N0XZXO-xgyNCH3qMpShgYotglo2j3g5SjlJHZQRSr8BSxIAcA6s1fNG5svJPY9gSpYDBWORsvU3kq0bckJefrYxsAakUf0YqDbwWRR1N7fb2yKmCgsZK4mK-_siYDZ9V7LrKvoU5ChS2dRh5J1kjDel7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5Dpb4RfYLPsqpE-6QaT0DOH2zN_I7QX22mu5uQ6sih-nj_ZwXCI1_LklRs_0F18DtAuafogNMUXqj1LrMXbVDjJHcFad2CpEZfwdtFSSo8aPTQiZS3hBjDQtJCOCaExOc2G0dWeEwZW2td5V91E_FY3NpGpF-l5oYFPNKDtdLRqQWX0F-wCaQN5VdAKtjrc9vDjFl6uh6RM_VZTJMj_B24PEzchj4KvQTKXypEv0PSYvXrMUg2JWEL4PRXySzGCpXL2QKTkO5-Fi1SEpSDIfrrGoZUATCO5BpNJ6e4PJ0M034T2Db5nDaxoMnmFw8hhbb1G5BUuGmuYG6vf7_WpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6J-dUTzefzwN09sIugF6tkF0vjDOsU5tsZG-j1jo3G3JcUib0Y8c9pdjLdTfkAz0wqWpUYF-eXMOaQnU0zDn42R2X-GSj4L7uBtZw99Czp8RJ47l37K7_uowVoRdk29qFGH1pejgOgZKhsdju3mSOItqjdn3sQeeljzOyOaOejyy-94CQkaULzAC0v8988IE-GA0pxYZFdMuKdgZF6fnsSzY7yQ5Uj_oOrgj0aTprdrujwHGrQn6JquudUT1vlZX2skkn11Pe2P32JBVSLdPwLLm65H5l1-vB4Z3M2UbMOysTIqBAnQlAUygf5rPdPOfmIT5FsUUCEjTKRvSzxpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk1shM2O5ZTOqiSiGfgMxaiP5RhVbrQqKmraR7sy-IqwVI3Ft611wCzABlzdmB6bhT-6Xpe0zJZ1l6hRMfIbo8u4gll9a_DZBuUmZbTKUFD0O8uasfHNBPGtqvmR9eAO3CIhlTeD59WUhpBj87mbJqhKGPpGSxpuuiqS-NwpfmAEAZqyz0-hZg-2op7jfrnyYYsyuQu_JbBV1AG76a5yN_Pbm7arqFdW-_51ZX2Aha1yufigQWQy_y5rgvlJno8pqzv0EsAlIPmhqBEKVV-jEZ5ZznETbPuKzQ2rNDiTc_A7QYuV2eNaQCaNSN7SIBkbJSGRrtlxb9e4viA9yX-CrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=t6ld4SVJNG5NAi8ZwWVJmZrQRY8k2kJnTdv37fVURktKaIiqychdY516xb4BFDiGFKirO8MZoFk_zJf5EPNsTrEe5xfo01gd5V-UVp3GMDhDemB1j8pcDq6RSFf9b8v3nb_39bdpc6dkSsoh3rLv5xz1qZVYmMm3ffnlncpileMw_xOFffTqOwdEIYsZ66MNEQmRcZUNlc0iet6B0AiZt-cpP1qLq_YopkXy7cEB862toZpR2HHhJyB60smHhW4ucjKsK4AXs5K0cEp1EDCEfsaG9ph9adA185nJq6qJBuGq9siD7YvyeJyFSHJR2qtE1ufjEd55_QfeztxIglflRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=t6ld4SVJNG5NAi8ZwWVJmZrQRY8k2kJnTdv37fVURktKaIiqychdY516xb4BFDiGFKirO8MZoFk_zJf5EPNsTrEe5xfo01gd5V-UVp3GMDhDemB1j8pcDq6RSFf9b8v3nb_39bdpc6dkSsoh3rLv5xz1qZVYmMm3ffnlncpileMw_xOFffTqOwdEIYsZ66MNEQmRcZUNlc0iet6B0AiZt-cpP1qLq_YopkXy7cEB862toZpR2HHhJyB60smHhW4ucjKsK4AXs5K0cEp1EDCEfsaG9ph9adA185nJq6qJBuGq9siD7YvyeJyFSHJR2qtE1ufjEd55_QfeztxIglflRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA0AEtsTT5pYgun3hRsyycmeY2BcviLiyz7qxpYWoPaxDnQh1NyU0VWBSwZU0KYkrY5m5-HCip1dw2QBcScWbG8Z6tevsDvnmYAXVNKhO_aeQA44Q057OKjPpVGf5pLYFw_xCI1FdtvgM9tG8kDegC-nJcZTpo-i750FmdmETo7VMv3NMQcAXoORz0GHUiVhz0LmZDPP_GhLoLx3roanTQ0cBy2c5d0KldWkc2gFEKu_Q6NlsIGScOzaUlJ8Uk_80zoqIsp-K4YfBS-6F67qx-fjdfjwPj-wp7rYcNBFKJriWj8EbyuhJyGHGopPUk3vvTx3tyrC-v13ZN46MfTvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=N-wWkWDnb8D5ydnSeZhYvRhxwLpjxh2JdvIOaSKtS3d4QzvfAbCZ60q6ATSmX1iPhw6WCPFBmAWIaS6jv3RtEfqhBAGUT-lW7KkAxwBgVZUH3wNwMo3iQgi76Sds0SXIcaawg1lQ1gSuUjLm1xbnY8VPZJBqK5gq-PcZ-riiTJS27KpmLHl27SsOFvVaAyaopf_Uk0xj5Fu_5LJjjtrEdoTB1eEvQXuPST01KL8Hi0P4WQUKoZWeja2N3zcdD68WnpWd6qvm8zqmN0h5ZwG_mpS6eRBQ8PzuVJ9CIzsLR6k77idW2FYu-rVGwdeVR2ndpivyIeq11OQFJt6eKI7iYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=N-wWkWDnb8D5ydnSeZhYvRhxwLpjxh2JdvIOaSKtS3d4QzvfAbCZ60q6ATSmX1iPhw6WCPFBmAWIaS6jv3RtEfqhBAGUT-lW7KkAxwBgVZUH3wNwMo3iQgi76Sds0SXIcaawg1lQ1gSuUjLm1xbnY8VPZJBqK5gq-PcZ-riiTJS27KpmLHl27SsOFvVaAyaopf_Uk0xj5Fu_5LJjjtrEdoTB1eEvQXuPST01KL8Hi0P4WQUKoZWeja2N3zcdD68WnpWd6qvm8zqmN0h5ZwG_mpS6eRBQ8PzuVJ9CIzsLR6k77idW2FYu-rVGwdeVR2ndpivyIeq11OQFJt6eKI7iYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJfSZjX9l0dtdFa5vCDhhty98h1ktsQNW0a5xF3o3JX5KAiZqXZ0X6ZfEqX2VSl4jQfkmyR7Aqt_pr_ykv7wzEaVCs1xVf7VsoDE6epMLAJeqH1_0YUVks12PRGMSdncLvnRVXAvX3ymP8MYabGkWRr2pCkrfUQ1ypNfT1Oc9O4ykiHMdfdyG2hfEwaaqUvUgXENH3PX_66zv8ya4qReU0hJsCfu-aINkzpUeczOLDlMLBUrjq3Ez2CR106G6ijCyhlxJ-ughq6GWSYuz8DSfhFEKw8Mosap2-8pxJRk6WK5lE_DJAE1n650hmVXOyjXtrWl8ZmAp64hSG73hvS49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oi95oeYemJLcD8r1Lpq0TexAJ8T_IhTDktnY98JuDonWDOYZZt18krxElCL-ZFhkYicz8qV4T1aRcwSIeJ8I0pgDdrpT3wzTOMWFztRi2WVI47vOX6oyx63438rAyFRVyQEicVXsKEdn_O8UKseziLT_8JCegTqcgqEY80Y_ODZSDOMo1epgZGSqGqrjQnlPqpyYc9P0Xs7wptr-OsYIkTvFy88cKn91O4qP8FVWZz9hhuYXhsiSUaLwlrJWCnbcYBDp2xbRqlR8lCRkfYVKUju8zRTIUcEdrUkZInBNrx-CYEDgeJgT_igym4c13HngDvogN0J5g7E2VtiU5Y-T2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOG3mI9NFuysq1lz8wwe8AR0yS4JpBO8Wb7DBlx4krKi0C1SaFDUPDROiQ1JEuUjKmH08vUUgCaLnQPIuJkEQPqDMIu9GXFclIyvUl8m7OUevMDELhRoaYRjjFixXs412BJqc76IeicDf66sreNsXZXjVv1GWSG46C8oBnUs7b3GFMsMRN3_zP9iUaBdAb7rZ1VRaGtytyvHKzT8WhU_rLpUQ86XBe_MZDek2FOcGm73uFZmuYuaxUhKtQQRTCZpmkTfmqTZ4rcK9hcrtkXAMaaROqacLx0NqrljpYfMiT2o8VCONi73k1W-bOIvdbs-3pE01vwyge5afPNIHAp_3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv7pKU3p2ebvGJ-XXexAT-3Se9GNwAu4jAvb25KxkKeZ4j_O-E1xj_yVi29du7N7f4jewqEjeVk76wk4XICQndIoGfJLLxmchTzqMt_nzSzVT6RsacozS-zBcGtw2eG9znC9mNmNq86QsZ2SzcfUCGmSp5msLD0KMic1a1Uq9Vyh3wDul86PVYLuKeaQyDI_lFfCHdSYxgTHr3ULQCsYD6jCClV1anSLGeNBRYttWKxD1cax_RKI5EN_ErOOgXFakvjEtjzwdSV6r1zt69hFAgVbzcZXzEcbDJur4dZ83kjvZ45u5MA4bUNdcLcUKCF8-xMTXmTv2_vlTTomWJl09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=UZf0JVuGXnNBrFc4AGmvYV9qYpLUzK4KvbSUzKeAsCzrAvHYJy7oQy9rZvcbVLvG9KSnHtVJ7_AYgFMlxitLyOJ8Oitv4FCxT-NLvC5Fw0uDVP5eeALTHP9KY4bfvzj5C23WWaFhKCfIY9luHNDRsZrkN9tjA0x-EGTEzGBp-2zbLRNw6uc477mUfNSY0LcGzY5fqciK01xVlolJ8iTrN7NWdcHxFRcXWbpQ7g_iLdvwrK_3Cg8g6ws2uUhyFeDn0pk5eheccvKyY0QhQpB9HkLIKZxxKdDac7h6gscsVGsAp_UDapG7q3tbayMB1BOOhtuRroDBqpKexl-wT_eTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=UZf0JVuGXnNBrFc4AGmvYV9qYpLUzK4KvbSUzKeAsCzrAvHYJy7oQy9rZvcbVLvG9KSnHtVJ7_AYgFMlxitLyOJ8Oitv4FCxT-NLvC5Fw0uDVP5eeALTHP9KY4bfvzj5C23WWaFhKCfIY9luHNDRsZrkN9tjA0x-EGTEzGBp-2zbLRNw6uc477mUfNSY0LcGzY5fqciK01xVlolJ8iTrN7NWdcHxFRcXWbpQ7g_iLdvwrK_3Cg8g6ws2uUhyFeDn0pk5eheccvKyY0QhQpB9HkLIKZxxKdDac7h6gscsVGsAp_UDapG7q3tbayMB1BOOhtuRroDBqpKexl-wT_eTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsKf5fgX286fINTpSKVJnhoT-wz3E7-IVqtOXZIPfcYsaVVrUlZw6pmjR_cAAPxSsJX06q7yBnpPeadyo3PwsuHUZubzHtB4AIzKrDnmRTBJxhaUnSt0veyqgtqba6OxDi6VYqGEo2E_DxGFJNWheCtbaRovfajI6odPz49q_P0v-RjnzRF8lP35gM1oNm0VZykHM1MzJcEdVt0ZEyA7dbD_0DemIJQ4qjpAwOIYlj1UyGNrldsZnPKCJ8x_f3UppFbnOu8EfP2y4WQunxMmcfwmeGSqNWwyS9IngMdXWUkhV1WMwj_vNIAK_-JtB-QhRqFw6rfcHvqp45CcQQXtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzlTf_8KDtC2Q6bVHE32VQEXU4OILdkJfKBqvk2vTXvIgy7dhqPM2BhKMQM9_MD4CdKI5Os9NUtOpxZ--gvp28s3oeFstsNZ1NNXXH044cB-E1cftLk0_gh23ISHSvE5GGRFC0iKgoeftvQZDyo4CdvP7TT-mslC86lsGZDCUyo3LJqF_7HxYt65T69jEdFgv8WzOUWYVPNrFeLw_0PAQi9Q1LufSpSw5_zTWgTYdUSOmRBqdwVnCE7fl8HhsH0A5alv6D52BMdTgs7__3SnbQgtHoLeTCFMmUEHJR_bCbMe5JIoATAfRdPHalwiHbQ48EhD-8Fd6HSdj0jEQ6Z21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmCPJ5rU8I0v2lIhZJpFd1sIGPa8XvntnfaH4-1dD-nWF6CZz6SiOQQe0M2MGxhxCERwVxQvU3bG6WXipVswNQjdUDAukoZ8jYZPfdHrOUAz8qF8aitL5LsreT3k38MSp7szde4a5aiLoneOGSjN4IkqjrUlAnzYK0iEdFEf6WczWDnsj92tL8Cx4D__MzTWvnG4L6OaAwP0M_Mc0e2l2z_Q5xrrXOUYvLU7bx2CXpMoY21K6kfScVpZ9cZjmj93aQkyYEX_MO0DlbkzUIOSFnLnTKZ4-AmhESC2bXYeJDmoBqK9cV7QYiEaE6oTlf1Hhad1Hor2ycNhJ2p-MU0Log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=WOtwHFZ1oPIMnZ4JY3VsYGvg5pboyQGnK7XaLbncYSSQ6JYQEVL-lIQQqx2IeVWUf6L151W3Qf6UZ4z-7jmRGnQDRGPD_2RDkOLMVGVHR8v49dQ964IbX06ANQtMWqYz_67gmU5k_FAfGv-yUemf46Pus-SHtGtKlUJ-nSk4_wgqNSID_SXnMVMRZ3lxOPHxYqdJyxBKUR8sYx1prN9YUeefdUtknDTbtHvJjWB8lb7Jtap9Dw3CHHH4E21zgoNXnKJF4Sd2X2BBB35h82AzBXJ5eYEfrjxYf065xMZ7Sj13w020KQNUFu1RV5ZpA5MffrHEeXL6_vsL3l6RKKXbOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=WOtwHFZ1oPIMnZ4JY3VsYGvg5pboyQGnK7XaLbncYSSQ6JYQEVL-lIQQqx2IeVWUf6L151W3Qf6UZ4z-7jmRGnQDRGPD_2RDkOLMVGVHR8v49dQ964IbX06ANQtMWqYz_67gmU5k_FAfGv-yUemf46Pus-SHtGtKlUJ-nSk4_wgqNSID_SXnMVMRZ3lxOPHxYqdJyxBKUR8sYx1prN9YUeefdUtknDTbtHvJjWB8lb7Jtap9Dw3CHHH4E21zgoNXnKJF4Sd2X2BBB35h82AzBXJ5eYEfrjxYf065xMZ7Sj13w020KQNUFu1RV5ZpA5MffrHEeXL6_vsL3l6RKKXbOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpcz7Swt-ISdaP-jNzhE0Cher7hyww25Z3P4_uJ8W356bna-7bu9vqWkq1zCqfbaYuNKN87Nm52zh3mbnkKhPtP1YB3aGwl4X7bvgSPRwevXlMZ2ak2VFw0sSaecUFzVvDu2zJ2qmXSmu1R6HoA90x-geKzo4-vB9942zS5_A8ZueJGRQUzqp7EyAubR0o_zDuqdJNDYEfoYzau1NO3ooclR-1NHyITq3M4IoFrw3uUjx_V6Xre7E2HYgoIlXWxKDAgofr-N_i-ik2utGxqBSyGtfxOuyGcvqb3_kcCEkldeLwWLw9HNPgo0YkLVkzzUPYdSllipSdO9lK0T8NTkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZWbZMeSDQWX0BVZGwu8TE0HUqZvH52t1mPy8MkVFeJzqnZjUvivcp7J_HIJc8wcL79UUOmz3VkyQmjKV4bF7IAREFgwT7ownTHQR87PO-Yep48kbrY7zydcquXPXQMvVGm9oQT17o4Mg23jtkEothkPktAvE1cbXOCUYoN9asSnTEWZRSKV-lPZZWQswtNZrO3B94Gt792SvxU4yzkl1DklPZXMOQRjCZbTz0y1pQ-57fYFTLXPgySqYcMJXtaYtSShndUn7pmO7XqF_fl3RJVOtZFR0w8bhu3AOlkl6yYA2qjbrUB6oe0TyEJ5w-MytmSkVsYFQJLld4KY5hI6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1v1nK5hQrI1mM-AHXBjN3nTo_zivTIZ-o2k7cJ7O6Pdt-eeJHe0pQLulW6U_sgRo_kqX8AV8m3nHRMQz3_irNX6W0bBVw89cB4oNsy2rKiw89cauwL5HgW2yJ8-FygzwDmkpQpQdF9r-Df1Hamp1AksHXX_T3fRI9Oh7bJD4ufFlNBLfjFHFWo1zfRlo9VDyeSpX9w0y1Qq1CtcWbZraSe8aQRnL_kMik-jKPjTpj_GsMeDC0AHcHznZiMKHgCfWvcp5wcfqXz282Z-jJ-yc9GqaZ8V5K1y9iuc5V4gmgJogXHJhjW4O3VWMRBpUy5B9r6gaQNbL-SL336jg75bgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=fED1QzL7R7E4kKHpEWF0b-oq1wbdgtplcaEpXWhk_02LcKSQgrmzlsI8YqJUNJ6ipaoPpoaJWWzsugPxwNkjMJ2wYFcwXVUlP7cYlVug_p5iZL82jH11obWqnlFdYjeWTO2fCsMOE9aM4HfGdHjSV6VbxICDjd-KRcS8mWqYX_3TdV4s3S3I4V5X92drLcTlDtw0W6a3B66VXnM1wstrDmqbJ5ZBCroLRNhiwMN1pzrqd7-ql5a6ejkMqtKb6l3COw6H9FD2tdbSE1cqKm_FtUs-RcZLPfIaWv46USdAyTSBpDnr4WU3k3YasA6LctrvzVbIZu5PsLOCpf_dHr4Ikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=fED1QzL7R7E4kKHpEWF0b-oq1wbdgtplcaEpXWhk_02LcKSQgrmzlsI8YqJUNJ6ipaoPpoaJWWzsugPxwNkjMJ2wYFcwXVUlP7cYlVug_p5iZL82jH11obWqnlFdYjeWTO2fCsMOE9aM4HfGdHjSV6VbxICDjd-KRcS8mWqYX_3TdV4s3S3I4V5X92drLcTlDtw0W6a3B66VXnM1wstrDmqbJ5ZBCroLRNhiwMN1pzrqd7-ql5a6ejkMqtKb6l3COw6H9FD2tdbSE1cqKm_FtUs-RcZLPfIaWv46USdAyTSBpDnr4WU3k3YasA6LctrvzVbIZu5PsLOCpf_dHr4Ikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezt5-F9w_UVKkPhThEqv4xmYNSgmHC73qlHlNAJnZQOBiTcUWp61aJIHpIr-Fh8kprrQ4UOH5sTngaA5ejH2eMDAVkjyh4rVFQ0dO2LkPOgiAbaIhYB5IGawFsmyj5TDx9cbUR4FIkKJC7AzxOBJshZJKlpG9zcwXLOhu5xcMXUmWdJKq-XqRVlzlJqjmOP_DXsc9wzWXmol3XDSHamNhH_MUgd53xiSvUfFd7Z_O5vBfppkJyAZWZjhH-TOVIGwQjg2N5xkD8nyDIQjHNqe7qkSnJiEr0qZT-CsHPrVCWKHFdrCpck0INgpiykBxber-Lb-1dTrlaYxwp7CNpiuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiCKxuBy-aNdv7TYLXRHWHJjW38XD7VovBbo9AnwcT-4lmv-5SWrHbtb5FEBZ03cHdYqbW6DbvOEMcVEMn086i0o7RqkSHjQc8nRZY_CTBRBq7uHFRlQX5Xo4UTsAPHSon244lPjiQFCGA6sXSBQ9iY6cEPeYSK1a1xOah525L8_8wvTyoYipz2_9acKbLNDve9S1vz_kr80g8DmN11dY7EaFxjUwVP6L4k9tGv28WZ4tGbMg8o5hNRIaETTdQ7efwbvX8OMZ5A7IncDo-hp_GNtu3ESXqG7RNcf3ki2kP5ITSuEAHXtFMSgV_j7OmgZo_EnqXUUMF7fgAZ_rZgTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4HasG84Grthvqf6H8Wfx3hcbq-0efRwr9KXsEeHkWv0GfVdRfhH_ZdFFZdaFdhNNihlN5sSVFvnG2cd5Oli5DQPztakDyvwgoefLu_fhhaHJrGrhfJe6uC-he6M5mwDIvIPWIgZIgeC_g13WuCAV5DZcFLyA6dk1xPHbEJA9_pd-6vUdzyYfZ44ZveDFITy2dH3lKfwL-T-vJYxDWBieoE7SzQFu8QoDmtFybXp3U927-t4Mj5ngD6qYQ_GNyP46X4ol43ptLsALnmkn1r7Fuxfb2wOKi9RV1k4GppNCA7xKBpH483U34fKcdtAqqQG3Xeoap4E7GU2KVauuqBq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9iTmO1Ge6D5moVnOtyXSQ7krf67n5PTgNj0jWlNr0rMhBMYTKjYrx49i3M5dvNRPWoiVZmEbz8_9vUA1jZu-mXfeM2ZqdWdACB5boIz-FeOHd5rhHsV7rvZURzMpf97T2XGOOSiUD-2Rr16IEbB-vRqLVA328u_qjcNnhZlrpPwoagUjqwrLQ05iG5kF44tpNfqul_xaenJOZc1X_mLTM1a3bAwIpq198rQGPbTrv7husj3ePfbuEKLem3-p-J0eW5RT-L4YmKh_W01CjWbbt40smfgLGc9d6lFAeqzKW8xyGI7ij_JC-lM_fBWRhAOxSYQWoGz2fRMr_YenodPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7XD8vWX1Jm0v4ZVESn64BPkd2UXmC4Xhkhhi9rLi_LMY0gpwerFHfcwoIRUuhTNc6gV9651bjuKlYXwXZPu7sxkzXEEfk8boutiSyajYoieMI0gTLUeNZSI1niUFJ3vMio1mtjadi9TwPx_At-XS-f1j9DxjbC-Z-1oLb0tVihwwsMui1IIlwq4EcaYiiydAgDWLlmB4U5M1w1DJBoxrowe3kC3J34KwkwVAQc_K-5LK7aLd6oYi01H0R-KG5BHUIRRSxxIol7LO79pAC2Vv2fCgddW9-94qZ9vGxzfesY-t_xKJeXL_A3ZpP9XBTmlxZ2l5Mo-2eFH9vhhpiceYxbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7XD8vWX1Jm0v4ZVESn64BPkd2UXmC4Xhkhhi9rLi_LMY0gpwerFHfcwoIRUuhTNc6gV9651bjuKlYXwXZPu7sxkzXEEfk8boutiSyajYoieMI0gTLUeNZSI1niUFJ3vMio1mtjadi9TwPx_At-XS-f1j9DxjbC-Z-1oLb0tVihwwsMui1IIlwq4EcaYiiydAgDWLlmB4U5M1w1DJBoxrowe3kC3J34KwkwVAQc_K-5LK7aLd6oYi01H0R-KG5BHUIRRSxxIol7LO79pAC2Vv2fCgddW9-94qZ9vGxzfesY-t_xKJeXL_A3ZpP9XBTmlxZ2l5Mo-2eFH9vhhpiceYxbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK7iBSzfcv8SZgSgJrfBO6LNpp1SNqDiXDUGkSoLuFi2V5DBPWuQ0fZsLhaQoGn_pw2n32hLkF4dQLUiwtP-SG7kg5DxMZ01bCPOg6Ztf_BnUiwFNCBxW_0Aqj9LKWXqCS8LmjmY2pbafBPoCKn8TtfwoH0_9ZgJ-k6tzOS_RNleaDT7qqmY4bul5Ox56YluIVa7ixFjvCGtdDY6irWkbCbdIdsYMdUdhRfDRf1-2y9HfTKy5cvXdOrX8ZPgOTO6LGG3GIZXW9DBOamwFA9rfjEFxqKHc3HgxRQOcaidOUoqeGzXbGQiPlftsdCPuX14BK6CC5J9QaMqlPRuBu07-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP5eD-1xrBmtmBT9c7KU52JKAxzJ5JpNEr91NRfqTMybQmTOrCcVb8UEddNG6V6L2WOZANyWXEYypltR0Nr8lHW6YC54rLSsH83JDlzcIXYgK5E_NqQ7b1G96Qn8gihQCh56EMtu7eZmM1_BEoHqdh2t4ZI16eR4GMycjICFimrgCxOCx5TlrQAQA-GN6UEIStVbs96EeolQHsqYo_968owJhaNoXuoNbuwtFIpieHceoOoUYGe58DkfYRnryabEOGr-04F8-B4Ovnj-1c0nobfXJyywsVgI7JR6YKpjVHSCT_QHd1l42RvRwmwlwgfUHQrYDa1USPVISRbAwPvz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkaSgghHg96zBY0abrPV3o57eCqxNT-tU422Q41-6RQGDLXWChywhgQWD3WEeUyex0sOJ7YWO2cW47nwYdV3DDnnzWlV9VLXR9xrZs_YfM-X4RRnAoIdt_d9GWEqWpotI5dkMU7ReiGYXm2t2WbNOdrVMJjv09Bkiw050ndySd5nX9O1toSEKhZjieeTQPPLCcD9Ov-U3O8fS-KsS2C7KQ_v3wgcpZ0CyZshhH2yNvNfE8QL-IV5x9TjqJ3HzHAfUuWSvbjE2Unaa0J8dogkRIoyYPjjPrYRPaWGVCvGVn5OZWAXeFPdN71HwM63bF0o3hG01xyO5blrJnNYU9AVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=lmNMK7ZMP-fIItdfue8QPRxLeMx4ve2xceJL0yZEmKvQvI0qi02cR7ceDut72F97GC8EvVch2tj0iCBeNZ3ZkwP_LqY-k6FDCjjjVqrt4hRDIq2qoBQbwSHrh74c4_wJhQRmUbO8oVyGkmJpTtglAJFOQ-Zy5ypa_dtXUwZ3CD1OkflBx4TIaxVxG445cEtZ13pBlsVlr_hVXqPJKTdkLQyX3A2gq8vs-NmKKhxtNy9jHq638I-vGDofNUlsQ8CuswUURtz3tChyvxMweV55USu8yptrtenG-uVoNrxkSKUrjeo5mYb2CaYn5Sskf1dcnRmRO79_CNmj7p8RzY3fRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=lmNMK7ZMP-fIItdfue8QPRxLeMx4ve2xceJL0yZEmKvQvI0qi02cR7ceDut72F97GC8EvVch2tj0iCBeNZ3ZkwP_LqY-k6FDCjjjVqrt4hRDIq2qoBQbwSHrh74c4_wJhQRmUbO8oVyGkmJpTtglAJFOQ-Zy5ypa_dtXUwZ3CD1OkflBx4TIaxVxG445cEtZ13pBlsVlr_hVXqPJKTdkLQyX3A2gq8vs-NmKKhxtNy9jHq638I-vGDofNUlsQ8CuswUURtz3tChyvxMweV55USu8yptrtenG-uVoNrxkSKUrjeo5mYb2CaYn5Sskf1dcnRmRO79_CNmj7p8RzY3fRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCX8u4PMyCmwxWxjoR4ip6VJ8jpjAzYG6vXUAWYHwvW-C4aKx8RrejqsZzTv0fRTXckyl9IhZFmlhgB7PSCE8Hn2-ePRWicd1hk4_wF-a_bHGmKgJw7FWZ4zsA3mzXzDNytJAHMb9wVnNd1qHPNQWwLEk0TbcVinUhbnx_vp6LKnu07XIoAgQsYQSstzJx3b1J2T_BYHoSLb1xRdDaKAiLyykC8JyC3BIvXEqmXmyEta3r1B7nyr96893wJSZl43mZ0pdZiW4HRUDm7UMnWMNiKI1kLZRNz_siEprqcYr91Mf-ovT2n68LWVU5MS-5jLM0UZxpaAQMffXezmuxSqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMEOUo-ubEih_oIc_We6qs6A4wp-ERHx27o4cjqZPvJRD3NxkzeSPUqpQ7aQGEwHT_JVwfSyrEzixkQkzboK8s292c2xVswCCA6mua32dUpEtS5y532zc0RtECHYMG0GZ5aE__mXMHh0O3zxBh8qxYXEoiZXGmybFJJOnmpPe6VXyeIup--SvyjJjEL4CdM3e4MhT0LQGLmT2YagSkYxBU-Xg0IPKIUPJUpXyLdmOo47twjz2fQtfeK3CLhD3kOB4k4PmtWPIf0rBLGTV0BNdzP0TzdfjIvYFoKYoOuanubSKTelfHjZwna9irNrY8p0lgl8zE7Pr2yguzDvVW5Kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5oE_-l7DuqHJWXB65HivACnCDAKU_KN-Y8LeVsX6c87W0SMx5luSAwdSFA8m-XOqfEX4qVFIIWSOdf6mfazqdmAfbvYO8PZ4qwBkya7RQ3tU3q5XPP37Hma9yelKQHVA4LyTt15ILA0pdqKTmR22YLJp46k4X6eOAyuS8TqHHBw1XRGuJGZv7nfO1UbPD23ePbU3_ZjESoVqae0MH7bsNXizdmjA0n_5ZWLgsw_kkpkGpzX5phxh3KC31neflkqRlWTEJsW9sBqTTvUHgHFrWXlbF1mFgKsT5ldpFa8Dk1KqRK6YsWv9SRh6KosFf51oQV_t8hlXR6mFIKTgpxtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7VHKPmy4f7sDDA7nU0M_yTgtRGvD68gRtC1bnHixdxhi73EkGZvWumvqVusd7a2jZrJEpEL4Y4Cte6jXob60UpwUh_IbeH8BnUo-nhO7jhiDJdEkgZEVT2dbpCu4vcuxsXNP5HPdCpLhuMnPwfDIhvtZZiU3t-BFPRynijbUio9QR9T79OoK4c8kywtFtcWbkJ6G0g472wXLhHfyhe4puZ4u0Zz34o4wQbZWhOrhPZzKyaeS8hksZ1-06rQ3qJYiLGaQASP5GKjRZG45lQgwhXl2uJD6Bc11THUqAkTb7IkGG7P1uJv_L8Z_DfcjmXBD1LTIwLP-DN2Yocb0CCM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQLjjwE3AJ0c5OiFN1PSGWAEBgt0x9UMkMIoOmmG6R7CcaJIwxiO_h9E-H0GZ5rhhiHtm_3yEc9S7DpQewuHf9d_4cG7dry9mPMbS2Kn_X0yf704QBktaqtV_aaGDzWkRPWvUjOQuWl84wSLrupzr_OCQiPIDHLtVXVfv8qZXai1OJYp8yMUUEI4ioUg0ZlkhOdEnZ52hmxHK169zjSFKnO7gU6u9gjp7LavgWbQhR5dxP82a1IkDaTJPCPcGD9e_tVhXtnvijP4c2VglTWk9GvPndIUOh-7OPh3pEWveA_yd8u14JrFfSi4Es2QuvtYJKLQ_P6xHfjy6tqovK9_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_HifFSMCdyITakVAzA5T2tm74htTFE8g0pRwrqfMJFgIGAxJlk1LBBXSCK678DWnvsUeMIMmBoJvAg46NYQUObD4_ElmhzOPmvZDjUGXsZZj33LXxhlQw9ce-bd_4GYHBn4_ZeX89fV2A5DOWExvCcQGW50kS2lKLH7WAafSglBc_uExnfXFXXGp1f3RcxjyrbLHaBUbTz72cmcMlTPfgZQiMxxIsdvSUCIwP6tYr86lMeYxx9wnoEBIiIhuU5YD5kYCKseBwQXJNWpFQqQLB14LtbSovcz6Nd-lHSPNCzNm9aSvOOTrkl2RvYVxk4b2uwiLbPJbqX2aZCWsP3ENg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYvIfGfIrfHdvtE93BytB9SPS-VusoPbElliFTvcZrOGOGXL-3VZ1GW_5bdk7zGGNclweRWD_-oAhI-PDnZtAydbQLQpaDY0J2A3bNskyXjaaO4Gb16sSSlY4FU2CMqlCKGlffxpdYoGRU-m_4hyT9iLGBeS60VEpBt0_BQMVwrf1tZ_G4t9yZKXa6NAXVIMVZV1kj5QtQGMvGCJgdnUENzlMVmkEKTGgIFCE6BnRrPuiIWrcZbe-pysSSQRsHOrFR-DhNo9g6DusD0eFFE6XGnhhENrCYi_hJU3fRNc2ew0AZH2cDMMTu1CUkzr5HrUV9IxOkV9W5G66OwQxCKuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNfWaRW-JEk5EoKRZPg2SoKnIoVxBFQGSRZ9lG6WsqOsnZ5W6I6Z2Cx2X2qleJIgm1ky_Qb9bmZ0qKgB4cJkpINe4NqDXW-8dRxctOEK0yFYCGsCK3Vkyx3EPh7dGVlE5uwP2G08vVAjzHoIn4rov-QxT29V5eDCGUTGHAmV7RAovZ1Y-GtrilsXgI_NljQdzM5XNTrB3F3CCYK4q5EEum0_-s-Hqgktla-TEUm8KOOKgPvC7ZSe_38bK1TjXjZHawxINkEkPsNEQIqXDl21ylCxLm6xGGHV50X0hb8zt92zGnjZSc3TfV6oznOFka4ojNBtOUdK6xIMa0T7TgRbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdLacqXfI9TmtVVbuuzOSM2TFkSfCaFREmAcTQdpa4D71-tpjO2gIkVyOMUjVqd3attSvLTvhZbJ1Rd1rXthVygDxujCqcoXmhkz-65pUPccfat4KAUWCZWkHK5BWpul8vVg2lck75Uh5a8hdKxc4qVq5nulnV7dU5bNJba2Wuu7yJDBXZfPdr4udvo6w2ea6nWoIIO2pYhlQOP-PP3tmEUJPBPRIX7n1Ea1tNntWohvJJCjoPON0M7IAI__MWJ_AeWKFeABMV0aKvC4z-uWioVeZhKLk3j3NzTEdXX8x_Hv4pOutp5tdEnJn9yOvqbg8FzZl0BPgWLk1ijYvPt4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=MOQO86bxnrhoZrkLITMluOdw0ZwI1FewUAPiVcuOst5BgyMkBBHiNjpMNO8i4JzSG9no-ViiraHYBsgDth4-MztIRjZ_jWgs1vN2MHVGqiCbhuj9MD4KLxKMJF9fbdWZTLcwgTgWDUTGp65I0oJS0NZSLeCATGCWA2AkSJYe_i8kkeQy0_-1Al8jSOZHIfUJ91niJkLzzqxqeM6mM97eNIknQrB3qmqU6ypv9sy9upFoXO-NqlAkf_tSSJioyi0XQ2G0n4RYKI173MzcCnH_yF7EEWdeOMSATRGI1MUbXQu68Yxzu4pNnr9loba5170RqYUH7qu3zxYmGAZ2Um3SFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=MOQO86bxnrhoZrkLITMluOdw0ZwI1FewUAPiVcuOst5BgyMkBBHiNjpMNO8i4JzSG9no-ViiraHYBsgDth4-MztIRjZ_jWgs1vN2MHVGqiCbhuj9MD4KLxKMJF9fbdWZTLcwgTgWDUTGp65I0oJS0NZSLeCATGCWA2AkSJYe_i8kkeQy0_-1Al8jSOZHIfUJ91niJkLzzqxqeM6mM97eNIknQrB3qmqU6ypv9sy9upFoXO-NqlAkf_tSSJioyi0XQ2G0n4RYKI173MzcCnH_yF7EEWdeOMSATRGI1MUbXQu68Yxzu4pNnr9loba5170RqYUH7qu3zxYmGAZ2Um3SFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JutTQPqg1hUWEfq0xPYDNZyM_wlgsur8htpVT3ON8dv-J389PSnXuzQqWnNSpWXd2ZCqDdsi_OEgz9B-IiIFKpo93O3G9tuyp9mC2bwLoKhf4MNo3AnSgUqY4Kqu6efzWH86ZrXHce_WKFi4bOi4h3944THrgimgq6BSycHcWF4USH2lyDrFn66UozXw1RwY3gfdyrkwIS06X5F9HU_6JI-qPD5-jgkYyytQESlkrouAqeCex-2MHFn3anAsmzL3qaOZYAD4NnYdJThShymnJY1Ag7d_TDZ2KzXlkmKEdb8TfhliRydGAXR7OFX5x9rW4xNmuUjFOCPVN0F6YLKoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=IGjJNjr30ioeSApBpv_FLs0m84I8AfrorJ0yeQ8XK2JpM4KECt_dgbaxzpnlYojnrlr5HTfOsaFJH5YsIRcSFB1S7-kKum9gZbzLuXcIE3LbfggWjaFGjkqrHOSuKsNjKds3eP32FCMsD9K5ypnqi7pQdq5RF_lhPnu5csJJl901e4qrciXzbBrQXe0JvVJOvyh7oezDOmDc6an0AAblk1M_ZMGy0pH5H4xfD0GbfFzmSeqzgJ_JzkRbiK1ep7qwhRTj9LYPfPuQ8TdLUad4xtCporOb4n8uDHxu01SSztsax246yjJT0GPax2bcC5-asZrt96z89ZeYyLwlzMlsxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=IGjJNjr30ioeSApBpv_FLs0m84I8AfrorJ0yeQ8XK2JpM4KECt_dgbaxzpnlYojnrlr5HTfOsaFJH5YsIRcSFB1S7-kKum9gZbzLuXcIE3LbfggWjaFGjkqrHOSuKsNjKds3eP32FCMsD9K5ypnqi7pQdq5RF_lhPnu5csJJl901e4qrciXzbBrQXe0JvVJOvyh7oezDOmDc6an0AAblk1M_ZMGy0pH5H4xfD0GbfFzmSeqzgJ_JzkRbiK1ep7qwhRTj9LYPfPuQ8TdLUad4xtCporOb4n8uDHxu01SSztsax246yjJT0GPax2bcC5-asZrt96z89ZeYyLwlzMlsxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj5HE0KuygwYCqlCvnzH9BIo6qQ6u0FBMzdFNbZr0NbgAh1rMG22QGJb8H2C5iNC4-V6aLoItDerIIajOpACThJ8wmgJ70L-I_FQUvdum3inSMDvl9ulMbHujqEzu43N2Ni33-AXoyAYCB8AEq31f9Z3zHTMEo9STl2S5ZO-tmSOq2q0vy3JUrXDwMEiVtqeHV-W6lt_ibwsznJimOeO5DEWqyvR0dvKkM11rXmZEN0UFUbWvnVEwwSf-I3CDqIiP066shvk99Qwnanr4zS12KBJ5KcEyBVe6I2nVDHpwpvjfFqrhijMDc_SjrV2-6p9d0cOZ4WnoBXPzfEctpA3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T08kjBrSa6lLpTLrXDaAaJ7X8jM_98gFJDdw8x08RJldM-BtMx4Uv6ZXVUbnECKuv9kSZ8E_-qidvc6gRnSdxU9L1_FP7C3Mtp8mVZTjkZbPqgrp-acTsN7sAZ24u_yZOa1v-wnYaHY4d8ItV73tY44cni8r0LGeM3hHTihAMzEt-ETxXAaSttgQCuMN_2cBF8rGHwsmhXkpN8OdHyPOzroMaJaUtaG-yZG-2OP-DaySXJon8DeX87BLgEsXsB5v5v_BLD4I2iXPwEIsccHN27sUuTB8rU_h2rg7RE_JnvBiWoUt9RxR1eNoI2YYG92BI-UgnUsiThLMwJLEwXxhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=UY4o4odf7mU7FS6wpkyAWD0ddYIn-RmcZe2_Sqliw1nxDO9c1hzDCBtd5cD367xuGGk6Et_CLIAY837ggyonH9AM3XrzlleCrsEEN-K5OBOok4KNjh1O-gaPmt5kuudRp9FEg9QNEE4h4QKzXdKPUqcNG0tcMLwGsNvhlgf0vFigv5NornmHhUvr3a_YK45Tq-VRwmPULbzn76Onso9yVwqxR0kzMOYDkCLXd8bez2J0qW7msxcpNjsYDGRRsfeVVgaWYHNyMct2XE9mfBDd29Ndx-vf2Vu7k0GbUSqdGa0oyUNgnS2nKpMG1fPelyCIwKdcgUodC4Lxoq5nq3tweQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=UY4o4odf7mU7FS6wpkyAWD0ddYIn-RmcZe2_Sqliw1nxDO9c1hzDCBtd5cD367xuGGk6Et_CLIAY837ggyonH9AM3XrzlleCrsEEN-K5OBOok4KNjh1O-gaPmt5kuudRp9FEg9QNEE4h4QKzXdKPUqcNG0tcMLwGsNvhlgf0vFigv5NornmHhUvr3a_YK45Tq-VRwmPULbzn76Onso9yVwqxR0kzMOYDkCLXd8bez2J0qW7msxcpNjsYDGRRsfeVVgaWYHNyMct2XE9mfBDd29Ndx-vf2Vu7k0GbUSqdGa0oyUNgnS2nKpMG1fPelyCIwKdcgUodC4Lxoq5nq3tweQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBbKeoi8oDmr5ZMXQ83t2Y1sVPomu-hl0wo1DmSxXEQoWXTKh5TQtP1m0-uSG7CuGBsRw8fWPcqCsDznFUCyxQQfB88iuBLB6U4gLT44fMCWAtETx5gCHgUNKAE25rPnjAXDZSnXlYfp-K-dXsPw9A9XqAagF7l9ZlkxUZBVTH5Dk10pcBYzLsQ-I5zv_E-3VyD11f6Scuj3yN2_TJfHDrOSF58eU0G3p09J4ax9GpKFdZeZIVmpySKsC8ulslA_9b30s81V_-UXZmZ3G3nps9QgHh8mdCurp_IwWWIhnCzj_fpjBKg6O6LXTehk2ZfuT05ao0G7x6urp5PHyitmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAFHbCom-wfgX_QIKnzhVe1VLriILqZymGU4p0ND61Kb5bVjSaSwePFnownjXeafZohcD_tSxdjCBAtZKGAydALV2HD4T06HEqkbLNeS3_AY2fy5pqEWK3Yd9HiCTJZiX-lxtBWpoDwQBw7CS8CjBax6vL1NSk9H-AXXklIM_RUaTpU3wqoUrA-XAGrFw4ydCRnX0s-j5jMCHPU-dYnb-9R53d-4b0exAOR0zJEGaFrx14Cj5FjN5HSYT4L0V_3tVRFz-qVVMc6SHfztRw14x6LFSjuAVjeRRN_wowPBVi7-_UDFBijQ21COS5XjyU5VMn8Ccg2gMGkgS7O0JNvJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd1sQtzKgwlPBDVKlCIWnsvM3QaDl_K3afXsiznRMaW0lcIdZdq0CJNG4_9W2lnN0OlhRR1EiqJlt4VTA-SWlLW2lN6cO1AwPlZsFKo3U2LMcOGOw_7DtKCBRlXzelpTbmSUOhbwt8lSVf3DTaGRLRpWZOrfOiutPNLsJUzis9kxjP-FzmPrSwoJKIbLpP81N8lmgoQNTc-ie39cRsn3vx2coLtQXQ9Bu7x0khar8TlkrtQmJYO2deIc-Zbj2SjaaGJNwcFb4FKgkAtDv5QRNkW9p4x3WV0VhJ2m4EBuqeYEAMNeFbuDrIgHV-hGqi_x-v6hOX-3mG6kBMV5GiEP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFDjK9dKAkOANZKRiXSvOQaBcu31NbvA08PbinUrPKRxH6WxkwGOgWOpEL0h8YIXnwsJrjpK5vCPVBaawkw-DpkAfDewIiDqSGxpD0wP6lH2B5DX-ymFZwi1dgj_CfYFb19_qw4wmItLvuf83yiBmGImuHjcRYg4u7elyens35AoOsxq-bOU1ePlyRS3dgs870KVjMYMaEPlFO8EEBCHbpVAZcf-z_rXHGD7lTfor2m6y1mHtWkNrBZoKD3JnUsNwgz9zQxPcgAGNTC3WtYQz3ZTJ4UQhcbgTPylNist0gUXYZsljZ2KhUCjYcHn4hnHxZCWmiNzFcIxWe7BDvYQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=WzBA1OECW-jo-cwvbIgiuHEgVYfuyi_6BRzmpv1054yQUBxdMslERSpYsiEx4tJZ1RktogGe6YCVxc0FxMiJB64boL0z9c6cu0ybN0veuxIXQP6wYW_EKh5MGWDMfPfY8hzVF2FC3L1vjEP8pVA3Iwy7E902rTtwVRvCAsTBYBQ9pdGfam9VjjO4f__Ayn5ra9Bm7ONiP7y8yS-6RaAXhZf8PC2ux94ftI89mHamv5oUT5rel2m1Y8SyXuvqrAE9JYmEcXD9j29w-HqvOHTy6uaDl_5tflQhsknwUGZOAas_44vHEMDSWW73Yb00kVGRO-mCzyBcLvnf2QoAYdwb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=WzBA1OECW-jo-cwvbIgiuHEgVYfuyi_6BRzmpv1054yQUBxdMslERSpYsiEx4tJZ1RktogGe6YCVxc0FxMiJB64boL0z9c6cu0ybN0veuxIXQP6wYW_EKh5MGWDMfPfY8hzVF2FC3L1vjEP8pVA3Iwy7E902rTtwVRvCAsTBYBQ9pdGfam9VjjO4f__Ayn5ra9Bm7ONiP7y8yS-6RaAXhZf8PC2ux94ftI89mHamv5oUT5rel2m1Y8SyXuvqrAE9JYmEcXD9j29w-HqvOHTy6uaDl_5tflQhsknwUGZOAas_44vHEMDSWW73Yb00kVGRO-mCzyBcLvnf2QoAYdwb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=pzbadcU5d2sT8wX6mmvwNJl1_QIHnnS4R9jza7xWrD9GBZrsEPS9s6uofeatR7C9RKIVtVRYDvPrTvuyKl-Y-8PjZxbeWL9xq7k8BjZrefeXOzNf0CDBPz6ktkBtsXZKyipiVERDRF1AbgOBQSbcS3bnqxxnrvA8InOLzFoFfFZleG5uIKVDa-CL5udF6NHc7a8GLxkguRv-Sh8bgyk3Wp_UDGoPYY4R4KP8QLETPKgqq5G7cwh3G0vEEsEAScF2xNuVonhrnCuVMDd4JmBHhCz6fGgkjKsP8FxurG8clTJhUuJyXoTiGtu3llT6R0a_GcS-5LjxRGlP84By7M0MPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=pzbadcU5d2sT8wX6mmvwNJl1_QIHnnS4R9jza7xWrD9GBZrsEPS9s6uofeatR7C9RKIVtVRYDvPrTvuyKl-Y-8PjZxbeWL9xq7k8BjZrefeXOzNf0CDBPz6ktkBtsXZKyipiVERDRF1AbgOBQSbcS3bnqxxnrvA8InOLzFoFfFZleG5uIKVDa-CL5udF6NHc7a8GLxkguRv-Sh8bgyk3Wp_UDGoPYY4R4KP8QLETPKgqq5G7cwh3G0vEEsEAScF2xNuVonhrnCuVMDd4JmBHhCz6fGgkjKsP8FxurG8clTJhUuJyXoTiGtu3llT6R0a_GcS-5LjxRGlP84By7M0MPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=fjCfcgv7OGH3vK4a7gIVsobWnwIlM3Apspku2BJ5OgBM3o3eruGTwbgMUYAqdKC50ZlGaR2928tePdc7Rl04cKdM9XHThvpKzu_0jE6NjkOAhF8Gd39YAP2k1Rl7KAZq_6OMppg3UPjT__vEv1TwFWAqAuDhj9owkXMU1cIuY9xEEdjwNGnfhRpLE7jN0A2c_uzc7NQlOABB6uQHU9otg87ePIy1RwpIPlwQYQMZM4HkKtt-ANUVEuspniW9SJfqVi47TzHozvim7bwlSe7gTQtVSBDOR7ZvQOGAAmIvI4J-PLWurZ4vwUgd-23lGUOD6LTeP1z0GBqCzLBEiqoFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=fjCfcgv7OGH3vK4a7gIVsobWnwIlM3Apspku2BJ5OgBM3o3eruGTwbgMUYAqdKC50ZlGaR2928tePdc7Rl04cKdM9XHThvpKzu_0jE6NjkOAhF8Gd39YAP2k1Rl7KAZq_6OMppg3UPjT__vEv1TwFWAqAuDhj9owkXMU1cIuY9xEEdjwNGnfhRpLE7jN0A2c_uzc7NQlOABB6uQHU9otg87ePIy1RwpIPlwQYQMZM4HkKtt-ANUVEuspniW9SJfqVi47TzHozvim7bwlSe7gTQtVSBDOR7ZvQOGAAmIvI4J-PLWurZ4vwUgd-23lGUOD6LTeP1z0GBqCzLBEiqoFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=SZIcycoyhv2L9vjHstJ0WLHZEOk_lEi5HEtFEG2jiyb9lFq1tQDmI3S1mDfyq-OA-6g5Vs63XkqiaMN1Hu5CvUB9FrteEtfvP2lYpy-D9czGq5ATo3eeul5xlSTOytPk8i90zkxeaJ3Js--YVCAg6N1FJ6Mrm0mpnaUpluz7BlSOz_eUY32IxYc5PhM1xK1_j98qeDhcaAeftFrfjZb3SFaHFtByNRXfUCqXvRtkYk6cz7zI8Rlf88tHKsHebprwdejLwypCTRn5oCh7O3qkpXvT_JYv-tnx93m-toadsB2a84AzBSpfoMz_mJVKNqqhXzvIqd4BR5-v9qdAuwfOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=SZIcycoyhv2L9vjHstJ0WLHZEOk_lEi5HEtFEG2jiyb9lFq1tQDmI3S1mDfyq-OA-6g5Vs63XkqiaMN1Hu5CvUB9FrteEtfvP2lYpy-D9czGq5ATo3eeul5xlSTOytPk8i90zkxeaJ3Js--YVCAg6N1FJ6Mrm0mpnaUpluz7BlSOz_eUY32IxYc5PhM1xK1_j98qeDhcaAeftFrfjZb3SFaHFtByNRXfUCqXvRtkYk6cz7zI8Rlf88tHKsHebprwdejLwypCTRn5oCh7O3qkpXvT_JYv-tnx93m-toadsB2a84AzBSpfoMz_mJVKNqqhXzvIqd4BR5-v9qdAuwfOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui1c7W3xhdn1EaF3FNEuC4llP6ORRbtXLJ33rwCNXMe7k8sWG-vCVcdV0VxbqqBh7kNyH5mxMchp1QU_fXqEs4AFKZ5g2fw6EXGHWq2c_K3V4GOJPfQuPmA09CWUrmHSScLzuSV7OnPGSTYMDfhJK9WC7xbkwcOW-ymj38XOHF3Bz3sk0nEQ4PcLpuJv-Roa8AO7RGygBMnr7XE12xDZj1VJm0VFcUYun2fKi12HSr02zrSViXGU-DiNulJJ-lF3C7VsMYtyc6gdYDgnxtTTfrLN-r5-MusATfQ6cRa4tp5oENIo2MGzhBW27WVkWLqNQ1Z4XZNod7xdDYHSsFSaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUTDKM01w2J5bSD9ZMIHUIZkL-opL5w7wSS9_37x_AIzpRcYjN1p-OO71TKTRRSUMh04hCSW9GRef8ALE4ZmmPnfWEjD0B5YdkYImwUCpXukSsg8ku2l05J4BO6ywi6DwRJUYH_GhWGasSkxZUQ-4pojQF9VMMS2dGm1bXB1AXhX4p3wX2MJvXO8emkcDMOXKH6OayAu_fX_3NXhfFowKDuNFK3lw1w5JxA6wtQoeKjd1ZuXEH48wa_nz8gabj-kG2AL4Gpb4bpd6bmrxd0JTYPC5HZZDyLVZ8iRqYYWIfop4DYmt4OGg4nZmOTGh03jYaffpMgM56rnGb23r---Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viHiNiz_j9iD29Z1eJ6_uA7OngvW0kE-NvngoSkqdCIA5n8zId6skxLu0M_3JvQnBJwxYVIYYMHB4p01mKPB94EWg2WFdCIAXFMD2EjYSk2Gg_SIIfGT8qDBOmDzhSOkbVi_RSX6XPj_Gg1Opn0uzuq_tCISHbH3_9HEMlvIyZSkI_L-UwqCLLKbARobKXLeSRZ1AGjf5ng5xvPhnD-lcP0onqQ4783Ng4nT1q_vFMN235gV1Dv5knruoFNOhm7_YwpIZQ2QKhM1w_IaAgklX_Ce5so_3gYU6z9jfM2anioldrPvEtsNonjfOwpE-RGFRtExfazB6bvmNec4-NMvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi17kEZ2WLuPHeeSbNQFhnY5nNekfACGbr1IM3nMZIMW7i1lys4VdLFeaMx8wZUzQaqsmbYLmy8tvu4iufrZ_G_q1Z-Pzaflth1Lm5DyfvGc16V8JpO7N-X3Tscce28ZSHsev2_YsxNOqVrnEglSOIGrLfJbX8H-n27OgHA692uvE3NdRs9HjRp_G65ljKrBZVnK0a2p11bSiGJmgVY9ghl41P5RIZhdG4QkTpw7_dnTIiDdBrExYP_BBJJTtKQ1NF2tjTe3pC-jvxbCfDQfws5c6hTvxpNwIVpcl2HaZXTA_6ZISyqYcvBz2TobsVMUqdGMzNqh-BrMRKDENER11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nICOeF_be94zaOHMfXlKSzYRpodVPyjObM5agqIRG_Ah85ziy9nk1xpyd6jpe0DThHZdsFyay68kQEKU3yEle4cgaqc9fk76952BB9TJ5T5ZqZIC9xPjXJiZsPY7uhMMLyghkAPemkuzEBiSy-FcIja7iskVVw80aFDx4kuwqDOUDOItvS1UlN51e--mLkYW6vE5OKo0wHs_EFoXXY2tf2WQcxTGUG4q-WWSxBFF9zd70P90Zw24H8QWzmpruRSmTGSt3N3FB88pdwuxqA6KhEZbwHIQGHmSifoSZoreyNxzuWs0WQGBQjK4pbnGWKIzU35Zy6rdyoyDSJEACh77IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHdI5SRh62iBQzbv1wwwDaJWJ2EietxHuw_VOG5MaeYk7MwNnE2W109rgyzxuj4XNZEqt7xzbUw-y3ck3wDFwt1DhN6JvAHuRLbapM8ipI6b9sA_YBf95bCuuzqEFBHdwS734x8MLJI6uBR-Kuzfrz3et1K-APe9bnJmV6dtUc0KwxrtF9ELapH9u0wmiE7kWvhoWcs_2aDtJuOj3mwp6zVPPDUfbWZNTBOxveMxq02C91V1oGtNs2daHXKbkpC4BtPWYShQn92LYoaO6-FeB9zsw1csq-CHsEpM8U6h0jQcVcV0Ywkkqv4V0jKw0kwm-LIug2RfCkPcXDuBPoG_BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9fn5dJf2AHTS3vBCJsIkA9hf-dB3lzAZEFlklt2rqHLO68qXAZQYvwnHcVBZUEAy7HP81cBOzXdFJ7YEiHXzDWRir04c1iGw29bv60_7iwJxDyIKixJzWqYtZJB4kaAs3Rykk0zWyvnTafTLPNpwl0yPNzARBtzJn8P4OvmjL0dBvG4_zW6NV-arEqDMfrSmHJt2Y1_wxwTIT_APTLYWAD_seiv-2BI1jDG6EbqIf6XKIFcemxXUeUGoAKMxIsssDCJQq5B2Vf4yPJhJUsHnEPtec1VVkElUc6-JofEfMDc7Z2PMvwQoX5APhmaVR4rtUkpqaBS6G0mSzZWr-P0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az7hrAk9-Dxo51GQEyzseiSP_OxAF9JS8cjHoChN16ShZ0fFScqBwSPKMI5YW0wWqjba6TdY2gu3n_ORQRRg6vL5_eghtZ5vh0G0-Ds2AzcqVZJ8hnSOILB2MvNk_BJfjgD47Aw72TWXFodeeqkwcZMnBfl9OXj6jbqrHo40A3GA8pS5JRW9-3IC1EnDb7kyLDvtn3HOxY3yhfhgqC0LqBJ3BqgTODXh6Az9J0E98YHGEusZA5e5UBvK8WZtwWdVkvPcRP18up9CvcMCI5HVOPe7Vu7CqJcO6WogldlZHK-QbXTdOvfSsuNwcWRqLcaHXxvXmCwXkqJtRiTwANrpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=nP8o67UawrdKo4SpGc7LLtFCprT5NV6H5EerN5YZpcHTw73tOCOIWTl6m_a7wHlJ845pVst9kwqghxO3o2tf5sJo3raibncZrsvzFqa_frgbvPlJ5vci-7SOhNQOU-Z4bFjYrTIZn97N0_J2o4fAt-46PEBIluIAOZgrDdb8XFIcNizpvJtL4H-Rfo72hB99XQN-Of22vN_5jrEGfrT8WAH0mYO5VNEORX8PE3vFFCd8f9ptXaE-gp_4-LK7ouMMbTni-HZXdpNP9nZKoXhBTtlxoDhDc3JL1geLuZlM2Cq4gyj7Ktq6Y3cbYCM-tXgQt3q7yn1IjrUdfE0Qb7n9iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=nP8o67UawrdKo4SpGc7LLtFCprT5NV6H5EerN5YZpcHTw73tOCOIWTl6m_a7wHlJ845pVst9kwqghxO3o2tf5sJo3raibncZrsvzFqa_frgbvPlJ5vci-7SOhNQOU-Z4bFjYrTIZn97N0_J2o4fAt-46PEBIluIAOZgrDdb8XFIcNizpvJtL4H-Rfo72hB99XQN-Of22vN_5jrEGfrT8WAH0mYO5VNEORX8PE3vFFCd8f9ptXaE-gp_4-LK7ouMMbTni-HZXdpNP9nZKoXhBTtlxoDhDc3JL1geLuZlM2Cq4gyj7Ktq6Y3cbYCM-tXgQt3q7yn1IjrUdfE0Qb7n9iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOx4a3W4837Y9TdYvgwQoDD1rme58PKSAPkRu3303VDZkiJ5pELlwzaUlvM6J_VfIyWLmrdztBw0sTfi_hkzQj_UD2m6qIgo7xduP47BxffLVhLO8t2A_RKiswyHXXgNis-6Q16XHRI07-fzea1bKRVeuh3rHRDawU712c0SNTFxgsXbA-BZjATuHkZp0xrlpoU9weRY-xYgp9I8HwR6A-eLXlPQsra695I0hEHZtC0fplKCqUMILZj5yEIrC80jIEo87u5LpvghvRsM9QNGGjhPjNehtw0L_rKcIY1cydlHDMuGD2gfvadptxVMfouOJlv4d4nYZOUJSFU2A_bInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=AjW_xDY6AomQSP50El4j-EHccVf1dgQZCk1HcMPE2vxlKuSzsfLdZlSnXzv28u6isLwEM9KEqKS1-9FosX7qtTWyLcJWFK19vR4ybM3Uw-jjTBciOG7n2m94oT3G3rXlEAZGXOQFtSFpcN7wkUO70gtBfYcRl5iVNDhg6Jg6SwDr0V5aAxVHLSvrZxxfDG7DOEX4xCX4fqCE81U4phJPQevstL64dY_1BQyyzrRtqyvB1DdbbnqBgHfmwMiH1_UbFTwtvYslznbEL3jjXVly5tDuOEdrxjli6i0PDxRt19OKWVmRoDfb8FYVPH4QaeRZJUMvr1-TbeicmOlxXKJ21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=AjW_xDY6AomQSP50El4j-EHccVf1dgQZCk1HcMPE2vxlKuSzsfLdZlSnXzv28u6isLwEM9KEqKS1-9FosX7qtTWyLcJWFK19vR4ybM3Uw-jjTBciOG7n2m94oT3G3rXlEAZGXOQFtSFpcN7wkUO70gtBfYcRl5iVNDhg6Jg6SwDr0V5aAxVHLSvrZxxfDG7DOEX4xCX4fqCE81U4phJPQevstL64dY_1BQyyzrRtqyvB1DdbbnqBgHfmwMiH1_UbFTwtvYslznbEL3jjXVly5tDuOEdrxjli6i0PDxRt19OKWVmRoDfb8FYVPH4QaeRZJUMvr1-TbeicmOlxXKJ21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1RStWsxG0V-aBaG1XsnrBYFNR8BzjfqPUA8UM9ANrURpQXuHpYHVb95n1v3Q9yewP0DZUxonu68z31GzRaQHzch7-VY-v-a_tve-25eBOd7ypliRb_s90tbZLjxILD82SKg1YyhulxFmpSRXqb-_m9ePadsoLoLGdc7HPcAVJ0gnkSDJecmI2uUpOy4XsdnWOY_cIG5OkWkma4WkW5erfUFni01kHKuxauoI0nZyY9q-Puz3VWwIZaSVowFgUKgfV_7lMpvZWy9tnY69W6l0-LJhNZ_t7u1haNVTVEKHcao-ANod8L5ItyK9f26zp5ZBLUpNLJ4foIBo2FHUHByrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msqeFovikZwbZR7-G8fjFWWqnZ919D6w-P9tJst86cRXNFtoBjs-icBtngqjFuG1jBnR0V8AFR5jD_x92Xifxm238CUHtGtEZ9mhT310RwrPgPHTSp6epY9ftNX4fz6CV3MWQYXULhWZ7Jg7EPGixVlMsrjnvm_D4ueO7Dnf7Ou6LOue3dEAl134lZlwHW6ISplwo8Uc5VImawnhICCA5ada1UlsPQu92vLlYRXLqdFztVs0QlalO1qAZ-fIeQh6q9DF4kJGQcULM1wdvItHHFG36Mad-9KSLJiy6SH3rf8pkdI4iq57cW82KgF_I_6ZTcAqF9Tpj3BJYBXmTrXqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWGzebuUiPedIKt5hBm6nxOnk9A2Ak5PzDB4Me2-heiAur0Y5_5kZ6IqtUid4I98K-Fg3uvEC-k7dadVLhEzgcwWbe45AawcPN3vxSFAuKgP0FGiDZtkeIGtHK15l0OMlrHcEWHXuCnOhKhwAt0gh2pRFLOVWzMwvqR-bbCppI4SWalkXgYHXK9NtyhXM3SsOFWMoYJEEgy2j2SmJe-CHvae1GJ3d-U1vBMLIQk4910VHTrYMuav6khkJQaG0XHHqRj4NaQlFLpk3E2u-Z5PFE3XcTSTHIJWqtCKmKbutFCp11rExIfUJihB390oEcVNTzZzFCrqgqO9-XvwcTgAt17E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWGzebuUiPedIKt5hBm6nxOnk9A2Ak5PzDB4Me2-heiAur0Y5_5kZ6IqtUid4I98K-Fg3uvEC-k7dadVLhEzgcwWbe45AawcPN3vxSFAuKgP0FGiDZtkeIGtHK15l0OMlrHcEWHXuCnOhKhwAt0gh2pRFLOVWzMwvqR-bbCppI4SWalkXgYHXK9NtyhXM3SsOFWMoYJEEgy2j2SmJe-CHvae1GJ3d-U1vBMLIQk4910VHTrYMuav6khkJQaG0XHHqRj4NaQlFLpk3E2u-Z5PFE3XcTSTHIJWqtCKmKbutFCp11rExIfUJihB390oEcVNTzZzFCrqgqO9-XvwcTgAt17E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=Ieos1GTapaqRzaLd0lMA-kd76UpHgwz72ZdNi_uASOtSOSM1-CJZSJfIU8koum1d55eejM4b72ou-e3nVzPTNOQPQA57rID8Q2HL6ruz0cuCfmtq2MhlxyjmwEnDHhcz1WzkTQpxGqVouTLrnYUrEFzFvGDQmcX1J8yQGhqIzkUchHPDbmQbZz0Z-0hPEJjcLA_urC6vZbFsD_H7IfszN74fXKP9bZzyL4Cles7LGgXwi4iLcVxDJuTbLfFVH0ySzVNlWRVV8Dm0oUk7UPoD-e1aVbPCeMrJjEffnBlqJeTQukOYZsp5Oc2mmINIxwRhvj6kYzURDEVaknLYtsmx1Faic-KGSXsHO2BKrFHJuzBObo_MnBM21xz4vzPM6tkhyn3ztaA1opRVbI5HLdunAJpvOOccMEr6Z2TKWiJHKtMwT0jBxIvL8xwmv3O5om-meZVy8xc2i9thDn4-O8ioOu7CTzIGDQzo69AYKeCZTnm8vV51CXoc6xhmI9LpRlFr_s8UxfIeYHCjfQIdcL-Ej6hhzVTDtfij4X2wTfdKp6U3oZYNeFk743a95YwfLK9ZrAOTWLGafG2IcMsq4PjOnt8WdKitfcqGy_gAK93vGw9BozhtBaDLqp6hL7cGVdXB1972c-0f2P6JBSFOqNBZqa4Vj9KuWlWse1IqKykp1FM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=Ieos1GTapaqRzaLd0lMA-kd76UpHgwz72ZdNi_uASOtSOSM1-CJZSJfIU8koum1d55eejM4b72ou-e3nVzPTNOQPQA57rID8Q2HL6ruz0cuCfmtq2MhlxyjmwEnDHhcz1WzkTQpxGqVouTLrnYUrEFzFvGDQmcX1J8yQGhqIzkUchHPDbmQbZz0Z-0hPEJjcLA_urC6vZbFsD_H7IfszN74fXKP9bZzyL4Cles7LGgXwi4iLcVxDJuTbLfFVH0ySzVNlWRVV8Dm0oUk7UPoD-e1aVbPCeMrJjEffnBlqJeTQukOYZsp5Oc2mmINIxwRhvj6kYzURDEVaknLYtsmx1Faic-KGSXsHO2BKrFHJuzBObo_MnBM21xz4vzPM6tkhyn3ztaA1opRVbI5HLdunAJpvOOccMEr6Z2TKWiJHKtMwT0jBxIvL8xwmv3O5om-meZVy8xc2i9thDn4-O8ioOu7CTzIGDQzo69AYKeCZTnm8vV51CXoc6xhmI9LpRlFr_s8UxfIeYHCjfQIdcL-Ej6hhzVTDtfij4X2wTfdKp6U3oZYNeFk743a95YwfLK9ZrAOTWLGafG2IcMsq4PjOnt8WdKitfcqGy_gAK93vGw9BozhtBaDLqp6hL7cGVdXB1972c-0f2P6JBSFOqNBZqa4Vj9KuWlWse1IqKykp1FM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmO7NnIImO-E1tiyAWBtBIwA2Y25152LyX2rm5TLY0Z00fYpcDCFIE3LzdRnI_pzHi6RWjmtUMDTqBqTIJWwyM376iXd1JnVdNJQk2zqR2zN60o5vRUnlnqNM7lPLZMwLOTcQxlLgBU9Z1D76N2k21JVElFn1-GYohdKOdGaPvkIy1CUYCidpXo6HRBcYMtFVPUX29Pd48hX9k2JtGVs-4rNV-9jsbFUxGFkGXhZo3_7UWn7RFEX8HqffLcKdvoHJNmGd0kYvhh69CkofkuugKUydjcVLOwUW6CPkRa-piPwsPBFfiHSri6IQo8EQmH6JlWghgRvB_GmiQVp164ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTRXNzpGTXBSPABO-EOOZPUK9ID7gKPXVMnzYl5rjB654aslrXfriZ6uOo70N1wMH_mUicLRxBWYTgLZvSX8CnZDkSo8JsPWphB1eLysDO4HUjuZNkO68eao2yj2XQp-ObcM90oe1ysJG5QfUYTWqLF0wmwjuYDkBPSPQf8wFkA7-P8aGYvaX5MSAgCMmDxoHTp7Jr5ifKQh4GTcO1j8aVpYRyvJGOWIX2djPw5_tHDc8Kzz6SQCfJScWWeSqXu1IM1SvwSY9d0c6RzGIeNJNuMB8azulGc6J8Kym7NCOQSZnprZ58n3KfQWPNDq8p6e114FMwEcD__QtnrHono__AqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTRXNzpGTXBSPABO-EOOZPUK9ID7gKPXVMnzYl5rjB654aslrXfriZ6uOo70N1wMH_mUicLRxBWYTgLZvSX8CnZDkSo8JsPWphB1eLysDO4HUjuZNkO68eao2yj2XQp-ObcM90oe1ysJG5QfUYTWqLF0wmwjuYDkBPSPQf8wFkA7-P8aGYvaX5MSAgCMmDxoHTp7Jr5ifKQh4GTcO1j8aVpYRyvJGOWIX2djPw5_tHDc8Kzz6SQCfJScWWeSqXu1IM1SvwSY9d0c6RzGIeNJNuMB8azulGc6J8Kym7NCOQSZnprZ58n3KfQWPNDq8p6e114FMwEcD__QtnrHono__AqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgxgdnHq-2I-KWgWlBNxAw_JIVgY2jSvkgB4dQksbf1Hfc497pF2qmk4UeOSOjVf8EKPWsSHLCDgw_2W-vsEuZfL5Paijo60O6y7XR8VMRERoMSreubBtar8Hbx2BNWN6DaDETmIS4iUfvhLMZgv0bpCXP-NtmaEvQZ-KzH35kinslCthqXVSn2Lxs3gjxpU8i2tx1YBc11oFMu23X_VlgLL5JUcnt6xK-AB8KZ8C9Zbpsmkwm3QlXwfvkh4PKbMSEWQo2V__3ngZYDJ5qguRetefh_8gjuNn5MOgbzFJMyi6T4EQ-qXipyJGdzFnJnJwMU1Fb1vCn1PfXZ3pQv8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=ujJjk_0pb6ML2_uSduRPpIzOMEWuvIuzwhFq9_D5CsPIFFToI7iQ0LVdrC-wtU6CY3Gal579194RJziCsNdTB08Qd_TWa58HCn0J8BzSs5edurHnNPqKv9snDLDegGywa2qc02LnUyLYvzAzTbeEUVcA7wHOeqgtRUmao1--_D1gSk69Onymg1sCIEoOluwXZWavcwkEJrfdJnKBF_C6VA0qRgbh-VHf345uIjzIhGoqR4FGDl5_Aax89S9tZ-HWZ0klNZh7DSJWCUv9Oni7pPtLWfZpXlZHi9eKjG3fKEV6dJnmnqKItNNYOGqYZeWtMVLCJ_wiaPQt9WPU4m0k1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=ujJjk_0pb6ML2_uSduRPpIzOMEWuvIuzwhFq9_D5CsPIFFToI7iQ0LVdrC-wtU6CY3Gal579194RJziCsNdTB08Qd_TWa58HCn0J8BzSs5edurHnNPqKv9snDLDegGywa2qc02LnUyLYvzAzTbeEUVcA7wHOeqgtRUmao1--_D1gSk69Onymg1sCIEoOluwXZWavcwkEJrfdJnKBF_C6VA0qRgbh-VHf345uIjzIhGoqR4FGDl5_Aax89S9tZ-HWZ0klNZh7DSJWCUv9Oni7pPtLWfZpXlZHi9eKjG3fKEV6dJnmnqKItNNYOGqYZeWtMVLCJ_wiaPQt9WPU4m0k1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvHTLk2cu0GrSzU5xF9DSKj5aw0megkBoL03D9nUfwQ3iy8ytOyBidZQlhG-imIrb8a7Zs3GjxFe7DTAiY8BOJDPzEfRgQXXSKMIql-_3b0YQrKPuInxDtirOu6eAPTZnCj_mpKYHhfeCnzsQW4MzErwI3xXggvJxYWaXegve6evdw49MHWVlMyvyHThXB3AkV590UNzSj4XmdVFqOaNMnWbWmTrgRtMT95yCFsgb4LFAzlx_ytBiL9k8wok0z2UnnDCxZ6LioNv3qmas2GEnyVbHnXcLQAjzVWw2Pbfjm5R5t_Pt-7ATAIso4OmmMnSP5SGUcfDEWKBWFBu1Q0SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_LITI89VXcpGdPaSxTM4iXhwaCaYNibtDvDoxQzD3Y3tSLOa4aqSY8zuTuf_4DOlNvdCCFtgyF0P6Ktyo_fjE4UOmUDjRWrouUnmlzMHctDF-j9I4yz16Bd5LirpZncjm-r3pY1_FHqPJESyjeT1VFYIVNiHYFSCkwszzpPQmaQajD_89VOlC-AUOalrpMZjOyahbYyBngyPrygS8nbDCTA9E8vrT5jxBwbmW6wdbM9nTRiX4m3EMQBDcfghIR4xAei_gQmOGqwiP4aZ9dEmblew6uU0VrEFaOKkR5yeWC_PZuOo393_Zlgyt-N8KTmCM83mr0OZWNht1P74ZFq_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
