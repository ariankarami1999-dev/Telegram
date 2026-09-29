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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 03:20:11</div>
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
<div class="tg-footer">👁️ 877 · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLvOz1C0VgEuxJV9SPtjqsGh3rawY6wS-GU1M3jPesur_qopvXzXlwiS0M1gEOQN0R1qG7xF6AKGOHYDZR5-5jTvE0-VtiEKNZSKZs29vqM1H4DPGWGTwanyahVoPJUiGzLK80P5RXiTIkvEX_MlcZdEkzEJMhl6nz-s5QGriqaJqShn06_tD0RUoRiyPKDI2SRCQHTLzuW1i22sYHMU9hGeMNBzh-mphWnHjR_mj0lbyUSmHy_R2P3sbw6nCYdzDqU46bwa4-d7W9_vJW11QGVsCN91bddwn99FfeGtSbmIT1m3al2_dt2H8QwzOUcL1caKa35GbMPqlOjks_hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pma6c4OM071HFnMvRffPumAf22sZMI6TYBKEidgO5pnCSa1Gqnw8KRFN9xF2zPSB2D6EfHex2jaoEKkLqT8QWYRQW-K0Tmj9znBiXrkJyrQjL_ZpvIHsTOLct9dTZbg6-0mMV2KWhXSu-qWsrTiu6aJv3QypHlEeIIXNFWDgx4L8_Vd3ugXoFKOMbgSP97hsUfWeJCA6woGzKEYuZmutr6Z0jut6ShyIT0FMtvJ7IbE00zxgEYPEYBfIywpJE2QMPaubS3PvJD_c2PogUrzmwufhG7qWi9Y7SUMM586EzJkc3YHW1XWi75QmbfKeQ4uxpKOTh64P9paoD8HH0FDw7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtD_7DIkoNay8pjvmO51XF8CSDllIkG_O1F1399O1z8Pw3SLGa64zpfrhgpOi2oDTIMNT6QgFxu2aqdbUUO53Zliq8EshgSk8-e2SlVu7hTj0V0-Lcuxjy9QGa9ZtSVRf7Ui-KhXnWXY1ucqlD8X1HVdV2ASw9cHRNGpPDv3dbBbdeVS5Y1uYwjUZ0xb8gg9BKlBpp98Bmm4pbLQEelkog59EwH2iDlLjJWBs6_pTP6EWCL_Ck4eAWhDXtZmQ4E_1vsvs9Z7TGfy4yDkz6BEpBrnW62YYWv2l2RU2-3ErDCL_zwfXzCQ_guyukY7KjhqiWN79eOVPtESQYyr6G5GDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtf4d8Ptp66iZGjNT4o9H-sD0vlQZA0oVxA2raRYmbDvUwWMfnk2c1OzVBeUGwOYnVkvtbVjA5Gsmy7kjgcTr8H4_84HubtKcWcqjdRBxi63PJlE5Eh43qOe5B8gNSGK_a1Z5CFgzyo8t8Evk0MhV5EIBQKhGvQQ5S9J6zHCEHAE2k9XWYYqHTtz0LZ3PLJwkBkXswvP4MkYROeYCSAf1qbLDu70PrrOKWggplcy39iQqa-CEZDiygM8zfEU0WA5Jy4JNoz0ccZUZB5L9la4tKbopworAipAkN2o4eS5nXk1FeDyybso6CdvZhiCFwnHNia6AOWHLUsszIhJuCuqrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fz_1n9LtqFArdv9mFrGaE1RZS2F3JSjwUNjYw-40FrcTnsgGGpnM5AkmCInfTzUKQbFMXhOWq7yLmytuH18jSLo-kg4W_JAh5UO3o5fZlV9K7LEn86eoa8MHj4Y_5LMkP6S6LcMFWZ8eh76R7snekMo0dOu5c93jr-kXG0PIRvQMBgqY1IFXk4RagB6jR8rgsWDDZnaTx0lGePKlauvFZUbufsRHMb7zIl3uS_6KRF99O5cAtO7MatloaQQ6yJhrHwg1rg8zVQ09SgJks2nKshr78eN9OGXiLj48lkJ1FOgJg3oJxoa3C4UdZtIFmVJcOfZYc4Nxno55cbL41bUABQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=fz_1n9LtqFArdv9mFrGaE1RZS2F3JSjwUNjYw-40FrcTnsgGGpnM5AkmCInfTzUKQbFMXhOWq7yLmytuH18jSLo-kg4W_JAh5UO3o5fZlV9K7LEn86eoa8MHj4Y_5LMkP6S6LcMFWZ8eh76R7snekMo0dOu5c93jr-kXG0PIRvQMBgqY1IFXk4RagB6jR8rgsWDDZnaTx0lGePKlauvFZUbufsRHMb7zIl3uS_6KRF99O5cAtO7MatloaQQ6yJhrHwg1rg8zVQ09SgJks2nKshr78eN9OGXiLj48lkJ1FOgJg3oJxoa3C4UdZtIFmVJcOfZYc4Nxno55cbL41bUABQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbWgMF3T2W4oO-96Q4Px8wHCt_QUrKFi5oBqv4c6X6cRGg_VT-YcTMu6szujxOVUH0S6talwmLNLpZ6vo6DMsZU7JhVE2YK4acKD6H6s-_uPWCEFb7laiUQVz6-mbkESsD450apk46mT1dXY0jeKGq_dfo_O_JW8Yiuo9PxTao-YeDuolzx9lkvemHq62CqpMPWuDd12nLxV7zsnmhYbC5t3_L5wqXezqXx0dhExPfgpzh_WrnXnVPoQpii_a8Yjb6shmnO1Ymzom1qYDUyrdVdTgAM35u_CWhLt5BiTnuaK_zmBAU7FHEPoUFnx1B6ZnEieWxQnbwQ44hA6X-ElXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9EhAsFXyhppo6XXpEHTIx5Hvelsfi1KhESWD15a2rE7X6tI-oBVeJCQsP7ElKPrZxG0B8Aj4X4LP0NMcWwm8ntGEoOXzvh3kXnqW8UY-0faUJCtP2kziVgK6Ngt5pq4o5BQJjE4HpKyv-nV19UM1f6yb6XmqlwYOE_K0dhzrwr-B7l4-DDK4OZTAVv1DH6B0UUHGVPGTAtJltr3wbXAuQYWSRcr11OIoYwkBd0GcS5Nn5DrGQ-ZKfRU5Zh-b0pcQmG7rbqSZEGq8ETq2VYC2Uyi0-qSckqnUbIzGlMpwieg6NUiTpgRAZIb98PRyoqYMbgqKEaZiMAvMZCKJe8pig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUulTMqtU9e__4QJ3c241_-l3sjWsEDoENt2Tind1vJhX_3NyRtwgduwrf2AHbWBhhW9pgBZo1vXUkUSz4cTP1TWYObZhccQa0iK0HlgKR8ZCGai6874BH2SZmieKx5-uscyJ3Vj_UwryALsUwsjP9Hj8LoLPyUtAW78MiLUfvkWe3ChwO1dCcqSKC45F0rH5ONOlpfNzSNtiIy5UWVX7JkGvBw6KsuZVwAfL_khpL5V8Hdu-K89mVqA2XTMDAEkNHt2lVMRDBJu6fqdMyWO82iBzjMsyzJm-T8Dpis8nZV5oZXBe3btwndYKtnizdKb84N0uz4FRGr5pJPFUjPivw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-xyvDZFt3ULJrrEanAQMfLVVJQ_1TiIQ__5FHv5AZEXxrNZr6tqWfhzTuLDjAqtqI8lwheceDQqlYAB977nRPdcvwAHTS9Nb0b4w3kOOBeSzXoxJ5kCsZo66ta2jHYsZb2RP2Mt1pEHzokBnWK_NWmcY1LNNGa9z5Cop9g2frX5UNnjnMvLV7ATR8bGYqHmo9u7ytl-XcimENcJcN2C2A2tiue-F1zXAZfcXj597WG8deIpFGYEazx-oCT4k9azJfhouK-qh91Bum42Td4BmYpLeIlayL2BS2rYsXFk9x6sseX9JYq_mM5lgvfi2PHYVsXkMNbY9KiiZJ-KTcfcKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX7UjhrhQ-9wmtgEc8W9fvTRM0LpOf7iYrTdd4HAfhknJieAIzTcWdLJj-Q6o5QXW_3_ij_hk_6Xvy_RIgyxNw5ul-d6Hk7DkPTY-x4jqu7-X297_XFVj41hA0h-05DIMq1sr8WFXVhhTntqoZn0jzop6eW_yQBONCyAmi8ajDvG2SHvQA07ZkcHQiPCtEfd5Dk0zLNs3yE-jQiy1VdASeqE0S6Np5kPufR4mtHAg1C7OZ5YoGtSG9TcQUqMHOAaco5firHHm-WcKWFpdpu7kdBkUG5L3GnPwIzNGP_8PshjlYKKQjhaJFpeKudVEsx9ZhMls0D-N0taEfmw_GhaBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qozNiJCje26pk1qCa4c8QJ0KvzakNKyXYSyuEyLMe-I1vK4Sx52XLI5uBV3AlIBgjFxeNITTS11SDyYVHWE4ZKhTbcP1ZK4KSb7bVsMKaw-poK-xw2fyjGekozlHkvKNrh-sm8Yle3VnrFI8udHXhMB_bSyMyim09f7h4wS7K2tvbYGMMn3isBi8np2Qjy9wIGIh-gAqPqNg48BySd5nA5FNZXjPhPmEuDvpY7tDn7Px25-9c7mVhB2XoOlZo9ch-QAWYQwukoMQtj0zRUDjj6XsteRPjIgXGNhqfAralPRGm920fyCbUroSYse21xYB0cStceM6ZYrb_kj4-jM6Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBpRCNeJH6yjAi5lwwf5XXnluGhjNpZroShmSDeDjTw_U-AXNL6C6i-SJki7KhftAlIEi6oPBPGLzhA2OV_G_q1mPBR7XAQWox3CYi4zlHsWAZmR1U2m2vOkxHoyE5MIkK7xHwWxLGq9hSIFjUcyYAtv14A5brKdQ6cdXdu5gWm9sMj2BLUaOKSit2S5Q1lrpkFBOc2X0n3BphRpKXNiRD3GTtOvFQ1waHZJj1UmyqLjPC5PNv9wCmmqC7ldJZTnSiZ4NPINgp8nfS4y1UayJxwV8MYNOX7ecJK9ion_e3q137dUADdZZZ2Fh5uAdQU6VeZ2f_OwI5kjf__MkWc2Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_z1iXqTJb6nTp1xoH0PRvsT7tkr8SbnJ6QuL03r3Bxgbkn6KwRtNYCql9pZDi_C5QaqVWg6XNLY1E0cWXjB97dNED2It57BPL5c7-cu_BV43S5ztSiKZLkClu8b1nj-H_lvSREsTzO91JbC4KmWRjokZv_YpW4DwHspLn7DxWyVsSQM82gcMYTaHjN_IuB_UAESobiFQ7dDj7hiahk63T-rQwPb8jwTjttxvf51csk7KECgSlxfh1WfZwUH9gEaela_oOKJL0ShgH2fE42G0wWg5ywldYGXPIH2Je1_APA6Uq_VylCe0YX35_6H6Sqr1U25gawdcI3gxKEnw4gz7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN_2QmtCoxjQspFhr0ODIlsuJ1hPDSs7e_qccWsu8JDVbgvaZJ9-Pq6CtmgSOKVu9B4GuKlCBWD_aWuHn8Ghsm2ZoKK_7yHeGQElS8GQGTmPdVk-k3yVZ7GkDJGwugQjkGltdcD0FlzW1qQTDUOkISdnuOmN1kdpfcl1JrNGMv9Nfr6Sh2CqQ9Oqorg2xV-E3ocKHsxm3oVDiY03_oz6G4dm-og5P2jHMX1Q13v9BX0wFQOObQwvW1TC0yrTN1zOLGPIOvTP_2_NIjiKSQRSB3eScoKBd9vuF-VkwPsfZLrnVX2fxhDlcfYZjBFEMmRVsZiGwzZFLUyjnwcnROr7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6--k5UiT1XFoSupMBTxVo3i36Cp8N05sWTh87pKz506FAgmRcmsTlSLb7yVNCQ3dd0S5yTxyFyUhGL3w-8c-PVFoFCBe0SLWm5AwdoJAOueThT8aGRIZsscVCxNApDGCTHf3Fhma-xCCSY_SX5OrLXVt32UQMGB2bn4QJqI-e4pIbc0_AvKDzZoN0k5VR18tAfDfavRrAzWUdN-P-fpo9lh5xvegN3vo7L6yHDfJBthIbZkZXwdVGtw8Cy1QAmsiCrx1AlBP7jWKfQ1pqgxxcGDJAJxPaEwl3WZ1MZN0r4Bc7VJydlzFXdZRElQtmEbdinVHfX-Z4Vdz73wAa5ZLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkKaMp5lDkAUKPQ6FXzBkBjrdkkMzKnR7mAy2Ex2HqdYhnlXv5Rhx24kk25NmWqCURUGSzm0k4Y-bQkuxf6in-mYaZRGjsaeQTOSohVNOmbzkViiPi251b4aL3Gntt0VbeSwnx_oLO0vwv_FX2adw2WwrDbo-2BlK7OVD3GP4tqycA0467nMHpocJ7dY9eZPjdZ9UzpXQyPNrVFy5oqvSoFkwlN3XqAWAvfXI7Q_goTgyOmOZDWsmiXDMiTRL8tyy9WJScnTG9uFraKIG-khIujun_dgweOBNW3jRfFKKIh6Domx3bL5KWhpVYoWkAf11xWahNcGP9Aae7FGA7MY4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkPSlDShiJxyK-apiSzWmD2aj_hGGPHlQxg97uoA4lCLyFsD0VMaMtc8AIqOJc9wzcXG4yZTga2jXyddb2b1WwdU_ueV6UGNP_56bS3R1VXLCZFAMYFwjNdcobhCMdno4fRMXwRNDVQPzyTrU18qzyMcOm4YOoqiT3-dXWFsbSteUp_UJa3DylCIU13WaXFLi1Jw409qObAjQNy7SBO8_v9zcaQpqI2fQXjchwLgogi1kjw8BjLx6JLDrY7O9OyIBQlXVf4rT08IkOJ6Vc1J9Eix8jN9kJ8jNAScF2WSHLXSJFX9pb78Ko_vDy4ygr1ASOxSOuezZJbE8qJuiIZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSS47vcQ1UePe34h_s7Cra_wT2UpjNLg5kQKFPsPKBJ7W1pRp0NTZU06RQUP43yhSnE-zNAEh2C03WyEyJ3fSPEx5QNkNZ63kBGCg-T_IVBQ6nxH0GO_c4XsoA3W11g4awv9Gpwb9H-gsO7A0P6ZY4GKBPkAGuoe4YIY4zEiI_wQY4Z5Gj6qgv1mlwmy8jcyMDOwNp1_KXKYgh4oo6d1wQNr_hubG9CYO0izfCBPkZYiGgGP35H40oV-prlm3AWX3g2jt1dLXhuP0GsdPeipYgbRTGrSvMLW3hV5nazq_lQ3wGKRrmTSU40qiEaOcqTzshgt1qy8hYwwtm93hLQsPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGLY-tqkqjGUZw1Itcaxx7NCHGoreqHV7meRbdqXSzzz-IOh596vakfXeXFEl2RvxUtRo1sfYtoildi1BlB7UwFomHa95I0ZTJwVQ4UcqFRmHbi_nb510bp6xRHFiTjgo98mM4T-Ke870IvLtbt8AU6gyPHYibs63YWXAuIUHkUyy-4osZEQa2Ij2FQz1AcdkpmpC8H1_QEQrQX6gz1NpoNG7VB3lo7_bj5CqMsSTz7j9K2GIRN4vn3UX-8L4lpshpxB0dEjET0EyOZL13zs1W5TLfpXTb8b5VzV_-ZObhxhKRtvFjYMfNtJyeCFSgyn_J2V0ILe5rp6Hnbr1PDwsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy0Zy1OJqjVDzGpu4kwa3cmT6GMY_CaC4QftkETbhxBfKhoeoxWF_K5BizY_Wm7PEXzp7OmKh2d3kDn28ErREGo0MIuPrISUtPctiCVCsB-bMQ7UHfx-0FUxDFx_FocRihEpWAykc6hJ8ovbUrti3u3IEXN7Q745Tsl4hAY7NvDdHtQfyzcx4qcCChF4ze2ru1RhwTI04aDksAz0WqB-6pmnCYqvvbvBoR5AbiO-sqHL-maAT_SRdAI5q9QMwTg7yOcurYP3Hsl5hqPEv-gbeOftnj0mkor22eZn3S3QCU53EyTHQ1tZQvY34cXD2wyRTBG1pOF-eKCn2OqV0KElyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRdLVb1LUnd_AfGxukKpbUGcrP1m-EUDDhteoqvAeHj6ekm3eNS-5OaEfPYpuP1-oOunBJeyYyqkDl2A4TSfPvR66Jkm7DuduuC_OqnizUJyGi5mmN8x_idvCwJWbsR93aeW-DEifGQh2VBR-f3rtfrUby9goX302IguQe-N9UkiXdk1Sp3PHYOD4S7v0uzLZggC94pQfuejJhpIzcTsTIYSYzpLWbGUdBo9q9kN7xTwsIN7Xui6uJwf7A5Pf6311uKhUKABr7pAJx_i0GzL0C3W31sKhWrlXL1laT8_fH86rHCxr2CaNxO95I6HHJvcchdjafUBd_8lm4xeBa3Fzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJBgZHDNfODG-gLoSrrXYFDHYfo2tj9C-RIyMeUIvR49Zj3DC_vnDnytnq4p396PcDhJwe_TR2YIYdFS9wvTh-Fi3lx0Hk6tkMsDIp-JiCGbJymqYNwyE6STWeM96j98FaNP65qU7PR6-46-ZkcnP7w0sRqONSjp0dx9RugGDW3mBmc2pSe86d8hHBWfwOGHUpxcH32nB13KWg0wa5od1UOY3mpyzl0L3rZQRvSFW266ffDFNxXBEs-2sqqO0F9raqwHD4gFDn0lLQwpddo7cnOynSDNslwpUsyAEovQK-IfVfEhjnD_gyaOYkMWgWUabTTRr-wKZMydoGe3jqCgSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCzCIU7USgdYfXM844byMn2LBpOuZzVKUstu6rJXnjhh0lBpsd4xEyGaOvwIcbR2v7m2wirVB22-VzLMXTu6nE5huvfNMTV2X8-3yLtOtIgRTaZv10143Q3DJD_HRIywm8WgcT0II5bUSmYOE2NVfj2CLPKcP-IFhqfzXLWYjsG2jspMVXtbbCwq1Xo22kpSX8GsAH6P2tlfqMkwaaoUno7NHNveFYjrwQbTR54up88jWrAd2l-dtO4TSinbXmYlFoqbZNsWetAn6h0_AVjjCQjdeJAVaaajcOCp6B5bU0BI_5L_WuTrRw7uVUPbGaEvvbrsi-9hejTzxwB4FBi5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUx3skOvImMNcowERfUIMqY-Scbk8XqLnkN21QkIEUV0ovJQSaZ902hl6nnXJPvP6b0hqSLUcGrgcy9QJabYrUN6_aImSXWM_GJeng5OMnk6U3kuZGGCv9GuX0wNt9uuS9wgrHUXkojxGHUI0cHQ2are0wxkKpaPUf7BSFQczyXUHFb6lN37QsuM1ehC5UgMdPQ5En0kN9qBL9wjoYOQWGCLVILanl1zNr5ChsDkNSjfapepX_rxWPAXuag8lMw4eT2kL2c55pcGuwV53J8_EUfvUjt64JkplcJPoJtMKCy2UvqeX0Cb_j322UxBHglIDHpALWBrkAPvGDc5Tar8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBtsPvrXKc-rQ2gyp1NMMKpk7-Ml2RnHoLv2f0GEwJ7CkoQt_2dqEGoU9A83dmxrgILUKCxg7kxpcaRNC8r_fj2EOsT8ciakqqKUXVkVojoQOd0UX9htoMqXAOQxKk00z-OXZvpQsFj4NC7HiR3_3cCDhtrfw6XxVUPARhRZfE_8BseVs9BbIwzkqYC88CaXSnxQYX4uZjYNXVKEstFSv_ozhRtKP-B2-zDRgGjR60gl2D0etHZ7Sp8tuh38oNeXJDguVVhL1GwebT4r6A61gtG_k9IokZvyEzyzkarkmDA-OwNqE4niYpqEsEyGDdRfjh8NOITOcsbIoFtNLLrh6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=bKu6y5dOgRCBNivC8hrgfHjn8FcF_IF1hynh_ZCeOMgEsVnXw-bQPpwz7VMBkmfvcillk_VfAwYLnFED675tmZPEaXncGjOJ7v2PPs7aFxCiq5vrUv04JMrD7MFdPtETw9pQ6g8o1EbQ2QxR6HJbDX5dsHEbc5c5bvBLS3eMmJl-BYrCstpkAv5UkV0qqzGI5FrhBGYlu4ibdGo-AuoWvEcJUmZTXDG6piKIbIIrItFDjYIfoUxSWXzMv17S4XFqZnP_kbElC4rk1zB6brh0bipBc10CBIUbNQUFCwrhgi84Dl-_AED2hqnDJsnCzDbJtkBW0r0VOqwY4_SMg6CrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=bKu6y5dOgRCBNivC8hrgfHjn8FcF_IF1hynh_ZCeOMgEsVnXw-bQPpwz7VMBkmfvcillk_VfAwYLnFED675tmZPEaXncGjOJ7v2PPs7aFxCiq5vrUv04JMrD7MFdPtETw9pQ6g8o1EbQ2QxR6HJbDX5dsHEbc5c5bvBLS3eMmJl-BYrCstpkAv5UkV0qqzGI5FrhBGYlu4ibdGo-AuoWvEcJUmZTXDG6piKIbIIrItFDjYIfoUxSWXzMv17S4XFqZnP_kbElC4rk1zB6brh0bipBc10CBIUbNQUFCwrhgi84Dl-_AED2hqnDJsnCzDbJtkBW0r0VOqwY4_SMg6CrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2sg1q8MBoJgwNu0_KW9JGCBoocWMS_nfFjvoOAPwdQfeOGf60IviUQt_Fs2jR5FmuSRMn1j6hiMmv_g8ZINIRkWD7QTOtoJwju8MQ3PoS4_aAQqlZ-oeqOYtFTvmu4RxROTcpA65KCnW9hti9ViAdGrN5EM0GiSYASGl3sLwdXi3-sMqvKBr2oYcrDzWEMMkIDJ3eP76LRN3tmwH7XhbVGaV3ENfuZN34q3ljVFht6BaqR0b2MgQH4kyYqKvLrM3SxstN7upMSaThey65PYHAsAAOo0PSO88gaOmbVOEguojZacscYN3QgaCe-Fd1tiCcQG6xq9YOyyvGM2gEBFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWurpiZtyCL2tu77ZeJGikAGcLwF5XsqzANgxK-lcJ4D7ID84JFZvJ3R8sCJRoUkqVraT0nTCNRGU24Gt1dzrNKKAu86_udNXAK2yU6W8ixVqe5YCS8WDnFcY6_FsfplxF_XWoJAE6Jy3eT8Of1xAXQmjSRozJnC1-b9LynuatvanjXjZOIWTsaAdbud2MSZRtXbRaS7W23KD3trisp1AruizgvS0F9e7YpLHya9Xj66PngHTpMMvq_LCk7nii0_paMuxQtXmatdkSHsP2CrlE90IU5INyF0KaHBlBgg5groHWDDyuk4y_DO39XvnufeqD2N58gekpax9GC7H1MpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTZ78pUcb0fIob_EmHNsmg5EEqYjKrRc6oR03CK0cXC9uFP9MRUm80MW_DeTcapm0-jc1NrkzWa2vrCqZyti0Kl9bzqWynGBxHSjFWIqqBTA90Ij-H1W2nzFEqsLgoCEepqZCUKYNT4q2uc4gYauZluW6MQiyG6f3OxE6KYlccyFAHeYGlMyORyUzcC5tSveRi9bLFpfqVb0tp9Phl58hrzLocCyrCIzp2GVvLYpD5q2Rlld2cOJmxTyba0haxT38K6rCh6rlNk_mC5Ser7vVrPXJgMYVV3pxJxS6CTUaFDxg9qi9BJNfnzwZLUrR1IcnkbRY7pZ2Yry4lof6U0XVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=oL2QP_geJqFpSqSBSza2N2yolvqIpWqocY8urO3ZCzhEhgEH-huad_2E5ZiYUUVJ-1PA9CApOoMMlAN8VmhOC9m0ZWP8ePGoW1O8rj0m6YqfETbmEPFVeACj6Gbj7-0zgxwPLVfve4ISqZHOaTxRggmVRq_djwNGh2MFR_GsduA8938G4RvPMEqWv3DKTLyN4SEaXW5nFV4lRfCBP_fK4YOZ47BbKAjEca3-qQBXNGEqCNQvhLO0xSEkWsuO64Mxfo7TRW6m-nQNxSGCMVc4LIXv7dJFhJLp-T2fBxH6DKTXc_jHFN5eUMmW3gqURMWhluvwVxLExLvIKiT8JMQHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=oL2QP_geJqFpSqSBSza2N2yolvqIpWqocY8urO3ZCzhEhgEH-huad_2E5ZiYUUVJ-1PA9CApOoMMlAN8VmhOC9m0ZWP8ePGoW1O8rj0m6YqfETbmEPFVeACj6Gbj7-0zgxwPLVfve4ISqZHOaTxRggmVRq_djwNGh2MFR_GsduA8938G4RvPMEqWv3DKTLyN4SEaXW5nFV4lRfCBP_fK4YOZ47BbKAjEca3-qQBXNGEqCNQvhLO0xSEkWsuO64Mxfo7TRW6m-nQNxSGCMVc4LIXv7dJFhJLp-T2fBxH6DKTXc_jHFN5eUMmW3gqURMWhluvwVxLExLvIKiT8JMQHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAbzPnmFC-xQmy3vM1tEuDWGPqVCAKzzZVVyi593ZtgkBtzdZrS1pT83WTgbyELJyzd596bQnsxu6zHZZij9A8ebmG5HWDapofE3gJFuySd0ppXI0Lxw1bDJAQxdZ3D27VVa-kG6sBLZma3mna6y1WZ6SZPdqLpthdRG4CVwgQgWsYVA_qpEnIVGykUXm_N7ftscWxL7QsQmzFx4zBq0AcG9T5K3F_zvZROL_3mjClcheNp4O_NQUcc463n-IWOLk7_hvzdBlX_vbU4276QHHxi15-aI3vtBbpx4HF8E_JkFY0D--QwkTNoR-X_waYWCCa7GQe3RtjzoAfp9pFTF1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgxaKSb6gwN0QfFT4YDor_5LlVxJeLpr9OSa-5mEDK2eTRU8R5FzF-qlNAlIsZvfetGDRwLRLfRXjRcldhpzNicPTN489a1JqdiEtj1FBvHLmApP0E1JBhwKaJ_NxZ7zyf57mz9-QWrxr1hvjPi-z64rHKDTkzKXeBGu7l_lZ79-LxwJisWmAMcF8dN8qo-NbxmfAyHkPliHPxfaFnDAa8--ks3MoJ1UJa54nQoXSkojT4ySFirsDYLejyF-jH-EjNs0OWa-UcDNKP2G8quhdURta3i7KzoJiTqiS3pbTNvImzSg1EMiVmwjBnH0CjYXaGy41jiK0qxr9lnDFWjP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg9-ZWLm9UiHLkK_Urexnk3Jj0C8F9LSq4PphBrbJa_Zl_FESqOxlRr54ykKRFLXRZf7gcilTYtws4NDjn9Rmkqw3tlBtxq51Rc1AZIZpuc6B-2V9cqb2TKe8CyMdG_KSGYujCxpOu0xJvoym1eE3wRC8OiXcdCUzUA19kZdyXIFkPD0PWooUw8PhYQ-Nu_jvAnrdi5rD2WPjPfMlrBpISUc9P-VSpvxG-OttEPtUsTKSPoVAljHcPBCIyUL3ute4pX1Qp1EfNDlpviaQv0a56M5ecMXhRC5CXUUJ2cj4jsVx_NriyyFihpVZ9vyItPz1zWUzHBLYEIs_QL_RAlzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSsFb1oQVkI92nPthLvuinGBsCpS0TsbYEM1wrKUabZHCGyhy6KnpJghVSKl3SzgF2_rQbXEJu1aEM1tR1NPTr0XibNaeQLEyoqBdqmkDiMy_FdTECaHgzb4NyCCthMQHZtfpeq23NEjqxgYLaaMT_2hmvexX9BgOZTjjrV0WxpoXiiPbL9iqLZFPvmbZ2q0VMaFXWiaaRNvstq2Rr88SasOgIgH5kfxmGhjubtZr2Qhb8shGFv_UtJDZwCAfGgTo-WZwhd9ow2eGVCv9X0nYEqPHvOO1Ti5hqWl4wykM_1f_Cv6wxGVP-4IJC53hiTxh4E3PzkmX886iuOABRNovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDsLOoAooyDPwAuH9qgcsVhBt8X-0ElpmbJ9HejTUFbu6LUwUkxZoI6o7CnWwNkXbmAx7mfXqKgOhlN-Lq5V5Ru9RBIhDTCdrbfKVF6lUHCl0CECxXsl35sNxDCp7bHbyIPWZ6g5qgFBbh7zAn7B7qGxdghH8P3qwbYY8rLji3QQR3D_PwloINwkqqFCk3TdCEsViPBv7gvkSerldw0B-IHgm-N1Lh4QMkwYm7x5NraK2MjmfHSlKbmfb_NARcOV7gWSQ8Ftz3dzenbDwYUR9Io_dvWvI1EvDaDp38X8MngWJek64iaVNxQFLFNQzBWT78tNK38nqtgWt8HGQRsKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BV0s1etJGsMy7s9v2v7d9pDpQIcahASrdJNb6LlzqpZmjMBYzy17j_pE9TJQO-39x2_LXwLzIyN1nFrhciSHO9AwTRfZANVW_Qcqiok27v4FAAWlYxRCp9qWxv5QI-Deb7w6pjP5eDMJkfA8SleKEp1fqqIcirqWdymA8iRQQobGg1E5SVGkSPkr48iJVzKE_9kaX27YlKMnqRB9DL9zPxnpxmfOjKI27FP8WYDADZ-1_D4gPPtEz8W7TN3vlOw-q5-PgJACjBjBulUWoMGh1vw_3H-lBddzGfWp1SR3Puri2D49r9_phL5t12kNYYjB88aSd9wCcYwKEmqAWjmp0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kllUgIVd7pZ50v2m9A6fyizjftqa84cmwxv7vqZoIG8rkzVBWNcbz9dZZ4ZlS5AX6_yjvJOqmv-39SSVogogowjmVzZ8a5zUUazU9k7vdQcf-ung7VnAmfDDG6KWBn1OseF1AdOe0IlY5k20hkSIHhLuKpVlw3vHqfBExhw_xS1KBRQ79DH8_ZH0BvATmfog3puDDyuYg5hc9iJyG0knDgkYJLRGdRMctiRdgHVK7kH3JB6_a3hCV7xGf9ioGWQDgKXfAC5rDq_4UK2fWbPvt5PH2YgQXC0BQXkKo6koowREjv7Fs6-iSAYh9Bw91N_zrnGhZ-msXxCH7RS1qVGU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=O7E4I7lQxAi8BNd3HqKW5TmO2TbMrJMaAbJkd9Z9anH5vIQyjpwqVulLhFFYQRjqY4dHgJJ9EEDNDpgMoD50KlE6cY7BFdoHes-bAtFB4SmwZ8Aranb2emVzfM4My3DiWOqd30X4aDPRGl5piZ2ebqhZmQd4IK0leVgOnz90S4amKVBhaXFGf-bkNEMoV_0X7z6yMC32ub4z4jWwluqbuo7SgHqT7s03JvHMEb93carIrrt-GY1blj7gcTP1bacOnaNH8UFVujy9okU0RTyROvFVgnGIjPq9UkGM0P1XpxIzVd_6svtNlCH8dnQ9HeM2Q4qf55_sYJNK1uFsbOMyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=O7E4I7lQxAi8BNd3HqKW5TmO2TbMrJMaAbJkd9Z9anH5vIQyjpwqVulLhFFYQRjqY4dHgJJ9EEDNDpgMoD50KlE6cY7BFdoHes-bAtFB4SmwZ8Aranb2emVzfM4My3DiWOqd30X4aDPRGl5piZ2ebqhZmQd4IK0leVgOnz90S4amKVBhaXFGf-bkNEMoV_0X7z6yMC32ub4z4jWwluqbuo7SgHqT7s03JvHMEb93carIrrt-GY1blj7gcTP1bacOnaNH8UFVujy9okU0RTyROvFVgnGIjPq9UkGM0P1XpxIzVd_6svtNlCH8dnQ9HeM2Q4qf55_sYJNK1uFsbOMyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJtY5yb0Dr9b9fMl-TeugmsvEm1KWwLRFbmoOGWtWnvYGXoycK_BWuSFItzna0BE-bWK7GFM8Kxb2ZjNUdoBeqLh9uqt9rMQJSqQltUFmNrHf-gqqg_sXb7oh7p-dPHyivCM0bOw7efdltesz73THNuQnGDg0a5U1dAmJ1N89dBfu30nr-ekx_XLzxA7RDK-Aa8tBSmvO-T4oQvoCeaxcPX7YVBXGwjcFxv_1HJEcZhHp1v7ptK_T-Nl0CtP4yllqNc1jGW0tK3jNLltNdJ3vc8kzfb3K4YMOcsa1wSzdIcWU6bGSP0IHSDxZu2CVV2URs1WlpWwk-D9Rnf-qOA43g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNP4OOy1i-A4dkXC2KEMlF0pOdJbjNRzSlsP_JFlM-hfJvD-8wgthv1vbDavMraq9ud2A7OWzJ3Kd2lzpvuL2lNcc8YCnjpCXFJey8e4CfGQdjlJWtjaE5zoHovsTTWhT26mCWhPBuw2P2YvK6-Qzdklyd_vMJXRJaqvwZJTeYYWLX9ijU8qTTEwxajE9bWPJgub153SoBuRlACdUM_r4smf-aGHnT08eBYi3fBKc8W5ajuIky9s71V_sirhhi4QGiS9P-EXyb_hsvqt82VqysHbtdutCvp4ky4rdZINQQzlnUvOB4AzNKRFEmOpAD3AI7HoHcnDGBbdxETHnHEYGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPcwnfOvxNXgYWh2SR-9i8e9lACXd5Fz9dofSW8ZXrrYShIlG_7Zlf4b_If2EweDh7DIYzwmd56ngzxxz27mYJnAFXQPCv3chJ5u2b1PEzGcI0_T94BUao9h4Aku03OHF4aMdz8GRhMHiYDml46dVPRaTPn_6gWyzM2krhFp5XfO_22FGJ6ZPZ_ECLsXozljaDikDRNBKjmUDyPewcH4Dr4lYWWdDDcXw28Leij6HRsD_B_4-qV-ShhMAWf4peUSeJZlxH1vFg8-tbXCHU01i8G1p5rHp_bwVXk5QHEvhlW-ojbJdoFkj-zpG41NyDJ6tC5W96y_TULp7lcHHWlr3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI87gDo18F955bLkqKW9630GRsKxFiGuR5UWANW3ikNkDTCdcrMfXGU-DO0o_fYBvCBFV2Ckx-HG2FagHxNOjUF0Hm2q-oLLD6c3xkHy5_vVQxwCudyBoNA6kj54wlKLOv2tBCy0mGZnbTM_2SgGd1pmw2vD32WrzpH9hTgYABNM6YmFv14MYA4ifivfzpq_PhVSBObisUApcmtO2Ue_EryVK_cHrEgzJHuEdccYwTdPSqiveSS_WkrJbMXWgHpajvliAX3a6ihzMSi5ts24fKpotFGY-A23trJKTreypsnoIEtgs968y_lvx1eeb9Qvww8LWt72Kl1rbtdHFtFCXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7D0WGzrWdhnCXCKIbqguiaoCxWwwVFbYoS79tOL9y9T2ZJ1_SrFxL50F-XLP2fvln1h2f8OkejWVQveXbiI8vD4MJ3q68o8SYmnmgplAf4UItFqtx-OynthbCeZ8Wi3rgy2EIxgorlcnzSDSw4UKO5hC8fL__Vvr-RSb4-RSUbHANbGdr-g5kVOWimd5PUTEzv8TyLHbTjgKUu-K3kH7ujMmQgp8YftO7HHJhM-Tp11XDetylA6edfn5aLIUaHxGcCLqJ099So_sPGwB64az4A_hOK44Vq2rxV_Rd3QBHfR6vapz-JX6re9utcU9uclDU7VpTo7lUGfTk4baMIDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8Gdc7BxeLZqFuYg3hSF3QaXchCpuKNywvzjvjtaszc1AckxTkeNBE5vcjgSAiiWeyP9XZL2Ogo1y48372uBLuxFAtw6t1uDFqWrL0etrZYLNFf2rDJyoIkamKqFNbK0_jj4eIUYAJg1c9ud0IlfrM6vip6ErQoF_entosYeHJjo5jQlKKrz6mJWeBAjpvMnHmMsQmBY1F8a3qc5SdR8Jj4ODGBgd0LPwW4ccrn2Z0VotzrPS2gNYoPkeZv5qHnPajlCsvTrjqttAXlcad8Bpw3DwmyUVJkOa81UEI3Ybua9C4C9UIZEkxTPyNPFmiTRx7KDFkuT7yEyTi5GzVR-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTzam15fyHkeS53DKUU3XTnXk5X9BPlXcrJUs4kdq28Ip5O77ik35BfoF4MAwUSslc_jNngQx8Qg7ccnQLlrPePGMzyigNjdgSvzZr-Jt0o00rrLaxLu50owL7jQJKUACS3eoOCi1qbwnh_ySMpSmFH9CVZFy5mkaJbNFLfKg1UdFeV7Bl-nCwtwD1a-dcmGmcRXS-vXMyxfFvapU_enRv760kF56H7rBdr-s8u4cQlkD6aHNdZDhJFHUaDiIDFp947ujfpH0qpeFgLUXMVRaiqqcauvY-NMCK9SEiXHu7kRgrV8qfPNtcVPIhJUQafb-uDsjCWxhGvHpgiTCENj7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB4rRw5dPJd1c4ldM61B41EjXEvDWcmBFZ7x1cf5v3NXcDgrALK98MsABeNT7UPD-ZYMlnQzuroQGMOqscE7ks34eEEUgNDrlm2UB1RDd-Za0qcb34NnlC9tpbiulHtiL8uUKRSe88KEQMMx0UfxlvM8XCGBn_A3i0ukWFNViCxBxTbwiGmACQ7mKTPumE92b4Rish8wQpBVzpIllVGaS3Gdp5Cl43jjK6AmaF8xERwjKdvUhyAiXcOjCzVpcf9Lr1EMej17janciYdFyY9DejT4l9uCWuM78mEtYIqDoxQokp2j6PrLFRw7U06GBgUaKIrV3jlteMDt4lYNOMWwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daaLCO08ELjky6YcKGN7i4-aXqjEJv8hoSBpYxqYyndiH6s40ki0YH7qnAR6G9BKGVOX5uV6lLvfnzrC08Fl_uWdECu6rpLS2-AvQOVRdoZamwbZEWNdtTb8QJSbMQtZmHGW91P42cCxVOaUQuxHyvufPROrEU0SxfGa3OxuB6HR23kI0EiuBZ-dRgKr61v3HWgsABAneq6_rfzyI0K2tPUEGb0ae7t6l2ZbiWPiVjwBh8G5cxQeMNTkCgYSdG1ANEgDuQMPxl9DVablm37uE4KS8OzvClmATUlArxPmIKThebEnG8yEFoi-uvxIEEEJbWzHaHfgAgSBUmiWUTjJyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mnu7unTR-YHlIUzKm29g5ZvJA9EP1sg5skFJ7D9GIT5wQ6oqqMfx-uZNYZH10TSuKXmdI-u23Go8ePSgvS5mQOv8qRjtIMtwafNsJUEeID8Q0Oq9jjqmnAI3XxalnhZ19jU0luz2-WMMXQrjcRBm_0uTHxLF2cGOdWyLFaf057HwrdsElQwxMU_1pd5IzvcQwsh-N74ztd6QkUAy8T5IYtTvHiEK9V-CyqVEg0TZKAkqe1GYPU5AYDBDIg7dDB6GWZN2Uf-RUgIic0vNn6VeE4J-nGHv81gh7zhpMFROeUa8F2ateZKGWRyDu24nYn23VT-k1V2hd7UtpdFEqzmk0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=mnu7unTR-YHlIUzKm29g5ZvJA9EP1sg5skFJ7D9GIT5wQ6oqqMfx-uZNYZH10TSuKXmdI-u23Go8ePSgvS5mQOv8qRjtIMtwafNsJUEeID8Q0Oq9jjqmnAI3XxalnhZ19jU0luz2-WMMXQrjcRBm_0uTHxLF2cGOdWyLFaf057HwrdsElQwxMU_1pd5IzvcQwsh-N74ztd6QkUAy8T5IYtTvHiEK9V-CyqVEg0TZKAkqe1GYPU5AYDBDIg7dDB6GWZN2Uf-RUgIic0vNn6VeE4J-nGHv81gh7zhpMFROeUa8F2ateZKGWRyDu24nYn23VT-k1V2hd7UtpdFEqzmk0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYtUJnGkQHUs19aWjUb1QTPQASOF17oqG0f4Rwvr4w4dqlhFGjyuZnx-sqAbcZFFrqqtAYFmYn2M-8Onn64XcDjf7WYeQeGN7_wcaJ13vsWufbcyjSGyixzMynwKIM_VEZjfEg4POcKfsawTzqWHXquVVLuUfzeX_6ETl5zL8INeqGIHweNocx6gG8acB2CLYATa2SsNz71_oOwtJrihIbQaRDYNvh7hhiYKqjJvyTFY01sIrXS8owV9J5O33rYMLfKc1j9chd53ClRUJcAzGImt3k58YO4uZ8bTfamR8cih6XgdIqtEoBaOVf3vxXWI8DX-VlXnaulk6SDnNKi4XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjL_5EWJFQVraVC93DZdsoIBb9KgttJVyr0mojvGos4nqw5MSw_DeJeOO-YzVT2P-_6Vczup4TJwLiCgNt0AEkNCB9TH3a6L7Ih30VJvWAON3Nt2iOyR_Ad3AHgraEO-H-T_LlU4_0euedrTnHhe284tYU98l4Y5A0RSP25p6bPzZ87nRt_dBZiPNg1px1dq_zihN8DS8dtjr7ILlCygThm9PAS3cBS14vb7YT349G9_j5FStDmRajgs85n_VjRKai_ylRhPpHw4ebzn5MVoJuAYobxi1KfViMjDcx76rz7wlA_YUDsx4493T9lB8420CuJ5b2mkNwaVdFdLu-_arQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW10yfNKUjmdkVHdJBLYgXZlczcVtDQsFHYIkgsFp3y0RUbqXRMlzDH5fzF-HIqwn92cQtRWNJYHS9xzKTNTMpTu2jRhe85CTY8r_0XP20ANmkls613FSf-ok_Zw4INg-LaJxizwljOk3Ur4wL7P865bdAVI8VnPpjWhIV1Awq7m_ipNSRePERBUH4XxBnOU1ztuj_UF1dOA2wAk5kPMZaQ3aehL4jmAwcvmYzhD1z-zVSq4o5pgnloqd5Y9q9lL1Wo600Rhp-K3SY-wwbMItp7g3o1e08ZI4388WOQVrLSPHqJ-K1zepUvDBNckQVcEeKu-IRV5GOUNaAfcpxPIkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbxmxu0LsbrvYeCctGeWnny7D8sruLCwtTZFOBatwFNQFNPUqj-gTVkEAb6TmR95-mhK6D10mtjD0pJJRBfY6bHaRWPwkLxbexgyqnggdwE8YBwuQFiGR_l0-ewL0w0ttc4x36lDJhb82mEnabC0X1Qlnc909woKJSvWdZO7q8SUZ2rJX8mkLnTwlAEh2Mkug_uONc-28O77O4VRfeVh69RzrM6P6KgVNPCSuWusqlGGrNqU9jnhdz3PEVnu7foaAT_s0tZHcWnviPqPHpexYPI113MSaypgokbDdBQheJEtTTqTqnRg6QZ3lkWEMh5ZAXrBaeJqs_RzYlyyJ3sjqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4iXvQqAV0L_hN4waupJ_XCU64CI8yHSXkKDr2Ya9YWk62X2peJQDTckwHfqO7Nuzg5bu2ClsNm0vIiYVAIH0fAVElNfi2BSyGb3UKlEszoQW9hIDTWpu8_jJTLK0pDrC9XjaXlCVIVV2Bjq8GUjfg9Wd0BrGpUKkwEAbrA0Bns142ctBhM7wfcxfGaNim3o1DHlBPso-DYnWqDdkAcsZR3KKd8a29dr6OAlX1n-D1OHdx1p29aT4brcURnZl_N9Ikw1_1c_GGk_JWyJpiNWg-KnwJGPaRzfLbUJvlqjNBnQ_DSOYIoGjRXFhCrgDsUMg_GJHEubUJfsjMw5THS0Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCImsdlwTF3pvm3JXjDu7m5kx6KHMrbm3H3Y8fA34aUFaECXrXWHWEWEKLVG2_JrxIKBzddon6lnxQpAmnGHG65n9vpWBj2etTFQdZMvBzvd6hMeqV2ALKFvfNF8qesVYJZm_9KNLfgFcs_tckFxft96Y0ezUoRHYWmHa_ZiRXnyvZNFJAFmYHOhQqmo4m-RKAzMre9aYDd-RwkguYbh6dC4zGi4rle4x73E74FjbFeZ51V_LHk-bFtoeTrALEG_LOfRtwM9tvBOC4whW-IEfsYlR2IHI0mvNe717R8BHWdTS-Wytpt3iA1m6EvGKWq_nP7TtlJu00-PLgx9BTJIZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9SXf2MHR7oJivNTBbTH5h6uI2MDub8AxhU79Aryb1Q-4oqCREbOCGiPFqin4x2OZYYG8RVhrNcxK30I0mVaxc6ILBGLMo0k-bAkqobHxWezE6O6Vln5MCFgH_y1OjwlAgc7kLP47Jxqrw8eZ1fXVu_tNJ7XlcMKh6A9GuvII5xZbhpLDMw8VovutuTYaBTwjiw2CQTiEIO8g1N3Cn3KFivY16DJXQqZ6sqVJ3_fgwhnka7aBjlvfITJ0Om_CQqkUDoDumUlQ-etPE5RFdD47N145sD5i35jrmFTQo31MDAHYyALlsfqOvnu2Bobmxc8gxeOqFw6G8d2QJxJ9Lq6Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZXTZrDitg37gd8xG_2jS10VLpm-U4jY7vYhTD1qQxNOREOgcmEAuQmNmFKzN5t_Xf3vm3s1S4Yx2nwjpe6eRn9gFOa6YZhvki6eTvTOX90jrIaYCkhi6g_V7TLWApLez8NG5gvAf5om2IevmBwT1B2Fyo7xLSjnsrWGWg8btU1pyuyEeqIyYO3CRjm90uutciqU6BfIO9CYcnRVuBeM-fPJXlnUIodqIFi3dvU8VD22OCJNpqSVQnGrw0fXXWLtAnm3eiQWofmtDwg936rC7v5gQZYeLKtdBNC8V9Cs7olyE5ZgbzzRIENYKsgSrxZFvnH5mWguTfvBibphrK4Tkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGSajl4e7AOtW1L1loS4TysIcdoZNyAtthXwGTI_OPNYRgBSNG6prnSYxZ8N1QJJei_vQULEVSZoIbRNeZ2uEa-qGW2K6PBpl0z_9Tyzt1Ca5Kxvw-8gfKHDxRqZCRuqaVJoXMaJpQcw7SYw1ME4m9BqoNenJTXZlsByxWOsyDSd5nMNudaaaGL7iK8TLCbPePrgSxif5TncusCakuNZ96QxyJ_RUIq2YTtuFKoGnggoXZkC7GoHXApU6dFjp-U2Wj5MHAJT52tQSILBxcxQ0lWk-CGyL1o3kBWFwdRSlbcBCyHACtJov0_PqAi5itw4rWD9wP51PAETeNGUIyvDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTKFttKb0pM7mPDeFV86fM63-Z5m8J0IUBcao2fDyPMfWOGSVugsNDGwEs4jjDSRqkFzRnTMs7-l8IfticL9TydShKJWg11pSNbGzUvYc1brDk_uKEBjZO2bOSMPUhwB1e5caMWY8SdoHne-UPApyM05TXvjbnL_lBaTN3sdtx2UDn32gstaxs7ugXVc_85I-sLzKoRbqR18oGyfFNhuvvzTYclp_BZtMl_NnmLWHz-w8aN-bhzqFWw5Dqq_A8AncC0seBB0w6eMp5pu1Q3ncc_F8ybnLireT97HWW1X0yKR8qvBqsjnSdrPKH0YcPW6xT621l5xh0ZytqpX1A9ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDZ_0dLTFvADV-V_S7tiY38fb926HuJWiGMkFE_ToZmOO5uKlKlVxq20p4BgENrqmcaKv4737UlKgEEb2fTDWk5TCWqTxcEWLg1EC3U0097WWi72tXPLXULH5LWZjmwmSSOdxE8liycjK9gHZMnhBxeMQT0Dsp1QQHarFdSDbbVHJ0GbIqa5r5cow4WJMAf-4UpgGiSBTzWjHhcZKLaDwO9dwwA7moQ1GYbzzpqQKwjy0JfMbW3n9Fl3CjBzlywPcfcxFpSamQ4MIcdSEc1BwBJrzzPoel7y89zc0JY9tdR9wLEnaQFzp1Iced270dPWYMiYAyHWv7QP_VgSiDuXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vanfFUc0B7PiuIkfuUVHHyKmUD9yyAJ3KKIACmFDVLJd-000yU_aELuh0ACcmRrw9e1p43zxyF8n_EAo5G7YXs8GP0zUyoGYwCpD6MPe65xKoWRsoE7XxbBX5w5rqSRLCqWoxQXha9Nj86xkxG9f3rtS2Nk1SaDsvRuYrWKk0ZFbGGAZnYfSYzZMwAPwaUAYdlYzJ_z1pWac9LjJuygoGrRytMHsYa0Pl-gbWB2AMf8ECYg2cOafWcFKogBPM9Vdhp9QcK_oUQY__U0fYvDwCTTNIsAzYPpbCvEOvR4XdS8Q9sgU2RAoF728feWCtGzFRQGwqFj5yz8FpXshc4yI2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxjlmkLHoW6O3lTeyXBJrS9nuxy0dMnZv-IPxZuUiqPvELDATvnEl9bVJ03XFY-1Ce3UAZ1K5XflqM_FRrD1BYPnxK81_30XwswKXGhs20n7DUv1-rXfAN1_Wls-mM8pMI5APiXUbArG1p6UHcV4LnO2jLWjDOsZyCor06CBu4rdPA5-jwL-cqjcmELcYxp7X-ec32_7LrLlv7Z4DvbHUFehYKYcIM4VmnH5hkegobNphDtDohXf73376vcTKIM4PSnV1U32-BJDCOBx33xPm-tDR_9DHfjCsHLJFoHbfk9Bo0wiZbJ8-I2E_WHwYiFM5mPlGy-J5fJ2EW3OjR-9XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvkb6rKa3QLNRWXtzSeie1piBxkMQNv5quXnPdojFSgLaqa0wDuTbSRZ8uy2cB7d7gTWKf77cwzSpwEZlPBTbJ3Yg6Z22s64PsBPzdFHXhxCx4ef7-TfySUV-qSN96do8Jt5jLPidQtGNkGMvG1l7OKwbyrpLD4ZTbrEWfSiWOX6qEKAN3kG8lw-6BpktHdXArZp7zx8rUMREw549P2vAuKktvWA53OcQ8taGCGZ3AaTbYaap_hvKKMDwzKubaS6LGEG_Z-Q4faBE9hoD-LV2WOgzdhFiFYQN8RO3dJWOkl3bEuqCgKag6cGRGn_YJgxzBsWY-caVI2KQ7NnMtX0Kg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=nr08V-23mkZYf8_SXRAZM00AC74jP91sBgFBNSQIQ3s8t9hLnfV_slcgtWTh9-4ATSEmu2EikHl182zhZqZQvB6mkQBfCtRpXKyrnXc-hghwghbn-qFNDX08AHzFJ61rOFLEezyc7oNIkVZHc2cyinIqgXEDbavPSvd3RF1MqI6to_TKaoFeGCLm2_zZF0y_y9NMyUe_Y1n_pRUBfK_uMU6o58RW8wHezx_NRjmwGens2B5M5SQ32Lr0VqgG2To_VQtb090OMbmOBGGfUc-w85s97pTeDtiZ_BoAHxY4PK8tL2X0O-l3TsK6QBRINMShmwNYUUp9QmEPLbPxyDjxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=nr08V-23mkZYf8_SXRAZM00AC74jP91sBgFBNSQIQ3s8t9hLnfV_slcgtWTh9-4ATSEmu2EikHl182zhZqZQvB6mkQBfCtRpXKyrnXc-hghwghbn-qFNDX08AHzFJ61rOFLEezyc7oNIkVZHc2cyinIqgXEDbavPSvd3RF1MqI6to_TKaoFeGCLm2_zZF0y_y9NMyUe_Y1n_pRUBfK_uMU6o58RW8wHezx_NRjmwGens2B5M5SQ32Lr0VqgG2To_VQtb090OMbmOBGGfUc-w85s97pTeDtiZ_BoAHxY4PK8tL2X0O-l3TsK6QBRINMShmwNYUUp9QmEPLbPxyDjxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/M1BkI_glSphbYZ_cjAks7MAUWQ00ebEBt56-AIcskuzD6nL7aCxrK2m4cDV85DWzD5aLQhl-5LisTBR5CrVaioRiH7x9ibxUFnQlJWiGR4R-M0rZTccY5pOOwkEpqcwZTPZCUDoyXiaN1KQNM7df-M-w13mJmSn0MlqfSOz5Cn_Q2HM-iLCwBdRO-wHqele5nwiidJc3dTMro0qJk4WOUdd4ZtQhrj2bgKNBbT9oSuXOWYEsMD715n8g8r4pPVgyfIIOxOnbi1Zdq1mdeDFXsv7vVD4Ceux_gpV9IUx9YLb4W1EcKLwY_tIOe6uE4oaQjPShSUlRoVKgTG5cKA9ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CN8ESWNQLp0dUF4ZjexWKBqsPuaLHJAdEZ0UBvCRUhHRH3c8QdI8UsSTd73NboJNq3frd8wAgAZ-RmWJuJJKGDwyzG_rIFUWmDb1JUuPb5IORnkxy4zkF3WkQBs3Davdjnk0YjW6IrwyDTRgjbwfPQq5j8Vf5vDBmHqqTya58yoHhTaeXr9zdt0mDhCIyyI17YXcpMborFMOzRKGvkkuXDPG5OF1XAwDtuUW9VZopbLBLY6-j_uvjxW2UqUuGEjIILMWaEXVuUIHwgCVCaMjZ8s4baO7XBXMdHNFt9lWC1gJ_lIFXLXTn2ToJmNKscidKpfTuUf0AD6E-uG335qZGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcumHVO7oYm6iszuvXG7hRlvwBmW7Z4GCjUUizN8Ku6e2AVPp5rTmWw1b0fozFADGbhkdTgQlLyh_J-Yxw7jKiBfVdWl3iTr8SPgpWISgc32oU5Qhloivp252tDMSuX0obHQs-3UJhIaX1rbMCOzLbANUfR21ysq8IIAkY__GTTcxlmSXy-TPa1tvUmGXOHWglbakXGzVzjG-Mt_nJ7QIKTpMzSfvx9CM1Kqv1GGaWxYZ1hb3-LIHqLXK8GHO7Xko11bxhomTOYNGT5m_5u6myajCD1lI4bueyPdBvePMOqaBV1dod_WGEU2-IQgK6fcSmwCHyuGeDxKCKo_id3roA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGbqKdC35q4ZzeWL1XujcPQuBhBilt2tw0luwMH_mp4tsu36SmBvFTww7Tb0D35qDijABtIogulajTWgBK5A_4x1imnnPUPHXtV60CkiTxva9rswCTfW0JLgmn-Y3phblNO-ZroUMs9fIpOWtqc92EwHu4c2dlw-dnK1MsBvEXt82vBOgLAN6Ad6-HmzGLHpExFHAre3SkA6B_mo5jlgnozmBtMiYgDvNjclBiyEpSWkNKXN5LUg9p2vppxJjvHZdeLQai1Vwafcdy0692wt0nkNgyJMxNFqd0oPGafolLp0vAaChIydNnzOjDASlyL-7SPjWPiqYjZNf0c11hXPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgEY6thrU5WUZe-qiclLIAkt37tq72RKlU54qYtx7IUm95SB9vFYnCl2uOT2Fr51kckgIwL3SdioLblTQwCDGb9LQmpVLvtqQWFgvrfLLFFRtDfJXNpgNtJA5i9eFOPgHjc4vd5K7LMB9hWygg1kgiFG8yswipzsmFZOxdWVsQCpF1585V403T8v8UX8Y2vYyu4LOXzAsBK1RC5qTT6Ysj3BwyYd9r7GYlBPHZwPuWNgV3_Y6XeS98FPLqJuEF3_qRQjur1vCxrBmFaGEbTJ92NxX4cnvLmCcLKRDhbNfOGaJlNpV8qQVqYeSShOgWmQIZfjpUIfcWLvNDs3ngKp0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MegZK1Y-ULOyFlVCult-4x9BLEwaUjWJMyxD86frp1IHDFkpkpYAAb6KLrSp7oA9V5R6tCcFd_KUKbkqnRqKBTM6eyv-7Ak_dqLdtyRt6hvSJGTRTM5uZThgVFeI6nv-2T7hIpcVXDedUciHoZRQ56K0MeSd4LsK-XGSzzpqH29sbLe2BnsWcYk1TbNCD3x1OSerYhUiradfkMHGjDvuWIoOjgvf42_MAQlExgDKNOpwb7_Qso0sNHg4kYv9HhhLHZcJffxY85FVEbLyHCIvneGsaBkf-qnWODjkQZBnbiJxfYyPErKgG5FVtoJ5Op_een79c3itQRRdXSQ1iDSfIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdZJUJ0KFt0dMzwJnxhfA5DXETqqBARYt9sLTOr0dSAgURNQT1D2FMEg9CwHw3sTBwhFqZEw2xqNHwIXY20vCGubvRwSyjHQY7irf4QR6Ib5zGSUViZrjiIlYL-ONXCiCDt0jX1hZ7v4abI7RnHlwZ-6GuC4SEFhzy3rc4F9gsvrRC8cCcNA1A4sVsYRtWjAZbEM43It2QE-najTOdctB-LuLTZb_gXkt8YluyPCEmumFlbzkh9N31IGjiH12GW3fRHIscmMh-kaTUHQ0Sgp83kUnKUq2Ch01APw67bWez__dMXqjQkZOMRbxtCfInT9Z5HKkYrnkPSBu324QaiLVw.jpg" alt="photo" loading="lazy"/></div>
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
