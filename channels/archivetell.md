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
<img src="https://cdn4.telesco.pe/file/GbhyCUEIl50r62c_J1EKXN5Lbn0Kr3vE30Cn49nhrFtUDzDEzNTYaF7pVMiK8ApWhfoNGH5gfWWezkl69rkU9ZRrckNybN3feLsr_olTe46_d4fPFXdWftbWkho0qAVdYlKhS619eQdCMf16cKJdYgzK2Avd_r5_eOI07XsLWb3MZPbFUq8CVMKM6yxFxni0PHATt3kYJ53zwzGziz4jGxptFqex1OsuFTXLM17GqMCzqp7Z15pV-cc0yiODT8YS6xEEQx2qlJvn_ELazl7K56hEue2GVuOkbt2s_iTVTpvmSvnFZgXJKp9x3id6idQ6G35Ioc4dMUF6ggkgJoReLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i29PHiaKQRcPFXyQWVKKhZCSGWPr-wYLxnub18yLWF7wEVaRQ0jK_uTfD7rvMI0kn428BOoJ3ZJ_7s2mNft5WfbP-OJwFc8u2aTI4eALvxOQCaYHKq5YJZ0wbbKmuMsyx1U00UzSr-a9ewegY8h5bIpcSbwRmr0Ssvw2wisHATZKgcQxs5Q45pBIHfNXtTYxiSI2LpAAXXb-K5nTOSzRio00xPgoWMlddOmQyL-fRs31UEqYtPnL-IibAFIDuuQaUj3CO1YGpjcfXcf-wL8VnHfpc1PorvBcUUj9Sjjh7JxxYZVlRI1Z_s_5h3V42hw4e5QqScoRCI1OVjKb6YHwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tj92ucQpxx3QC1S0BKQkNNqtdDJe9-3OgG1oRgtaJLZzGLjtpZn9Wu9O5QLaFuvvB73lW7b7bMV4X8fnF40-Jw89irR42bjXlEY7-760ZAEOkaS7Y7vKM_B0KY-Yt96ovCWHanh0u00P87cpgDPuJ4YOMvjOThoFxI0OjpO2UeKp7HYXRiE3sHfEltcNoNv0rbz7PeCJwKj5ZKMcUijem-5yZEliL-4aqGoiulQ1AXWqvb5-XESXbOqxnIbhnusoqMnBjASXG1l9LzZTDsvw6-I57CbohC-oMtja-7t0g2Dr2Se_uK1x7dV6lHgr0-L0e-ZSo27VFY8G5n64HDV2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hX38EOIkBiy3HEazpWc8MNWcegGlEv7ug9H_HtVbrNK1ujIcRS3t7Z0jkfGS9OVzQPA8vBq9OiKMB7d-0p4BSJayHJGq78LTB_RhdQvBy15FlKwSmV96-QeAJv98SncBiBcZHhMvHDcu06cL_FcCKo8erSDU_oZY7g8aclqwAUX7vrWpZVLNVt3NxoTTWIxuL4QzTFegVYWcTPgV_r9kzSGWNxjbWpIqKjKpzYIbDaKd4LInq9G8785cDsfehvI9Z-mzzFa3wx4GvMpc_cqhTY0yUIndwR7TJBUgTOEzaHgL351i6HSdXM-_RvgBXrllZwk08utWiqZrNqwIjOlPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fl7W0iyGXtUdfaZPFYRdvq9PdsOKaJPsda0GRuIIcOnZbiti0VlRYC7PVo80sLF0j0_Fzq2dkb4bCvqowTv4F5AyfohnxOaBbXy_xAvQop5heXP_GNvo7GoV8kMTguKDSXUEYiwdg5g9ec7LjcmeLvF0xQMrpeng2NUHXjSQ4F9r1lQlMcK_xAyC2puMcoQVcw4I1go0tO2AZUdlwrTpZTeFoSv25wZpeVi14Z8wExanaGXXy_-mexBcU4KDn5D72L_iiUHjxJT2gmSvAcw4n5IG5O4CbO7se89kE9ApxqMZseVXFjq5E1k5Ssuo-tsaOxVoPHUM6ZLAFV-0RktL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP9w8obLMPQenuPCxlunaXT17bruupU-wL1TEzqLkaxNdmQfwfFJBhhfBG5KH_VhLzhlvCn5nBF-a5oewOUmO8qkFkuMdnRXv3e5nHrYQYtpCnVDl6lAxVz9d6c_yqh9sfFixqsFKQYksATVJLcRZ-ECX_BkVoJznOAABKwyzuWR6IwnbgaUIU6Dsm9Q3-OjML8mNK0oFwhKJ-uY7kgIP4gns-pVicGvbqx8SIz7nGfz9VwgQpoXByWzO_bmA0-RFGdqpiBpRD9F2H0_Hp9SGvPIpIQNSAteAcrUOdGuhJi6-nIg4WU060A3DsXefmc-EL5syZAs-jxO23fDEIGmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1CsBwos-3gs-G5NmrQF43uaK3GebjZDkwQIthotayHhmv84m0IpkdAax-uzy9uZRTjTg_91QFuXuyEISevIpSw9BAEg2zTGAtbjgRBbGofoJEAhP7P-880lKabs_Q5-jYb1MT9VRKTawtzpYDjy5LbQdHLNQndDzWbdgh5HU1uBv9GpDhABRKDlMxGxp9NibPQqF15rX8B_EfN4Xq8H4gmerCbGcEQuYCfJAD76Ha3WLg49LJ9bYj91aNVmJ-S4wcVtBatWDAFXjpzGhF4XLViRviyvk2VR_Ic-cdp8d8ZUqjmFrAhGD-65L7b2ZwLDq_EjmyuAsfxGx9HcjF47vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3PL_cZzahhvsTi-2pisvJzRCFkSrHfrV94OD83-M9lZCjj-1K0mk0CTZFHcvuz0g2ucZ4MzrP_-Op-jn2bf0-acuusxuAXSTNdDoNxYdMep9l8JyIg2_e-viC28pDckb4_181ziWza5uUpDD9Z4okg18bPsMZCD15YWC5RLHTx_TieB3NYKDW8V8r-MPRF2oZssnD89EkYIY_WHlhzpVIiB9aLJ4jjy-Y07tTB5T36G22W2xMhRukD9T_mnvnac9tKMM1xMdH_sdJGng3sKuceRU_JMyJ-zTihfWZOysOaZT1e3ozTflkEvwCCSOJV6-oR0464tJo0z4jZ3CeTDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEheQYzx11i3RaNSTMu_5OpxCaLtO9Dmp3D-RkPuuxHFjgg4JWVfcSW6jk0zbS5HduX2Vqep-xFpV8WKGcfV0hs3LocgK2S4eArZkQERNk3vW8zaBht1xb8DuG5EZL_5uSxMR2Q3A4PtilJrdIcnGY-28G1cKRDOSFuCRsfA428MoqZVeFgnoTrr8DGlNmkW-4DIm7nEJXpjVYAQq5xd_woWUjnUDFTFVNVE9DUrWSu5IF9qLKSmy6xg6sYLglsGtT0xvbM_aeQhuU1P-AfqvkvpCEtfy1xjaLCheW8RRc6o6ku5qtqsVfP_rBq2Xgc8qKUaSgJ5R6sDUSjd8GEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNWb1SUnY_NjqQxXn2PeM6jNgung-71oWjOLSZ_gc-qcKS6Pns3SWAvFlu83cBsTpGOerceCNKNgD3taAKojLAVdQ1OaPC7tMo_KBRpGce3Raxsf_upGuXniy_jCyUMwXFjXwRCKQiGX3hVnp39ja-hlh1KHszMpmX32u_D3y90ZrSeRoo9LbA96B9CB2dwb-4kmlX2zQyOT8mww067Fc1wFpy_1_dhWU8KCcP5GJJlMDtSJ7_xujX7orEeMXB3wgAUBNIujvtMmQ9V9_RZ49dUMeX-ARF6kuS1a6fxgi33KGzsZIPXcHj6irVHy9PTk4xyeUCxbhOZSc7BywIxcQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUQCeWqVuQzkxrrisGE6TIZhP-BDimJ8HMsbKqcSoPYNMhLqvDEsbfVCtrn5QkNfSXHqI1dqiDpf0otjETh-BYGEhDCdtVvlxrO230ttIOksqP2wcDAyd8kUjjVaAW9gYP_DEnBMPolrAuwVlkEaoy8iaywpDL_WqHstn0Gwg_tymorQUl9d4ANGbgo1OelhVM7p3Q7R-MZ8AeyUw4vSN_gQZItKk9oPfSRiX_sXdeelYUZAKlxAQ72_YpJ8NkUbLpB2AzfbpXEEE_Vhx4XEkPEKtvPy9X20Ko5IICjwkXTE2f9Cj-QP6Q8E0LqbDoZFx_Oygpg33iyXr8F_QMOIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F11WH2XRtPdQM2XguGlmFJKtJ99ktogRT_XJ7DkgQEP0IB7cBThewrvwdiI2EHmYSfNX8uQTAFvHhp9uJ40euPnvJEicOjcrwBZrbB1vXt5HP-6DuUGkvbzuO_joly9Sg--_VitijFsZwMz8KFIJ8ujxrFww06ktHeAe3BqF32xSvJSDdukJrV6hbxp5EOOFtoKJrtSSgN59vR_XgSZPxtb3wEZoBwy40wADRmqc7jym-lRPXJKPa7PGfNjQpvUCeBljDwmDjIqaJGuStG-pZIkExqTZOmjhkkT2j1lmDEYqeVpPEcxsUJUjkIwW2ILgs_2TNi0tx7tHzg_X2DB03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMyU5AeYGgVKuhNQ9nHQbx8kKpxosjioPJCGMU9NH6p-13OiyMMJe4OJw9mYEwbn0Ko5nfCMLTTQCKRNftibcw13wSRWUILwmEq-kUkTYY1Uqk_H8ILStT2FhiBegRtu6yc2ww0b7XAfsdcxdP8FloHGju41k8pFy15q8HoOptxOIcq4P4weACagVaMjEqOBzIWIFOz8l_ElqResQBv8wBhzWrh_NdLbwCN05xNaJ7IOTi7Ah5DOieP04cFGhtIjtzJNhnvEs3qu2Idp9pQAWfelJ1nEngLxYtzjX4dmKVuMQtqyK5oj5X0AiuBhGJZVpDCxyNvYMxkbTa8x_iDWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu0xJq_fYs0AfrjenwGW4sW_FfIM_PxNJY8kAS2Y_c97Wa7b4UWU_jbxCPaPsAuUCdw4pqnxCaS3Ep4gyJKxx1JJJOKN8dxpa0PXBb0xxrIfH3-tMWa6ThJZt4QdmldHHd_HppVr7YPO6IyRgzlrNfZwSdL4AnDo3lvLG8TjPAEZH-F_e-q-yLZ39mzexV0dGVvHyvFQ_bz6ct6SE5l4emKI-koGUt9pmTc53O8pBB8rND-5IMkTtllMpkXKM1daEbH8XQvrwy5vfmqYpA0WSSseFmzw6h2DBnoCUXACn8a3ofGbEC3O1jKrDNvFk8u-hbwvdhjMxDxrfQlPYlUiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRHE0lu_Y5vkejTwWm0Six7cCGZzhJImTnQ-CCSKNUaOp6FPQ12ubIZfPdT7IiBatTvXSvp0QSKbPCWV9kSqd_B1if5hdlpuvhbM3Mkuu7GjreDWyHd1XsuizfML4UD1sjBILfFH0cKkN9xFumgfCdaeRg1IvixB90wqZqjy2nzymrgIsY7U7fkgHpm-7Iizc1tx5JMcMUYTDgpfEKLX5QPtrXnsUdLKr6mQjYNEyEZEOGUIvSSn3QPBp7Rj9EEelHlQYqhFTbA0UjDnNjdiEDV4gEyOUjHXDGUeYUhr320E2ysCba7f7Xj7AYGmUNaQA_2DNz3zhkhTExX0KqW0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO7J2MLRsZ9FCudqevoUTOtk7FKSfvfWHDW0OvMbJToIo_xfcUq6W6k3xDcp8_Oo644F59h2kT6kcac58esOK0NlNaIf7qJJeJqSA0JGOegi56yzJHF8gXqCx1V_PIcs7IGQ_IYyEbwb-iKx9se_HrfUqQQosADvenyj87_LTCx7kkdoFDEe_PZ6SSCVpsnaUXiPli6EMQcYk4htBfkSauPZ1G79ieexr3MhZl8fV9haCJMKlBndqiK95lhKxnwZy-MDZM5lkyXmSfacurAtzJ9PSv0pEeaPEzZ5qEvXqZ8wvepbPo1xydYuSvcd4W7fA064qWeHvf89WHHyoLWltQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn8yikBMy6frNGJ4PiiV8kdj-A60NUWCLgxJIv7nyeYWGOE6BppeN3DKVJhSFwpPxcvNiCeEfqvSFZxnYDD2gNIwAHXGtX_0e9NYtYsnn5N0-gPAEikoWMXD6_a4I-WCvUUh1DwTbJX4KkJdjZMhHm3BodrWjzUqErgrJs0frlbEbMbmIPZLPYPmZgGhx0TlXJWmnEM4hNcC2Za2fDyXTF_7S6R1rLG9hlzJngP9ZCI8HsBFjQG1rM5zyB3vTJPJnPhEjtCvxV2YJLFyg4w1ZAt_Fdaz-rqkLEAQGCfVb5qLe_cVA250nY6pEU5al1JFplIkwIOgc_8MavAXNHfR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKkjtALhz4cNw0KLcSf5wVjvLrCMf-_4WWTiianZL1JNUMvOzrc6TI-vEIgpMJLyoF2np-Koe66MLqQ4gWJSKD8ib6zGLipJd8EFRYNX3zOEe7qcXB6C8CeiVg58mqo3k4kJEZpIMmiuT-C82tlijtbEfcmybG2soVFhdh85dEDh8ltzVBU-4hjSRZEBpdJTRx8XLnFqmhe7st7Ksj9uOOuxFWhia19MxfJUUTAdIrS04qiL1CQNJwnEFD2VTOeuJK1Mc-JQDVD-WjikmhlMeP08t8yV6lA4kZs5Kd9mS_o8US_FiEgqbizdLiLORTVMGT2niKVNtxp7cRi1cURYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLvOz1C0VgEuxJV9SPtjqsGh3rawY6wS-GU1M3jPesur_qopvXzXlwiS0M1gEOQN0R1qG7xF6AKGOHYDZR5-5jTvE0-VtiEKNZSKZs29vqM1H4DPGWGTwanyahVoPJUiGzLK80P5RXiTIkvEX_MlcZdEkzEJMhl6nz-s5QGriqaJqShn06_tD0RUoRiyPKDI2SRCQHTLzuW1i22sYHMU9hGeMNBzh-mphWnHjR_mj0lbyUSmHy_R2P3sbw6nCYdzDqU46bwa4-d7W9_vJW11QGVsCN91bddwn99FfeGtSbmIT1m3al2_dt2H8QwzOUcL1caKa35GbMPqlOjks_hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HElJN6JqcKUdHcISsicU5238UU96Dp7_31Odv4Sde9BEwfH4-KmDfJLtLsPVL-k1kfF4w3PyzT8hWAw32kpAw6jssPMyQHe0lXxLdFsfphHdMVf11g3_o6JNv-7H_vPnqJHDTBsQQE3uuyzhq5tVpYzcxTwTpMViWOxdNgoQ4twqnD1wok5mGMyAIIwfPFv1fnmbe3laPzTU6jCGe7DjiIAopNFU1FCYi3r_mUfSWNzakLUhzikcwBS7ruTxmoPMeKDWF9mVBbm8hH0U7R6mB1SZORwhz0x7RQ258AKAAEpZtpCL4eFuRmMGW5zDcJyJz5p9npIz2CM-WDtUHhqiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQfugt3st4b4HNrj7sfuHfnpPeLUPIJWordfqokE4X7P87TZlVFg46YWkJ5EPkY4u6-PceIMx1A4ynFZG3StKDWq2S9fN2o_PlGqkIJrvIU8vBlhKj9tcPWyV25-epR61S7lRRVOqELUDYrKEDFdqWcBpjZl2WOFSIaCOydQtiKYYsV9Rv1ZRojuz9yk2-SDL5y10oNq1WUMbPGKneKUJwg3IO-qzAln2ZFPV4m1ZjjxwIypAxYWtOX9xeeSsQFy1srXQPxqllYYCk_JrmFTXQzN7NEtHBrfzCYc8B7Fawrfjx-80N32frCs6Dg6BGdaLSFHy8VQtnCbX2SnoKgcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fco0SYA2rG1hZrPRN2NekM_BM8A5XPEZqhp32k8jdwsJ4jHiSriT1XEhEcZcoOhyPQdAUmduEec9LwecYtrld-6XfJuy4NoW4dymZOEYztzzTnpxA6RMHwm7kq3pwPhPNz99EQEBffkIErsl9lRmUQSthXEoEwAgVyHul-uu3scsiZgJl7BCV_8pesu54XtjLeaZe6UmbFxXDbkNRtE9KorqXKA5T-50o2SEzvACHh3PglIXujjdUkSDV8bFQrIXj-MaGw_zDGyDshW3VUIJji3i1GxFqYvTUYYCSNH2Qb4_srN8I2zso8TECvx7jzOSTZsHYru_PDbynoL3pM5FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=uj3P6R0nSXII-asS5qM0l68e8EaFwNpOsl-aLallF1khhZWPUOHKc_r5pocrWSdLZqJlJAdGY-ccV9Qa8Y8JWnoXsHZ4ydcoO2Er0IXf73B12XRDZT1eV7vcl7nueuUIDdJGNoMfwAHuQWz7SSDDMIGMO6NthhqoOQY2_KaVaoUtJ0BHTWHFJp08YVawAQ_tRhco537jNm4-Ii98ohCA-drryL-WjYAYfN1Z-ggD46dt2z-xjXXp9LlDiVd59oNNub7eyIuWh9MUdCek_hUL_Z4yb6fqjRUz2IKy_BI1eIfL_4b7UnXAcT---4GivdF9EDJ6-rcCYuIb98zyk1Bo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=uj3P6R0nSXII-asS5qM0l68e8EaFwNpOsl-aLallF1khhZWPUOHKc_r5pocrWSdLZqJlJAdGY-ccV9Qa8Y8JWnoXsHZ4ydcoO2Er0IXf73B12XRDZT1eV7vcl7nueuUIDdJGNoMfwAHuQWz7SSDDMIGMO6NthhqoOQY2_KaVaoUtJ0BHTWHFJp08YVawAQ_tRhco537jNm4-Ii98ohCA-drryL-WjYAYfN1Z-ggD46dt2z-xjXXp9LlDiVd59oNNub7eyIuWh9MUdCek_hUL_Z4yb6fqjRUz2IKy_BI1eIfL_4b7UnXAcT---4GivdF9EDJ6-rcCYuIb98zyk1Bo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0ve0F238XgYIspwLj9RkhD_pE9XKuLqCUKd-AaWZL052VDEa60MWpjuyWSxHMcQ6ZdyIEr0ejk99QYl0USWlNY6408e_bmaSB96YHAMfK3mdTc-56hSgPkl4FbCr7PDfyi1vECiQ2_SMCDUx2twalpX0imYg6i8SFxdb_1fEZ7L-ffVrkR4tISWB77HGTUExfAWm28Oeui6os5IgZiKn0n0hiTnkLmHJzmyCtueuH2mNFcG7QHxZC9_aKaJ4T3T1frvlkVB6XsFkwnYEQYz-aJsro8dMlhrUQYfEeGre7YQoBKWFN4SHjSz0n1o1wORSRBkCtA6DC3VrYsQCAHSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC5jJN0V1EuZiPvZH1_ZwL596N0oQPX3bVgxhrA-XaMZ25V-NJOlGjg36mb0-xLvCYj3keoULB6DPJZsP-u4pOA5B4zXB9avMlR44swQlL6y-elfP_twWyCIeZ74GJMtkVHiuKVwnYyB4ozDkYn5L1iVf1qUWKc2e7aBzFdTA71bFGsv5NRvV6KgJISRzILfiJ62YAhrajPbGeiMloobIEOwS00jX6IBaiyLBYNVsgzxTaAUMqbtoZcD3P3Ngsf1DrwF4xv1zUGcv6OsyMuMhhx2KdwJsbV2oPJx6340Ic7f8Nd7fEeORKcX6iHuVJ11-m2P59fZ1MQuhPN7IyTG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osos-Cb5YSWJnn5q4lWXnROg_1He2Xd96HDpedSJNGTOczqBqnOaqu22tfnv-krueBxSMsEtMSa5LOGQV69x9LDj4FBDrQX_PEXvitTTYew8wtKha7ntK68Tn-Bud6BZLF8-ev-TSoFYBDKXtvK_lmJxmUJYEP07UZSSW907mRD3twz6s9346B0JpBIV2i5KtMeuBwLDxXBZdKyX19sIJKsVgZ54Rxji2wk9cDoNhUtapiXSm-9aYG6dOzUqzTZlkVM03_tJRqsytbX8Of2zqEAWGMwoy63wuMZz7fQ5rzjCs34HAAwD6fs3zBqZ_ra2Y3_8hMn7VZnlg7ZIyfOiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq8n98jHXAado2Y00pCa583ZxUMwRd1gzflHK6C33BSfHI8duiQ4LrsRUO-DmRg3rjqlAUcBKPfM0bPR4iMXoY0Top1mNecK3SQ-Y1EfX2SBojQ44B75KqKvwIwtPgkzwDXBL3hOE9JrXJlS4QEUlixP7XcTxm5ipHKf70hEHjobFsMHO59B1Clm-OepKuRPEoyoAgppyTvMgJWg2i7YxNwUTX3F67fdXOYNrPGdM4eRJ2DMIm0pJy5eOPurh8JkkZLlqmOn13x15Wdc_kCnYA6VbRCd3FfPtk9xF0XDerNIr0WcWGc_UpSWat9mqJEq80HoEYJ3SuH5ZjPBz_28Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVmhfIv_Oc7GdH7TwHJqe2wHf3xGZY9ZJ1WLoZfFMwGGQrUBLg1BHtyxyi465mny6oq1RhExjLhGeLjw1mszB-6SgZ2gNMbIirljF2EgAchrbLIkoUueBYbV5MmHjomQ5Dr-Y0i6DM9ackhl4bcJKuedzRd-vyqW4QvRYMt2507xR21EY5zWwAy1EVohdw7A-Kp8JBcrcwhpCZBjCAzWF0hLosm4sfgs5_vbtDnVVqaMIqplF82SRzDguTIKJnjaLUCeNZv0DoWOa2AfM7mLGiSDG1BskTTt7KHLBHcip-UQrBQgf-aEbp1_GHnW1yztvvHoWEaZE2T4Oex9IcVIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omh0xsFr92deyVoVuC1qgUYg8xTjcrusje1fJ2jl1pX-7qMrjcJatNDUTQHqM5TSYpeuw3LTupCpW3cOiQoib7wpJszEO36yo7AjlPHyM-_zJxZAVWByT4fnZSwmOuFD8jRbYC5LSpxXmYE0UUPH_5ZZAt6ghliokNEaHNyffU5JECVyNeegro3YuOMjTdYppyWkDbO5IMRJ7XWBTDcX8PQX1YFGZOPoYgGh22JwZG1N7dmICClRcCEcqxx0R0dnroZ2XoBfcEUYj-f7aAYmUErcmU-RIot3G-uXcjkH1WPnXOXApKNv2KohfaTGU8fRqPuXt2dKnhSbgLd7zanCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH9slLb5wcsh5NN9LXw8YP4WiX9tysASiCvF3r_uJA49ApQJ3z7-J1EnGMANBbAXqAEx4VWUnfXWm-ZpG9TsqsZ2dkncB9u0XlpdgG_wwa-H-LjrM0nVeXUENNqHvVOYA3vCPF9Q69n3MhxCkUtwZe4_0LW_aFOmmCwFeRKsjUAi6Tf6aHMS9KpOyswjHbzYeXqWCpJ3ruVmSnqvR1uiaUWfMwmO_E7e4NfNM6YYTOLZejAR2xlGxAifYIb4y92cQNn6jor84SP4h5eKLG4LApT9LIPjhR6PNXE1eVfjO2OtXRLvaGqHR1ydwIOJrNMjlnQWJWPiDWJQ1DDwmYk1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDeNS0xyP3v74tnZNx5VMav4E12VX0H7v0f-ZWFMhksFQ-3rd5qq-fCfVR8Bz9_CAM1uIKeGAvSZGjoPGxuQJFL7JaRq89M1ywRUUwd5iZdELoqn4ur35FkNDW65i33LEzh8ZzIDvn7xp4NbGETuNCo9X3pSE4hdoMBunt4zDCSbZUJmdCUETVZHokZERJ8AWFIcBKr2Q32Ct-B3f959vRsjSlmu1p9OP5m_Zx5bkLMV1ZRKxEPy2PQqFL9dvo2QJpXPw7-wvwUj6Egs5sikvtxYiwLM59V6rtye2PQcSsGCyKAatnYK6byHlimo2JUQ1bWRVZ-y_WOs23B6IMErMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcbX0m7OJyOMKmokqmRCUn4VfNcTzNc2BjeFkKkzY0VUKe9TnKB_6_B-B7q8pUMRxAGT7c1z9rXZcdZA9Xi1jTAoxJ_8Xy8fmVoNDNfQvMh4P8BY0KG2ASmWswFq4vnrhgVZhQtwCgBMjaGDCJsnBLeLyY3URb1CfQrDz9Nd8GzbyLUkvuzihqTCJkKkrY8_x2vsVqWNxhrwYXmIvWqqCsumv-j-mcGYbpVIyJbM8dRUUR3Ayfemt14wDjEdirjhHnHsl0q-OMO9A9YcfEILZnolHVTPridciS0H8DdmO5V22NwUvYJH6pR7JUXOnFdJCklGqhWnH_jQzPjxGsldYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFLHYYqmIjxshC1hoMs7b4161ohNz_LgAZz8MM-_DleaPR6ohFfRd-9MEH-XBw8KnZ3WnicH2ZaP5wdOPb5bWP_yFbD7193ph6fCOVZFstKxtKuD2rJIAiZt0TlJWD3zZRO3xKJtY9IWYdort2RRKz0iqxaL2GLBgmPsFVxBdDdzz2E-3vr4Q1g4bt3Q1-jcRvUFDc_RxJ5annPQI-pTZM9cA6R293gB2NpIZreklzAafOc5i3lnJHo9fMQuvp4Wz_Vp6Q1_WIh8atloQRWVvEnH-ZNGmMZXDH4M-M9wVurMYQ04seNZi-1O6wc8MQm3HTuJpR1AT4VNubwhcdPKKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6Z5Lsa8XAqDnBvug1pF94REkRF2jLMpV8iQ8Zk9J0PSnDzF_iOw74c4stYcgY-QAlfXCI2e4L_jb7-vkqiIxKDLBFKPy6IHaMDX-bfpk6JyAcROVqIVaHmbhLEY6VKBqU-CiXTmJLmanqi0B6T0wHyDCicTar6WfVvNnAzgtzzGW9D5Z2PD_yMOQ9IuYPe5nY8KjsEuuLIEYS1BPIPEo6TbIVRc4_daNHyDnexq9t0SSzGyGVPDQ9pBKLxJ2rjdkgdq_SHN-_KxJL38Kj2-brL9Nrcw8rnSSgDfXwRaOoiETDiHnAzxpCHiH0lNWjHCKzCIxic3ZeCB6VWSGDR7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EokRweCw41NbAy5YhzQECXO2UYQJcfWshWeA99MzWw3h2MakcTcYPE94xj4efRN4ta9-qAK2PnGjhbrNmE2vybzmph1m7Ec4zvxjyR6krg5cUSxh1d46TaftaalC7upARaFiCl6nJg1362GQfmO0_1WMDMqRu349HklFAx-iBcNTZ3p5I8al9Iu7nDhW7H_fGjwATWRstMtJyWVBtP58vdY89g8NosUrycEwLonMsYu52n0ri8nSMIm4drALympao9_GYzzUPXZ-u1jKx8v71Mo9mNSaOVqYkCgzH_UEQEC3KPL8bd386c6XK-PhvMJjkwMFs8fbon_aDnDExt-i1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An_je_rMb9FC61OWDgNrdq3BldPWcUprVhL4qjPykCAiUtqQoz2AzrS4jmaIYpi3GR_ZBZCOQjNXr4jyMxSuOZd6Wu-v13YWK5v6nI62lPuL6zSsP2PXpkTPa3fYG0DDNkZcPsjpAsspQ4YY8AAZeCvacsdv5kd1qXwPTBC4h_dG0BSTD4fkqPFjzx-EN8h-_ZKdHXBBKjBcmmyfhYBjVvjmJT4no1JVaOUkZSzosMMvcbi41-cYIHiU4_5VuFdvimnP2U1KEtHRjk7WiNja1WWELATL9JdZ5T-l6dDkx6Ds5WD9FXK-Eew40l5nHwpCtFTYkNs-um-svFYFYK33dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFupGtbpwprw8_TWmNKMB2im-zT_WNkpzdwsUBlxwRKzjUzJFHv_Xuh5zROxlB5cbPfBYj_9Z5MpiWtOCqHjti7QQTRVvE2SWHTNhLz5kolq0vvO2y_AmzFfsiaSomjzOt01jb7DLax-MKN9bpZREWX1wxs6LZO51-Pss4JsupntVF3vypwfpGsd5A8KRH5WOLx4Qux8z0MRvax0cnh4CKony5yeYot9bp54vOCTADHrg9MjCe74nBOEh8u6NGf78SH3RsadZKpBa3S08_7VibMAwKmW4ks0NRteS1sZ4NYQ-t4EvFv0enmpU-aBuOud64aKhXCysfJ1A73-aFC7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7cOn0fd8FOAnQE5yf2RxGfa_fuHCDe6wlYRiZAU16vspTyuxGu_n13KIrEGWXnagTB6f4JorV7MqrU7YsciNr06umieG6mrI2uwYx17clI61PAPMgUZaLifQgrMB4A0k6Tl77F7OPPUdwP82v2WvGYuk2uF899sVU_TW3RzHrMtk7VWp4Mb0rAuAw-2PoQR1IU2vL_GFG389Kz4vX-bDXM0TyT_JEIyMY1Gurb57LdCu84zJ13uRuf243R-64-w0GTku8deaHd9UTK0fAwN4BYMfW6fB4Du-3iJER8bEg_3scQGJgX37DcR9P-yRYnHaGdV30gURkD7tqZcpmZ1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA6LZsl8YDdAskbdd9kV0Z53p9p9fQOTYomlCX4eYVkDR-8MbwfLwbVu-fsWYA67j2AeFaZFhnY7j6ddglYbbJcW77P3WNPBGyOJKxY0Txw9ncEXVzctDLMdrORnQxIbCLY5J7EPx7_MqlSbNbR-NzL8r7MvLJiTUFvSbgESgyLeDu8hbYtUlBJH4BcK3sugf6vP-5waHv9vc3UhkZlvery8UbpVH8Ccxgte4RdmV5xnP8Z8rcMMHHHOIkE3AuXSaq565P_5lVLShbVpWdp_GT5b4yY-j__I-3WLjk3dojlu7ANawOSZ0lTsFPbQmjnurUoWumeWOhN3d0_yYpKyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9Uhn7NQVePN16anJ6yB6AQRwWiSx7hVWjq6xuy_nC4a50OqVXhGUQpppl27XI6cp3vI50RXm9jwN6mShytwET1G0c_lM46i7pNfQ9KmGwVNLoR2kW_28b0rcr5rFJos8KWATKt6cOVpWgY8C3x63lp2awyQ06ZAHirmLZaUg2LUYzAjmNiTW2WdyCkS0cCZ_eOHFcdpeAyxFtUThWR0vZKLk0ttSHCQp3DcZf3bX7nwS_54XQ6V1HVUMJea4O5rrIqTGmECLa7h4IbLjzZ4j63CFMOCaIyo1L8gr5R3mXyh9wTz4fS3v2zwkwdsjKwsCQAL80-P2GlkATvQrp359Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO_MOFZStfwDQtbX6228PXbhDbvvLaBcxc3rl5lpzxlknZJKzfod9ImM9kxcvv3jhuYU3-ZeFHTYxSe6l8H8RNuLPSrmee39IE1dbz9c4kbVAVOqP8wrQYt6tS1jCoifwEfvfi6NyVaur5QANiW_NIar21QbLqlbDYfg7o_HDZ0OlndHnJySh17Qa3TDDWAjtpFjwtTu2wGSTuKQFzyD8a5SO1VzcWufdHbVPGbdqlMPypdqEE0kLMIeJcrXWIZSBWSuStskn88wKCHnVJ8vC2LdBww81ewxOLSwuip1eW2JLtF0UnE5SzebJ78lfpRS6S43MF-UqxGR2jMxWuW21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EntIU7Hy4q8AtH6jIaQcMCowNTVoBzuVYxw_CTzxT3pP0qVQ7MER9Yt25E441Pv5rl-gB7tSmuyx2vLTbOemEWGYOAllVo7DOcjC7tLzifp6uivZYOCnVGLpmwzJ2Z3yVE12ZBbBeU0ASKqHvRntFdg8LvhHL_q4a50kB2Jx9Lxn9WvwW1jWIDkbjVKc8A41Vpu7Zkuf2dLW6TDKEh8uHn1JlxpYHeCrCYvzsrXo1DtIdR2pMuK5B_Ob7z8P1fUc7u0uuqgiOE085ukIIF9EcK2JblfA-4UwXwegZCTbYuUrKRJXEEfiD1L_hi8UGThGVXSrYCedr47C29h9fJ-Yeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjhxiQIWEB-HKkgSRe5-g-xh3ZXdwyQhhS-iQU1ja9ntYTE4PBl0biHWmuCLDCiOGcv_pJbTHUt3VU6PYRjyEge-Hf5nmKuYEFXyxFJ7OEEG-OV9DtYkkUrurj-TjTWXfquaRQpbKAVB9MjsBHD_uLDMHc9GtfPSstvJ9KTWq9AgeripxECSBKA2J4zgYt_f4zpHAj7Zle45VzhYwlArnW48BKO0YDJ5N9PvJfLmE6aPLXcEwdunjAJ8jwOnIusyzVlgOJoqEVv5l8nB9EDWxIDMQvPaDdg5J5v2PutDw2ULNl5z479gF4i4uE1n1FBHco0swWEXhKEXTuJhnRTIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiUlsuFZW0Y8ACYkJSLIuYpYmbAiLmlsov7D6kW4SSMOtI1dAVd6z_n-XJFxp-5rGHaciE5j1mOf3-_RqzfhmTCM2sVRV_O9UBWZqCEO7Ctus_GhR91EVTxm4uQxzGtEXJgoFV6uIew1F9gy54vvUk0-ZDsqlMcpf4L0zXsA5n2hgM-MlKPEhFR9AOkVDaHG3HnWcEHYTVMootk5qFa3zamr4xf30GJJnTJJKJPO5TLWVQDxgGODr0zvmtDs_pUcf-1Ft9y4OhGctnH4KQe-iCPgKukpKUhWFHQ7sKIyP1GXl4LGBUOwQzZjdxVTsxtAy05Ix4RtvfFHS1GKOvdkfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=V-eFKkSYPJ7xbIX5rv6_ZXrsDRUBiRKcSBpz7BHaHI39OZgLXSLcWPcs8Zafofo7zBFppPDteqZTzB0I0gqiH1F_Z5QeGocJe3WDQ_Vqx0dmPFgOlDyafMGKy5xypc0ZhbEz-xLLu8uBeWpXvowGWH6RsWZUna5uc8HPHJAYAibqHbqwO8NDRiDrs_M8C2LXCIoYiAq6fHXfL-EAwJhdmIp7jMwclgNhXanC90N3MBSoN00QpfngPQrnN22U-mSZfRDE42YNpHUyljHn_-LohmLXtWnd4zeNKq4QQaPCNTpXb8b7k55g-DItCGXYsYTKxjWIzNydoIOHC0FehYJWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=V-eFKkSYPJ7xbIX5rv6_ZXrsDRUBiRKcSBpz7BHaHI39OZgLXSLcWPcs8Zafofo7zBFppPDteqZTzB0I0gqiH1F_Z5QeGocJe3WDQ_Vqx0dmPFgOlDyafMGKy5xypc0ZhbEz-xLLu8uBeWpXvowGWH6RsWZUna5uc8HPHJAYAibqHbqwO8NDRiDrs_M8C2LXCIoYiAq6fHXfL-EAwJhdmIp7jMwclgNhXanC90N3MBSoN00QpfngPQrnN22U-mSZfRDE42YNpHUyljHn_-LohmLXtWnd4zeNKq4QQaPCNTpXb8b7k55g-DItCGXYsYTKxjWIzNydoIOHC0FehYJWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GORDeeYLSu9TCC86CTY9YHcZ0nQIhEFuSFbKalL2hyVG7Q7nzjJco97OA5tZuQRIV4V9v56cseDG8KRFbXrwImN_HE53G8Q6srAcdWh0MT_N4QxaF82VcrvYxce0FKBvcluPy4vKkPtDIL3UQ98EOGoQgsskr9lK0Q1PMXkN_aYPyqRjxg6bqqFCZT8zolTIcDOtl1PxC88N8j3hdasNeQqRHr3ybehoe8tcS48MrL_Cw-FmI-wJeLxMlAi_gmXZT2tIfgaKZZAgtlcH_v447WTLqvuaJWHJmEj9X7EP9fqU0p8kQD7P_Gk3H8amJ-ODuhqI5Wg-6FMlTN8CN1jJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZb-UwvfjKdANaVINsqhk8xYFsiqjOnVaI_SEQaNfyJnLZqGNbTwMk4CdB6w0cwQ3B2LfnHjMvGnpdZ9iqZP0_KfNP6QjLrFAAVcRzV3sJ3z7VY2ACcSRV9mPER5whROCLkn4ZsQpn0E94XzCVcyo5Am1Yww4gHniy8yhKDPJR9CRXAu4SGG4QP4eqmXqJbXM-O6Fx6NXY5X4X24Gshx1dR90tMsbfZj82pVEnzy4OFAq5o9oq08btke__utF5lZyYXbQMqDlW8INWsaQHSjv7HJIPa5zD6_Ia7VvftScC0aCuf1K6J0ltJk_bKwlpC4CIvwtZplyRylhdxd6kUEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqOetzOO7xgPvWF-P00ijEbU1ffWk3KNwQM9me-a-T2fMjy6ccSkV9TBkORN7V0kG8t9b5jkfY7bi6yI-Cyg3fmIwKJ53kW96r-vbiM5NdzcKdRxwo6kP_gYFTHwmzAKm-4WxxclIycdmjyEw21FYW0B6mQllSbIip32WMF3FMlDRpb_JRaMH6xBrXo52387Z99Vq7Fqb_eWmuSVs2T96ZZcVzilvQq7EIsWZHctFc8xDQqwPNuMQhDtcGjJAOEiLQyGdDEWRotCk-uuRhlpwFRfb4e0bN3LuD4DIEopu8nFWFWtkvHX--fwOtCdusJXZRgYmjK7YzKazbk3BOBGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=oRPw_EKt9mqs6OjUDWG_p5SaWecI3rVl-kkpJl7_AURqySxK-27eAhnryS-mlrCRI4ppAxhV4H2Kwr7dyiTHXahj3actH5UzOq0MVcwfDKKs942sJg86s4d4U0ZuPtSV1wfiqY9MY84EQqn9qRba6t6o1YDPPm3cqlhFRHqp2vBX7cLPvv9WmhRwVhoJ1vKLpT_9SHBtNWwZQJAIv_V6eN44FzbVwdmiSm9zoZVTrZYkfpF6F5cnRrgI4XmHhfd84IheGeQabHoRN8xPGyU69kIYC-jW5yA0ZdAP1H--gT4TF9PrR6eT35cuCBTqRm3zcvYrJVRnpVZQOnSvsKEnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=oRPw_EKt9mqs6OjUDWG_p5SaWecI3rVl-kkpJl7_AURqySxK-27eAhnryS-mlrCRI4ppAxhV4H2Kwr7dyiTHXahj3actH5UzOq0MVcwfDKKs942sJg86s4d4U0ZuPtSV1wfiqY9MY84EQqn9qRba6t6o1YDPPm3cqlhFRHqp2vBX7cLPvv9WmhRwVhoJ1vKLpT_9SHBtNWwZQJAIv_V6eN44FzbVwdmiSm9zoZVTrZYkfpF6F5cnRrgI4XmHhfd84IheGeQabHoRN8xPGyU69kIYC-jW5yA0ZdAP1H--gT4TF9PrR6eT35cuCBTqRm3zcvYrJVRnpVZQOnSvsKEnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1OQD63MYSUbSNf-yGN3QcR_Q2Aej_e4HSQ3vZzqTd61P-GVMxxYahzdedt2GxP5P75feqJTgB8uuhwD-7-aPg_Eh7Qo2cLjyuf91397DhdSHooa6_k7bXFnVMMa5mQxVlI5jZWDYx-XQ2HZJb_3oSpH_tZQsHbnaDgUcmtCDUejtBi9i-0B0qlV6wl8fb5hYxWPOizYjt9RL32r-MDXSrN-YoF7Di_axrviqJ7cwhKSTSDjTbGniAx06j1q_5uIQ-gjVWpuTS9WcBgA1kvigIvhyY_ERs8Ndg3y0gbISAloOlD8AuD9nyFo1YTuMLLhdatWSnkQkGkin8fclOYHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZQ0gCdci3AY_MN3-xnhDZIkd0s5Xasi9CpY5ydVVMFLwJmSya2FszexNY19nQfPqikz5vaHS69vCywsEax4scogbpviBMxbeIxWLKHXuqhnQ0nRZENs8PJKUEXIFQRY3so8OJpB7qKyOTwGHt7Qxe9WFSLbIjiodDP0osFEYm6ibcCiw0aJf9XNusgiqpCQjuRFicnXycckxGiOuJf8oMElMT6_MT651bjBW3ksDT_DqTOYR9m-XssiOpaeoDvF3NzfRZcVVV-Eh4K6vTwVIYm1SD9TQzC6KzrgxryjS7c9ND9bCJymE26qi4QPd61pWIJT4PHVdzYnBu9H3WnTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0Qj8SgLe2vvdgTNoV3XNQ9BaMfoaxODvPj26G_OHxhKvbNMEZ7657Io0LyTsMiRaW4DnxzeF0xzDrPBon6YWXtHOQoK0hEBn5H6umc8TCPFSh3nBZWbv2fiCpiTr9jTZ6o6tqnM-L1wAag2DFf4-KSVCO5QpfORx7t1L3L5PGppQXqjg_WnMROVGKzmod1Bs6q-Djn6ySSmlXSfcRGryIrMAXimXIulF6PmnHViInIegSTCSh4_BmGJ0tXDE2NfIa86W93oB7vsk3kogtIYgHEsBLLAzH9GscpJ5crhB5uh4GKKePMEUzIgpUCDtkyxc93C5s4e5ZoWChwjh0ngZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLlS3vgt-sTjxQxA5zrayAueQtO4GBRPju2HUN-bh0w_zKbV9stsIgiu8qCwGD6vL-h5x8tL7ziBxrdw_9FaqKUbSdxKydNpWQ99kaQbvVQ-fI6NRN7v9HGwzYpf9Tp1rN4swnLhf-1zD5VVXEon3GiwXCOAalMAOFiPZkQ45R34Lcsvd2EumkKHlmxAVugRcDQE9feF6Vu2TjhjcWsaOlgxDIw4A4tx5dqGhViumhDkEjzPgO0U40Zo1Ic-kfpuzhWYJEIl17gtqM5FQKDjcGbpC9odN5wYgHReYZK3O9TEyStSpP5Tm4tsc4j0K-r-Y1V2cUIlewQ_5FaL5YFZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1EA75wueNAtpnfMEj64duN3mcVI-Dn0iJO86typTBXAUNLA5MyIPUKph9Ta7J0AZATGrKuPHnYCVlLEFQ03ERIAjarin23EnOTT3NAreslxm-xsOX6BvipXwsgH6rHEQanGbUu6b51ja1kO8pjPWh1XR0RbfgIy_JWcUctcvu11WdXf9QJERuLiXxnwB-ZqL0Xeu-GvE26Dd68q4kmKEoFNttnhvYt_7h0s2WpOYVGMYzqEX0wh9Ybpzo-vWK-GDb0McNBLCocIwR5CU-vasF308vhRYZ-fjHqPyxIQuoJv5g7JECY_FkU8-EZ9egsJEhnJqLFxG9Q8_MnWc15rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-bpYplk-CuNU_Mw5cZZGdljps7mBUFZjfv4DMnJH9tUiB0F1lYg5Hdj7QGa6spGCqtANW5ohqLkulXyQ6Vu1eL5tHqxClzuGvHyheem075RJLWR7L8RpB-HBeuavyAJZ7MRFsmZuBHCGmSlzD78SwCk-eTmRyNqX2ipz-rHVyKMv0RsskCZOxxF2Wg4WTJFlhPQlfoirWlqCU_4bEDcJTg9pBnDNDTpd1FVDXjMaHrJJx_x6JGaUljTTGxEJT00sNAy9qzsbUGuWu3a9Gfqvt02qlb0UNR4p0uLZ_x50EZubm4YhK5SizEWFCUz31bM9nikv7nNhgHFLZAJewkxyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llGVMXLv-JWcrJixqibOPxWXyzi5PcKCItkqWsM0WVVdyEHVdLk5XGoGUh9crBUy1yGwsZab_8rhzPGiKl_7TmVWFdml9MI6XlAiWFGgTdFZnAJN_FjCc2sejIISQF6SsclXLnFL8V-4j7JbUhUE1tWlRikLmL4BxTPFK-YQ8uSvrlsA0EcLki9P2qHvLhATb2CsUTuzX9F7gtkBkr9he_GJGODrGYW9aG415S7rFXFyFvQTXElX7EJk_pVPJJiADLe_9-ptpu6v0AIMLKKu434Ov7hMl9zkNlBC5-DjEQeXc6vfzKONFywE-ib_LJjRGyRH3sOA3eTx_OGuYkHYtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=r8bZEGZCrOGHBCazh_SZ1TXtXYq9rwMSeMyWT0Iefbz5-zup1MCr5lshWz9IGCbB1NK1vgsBrwa4EIfQsc66PQ-E5HaK4ZH6eIQ0cfvnXpgXOoN6tgrWDS6aLAGJRyk0uoxBHYFEFajthhHxKql5MeEnBneFOowpGTSxjSaUcTVYhdOjSQcwTwrP87Jf2lkmjh6u8ZOaeeYyIWf9RK-cSeFJYqSQbyXOBeSIgsJNlLG2lRvDCLeVeE89XPLuM7n2eqWfp-Rr7U6y8XwwqD36JesIor9IpzUwk0YIbUo06LuZyH1D7JpFSO4i8UzCrByBihoXvDcUStS0ryYbvrUBuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=r8bZEGZCrOGHBCazh_SZ1TXtXYq9rwMSeMyWT0Iefbz5-zup1MCr5lshWz9IGCbB1NK1vgsBrwa4EIfQsc66PQ-E5HaK4ZH6eIQ0cfvnXpgXOoN6tgrWDS6aLAGJRyk0uoxBHYFEFajthhHxKql5MeEnBneFOowpGTSxjSaUcTVYhdOjSQcwTwrP87Jf2lkmjh6u8ZOaeeYyIWf9RK-cSeFJYqSQbyXOBeSIgsJNlLG2lRvDCLeVeE89XPLuM7n2eqWfp-Rr7U6y8XwwqD36JesIor9IpzUwk0YIbUo06LuZyH1D7JpFSO4i8UzCrByBihoXvDcUStS0ryYbvrUBuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIWSlVqwUACy6mJ9UotigFvsefgWE3kkTjyZEb1KC3Xts4o62ZuvJVToCFVLUWLIt8WVW6uL1VzS8_N2rvoCO4GaU7THDtCVnk3ds4U47yGJLI-4xsxi8-Toqrdp61MFLku2cUrvr6rPZNcrsbcnTpEdXz98eC-p4Krk-3mV--rjmiSRTnD01d4EaoRDIMnbF4Ph0bUeXt0vp6Sa21SxfPtkDC-v9YbvV3iAeGqQphADrAezU30Erow4akl8u0CNamePF0O19S7XAn5CKErwRylzupOhB7vBmW7fxhxW1nYU3rvs5opxp2H-Xf6hDD5uzXzUgR3HDU6wchbkguQN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzazor_L8nLEKRCCqZnNHgf-MwwRiApcjkKNMo-zAPOQfcKObwnH6QfsoI3SoddQQAyY2bcwRjrQ-73_rbD3kjIUgtM-7Qlj9nAmzBRaqpC8Q0AxsDWxhNCr9YrtmzzNBDCErB9NVqUG5pbUV0GyAp5f6aWGnLlJEAh_5nB3HcgS8TcTm8W121MhW_Y_BT6ARIFT6CZp2coRrqSHbddV6DDmkVItb7Lc134T-V_f69HfqE7MdqlodffT2WUYcKs4fLsO15yw8kwITK99oIpfSTQ1fcXPAbnkZUeFlZt1Uow4G8MIGwU0ma3yl7oXx16YOKDDm-s6_DBv67cnrMiGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_hAUTFktffiisg2t91dP26PA9u8K3mq83kXCu8atCXcevjdAFDIbeR8yO-EwkqNzYXtv9DdgtHkI9ZhFiFBHkfA_zEukRAuo_I2NHQfOletfrVmK8J9zXqkqMrUSwvVTdbfNS68IR49uWBXwNr0fBydnljhXFeyhMVbbYoHsbMrBY6xZdKVu5hPtyDbBKJNGtHt1ooBhNQE9cVuNMn1nize46_krpYh9D756Tfoh-Oh31K56z7GjMxuth6qB37dxJta-FykeHbEpmIJNjCFx3NjIANhY6XAy91yrVgvqEF6Kc91gT4txZF2RZVx0gcY6A6kJ5sGEndtixKoc5AU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAclgjNsK-x4ufokiX7YOXe273XVCPyRxy1nzbfTXCROAFdl8tL4VL2xEsldb_yHWy8kQJ4hS_7ZiP2j-DUVW4v2iIV53R9f6J9k8piFgakSMwmlN5aUmpLIo7CCHp5iWAB4st1Q6xh2YCesvoYgHaM18zjdFaNhT6uzVkWISHLmgrRYAmY5rbgVbbHj1M2p_fvynOleiN7TmXONYJCFa0W05ZaAgNCUkfxcXn09NSCOcC9ggcNcc_Jkt4kCkjQZBT4r6kinsu4NFnlTHVOqSXZCV9hLk-EQ-JMXf6TRzbCJzlwuNpEavEyU-ypS2K1ZGbM0rr8hAsYrNwS1mXnCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXVE84TsrKIpN2_-Yzy4R1TRO2UlKSCtyNfa-AbPYBXtl9cRAJ1De7xaDesIBuNeUOgNSzd_OeKP-QDv3RLa0i2E2dxp5xBu5lnkCk2mtzvZ5wIPxZIo01ah5V6luNCSy7kAeCBM46KW3tJrbWpQksdnfyYgjXMrPp9XhpinDg9TrD9EKVJQjsTrVjLQpajDQU3xew1oaJ4JFWf-uywtFYlyKO9I3bpBZkn4sc6EMhuG0F--pmaDWDL9j7Rp4_lC7a0bpB0bTE539ACeQjE4YELYuHWSJxVElDOZTgvG-6DzGQ6icqsgIGitspaSdNws4Wp1m35WAx3It2krHgYhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzjaUiZAAWQj5UTbjgfYnTlx_lFewD6eZuOQv3lX29a1LvdIqiXVBSAzr2hQGJXlGeifoemBe9z795Q8CFiWS0mNXpje0ycnvbsehlKtDLFlzJco7Lsdm6OOeXqoU8D_duYypRb8JqMWGQ4gHiKpeImVM31iRdFqDxOP1vjH6j1mnQWHbEl8EwXIyBglqZd6k9zp3KOCrgCpfToo6h_jbs9tDkNBnJvzcCfQJQWJAhpWkn8IPIk156KWzMkTVBWeZr4Lj3K6LeAkQyDKCWSglNNZw0qkqf0_af2ESvfeNoWsWN2UX5swO7WeUpGjpHplPpvtDkWZ524IS1xVVz2zTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnau80l8BsExY_JpiNUGj0fzwNFawi47_EbIZn9C0H6XwhgwDC69vlf9Awhr-oEw6LWDhAaiE1raxOR-e3TG0Mj-Oh-XyDOPl4iH8pkMzWP6Bg3OTyDzQICJkrGK0teNAvh_jkFiaZpMsLwKfQ9uiulf-q6u3AbBslPlXXxGbhmx8EzQEUB2ioiWCqiiTht812Vn8vBZ7tq0x--L-l1E-gx1YKz8wT1IoUanyiyxWnOrLA7oUx6uicBEIpsO3Wy8EUdIBaAyvMofNXPS9Pzlal1KiB5-5nkSaPgBFAHfTrGAc6n6OGrQSOSVdy-KmDLIFXIOgl2DTXRWHXJfpaKpRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkmM88pjYkmAi8mWu2pSfUeKxzZYA8eiTTRcN8DCLVnzpRD4z7Yz2wsSH6o1KOE5vujON2qyg3adRjrOdK8gOdIXTjSgQB8FIJbiXflMvI0B7FvP7rsHqV6-4HZ_p0er4oI61KFcOBU8RMfIHHG2mMCDhx8-DbWk8b7WqWNa-H2zbwSwA4184l-QdlJOYA0tkNi-Wj2DFPFZvOqV_aCbrJ07s31JMduOvyrAZjlTwQACmw5oDHuOzd8lbtt5XEnb4LfX5cnBcgu0OtuUNJQPmdZPOf9mHCaWyN9AwktQ8ECH_MvTda1-aePgCZe9vcmQ6bg8N7COFcPlt8LNd5_CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnyAUlr7lD7U1pCceeHsp5-gn-BBxvF-_IaqadTu8I-rDKDdP0UguWiI6KtvYDZP2jOAJKvwTqKgi_O55l0roI2Iby-YojkQlpuC9qPqoutL_GZrU6nPfSIKF1MCmFfEvg6iHW61UuNktDwRay9zt9NzSFtqhyprfNhm-vUYyLMGvPfm108Mg3u5038p7P7JT3qlfuToUs6Z_zaBCuOlZMt-OKGd4KHPt2-QlVkuVCwShb1KKO9DVKonmfXi12G_PJKIxutqZ8wFkvw-omDhHK4SEnzPdeTb0moq1Rc4vrxn85qG55riSBFrH4NaSjuDWnFAqFljCUz_WsXWWCjjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=ly8th2zG0IjM2SBVC3ez_3UFyxGAe-VxHv7H27LkaLLbA0hCxWl5JeAJPYs-ROpQ5vZ79LVMmqTtXx6JbRtyGu9sOiscbn2qTBEiLtq1eXv9AA2Eyx8iLL44szfRqgKA6KTEVSvJrutLpSF0MnHPoKjoIYsQob2ngMUi2u0ooSvdEsSPqeS3I9ZaIb-JxuSG1i7ns18uA9Vxtypa47AE5DDKU05VYUVyqvT0Qq460gdFWGnqPxenLO50cGDKN9DwsHnBZVZlYiR6wpIB0uVjkO81Y7wn2c8nHEgrEWkAVtPLwAzFlXRUxUlHsPPpfiJV7-KBK_HjlkC4xZco49LYWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=ly8th2zG0IjM2SBVC3ez_3UFyxGAe-VxHv7H27LkaLLbA0hCxWl5JeAJPYs-ROpQ5vZ79LVMmqTtXx6JbRtyGu9sOiscbn2qTBEiLtq1eXv9AA2Eyx8iLL44szfRqgKA6KTEVSvJrutLpSF0MnHPoKjoIYsQob2ngMUi2u0ooSvdEsSPqeS3I9ZaIb-JxuSG1i7ns18uA9Vxtypa47AE5DDKU05VYUVyqvT0Qq460gdFWGnqPxenLO50cGDKN9DwsHnBZVZlYiR6wpIB0uVjkO81Y7wn2c8nHEgrEWkAVtPLwAzFlXRUxUlHsPPpfiJV7-KBK_HjlkC4xZco49LYWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5lJBnApZK0y-YhYcp07WzXMkn988138uB6Cuqk0-2KZpxOCO6GSGduLknqsr3MJBEU-H2RIM9vzqQKry8FWfOLggEKW_fYvrcVgBjaRlzTtT53H5l2HXlv09PoacNB68plALD02anwUhXjFr4FKv_QDs2QpnXS7EXlV2wUyOTvUCEdC6yD9gMSINcRXpR1iSIeBWNEG270gKrT-gxGImWp4WfBu9krQve1P_L7MsreVCtQybtq_peJrPulDKS7v9uCK0OD64uNRE9yOY-j0RQ9IgPupwCb0OJu5TqY6sl5jfPyy2SEnBpF-4tNk52-dZJ-uYivEwW-ImcOHxs32TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtP4U5fEfgh_p3QZh9OvjsuA1-9lqplxUUbI8DG9tMZsuayD46l5_uczutUhOIArYkEVX5m-GUwxFrUJWOyhicL2_Z0AL8uFhWLYO4fnqi6zxGkAIsN43wXxy-8Q79ZtelX5E7oudUTx-id7FTXZ1BGMbA3hSzIDshFtaM-lnJqamQcir70FLFSa_nYV8GtyRmt1cLq__CXGCvs8Z_NL5nOZc5rbhGLUSO6xU_wrVoF44eqt6dANFwJs9VS8agnOr2ajJXUkoDZMgPkmryICiKExepMOKbvFH6j_TYnIVRfOk0n9cTIRh12rhdtfnqpvwP0ztm7b3EOlTNDSd3Xxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV6q0VcOOlXytlqKMfTeYEMOf_Rn3SP8hbzU21TmjrUIlYwD95uDUqFyjsdIR86wLDzmPF4ZTC3aUVYVU_6e8CyWAle291XCM7Zj2ZKpLYVdRnsStuaAl1TdlZeiOXn1UrUotmvxDnmxkt5r7h2_SqybLpcfIJI1MXiGLepsCAhvoX9Q2vyqg9UygXMB3WrUPsstdCewLxTp1Xgsr1CRUR9TsixybA5OJfNJ7pb5yBBufvlpzugBAWBeBeOpBtpDWuYW7onQE3JfGnwULxV2bwV6DJhxdy10gyLoX-MUtxASLCrNhgUAAAU9okbPJmQsnIxVR6Aaij3WwON0I_1H9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbtI9_jo8pN5OuDt9G8ggTHSGYXOubOOp-gszv8n7nBXWfx_hoa0m7qskqBkpD86Ks6x94yDNm3bND3R9lawI_80yK6yxQ6x2T3-pkmmEZPaLpEUA-sXiMq0daiA47DAQdP_iw93E6HaFIWSk2IlToqboTDAAwxhj9UH3DqtnodVQw_XXmohknwrDwEY2ipEyywswYU377YkwcggUjT48ySlJ16eLcHpbjUCt_Dw_AzxYP0atpu_0-hUhYy3Zazs0SaCcvZqwiZpahykcGMgCAl29wyIqxvSBuKkQHomD02TVhhWjlIx_VbxShJIeUIm7_C4ddVP2cgU9EwFZqV5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDMjhBNtZ2EIRyWf_SLQDHiZT08fh9QjMPLH6hAK7x_8If5pCxDA4Z_UcVrF1_wDuVs3x3sET9o3xH88gQ2KYGiE7zsYC9C5kiOxGgTtVvZYismsJefxvNMlvzuOgxfYdceeVcraEsgNdapYdeMAfWKfb7_kKoWPfCNVItvPngFblU0oH81Tfim7eBJRdOAitoIEjMt_-jjwoR-yL1kDuxYvtpjT2pXjSvh1teTUnznUXwyjvT7PLtfEogukLrTaQ5hLja9C31A_F5nt7bATLVwJJGsaBT0guzvPgu3uOTIszbwWRdQPPA3St36XPSDDBZiJNcnjkZrACjaLrwzpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIU4YHzmdmcnmi-VtaRAhfD3gZHNzRnsN1HdHU2KGIOMXzSXEhTM3fasc1MUP1vnYMHbX3ZiPosQiHjUL7MRfQQVTeZFQWv9jWea1Qb9Zf2cgN_NWz9APCQ3WX4g9DqvojkZGKi65kGmdjG1PvaIpIr0qn9zFAh1l2CWyCDuuE61wuqhfs4YzX-LdXunIwpiYzMnCz59hiAq7BNTqh1_3FkJlWffVwBgXogVbSCdO__S15QSIGcwxHONtV_ppV9Xx7aClv15CytAxo9GgF_Rpsoh8EUyWH02AG2JIhdji2sml4BM-W5LenDXrSH_ZMwzzllDirNxOv9RSoDzBS2otw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwg48mmQyWBupLwHoWcpDw-u9EvnUWPmXzG6XQU488kJob3I1oVHG1z4BdD3rnHJ3kGvRQDwonYRiLbivxTq7NuTu3XyospMnrKBqhceqvpTuIQG-l9rtmPG2f4rccQbglhpPyg2iuPVTx0LdIK69KVf03zTpVUNlsXc7WaCxp0dCeiZc5Ti3vu8pxRUJ5dHaq2Vzf482QEtl_24CHxglja4h3ffazV0bgaMgu8H0dhOUoimfM-43sPxTgERZbgp2HsqEmwgaW6qOllqWEHgS-QttSiGFHp2FCqIhF9JU0u2GdQrHtKqsHse1TdlGMWDUyn9Q29BzZJj4VEwjeSxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdHyLgGdJp0RQW59GcbJMcnt5VmGb5IS8f68VLw7NY3M46G1i1kL4jxAFx5I9uMOc7anD-MrvUN6M-Twvb2_ZNSwZdWuX0ixab80psMHCv4W9McwCgvKwH7y4JarxFlEWerm72guR2lvV4xjdDOvZpsm7i6BSol38h03HYcB84jgSI9QbUxdmwaap5TVL94wEwA6F_mLpM0byiXoZ_KzyDicEngKTndKYKidkdcY8Ig_7eQkyZqZBBLCywaLTXwETOrN_mrgL6IBnC-A2Qt9ApclfeGm4M3IpxcpQY-fjV9qeKK_Z3LNL2ZwU_oipW7-1GW6jVsUCEVbZLAK1OkRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6XAWg5bqciRpJMyNmd6kylEArmwqjUX1X7_ddX6J59s61qLu5wFSgUcuwoBEkCFE1TGjI-_ucjB5Cqjca0dc9-HAarwpVvqVdKjIh4Ukk7zpy8WK6HzmQcDtuoUCyyLhU0i6SAFBSDrrdCdx-M4MQ3igT3yyzJ2CdW2SNKnRIL-ygS7YXCovS5XFZ8IYWfAH9fwEA3kzDcx9cssJ1lgFI5vpXmhXbnHoBaMBAAvReg5RyVugag-eFIi47KHd5W1XO_7a3SCTThhF2pdxOkHPQ_4C5DFEecR6knyW0C-YIvjXOsORgMK6xPHQolFhVgicphNuh7BZ9MxCQAbajVifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSR1LeHrLRDqPjvIdGWgJClBcACJ399hCSQMAjkO7PgJJPr5UUSwH7szy6AFSUGD2EkE0EgqXauMb6m1a1Ve5bVEkTxm1zG-2fApezqc6LBmCdmz8Cu8h9p3A_7AB6Y0J9wHJcuGvy8C-1kFQ7ex2Oxck_ZrOk-LO_KAE1bK4PU4XV59M6EoDutcIf3z3HQ8lydIvx5qKXyIoVSdFfjT-QDM6RejLWtn7ByXwH_x8gG5kJKDqeI7nUQg4H29NW2hPHxquJPqjxCPVEyh4YyoSAQxdhyDX_-imIJTmMWcVNB1GtEwSH5mga7og20fbWF7ADwiI5EnES08_ZnC1qRS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkpZpbWI9UEdtix_xH6nOVK3A4N5hG2ee8S4vlvexPHVx_8cRuc8xd6X9uJaXHDSitHnc27t3_4nKFskSZP25sVii4R7W4rlkeMD-dlKu8tEXWagsbJv5njO7quxs4AWjnnjsWOfD5NE-OjFSEi3Zq8MgZotFykmwO-YUEsm5SNEV1V-vK60WefZo_Nd_NiUbkzKCzXF9ysaHFqPDQwTcesSiQlDymw5Azb4jUbfxMrG9dKdDpDTc4aPEsfiOXFWRSxtmyM2jrDScpRrmBBD6LhGH9Oa8I0ql-ICQPAA2ZPW9zhf_diK-bB9woWVfWhShj9aW0dwDtvNXcGGNKTjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRPrbdwkEWs4XaNZa91a_RU7yjM9H2vB5DCom0Wi2CTOHlQC4ley0FKl27jFl0wt0RwwbxUAHqI-amYlbn3PGCILDnc8ldIRJnS8BKx6ioOpgEe_7E-1HekESyt9VHWGInROiFIiBFRNSekMA1znsGk9DKGtmPnajH23Yqs114BMgYudA2_tKy6wyb4LyGVNdisqjnsFv0Fq2RtPCt0fPHaB-FoC0xWriCXaI9_0_KIn1lOFP-CQNLrQevOcQSCtZFt1iv2HM7E7-lsbLBF0tCw3vvJ3aRrQ1TyksAHI0tQBuGj0hclnTb0TntVCd13VK1wRJkEXplpMC6ssmMoSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk8a99abXFBvGDgKlKnILHN4yCyn482AgFmdn6OdhDOeZafJguhDMuFM-5DJ03S28e8ATtaP-gxhICXi8yje4mTIrQvTSqjVI_ALQZykqggvankI3TITCKS4FCiIjMWd1rZ8FyduDpDmEFyEAYpvuAiVBj4ZdFtU4I7Vn7gu52-p6tCnZMh5GhHu5CIdiHuieJxkawoSwW765YdURjiRSHguOA7KtisIeVRk02mvi2XxOtOiMHt1kpqhnySCGMdVr0EnYJUbycci3TX5UPywrBa9X4syqi30g-uD7T5qtokq3Y7YGSFnCRxLM0Fvspy96nc7OgzANUPMDkOt0uYYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDHBRyMgjKKJhI23TM1PN6vjqzyQTAt5qf3C4kBKyRHLGqBCwgvZCoEjJqS7YTXqmqBpoAxaz326s8wj9cyC93S7cLEUB5U1v5ebtCzdd6HNfjAtbS1B6si03vfbZ6F_fify49EIUI1C58nryIppa6MwuMn0s1GQVwZiRnJ4cE7WnPyglF5yhnv1H5aYBVrHdmcU3MHC8Z-BD5Jx_Aq9dXJMvhz90c6zSVr6R52JOpnum8JkGvFsKrOtJUepJuTVFp4VB3C7hHeGhSIYgHyngDdNQnvBIY08DCquIvmMH0zmc_8aQekuhivxnwQaRt-nF--dNA9OF8bvJkd--TlFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=A3e3erBuTZimxp3Jq4gq7Y_0jl5crYmgHf7W9Jfat6Q0gPLeuyKS7DZ94crN_X6B2fSrjOeOUawLb13xmB4Cnz4m7c96CkAEpfbpPq5ResfRgkdiLY3xxLbaFcB3oY64i-BJpugMCDa4iRzhn-m85tUhkSNMrqtToYHGWaJojWaN4QGrcBcWHdXPsP4-3khd0W97qZ0Rx41bCeuMe1JgImkgolQmu1263X-9N9KTd37ln1Aq-OUsAIDv1vBzc_-nafryn0JN9sJ5MNd6986JNjOvIZGXPc95qxy3kkFPYp_OswEOhiZKfKyz_zxMztG71z5D9CIYHGhO3b7gRdd4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=A3e3erBuTZimxp3Jq4gq7Y_0jl5crYmgHf7W9Jfat6Q0gPLeuyKS7DZ94crN_X6B2fSrjOeOUawLb13xmB4Cnz4m7c96CkAEpfbpPq5ResfRgkdiLY3xxLbaFcB3oY64i-BJpugMCDa4iRzhn-m85tUhkSNMrqtToYHGWaJojWaN4QGrcBcWHdXPsP4-3khd0W97qZ0Rx41bCeuMe1JgImkgolQmu1263X-9N9KTd37ln1Aq-OUsAIDv1vBzc_-nafryn0JN9sJ5MNd6986JNjOvIZGXPc95qxy3kkFPYp_OswEOhiZKfKyz_zxMztG71z5D9CIYHGhO3b7gRdd4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/MdT9D4oJ73_kQfR4OB_k5w5w1-UXrUU5vVlPd90Nu5jMsU8_JMrwygsJltwi3wmCDXvrCOSQNaohUACp5PhxZgkqCxV4aKOU8QpIu9ybQiE1R_ZxMaABpdOOP8QhepXaZQHfl19b3GvGnrZHK_ubkNXHbo7G6Yqs-UJSoemykHgfdjvX0e-AVmF8MSR_axmddeMI7N4cH4vnSVPMYYcjY-lnEeuAkwlJv8K3s1DI382QOGLVr7S43zkS8EYGXammy7vmdS7ui-M4yYryagL-fjkfYK0d09oQpF3N15rzhO3Tqy1vr9WQK4X-DRifDoZdmfAv5oeYh3ojQ_AOQHZgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYjx2kv1cbFUWp_Kciuf7PdiqR0ZEC0LAEXswdLfthw1yw5lvJ1OdJnvuKCuDAj4fsCuiO6T2k8LXCCcvisWNUizWdZPzBLnqkbT-6YwStMtDFLjerpJ22XZlJQnMBmz0O8pzpp5dSmskPAkuq4KHzFgEDCM2gWdmUa5eTXJb_lz8J7G4Jm78yTQSwbpMoxW0-rmCczW_wneVn4_HVNLgyfGCtRT62yaGIHi4J0G3ZpJPgTJinfpGKpZN7tyOJ-4MDZsA9mM-Ppa3CesTLJP_ZcvAdmGGyJKXDYzo7thq3k1bjuSLM2ul__nZ9Ovghk4d2y9kOMitVsm2mDpZMhe-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIOKcUMkq25O3XJ6fnucmsXZy769KfdjGKpOGw18AcxMG8MQlFnP6YYYC5IAO3VOovGScaZRf7NcoQkZfcs_NcwaFPFKF7HeUHu7VWQMYMD0axQez5B4kPXMkPBL65ffIxNqBO4cp2CGlF0dPekL1LOWO3xG5ClgFSqZLP8hwRNdXDfeFAhe8chWImMWqw-QJIBgT0zO8C5yBfkrLg300JEdOaUutVkYISCILdkeunNu4D6CDtX-1PZmVg3a_Ah2yrwcWPWnd6_bn3Q1_WzpGQo9FsbDjduq1MkXg-0vgTzo_FpTC0K-Eia5FEbrZn0f-oR72CGcQNhqf4qP8-EXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxyP4vByidiKiKwSw5K7Bc1PX6EUNXNPbQToVXdMbKO0JEVqQpWcEhaTZ3bn7-YkXW6U700pgd6RANX3_Efxb-9wqZTzu2W6W5nJq4WJXQoSpjTgLBbHzogLtPRv2G4Yy5J_xWImWO8XOvq731DwbxMnmSD2ofj03GOUvzHf2YMeo-yB4YIfkFwpXcCanwt45FEbj8onoYUFDcQ-Mzl85dSzDt-qTc-ZTc61HU46ZVLW9tufOD_3Df3Hfyd2sssYpMUkim0OUrN0erbTRRSEEFwyrmZ8pfGbNiyWP6Dkvqf-HU00mr3KytJXQtGtq_QFV9hjaI0REOS1daBnUujInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTwvZU7qqJZordGvbL3BJZz3E_qK3NBjukt2VWeB19h926kSUhXVRcerYy3Cw2mOFnfntn25AX4UETg4zzjV9tK9iMpBQml8YYGv5hk1-PWTIxZVB4YxCm0ecMD_RqOpDk_tUVdn4PI4g-MYoOKqvTlo7IsJZuOSbYf2kw4Jv2bB-AFiUvNsLfiIO0Kx6cQaXYBAwNVC4aLXz54DCrZg2B5uWCcJevU0MPezubjTjU2C3dJ36yuvFBLYojF_PzX1vjRErNdLPwGscRP08kmzgaXYtraIwvT9ip3NoI-c_UqHhVDP29eoIFhkc9Fvok4yEoZZH8sDA_6DNNuWScAybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT7I6AnzIwdZnTevfCuZz_K7EK8WZ-GtdnT-l37nEVHGjwHD4rkGEIV3Yi_I8rxVt_HDrHOg8hN95pRq5J47jHbk9NRKKS8km1QKNIR2dkmMeBGhsO8gfE3ohzeexyV6PhhF1RlKYXBl48GmuLMv880HUp4l6rPUbDmhHLt1-QvOZbYYdsLLgr9FCtNJLOv6s8YSLP0wbUnmO7GSYBm0Jef6DJGY8iglHy6FHIRRYWBJp7VqXcOBC7IpVlzlZ9CDfXEZYQOobxbd2jSzGAbAM9zbMrciBZS9hzotgS7u2obP1m9Xe3srgxWAwHOgrwHgXtFeumtWcwJhoZnnGa0N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جنریت رایگان تصویر با مدل جدید GPT 2.5 SUNBURST!
بچه‌ها پلتفرم Weavy داره کردیت روزانه میده و می‌تونید جدیدترین مدل‌های تصویرساز مثل GPT 2.5 و حتی ابزارهای تاپی مثل Topaz و Magnific رو رایگان تست کنید.
✨
ویژگی‌های کلیدی:
🔺
کردیت رایگان روزانه:
فقط با اولین لاگین ۱۵۰ کردیت هدیه میده.
🔺
مصرف اقتصادی:
هر جنریت با GPT 2 فقط ۱ کردیت و با کیفیت بالای GPT 2.5 فقط ۳ کردیت کم می‌کنه.
🔺
محیط نود‌بیس:
دستتون برای تنظیمات دقیق پرامپت، رفرنس و تغییر کیفیت کاملاً بازه.
🔺
ابزارهای پیشرفته:
به ابزارهای محبوبی مثل Magnific و Topaz هم داخل محیط کار دسترسی دارید.
💡
نکته:
وارد سایت بشید، یک نود از مسیر image models -> edit image -> gpt 2.5 اضافه کنید، پرامپت یا عکس رفرنس رو بهش وصل کنید و ران بگیرید!
🔗
لینک ورود به پلتفرم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOehh584hS_0qiqrubWY80G9z2IqKbPxIKzP_iMk6pl1Ev46_i9I58EaYhJnBVhJhjt1Ge0U9WVAXcx5RDsd_peJgb0XOsnGoA0ssiRVO6uqyRgJw6RLe1QphSeGTUsnXGdbjDfK2_xQIlkSW9kLgP3_qfCGf5NT3I3LYEcYk3XGSBO2-i3UOxtLm7NRVQ7uJ9mfeU5ToWusQsTrTviwebrK3Nu9bu3QtXNib6ytcoWxh67kxAzGuwvKgmXA-PjqENIiGDfi36prIVs8pXEIBju06ne8_79qYxMktH9i4cC6Ia-2Wh6b5ryc28VYoyZ8DzVYvva2-TpczpkjFagp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
